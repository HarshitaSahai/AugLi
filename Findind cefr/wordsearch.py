from nltk.corpus import words
import pandas as pd
import numpy as np
df_csv1 = pd.read_csv('Auglidb.csv')# Meaning of level mentioned
ftCol = df_csv1.iloc[:,1].values
cefr = df_csv1.iloc[:,8].values
df_csv2 = pd.read_csv('wordsfounddb.csv',encoding='windows-1252')# Extracted 5 words from each level
ftCol2 = df_csv2.iloc[:,0].values
#cefr = df_csv1.iloc[:8].values

cefra=[]
for i in cefr:
    cefra.append(i)
#print(cefra)
#print(len(cefra))
#var = ftCol
#print(ftCol2)
aw=[]
array=[]
for l in ftCol2:
    print(l)
   # print(l)
    c = -1
   
    for j in ftCol:
     
     c= c+1
     if(l==j): 
        aw.append(l)
        array.append(cefr[c])
        print (j)
      
           
        
df_csv = pd.read_csv('wordsfounddb.csv',encoding='windows-1252')# Extracted 5 words from each level


for i in range(len(aw)):
     df_csv.loc[i] = [aw[i]]
df_csv.to_csv('word.csv', index=False, mode= 'w')       
for i in range(len(array)):
     df_csv.loc[i] = [array[i]]
df_csv.to_csv('cefr.csv', index=False, mode= 'w')       
  
print(len(aw))
print(aw)
print(len(array))
print(array)
