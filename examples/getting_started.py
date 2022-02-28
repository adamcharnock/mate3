from pathlib import Path

from loguru import logger
from mate3.api import Mate3Client

CACHE_PATH = Path(__file__).parent.parent / "mate3" / "tests" / "known_systems" / "chinezbrun" / "modbus.json"

if __name__ == "__main__":
    import sys
    import time

    logger.remove()
    logger.add(sys.stderr, level="INFO")

    # Creating a client allows you to interface with the Mate. It also does a read of all devices connected to it (via
    # the hub) on initialisation. The following works on a cached file so you can see how things work without actually
    # accessing/affecting a real Mate3. If you want to try it on your own system (in which case you should remove the
    # writes first!) just replace the line below with `with Mate3Client("<your mate3's IP address>") as client:`
    with Mate3Client(host=None, cache_path=CACHE_PATH, cache_only=True) as client:
        # What's the battery voltage? (For those who know about Modbus/SunSpec, it's auto-scaled to a float.)
        voltage = client.fndc.battery_voltage
        print(f"Battery voltage is {voltage.value} {voltage.units}")
        # What about when there are multiple devices (on different ports)?
        inverters = client.single_phase_radian_inverters
        for port, inverter in inverters.items():
            print(f"Output for inverter on port {port} is {inverter.output_kw.value} {inverter.output_kw.units}")
        # Values aren't 'live' - they're only updated whenever you initialise the client, or re-read a particular value.
        # Here's how we re-read the battery voltage. Note the change in the read time
        print(f"Time battery voltage was read: {voltage.read_time:%H:%M:%S.%f}")
        time.sleep(0.1)
        voltage.read()
        print(f"Time battery voltage was read (after second read): {voltage.read_time:%H:%M:%S.%f}")
        # We can write new values to the device too. Note that we don't need to worry about scaling etc.
        mate = client.mate3
        mate.system_name.write(b"New system name")
        # All the fields and options are well defined so e.g. for enums you can see valid options e.g:
        print(list(mate.ags_generator_type.enum))
        # In this case these are normal python Enums, so you can access them as expected, and assign them:
        mate.ags_generator_type.write(mate.ags_generator_type.enum["DC Gen"])
