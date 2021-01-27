#!/usr/bin/python3

import sys
import getopt
import os
from movie import MovieTheater

def main(argv):

    inputfile = ""
    outputfile = ""

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('./'+os.path.basename(__file__)+' -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('./'+os.path.basename(__file__)+' -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    try:
        with open(inputfile, "r") as f:
            with open(outputfile, "w") as out:
                lines = f.readlines()
                myMovie = MovieTheater(lines)
                out.write(str(lines))
    except OSError:
        print("Could not open/read file:", inputfile)
        sys.exit()
        

        


if __name__ == "__main__":
    main(sys.argv[1:])