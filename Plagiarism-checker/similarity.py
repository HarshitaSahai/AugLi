import nltk
import websearch
from difflib import SequenceMatcher
import pandas as pd
import csv
import numpy as np

nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(nltk.corpus.stopwords.words('english')) 

df_csv1 = pd.read_csv('argument.csv',encoding='cp1252')
arg = df_csv1.iloc[0:275,0].values
ans = []
links = []

def purifyText(string):
    words = nltk.word_tokenize(string)
    return (" ".join([word for word in words if word not in stop_words]))

def webVerify(string, results_per_sentence):
    sentences = nltk.sent_tokenize(string)
    matching_sites = []
    for url in websearch.searchBing(query=string, num=results_per_sentence):
        matching_sites.append(url)
    for sentence in sentences:
        for url in websearch.searchBing(query = sentence, num = results_per_sentence):
            matching_sites.append(url)

    return (list(set(matching_sites)))

def similarity(str1, str2):
    return (SequenceMatcher(None,str1,str2).ratio())*100

def report(text):

    matching_sites = webVerify(purifyText(text), 2)
    matches = {}

    for i in range(len(matching_sites)):
        matches[matching_sites[i]] = similarity(text, websearch.extractText(matching_sites[i]))

    matches = {k: v for k, v in sorted(matches.items(), key=lambda item: item[1], reverse=True)}
    flag = False
    print(matches)
    # If any link present
    if matches:
        # appending link + % 
        res = matches.items()
        data = list(res)
        links.append(data)
        # If greater than 30 then true
        for i in matches:
            if(matches[i] >= 30):
                ans.append('1')
                flag = True
                break
    # no link therefore 0 
    else:
        ans.append('0')
        return matches
    # if no link with >= 30 %
    if flag == False:
        ans.append('0')


for i in arg:
    print(i)
    report(i)

df_csv = pd.DataFrame(columns=['Argument'])
df_csv1 = pd.DataFrame(columns=['Argument'])
k = 0
print(ans)
print(links)

# Appending 0 or 1
for i in ans:
    
    df_csv.loc[k] = i 
    k = k + 1

# Appending links with %
for i in links:
    df_csv1 = df_csv1.append(i)
    

    
df_csv.to_csv('sampleplargresult.csv', index=False, mode= 'w') # Sheeting have the required list
df_csv1.to_csv('sampleplinks.csv', index=False, mode= 'w') # Sheeting have the required list
