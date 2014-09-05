#!/usr/bin/env python

# i know what I want to do, no idea on how to code it

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
        transcript.append( field[0] )
        transcript.append( field[5] )
        
    
    print transcript  
    
