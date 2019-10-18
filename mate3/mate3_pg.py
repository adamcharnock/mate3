import argparse
from sys import argv
from typing import NamedTuple, List, Type, Iterable

from pymodbus.constants import Defaults

from mate3 import mate3_connection
import time

from mate3.api import AnyBlock, Device

try:
    from yaml import load, FullLoader
except ImportError:
    raise ImportError("To use this command you must install the pyyaml package")

try:
    import psycopg2
    from psycopg2.extensions import quote_ident
except ImportError:
    raise ImportError("To use this command you must install the psycopg2-binary (or psycopg2) package")

host = '192.168.0.123'
port = 502


class Table(NamedTuple):
    name: str
    definitions: List["Definition"]


class Definition(NamedTuple):
    port: int
    device: Device
    field: str
    db_column: str


def read_definitions(f) -> List[Table]:
    in_yaml = load(f, Loader=FullLoader)
    tables = []

    for table_name, in_definitions in in_yaml.get('tables', {}).items():
        definitions = []
        for in_definition in in_definitions:
            # Get the block class
            definitions.append(Definition(
                port=int(in_definition['port']),
                device=Device[in_definition['device']],
                field=in_definition['field'],
                db_column=in_definition['db_column'],
            ))

        tables.append(
            Table(table_name, definitions)
        )

    return tables


def create_tables(conn, tables: List[Table], hypertables: bool):
    with conn.cursor() as curs:
        for table in tables:
            sql = (
                f"CREATE TABLE IF NOT EXISTS {quote_ident(table.name, curs)} (\n"
                f"    timestamp TIMESTAMPTZ NOT NULL,"
            )
            for definition in table.definitions:
                sql += f'\n    {quote_ident(definition.db_column, curs)} INT NULL,'
            sql = sql.rstrip(',')
            sql += '\n)'

            curs.execute(sql)
            if hypertables:
                try:
                    curs.execute("SELECT create_hypertable(%s, 'timestamp')", [table.name])
                except psycopg2.DatabaseError as e:
                    if 'already a hypertable' in str(e):
                        pass
                    else:
                        raise


def _get_value(blocks: List[AnyBlock], definition: Definition) -> ...:
    for block in blocks:
        if not hasattr(block, 'port_number'):
            continue

        if block.port_number == definition.port and block.device == definition.device:
            return getattr(block, definition.field)


def insert(conn, tables: List[Table], blocks: List[AnyBlock]):

    with conn.cursor() as curs:
        for table in tables:
            insert_kv = {}
            for definition in table.definitions:
                value = _get_value(blocks, definition)
                if value is not None:
                    insert_kv[definition.db_column] = value

            column_names = [quote_ident(c, curs) for c in insert_kv.keys()]
            placeholders = ['%s'] * len(insert_kv)
            sql = (
                f"INSERT INTO {quote_ident(table.name, curs)} "
                f"(timestamp, {', '.join(column_names)}) "
                f"VALUES (NOW(), {', '.join(placeholders)})"
            )
            curs.execute(sql, list(insert_kv.values()))


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
        "--interval", "-i",
        dest="interval",
        default=5,
        help="Polling interval in seconds",
        type=int,
    )
    parser.add_argument(
        "--database-url",
        dest="database_url",
        help="Postgres database URL",
        default="postgres://postgres@localhost/postgres",
    )
    parser.add_argument(
        "--definitions",
        dest="definitions",
        default='text',
        help="YAML definition file",
        type=argparse.FileType('r'),
        required=True,
    )
    parser.add_argument(
        "--hypertables",
        dest="hypertables",
        help="Should we create tables as hypertables? Use only if you are using TimescaleDB",
        action='store_true',
    )

    args = parser.parse_args(argv[1:])
    tables = read_definitions(args.definitions)

    with psycopg2.connect(args.database_url) as conn:
        conn.autocommit = True

        create_tables(conn, tables, hypertables=args.hypertables)
        with mate3_connection(args.host, args.port) as client:
            while True:
                start = time.time()

                insert(conn, tables, list(client.all_blocks()))

                total = time.time() - start
                sleep_time = args.interval - total
                if sleep_time > 0:
                    time.sleep(args.interval - total)


if __name__ == '__main__':
    main()
