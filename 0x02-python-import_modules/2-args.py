#!/usr/bin/python3
import sys
if __name__ == "__main__":
    an_arguments = len(sys.argv) - 1
    if an_arguments == 0:
        print("{} arguments.".format(an_arguments))
    elif an_arguments == 1:
        print("{} an_arguments:".format(an_arguments))
    else:
        print("{} an_arguments:".format(an_arguments))

    if an_arguments >= 1:
        for an_arguments, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(an_arguments, arg))
