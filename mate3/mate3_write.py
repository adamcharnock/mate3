#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import json
import logging
import sys

from sys import argv

from pymodbus.constants import Defaults

from mate3.api import mate3_connection, NoDefinitionFoundForDevice

# Setup logging
from mate3.base_definitions import Mode
from mate3.base_structures import get_definition, Device

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%Y%m%d %H:%M:%S")
logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Set values on the mate3s")

    parser.add_argument(
        "--host", "-H",
        dest="host",
        help="The host name or IP address of the Mate3",
        required=True,
    )
    parser.add_argument(
        "--port", "-p",
        dest="port",
        default=Defaults.Port,
        help=f"The port number address of the Mate3. Optional, defaults to {Defaults.Port}",
    )
    parser.add_argument(
        "--set", "-s",
        dest="set",
        help=(
            "The field and value to set in the form field=value. "
            "For example: --set charge_controller_configuration.absorb_volts=330"
        ),
        action="append",
    )
    parser.add_argument(
        "--list-fields", "-l",
        dest="list_fields",
        help=(
            "List all available values for the --field parameter. Will only show fields that are writable,"
            "and devices which are available on your hub."
        ),
        action='store_true',
    )
    parser.add_argument(
        "--hub-port", "-P",
        dest="hub_port",
        type=int,
        help=(
            "The hub port to which the destination device is connected. "
            "Only required if more than one of the specified device is "
            "connected to the hub (for example, multiple charge controllers "
            "or inverters)."
        ),
    )

    args = parser.parse_args(argv[1:])

    with mate3_connection(args.host, args.port) as client:
        if args.list_fields:
            show_fields(client)
            return
        elif args.set:
            for set_arg in args.set:
                device_and_field, value = set_arg.split('=', maxsplit=1)
                device_name, field_name = device_and_field.split('.', maxsplit=1)

                try:
                    device = getattr(Device, device_name)
                except AttributeError:
                    sys.stderr.write(f"Device name {device_name} is not recognised. Perhaps you made a typo?\n")
                    exit(1)

                definition = get_definition(device)()

                try:
                    field = getattr(definition, field_name)
                except AttributeError:
                    sys.stderr.write(f"Device {device_name} has no field named {field_name}\n")
                    exit(1)

                try:
                    value = int(value.strip())
                except ValueError:
                    sys.stderr.write(f"Invalid value '{value}'. Must be an integer")

                client.set_value(field, value, port=args.hub_port)
                sys.stderr.write(f"Done\n")


def show_fields(client):
    devices = {device for device, _ in client._block_information()}
    print(f"{' Devices ':=^80}\n")
    print(f"{'DEVICE NAME':<35} HUB PORT(S)")

    display_devices = []
    for device in devices:
        try:
            definition = get_definition(device)()
        except NoDefinitionFoundForDevice:
            continue

        # Does the device have writable fields?
        has_writable_fields = False
        for field in definition.fields.values():
            if field.mode in (Mode.W, Mode.RW):
                has_writable_fields = True

        if not has_writable_fields:
            continue

        if hasattr(definition, 'port_number'):
            ports = list(client.get_values(definition.port_number).values())[0]
            ports = list(map(str, ports))
        else:
            ports = None

        display_devices.append((device, definition, ports))

    for device, _, ports in display_devices:
        print(f"{device.name:<40} {', '.join(ports) if ports else 'N/A'}")

    print(f"\n{' Fields ':=^80}\n")

    print(f"{'FIELD NAME':<68} {'HUB PORT(S)':<12}")
    for device, definition, ports in display_devices:
        for field in definition.fields.values():
            if field.mode not in (Mode.W, Mode.RW):
                continue

            formatted_ports = ', '.join(ports) if ports else 'N/A'
            field_name = f"{device.name}.{field.name}"
            print(f"{field_name:<68} {formatted_ports:<12} {field.description}")



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
