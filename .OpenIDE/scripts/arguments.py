#!/usr/bin/env python
import sys

def print_definitions():
    print("Runs a script with arguments|")
    print("NAME|\"Name of the person to greet\" end")

def run_command(run_location, global_profile, local_profile, args):
    if len(args) == 0:
        print("error|You must pass the argument NAME as the person you want to greet")
        return
    print("Hello "+args[0]+"!")

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1 and args[2] == 'get-command-definitions':
        print_definitions()
    else:
        run_command(args[1], args[2], args[3], args[4:])