#!/usr/bin/env python3

# open file in read mode
dnsfile = open("dnsservers.txt", "r")
with open("dnsservers.txt", "r") as dnsfiles:
    # create list of lines
    dnslist = dnsfile.readlines()
    # loop over lines
    for svr in dnslist:
        #print and end without a newline
        print(svr, end="")
# no need to close your file
#dnsfile.close()

