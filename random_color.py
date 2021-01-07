import os
import subprocess
import random
import datetime
import pathlib

def new_colour(run=True):
    base16_shell = os.environ['BASE16_SHELL'] 
    proc = subprocess.run(['ls', '{}/scripts'.format(base16_shell)], capture_output=True)
    out = proc.stdout.split()
    cmd = random.choice(out).decode('utf-8').split('.sh')[0].replace('-','_',1)

    if run:
        print("New colour: {}".format(cmd))
        subprocess.run(['/bin/zsh', '-i', '-c', cmd])
    return cmd

def log_colour(colour, colour_file):
    now = datetime.datetime.now()
    string = "{} {}\n".format(colour, now)
    with open(colour_file, "a") as outfile:
        outfile.write(string)



if __name__ == "__main__":
    cmd = new_colour(run=False)
    colour_file = "./prev_colours.txt"
    current = new_colour()
    while input('Nice colour? (y/N)')!='y':
        current = new_colour()
    log_colour(current, colour_file)


