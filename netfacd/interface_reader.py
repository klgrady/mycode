#!/usr/bin/python3

import netifaces

def get_ip_addr():
    return (netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']

def get_mac_addr():
    return (netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']

print(netifaces.interfaces())

for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print('MAC:', end='')
            print('IP:', end='')
        except:
            print("Noping on out of here. No adapter info for you.")
