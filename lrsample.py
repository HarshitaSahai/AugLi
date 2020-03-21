import numpy
import pandas as pd
from nltk.corpus import stopwords

from nltk import pos_tag

df_csvw = pd.read_csv('lrlrnew.csv',encoding='ISO-8859-1')
df_csvsuf = pd.read_csv('suffixes.csv')
suffix = df_csvsuf.iloc[:, 0].values
english_stops = ['a', 'about', 'above', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around', 'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'do', 'done', 'down', 'due', 'during', 'each', 'eg', 'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 'fifteen', 'fify', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'ie', 'i','I','if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'it', 'its', 'itself', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'she', 'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the', 'their', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', 'thick', 'thin', 'third', 'this', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves', 'the', 'A', 'About', 'Above', 'Above', 'Across', 'After', 'Afterwards', 'Again', 'Against', 'All', 'Almost', 'Alone', 'Along', 'Already', 'Also', 'Although', 'Always', 'Am', 'Among', 'Amongst', 'Amoungst', 'Amount', 'An', 'And', 'Another', 'Any', 'Anyhow', 'Anyone', 'Anything', 'Anyway', 'Anywhere', 'Are', 'Around', 'As', 'At', 'Back', 'Be', 'Became', 'Because', 'Become', 'Becomes', 'Becoming', 'Been', 'Before', 'Beforehand', 'Behind', 'Being', 'Below', 'Beside', 'Besides', 'Between', 'Beyond', 'Bill', 'Both', 'Bottom', 'But', 'By', 'Call', 'Can', 'Cannot', 'Cant', 'Co', 'Con', 'Could', 'Couldnt', 'Cry', 'De', 'Describe', 'Detail', 'Do', 'Done', 'Down', 'Due', 'During', 'Each', 'Eg', 'Eight', 'Either', 'Eleven', 'Else', 'Elsewhere', 'Empty', 'Enough', 'Etc', 'Even', 'Ever', 'Every', 'Everyone', 'Everything', 'Everywhere', 'Except', 'Few', 'Fifteen', 'Fify', 'Fill', 'Find', 'Fire', 'First', 'Five', 'For', 'Former', 'Formerly', 'Forty', 'Found', 'Four', 'From', 'Front', 'Full', 'Further', 'Get', 'Give', 'Go', 'Had', 'Has', 'Hasnt', 'Have', 'He', 'Hence', 'Her', 'Here', 'Hereafter', 'Hereby', 'Herein', 'Hereupon', 'Hers', 'Herself', 'Him', 'Himself', 'His', 'How', 'However', 'Hundred', 'Ie', 'If', 'In', 'Inc', 'Indeed', 'Interest', 'Into', 'Is', 'It', 'Its', 'Itself', 'Keep', 'Last', 'Latter', 'Latterly', 'Least', 'Less', 'Ltd', 'Made', 'Many', 'May', 'Me', 'Meanwhile', 'Might', 'Mill', 'Mine', 'More', 'Moreover', 'Most', 'Mostly', 'Move', 'Much', 'Must', 'My', 'Myself', 'Name', 'Namely', 'Neither', 'Never', 'Nevertheless', 'Next', 'Nine', 'No', 'Nobody', 'None', 'Noone', 'Nor', 'Not', 'Nothing', 'Now', 'Nowhere', 'Of', 'Off', 'Often', 'On', 'Once', 'One', 'Only', 'Onto', 'Or', 'Other', 'Others', 'Otherwise', 'Our', 'Ours', 'Ourselves', 'Out', 'Over', 'Own', 'Part', 'Per', 'Perhaps', 'Please', 'Put', 'Rather', 'Re', 'Same', 'See', 'Seem', 'Seemed', 'Seeming', 'Seems', 'Serious', 'Several', 'She', 'Should', 'Show', 'Side', 'Since', 'Sincere', 'Six', 'Sixty', 'So', 'Some', 'Somehow', 'Someone', 'Something', 'Sometime', 'Sometimes', 'Somewhere', 'Still', 'Such', 'System', 'Take', 'Ten', 'Than', 'That', 'The', 'Their', 'Them', 'Themselves', 'Then', 'Thence', 'There', 'Thereafter', 'Thereby', 'Therefore', 'Therein', 'Thereupon', 'These', 'They', 'Thick', 'Thin', 'Third', 'This', 'Those', 'Though', 'Three', 'Through', 'Throughout', 'Thru', 'Thus', 'To', 'Together', 'Too', 'Top', 'Toward', 'Towards', 'Twelve', 'Twenty', 'Two', 'Un', 'Under', 'Until', 'Up', 'Upon', 'Us', 'Very', 'Via', 'Was', 'We', 'Well', 'Were', 'What', 'Whatever', 'When', 'Whence', 'Whenever', 'Where', 'Whereafter', 'Whereas', 'Whereby', 'Wherein', 'Whereupon', 'Wherever', 'Whether', 'Which', 'While', 'Whither', 'Who', 'Whoever', 'Whole', 'Whom', 'Whose', 'Why', 'Will', 'With', 'Within', 'Without', 'Would', 'Yet', 'You', 'Your', 'Yours', 'Yourself', 'Yourselves', 'The']



def lrsuf(word,string,k):
  
    print(word)
    #print(string)
    res = 'true'
    
 
    words = list(string.split(' ')) # converting string into list
    arr = [] #array w/o stopwords
    farr=[] #array w/o stopwords + proper noun
    
    
    for i in words: # appending array with list in string w/o stopwords
        if i not in english_stops:
            arr.append(i)
    #print(arr) # printing array w/o stopwords
    tokens_tag = pos_tag(arr)
    for i in tokens_tag: # appending array with list in string w/o proper noun
        if i[1]!=  'NNP':
            farr.append(i[0])
    #print(farr) # printing array w/o stopwords and proper noun
        
    try:
            
           sindex = farr.index(word) # finding index of word
           #checking if left word present
           try:
                lindex = sindex - 1 # left word index
                #print(lindex)
                if lindex == -1:
                    lword = "No left word"
                else:
                    lword = farr[lindex] # left word
                #print(lword)
                dfl = pd.DataFrame([lword])
                dfl.to_csv('llist.csv', index=False, mode= 'a', header=False)
           except:
                  print('f')
           try: # checking if right word
                 rindex = sindex + 1 # right word index
                 rword = farr[rindex] # right word
                 #print(rword)
                 dfr = pd.DataFrame([rword])
                 dfr.to_csv('rlistnew.csv', index=False, mode= 'a', header=False)
           except: # no right word
                 rword = "No right word"
                 dfr = pd.DataFrame([rword])
                 dfr.to_csv('rlistnew.csv', index=False, mode= 'a', header=False)
    except:
             res = 'false'
    return res

                    
    
def lr(word,string,k):

    ns = -1
    
    print(word)
 
   
    print(string)
    words = list(string.split(' ')) # converting string into list
    arr = [] #array w/o stopwords
    farr=[] #array w/o stopwords + proper noun
    
    
    for i in words: # appending array with list in string w/o stopwords
        if i not in english_stops:
            arr.append(i)
    print(arr) # printing array w/o stopwords
    tokens_tag = pos_tag(arr)
    for i in tokens_tag: # appending array with list in string w/o proper noun
        if i[1]!=  'NNP':
            farr.append(i[0])
    #print(farr) # printing array w/o stopwords and proper noun
        
    try:
           sindex = farr.index(word) # finding index of word
           #checking if left word present
           try:
                lindex = sindex - 1 # left word index
                #print(lindex)
                if lindex == -1:
                    lword = "No left word"
                else:
                    lword = farr[lindex] # left word
                #print(lword)
                dfl = pd.DataFrame([lword])
                dfl.to_csv('llist.csv', index=False, mode= 'a', header=False)
           except:
                  print('f')
           try: # checking if right word
                 rindex = sindex + 1 # right word index
                 rword = farr[rindex] # right word
                 #print(rword)
                 dfr = pd.DataFrame([rword])
                 dfr.to_csv('rlistnew.csv', index=False, mode= 'a', header=False)
           except: # no right word
                 rword = "No right word"
                 dfr = pd.DataFrame([rword])
                 dfr.to_csv('rlistnew.csv', index=False, mode= 'a', header=False)
                    
            
        
    except: # no word present
            print('Enter exception word')
            #print(k)
            
            try:
            
                
                for i in suffix:#checking for suffix
                    word1 = word
                    print(i)
                    res = lrsuf(word1 + i,string,k) #callinf suffix function
                    if res == 'true':
                        ns = 0
                        break
                if ns == -1:# no suffix in the list
                    nos="No suffix found"
                   
                    dfl = pd.DataFrame([nos])
                    dfr = pd.DataFrame([nos])
                    dfl.to_csv('llist.csv', index=False, mode= 'a', header=False)
                    dfr.to_csv('rlistnew.csv', index=False, mode= 'a', header=False)
                    
            

           

                    
                    
                        
                        
                
            except:
                    lword="No word found"
                    rword = "No word found"
                    dfl = pd.DataFrame([lword])
                    dfr = pd.DataFrame([rword])
                    dfl.to_csv('llist.csv', index=False, mode= 'a', header=False)
                    dfr.to_csv('rlistnew.csv', index=False, mode= 'a', header=False)
                    
            

           
for index,row in df_csvw.iterrows():
    i=row['word']
    j = row['meaning']
    k=0
    lr(i,j,k)
        
    
