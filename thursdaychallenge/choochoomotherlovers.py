#!/usr/bin/python3

import os
from subprocess import STDOUT, check_call

def main():
    #install sl
    check_call(['sudo', 'apt-get', 'install', '-y', 'sl'], stdout=open(os.devnull, 'wb'), stderr=STDOUT)

    #create a new directory
    if os.path.exists("/home/student/mycode/slappy"):
        os.system("rm -rf /home/student/mycode/slappy")

    os.mkdir("/home/student/mycode/slappy")

    #create the file
    f = open("/home/student/mycode/slappy/chad_stop_using_that_word.txt", "w")
    f.close()

if __name__ == "__main__":
    try:
        main()
    except:
        print("Your attempts to use that word have failed. Tiny violins play in the distance...")
