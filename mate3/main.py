#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import json
import logging

# Setup logging
from sys import argv

from pymodbus.constants import Defaults

from mate3.api import mate3_connection
from mate3.base_structures import Device

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%Y%m%d %H:%M:%S")
logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Read all available data from the Mate3 controller")

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
        help="The port number address of the Mate3",
    )
    parser.add_argument(
        "--format", "-f",
        dest="format",
        default='text',
        help="Output format",
        choices=('text', 'prettyjson', 'json')
    )

    args = parser.parse_args(argv[1:])

    with mate3_connection(args.host, args.port) as client:
        blocks = client.all_blocks()

        if args.format == 'text':
            for block in blocks:
                print(f"{block.device.name.replace('_', ' ').title()}:")
                for field_name, value in block._asdict().items():
                    print(f"    {field_name}: {value}")
                print("")

        if args.format in ('json', 'prettyjson'):
            indent = None if args.format == 'json' else 4
            block_dicts = [b._asdict() for b in blocks]
            for block_dict in block_dicts:
                block_dict['device'] = block_dict['device'].name
            print(json.dumps(block_dicts, indent=indent))



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
