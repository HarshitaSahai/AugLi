import pandas as pd
import re

df_csv1 = pd.read_csv('readalouddata.csv',encoding='cp1252',sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
xml = df_csv1.iloc[0:2,4].values 

indexArray = []
wordArray = []
valueFinal= []
wordFinal = []
#sentence= '<instance>teamwork simply stated it is less me and more we</instance><input mode="speech" intelligibility="1">teamwork</input>'

# Fetaching the sentence for words
def createSentence(start,sentence):
    index = start
    while(sentence[index] != '<'):
            newWord = " "
            while(sentence[index] != " " or sentence[index] != '<'):
                
                if(sentence[index] == '<' ):
                    break
               
                newWord = newWord + str(sentence[index])
                index = index + 1
            # print(newWord)
            # Removing space
            wordArray = re.split('\s+', newWord) 
            print(wordArray)
            # Words in parse
            for i in wordArray[1:]:
                wordFinal.append(i)

# Starting index of sentence     
def occurSentence(word,sentence):

    index = 0
    
    while index < len(sentence):
        index = sentence.find(word, index)
        if index == -1:
            break
        #print('{} found at {}'.format(word, index))
        index = index + 10
        createSentence(index,sentence)
    
# Storing index for intelligibility= 
def occurCount(word,sentence):

    index = 0
    while index < len(sentence):
        index = sentence.find(word, index)
        if index == -1:
            break
        print('{} found at {}'.format(word, index))
        indexArray.append(sentence[index+17])
        print(sentence[index+17])
        index += len(word)

for i in xml:
    
    # new for every entry
    indexArray = [] 
    wordArray = []
    valueFinal = []
    wordFinal
    occurSentence("<instance>",i)
    occurCount("intelligibility=",i)
    for i in indexArray[1:]:
         valueFinal.append(i)
    print(valueFinal)
    








