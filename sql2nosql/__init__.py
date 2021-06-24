import simplejson as json

from .errors import NoDBClients
from typing import Dict, Any, Optional, List
from tqdm import tqdm


class Migrator(object):
    """This class allows you to extract table records, pass them to a Python dictionary and finally insert them into a NoSQL collection."""

    sql_client: Any = None
    nosql_client: Any = None
    config: Dict[dict, Dict[str, Any]] = {}

    def __init__(
        self,
        sql_config: Dict[str, str],
        sql_client: str,
        nosql_config: Dict[str, str],
        nosql_client: str,
    ):
        self.config["sql"] = sql_config if isinstance(sql_config, dict) else None
        self.config["nosql"] = nosql_config if isinstance(nosql_config, dict) else None
        self.sql_client = (
            self.__get_connector(sql_client)(**sql_config) if sql_config else None
        )
        self.nosql_client = (
            self.__get_connector(nosql_client)(**nosql_config) if nosql_config else None
        )

    def __get_connector(self, client: str) -> Any:
        if isinstance(client, str) and client:
            try:
                if client == "sqlite3":
                    from sqlite3 import connect

                    return connect
                elif client == "pymysql":
                    from pymysql import connect

                    return connect
                elif client == "mysql.connector":
                    from mysql.connector import connect

                    return connect
                elif client == "pymongo":
                    from pymongo import MongoClient

                    return MongoClient
                else:
                    raise NotImplementedError
            except ModuleNotFoundError:
                raise ModuleNotFoundError(
                    f"The {client} client is not installed in the Python packages."
                )
        raise TypeError(
            "The argument 'client' must be of type 'string' and must not be empty."
        )

    def migrate_data(self, tables: List[str], query: Optional[str] = None) -> None:
        if isinstance(tables, list) and len(tables):
            if self.sql_client and self.nosql_client:
                db_nosql = self.nosql_client[self.config["sql"]["database"]]
                cursor = self.sql_client.cursor(dictionary=True)
                for table in tqdm(tables):
                    mongo_collection = db_nosql[table]
                    if query:
                        cursor.execute(query)
                    else:
                        cursor.execute(f"SELECT * FROM {table}")

                    data = json.loads(json.dumps(cursor.fetchall()))
                    mongo_collection.insert_many(data)
            else:
                raise NoDBClients
        else:
            raise TypeError("The argument 'tables' is expecting a list of table names.")
