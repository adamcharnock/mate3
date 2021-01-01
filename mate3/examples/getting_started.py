from pathlib import Path

from loguru import logger
from mate3.api import Mate3Client

CACHE_PATH = Path(__file__).parent.parent / "tests" / "known_systems" / "chinezbrun" / "modbus.json"

if __name__ == "__main__":
    import sys
    import time

    logger.remove()
    logger.add(sys.stderr, level="INFO")

    # Creating a client allows you to interface with the Mate. It also does a read of all devices connected to it (via the
    # hub) on initialisation. The following works on a cached file so you can see how things work without actually
    # accessing/affecting a real Mate3. If you want to try it on your own system (in which case you should remove the
    # writes first!) just replace the line below with `with Mate3Client("<your mate3's IP address>") as client:`
    with Mate3Client(host=None, cache_path=CACHE_PATH, cache_only=True) as client:
        print("# What's the system name?")
        mate = client.devices.mate3
        print(mate.system_name)
        print("# Get the battery voltage. Note that it's auto-scaled appropriately.")
        fndc = client.devices.fndc
        print(fndc.battery_voltage)
        print("# Get the (raw) values for the same device type on different ports.")
        inverters = client.devices.single_phase_radian_inverters
        for port, inverter in inverters.items():
            print(f"Output KW for inverter on port {port} is {inverter.output_kw.value}")
        print(
            (
                "# Values aren't 'live' - they're only updated whenever you initialise the client, call"
                " client.update_all() or re-read a particular value. Here's how we re-read the battery voltage. Note"
                " the change in the last_read field"
            )
        )
        time.sleep(0.1)
        fndc.battery_voltage.read()
        print(fndc.battery_voltage)
        print("# Nice. Modbus fields that aren't implemented are easy to identify:")
        print("Implemented?", mate.alarm_email_enable.implemented)
        print("# We can write new values to the device too. Note that we don't need to worry about scaling etc.")
        mate.system_name.write("New system name")
        print("After write: ", mate.system_name)
        print("# All the fields and options are well defined so e.g. for enums you can see valid options e.g:")
        print(list(mate.ags_generator_type.field.options))
        print("# In this case these are normal python Enums, so you can access them as expected, and assign them:")
        mate.ags_generator_type.write(mate.ags_generator_type.field.options["DC Gen"])
        print(mate.ags_generator_type.value)
