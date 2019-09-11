#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import time

# Setup logging
from mate3.api import mate3_connection

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%Y%m%d %H:%M:%S"
)
logging.getLogger(__name__)


host = "192.168.1.246"
port = 502


def main():
    with mate3_connection(host, port) as client:
        while True:
            for block in client.all_blocks():
                print(block)

            time.sleep(3)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
