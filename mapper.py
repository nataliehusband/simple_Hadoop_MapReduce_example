#!/usr/bin/env python
import sys
import collections
# import stopwords
from sklearn.feature_extraction import stop_words
stops = set(stop_words.ENGLISH_STOP_WORDS)
# define punctuation
#punctuations = set('''!()-[]{};:'"\,<>./?@#$%^&*_~''')

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words; splits on any whitespace
    words = line.split()
    #for x in words:
        #if x in punctuations:
            #words = words.remove(x)

    # remove stopwords
    for word in words:
        if word not in stops:
            print ('%s\t%s')%(word, '1')
