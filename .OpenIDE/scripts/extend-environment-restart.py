#!/usr/bin/env python
import sys

def print_definitions():
    print("Extension for environment adding environment restart|")
    print("[[environment]]|\"\"")
    print("  restart|\"Restarts environemnt\" end ")
    print("end")

def write(msg):
    sys.stdout.write(msg+"\n")
    sys.stdout.flush()

def wait_for_command():
    while True:
        line = sys.stdin.readline().strip("\n")
        if line == "end-of-command":
            break

def run_command(run_location, global_profile, local_profile, args):
    # Run shutdown command to kill the environment and then starting it up again
    write("shutting down..")
    write("command|shutdown")
    wait_for_command()
    write("starting up...")
    write("command|environment start")

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1 and args[2] == 'get-command-definitions':
        print_definitions()
    else:
        run_command(args[1], args[2], args[3], args[4:])
