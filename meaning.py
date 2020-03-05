from PyDictionary import PyDictionary
import pandas as pd
import numpy as np
import csv


dataset = pd.read_csv('level1 + syllable + word filter + word family.csv')
ftCol = dataset.iloc[:, 0].values


var = len(ftCol)

def meaningg(word):
   
    #print(word)
    return print(PyDictionary.meaning(word))

print(ftCol)
array = []
array.append([meaningg(i) for i in ftCol])
print(array)

list1 = {'Names':array}
#print(list1)
df = pd.DataFrame(list1)
#f_csv = pd.read_csv('level1 + syllable + word filter + word family.csv')

df_csv = pd.DataFrame(columns=['Meaning'])
for i in range(var):
     df_csv.loc[i] = [array[i][i]]
df_csv.to_csv('new.csv', index=False, mode= 'w')
