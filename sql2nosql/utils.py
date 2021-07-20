from importlib import import_module
from typing import Any

# Helpers
clients = {
    "pymysql": "connect",
    "mysql.connector": "connect",
    "psycopg2": "connect",
    "pymongo": "MongoClient",
}

cursors = {
    "pymysql": ["pymysql.cursors", "DictCursor"],
    "psycopg2": ["psycopg2.extras", "RealDictCursor"],
}


def get_connector(client: str) -> Any:
    """
    This function returns a client from a database according to package

    Args:
        client (str): the package to use, e.g.: mysql.connector

    Raises:
        NotImplementedError: in the absence of a customer
        ModuleNotFoundError: the package is not installed
        TypeError: The argument is empty or the type is incorrect

    Returns: A client of the package that is passed by parameter
    """
    if isinstance(client, str) and client:
        try:
            if client in clients:
                return getattr(import_module(client), clients[client])
            raise NotImplementedError
        except ModuleNotFoundError:
            print(f"The {client} client is not installed in the Python packages.")
            raise
    raise TypeError(
        "The argument 'client' must be of type 'string' and must not be empty."
    )


def get_cursor(client: str) -> Any:
    """
    This function return a client with cursor according to package

    Args:
        client (str): the package to use, e.g.: mysql.connector

    Raises:
        NotImplementedError: in the absence of a customer
        TypeError: The argument is empty or the type is incorrect

    Returns:
        Any: A client with cursor
    """
    if isinstance(client, str) and client:
        if client in cursors:
            return getattr(import_module(cursors[client][0]), cursors[client][1])
        else:
            raise NotImplementedError
    raise TypeError(
        "The argument 'client' must be of type 'string' and must not be empty."
    )
