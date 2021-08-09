#!/usr/bin/python3
import json

def commandpush(devicecmd):

    for ip in devicecmd.keys(): # looping through the dict
        print(f'Handshaking. .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

def devicereboot(ip_list):
    for ip in ip_list.keys(): # iterate through a list of ips
        print("Connecting to...", ip)
        print("REBOOTING NOW!")


    
# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    #devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    #["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    #print("\nData set found\n") # replace with function call that reads in data from file

    ## run

    with open("devicecmd.json", "r") as devicecmdfile:
        devicecmd = json.load(devicecmdfile)
        
    commandpush(devicecmd) # call function to push commands to devices
    devicereboot(devicecmd)
# call our main function
main()
