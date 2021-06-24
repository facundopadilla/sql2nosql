# SQL2NoSQL 

![](https://i.ibb.co/yP64MvT/logo-small.png)
####  Migrate data from SQL to NoSQL easily
![](https://img.shields.io/badge/python-%203.6%20|%203.7%20|%203.8%20|%203.9%20-blue)
![](https://img.shields.io/badge/black-v21.6b0-blue)
![](https://img.shields.io/github/downloads/facundopadilla/sql2nosql/total?style=plastic)

## Installation

## How to use
####Basic usage
You indicate the SQL and NoSQL database connection data in a dictionary, and the "client"/"engine" you normally use for this conversion (I recommend PyMongo for MongoDB).
```python
from sql2nosql import Migrator

host = "0.0.0.0"

sql_config = {
    "host": host,
    "port": 33060,
    "username": "root",
    "password": "1234",
    "database": "classicmodels",
}

nosql_config = {
    "host": host,
    "port": 27018,
    "username": "sql2nosql",
    "password": "1234",
}

migrator = Migrator(
    sql_config=sql_config,
    nosql_config=nosql_config,
    sql_client="mysql.connector",
    nosql_client="pymongo",
)

migrator.migrate_data(tables=["customers", "employees", "offices"])

```
