#!/usr/bin/env python
import sys

def print_definitions():
    print("Opens the running scrip in the editor")

def write(msg):
    sys.stdout.write(msg+"\n")
    sys.stdout.flush()

def wait_for_command():
    while True:
        line = sys.stdin.readline().strip("\n")
        if line == "end-of-command":
            break

def run_command(run_location, global_profile, local_profile, args):
    # Runs editor goto command to open current file on line 1 column 1
    # Waiting for the command to finish is not required it is just
    # here to show you how to do it.
    write("command|editor goto \""+sys.argv[0]+"|1|1\"")
    wait_for_command()

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1 and args[2] == 'get-command-definitions':
        print_definitions()
    else:
        run_command(args[1], args[2], args[3], args[4:])
