usage: csvToSubstitution [-h] [-o [OUTPUT]] [-d [DATABASE ...]] [fname ...]

Munge CSV files into an EPICS compatible substitution file

positional arguments:
  fname                 Files to be munged

options:
  -h, --help            show this help message and exit
  -o, --output [OUTPUT]
                        Output file. If unspecified, each fname munges into
                        separate fname.substitutions
  -d, --database [DATABASE ...]
                        Database files being substituted. Paths relative to
                        IOC top. Default: db/fname.db for all input files
