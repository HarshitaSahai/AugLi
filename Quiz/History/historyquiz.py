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


# TRY AND EXCEPT BLOCK AS THERE MIGHT BE A YEAR NOT PRESENT IN THE FUNCTION CALLED

file = open('historyquizsheet.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(["Question", "Option 1", "Option 2","Option 3","Option 4","Correct answer","Question type"])
def datawrite(ques,f,s,t,f4,cans,qtype):
    

        
        writer.writerow([ques, f, s,t,f4,cans,qtype])
# Women    
df_csv1 = pd.read_csv('history-date-events.csv',encoding='cp1252')
hdeyear = df_csv1.iloc[1:33,0].values
hdeevents = df_csv1.iloc[1:33,1].values
hdeyearl = hdeyear.tolist()

# Cricket World cup
df_csv2 = pd.read_csv('history-date-events-importance.csv',encoding='cp1252')
hdeiyear = df_csv2.iloc[1:105,0].values
hdeievents = df_csv2.iloc[1:105,1].values
hdeiimp = df_csv2.iloc[1:105,2].values
hdeiyearl = hdeiyear.tolist()
hdeieventl = hdeievents.tolist()

# Data with year and events
def hdeeventsfunction(year,uanswerarray,answer): #Function to find events in the year
    
    hdeeventl = hdeyear.tolist()
    try:
        hdeeventsi =hdeeventl.index(year)
    except:
        year = random.choice(hdeyearl)
        hdeeventsi =hdeeventl.index(year)
    print("Which of the following event took place in the year " + str(year) + " ? " )
    ques = "Which of the following event took place in the year  " + str(year) + " ? "

    ans  = hdeevents[hdeeventsi]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
  

    if ansv == 'A':
        print("A) " + str(ans))
        f = ans
    else:
        if hdeeventsi - 1 != 0 :
            f = hdeevents[hdeeventsi-1]
            print("A) " + str(f))
        else:
            f = hdeevents[hdeeventsi+1]
            print("A) " + str(f))
    if ansv == 'B':
        print("B) " + str(ans))
        s = ans
    else:
        if hdeeventsi - 2 != 0 :
            s = hdeevents[hdeeventsi-2]
            print("B) " + str(s))
        else:
            s = hdeevents[hdeeventsi+2]
            print("B) " + str(s))
    if ansv == 'C':
        print("C) " + str(ans))
        t = ans
    else:
        if hdeeventsi - 3 != 0 :
            t = hdeevents[hdeeventsi-3]
            print("C) " + str(t))
        else:
            t = hdeevents[hdeeventsi+3]
            print("C) " + str(t))
    if ansv == 'D':
        f4 = ans
        print("D) " + str(ans))
    else:
        if hdeeventsi - 4!= 0 :
            f4 = hdeevents[hdeeventsi-4]
            print("D) " + str(f4))
        else:
            f4 = hdeevents[hdeeventsi+4]
            print("D) " + str(f4))
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype = "static")
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def hdeieventsfunction(year,uanswerarray,answer): #Function to find events in the year for date event and importance data
    
    hdeieventl = hdeiyear.tolist()
    try:
        hdeieventsi =hdeieventl.index(year)
    except:
        year = random.choice(hdeiyearl)
        hdeieventsi =hdeieventl.index(year)
    print("Which of the following event took place in the year " + str(year) + " ? " )
    ques = "Which of the following event took place in the year " + str(year) + " ? "

    ans  = hdeievents[hdeieventsi]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
  

    if ansv == 'A':
        print("A) " + str(ans))
        f = ans
    else:
        if hdeieventsi - 1 != 0 :
            f = hdeievents[hdeieventsi-1]
            print("A) " + str(f))
        else:
            f = hdeievents[hdeieventsi+1]
            print("A) " + str(f))
    if ansv == 'B':
        print("B) " + str(ans))
        s = ans
    else:
        if hdeieventsi - 2 != 0 :
            s = hdeievents[hdeieventsi-2]
            print("B) " + str(s))
        else:
            s = hdeievents[hdeieventsi+2]
            print("B) " + str(s))
    if ansv == 'C':
        print("C) " + str(ans))
        t = ans
    else:
        if hdeieventsi - 3 != 0 :
            t = hdeievents[hdeieventsi-3]
            print("C) " + str(t))
        else:
            t = hdeievents[hdeieventsi+3]
            print("C) " + str(t))
    if ansv == 'D':
        f4 = ans
        print("D) " + str(ans))
    else:
        if hdeieventsi - 4!= 0 :
            f4 = hdeievents[hdeieventsi-4]
            print("D) " + str(f4))
        else:
            f4 = hdeievents[hdeieventsi+4]
            print("D) " + str(f4))
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype = "static")
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def hdeiimportancefunction(uanswerarray,answer): #Function to importance of events
    
    hdeiimpl = hdeievents.tolist()
   
    event = random.choice(hdeieventl) # selecting the events
    hdeiimpi =hdeiimpl.index(event) # finding index of event in the event list and store it to find ans in importance 
    print("What was the importance of " + str(event) + " ? " )
    ques = "What was the importance of " + str(event) + " ? "

    ans  = hdeiimp[hdeiimpi]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
  

    if ansv == 'A':
        print("A) " + str(ans))
        f = ans
    else:
        if hdeiimpi - 1 != 0 :
            f = hdeiimp[hdeiimpi-1]
            print("A) " + str(f))
        else:
            f = hdeiimp[hdeiimpi +1]
            print("A) " + str(f))
    if ansv == 'B':
        print("B) " + str(ans))
        s = ans
    else:
        if hdeiimpi - 2 != 0 :
            s = hdeiimp[hdeiimpi-2]
            print("B) " + str(s))
        else:
            s = hdeiimp[hdeiimpi+2]
            print("B) " + str(s))
    if ansv == 'C':
        print("C) " + str(ans))
        t = ans
    else:
        if hdeiimpi - 3 != 0 :
            t = hdeiimp[hdeiimpi-3]
            print("C) " + str(t))
        else:
            t = hdeiimp[hdeiimpi+3]
            print("C) " + str(t))
    if ansv == 'D':
        f4 = ans
        print("D) " + str(ans))
    else:
        if hdeiimpi - 4!= 0 :
            f4 = hdeiimp[hdeiimpi-4]
            print("D) " + str(f4))
        else:
            f4 = hdeiimp[hdeiimpi+4]
            print("D) " + str(f4))
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype = "static")
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

funcnum = [1,2,3]

def questions(): # Function will create 5 questions randomly
    one = 0
    two = 0
    three = 0
    answer = [ ] # Storing correct answer
    uanswerarray = [ ] # Storing user answer
    year = random.choice(hdeyear)
    for i in range(5): # Can change number of questions from here
        j = random.sample(funcnum,1)
        #print(j)
        if j == [1]:
            one = one + 1
            if one > 1: #If already accessed with global country selected the change the name
                hdeeventsfunction(random.choice(hdeyear),uanswerarray,answer)
                
            else:
                hdeeventsfunction(year,uanswerarray,answer)
            

        elif j == [2]:
            two = two + 1
            if two > 1: #If already accessed with global country selected the change the name
                hdeieventsfunction(random.choice(hdeiyear),uanswerarray,answer)
                
            else:
                hdeieventsfunction(year,uanswerarray,answer)
                
        elif j == [3]:
            three = three + 1
            if three > 1: #If already accessed with global country selected the change the name
                hdeiimportancefunction(uanswerarray,answer)
                
            else:
                hdeiimportancefunction(uanswerarray,answer)
                

            
    return answer,uanswerarray
name = input("Please enter your name: ").title()
aq = input("Please enter number of times you like to play the quiz: ") # Number of times you want to attempt the quiz

lenq = 5
def run_quiz(aq):
    
     x = 0
     while (x < int(aq)):
          score = 0
          print(score)
          answer=[]
          unanswerarray= []
          answer,unanswerarray = questions() # Return array of user and actual answer 
          for j in range(5):
           
            a = unanswerarray[j]
            b = answer[j]
            
            if a == b: # Comparing user answer and actual answer
                 score += 1
          print("\nAttempt: " + str(x+1)) # Printing number of attempt 
          print("\n{0}, you scored {1} out of {2}.".format(name, score,5)) # printing the score
          x = x + 1
          
          
           



run_quiz(aq) # Starting the quiz
