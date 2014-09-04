#!/usr/bin/env python

import sys


output = [] # we have an epty  box in which we will be comiling our sequence
while True:
    line = sys.stdin.readline() #we start reading our line
    
    if line.startswith("Query="): #We break when we reach a line with the header, because thats the next sequence
        fly = line[1:].rstrip("\r\n").split(" ")[2]
        #fly1 = fly[2]
        
    if line.startswith(">"): 
        name = line[1:].rstrip("\r\n").split(" ")[1]
        #name1 = name[1]
        
        
    if line.startswith(" Identities"): 
        ident = line[1:].rstrip("\r\n").split(" ")[2, 6]
        #ident1 = ident[2]
        #ident2 = ident[6]
        #output.append(ident)
        print fly, name, ident
        #strip ("Identities = ", "Gap = ")
    
    if line == "":
        break
        
  


#print name, ident