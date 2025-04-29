"""Cleaning up of SOL 145 output files
   
   Author: Cristina Riso
"""

import os

# analysis files
files = os.listdir(".")
outfiles = []
for file in files:
    if (
        "sol" in file
        and ".txt" in file
        or ".xdb" in file
        or ".f04" in file
        or ".DBALL" in file
        or ".MASTER" in file
        or ".IFPDAT" in file
    ):
        os.remove(file)
    elif "sol" in file and ".f06" in file:
        outfiles.append(file)

# loop the analysis files
for file in outfiles:

    print("\nProcessing file " + file)

    # open file
    input_file = open(file, "r")
    lines = input_file.readlines()
    input_file.close()

    # rewrite file
    output_file = open(file.replace(".f06", "_visualization.txt"), "w")

    write_line = False

    for line in lines:

        if (
            "KFREQ            1./KFREQ         VELOCITY            DAMPING         FREQUENCY            COMPLEX   EIGENVALUE"
            in line
        ):
            write_line = True
            continue

        if "1.0000000E+25" in line:
            line.replace("1.0000000E+25", "1.0000000E+00")

        if write_line and not "PAGE" in line:
            output_file.write(line)
        else:
            write_line = False
