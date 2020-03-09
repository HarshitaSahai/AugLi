from nltk.corpus import words
import pandas as pd
import numpy as np
df_csv1 = pd.read_csv('onsetsample.csv')
df_csv2 = pd.read_csv('onsetsample.csv')
df_csv3 = pd.read_csv('onsetsample.csv')
ftCol = df_csv1.iloc[:, 0].values
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
def onset2word(word):
    result = []
    a = word
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    post_string1 = a[0]
    post_string2 = a[2:]
    final2 = [post_string1+letter+post_string2 for letter in alphabet]
    setofwords = set(words.words())
    for i in final2:
         if i in setofwords:
              result.append(i)     
    return result
        

print(ftCol)
array2word2=[]
add=[]
resultn=[]
array1word2=[]
for j in ftCol:
    resultn.append('[')
    first= onset(j)
    second = onset2word(j)
    #print(first)
    #print(array1word)
    for i in first:
        #for k in i:
        array2word2.append(onset2word(i))
        array1word2.append(onset(i))
        flatList1 = [ item for elem in array1word2 for item in elem]
        #print(flatList1)
        flatList2 = [ item for elem in array2word2 for item in elem]
        #print(flatList2)
        
        add = flatList1 + flatList2 
        for i in add:
            if i not in resultn:
                resultn.append(i)
    resultn.append(']')
print(resultn)

#print(array2word2)
#print(array1word2)
#flatList1 = [ item for elem in array1word2 for item in elem]
#print(flatList1)
#flatList2 = [ item for elem in array2word2 for item in elem]
#print(flatList2)
            
#in_first = set(flatList1)
#in_second = set(flatList2)

#in_second_but_not_in_first = in_second - in_first

#result = flatList1 + list(in_second_but_not_in_first)

#print( result )



"""df_csv1 = pd.DataFrame(columns=['Onset count for first letter'])
for i in range(len(array1c)):
     df_csv1.loc[i] = [array1c[i]]"""
df_csv2 = pd.DataFrame(columns=['Onset word for second letter'])
for j in range(len(resultn)):    
     df_csv2.loc[j] = [resultn[j]]
"""df_csv3 = pd.DataFrame(columns=['Onset count for second letter'])
for k in range(len(array2c)):    
     df_csv3.loc[k] = [array2c[k]]"""
     
df_csv2.to_csv('oc10.csv', index=False, mode= 'w')
"""df_csv2.to_csv('ow2.csv', index=False, mode= 'w')
df_csv3.to_csv('oc2.csv', index=False, mode= 'w')"""

