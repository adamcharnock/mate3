from pathlib import Path

CACHE_PATH = Path(__file__).parent / "known_systems" / "chinezbrun" / "modbus.json"


def test_read_txt(script_runner):
    ret = script_runner.run("mate3", "read", f"--cache-path={CACHE_PATH}", "--cache-only")
    assert ret.success


def test_read_json(script_runner):
    ret = script_runner.run("mate3", "read", f"--cache-path={CACHE_PATH}", "--cache-only", "--format", "json")
    assert ret.success


def test_devices(script_runner):
    ret = script_runner.run("mate3", "devices", f"--cache-path={CACHE_PATH}", "--cache-only")
    assert ret.success


def test_write(script_runner):
    ret = script_runner.run(
        "mate3", "write", f"--cache-path={CACHE_PATH}", "--cache-only", '--set=mate3.system_name="testing"'
    )
    assert ret.success
