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

#print sorted(ref, reverse=True)[0:100]
ref2 = []
ref2 = sorted(ref, reverse=True)[0:100]
#ref3 = list(ref2)
#start = ref2.strip("\r\n").split("ATG")

start = "ATG"

codon_table = {
    'A': ('GCT', 'GCC', 'GCA', 'GCG'),
    'C': ('TGT', 'TGC'),
    'D': ('GAT', 'GAC'),
    'E': ('GAA', 'GAG'),
    'F': ('TTT', 'TTC'),
    'G': ('GGT', 'GGC', 'GGA', 'GGG'),
    'I': ('ATT', 'ATC', 'ATA'),
    'H': ('CAT', 'CAC'),
    'K': ('AAA', 'AAG'),
    'L': ('TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'),
    'M': ('ATG',),
    'N': ('AAT', 'AAC'),
    'P': ('CCT', 'CCC', 'CCA', 'CCG'),
    'Q': ('CAA', 'CAG'),
    'R': ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
    'S': ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'),
    'T': ('ACT', 'ACC', 'ACA', 'ACG'),
    'V': ('GTT', 'GTC', 'GTA', 'GTG'),
    'W': ('TGG',),
    'Y': ('TAT', 'TAC'),
    '*': ('TAA', 'TAG', 'TGA'),
}

ref2.rstrip("\r\n").split("ATG", ("TGA", "TAG", "TAA"))

print ref2
