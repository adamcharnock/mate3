# Outback Mate 3 Python Library

This library provides complete support for all outback devices (at least in theory, 
I don't own all the devices so cannot test it).

This data is accessed though the Mate3's Modbus interface.

Tested on Python 3.7. May work on 3.6.

## Enabling the Modbus interface on your Mate 3

TBA. System -> opticsre -> Modbus?

## Using this library

Example use:

```python
from mate3 import mate3_connection
import time

host = '192.168.0.123'
port = 502

with mate3_connection(host, port) as client:
    while True:
        for block in client.all_blocks():
            print(block)

        time.sleep(3)
```

## Various notes

The `structures.py` and `parsers.py` files are *auto generated* 
from the CSV files located in `registry_data/`. The CSV files are 
generated though text extraction from the 
[axs_app_note.pdf](http://www.outbackpower.com/downloads/documents/appnotes/axs_app_note.pdf) 
PDF provided by OutBack. This process is handled by two python files:

* `csv_generator.py` – Extract the CSV data from the PDF
* `code_generator.py` – Generate the Python code from the CSV data

## Future work

* Create a command line interface
* Support the writing of values back to the Mate3
* Web interface?

## Credits

This is a heavily refactored version of 
[basrijn's Outback_Mate3 library](https://github.com/basrijn/Outback_Mate3).
Thank you basrijn!
