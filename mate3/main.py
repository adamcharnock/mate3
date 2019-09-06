#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import logging
import contextlib

import psycopg2.pool

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

# Setup logging
from mate3.io import read_sun_spec_header, read_block
from mate3.parsers import (
    parse_single_inverter_block,
    parse_charge_controller_block,
    parse_flexnet_dc_block,
)
from mate3.structures import Device

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%Y%m%d %H:%M:%S"
)
logging.getLogger(__name__)


mate3_ip = "192.168.1.246"
mate3_modbus_port = 502

SUNSPEC_REGISTER_OFFSET = 40000


@contextlib.contextmanager
def get_db_connection():
    connection = pool.getconn()
    yield connection
    pool.putconn(connection)


def main():
    # Try to build the mate3 MODBUS connection
    logging.info("Building MATE3 MODBUS connection")
    # Mate3 connection
    try:
        _client = ModbusClient(mate3_ip, mate3_modbus_port)
        logging.info(".. Make sure we are indeed connected to an Outback power system")
        size = read_sun_spec_header(_client, SUNSPEC_REGISTER_OFFSET)

        if size is None:
            logging.info("We have failed to detect an Outback system. Exciting")
            exit()

    except:
        _client.close()
        logging.info(
            ".. Failed to connect to MATE3. Enable SUNSPEC and check port. Exciting"
        )
        raise
        exit()

    logging.info(".. Connected OK to an Outback system")

    base_reg = SUNSPEC_REGISTER_OFFSET + size + 4

    pool = psycopg2.pool.SimpleConnectionPool(
        minconn=1,
        maxconn=2,
        dbname="postgres",
        host="127.0.0.1",
        port=5432,
        user="postgres",
        password="password",
    )

    while True:
        reg = base_reg
        for block in range(0, 30):
            block_size, device = read_block(_client, reg)
            structure = None

            if device == Device.single_phase_radian_inverter:
                structure = parse_single_inverter_block(_client, reg)
            elif device == Device.charge_controller:
                structure = parse_charge_controller_block(_client, reg)
            elif device == Device.flexnet_dc:
                structure = parse_flexnet_dc_block(_client, reg)
            elif device == Device.end_of_sun_spec:
                break
            else:
                logging.info(f"Device {device} not implemented")

            if structure:
                print(structure)

            reg = reg + block_size + 2

        time.sleep(3)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
