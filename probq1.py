#!/usr/bin/env python


import sys
import pandas
import matplotlib.pyplot as plot
import scipy.stats

f = open("/Users/cmdb/data/day1/transcripts.gtf")

f.line.strip("\r\n").split("\t")

transcript = []


for line in f:
    field = line.strip("\r\n").split()
    if field [2] == "transcript":
        if field [6] == "+":
            name = line.rstrip("\r\n").split()
        if field [6] == "-":
            name = line.rstrip("\r\n").split()
        if field [2] == "":
            break
            
        transcript.append( field[0] )
        transcript.append( field[5] )
        
    
print transcript  
    
