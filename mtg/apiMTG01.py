#!/usr/bin/python3

import requests

def main():
    resp = requests.get("https://api.magicthegathering.io/vi/sets")
    print( dir(resp) )

if __name__ == "__main__":
    main()

