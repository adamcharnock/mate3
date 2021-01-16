import json
from pathlib import Path

import pytest
from mate3.api import Mate3Client
from mate3.sunspec.fields import Mode
from pytest_dictsdiff import check_objects

KNOWN_SYSTEMS = sorted((Path(__file__).parent / "known_systems").iterdir())


def _test_read_gives_expected_results(client, system_dir):

    # Get the values for this client:
    read_devices = []
    for device in client.connected_devices:
        name = device.__class__.__name__
        values = {}
        for value in device.fields([Mode.R, Mode.RW]):
            values[value.name] = value.to_dict()
        read_devices.append({"name": name, "address": device.address, "values": values})
    read_devices = sorted(read_devices, key=lambda x: x["address"])

    # Compare them with what we expect:
    with open(system_dir / "expected.json") as f:
        expected_devices = json.load(f)
    expected_devices = sorted(expected_devices, key=lambda x: x["address"])

    assert check_objects(expected_devices, read_devices)


@pytest.mark.parametrize("system_dir", KNOWN_SYSTEMS)
def test_known_system(subtests, system_dir):
    # Read it (which is a test in itself)
    with Mate3Client(
        host=None, cache_path=system_dir / "modbus.json", cache_only=True, cache_writeable=False
    ) as client:
        with subtests.test("Reading gives expected results"):
            _test_read_gives_expected_results(client, system_dir)
        with subtests.test("Writing the same values back gives the same results"):
            # ... 'cos if that isn't the case, it implies we're serialising/deserialising incorrectly.
            cache = {k: v for k, v in client._client._cache.items()}
            for device in client.connected_devices:
                # NB: ignoring Mode.W as we can't read the value to be able to write it back i.e. we don't know what to
                # write.
                for value in device.fields(modes=[Mode.RW]):
                    if value.implemented:
                        value.write(value.value)
            new_cache = client._client._cache
            assert check_objects(cache, new_cache)
