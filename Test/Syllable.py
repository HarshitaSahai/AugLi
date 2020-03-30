import pandas as pd
import numpy as np
import csv

import collections
dataset = pd.read_csv('level1sam.csv')
ftCol = dataset.iloc[:, 0].values


var = len(ftCol)

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
print(ftCol)
array = []

for j in range(var):
   array.append([syllable_count(i) for i in ftCol])
#print(array)

list1 = {'Names':array}
#print(list1)
df = pd.DataFrame(list1)
df_csv = pd.read_csv('level1 + syllable + word filter.csv')
#df_csv['syllable'] = df.Names  # changed here
#df_csv.to_csv('withsyllable.csv', index=False, mode= 'w')
df_csv = pd.DataFrame(columns=['Syllabel'])
for i in range(var):
     df_csv.loc[i] = [array[i][i]]
df_csv.to_csv('syllablemlll,ll,l.csv', index=False, mode= 'w')
