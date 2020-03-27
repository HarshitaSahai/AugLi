from nltk.corpus import words
import pandas as pd
import numpy as np
df_csv = pd.read_csv('level6 + syllable + word filter + word family.csv')
ftCol = df_csv.iloc[:, 0].values

def onset(word):
    result=[]

    a = word
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    post_string = a[1:]
    final = [letter+post_string for letter in alphabet]


    setofwords = set(words.words())
    for i in final:
         if i in setofwords:
               result.append(i)
               
               
    return result
        

print(ftCol)

array=[]
for j in ftCol:
    array.append(onset(j))
print(array)

df_csv = pd.DataFrame(columns=['Onset for first letter'])
for i in range(len(array)):
     df_csv.loc[i] = [array[i]]
df_csv.to_csv('onedata.csv', index=False, mode= 'w')

