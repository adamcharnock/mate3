## Writing data to Postgres

> NB: this used to be in `mate3_pg` command, but has been moved to `./examples/postgres_monitor/main.py`.

> NB: This has not been tested since v0.4.0 (at the latest).

The `./main.py` file reads data from your Mate3 and writes it to a Postgres database.

In addition to a Mate3s connected to your network, you will need:

* A running Postgres database
* A definitions YAML file. An example is at [./config.yaml](./config.yaml))

Example use:

```
$ python main.py \
    -H 192.168.0.123 \ 
    --definitions config.yaml \
    --database-url postgres://username:password@host:5432/database_name \
    --debug
```

You will need to replace `192.168.0.123` with your Mate3s' IP. Replace the `username`, `password`, `host`, and `database_name` values with those for your Postgres database.

Full details of the `main.py` command:

```
$ python main.py --help
usage: mate3_pg [-h] --host HOST [--port PORT] [--interval INTERVAL] [--database-url DATABASE_URL] --definitions DEFINITIONS [--hypertables] [--quiet] [--debug]

Read all available data from the Mate3 controller

optional arguments:
  -h, --help            show this help message and exit
  --host HOST, -H HOST  The host name or IP address of the Mate3
  --port PORT, -p PORT  The port number address of the Mate3
  --interval INTERVAL, -i INTERVAL
                        Polling interval in seconds
  --database-url DATABASE_URL
                        Postgres database URL
  --definitions DEFINITIONS
                        YAML definition file
  --hypertables         Should we create tables as hypertables? Use only if you are using TimescaleDB
  --quiet, -q           Hide status output. Only errors will be shown
  --debug               Show debug logging
```  