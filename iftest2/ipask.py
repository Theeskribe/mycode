#!/usr/bin/env python3
ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string willl test True
if ipchk:
   print("Looks like the IP address was set: " + ipchk)
else:   # if data is NOT provided
    print("You did not provide input.") # indented under else
