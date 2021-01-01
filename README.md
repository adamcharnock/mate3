# Outback Mate 3 & 3s Python library & command line interface

[![PyPI version](https://badge.fury.io/py/mate3.svg)](https://badge.fury.io/py/mate3)

This library provides complete support for all Outback devices (at least in theory, I don't own all the devices so cannot test it). Writing data is also supported.

This data is accessed though the Outback Mate3s' Modbus interface. You must therefore have a Mate3/Mate3s which is connected to your local network using its ethernet port.

Tested on Python 3.7. May work on 3.6.

## Installation

The recommended installation is as follows:

```sh
pip install mate3
```

After this you should be able to run the `mate3` command.

## Background info you probably should know ...

Reading this will help you understand this libary and how to interact with your Mate.

### Modbus

Hopefully, you don't need to worry about Modbus at all - this library should abstract that away for you. The key thing to note is that Modbus is a communication protocol, and this library works by interacting with the Mate3 physical devices using synchronous messages. So:

- The information isn't 'live' - it's only the latest state since we last read the values. Generally, you should be calling `read` or `write` before/after any operation you make.
- Don't over-communicate! If you start doing too many `read`s or `write`s you might brick the Modbus interface of your Mate (requiring a reboot to fix). As a rule of thumb, you probably don't want to be reading more frequently than once per second (and even then, preferably only specific fields, and not the whole lot). Since it's a communication protocol (and it's not actually clear what the latency is inherent in the Mate), there's not much point reading faster that this anyway.
- Given the above, you might want to use the caching options in the `Mate3Client`, which can allow you to completely avoid interacting with/bricking your Mate while you're developing code etc. It's really tedious having to restart it every time your have a bug in your code.
- Weird things happen when encoding stuff into Modbus. Hopefully you'll never notice this, but if you see things where your `-1` is appearing as `65535` then yeh, that may be it.

### SunSpec & Outback & Modbus

You can check out the details of how Outback implements Modbus in [./mate3/sunspec/doc](./mate3/sunspec/doc), but the key things to note are:

- SunSpec is a generic Modbus implementation for distributed energy systems include e.g. solar. There's a bunch of existing definitions for what e.g. charge controllers, inverters, etc. should be.
- Outback use these, but they have their own additional information they include - which they refer to as 'configuration' definitions (generally as that's where the writeable fields live i.e. things you can change). Generally, when you're using this library you might see e.g. `charge_controller.config.absorb_volts`. Here the `charge_controller` is the SunSpec block, and we add on a special `config` field which is actually a pointer to the Outback configuration block. This is to try to abstract away the implementation details so you don't have to worry about their being multiple charge controller things, etc.

### Pseudo-glossary

Words are confusing. For now, take the below as a rough guide:
  - `Field` - this is a definition of a field e.g. `absorb_volts` is `Uint16` with units of `"Volts"` etc.
  - `Model` - This is generally referring to a specific Modbus 'block' - which is really just a collection of fields that are generally aligned to a specific device e.g. an inverter model will have an output KWH field, which a charge controller model won't. (Again, it's confusing here as Outback generally have two models per device.) In the case above `charge_controller` represents one (SunSpec) model, and `charge_controller.config` another (Outback) model. 
  - `Device` - this is meant to represent a physical device and is basically our way of wrapping the Outback config model with the SunSpec one.
  - `FieldValue` - this is kind of like a `Field` but with data (read from Modbus) included i.e. "the value of the field". It includes some nice things too like auto-scaling variables ('cos floats aren't a thing) and simple `read` or `write` APIs.

## More documentation?

At this stage, it doesn't exist - the best documentation is the code and [the examples](./examples), though this only works well for those who know Python. A few other quick tips:

- Turn intellisense on! There's a bunch of typing in this library, so it'll make your life much easier e.g. for finding all the fields accessible from your charge controller, etc.
- [./mate3/sunspec/models.py](./mate3/sunspec/models.py) has all of the key definitions for every model, including all the fields (each of which has name/units/description/etc.). Error flags and enums are properly defined there too.

## Using the library

More documentation is needed (see above), but you can get a pretty code idea from [./examples/getting_started.py](./examples/getting_started.py), copied (somewhat) below.

```python
# Creating a client allows you to interface with the Mate. It also does a read of all devices connected to it (via the
# hub) on initialisation:
with Mate3Client("...") as client:
        # What's the system name?
        mate = client.devices.mate3
        print(mate.system_name)
        # >>> FieldValue[system_name] | Mode.RW | Implemented | Value: OutBack Power Technologies | Read @ 2021-01-01 17:50:54.373077
        
        # Get the battery voltage. Note that it's auto-scaled appropriately.
        fndc = client.devices.fndc
        print(fndc.battery_voltage)
        # >>> FieldValue[battery_voltage] | Mode.R | Implemented | Scale factor: -1 | Unscaled value: 506 | Value: 50.6 | ...
         Read @ 2021-01-01 17:50:54.378941

        # Get the (raw) values for the same device type on different ports.
        inverters = client.devices.single_phase_radian_inverters
        for port, inverter in inverters.items():
            print(f"Output KW for inverter on port {port} is {inverter.output_kw.value}")
        # >>> Output KW for inverter on port 1 is 0.7
        # >>> Output KW for inverter on port 2 is 0.0

        # Values aren't 'live' - they're only updated whenever you initialise the client, call client.update_all() or
        # re-read a particular value. Here's how we re-read the battery voltage. Note the change in the last_read field
        time.sleep(0.1)
        fndc.battery_voltage.read()
        print(fndc.battery_voltage)
        # >>> FieldValue[battery_voltage] | Mode.R | Implemented | Scale factor: -1 | Unscaled value: 506 | Value: 50.6 | Read @ 2021-01-01 17:50:54.483401

        # Nice. Modbus fields that aren't implemented are easy to identify:
        print(mate.alarm_email_enable.implemented)
        # >>> False

        # We can write new values to the device too. Note that we don't need to worry about scaling etc.
        # WARNING: this will actually write stuff to your mate - see the warning below!
        mate.system_name.write("New system name")
        print(mate.system_name)
        # >>>  FieldValue[system_name] | Mode.RW | Implemented | Value: New system name | Read @ 2021-01-01 17:50:54.483986

        # All the fields and options are well defined so e.g. for enums you can see valid options e.g:
        print(list(mate.ags_generator_type.field.options))
        # >>> [<ags_generator_type.AC Gen: 0>, <ags_generator_type.DC Gen: 1>, <ags_generator_type.No Gen: 2>]

        # In this case these are normal python Enums, so you can access them as expected, and assign them:
        mate.ags_generator_type.write(mate.ags_generator_type.field.options["DC Gen"])
        # >>> ags_generator_type.DC Gen
```

## Using the command line interface (CLI)

A simple CLI is available, with four main sub-commands:

- `read` - reads all of the values from the Mate3 and prints to stdout in a variety of formats.
- `write` - writes values to the Mate3. (If you're doing anything serious you should use the python API.)
- `devices` - shows the connected devices.
- `dump` - dumps all of the raw modbus values to a (JSON) file in a format compatible with `CachingModbusClient` which you can then share with others to help in debugging any problems you may have. 

For each you can access the help (i.e. `mate3 <cmd> -h`) for more information.

## Warnings

First, the big one:

> **WARNING!** Please make sure you read [the license](https://github.com/adamcharnock/mate3/blob/master/LICENSE) before using any of the `write` functionality. You could easily damage your equipment by setting incorrect values (directly or indirectly).

In addition, there are other edges cases that may cause problems, mostly related to if a device is re-assigned a new port. For example, you have two inverters, read some values, then switch their ports over in the Hub before writing some values - which may now go to the 'wrong' one. For now, it's safest not to do that, unless you restart the `Mate3Client` each time. On that note, the recommended approach if you need to poll over time is to recreate the `Mate3Client` on every poll (as opposed to re-using one), as that'll help avoid these (or other) issues. There are exceptions to this rule, but you should know why you're breaking it before you do so.

## Troubleshooting

Some ideas (which can be helpful for issues)

### Set log-level to DEBUG

See `mate3 -h` for the CLI, otherwise the following (or similar) for python code:

```python
from loguru import logger
logger.remove()
logger.add(sys.stderr, level="DEBUG")
```

### List the devices

```sh
$ mate3 devices --host ...
name                                               address    port
----                                               -------    ----
Mate3                                              40069      None
ChargeController                                   40986      4
ChargeControllerConfiguration                      41014      4
...
```
Are they all there?

### Create a dump of the raw modbus values

See `mate3 dump -h`. You can send the resulting JSON file to someone to help debug. (Just note that it includes all the data about the Mate, e.g. any passwords etc.)

## Writing data to Postgres

See [./examples/postgres_monitor/README.md](./examples/posgres_monitor/README.md)

## Contributing

See [./CONTRIBUTING.md](./CONTRIBUTING.md)

## Credits

This was originally a heavily refactored version of
[basrijn's Outback_Mate3 library](https://github.com/basrijn/Outback_Mate3), though has largely been completely rewritten since. Thanks anyway basrijn!
