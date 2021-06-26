from typing import Any


def get_connector(client: str) -> Any:
    """
    This function returns a client from a database according to package

    Args:
        client (str): the package to use, e.g.: mysql.connector

    Raises:
        NotImplementedError: in the absence of a customer
        ModuleNotFoundError: the package is not installed
        TypeError: [description]

    Returns: A client of the package that is passed by parameter
    """
    if isinstance(client, str) and client:
        try:
            if client == "pymysql":
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
            print(f"The {client} client is not installed in the Python packages.")
            raise
    raise TypeError(
        "The argument 'client' must be of type 'string' and must not be empty."
    )
