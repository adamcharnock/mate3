from loguru import logger

from mate3.api import Mate3Client

if __name__ == "__main__":
    import sys
    import time

    logger.remove()
    logger.add(sys.stderr, level="INFO")

    with Mate3Client("192.168.1.12") as client:
        client.read()
        print("# What's the system name?")
        print(client.devices.mate3.system_name)
        print("# Get the battery voltage. Note that it's auto-scaled appropriately.")
        print(client.devices.fndc.battery_voltage)
        print("# Get the (raw) values for the same device type on different ports")
        for port in client.devices.fx_inverters:
            print(f"FET temp on port {port} = {client.devices.fx_inverters[port].fet_temperature.value}")
        print("# Read only battery voltage again and check only it's read time was updated but not system name")
        time.sleep(1)
        client.read(only=[client.devices.fndc.battery_voltage])
        print(client.devices.mate3.system_name)
        print(client.devices.fndc.battery_voltage)
        print("# Nice. What about modbus fields that aren't implemented?")
        print(client.devices.mate3.sched_1_ac_mode.implemented)
        print("# Cool. Can we set a new value? Note that we don't need to worry about scaling etc.")
        volts = client.devices.charge_controller.config.absorb_volts
        print("Before:", volts)
        client.devices.charge_controller.config.absorb_volts.value = volts.value + 0.1
        print("After: ", volts)
        print("# OK, but what about fun fields like Enums?")
        new_value = client.devices.charge_controller.config.grid_tie_mode.field.options["Grid Tie Mode disabled"]
        client.devices.charge_controller.config.grid_tie_mode.value = new_value
        print("# Finally, write any values that have changed to the device itself - BE CAREFUL!")
        client.write()
