from nltk import pos_tag
import pandas as pd
import numpy as np

df_csv1 = pd.read_csv('meanslpitsample.csv')# Meaning of level mentioned
df= pd.DataFrame(columns=['Onset word for second letter'])
ftCol = df_csv1.iloc[:, 0].values
final=[]
def sppos(mean):
    print(mean)
    result=[]
    print(mean)
    text =mean.split()
    #print("After Split:",text)
    tokens_tag = pos_tag(text)
    #print("After Token:",tokens_tag)
    for i in tokens_tag:
        if i[1] == 'NN' or i[1] == 'NNS' or i[1] == 'NNPS' or i[1] == 'NNP' or i[1]=='VBP' or i[1]=='VBN' or i[1]=='VBZ' or i[1] == 'VBG' or i[1]=='VBD' or i[1]=='JJ' or i[1]=='JJR' or i[1] == 'JJS':
            result.append(i[0])
    #print(result)
    return result

for j in ftCol:
    final.append(sppos(j))
for k in final:
    print(k)
    df = pd.DataFrame([k])
    df.to_csv('msr.csv', index=False, mode= 'a', header=False)

