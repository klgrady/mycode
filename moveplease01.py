#!/usr/bin/env python3

import shutil
import os

def main():
    os.chdir('/home/student/mycode/')

    # move the file. if it exists, it will be overwritten. if filename is given in dest, filename will change
    shutil.move('raynor.obj', 'ceph_storage/')

    xname = input("What is the new name for kerrigan.obj? ")
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


if __name__ == "__main__":
    main()
