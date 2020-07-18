#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import json
import re
from argparse import ArgumentError
from typing import List, Tuple

from loguru import logger
from pymodbus.constants import Defaults

from mate3.api import Mate3Client
from mate3.sunspec.fields import Mode


def read(client, args):
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
            name = device.__class__.__name__
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
            devices.append({"name": name, "address": device.address, "values": values})
        indent = None if args.format == "json" else 4
        print(json.dumps(devices, indent=indent))


def write(client, args):

    # Util functions to get the field from a string such as `charge_controllers[3].config.absorb_volts`
    attr_idx_pattern = re.compile(r"([^\[\.]+)(\[[0-9]+\])?")

    def get_field(field, paths: List[Tuple[str]]):
        attr, idx = paths[0]
        field = getattr(field, attr)
        if idx:
            field = field[int(idx)]
        # Keep recursing:
        paths = paths[1:]
        if paths:
            return get_field(field, paths)
        return field

    for set_arg in args.set:
        path, value = set_arg.split("=")
        field = get_field(client.devices, attr_idx_pattern.findall(path))
        value = eval(value, globals(), locals())  # TODO: get rid of eval!
        field.value = value
    client.write()


def list_devices(client):
    print("name".ljust(50), "address".ljust(10), "port")
    print("----".ljust(50), "-------".ljust(10), "----")
    for device in client.devices.connected_devices:
        name = device.__class__.__name__.replace("DeviceValues", "").replace("Values", "")
        port = device.port_number.value if hasattr(device, "port_number") else None
        print(name.ljust(50), str(device.address).ljust(10), port)


def debug(args, port):
    if args.cache_only:
        raise RuntimeError("Can't use --cache-only for debug, as we're creating the cache, not using it!")
    if args.cache_path is None:
        raise RuntimeError("You must specify --cache-path for debug, as this is where the debug file will be written")
    if args.host is None:
        raise RuntimeError("You must specify a --host when using debug.")
    with Mate3Client(host=args.host, port=port, cache_path=args.cache_path, cache_only=False) as client:
        client.read()
        print(
            f"All debug modbus reads are cached in the file '{args.cache_path}'.\nNOTE THAT THIS MAY CONTAIN SENSITIVE "
            "INFORMATION LIKE PASSWORDS ETC."
        )


def main():
    import sys

    # base parser for shared arguments (which makes sub parsers nicer)
    base_parser = argparse.ArgumentParser(add_help=False)
    base_parser.add_argument(
        "--host", "-H", dest="host", default=None, required=False, help="The host name or IP address of the Mate3",
    )
    base_parser.add_argument(
        "--port",
        "-p",
        dest="port",
        type=int,
        default=None,
        required=False,
        help="The port number address of the Mate3",
    )
    base_parser.add_argument(
        "--cache-path",
        "-c",
        dest="cache_path",
        default=None,
        required=False,
        help="Path to a cache to use instead of host/port.",
    )
    base_parser.add_argument(
        "--cache-only",
        dest="cache_only",
        action="store_true",
        required=False,
        help="Pass this option if you only want to use the provided cache.",
    )
    base_parser.add_argument(
        "--loglevel",
        "-l",
        dest="loglevel",
        default="WARNING",
        required=False,
        help="Logging level",
        choices=("DEBUG", "INFO", "WARNING", "ERROR"),
    )

    parser = argparse.ArgumentParser(description="CLI for the Mate3 controller", parents=[base_parser])
    sub_parsers = parser.add_subparsers(dest="cmd", help="Use mate3 <cmd> -h for help")
    read_parser = sub_parsers.add_parser("read", help="Read mate3 values", parents=[base_parser])
    read_parser.add_argument(
        "--format",
        "-f",
        dest="format",
        default="text",
        required=False,
        help="Output format",
        choices=("text", "prettyjson", "json"),
    )
    write_parser = sub_parsers.add_parser("write", help="Write mate3 values", parents=[base_parser])
    write_parser.add_argument(
        "--set",
        "-s",
        dest="set",
        help=(
            "The field and value to set in the form field=value. For example: "
            "`--set charge_controllers[3].config.absorb_volts=57.6` You can add more than one --set options if you want"
            " to set many fields at once."
        ),
        action="append",
    )
    devices_parser = sub_parsers.add_parser("devices", help="List the devices", parents=[base_parser])
    debug_parser = sub_parsers.add_parser("debug", help="Dump debug info", parents=[base_parser])

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()

    # Set up logging:
    logger.remove()
    logger.add(sys.stderr, level=args.loglevel)

    # Get the client:
    if args.cache_only and args.cache_path is None:
        raise RuntimeError("You must specify --cache-path if you're using --cache-only")
    if args.cache_path is not None:
        if args.cache_only and (args.host is not None or args.port is not None):
            raise RuntimeError("If using --cache-only, you can't specify a host/port")
    else:
        if args.host is None:
            raise RuntimeError("If not using --cache-path, you must specify a host")
    port = Defaults.Port if args.port is None else args.port

    # If debug, let's do it:
    if args.cmd == "debug":
        debug(args, port)

    else:
        with Mate3Client(host=args.host, port=port, cache_path=args.cache_path, cache_only=args.cache_only) as client:
            client.read()
            if args.cmd == "read":
                read(client, args)
            elif args.cmd == "write":
                write(client, args)
            elif args.cmd == "devices":
                list_devices(client)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
