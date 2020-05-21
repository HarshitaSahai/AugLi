Question Categorization Documentation

Python Version: Python 3.7

Libraries used: 
String
Pandas
Numpy 
CSV
language_check 
Collections
nltk (pos_tag)
nltk.corpus (wordnet)

The array of words mentioned below along with the meaning 

conversation = ["Thank you so much","Do not mention","Thanks a lot","Thanks a ton","Hey thank you","Hey thank you so much","Hey thanks a lot","Thank you for your help","Thank you for the answer"] # For identifying coutous or starting/ending of conversation level 1.1
ques = ["Where","where","what","What","how","How","Where","where","What","what","when","When","Did","did","who","Who","whom","Whom","Why","why","could","Could","Will this","How","how","Tell","tell","Can","can","if","If"] # List of question word which help in level 2 and level 5
mean = ["Mean","Meaning","Means","Meant","Meaned","meaned","meant","means","meaning","mean","form","Form"] # List of word for helping in level 3.1
qword = ["what","when","did","What","When","Did","could","Could","How","how"] #Question word for level  3.2  
opinionq = ["what","why","did","if","else","what if","why not","What","Why","Did","If","Else","What if","Why not"] #Question words for level 4


sampleques.csv : Having all question 

Each entry in sampleques will be passed to the following function in the order defined and will pass as per condition satisfied.



Functions:

lengthofsentence(test_string):
test_string: Question in the current row
res: Stores number of words in the sentence if less than 3 then belongs to level 0 if not then passed to checksen(test_string).

checksen(test_string):
test_string: Question in current row
matches: Used to find errors such as spelling or grammar in en-US. If found length of match will not be 0.
If length of matches not == 0 then the error found are rectified and test_string have the corrected sentence.
The test_string is then passed to checkcourtesy(test_string)

checkcourtesy(test_string):
test_string: Question in the current row
Compare the test_string with sentences in conversation array if any match found then test_string belongs to level 1 else then test_string is passed to ss(test_string)

ss(test_string):
test_string: Question in the current row
The string of sentence is divided into list of words. Then pos_tags of each word is found.
If any adjective word is found flaga is 1 and if any word matches to words in ques array then flagq is 1.
If both flagq and flaga are 1 then the test_string is passed to findpronoun(test_string)
If only flaga is 1 then the test_string belongs to level 1 
For any other case, the test_string is passed to findpronoun(test_string)

findpronoun(test_string):
test_string: Question in the current row
The string of sentence is divided into a list of words. Then pos_tags of each word is found.
If wh-pronoun or pronoun is found then qpro or npro are incremented respectively. If noun is present then np is incremented.
If np or qpro is greater than 0 or if npro is not greater than 0 the test_string is passed to findmean(test_string)
If and only npro>0 and all other above specified conditions fail then test_string belongs to level 2.

findmean(test_string):
test_string: Question in the current row
The string of sentence is divided into a list of words. Then pos_tags of each word is found.
If any word in test_string matches with the word in the mean array and if any word in test_string is a noun (singular or plural) then flagm is incremented.
If flagm is greater the 0 then the test_string belongs to level 3 else it will be passed to findqpast(test_string).

findqpast(test_string):
test_string: Question in the current row
The string of sentence is divided into a list of words. Then pos_tags of each word is found.
If any word in test_string matches with the word in qword array then flagq = 1 and is a verb then flag = 1 the test_string belong to level 3.
If only flagq = 1 then test_string will pass to findopinion(test_string,flag3 = 1) else
for any other condition findopinion(test_string,flag3 = 0)

findopinion(test_string,flag3):
test_string: Question in the current row
The string of sentence is divided into a list of words. 
If any word in test_string matches with word in opinionsy array then flago = 1.
If any word in test_string matches with word in opinionq array then flagq = 1.
If flago = 1 then the test_string is passed to findfutures(test_string,flag3,flag4 = 1) else for any other condition test_string will be passed as findfuture(test_string,flag3,flag4=0).

findfurture(test_string,flag3,flag4):
test_string: Question in the current row
The string of sentence is divided into a list of words. Then pos_tags of each word is found.
If any word in test_string matches is adjective then flaga = 1 or any word is model then flagm = 1.
If any word in test_string matches with any word in ques array then flagq = 1.
If flagq = 1 then we will check the following conditions:
If both flagm and flaga are 1 then the test_string belongs to level 5.
  Else If flag4 is 1 then test_string belongs to level 4
  Else If flag3 is 1 then test_string belongs to level 3
  Else test_string belongs to level 5
If flagq is not equal to 1 then check the following conditions:
  If flag3 is 1 then test_string is level 3
  Else if flag4 is 1 then test_string is level 4.
  Else the test_string doesn’t belong to any level 

The above level decided will be appended to resa (result array).
The value is resa will be appended to samplelevelq.csv


 






