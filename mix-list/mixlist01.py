#!/usr/bin/env python3

# Create a list of data
my_list = ["192.163.0.5", 5060, "UP"]

# Print the IP address
print("The first item in the list (IP): " + my_list[0])

# Print the port number
print("The second item in the list (port): " + str(my_list[1]))

# Print the state:
print("The last item in the list (state): " + my_list[2])


# This should be done with a regexp, tho.
iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

print(f"IP addresses are: {iplist[3]}, {iplist[4]}");
