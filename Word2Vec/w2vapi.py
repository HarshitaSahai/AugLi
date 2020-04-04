import pandas as pd
import numpy as np
import csv
import collections
from datamuse import datamuse

dataset = pd.read_csv('w2veg.csv')
ftCol = dataset.iloc[:, 0].values

api = datamuse.Datamuse()

resa=[]
var = len(ftCol)
for i in ftCol:
    print(i)
    res = api.words(rel_spc=i, max=5)
    print(res)
    resa.append(res)

df = pd.DataFrame(resa)


dataset = pd.DataFrame(columns=['Kind of'])
for i in range(var):
     dataset.loc[i] = [resa[i]]
dataset.to_csv('w2vreskindof.csv', index=False, mode= 'w')

