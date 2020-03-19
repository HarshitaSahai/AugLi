import numpy
import pandas as pd
from nltk.corpus import stopwords

from nltk import pos_tag

df_csvw = pd.read_csv('lrlr.csv')


def lr(word,string):
    print(word)
    print(string)
    i = 0
    string.lower()
    words = list(string.split(' ')) # converting string into list
    arr = [] #array w/o stopwords
    farr=[] #array w/o stopwords + proper noun
    
    j=0

    english_stops = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"] # gathering stop words
    for i in words: # appending array with list in string w/o stopwords
        if i not in english_stops:
            arr.append(i)
    print(arr) # printing array w/o stopwords
    tokens_tag = pos_tag(arr)
    for i in tokens_tag: # appending array with list in string w/o proper noun
        if i[1]!=  'NNP':
            farr.append(i[0])
    print(farr) # printing array w/o stopwords and proper noun
        
    try:
        sindex = farr.index(word) # finding index of word
        try:#checking if left word present
            lindex = sindex - 1 # left word index
            lword = farr[lindex] # left word
            dfl = pd.DataFrame([lword])
            dfl.to_csv('llist.csv', index=False, mode= 'a', header=False)
            try: # checking if right word
                rindex = sindex + 1 # right word index
                rword = farr[rindex] # right word
                
                dfr = pd.DataFrame([rword])
                
                dfr.to_csv('rlist.csv', index=False, mode= 'a', header=False)
            except: # no right word
                rword = "No right word"
                dfr = pd.DataFrame([rword])
                dfr.to_csv('rlist.csv', index=False, mode= 'a', header=False)
        except: # no left word
                # as soon as adding .csv append 
                print('fm')
                
            
        
    except: # no word present
            print('Enter exception word')
            j += 1
            try:
                print('enter try ')
                for i in range(0,2):
                    if j == 1:
                        print('adding ed')
                        lr(word+'ed',string)
                        
                    elif j == 2:
                        print('adding ing')
                        lr(word+'ing',string)
                        
                    break
            except:
                    lword="No word found"
                    rword = "No word found"
                    dfl = pd.DataFrame([lword])
                    dfr = pd.DataFrame([rword])
                    dfl.to_csv('llist.csv', index=False, mode= 'a', header=False)
                    dfr.to_csv('rlist.csv', index=False, mode= 'a', header=False)
                    
            

           
for index,row in df_csvw.iterrows():
    i=row['Word']
    j = row['Meaning']
    lr(i,j)
        
    
