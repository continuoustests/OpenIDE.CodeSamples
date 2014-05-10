#!/usr/bin/env python
import sys, subprocess

# Runs process and returns lines ouputted by the process
def run_process(exe):
    p = subprocess.Popen(exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = []
    while(True):
        retcode = p.poll() # returns None while subprocess is running
        line = p.stdout.readline().strip('\n').strip('\r')
        if line != "":
            lines.append(line)
        if(retcode is not None):
            break
    return lines

def print_definitions():
    print("Reads configuration and prints value")

def run_command(run_location, global_profile, local_profile, args):
    lines = run_process(["oi","conf","read","read-configuration.test"])
    if len(lines) != 1:
        print("error|Could not find a config entry for read-configuration.test")
        return
    print("Entry is: "+lines[0])

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1 and args[2] == 'get-command-definitions':
        print_definitions()
    else:
        run_command(args[1], args[2], args[3], args[4:])
