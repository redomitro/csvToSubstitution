Example templates and csvs for csvToSubstitution. Based on the Keithley 6487 picometer/voltage source.

With no switches, EXAMPLE.csv will be munged into EXAMPLE.substitutions. When `make` is run with the included Makefile, the EPICS build system will intercept the substitution file to generate EXAMPLE.db and place it in the $(TOP)/db folder. On runtime with the included st.cmd file, EPICS will expand EXAMPLE.db according to runtime.substitutions.
