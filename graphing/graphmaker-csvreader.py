#!/usr/bin/env python3

INPUTFILE = "/home/student/mycode/graphing/2018summary.csv"
OUTPUTFILE = "/home/student/mycode/graphing/2018summaryv2.png"

# from python std library
import csv
import os

# python -m pip install np
import numpy as np
# python -m pip install matplotlib==3.0.3 # bugs encountered in latest version
import matplotlib
matplotlib.use('Agg')
# sudo apt install python3-tk
import matplotlib.pyplot as plt

def parsecsvdata(inputfile):
    """returns a list. [0] is LAN and [1] is WAN data"""
    summary = [] # list that will contain [(LAN), (WAN)]

    # open csv data
    with open(inputfile, "r") as downtime:
        # parse csv data with csv.reader
        downdata = csv.reader(downtime, delimiter=",")
        for row in downdata:
            rowdat = (row[0], row[1], row[2], row[3])
            summary.append(rowdat) # add dict to list
    return summary


def main():
    N = 4
    ## grab your data
    summary = parsecsvdata(INPUTFILE) # grab our data from file
    
    # convert WAN data from STRING to INT for WAN outage list
    localnetMeans = list(map(int,summary[0]))
    # convert WAN data from STRING to INT for WAN outage list
    wanMeans = list(map(int,summary[1]))

    # print out local inputdata vars for script debug
    print(f"localnetMeans = {localnetMeans}")
    print(f"wanMeans = {localnetMeans}")

    ind = np.arange(N)          # the x locations for the groups
    # width of the bars: can also be len(x) sequence
    width = 0.35


    # Decribe where to display p1
    p1 = plt.bar(ind, localnetMeans, width)
    # stack p2 on top of p1
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    # Describe the table metadata
    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    # check if PNG file exists from previous run
    if os.path.isfile(OUTPUTFILE):
        os.remove(OUTPUTFILE)
    # save the new outputfile to disk
    plt.savefig(OUTPUTFILE)
    print("Graph created: " +  OUTPUTFILE)

if __name__ == "__main__":
    main()
