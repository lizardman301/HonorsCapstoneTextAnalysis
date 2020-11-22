import pandas as pd
import os
import csv
import matplotlib.pyplot as plt

#get csv file
loc = os.listdir("csv")

# generate for all csv files
for file in loc:
    # only do csv files
    if file.endswith(".csv"):
        print("Creating graph for {0}".format(file))
        # read first 20 entries from csv
        top20 = pd.read_csv("csv/"+file, nrows=20)
        # set size
        plt.figure(figsize=(10,6))
        # create bar chart
        plt.bar(x = top20['word'],height = top20['frequency'])
        # rotate words to fit
        plt.xticks(rotation = 35)
        # add file name as title
        plt.title(file, fontsize = 16)
        # save as image
        plt.savefig("imgs/"+file[:-3]+"png")
        # close
        plt.close()