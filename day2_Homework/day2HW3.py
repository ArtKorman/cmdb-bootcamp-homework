#! /usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

cufflinks_output10 = "/Users/cmdb/data/results/SRR072905_clout/genes.fpkm_tracking"
cufflinks_output11 = "/Users/cmdb/data/results/SRR072906_clout/genes.fpkm_tracking"
cufflinks_output12 = "/Users/cmdb/data/results/SRR072907_clout/genes.fpkm_tracking"
cufflinks_output13 = "/Users/cmdb/data/results/SRR072908_clout/genes.fpkm_tracking"
cufflinks_output14A = "/Users/cmdb/data/results/SRR072909_clout/genes.fpkm_tracking"
cufflinks_output14B = "/Users/cmdb/data/results/SRR072911_clout/genes.fpkm_tracking"
cufflinks_output14C = "/Users/cmdb/data/results/SRR072913_clout/genes.fpkm_tracking"
cufflinks_output14D = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

df10 = cufflinks_output10
df11 = cufflinks_output11
df12 = cufflinks_output12
df13 = cufflinks_output13
df14 = cufflinks_output14A
df15 = cufflinks_output14B
df16 = cufflinks_output14C
df17 = cufflinks_output14D

df_all=[df10, df11, df12, df13, df14, df15, df16, df17]

FPKM_level = []
for i in df_all:
    f = open (i)
    while True:
        line = f.readline()
        if "Sxl" in line:
            fields = line.rstrip("\r\n").split("\t")
            FPKM_level.append(fields[9])
            break
            
plt.figure()
plt.plot(FPKM_level)
plt.savefig("FPKM_levels.png")
            


    