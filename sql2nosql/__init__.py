import simplejson as json

from .errors import NoDBClients
from .utils import get_connector, get_cursor

from typing import Dict, Any, Optional, List, Union
from tqdm import tqdm

from copy import deepcopy


class Migrator(object):
    """
    Args:
        object ([type]): refers to a parent class

    Raises:
        NoDBClients: when there are no clients
        TypeError: when wrong arguments are passed on

    Returns: Nothing is returned, a progress bar is displayed on the terminal or console.
    """

    sql_client: str = None
    nosql_client: str = None
    __sql_client: Any = None
    __nosql_client: Any = None
    config: Dict[str, Dict[str, Union[str, int]]] = {}
    old_config: Dict[str, Dict[str, Union[str, int]]] = {}

    def __init__(
        self,
        sql_config: Dict[str, Union[str, int]],
        sql_client: str,
        nosql_config: Dict[str, Union[str, int]],
        nosql_client: str,
    ):
        self.sql_client = sql_client
        self.nosql_client = nosql_client
        self.old_config["sql"] = deepcopy(sql_config) if isinstance(sql_config, dict) else None
        self.config["sql"] = self.__check_config(sql_client, sql_config)
        self.config["nosql"] = nosql_config if isinstance(nosql_config, dict) else None
        self.__sql_client = (
            get_connector(sql_client)(**self.config["sql"]) if sql_config else None
        )
        self.__nosql_client = (
            get_connector(nosql_client)(**nosql_config) if nosql_config else None
        )

    def __check_config(self, client: str, config: Dict[str, Union[str, int]]) -> dict:
        if client == "pymysql":
            if "username" in config.keys():
                config["user"] = config.pop("username")
        elif client == "psycopg2":
            if "database" in config.keys():
                config["dbname"] = config.pop("database")
            if "username" in config.keys():
                config["user"] = config.pop("username")
        return config

    def __get_cursor(self):
        if self.sql_client == "mysql.connector":
            return self.__sql_client.cursor(dictionary=True)
        else:
            cursor = get_cursor(self.sql_client)
            if self.sql_client == "psycopg2":
                return self.__sql_client.cursor(cursor_factory=cursor)
            return self.__sql_client.cursor(cursor)
    
    def __update_table(self, table: str) -> str:
        updated_table = table.replace("'", "").replace('"', '')
        return updated_table

    def migrate_data(self, tables: List[str], query: Optional[str] = None) -> None:
        if isinstance(tables, list) and len(tables):
            if self.__sql_client and self.__nosql_client:
                db_nosql = self.__nosql_client[self.old_config["sql"]["database"]]
                cursor = self.__get_cursor()
                for table in tqdm(tables):
                    upd_table = self.__update_table(table)
                    mongo_collection = db_nosql[upd_table]
                    if query:
                        cursor.execute(query)
                    else:
                        cursor.execute(f"SELECT * FROM {table}")

                    data = json.loads(json.dumps(cursor.fetchall()))
                    mongo_collection.insert_many(data)
                cursor.close()
                self.__sql_client.close()
                self.__nosql_client.close()
            else:
                raise NoDBClients
        else:
            raise TypeError("The argument 'tables' is expecting a list of table names.")
