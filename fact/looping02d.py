#!/usr/bin/env python3

# open file in read mode
dnsfile = open("dnsservers.txt", "r")
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile open
    # loop across the lines in the file
    for svr in dnsfile:
        #print and end without a newline
        svr = svr.rstrip('\n') # remove newline char if exists
                               # would exist on all bu the last line
        # IF string svr ends with 'org'
        if svr.endswith('org'):
            with open("org-domain.txt", "a") as svrfile:
                svrfile.write(svr + "\n")
        # ELSE-IF string svr ends with 'com'
        if svr.endswith('com'):
            with open("com-domain.txt", "a") as svrfile:
                svrfile.write(svr + "\n")
# no need to close your file
