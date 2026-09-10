Munge CSV files into an EPICS compatible substitution file

usage: `csvToSubstitution [-h] [-o [OUTPUT]] [-d [DATABASE ...]] FNAME ...`

CSV formatting: Patterns are separated by an empty line. The line after an empty line is formatted as a pattern line.

Dependencies:
- Python 3

Limitations:
- One db file per csv. It's simple enough to pass `*.csv` as the argument.
