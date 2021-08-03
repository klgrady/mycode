#!/usr/bin/env python3
#ipchk = "192.168.0.1"
ipchk = input("Apply an IP address: ")

# a string tests as True
if ipchk:
   print("Looks like the IP address was set: " + ipchk)
else:
    print("You did not provide input.")
