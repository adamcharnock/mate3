# Outback Mate 3 & 3s Python library & command line interface

[![PyPI version](https://badge.fury.io/py/mate3.svg)](https://badge.fury.io/py/mate3)

This Python library aims to provide complete support for all Outback devices connected to a Mate3/Mate3s (or AXS port?) via Modbus. You can:

- Read values in Python - and then do whatever you want with them e.g. monitoring/alerting/dynamic power management etc.
- Write values - i.e. control your Outback system with Python.
- (Hopefully) avoid ever having to know about Modbus at all. Just use the Python API or the CLI.
- (Hopefully) get access to the full Outback spec in a 'user friendly' form. You don't need to know about the magic numbers in Enums or Bitfields (or the SunSpec), or how to interpret fault codes, and nor do you have to worry about twos-complements and other such things.
- Co-develop without giving access to your system. That is, you can 'dump' a snapshot of your system and others can then interact with it (within reason) as if it were a real Mate3 over Modbus - which is great for testing/debugging/etc.

Tested on Python 3.7. May work on 3.6.

## Installation

The recommended installation is as follows:

```sh
pip install mate3
```

After this you should be able to run the `mate3` command. To access your Mate it must be connected to your local network using its ethernet port.

## Quickstart

Here's how you'd update a value and then read the battery voltage every second in Python:

```python
with Mate3Client(host="<your mate3 IP address>") as client:
    # Rename the system 'cos why not?
    mate.system_name.write(b"New system name")
    # Now monitor the battery voltage:
    voltage = client.fndc.battery_voltage
    while True:
        print(f"Battery voltage is {voltage.value} {voltage.units}")
        if voltage < 48:
            # Panic stations!
            # ...
```

You can also use the CLI, which has four main sub-commands:

- `read` - reads all of the values from the Mate3 and prints to stdout in a variety of formats.
- `write` - writes values to the Mate3. (If you're doing anything serious you should use the python API.)
- `devices` - shows the connected devices.
- `dump` - dumps all of the raw modbus values to a (JSON) file in a format compatible with `CachingModbusClient` which you can then share with others to help in debugging any problems you may have. 

For each you can access the help (i.e. `mate3 <cmd> -h`) for more information.

## More documentation?

At this stage, it's not really complete, but there are a few avenues:

- [./doc/general.md](./doc/general.md) has a dicussion about modbus/SunSpec/etc. and some other potentially useful things.
- The best documentation is the code and [the examples](./examples), especially [./examples/getting_started.py](./examples/getting_started.py). However this only works well for those who know Python.
- Turn intellisense on! There's a bunch of typing in this library, so it'll make your life much easier e.g. for finding all the fields accessible from your charge controller, etc.
- [./mate3/sunspec/models.py](./mate3/sunspec/models.py) has all of the key definitions for every model, including all the fields (each of which has name/units/description/etc.). Error flags and enums are properly defined there too.
- [./mate3/sunspec/doc](./mate3/sunspec/doc) has more detailed vendor information about modbus/SunSpec/OutBack details, though this is unlikely to be useful to you unless you're developing the library.

## Warnings

First, the big one:

> **WARNING!** Please make sure you read [the license](https://github.com/adamcharnock/mate3/blob/master/LICENSE) before using any of the `write` functionality. You could easily damage your equipment by setting incorrect values (directly or indirectly).

In addition, there are other edges cases that may cause problems, mostly related to if a device is re-assigned a new port. For example, you have two inverters, read some values, then switch their ports over in the Hub before writing some values - which may now go to the 'wrong' one. For now, it's safest not to do that, unless you restart the `Mate3Client` each time. On that note, the recommended approach if you need to poll over time is to recreate the `Mate3Client` on every poll (as opposed to re-using one), as that'll help avoid these (or other) issues. There are exceptions to this rule, but you should know why you're breaking it before you do so.

## Troubleshooting

See [./doc/troubleshooting.md](./doc/troubleshooting.md).

## Writing data to Postgres

See [./examples/postgres_monitor/README.md](./examples/posgres_monitor/README.md)

## Contributing

See [./CONTRIBUTING.md](./CONTRIBUTING.md)

## Credits

This was originally a heavily refactored version of
[basrijn's Outback_Mate3 library](https://github.com/basrijn/Outback_Mate3), though has largely been completely rewritten since. Thanks anyway basrijn!
