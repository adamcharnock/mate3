# Generally useful information

Reading this will help you understand this libary and how to interact with your Mate.

### Modbus

Hopefully, you don't need to worry about Modbus at all - this library should abstract that away for you. The key thing to note is that Modbus is a communication protocol, and this library works by interacting with the Mate3 physical devices using synchronous messages. So:

- The information isn't 'live' - it's only the latest state since we last read the values. When you create a client, it reads everything from all of your devices once, but then you should be calling `read` or `write` on a field as required.
- Don't over-communicate! If you start doing too many `read`s or `write`s you might brick the Modbus interface of your Mate (requiring a reboot to fix). As a rule of thumb, you probably don't want to be doing a full read more frequently than once per second (and even then, preferably only specific fields, and not the whole lot). Since it's a communication protocol (and it's not actually clear what the latency is inherent in the Mate), there's not much point reading faster that this anyway.
- Given the above, you might want to use the caching options in the `Mate3Client`, which can allow you to completely avoid interacting with/bricking your Mate while you're developing code etc. It's really tedious having to restart it every time your have a bug in your code.
- Weird things happen when encoding stuff into Modbus. Hopefully you'll never notice this, but if you see things where your `-1` is appearing as `65535` then yeh, that may be it.

### SunSpec & Outback & Modbus

You can check out the details of how Outback implements Modbus in [./mate3/sunspec/doc](./mate3/sunspec/doc), but the key things to note are:

- SunSpec is a generic Modbus implementation for distributed energy systems include e.g. solar. There's a bunch of existing definitions for what e.g. charge controllers, inverters, etc. should be.
- Outback use these, but they also have their own additional information they include - which they refer to as 'configuration' definitions (generally as that's where the writeable fields live i.e. things you can change). Generally, when you're using this library you might see e.g. `charge_controller.config.absorb_volts`. Here the `charge_controller` is the SunSpec ChargeController block, and we add on a special `config` field which is actually a pointer to the Outback configuration block. This is to try to abstract away the implementation details so you don't have to worry about their being multiple charge controller things, etc.

### Pseudo-glossary

For now, take the below as a rough glossary:

  - `Field` - this is a definition of a field e.g. `absorb_volts` is `Uint16` with units of `"Volts"` etc. It includes nice APIs for doing things like `read` and `write` and getting additional info about a field's value.
  - `Model` - This is generally referring to a specific Modbus 'block' - which is really just a collection of fields that are generally aligned to a specific device e.g. an inverter model will have an output KWH field, which a charge controller model won't.
  - `Device` - this is meant to represent a physical device and is basically our way of adding the 'config' model (e.g. `ChargeControllerConfigurationModel`) with the 'main' model (e.g. `ChargeControllerModel`) via a `.config` attribute.