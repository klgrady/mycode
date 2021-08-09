#!/usr/bin/python3
import re

loginfail = 0
loginsuccess = 0
ip = []

with open("keystone.common.wsgi") as kfile:
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
            xp = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', line.split(" ")[-1])
            if xp != None : ip.append(xp.group(0))
        #elif "- - - - -] Loaded" in line:
        elif "-] Authorization failed" in line:
            loginsuccess += 1


print("Failed login attempts:", loginfail)
print("Successful login attempts:", loginsuccess)
print(ip)
