<p align="center">
    <img src="https://i.ibb.co/VDNZpvZ/logo-transparent.png" width="450">
</p>
<p align="center" style="font-size:200px;">
    Migrate data from SQL to NoSQL easily
</p>
<div align="center" style="display:inline;">
<img src="https://img.shields.io/badge/python-%203.6%20|%203.7%20|%203.8%20|%203.9%20-blue" />
<img src="https://img.shields.io/badge/black-v21.6b0-blue" />
<img src="https://img.shields.io/github/downloads/facundopadilla/sql2nosql/total?style=plastic" />
<img src="https://img.shields.io/pypi/v/sql2nosql" />
</div>


## Installation 💯
```python
pip install sql2nosql --upgrade
```

## Dependencies 📢

For the package to work, it first needs "clients", which are other packages that are in charge of managing the data in the database. Most of them work very similar, as in the case of 'mysql-connector' and 'pymysql' for MySQL databases, and 'PyMongo' for MongoDB databases.

For example, the parameter 'sql_client' of the Migrator() class, receives by parameter a string where it is indicated which is the "client" to use, for example:
```python
from sql2nosql import Migrator

Migrator(sql_client="mysql.connector")
```
For this case, you will need to manually install 'mysql.connector', as it is not a 'native package' of Python, therefore, the installation you need to do is as follows: `pip install mysql-connector-python`

In case you want to use 'pymysql', then first install it: `pip install pymysql`
And then pass it as a parameter in the form of a string:

```python
from sql2nosql import Migrator

Migrator(sql_client="pymysql")
```

SQL2NoSQL takes care of the rest.

| Engine  | Supported  | Client / Dependence|
| :------------: | :------------: | :------------: |
| MySQL/MariaDB  | ✅  |mysql.connector, pymysql|
| PostgreSQL  | ✅   |psycopg2|
| MongoDB  | ✅ |  PyMongo |
| Other DB  |  👷  | in progress...|

### ⚠️ Attention:

It is not yet implemented with SQLite3 and SQLServer, but will be tested with those databases soon. For the moment, it works with MySQL, MariaDB and PostgreSQL.

## How to use 🤓
#### Basic usage
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
## Full examples with another dependencies 👽

| Examples | Link  |
| :------------: | :------------: |
| MySQL & MongoDB  | [Click me!](https://github.com/facundopadilla/sql2nosql-example "Click me!")  |
| PostgreSQL & MongoDB  | [Click me!](https://github.com/facundopadilla/sql2nosql-postgresql-mongodb "Click me!")  |


If you want to see a more complete example of how to use this package, visit this repository: [Click me!](https://github.com/facundopadilla/sql2nosql-example "Click me!")



https://user-images.githubusercontent.com/64610246/123431691-eeeda480-d59f-11eb-8dbc-0865cace8a39.mp4




