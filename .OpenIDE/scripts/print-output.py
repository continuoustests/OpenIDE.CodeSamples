#!/usr/bin/env python
import sys

def print_definitions():
    print("Prints text, warnings and errors")

def run_command(run_location, global_profile, local_profile, args):
    print("Hello text!")
    print("warning|Hello warning!")
    print("error|Hello error!")

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1 and args[2] == 'get-command-definitions':
        print_definitions()
    else:
        run_command(args[1], args[2], args[3], args[4:])
