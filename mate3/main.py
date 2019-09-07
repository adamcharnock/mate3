#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import logging
import contextlib

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

# Setup logging
from mate3.io import read_block
from mate3.base_parser import parse
from mate3.base_structures import Device

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%Y%m%d %H:%M:%S"
)
logging.getLogger(__name__)


mate3_ip = "192.168.1.246"
mate3_modbus_port = 502

SUNSPEC_REGISTER_OFFSET = 40000


def main():
    _client = ModbusClient(mate3_ip, mate3_modbus_port)
    base_reg = SUNSPEC_REGISTER_OFFSET

    while True:
        reg = base_reg
        for _ in range(0, 30):
            block_size, device = read_block(_client, reg)

            if device is Device.end_of_sun_spec:
                # No more blocks to read
                break

            if not device:
                # Unknown device
                continue

            structure = parse(device, _client, reg)

            if structure:
                print(structure)

            reg = reg + block_size + 2

        time.sleep(3)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
