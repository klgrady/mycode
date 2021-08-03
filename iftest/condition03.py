#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")

## test for mtg (case insensitive) input
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

## print something so even people who can't type mtg know we're done
print("Exiting the script.")

