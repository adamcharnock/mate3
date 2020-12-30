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
        mate = client.devices.mate3
        print(mate.system_name)
        print("# Get the battery voltage. Note that it's auto-scaled appropriately.")
        fndc = client.devices.fndc
        print(fndc.battery_voltage)
        print("# Get the (raw) values for the same device type on different ports")
        inverters = client.devices.fx_inverters
        for port in inverters:
            print(f"FET temp on port {port} = {inverters[port].fet_temperature.value}")
        print("# Read only battery voltage again and check only it's read time was updated but not system name")
        time.sleep(1)
        client.read(only=[fndc.battery_voltage])
        print(mate.system_name)
        print(fndc.battery_voltage)
        print("# Nice. What about modbus fields that aren't implemented?")
        print(mate.sched_1_ac_mode.implemented)
        print("# Cool. Can we set a new value? Note that we don't need to worry about scaling etc.")
        cc = client.devices.charge_controller.config
        volts = cc.absorb_volts
        print("Before:", volts)
        cc.absorb_volts.value = volts.value + 0.1
        print("After (before writing): ", volts)
        print("# OK, but what about fun fields like Enums?")
        new_value = cc.grid_tie_mode.field.options["Grid Tie Mode disabled"]
        cc.grid_tie_mode.value = new_value
        print("# Finally, write any values that have changed to the device itself - BE CAREFUL!")
        client.write()
