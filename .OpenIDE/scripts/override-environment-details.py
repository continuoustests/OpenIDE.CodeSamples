#!/usr/bin/env python
import os, sys

def print_definitions():
    print("Overrides environment details to when no key path is specified it uses current|")
    print("[[environment]]|\"\"")
    print("  details|\"Displays details about a running environment\"")
    print("    [KEY]|\"The environment key path. Default current\" end ")
    print("  end ")
    print("end")

def run_command(run_location, global_profile, local_profile, args):
    key = os.getcwd()
    # First argument is the name of the sub command "details" so path is second
    if len(args) > 1:
        key = args[1]
    # Run the command that was overridden by this script
    print("command-original|environment details \""+key+"\"")

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1 and args[2] == 'get-command-definitions':
        print_definitions()
    else:
        run_command(args[1], args[2], args[3], args[4:])
