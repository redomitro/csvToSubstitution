Munge CSV files into an EPICS compatible substitution file. Compatible both with compile-time expansion with MSI and run-time expansion with dbLoadTemplate.

usage: `./csvToSubstitution [-hqf] [-o OUTPUT] FNAME ...`

Formatting:
- Separate files by an empty line
- The first line after an empty line is the file being substituted. For compile-time expansion, the path is relative to the directory containing the substitution file. For run-time expansion it's relative to IOC top.
- The second line after an empty line is the pattern.
- The remaining lines until an all-commas line is found are substitution lines.
- Comment lines with `#`.

Dependencies:
- Python 3

Portable use: Drop the file into a location recognised by PATH.

Please consult the output of the --help switch for additional information.
