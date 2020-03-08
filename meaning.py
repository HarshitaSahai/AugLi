from PyDictionary import PyDictionary
import pandas as pd
import numpy as np
import csv

df_csv = pd.read_csv('meantest.csv')
ftCol = df_csv.iloc[:, 0].values


var = len(ftCol)

def meaningg(word):
   
    #print(word)

    return PyDictionary.meaning(word)

print(ftCol)
array = []

for i in ftCol:
    ans = meaningg(i)
    array.append(ans) 
print(array)
print(len(array))

df_csv = pd.DataFrame(columns=['Meaning'])
for i in range(len(array)):
     df_csv.loc[i] = [array[i]]
df_csv.to_csv('newmeanresult.csv', index=False, mode= 'w')
