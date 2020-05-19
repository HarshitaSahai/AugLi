import string 
import pandas as pd
import numpy as np
import csv
import language_check
import collections
from nltk import pos_tag
from nltk.corpus import wordnet


dataset = pd.read_csv('sampleques.csv',encoding= 'Utf-8') # Reading the sheet with questions
ftCol = dataset.iloc[:, 0].values # Saving the question column in ftCol
tool = language_check.LanguageTool('en-US') # Will use the tool to corect speeling and grammar mistake 

conversation = ["Thank you so much","Do not mention","Thanks a lot","Thanks a ton","Hey thank you","Hey thank you so much","Hey thanks a lot","Thank you for your help","Thank you for the answer"] # For identifying coutous or starting/ending of conversation level 1.1
ques = ["Where","where","what","What","how","How","Where","where","What","what","when","When","Did","did","who","Who","whom","Whom","Why","why","could","Could","Will this","How","how","Tell","tell","Can","can","if","If"] # List of question word which help in level 2 and level 5
mean = ["Mean","Meaning","Means","Meant","Meaned","meaned","meant","means","meaning","mean","form","Form"] # List of word for helping in level 3.1
qword = ["what","when","did","What","When","Did","could","Could","How","how"] #Question word for level  3.2  
opinionq = ["what","why","did","if","else","what if","why not","What","Why","Did","If","Else","What if","Why not"] #Question words for level 4

# The below code will help in forming an array of words related to level 4 i.e representing an opinion or suggesting something along with question
synonyms = [] 
synonyms1 = []
synonyms2 = []
opinionsy = []
capw = []

for syn in wordnet.synsets("opinion"): # Finding synonyms of opinion
    for lm in syn.lemmas():
             synonyms.append(lm.name())
             opinionsy.append(lm.name())

for i in synonyms:
    for syn in wordnet.synsets(i):
        for lm in syn.lemmas():
                opinionsy.append(lm.name())

for syn in wordnet.synsets("despite"): # Finding synonyms of despite
    for lm in syn.lemmas():
            
             synonyms1.append(lm.name())
             opinionsy.append(lm.name())
    
for i in synonyms1:
    for syn in wordnet.synsets(i):
        for lm in syn.lemmas():
                opinionsy.append(lm.name())
             

for syn in wordnet.synsets("response"):# Finding synonyms of response
    for lm in syn.lemmas():
             
             synonyms2.append(lm.name())
             opinionsy.append(lm.name())
    
for i in synonyms2:
    for syn in wordnet.synsets(i):
        for lm in syn.lemmas():
                opinionsy.append(lm.name())

opinionsy.append("should") # Adding should
opinionsy.append("if") # Adding if

#Changing first letter of words added in opinionsyn 
for i in opinionsy: 
    cw = i.title()
    capw.append(cw)

for i in capw:
    opinionsy.append(i)



resa = [ ] # Array storing level of every question in sheet or ftCol


#checking the number of words in sentence
def lengthofsentence(test_string):
    
    #print(test_string)
    res = sum([i.strip(string.punctuation).isalpha() for i in test_string.split()]) # Calculation takes place
    if res == 1 or res == 2 or res == 0: # If number of words < 3 then level = 0 i.e level 1.1 and level 1.2
        res = 0
        #print("RES 0")
        resa.append(res) # appending 0 in result array 
    else:
        checksen(test_string)


#Checking spelling and grammar 
def checksen(test_string):
    
    #print(test_string)
    matches = tool.check(test_string) # Identify the errors in sentence
    if len(matches) != 0:
        cor = language_check.correct(test_string, matches) # perform correction
        test_string=cor
    #print(test_string) 
    checkcourtesy(test_string) # Will pass to checkcourtesy to check level 1.1

#Checking level 1.1
def checkcourtesy(test_string):

    flag = 0
    res = 1
    for i in conversation:  # Using array conversation
        if (i.find(test_string) == -1):  # Finding if any i in conversation is equal to test_string if yea then level 1 
            flag = 1  
    if flag == 1:
        #print("RES 1")
        resa.append(res) # Appeding 1 in result  array
    else:   
        ss(test_string) # Will pass to simple sentence (ss) function

#level 1.2  + 1.3 
def ss(test_string):

    res = 1
    noss = -1
    flaga = 0
    flagq = 0
   
    test_stringn = test_string.split() # Spliting string into sepreate words 
    tokens_tag = pos_tag(test_string) # assiging POS tags to each word in string

    for i in tokens_tag:
       
        if i[1] == "JJ" or i[1] == "JJR" or i[1] == "JJS" : # Finding if adjective is present
            flaga = 1
   
    for i in test_stringn:
        for j in ques: # Finding if question words in ques array are present 
            if i == j:
                flagq = 1
           

    if flagq == 1 and flaga == 1: # If both question word and adjective are present then will further consider
        findpronoun(test_string)  # Passing to find pronoun
    elif flaga == 1: # If only adjective is present
        
        resa.append(res) # Appending 1 in result array
    else: # if no adjective present but question word present
        findpronoun(test_string)  # Passing to find pronoun

        

#Checking for level 2 checking pronoun and ques word
def findpronoun(test_string):
    
    
    npro = 0
    qpro = 0
    res = 2
    exp = 6
    np = 0
    flagif2 = 0
    test_stringn = test_string.split() # Spliting string into sepreate words 
    tokens_tag = pos_tag(test_stringn) #assiging POS tags to each word in string
    for i in tokens_tag:
        if i[1] == "PRP" or i[1] == "PRP$": # If personal or possessive pronoun present
            npro = npro + 1
        if i[1] == "WP" or i[1] == "WP$": # If WH-Pronoun present 
            qpro = qpro + 1
        if i[1] == "NNP" or i[1] == "NNPS": # If proper noun singular + plural
            np = np + 1
    
    if  np > 0: # if noun present 
        findmean(test_string) # pass string to findmean
    elif npro > 0: # if only pronoun are present
  
        resa.append(res) # Appending 2 in result array
    elif qpro > 0: # If wh-pronoun present
    
        findmean(test_string) # pass string to find mean
    else :
        findmean(test_string) #If question word are present then move to find mean
    

#Checking for level 3.1
def findmean(test_string):
    res = 3
    flagm = 0

    test_stringn = test_string.split()# Spliting string into sepreate words 
    tokens_tag = pos_tag(test_stringn) #assiging POS tags to each word in string
  
    for i in test_stringn:
       for j in mean: # Finding if any word in string matches to words in mean array
            if i== j : # If true
                for i in tokens_tag: # Will check POS Tags of word in string
                    if i[1] == "NN" or i[1] == "NNS" : # If noun present 
                        flagm = flagm + 1 # Incrementing flagm 
       
    if flagm > 0: # If flagm > 0 then the string belongs to level 3
        resa.append(res) # Appending 3 in result array
    else:
        findqpast(test_string)# Passing the string to findqpast function

#Checking for level 3.2
def findqpast(test_string):
    res = 3
    flagqw = 0
    flagvp = 0
    flag3 = 0
    test_stringn = test_string.split()# Spliting string into sepreate words 
    tokens_tag = pos_tag(test_stringn) #assiging POS tags to each word in string
    for i in test_stringn:
        for j in qword: # Comparing word in string to question word in qword
            if i == j: # If present 
                flagqw = flagqw + 1 # Incrementing the flagqw 
    for i in tokens_tag: # Analyzing tags of words in string 
        if i[1] == "VBD"or i[1] == "VBN": # if verb present 
            flagvp = flagvp + 1 # flagvp == 1
        
    if flagvp  > 0  and flagqw > 0: #if both verb and qword present in string
        resa.append(res) # Appending 3 in result array
    elif flagqw > 0:
        findopinion(test_string,flag3 = 1) #If only question word are present then pass string + flag3 = 1 as there can be a possibility that it belongs to level 3
    else:
        findopinion(test_string, flag3 = 0) #If not question word present then further process it with flag3 = 0 

#Checking for level 4 
def findopinion(test_string,flag3): 
    res = 4
    flagq = 0 
    flago = 0
    test_stringn = test_string.split() # Spliting string into sepreate words
    for i in test_stringn:
        for j in opinionq: # Checking if any word in opinionw array present 
            if i == j: # If yes
                flagq = 1 # Declare flagq == 1
       
    for i in test_stringn:
        for j in opinionsy: # Checking word in opinionsy array 
            if i == j: # If there is a match 
                flago = 1 # flago =1
       
    if flago == 1: # If flago is 1 then chances of level 4 increase
        findfuture(test_string,flag3,flag4 = 1) # Passing string and flag4 == 1 to findfuture
    else:
        findfuture(test_string,flag3,flag4 = 0) # Passing string and flag4 == 0 to findfuture

# Checking for level 5 
def findfuture(test_string,flag3,flag4):
    
    flagq = 0
    flaga = 0
    flagm = 0
    res = 5
    res4 = 4
    res3 = 3
    nocond = -1
    test_stringn = test_string.split()# Spliting string into sepreate words 
    tokens_tag = pos_tag(test_stringn) #assiging POS tags to each word in string
    for i in tokens_tag: # Analyzing array with tokens 
        if i[1] == "JJ" or i[1] == "JJR" or i[1] == "JJS" : # If word in string are adjective
            flaga = 1 # Declare flaga = 1
        if i[1] == " MD": # If word in string modal
            flagm = 1 # Declare flagm = 1
    for i in ques: # Analyzing question word in ques in array
        for j in test_stringn: # Checking word in string
            if i == j: # If same
                flagq = 1 # Declare flagq = 1

    if flagq == 1: # When flagq is 1 
        if flaga == 1 and flagm == 1: # if both adjective and modal are present
            resa.append(res) # Appending 5 in result array
        elif flag4 == 1:# If above condition not satisfied then checking if level 4 conditions are valid if yes then appending 4 in result array
            resa.append(res4) 
        elif flaga == 1 or flagm == 1: # If either of adjective or modal are present then appending 5 in result array
            resa.append(res)    
        elif flag3 == 1: # If above condition not satisfied then checking if level 3 conditions are valid if yes then appending 3 in result array
            resa.append(res3)
        else:
            resa.append(res)  #If level 3 and level 4 not valid then appending 5 in result array 
    else:
        if flag3 == 1: # If level 3 is getting sattisfied appending 3 in result array
            resa.append(res3)
        elif flag4 == 1: # If level 4 is getting satisfied appending 4 in result array 
            resa.append(res4)
        else:
            resa.append(nocond) # All the levels are compared if not yet appended then no level is satisfied append -1 in array 

var = len(ftCol) # Finfding number of questions



for i in ftCol: # Identifying of level starts

    lengthofsentence(i) # Passing the ith entry
    
'''
Used to print array of list
for i in resa:
    print(i) 
'''


df_csv = pd.read_csv('sampleques.csv',encoding= 'Utf-8') # Readinf question sheet again

df_csv = pd.DataFrame(columns=['Question Level']) # Creating a column which will store level of each question 
k = 0 
for i in resa:
     df_csv.loc[k] = i 
     k = k + 1
df_csv.to_csv('smaplelevelq.csv', index=False, mode= 'w') # Sheeting have the required ;ist
