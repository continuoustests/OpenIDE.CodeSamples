#!/usr/bin/env python
import os, sys

def print_definitions():
    print("Creates a new file and appends appropriate header|")
    print("FILE|\"Path to the file you want to create\" end ")

def write(msg):
    sys.stdout.write(msg+"\n")
    sys.stdout.flush()

def get_filepath(run_location, input_path):
    # First check to see if a relative path is specified
    # if not expect inputted path to be fullpath
    path = os.path.relpath(os.path.join(run_location, input_path))
    if os.path.isfile(path):
        return path, os.path.splitext(path)[1]
    return input_path, os.path.splitext(input_path)[1]

def header_from_extension(extension):
    if extension.lower() == ".sh":
        return "#!/bin/bash"
    if extension.lower() == ".py":
        return "#!/usr/bin/env python"
    return None

def wait_for_command():
    while True:
        line = sys.stdin.readline()
        if line == "end-of-command\n":
            break

def run_command(run_location, global_profile, local_profile, args):
    if len(args) != 1:
        write("error|Script expects path to the file to create")
        return
    # Force running the builtin version of the touch command as this
    # is the one we are overriding
    write("command-builtin|touch \""+args[0]+"\"")
    # Wait for the command to complete so the file is actually created
    wait_for_command()
    filepath, file_extension = get_filepath(run_location, args[0])
    # Get the header we want to insert
    header = header_from_extension(file_extension)
    if header == None:
        return
    # Insert the heading into the first line and first column of the 
    # newly created file in the editor
    write("command|editor insert \""+header+"\" \""+filepath+"|1|1\"")


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1 and args[2] == 'get-command-definitions':
        print_definitions()
    else:
        run_command(args[1], args[2], args[3], args[4:])
