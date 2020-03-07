from PyDictionary import PyDictionary
import pandas as pd
import numpy as np
import csv

df_csv = pd.read_csv('meantest.csv')
ftCol = df_csv.iloc[:, 0].values


var = len(ftCol)

def meaningg(word):
   
    #=print(word)

    return PyDictionary.meaning(word)

print(ftCol)
array = []
for j in range(var):
    print("1")
    array.append([meaningg(i) for i in ftCol])
print(array)
print(len(array))

df_csv = pd.DataFrame(columns=['Meaning'])
for i in range(var):
     df_csv.loc[i] = [array[i][i]]
df_csv.to_csv('newmeanresult.csv', index=False, mode= 'w')
