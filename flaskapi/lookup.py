#!/usr/bin/python3
import requests

for i in range(51):
    stuff = requests.get("http://0.0.0.0:2224/fast")
    print(stuff)


