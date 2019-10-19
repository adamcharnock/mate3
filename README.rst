
Outback Mate 3 Python Library
=============================

This library provides complete support for all outback devices (at least in theory,
I don't own all the devices so cannot test it).

This data is accessed though the Mate3's Modbus interface.

Tested on Python 3.7. May work on 3.6.

Installation (pip)
------------------

Install via pip/poetry:

```
pip install mate3
```

Installation (Docker)
---------------------

sudo docker --rm --ti adamcharnock/mate3 poetry run mate3_pg -H 192.168.1.246

Enabling the Modbus interface on your Mate 3
--------------------------------------------

TBA. System -> opticsre -> Modbus?

Using the library
-----------------

Example use:

.. code-block:: python

   from mate3 import mate3_connection
   import time

   host = '192.168.0.123'
   port = 502

   with mate3_connection(host, port) as client:
       while True:
           for block in client.all_blocks():
               print(block)

           time.sleep(3)

Using the command line interface (CLI)
--------------------------------------

A simple CLI is available which will read all available values from the Mate3:

.. code-block::

   $ mate3 -h
    usage: mate3 [-h] --host HOST [--port PORT] [--format {text,prettyjson,json}]

    Read all available data from the Mate3 controller

    optional arguments:
      -h, --help            show this help message and exit
      --host HOST, -H HOST  The host name or IP address of the Mate3
      --port PORT, -p PORT  The port number address of the Mate3
      --format {text,prettyjson,json}, -f {text,prettyjson,json}
                            Output format

Example use:

.. code-block::

   $ mate3 --host 192.168.0.123

The mate2_pg utility
--------------------

This utility will periodically fetch values from your Mate3 and insert them into a
Postgres database & table of your choosing:

```
$ mate3_pg -h
usage: mate3_pg [-h] --host HOST [--port PORT] [--interval INTERVAL]
                [--database-url DATABASE_URL] --definitions DEFINITIONS
                [--hypertables] [--quiet] [--debug]

Read all available data from the Mate3 controller

optional arguments:
  -h, --help            show this help message and exit
  --host HOST, -H HOST  The host name or IP address of the Mate3
  --port PORT, -p PORT  The port number address of the Mate3
  --interval INTERVAL, -i INTERVAL
                        Polling interval in seconds
  --database-url DATABASE_URL
                        Postgres database URL
  --definitions DEFINITIONS
                        YAML definition file
  --hypertables         Should we create tables as hypertables? Use only if
                        you are using TimescaleDB
  --quiet, -q           Hide status output. Only errors will be shown
  --debug               Show debug logging
```

Specify your table/fields in the definitions yaml file
(example: [pg_config.yaml](https://github.com/adamcharnock/mate3/blob/master/pg_config.yaml)).
Specify `--hypertables` if you are using TimescaleDB, as this will create
the tables as hypertables.

Example use
~~~~~~~~~~~

```
$ mate3_pg -H 192.168.1.123 --definitions pg_config.yaml --database-url=postgres://user:password@simone.local:5433/postgres
```

Docker use
~~~~~~~~~~

You can run `mate3_pg` within docker as follows:

```
docker run \
    -d --init --restart=unless-stopped \
    --name=mate3_pg \
    -v /path/to/local/pg_config.yaml:/mate3/pg_config.yaml \
    adamcharnock/mate3 \
    poetry run mate3_pg \
    -H 192.168.1.123 \
    --definitions pg_config.yaml \
    --database-url=postgres://user:password@simone.local:5433/postgres
```

Various notes
-------------

The ``structures.py`` and ``parsers.py`` files are *auto generated*
from the CSV files located in ``registry_data/``. The CSV files are
generated though text extraction from the
`axs_app_note.pdf <http://www.outbackpower.com/downloads/documents/appnotes/axs_app_note.pdf>`_
PDF provided by OutBack. This process is handled by two python files:


* ``csv_generator.py`` – Extract the CSV data from the PDF
* ``code_generator.py`` – Generate the Python code from the CSV data

Future work
-----------


* Support the writing of values back to the Mate3
* Web interface?

Packaging
---------

Package a new release using:

```shell
# Create packaging files for compatibility  with pip
dephell deps convert

# Bump version
poetry version {patch|minor|major}

# Commit and push
git commit -a
git push

# Docker build
docker build -t adamcharnock/mate3:{version_number} .
docker build -t adamcharnock/mate3:latest .

# Release to pypi
poetry publish --build

# Release to docker hub hub
docker push adamcharnock/mate3:{version_number}
docker push adamcharnock/mate3:latest
```

Credits
-------

This is a heavily refactored version of
`basrijn's Outback_Mate3 library <https://github.com/basrijn/Outback_Mate3>`_.
Thank you basrijn!
