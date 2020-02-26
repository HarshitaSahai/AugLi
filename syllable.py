import pandas as pd
import numpy as np
import csv

import collections





dataset = pd.read_csv('sample.csv')
ftCol = dataset.iloc[:, 0].values




def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

numpyarray = np.empty(3767)

for i in range(3767):
    numpyarray=[syllable_count(i) for i in ftCol]
print(numpyarray)

