#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import json

from loguru import logger
from pymodbus.constants import Defaults

from mate3.api import Mate3Client
from mate3.sunspec.fields import Mode


def main():
    import sys

    logger.remove()
    logger.add(sys.stderr, level="INFO")
    parser = argparse.ArgumentParser(description="Read all available data from the Mate3 controller")

    parser.add_argument(
        "--host", "-H", dest="host", default=None, required=False, help="The host name or IP address of the Mate3",
    )
    parser.add_argument(
        "--port",
        "-p",
        dest="port",
        type=int,
        default=None,
        required=False,
        help="The port number address of the Mate3",
    )
    parser.add_argument(
        "--cache-path",
        "-c",
        dest="cache_path",
        default=None,
        required=False,
        help="Path to a cache to use instead of host/port.",
    )
    parser.add_argument(
        "--format",
        "-f",
        dest="format",
        default="text",
        required=False,
        help="Output format",
        choices=("text", "prettyjson", "json"),
    )

    args = parser.parse_args()
    if args.cache_path is not None:
        if args.host is not None or args.port is not None:
            raise RuntimeError("If using --cache-path, you can't specify a host/port")
    else:
        if args.host is None:
            raise RuntimeError("If not using --cache-path, you must specify a host")
    port = Defaults.Port if args.port is None else args.port
    with Mate3Client(host=args.host, port=port, cache_path=args.cache_path, cache_only=True) as client:
        client.read()
        if args.format == "text":
            for device in client.devices.connected_devices:
                # name:
                name = device.__class__.__name__
                if hasattr(device, "port"):
                    name = f"{name} on port {device.port_number.value}"
                print(name)
                # values:
                print("\t" + " | ".join(["name".ljust(50), "impl", "sf", "unscaled", "value".ljust(20)]))
                print("\t" + " | ".join(["-" * 50, "----", "--", "--------", "-" * 20]))
                for value in device.fields([Mode.R, Mode.RW]):
                    ss = [f"\t{value.field.name.ljust(50)}"]
                    ss.append("Y".rjust(4) if value.implemented else "N".rjust(4))
                    if value.scale_factor is not None:
                        ss.append(f"{value.scale_factor}".rjust(2))
                        ss.append(f"{value.raw_value}".rjust(8))
                    else:
                        ss.append(" -")
                        ss.append(" " * 7 + "-")
                    ss.append(f"{repr(value.value)}".ljust(20) if value.implemented else "-".ljust(20))
                    print(" | ".join(ss))
                print()

        elif args.format in ("json", "prettyjson"):
            devices = []
            for device in client.devices.connected_devices:
                # name:
                name = device.__class__.__name__
                # values:
                values = {}
                for value in device.fields([Mode.R, Mode.RW]):
                    values[value.field.name] = {
                        "implemented": value.implemented,
                        "scale_factor": value.scale_factor,
                        "raw_value": value.raw_value
                        if value.raw_value is None or isinstance(value.raw_value, (str, int, float))
                        else repr(value.raw_value),
                        "value": value.value
                        if value.value is None or isinstance(value.value, (str, int, float))
                        else repr(value.value),
                    }
                devices.append({"name": name, "address": device._address, "values": values})
            indent = None if args.format == "json" else 4
            print(json.dumps(devices, indent=indent))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
