# Joshua Steinberg
import os
import sys
import re
import numpy
import nltk
import nltk.corpus
import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# grab all book files from directory
loc = os.listdir("books")

#create stats file for each thing
stats = open("csv/stats.txt","w")


for file in loc: # loop through all files in the directory
    print("Doing analysis on {0}".format(file))
    stats.write(file + "\n")
    text = open("books/" + file,encoding="utf8")

    # create csv file with same name as the book
    # add headers
    file = csv.writer(open("csv/" + file[:-3] + "csv","w"))
    file.writerow(["word","frequency"])

    # lower all text to make it standard
    text_actual = text.read().lower()

    # get rid of punctuation
    # we do not care about how many "." are used in the text
    nopunc = re.sub("[^a-zA-Z0-9\s]+", " ",text_actual)

    # tokenize items
    tokens = word_tokenize(nopunc)

    # get rid of stop words
    # and, the, or, etc do not provide anything to us
    stop_words = set(stopwords.words('english'))
    cleantokens = [words for words in tokens if not words in stop_words]
    stats.write("Token count before cleaning: {0}\nToken count after cleaning: {1}\n".format(len(tokens),len(cleantokens)))

    # we can tag the words left then
    # tokens_tagged = nltk.pos_tag(cleantokens)

    fdist = FreqDist(cleantokens)

    # get top 1000 most common words 
    topOnes = fdist.most_common(1000)
    
    for key, count in topOnes:
        file.writerow([key,count])

# do it all again in one text file to get a master list
print("Doing final analysis on all of the text files.")
alltext = ""
allfile = csv.writer(open("csv/alltext.csv","w"))
allfile.writerow(["word","frequency"])
stats.write("alltext.csv\n")

for file in loc:
    text = open("books/" + file,encoding="utf8")
    alltext = alltext + text.read().lower()

# same format as the loop above
nopunc = re.sub("[^a-zA-Z0-9\s]+", " ",alltext)
tokens = word_tokenize(nopunc)
stop_words = set(stopwords.words('english'))
cleantokens = [words for words in tokens if not words in stop_words]
stats.write("Token count before cleaning: {0}\nToken count after cleaning: {1}\n".format(len(tokens),len(cleantokens)))
fdist = FreqDist(cleantokens)
topOnes = fdist.most_common(1000)
    
for key, count in topOnes:
    allfile.writerow([key,count])