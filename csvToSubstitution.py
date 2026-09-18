#!/usr/bin/env python3

import argparse, os, sys

def listSplit(array, separator):
    # split an array based on a separator element - replicating string.split for arrays
    splitIndices = [-1]+[i for i in range(len(array)) if array[i]==separator] # define slice points
    slicedArray = [array[1+splitIndices[i]:splitIndices[i+1]] for i in range(len(splitIndices)-1)]
    return slicedArray

def lineMunge(line, index):
    if not index:
        # leading line of pattern: leading string is "    pattern {", elements are unquoted
        s = ', '.join(line.split(','))
        return f"{4*" "}pattern {{ {s} }}"
    else:
        # other lines: leading string is 12 spaces, elements are quoted
        s = ', '.join([f'\"{i}\"' for i in line.split(',')])
        return f"{12*" "}{{ {s} }}"

def patternMunge(pattern):
    return "\n".join([lineMunge(pattern[i], i) for i in range(len(pattern))]) # munges each pattern line and joins them into a string

def csvMunge(fname, dbname):
    dbLeading = f"file \"{dbname}\"" # placeholder for readability
    lines = [i.strip(',') for i in open(fname).read().split("\n")] # strip all lines of trailing commas
    patterns = [patternMunge(i) for i in listSplit(lines, '')]
    return f"{dbLeading}{{\n{'\n'.join(patterns)}\n}}"

def main():

    # ingest arguments from command line
    parser = argparse.ArgumentParser(description="Munge CSV files into an EPICS compatible substitution file")
    parser.add_argument("FNAME", nargs="+", help="Files to be munged")
    parser.add_argument("-f", "--force", help="Overwrite existing files. If unspecified, attempting to output to an existing file throws an error.", action="store_true")
    parser.add_argument("-o", "--output", help="Output file. If unspecified, each fname munges into separate fname.substitutions", nargs='?')
    parser.add_argument("-d", "--database", help="Database files being substituted. Paths relative to IOC top. Default: db/fname.db for all input files", nargs="*") #Maybe change to paths relative to $(TOP)/db?
    args = parser.parse_args()

    nFiles = len(args.FNAME)
    fnameBases = [(i[:-4] if i.endswith('.csv') else i) for i in args.FNAME]

    # handle existing files
    outputFiles = [args.output] if args.output else [f"{i}.substitutions" for i in fnameBases]
    if (not args.force and any([os.path.exists(i) for i in outputFiles])):
        print(
            f"Error: File '{[i for i in outputFiles if os.path.exists(i)][0]}' already exists in the current directory. Pass -f to overwrite.",
            file=sys.stderr,
        )
        sys.exit(1)

    # munge CSVs
    dbs = []
    for i in range(nFiles):
        if(not args.database or i>=len(args(database))): #non-commutative logical or; inverting this causes an error
            x = csvMunge(args.FNAME[i], f'db/{fnameBases[i]}.db')
        else:
            x = csvMunge(args.FNAME[i], args.database[i])
        dbs.append(x)

    # handle output
    if args.output:
        outString = "\n\n".join(dbs)
        with open(args.output, "w") as outFile:
            outFile.write(outString)
    else:
        for i in range(nFiles):
            with open(outputFiles[i], "w") as outFile:
                outFile.write(dbs[i])

if(__name__=="__main__"):
    main()
