# Troubleshooting

Some ideas (which can be helpful for issues)

## Set log-level to DEBUG

See `mate3 -h` for the CLI, otherwise the following (or similar) for python code:

```python
from loguru import logger
logger.remove()
logger.add(sys.stderr, level="DEBUG")
```

## List the devices

```sh
$ mate3 devices --host ...
name                                               address    port
----                                               -------    ----
Mate3                                              40069      None
ChargeController                                   40986      4
ChargeControllerConfiguration                      41014      4
...
```
Are they all there?

## Create a dump of the raw modbus values

See `mate3 dump -h`. You can send the resulting JSON file to someone to help debug. (Just note that it includes all the data about the Mate, e.g. any passwords etc.)