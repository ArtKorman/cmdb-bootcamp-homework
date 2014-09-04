#! /usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

cufflinks_output = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
cufflinks_output2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

df = pd.read_table( cufflinks_output )
df2 = pd.read_table( cufflinks_output2 )

#Male Data
top = df.sort("FPKM", ascending=False)["FPKM"] [0:5200]
middle = df.sort("FPKM", ascending=False) ["FPKM"] [5200:10400]
bottom = df.sort("FPKM", ascending=False) ["FPKM"] [10400:]

data_set = [top, middle, bottom]
fig = plt.figure
plt.boxplot(data_set)
plt.savefig("Box_Male")

#Female Data
top2 = df2.sort("FPKM", ascending=False)["FPKM"] [0:5200]
middle2 = df2.sort("FPKM", ascending=False) ["FPKM"] [5200:10400]
bottom2 = df2.sort("FPKM", ascending=False) ["FPKM"] [10400:]

data_set2 = [top2, middle2, bottom2]
fig = plt.figure
plt.boxplot(data_set2)
plt.savefig("Box_Female")