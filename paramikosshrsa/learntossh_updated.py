#!/usr/bin/env python3

## std library imports on top
import os

## 3rd party imports below
import paramiko

## work assigned to a junior programming asset on our team
from jrprogrammer import cmdissue


def get_input():
    commands = ""
    all_commands = []
    while commands != "done":
        commands = input("Full command you wish to run: > ").strip()
        all_commands.append(commands)
    return all_commands


def get_ips():
    ips = ""
    all_ips = {}
    print("""
    Enter all IP addresses and associated username in this format: [ip address] [username]
       e.g.   192.168.13.13 blackhatcat
       Enter 'done' when done.
       """)

    while True:
        ips = input("> ")
        if ips.lower() == "done":
            break
        data = ips.strip().split(' ')
        all_ips[data[0]] = data[1]
    return all_ips

def main():
  ## create session object
  sshsession = paramiko.SSHClient()
  sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")
  
  our_commands = get_input()
  ips = get_ips()

  ## create SSH connection
  for key in ips.keys():
      hostname = key
      username = ips[key]
      sshsession.connect(hostname=hostname, username=username, pkey=mykey)
  

      for x in our_commands:
        ## call our imported function and save the value returned
        resp = cmdissue(x, sshsession)
        ## if returned response is not null, print it out
        if resp != "":
          print(resp)
  
      ## end the SSH connection
      sshsession.close()

if __name__ == '__main__':
  main()

