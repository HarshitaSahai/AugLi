from nltk.corpus import words
import pandas as pd
import numpy as np
df_csv3 = pd.read_csv('onsetsample.csv')
df_csv2 = pd.read_csv('onsetsample.csv')
df_csv1 = pd.read_csv('onsetsample.csv')

df= pd.DataFrame(columns=['Onset word for second letter'])
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



sarray1word2=[]
for j in ftCol:
    print(j)
    add = []
    resultn=[]
    sflatList1 = []
    oflatList2=[]
    sarray1word2 =[]
    oarray2word1=[]
    first= onset(j)
    second = onset2word(j)
   
    for i in first:
        
        oarray2word1.append(onset2word(i))
        oflatList2 = [ item for elem in oarray2word1 for item in elem]
       
    for k in second:
        
        sarray1word2.append(onset(k))
        sflatList1 = [ item for elem in sarray1word2 for item in elem]
       
        
    add = sflatList1 + oflatList2 
    for i in add:
        if i not in resultn:
        
            resultn.append(i)
    print(resultn)
    df = pd.DataFrame([resultn])
    df.to_csv('osw.csv', index=False, mode= 'a', header=False,sep=';')



