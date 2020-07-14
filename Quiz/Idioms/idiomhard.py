import random 
import pandas as pd
import numpy as np
import cgi
import sys
import csv
import gspread 
from Google import Create_Service
from oauth2client.service_account import ServiceAccountCredentials
import pygsheets


# TRY AND EXCEPT BLOCK AS THERE MIGHT BE A idiom NOT PRESENT IN THE FUNCTION CALLED

file = open('idiomquizsheethard.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(["Question", "Option 1", "Option 2","Option 3","Option 4","Correct answer","Question Type","Level"])
def datawrite(ques,f,s,t,f4,cans,qtype):
    
        qlevel = "HARD"
        
        writer.writerow([ques, f, s,t,f4,cans,qtype,qlevel])

df_csv1 = pd.read_csv('IdiomHard.csv',encoding='cp1252')
idiomp = df_csv1.iloc[:,0].values
meaning = df_csv1.iloc[:,1].values
idioml = idiomp.tolist()

def idiommeaning(i,uanswerarray,answer):

    
    try:
        idiomi =idioml.index(i)
    except:
        idiom = random.choice(idioml)
        idiomi =idioml.index(idiom)
    print("What is the meaning of the idiom : " + str(i) + " ? " )
    ques = "What is the meaning of the idiom : " + str(i) + " ? " 

    ans  = meaning[idiomi]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
  

    if ansv == 'A':
        print("A) " + str(ans))
        f = ans
    else:
        if idiomi - 1 != 0 :
            f = meaning[idiomi-1]
            print("A) " + str(f))
        else:
            f = meaning[idiomi+1]
            print("A) " + str(f))
    if ansv == 'B':
        print("B) " + str(ans))
        s = ans
    else:
        if idiomi - 2 != 0 :
            s = meaning[idiomi-2]
            print("B) " + str(s))
        else:
            s = meaning[idiomi+2]
            print("B) " + str(s))
    if ansv == 'C':
        print("C) " + str(ans))
        t = ans
    else:
        if idiomi - 3 != 0 :
            t = meaning[idiomi-3]
            print("C) " + str(t))
        else:
            t = meaning[idiomi+3]
            print("C) " + str(t))
    if ansv == 'D':
        f4 = ans
        print("D) " + str(ans))
    else:
        if idiomi - 4!= 0 :
            f4 = meaning[idiomi-4]
            print("D) " + str(f4))
        else:
            f4 = meaning[idiomi+4]
            print("D) " + str(f4))
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype = "static")
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 
    

def questions():


    answer = [ ] # Storing correct answer
    uanswerarray = [ ] # Storing user answer
    for i in idiomp: # Can change number of questions from here
        
        idiommeaning(i,uanswerarray,answer)

name = input("Please enter your name: ").title()
aq = input("Please enter number of times you like to play the quiz: ") # Number of times you want to attempt the quiz

def run_quiz(aq):

          questions()
        
          
          
           



run_quiz(aq) # Starting the quiz
