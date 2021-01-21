import nltk
import websearch
from difflib import SequenceMatcher
import pandas as pd

nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(nltk.corpus.stopwords.words('english')) 


df_csv1 = pd.read_csv('argument.csv',encoding='cp1252')
arg = df_csv1.iloc[106:200].values

ans = []

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
    for i in matches:
        print(matches[i])
        if matches[i] >=20 :
            ans.append("True")
            print(i)
            flag = True
        if flag:3
            break

    if flag == False :  
        ans.append("False")
    
    print(ans)


for i in arg:
    print(i)
    report(str(i))

df_csv = pd.DataFrame(columns=['Argument'])
k = 0
for i in ans:
    df_csv.loc[k] = i 
    k = k + 1
df_csv.to_csv('Result.csv', index=False, mode= 'w') # Sheeting have the required list


