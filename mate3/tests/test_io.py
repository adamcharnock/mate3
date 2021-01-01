from pathlib import Path

from mate3.api import Mate3Client

CACHE_PATH = Path(__file__).parent / "known_systems" / "chinezbrun" / "modbus.json"


def test_individual_reads_work(subtests):
    """
    It should a) read successfully, and b) have an updated last_read value
    """

    with Mate3Client(host=None, cache_path=CACHE_PATH, cache_only=True) as client:
        field = client.devices.mate3.system_name
        first_read_time = field.last_read

        with subtests.test("Reading doesn't fail"):
            field.read()
        with subtests.test("Reading updates the last_read time"):
            assert field.last_read > first_read_time


def test_individual_writes_work(subtests):
    """
    It should a) write successfully, and b) have the new value, and c) have an updated last_read value.
    """

    with Mate3Client(host=None, cache_path=CACHE_PATH, cache_only=True) as client:
        field = client.devices.mate3.system_name
        first_read_time = field.last_read
        with subtests.test("Writing doesn't fail"):
            field.write("Test")
        with subtests.test("A read occurs after writing (i.e. there's an updated last_read time)"):
            assert field.last_read > first_read_time
