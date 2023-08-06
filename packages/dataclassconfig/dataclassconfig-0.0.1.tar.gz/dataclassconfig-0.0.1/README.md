# dataclassconfig

## Installation

```
pip install dataclassconfig
```

## Usage
Describe the structure of your config file like a `dataclass` and inherit it from `Сonfig`

For example:

```python
from dataclassconfig import Config

class Socket(Config):
    host: str
    port: int

class DatabaseConnection(Socket):
    database: str
    username: str
    password: str

class ServerConfig(Config):
    root: str
    db: DatabaseConnection
```

Create a configuration file according to the described structure in YML or JSON format

For example:

```yaml
# server-config.yml
root: ~/server
db:
  host: localhost
  port: 1234
  database: database
  username: demouser
  password: demopassword
```

```json
# server-config.json
{
    "root": "~/server",
    "db": {
        "host": "localhost",
        "port": 1234,
        "database": "database",
        "username": "demouser",
        "password": "demopassword",
    },
}
```

Load the config file using your class.

```python
config = ServerConfig.load("server-config.yml")
```

or

```python
config = ServerConfig.load("server-config.json")
```

The `load` method will check the completeness of the provided data in the configuration file and strictly match the data types. The result will be the same in both cases, the config object contains fields defined in the class

```bash
config :- ServerConfig(
    root='~/server',
    db=DatabaseConnection(
        host='localhost',
        port=1234,
        database='database',
        username='demouser',
        password='demopassword'
    )
)

config.db.username :- 'demouser'
```
