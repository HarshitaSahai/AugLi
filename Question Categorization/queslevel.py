import string 
import pandas as pd
import numpy as np
import csv
import language_check
import collections
from nltk import pos_tag
from nltk.corpus import wordnet


dataset = pd.read_csv('sampleques.csv',encoding= 'Utf-8')
ftCol = dataset.iloc[:, 0].values
tool = language_check.LanguageTool('en-US')
#For level 1.0 not found any resource created a small list 
conversation = ["Thank you so much","Do not mention","Thanks a lot","Thanks a ton","Hey thank you","Hey thank you so much","Hey thanks a lot","Thank you for your help","Thank you for the answer"]
#for level 1.1 and 1.2
ques = ["Where","where","what","What","how","How","Where","where","What","what","when","When","Did","did","who","Who","whom","Whom","Why","why","could","Could","Will this","How","how","Tell","tell","Can","can","if","If"]
mean = ["Mean","Meaning","Means","Meant","Meaned","meaned","meant","means","meaning","mean","form","Form"]
qword = ["what","when","did","What","When","Did","could","Could","How","how"] #level  3.1 words 
opinionq = ["what","why","did","if","else","what if","why not","What","Why","Did","If","Else","What if","Why not"] #level 4
synonyms = []
synonyms1 = []
synonyms2 = []
opinionsy = []
capw = []

for syn in wordnet.synsets("opinion"):
    for lm in syn.lemmas():
             synonyms.append(lm.name())
             opinionsy.append(lm.name())

for i in synonyms:
    for syn in wordnet.synsets(i):
        for lm in syn.lemmas():
                opinionsy.append(lm.name())

for syn in wordnet.synsets("despite"):
    for lm in syn.lemmas():
            
             synonyms1.append(lm.name())
             opinionsy.append(lm.name())
    
for i in synonyms1:
    for syn in wordnet.synsets(i):
        for lm in syn.lemmas():
                opinionsy.append(lm.name())
             

for syn in wordnet.synsets("response"):
    for lm in syn.lemmas():
             
             synonyms2.append(lm.name())
             opinionsy.append(lm.name())
    
for i in synonyms2:
    for syn in wordnet.synsets(i):
        for lm in syn.lemmas():
                opinionsy.append(lm.name())

opinionsy.append("should")
opinionsy.append("if")

#First letter uppercase
for i in opinionsy:
    cw = i.title()
    capw.append(cw)

for i in capw:
    opinionsy.append(i)



resa = [ ] # Level classification


#checking the length and finding level 0.0 and level 0.1 
def lengthofsentence(test_string):
    
    print(test_string)
    
    res = sum([i.strip(string.punctuation).isalpha() for i in test_string.split()])
    if res == 1 or res == 2 or res == 0:
        res = 0
        #print("RES 0")
        resa.append(res)
    else:
        checksen(test_string)


#Checking if sentence okay or not 0.2
def checksen(test_string):
    
    #print(test_string)
    matches = tool.check(test_string)
    if len(matches) != 0:
        cor = language_check.correct(test_string, matches)
        test_string=cor
    print(test_string) #Will pass this only to other level as pass unable to reflect changes in sheet
    ss(test_string)

#level 1.0 
def checkcourtesy(test_string):

    flag = 0
    res = 1
    for i in conversation:
      
      
       if (i.find(test_string) == -1):   
    
            flag = 1  
       if flag == 1:
            break
    if flag == 1:
        #print("RES 1")
        resa.append(res)
    else:   
        ss(test_string)

#level 1.1  + 1.2 finding adjective and ques word
def ss(test_string):

   # print("1")
    res = 1
    noss = -1
    flaga = 0
    flagq = 0
   
    test_stringn = test_string.split()
    tokens_tag = pos_tag(test_string)

    for i in tokens_tag:
       
        if i[1] == "JJ" or i[1] == "JJR" or i[1] == "JJS" :
            flaga = 1
   
    for i in test_stringn:
        for j in ques:
            if i == j:
                flagq = 1
           

    if flagq == 1 and flaga == 1:
        findpronoun(test_string) 
    elif flaga == 1:
        #print("RES 1")
        resa.append(res)
    else:
        findpronoun(test_string)
        

#Checking for level 2.0 checking pronoun and ques word
def findpronoun(test_string):

   # print("2")
    test_stringn = test_string.split()
    #print(test_stringn)
    npro = 0
    qpro = 0
    res = 2
    exp = 6
    flagq =0
    np = 0
    flagif2 = 0
    #nocondn = -1
    tokens_tag = pos_tag(test_stringn)
    for i in tokens_tag:
        if i[1] == "PRP" or i[1] == "PRP$":
            npro = npro + 1
        if i[1] == "WP" or i[1] == "WP$":
            qpro = qpro + 1
        if i[1] == "NNP" or i[1] == "NNPS":
        
            np = np + 1
    for i in test_stringn:
        for j in ques:
            if i == j:
                flagq = 1
        if flagq == 1:
            break
    
    if  np > 0:
        findmean(test_string)
    elif npro > 0:
      #  print("RES 2")
        resa.append(res)
        
    elif qpro > 0:
      #  print("RES 2")
        findmean(test_string)
        
    else :
        findmean(test_string)

#Checking for level 3.0 
def findmean(test_string):
    res = 3
   # print("3")
    nocond = -1
    flagm = 0

    test_stringn = test_string.split()
    tokens_tag = pos_tag(test_stringn)
    for i in test_stringn:
    
        for j in mean:
            if i== j :
                for i in tokens_tag:
                    
                    if i[1] == "NN" or i[1] == "NNS" :
                        flagm = flagm + 1
       
    if flagm > 0:
      
      #  print("RES 3")
        resa.append(res)
    else:
        findqpast(test_string)

#Checking for level 3.1
def findqpast(test_string):
    res = 3
   # print("3")
    nocond = -1
    flagqw = 0
    flagvp = 0
    flag3 = 0
    test_stringn = test_string.split()
    tokens_tag = pos_tag(test_stringn)
    for i in test_stringn:
        for j in qword:
            if i == j:
                flagqw = flagqw + 1
        

    
    for i in tokens_tag:
        if i[1] == "VBD"or i[1] == "VBN":
            flagvp = 1
        if flagvp == 1:
            break
    if flagvp  > 0  and flagqw > 0:
      #  print("RES 3")
        resa.append(res)
    elif flagqw > 0:
        findopinion(test_string,flag3 = 1)
    else:
        findopinion(test_string, flag3 = 0)

#Level 4
def findopinion(test_string,flag3): 
    res = 4
    #print("4")
    oo = 1 #only opinion so in level1 
    flagq = 0 
    flago = 0
    nocond = -1
    test_stringn = test_string.split()
    for i in test_stringn:
     
        for j in opinionq:
            if i == j:
                flagq = 1
       
    for i in test_stringn:
        for j in opinionsy:
            if i == j:
                flago = 1
       
    
    if flago == 1:
        findfuture(test_string,flag3,flag4 = 1)
       

    else:
        findfuture(test_string,flag3,flag4 = 0)

# level 5 MD could would ... 
def findfuture(test_string,flag3,flag4):
    
    flagq = 0
    #print("5")
    flaga = 0
    flagm = 0
    res = 5
    res4 = 4
    res3 = 3
    nocond = -1
    test_stringn = test_string.split()
    tokens_tag = pos_tag(test_stringn)
    for i in tokens_tag:
        if i[1] == "JJ" or i[1] == "JJR" or i[1] == "JJS" :
            flaga = 1
        if i[1] == " MD":
            flagm = 1
    for i in ques:
        for j in test_stringn:
            if i == j:
                flagq = 1

    if flagq == 1:
    
        if flaga == 1 and flagm == 1:
         #   print("RES 5")
            resa.append(res)
        elif flag4 == 1:
         #   print("RES 4")
            resa.append(res4)
        elif flaga == 1 or flagm == 1:
         #   print("RES 5")
            resa.append(res)    
        elif flag3 == 1:
            resa.append(res3)
        else:
            resa.append(res)
    else:
        if flag3 == 1:
            resa.append(res3)
        elif flag4 == 1:
            resa.append(res4)
        else:
            resa.append(nocond)



    
    


var = len(ftCol)
# Passing enteries
for i in ftCol:

    lengthofsentence(i)

# Printing level
print("start")
for i in resa:
    print(i)

df_csv = pd.read_csv('sampleques.csv',encoding= 'Utf-8')

df_csv = pd.DataFrame(columns=['Question Level'])
k = 0
for i in resa:
     df_csv.loc[k] = i 
     k = k + 1
df_csv.to_csv('smaplelevelq.csv', index=False, mode= 'w')
