#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it
"""
import sys
from fasta import FASTAReader
        
reader = FASTAReader(sys.stdin)

ref = []

for sid, sequence in reader:
    ref.append((len(sequence), sequence))

ref2 = []
ref2 = sorted(ref, reverse=True)[0:100]
#ref3 = list(ref2)
#start = ref2.strip("\r\n").split("ATG")

print ref2