Munge CSV files into an EPICS compatible substitution file

usage: `./csvToSubstitution.py [-h] [-f] [-o [OUTPUT]] [-d [DATABASE ...]] FNAME ...`

alternate: `python3 csvToSubstitution.py [-h] [-f] [-o [OUTPUT]] [-d [DATABASE ...]] FNAME ...`

CSV formatting: Patterns are separated by an empty line (all commas). The line after an empty line is formatted as a pattern line. See the example files for guidance.

Dependencies:
- Python 3

Limitations:
- One db file per csv. It's simple enough to pass `*.csv` as the argument.

Please consult the output of the --help switch for additional information.
