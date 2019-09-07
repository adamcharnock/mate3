# Outback Mate 3 Python Library

This library provides complete support for all outback devices (at least in theory, 
I don't own all the devices so cannot test it).

This data is accessed though the Mate3's Modbus interface.

## Enabling the Modbus interface on your Mate 3

TBA. System -> opticsre -> Modbus?

## Using this library

Still in development, so for now open `main.py` and take a look

## Various notes

The `structures.py` and `parsers.py` files are *auto generated* 
from the CSV files located in `registry_data/`. The CSV files are 
generated though text extraction from the 
[axs_app_note.pdf](http://www.outbackpower.com/downloads/documents/appnotes/axs_app_note.pdf) 
PDF provided by OutBack. This process is handled by two python files:

* `csv_generator.py` – Extract the CSV data from the PDF
* `code_generator.py` – Generate the Python code from the CSV data

## Future work

* Support use as a Python library (I want to get this data into Timescale DB)
* Create a command line interface
* Support the writing of values back to the Mate3
* Web interface?

## Credits

This is a heavily refactored version of 
[basrijn's Outback_Mate3 library](https://github.com/basrijn/Outback_Mate3).
Thank you basrijn!
