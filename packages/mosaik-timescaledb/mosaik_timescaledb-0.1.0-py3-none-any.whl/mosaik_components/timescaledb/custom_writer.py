import mosaik_api_v3
import psycopg2
from psycopg2.sql import Composed as SQLComposed, Identifier as SQLIdent, SQL
import json
from pgcopy import CopyManager
from mosaik_api_v3.datetime import Converter
from .writer import Writer

META = {
    "type": "time-based",
    "models": {},
}


class CustomWriter(Writer):
    """A moasik simulator that uses timescaledb to save the inputs it is given into user defined and created sql tables."""

    _attr_dict: None
    _entities: None
    _schema_name: None
    _table_name: None
    _ts_col: None
    _run_col: None
    _src_col: None
    _run_id: str

    def __init__(self):
        """Init of the class"""
        super().__init__(META)
        self._entities = []

    def init(
        self,
        sid,
        db_name,
        db_user,
        db_pass,
        time_resolution,
        start_date=None,
        step_size=900,
        db_host="localhost",
        db_port="5432",
        ssl_mode="prefer",
        schema_name="mosaik_schema",
    ):
        """mosaik specific init function, sets start date and decides if Simulator is event or time based and initiates the database connection.

        :param db_name: The database name
        :type db_name: str
        :param db_user: The name of the database user
        :type db_user: str
        :param db_pass: The database password
        :type db_pass: str
        :param sid: ID of the Simulator
        :type sid: str
        :param time_resolution: Time resolution of the Simulator
        :type time_resolution: float
        :param start_date: The start date of the simulato, defaults to None
        :type start_date: str, optional
        :param step_size: The steo size of the Simulator, defaults to 900
        :type step_size: int, optional
        :param db_host: The database host address, defaults to "localhost"
        :type db_host: str, optional
        :param db_port: The database port, defaults to "5432"
        :type db_port: str, optional
        :param ssl_mode: The ssl mode of the database, defaults to "prefer"
        :type ssl_mode: str, optional
        :return: The metadata of the simulator
        :rtype: mosaik_api_v3.types.Meta
        """
        # add table columns to attr
        self._db_user = db_user
        self._db_pass = db_pass
        self._db_host = db_host
        self._db_port = db_port
        self._db_name = db_name
        self._ssl_mode = ssl_mode
        connection = f"postgres://{self._db_user}:{self._db_pass}@{self._db_host}:{self._db_port}/{self._db_name}?sslmode={self._ssl_mode}"
        self._conn = psycopg2.connect(
            connection,
            keepalives=1,
            keepalives_idle=30,
            keepalives_interval=10,
            keepalives_count=5,
        )
        self._cur = self._conn.cursor()
        if step_size:
            self._step_size = step_size
        else:
            self.meta["type"] = "event-based"
            self._first_step = True

        if start_date:
            self._time_converter = Converter(
                start_date=start_date,
                time_resolution=time_resolution,
            )
        self._schema_name = schema_name
        get_existing_tables = (
            "SELECT table_name FROM information_schema.tables WHERE table_schema = %s;"
        )

        self._cur.execute(get_existing_tables, (self._schema_name,))
        layout = {}
        tables = self._cur.fetchall()
        for table in tables:
            get_table_columns = "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = %s;"
            self._cur.execute(get_table_columns, (table,))
            layout[table[0]] = self._cur.fetchall()
        self._attr_dict = layout
        for table in self._attr_dict.keys():
            self.meta["models"].update(
                {
                    str(table): {
                        "public": True,
                        "any_inputs": True,
                        "params": [
                            "db_name",  # the database name for the timescaldb
                            "db_user",  # the database user
                            "db_pass",  # the database password
                            "db_host",  # the database host networkaddress
                            "db_port",  # the database port
                            "ssl_mode",  # the ssl_mode, require for remote and prefer for standard use
                            "schema_name",  # name of the schema to scan
                            "postgres_mode",  # Enables postgres mode if true and does not create a hypertable
                            "drop_tables",  # Determines if the tables should be dropped or not(if they already exists) Not in use here
                            "run_id",  # The run id,
                            "src_col",  # Mapping for src_id col
                            "ts_col",  # Mapping for ts col
                            "run_col",  # Mapping for run_id col
                        ],
                        "attrs": str([col for col, _ in self._attr_dict[table]]),
                    }
                }
            )
        return self.meta

    def create(
        self,
        num,
        model,
        postgres_mode=False,
        drop_tables=False,
        run_id="run 1",
        src_col="src",
        ts_col="time",
        run_col="run_id",
        **model_params,
    ):
        """Creates the simulator by reading out model parameters and saving them in the class parameters.

        :param num: The number of entities to create
        :type num: int
        :param model: model name in the meta
        :type model: str
        :param postgres_mode: Determines if the adapter is in timescale or postgres mode, defaults to False
        :type postgres_mode: bool, optional
        :param drop_tables: Not used in this writer, defaults to False
        :type drop_tables: bool, optional
        :param drop_tables: Not used in this writer, defaults to False
        :type drop_tables: bool, optional
        :param run_id: The simulation run id. Defaults to run 1
        :type run_id: str, optional
        :param src_col: Name of the column where the src sim string will be saved. Defaults to 'src'.
        :type src_col: str, optional
        :param ts_col: Name of the column where the timestamp will be saved. Defaults to 'time'.
        :type ts_col: str, optional
        :param run_col: Name of the column where the simulation run id string will be saved. Defaults to 'run_id'.
        :type run_col: str, optional
        :return: A list with the eid and model of the simulator
        :rtype: List[mosaik_api_v3.types.CreateResults]
        """
        errmsg = (
            "The Custom writer simulator only supports one entity. Create a second "
            "instance of the simulator if you need more."
        )

        assert num == 1, errmsg
        super().create(
            num,
            model,
            postgres_mode=postgres_mode,
            drop_tables=drop_tables,
        )
        self._run_id = run_id
        self._table_name = model
        self._src_col = src_col
        self._run_col = run_col
        self._ts_col = ts_col
        return [{"eid": f"{model}-1", "type": model}]

    def step(self, time, inputs, max_advance):
        """Fills in the database for every timestep

        :param time: the timestep of the simulator
        :type time: int
        :param inputs: the inputs of the simulator
        :type inputs: mosaik_api_v3.types.InputData
        :param max_advance: The max allowed advance of the simulator
        :type max_advance: int
        :return: Returns the next timestep time
        :rtype: int
        """
        self.add_to_table(inputs, time)
        if self._step_size:
            return time + self._step_size

    def remove_chars(self, chars, string: str):
        """Replaces the given chars with '' if they exist in the string

        :param chars: Array of character to replace
        :type chars: list
        :param string: string in which to replace characters
        :type string: str
        :return: String without the characters
        :rtype: str
        """
        for c in chars:
            if c in string:
                string = string.replace(c, "")
        return string

    def add_to_table(self, inputs, time):
        """Adds input values to the tables at each timestep The layout dict need to follow the follwing schemaÖ
        layout_dict={"tb1":{"Grid-0.0-LV1.1 Bus 1": ["time", "p_mw", "n"], "PV-0.PV_0":["time", "p_mw", "P_gen"]}}

        :param inputs: Inputs to add to tables
        :type inputs: mosaik_api_v3.types.InputData
        :param time: timestep of the simulator
        :type time: int
        """
        src_dict = {}
        already_written = False
        data = inputs.get(f"{self._table_name}-1", {})
        if "local_time" in data:
            timestamp = next(iter(data["local_time"].values()))
        elif self._time_converter:
            timestamp = self._time_converter.datetime_from_step(time)
        cols = [col for col, _ in self._attr_dict[self._table_name]]
        values = []
        attrs = cols.copy()
        attrs.remove(self._ts_col)
        attrs.remove(self._run_col)
        attrs.remove(self._src_col)
        for attr in attrs:
            iter_list = []
            for col in cols:
                if col == self._ts_col:
                    iter_list.append(timestamp)
                elif col == self._run_col:
                    iter_list.append(self._run_id)
                elif col == self._src_col:
                    continue
                elif col != attr:
                    iter_list.append(None)
                else:
                    src = list(data[attr].keys())[0]
                    val = data[attr][src]
                    iter_list.append(val)
                    iter_list.insert(cols.index(self._src_col), src)
            values.append(tuple(iter_list))
        mgr = CopyManager(self._conn, f"{self._schema_name}.{self._table_name}", cols)
        mgr.copy(values)
        self._conn.commit()


if __name__ == "__main__":
    mosaik_api_v3.start_simulation(MultiWriter())
