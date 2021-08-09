#!/usr/bin/python3

loginfail = 0

keystone_file = open("keystone.common.wsgi", "r")
keystone_file_line = keystone_file.readlines()

for line in keystone_file_line:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1

print("Failed login attempts:", loginfail)
keystone_file.close()

