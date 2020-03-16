import pandas as pd
import numpy as np
from colorama import Fore

x = 2
df_csv = pd.read_csv('msr5c.csv')# Meaning of level mentioned
ftCol = df_csv.iloc[:, 0].values
df = pd.read_csv('diffleveldata.csv')
ftCol1 = df.iloc[:,0].values
ftCol2 = df.iloc[:,1].values
ftCol3 = df.iloc[:,2].values
ftCol4 = df.iloc[:,3].values
ftCol5 = df.iloc[:,4].values
ftCol6 = df.iloc[:,5].values
def search(word):
    #print(word)
   
    res = 0
    for j in ftCol1:
        #print(j)
        if(word.find(j) != -1):
            res = 1
    for j in ftCol2:
        #print(j)
        if(word.find(j) != -1):
            res = 2
    for j in ftCol3:
        #print(j)
        if(word.find(j) != -1):
            res = 3
    for j in ftCol4:
        #print(j)
        if(word.find(j) != -1):
            res = 4
    for j in ftCol5:
        #print(j)
        if(word.find(j) != -1):
            res = 5
    for j in ftCol6:
        #print(j)
        if(word.find(j) != -1):
            res = 6
    if word == 'BLANK':
        res = "Blank"
  
    return res
        


for i in ftCol:
    result=[]
    print(i)
    result.append(search(i))
    print(result)
    dfr = pd.DataFrame([result])
    dfw = pd.DataFrame([i])
    x += 1
    print(x)
    dfr.to_csv('level8.csv', index=False, mode= 'a', header=False)
    dfw.to_csv('tryword1.csv', index=False, mode= 'a', header=False)



