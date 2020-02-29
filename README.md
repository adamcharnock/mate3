# Outback Mate 3s Python Library

This library provides complete support for all outback devices (at least in theory, 
I don't own all the devices so cannot test it).

This data is accessed though the Mate3s' Modbus interface. You must therefore 
have a Mate3s which is connected to your local network using its ethernet port.

Tested on Python 3.7. May work on 3.6.

## Installation

The recommended installation is as follows:

```
pip install mate3
```

After this you should be able to run the `mate3` command.

---

If you wish to edit the mate3 source (contributions are gladly received!), 
then you can get the project directly from GitHub:

```
# Install poetry if you don't have it already (if you're unsure, you don't have it)
pip install poetry

# Get the source
git clone https://github.com/adamcharnock/mate3.git
cd mate3

# Install mate3 and its dependencies. This also makes the mate3 command available.
poetry install
```

After this you should be able to run the `mate3` command and edit the 
project's source code.

## Enabling the Modbus interface on your Mate 3

TBA. System -> opticsre -> Modbus?

## Using the library

Example use:

```python
from mate3 import mate3_connection
import time

# IP address of your Mate3s
host = '192.168.0.123'
# The Modbus port on the Mate3s. The default (502) will be 
# fine unless you have configured your Mate3s differently
port = 502

# Connect to the Mate3s
with mate3_connection(host, port) as client:
    # Loop forever
    while True:
        # Get all blocks of fields from the Mate3s 
        # and print each one out.
        for block in client.all_blocks():
            print(block)

        time.sleep(3)
```

## Using the command line interface (CLI)

A simple CLI is available which will read all available values from the Mate3:

```
$ mate3 -h
usage: mate3 [-h] [--host HOST] [--port PORT]
             [--format {text,prettyjson,json}]

Read all available data from the Mate3 controller

optional arguments:
  -h, --help            show this help message and exit
  --host HOST, -H HOST  The host name or IP address of the Mate3
  --port PORT, -p PORT  The port number address of the Mate3
  --format {text,prettyjson,json}, -f {text,prettyjson,json}
                        Output format
```

Example use:

```
$ mate3 --host 192.168.0.123
```

## Using `mate3_pg` to write data to Postgres

The `mate3_pg` command reads data from your Mate3 and writes it to a Postgres database.

In addition to a Mate3s connected to your network, you will need:

* A running Postgres database
* A definitions YAML file. ([example](https://github.com/adamcharnock/mate3/blob/master/pg_config.yaml))

Example use:

```
$ mate3_pg \
    -H 192.168.0.123 \ 
    --definitions /path/to/my/definitions.yaml \
    --database-url postgres://username:password@host:5432/database_name \
    --debug
```

You will need to replace `192.168.0.123` with your Mate3s' IP. Replace `/path/to/my/pg_config.yaml` with 
a path to your definitions file (see [example](https://github.com/adamcharnock/mate3/blob/master/pg_config.yaml)).
Replace the `username`, `password`, `host`, and `database_name` values with those for your Postgres database.

Full details of the `mate3_pg` command:

```
$ mate3_pg --help
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

## Various notes

The `structures.py` and `parsers.py` files are *auto generated* 
from the CSV files located in `registry_data/`. The CSV files are 
generated though text extraction from the 
[axs_app_note.pdf](http://www.outbackpower.com/downloads/documents/appnotes/axs_app_note.pdf) 
PDF provided by OutBack. This process is handled by two python files:

* `csv_generator.py` – Extract the CSV data from the PDF
* `code_generator.py` – Generate the Python code from the CSV data

## Future work

* Support the writing of values back to the Mate3
* Web interface?

## Release process

```
# Check everything has been comitted
git diff
# Up the version
dephell deps convert
# Review the resulting changes
git diff
# Commit
git ci  -m "Version bump"
git push
git push --tags
```

## Credits

This is a heavily refactored version of 
[basrijn's Outback_Mate3 library](https://github.com/basrijn/Outback_Mate3).
Thank you basrijn!
