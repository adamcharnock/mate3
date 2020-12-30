# Outback Mate 3 & 3s Python library & command line interface

[![PyPI version](https://badge.fury.io/py/mate3.svg)](https://badge.fury.io/py/mate3)

This library provides complete support for all Outback devices (at least in theory, 
I don't own all the devices so cannot test it). Writing data is also supported.

This data is accessed though the Outback Mate3s' Modbus interface. You must therefore 
have a Mate3s which is connected to your local network using its ethernet port.

Tested on Python 3.7. May work on 3.6.

## Warnings

First, the big one:

> **WARNING!** Please make sure you read [the license](https://github.com/adamcharnock/mate3/blob/master/LICENSE) before using any of the `write` functionality. You could easily damage your equipment by setting incorrect values (directly or indirectly).

In addition, there are other edges cases that may cause problems, mostly related to if a device is re-assigned a new port. For example, you have two inverters, read some values, then switch their ports over in the Hub before writing some values - which may now go to the 'wrong' one. For now, it's safest not to do that, unless you restart the `Mate3Client` each time. On that note, the recommended approach if you need to poll over time is:

```python
while True:
    with Mate3Client(...) as client:
        client...
    sleep(1)
```

As opposed to

```python
with Mate3Client(...) as client:
    while True:
        client...
    sleep(1)
```

Why? It means you're getting point-in-time values, and don't have to worry about changes (such as ports being switched). There are exceptions, but you should know why you're doing it.

## Installation

The recommended installation is as follows:

```sh
pip install mate3
```

After this you should be able to run the `mate3` command.

## Using the library

More documentation is needed, but you can get a pretty code idea from [./examples/getting_started.py](./examples/getting_started.py), copied (somewhat) below. 

```python
with Mate3Client("192.168.1.12") as client:
        # Read all devices:
        client.read()
        
        # What's the system name?
        client.devices.mate3.system_name
        # >>> FieldValue[system_name] | Implemented | Read @ 2020-07-19 21:27:57.747231 | Value: --- | Clean
        
        # Get the battery voltage. Note that it's auto-scaled appropriately.
        client.devices.fndc.battery_voltage
        # >>> FieldValue[battery_voltage] | Implemented | Read @ 2020-07-19 21:27:57.795158 | Scale factor: -1 | Unscaled value: 544 | Value: 54.4 | Clean

        # Get the (raw) values for the same device type on different ports
        for port in client.devices.fx_inverters:
            print(f"FET temp on port {port} = {client.devices.fx_inverters[port].fet_temperature.value}")
        # >>> FET temp on port 1 = 36
        # >>> FET temp on port 2 = 35

        # Read only battery voltage again and check only it's read time was updated but not system name
        time.sleep(1)
        client.read(only=[client.devices.fndc.battery_voltage])
        client.devices.mate3.system_name
        client.devices.fndc.battery_voltage
        # >>> FieldValue[system_name] ... 2020-07-19 21:27:57 ...
        # >>> FieldValue[battery_voltage] ... 2020-07-19 21:27:58 ...
        
        # Nice. What about modbus fields that aren't implemented?
        client.devices.mate3.sched_1_ac_mode.implemented
        # >>> False

        # Cool. Can we set a new value? Note that we don't need to worry about scaling etc.
        volts = client.devices.charge_controller.config.absorb_volts
        # >>> ... | Scale factor: -1 | Unscaled value: 535 | Value: 53.5 | Clean
        client.devices.chjarge_controller.config.absorb_volts.value = volts.value + 0.1
        # >>> ... | Scale factor: -1 | Unscaled value: 535 | Value: 53.5 | Dirty (value to write: 536)
        
        # OK, but what about fun fields like Enums? It's doable, though a bit gross ...
        new_value = client.devices.charge_controller.config.grid_tie_mode.field.options["Grid Tie Mode disabled"]
        client.devices.charge_controller.config.grid_tie_mode.value = new_value


        # Finally, write any values that have changed to the device itself - BE CAREFUL!
        client.write()
```


## Using the command line interface (CLI)

A simple CLI is available, with four main sub-commands:

- `read` - reads all of the values from the Mate3 and prints to stdout in a variety of formats.
- `write` - writes values to the Mate3. (If you're doing anything serious you should use the python API.)
- `devices` - shows the connected devices.
- `dump` - dumps all of the raw modbus values to a (JSON) file in a format compatible with `CachingModbusClient` which you can then share with others to help in debugging any problems you may have. 

For each you can access the help (i.e. `mate3 <cmd> -h`) for more information.

## Writing data to Postgres

> NB: this used to be in `mate3_pg` command, but has been moved to `./examples/postgres_monitor.py`.

The `postgress_monitor.py` command reads data from your Mate3 and writes it to a Postgres database.

In addition to a Mate3s connected to your network, you will need:

* A running Postgres database
* A definitions YAML file. ([example](https://github.com/adamcharnock/mate3/blob/master/pg_config.yaml))

Example use:

```
$ python postgres_monitor.py \
    -H 192.168.0.123 \ 
    --definitions /path/to/my/definitions.yaml \
    --database-url postgres://username:password@host:5432/database_name \
    --debug
```

You will need to replace `192.168.0.123` with your Mate3s' IP. Replace `/path/to/my/pg_config.yaml` with 
a path to your definitions file (see [example](https://github.com/adamcharnock/mate3/blob/master/pg_config.yaml)).
Replace the `username`, `password`, `host`, and `database_name` values with those for your Postgres database.

Full details of the `postgres_monitor.py` command:

```
$ python postgres_monitor.py --help
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

## Contributing

If you wish to edit the mate3 source (contributions are gladly received!), 
then you can get the project directly from GitHub:

```sh
# Install poetry if you don't have it already (if you're unsure, you don't have it)
pip install poetry

# Get the source
git clone https://github.com/adamcharnock/mate3.git
cd mate3

# Install mate3 and its dependencies. This also makes the mate3 command available.
poetry install
```

After this you should be able to run the `mate3` command and edit the project's source code.

## Release process

```sh
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

This was originally a heavily refactored version of
[basrijn's Outback_Mate3 library](https://github.com/basrijn/Outback_Mate3), though has largely been completely rewritten since. Thanks anyway basrijn!
