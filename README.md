# TODO

- check for TODOs
- rename "values" to "data"?
- add caveats on write:
  - never change the port mappings on devices! TODO: add a safety check to check the device IDs (mac addresses?) are the same before we update a dirty value? this will ensure any port swapping doesn't mess with things.
  - if you have two inverters, do a read, then write, the device-port reference will be wrong so you'll write to the wrong device.
- general code tidyups
- nicer debug logging etc.
- tests:
  - indivudal fields etc.
- update toml, new version, etc.
- update readme
- update mate3_pg and mate3_write
- add a 'save cache' to mate3 command so this can be shared.
- add a `name` attr to each device.
- add command to cli to just list connected devices & their ports.
- all loguru
- allow reading only a single field *from a single device* (i.e. a specific port if there are multiple). We'd still need to read all devices of this type to get the port, but we could bail after that if it's not the port we want.
- caveats: should be ok if you add/remove devices in most cases. but if e.g. you do a read, then swithc the ports of your two inverters, and then do a read again, you may have fun. Actually, likewise with writing values - if you read, then change ports, and write, it may go to the wrong address.

# Outback Mate 3s Python library & command line interface

[![PyPI version](https://badge.fury.io/py/mate3.svg)](https://badge.fury.io/py/mate3)

This library provides complete support for all Outback devices (at least in theory, 
I don't own all the devices so cannot test it). Writing data is also supported.

This data is accessed though the Outback Mate3s' Modbus interface. You must therefore 
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
from mate3.definitions import ChargeControllerParser, ChargeControllerConfigurationParser
from mate3.base_structures import Device

# IP address of your Mate3s
host = '192.168.0.123'
# The Modbus port on the Mate3s. The default (502) will be 
# fine unless you have configured your Mate3s differently
port = 502

# Connect to the Mate3s
with mate3_connection(host, port) as client:
    # Get all blocks of fields from the Mate3s 
    # and print each one out.
    all_blocks = client.all_blocks()
    for block in all_blocks:
        print(block)
    
    # Get all values for a specific device
    values = client.get_device_blocks(Device.charge_controller)
    print(list(values))

    # Or get specific fields
    values = client.get_values(
        ChargeControllerParser.battery_current, 
        ChargeControllerParser.battery_voltage
    )
    # Prints a list of currents, one for each of your charge controllers
    print(values[ChargeControllerParser.battery_current]) 
    # Prints a list of voltages, one for each of your charge controllers
    print(values[ChargeControllerParser.battery_voltage])

    # Writing data
    # (BE CAREFUL! YOU COULD EASILY DAMAGE YOUR EQUIPMENT WITH THIS FEATURE!)
    client.set_value(
        field=ChargeControllerConfigurationParser.absorb_volts,
        value=330,
        port=3
    )

```

## Using the command line interface (CLI)

### Reading data

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

### Writing data

You can also set values on the mate3s using the `mate3_write` command.

**WARNING:** Please make sure you read [the license](https://github.com/adamcharnock/mate3/blob/master/LICENSE) 
before using this feature. You could easily damage your equipment by setting 
incorrect values. Don't come crying to me if you destroy your batteries, 
or if this library takes it upon itself to do so.

Warnings aside, here is how you use it:

```
# Show the available writable fields
$ mate3_write -H 192.168.0.123 --list-fields

# Start your backup generator! 
# (if that is what your inverter's auxiliary output is connected to)
$ mate3_write -H 192.168.0.123 --set radian_inverter_configuration.aux_control=2

# Turn it off again
$ mate3_write -H 192.168.0.123 --set radian_inverter_configuration.aux_control=0
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

* Web interface?

## Release process

```
# Check everything has been comitted
git diff

# Update setup.py et al
dephell deps convert

# Up the version
poetry version {major|minor|bug}

# Review the resulting changes
git diff

# Build
poetry publish --build

# Docker: build & push
docker build -t adamcharnock/mate3:{VERSION_HERE} .
docker push adamcharnock/mate3:{VERSION_HERE}

# Commit
git ci  -m "Version bump"
git push
git push --tags
```

## Credits

This is a heavily refactored version of 
[basrijn's Outback_Mate3 library](https://github.com/basrijn/Outback_Mate3).
Thank you basrijn!
