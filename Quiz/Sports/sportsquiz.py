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

file = open('sportsquizsheet.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(["Question", "Option 1", "Option 2","Option 3","Option 4","Correct answer","Question Type"])
def datawrite(ques,f,s,t,f4,cans,qtype):
    

        
        writer.writerow([ques, f, s,t,f4,cans,qtype])
# Women    
df_csv1 = pd.read_csv('womens_participation_in_the_games_of_the_olympiad.csv',encoding='cp1252')
wgyear = df_csv1.iloc[:,0].values
wgevent = df_csv1.iloc[:,1].values
wgpart = df_csv1.iloc[:,2].values
wgyearl = wgyear.tolist()

# Cricket World cup
df_csv2 = pd.read_csv('Cricket World Cup Winners.csv',encoding='cp1252')
cwcyear = df_csv2.iloc[1:11,0].values
cwchost = df_csv2.iloc[1:11,1].values
cwcvenu = df_csv2.iloc[1:11,2].values
cwcwinner = df_csv2.iloc[1:11,3].values
cwcyeral = cwcyear.tolist()

# Asia Cup
df_csv3 = pd.read_csv('Asia Cup Winners.csv',encoding='cp1252',error_bad_lines=False)
acyear = df_csv3.iloc[1:13,0].values
achost = df_csv3.iloc[1:13,1].values
acvenu = df_csv3.iloc[1:13,2].values
acwinner = df_csv3.iloc[1:13,3].values
acyearl = acyear.tolist()

def womenparticipants(year,uanswerarray,answer): #Function to find number of women participants
    
    wgpartl = wgyear.tolist()
    try:
        wgparti =wgpartl.index(year)
    except:
        year = random.choice(wgyearl)
        wgparti =wgpartl.index(year)
    print("Number of women who participated in olympics in the year " + str(year) + " ? " )
    ques = "Number of women who participated in olympics in the year " + str(year) + " ? "

    ans  = wgpart[wgparti]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
  

    if ansv == 'A':
        print("A) " + str(ans))
        f = ans
    else:
        if wgparti - 1 != 0 :
            f = wgpart[wgparti-1]
            print("A) " + str(f))
        else:
            f = wgpart[wgparti+1]
            print("A) " + str(f))
    if ansv == 'B':
        print("B) " + str(ans))
        s = ans
    else:
        if wgparti - 2 != 0 :
            s = wgpart[wgparti-2]
            print("B) " + str(s))
        else:
            s = wgpart[wgparti+2]
            print("B) " + str(s))
    if ansv == 'C':
        print("C) " + str(ans))
        t = ans
    else:
        if wgparti - 3 != 0 :
            t = wgpart[wgparti-3]
            print("C) " + str(t))
        else:
            t = wgpart[wgparti+3]
            print("C) " + str(t))
    if ansv == 'D':
        f4 = ans
        print("D) " + str(ans))
    else:
        if wgparti - 4!= 0 :
            f4 = wgpart[wgparti-4]
            print("D) " + str(f4))
        else:
            f4 = wgpart[wgparti+4]
            print("D) " + str(f4))
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype = "static")
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 


def womenevents(year,uanswerarray,answer): #Function to find number of women participants
    
    wgeventl = wgyear.tolist()
    try:
     wgeventi =wgeventl.index(year)
    except:
        year = random.choice(wgyearl)
        wgeventi =wgeventl.index(year)
    print("Number of women events that took place in Olympic in the year "+ str(year) + " ? " )
    ques = "Number of women events that took place in Olympic in the year "+ str(year) + " ? " 
    ans  = wgevent[wgeventi]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
  

    if ansv == 'A':
        print("A) " + str(ans))
        f = ans
    else:
        if wgeventi - 1 != 0 :
            f = wgevent[wgeventi-1]
            print("A) " + str(f))
        else:
            f = wgevent[wgeventi+1]
            print("A) " + str(f))
    if ansv == 'B':
        print("B) " + str(ans))
        s = ans
    else:
        if wgeventi - 2 != 0 :
            s = wgevent[wgeventi-2]
            print("B) " + str(s))
        else:
            s = wgevent[wgeventi+2]
            print("B) " + str(s))
    if ansv == 'C':
        print("C) " + str(ans))
        t = ans
    else:
        if wgeventi - 3 != 0 :
            t = wgevent[wgeventi-3]
            print("C) " + str(t))
        else:
            t = wgevent[wgeventi+3]
            print("C) " + str(t))
    if ansv == 'D':
        f4 = ans
        print("D) " + str(ans))
    else:
        if wgeventi - 4!= 0 :
            f4 = wgevent[wgeventi-4]
            print("D) " + str(f4))
        else:
            f4 = wgevent[wgeventi+4]
            print("D) " + str(f4))
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype = "static")
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 


def cwchostfunction(year,uanswerarray,answer): #Function to find cwc host
    
    cwchostl = cwcyear.tolist()
    try:
        cwchosti =cwchostl.index(year)
    except:
       year = random.choice(cwcyeral)
       cwchosti =cwchostl.index(year)
    print("Which country was the host for Cricket World Cup of the year "+ str(year) + " ? " )
    ques = "Which country was the host for Cricket World Cup of the year "+ str(year) + " ? " 
    ans  = cwchost[cwchosti]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
  

    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if cwchosti - 1 != 0 :
            f = cwchost[cwchosti-1]
            print("A) " + f)
        else:
            f = cwchost[cwchosti+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if cwchosti - 2 != 0 :
            s = cwchost[cwchosti-2]
            print("B) " + s)
        else:
            s = cwchost[cwchosti+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if cwchosti - 3 != 0 :
            t = cwchost[cwchosti-3]
            print("C) " + t)
        else:
            t = cwchost[cwchosti+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if cwchosti - 4!= 0 :
            f4 = cwchost[cwchosti-4]
            print("D) " + f4)
        else:
            f4 = cwchost[cwchosti+4]
            print("D) " + f4)
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype = "static")
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def cwcvenufunction(year,uanswerarray,answer): #Function to find cwc venu
    
    cwcvenul = cwcyear.tolist()
   
    try:
        cwcvenui =cwcvenul.index(year)
    except: 
        year = random.choice(cwcyeral)
        cwcvenui =cwcvenul.index(year)
    print("What was the venu for Cricket World Cup of the year "+ str(year) + " ? " )
    ques = "What was the venu for Cricket World Cup of the year "+ str(year) + " ? " 
    ans  = cwcvenu[cwcvenui]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
  

    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if cwcvenui - 1 != 0 :
            f = cwcvenu[cwcvenui-1]
            print("A) " + f)
        else:
            f = cwcvenu[cwcvenui+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if cwcvenui - 2 != 0 :
            s = cwcvenu[cwcvenui-2]
            print("B) " + s)
        else:
            s = cwcvenu[cwcvenui+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if cwcvenui - 3 != 0 :
            t = cwcvenu[cwcvenui-3]
            print("C) " + t)
        else:
            t = cwcvenu[cwcvenui+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if cwcvenui - 4!= 0 :
            f4 = cwcvenu[cwcvenui-4]
            print("D) " + f4)
        else:
            f4 = cwcvenu[cwcvenui+4]
            print("D) " + f4)
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype = "static")
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 


def cwcwinnerfunction(year,uanswerarray,answer): #Function to find cwc winner
   
    cwcwinnerl = cwcyear.tolist()
    try:
        cwcwinneri =cwcwinnerl.index(year)
    except:
        year = random.choice(cwcyeral)
        cwcwinneri =cwcwinnerl.index(year)
    print("Which country was the winner for Cricket World Cup of the year "+ str(year) + " ? " )
    ques = "Which country was the winner for Cricket World Cup of the year "+ str(year) + " ? " 
    ans  = cwcwinner[cwcwinneri]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
  

    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if cwcwinneri - 1 != 0 :
            f = "South Africa"
            print("A) " + f)
        else:
            f = "South Africa"
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if cwcwinneri - 2 != 0 :
            s = "Ireland"
            print("B) " + s)
        else:
            s = "Ireland"
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if cwcwinneri - 3 != 0 :
            t = "New Zealand"
            print("C) " + t)
        else:
            t = "New Zealand"
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if cwcwinneri - 4!= 0 :
            f4 = "Bangladesh"
            print("D) " + f4)
        else:
            f4 = "Bangladesh"
            print("D) " + f4)
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype = "static")
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 


def achostfunction(year,uanswerarray,answer): #Function to find ac host
   
    achostl = acyear.tolist()
    try:
        achosti =achostl.index(year)
    except:
        year = random.choice(acyearl)
        achosti =achostl.index(year)
    print("Which country was the host for Asia Cup of the year "+ str(year) + " ? " )
    ques = "Which country was the host for Asia Cup of the year "+ str(year) + " ? " 
    ans  = achost[achosti]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
  

    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if achosti - 1 != 0 :
            f = "Oman"
            print("A) " + f)
        else:
            f = "Nepal"
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if achosti - 2 != 0 :
            s = "Singapore"
            print("B) " + s)
        else:
            s = "Indonesia"
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if achosti - 3 != 0 :
            t = "Kuwait"
            print("C) " + t)
        else:
            t = "Brunei"
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if achosti - 4!= 0 :
            f4 = "Japan"
            print("D) " + f4)
        else:
            f4 = "Thailand"
            print("D) " + f4)
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype = "static")
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def acvenufunction(year,uanswerarray,answer): #Function to find venu
    
    acvenul = acyear.tolist()
    try:
        acvenui =acvenul.index(year)
    except:
        year = random.choice(acyearl)
        acvenui =acvenul.index(year)
    print("Which country was the venu for Asia Cup of the year "+ str(year) + " ? " )
    ques = "Which country was the venu for Asia Cup of the year "+ str(year) + " ? " 
    ans  = acvenu[acvenui]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
  

    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if acvenui - 1 != 0 :
            f = "Mumbai"
            print("A) " + f)
        else:
            f = "Jaffna"
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if acvenui - 2 != 0 :
            s = "Lahore"
            print("B) " + s)
        else:
            s = "Bentota"
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if acvenui - 3 != 0 :
            t = "Delhi"
            print("C) " + t)
        else:
            t = "Bangalore"
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if acvenui - 4!= 0 :
            f4 = "Galle"
            print("D) " + f4)
        else:
            f4 = "Colombo"
            print("D) " + f4)
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype = "static")
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def acwinnerfunction(year,uanswerarray,answer): #Function to find winner
    
    acwinnerl = acyear.tolist()
    try:
        acwinneri =acwinnerl.index(year)
    except:
        year = random.choice(acyearl)
        acwinneri =acwinnerl.index(year)

    print("Which country was the winner for Asia Cup of the year "+ str(year) + " ? " )
    ques = "Which country was the winner for Asia Cup of the year "+ str(year) + " ? " 
    ans  = acwinner[acwinneri]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
  

    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if acwinneri - 1 != 0 :
            f = "UAE"
            print("A) " + f)
        else:
            f = "Hong Kong"
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if acwinneri - 2 != 0 :
            s = "Bangladesh"
            print("B) " + s)
        else:
            s = "Singapore"
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if acwinneri - 3 != 0 :
            t = "Oman"
            print("C) " + t)
        else:
            t = "Nepal"
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if acwinneri - 4!= 0 :
            f4 = "Qatar"
            print("D) " + f4)
        else:
            f4 = "Bahrain"
            print("D) " + f4)
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype = "static")
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 



funcnum = [1,2,3,4,5]

def questions():
    one = 0
    two = 0
    three = 0
    four = 0 
    five = 0
    six  = 0
    seven = 0
    eight = 0

    answer = [ ] # Storing correct answer
    uanswerarray = [ ] # Storing user answer
    yearselected = random.choice(wgyear)
    for i in range(5): # Can change number of questions from here
        j = random.sample(funcnum,1)
        #print(j)
        if j == [1]:
            one = one + 1
            if one > 1: #If already accessed with global country selected the change the name
                womenevents(random.choice(wgyear),uanswerarray,answer)
                
            else:
                womenevents(yearselected,uanswerarray,answer)
            

        elif j == [2]:
            two = two + 1
            if two > 1: #If already accessed with global country selected the change the name
                womenparticipants(random.choice(wgyear),uanswerarray,answer)
                
            else:
                womenparticipants(yearselected,uanswerarray,answer)
        if j == [3]:
            three = three + 1
            if three > 1: #If already accessed with global country selected the change the name
                cwchostfunction(random.choice(cwcyear),uanswerarray,answer)
                
            else:
                cwchostfunction(yearselected,uanswerarray,answer)
            

        elif j == [4]:
            four = four + 1
            if four > 1: #If already accessed with global country selected the change the name
                cwcvenufunction(random.choice(cwcyear),uanswerarray,answer)
                
            else:
                cwcvenufunction(yearselected,uanswerarray,answer)
        
        elif j == [5]:
            five = five + 1
            if five > 1: #If already accessed with global country selected the change the name
               cwcwinnerfunction(random.choice(cwcyear),uanswerarray,answer)
                
            else:
                cwcwinnerfunction(yearselected,uanswerarray,answer)
        elif j == [6]:
            six = six + 1
            if six > 1: #If already accessed with global country selected the change the name
               achostfunction(random.choice(acyear),uanswerarray,answer)
                
            else:
                achostfunction(yearselected,uanswerarray,answer)
        elif j == [7]:
            seven = seven + 1
            if seven > 1: #If already accessed with global country selected the change the name
               acvenufunction(random.choice(acyear),uanswerarray,answer)
                
            else:
                acvenufunction(yearselected,uanswerarray,answer)
        elif j == [8]:
            eight = eight + 1
            if eight > 1: #If already accessed with global country selected the change the name
               acwinnerfunction(random.choice(acyear),uanswerarray,answer)
                
            else:
                acwinnerfunction(yearselected,uanswerarray,answer)
                
                
      
            
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
          
         
          unanswerarray,answer = questions()
         
          for j in range(5):
           
            a = unanswerarray[j]
            b = answer[j]
            
            if a == b: # Comparing user answer and actual answer
                 score += 1
          print("\nAttempt: " + str(x+1)) # Printing number of attempt 
          print("\n{0}, you scored {1} out of {2}.".format(name, score,5)) # printing the score
          x = x + 1
          
          
           



run_quiz(aq) # Starting the quiz
