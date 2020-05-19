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





# Creating a sheet and adding the questions,options and result
df_csv = pd.DataFrame(columns=['Questions'])


file = open('countryquizsheet.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(["Ques", "Option 1", "Option 2","Option 3","Option 4","Correct answer"])
def datawrite(ques,f,s,t,f4,cans):
    

        
        writer.writerow([ques, f, s,t,f4,cans])
    







df_csv1 = pd.read_csv('countrylangcurrencyhoc.csv',encoding='cp1252')
cn = df_csv1.iloc[:,0].values
cc = df_csv1.iloc[:,1].values
ccu = df_csv1.iloc[:,2].values
col = df_csv1.iloc[:,3].values
chog = df_csv1.iloc[:,4].values


def capital(country,uanswerarray,answer): #Function to find capital
    
    print("what is the capital of "  + country)
    cnl = cn.tolist()
    countryi =cnl.index(country)
    ans = cc[countryi]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
   
    ques = "what is the capital of" + country
    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if countryi - 1 != 0 :
            f = cnl[countryi-1]
            print("A) " + f)
        else:
            f = cnl[countryi+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if countryi - 2 != 0 :
            s = cnl[countryi-2]
            print("B) " + s)
        else:
            s = cnl[countryi+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if countryi - 3 != 0 :
            t = cnl[countryi-3]
            print("C) " + t)
        else:
            t = cnl[countryi+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if countryi - 4!= 0 :
            f4 = cnl[countryi-4]
            print("D) " + f4)
        else:
            f = cnl[countryi+4]
            print("D) " + f4)
    cans = ans
    uanswer = input()
    datawrite(ques,f,s,t,f4,cans)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def currency(country,uanswerarray,answer): #Function to find currency 
    print("what is the currency of " + country)
    ques = "what is the currency of " + country
    ccul = cn.tolist()
    currencyi =ccul.index(country)
    ans  = ccu[currencyi]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
  

    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if currencyi - 1 != 0 :
            f = ccul[currencyi-1]
            print("A) " + f)
        else:
            f = ccul[currencyi+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if currencyi - 2 != 0 :
            s = ccul[currencyi-2]
            print("B) " + s)
        else:
            s = ccul[currencyi+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if currencyi - 3 != 0 :
            t = ccul[currencyi-3]
            print("C) " + t)
        else:
            t = ccul[currencyi+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if currencyi - 4!= 0 :
            f4 = ccul[currencyi-4]
            print("D) " + f4)
        else:
            f = ccul[currencyi+4]
            print("D) " + f4)
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

    
def officialang(country,uanswerarray,answer): #Function to find language
    print("what is the official language of " + country)
    ques = "what is the official language of " + country
    coll = cn.tolist()
    languagei =coll.index(country)
    ans = col[languagei]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
    

  
    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if languagei - 1 != 0 :
            f = coll[languagei-1]
            print("A) " + f)
        else:
            f = coll[languagei+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if languagei - 2 != 0 :
            s = coll[languagei-2]
            print("B) " + s)
        else:
            s = coll[languagei+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if languagei - 3 != 0 :
            t = coll[languagei-3]
            print("C) " + t)
        else:
            t = coll[languagei+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if languagei - 4!= 0 :
            f4 = coll[languagei-4]
            print("D) " + f4)
        else:
            f = coll[languagei+4]
            print("D) " + f4)
    cans = ans

    uanswer = input()

    uanswerarray.append(uanswer)
    datawrite(ques,f,s,t,f4,cans)
    answer.append(ansv)

def headofgovt(country,uanswerarray,answer): #Function to find head of government
    print("who is the head of government of " + country)
    ques = "who is the head of government of " + country
    chogl = cn.tolist()
    headi =chogl.index(country)
    ans = chog[headi]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
   
    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if headi - 1 != 0 :
            f = chogl[headi-1]
            print("A) " + f)
        else:
            f = chogl[headi+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if headi - 2 != 0 :
            s = chogl[headi-2]
            print("B) " + s)
        else:
            s = chogl[headi+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if headi - 3 != 0 :
            t = chogl[headi-3]
            print("C) " + t)
        else:
            t = chogl[headi+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if headi - 4!= 0 :
            f4 = chogl[headi-4]
            print("D) " + f4)
        else:
            f = chogl[headi+4]
            print("D) " + f4)
    cans = ans

    uanswer = input()
    uanswerarray.append(uanswer)
    datawrite(ques,f,s,t,f4,cans)
    answer.append(ansv)         # Appending the answer option in array 


funcnum = [1,2,3,4] # 1. Capital 2. Currency 3. Language 4. Head og govt.



def questions(): # Function will create 5 questions randomly
    one = 0
    two = 0
    three = 0
    four = 0
    answer = [ ] # Storing correct answer
    uanswerarray = [ ] # Storing user answer
    country = random.choice(cn)
    for i in range(5): # Can change number of questions from here
        j = random.sample(funcnum,1)
        #print(j)
        if j == [1]:
            one = one + 1
            if one > 1: #If already accessed with global country selected the change the name
                capital(random.choice(cn),uanswerarray,answer)
                
            else:
                capital(country,uanswerarray,answer)
            

        elif j == [2]:
            two = two + 1
            if two > 1: #If already accessed with global country selected the change the name
                currency(random.choice(cn),uanswerarray,answer)
                
            else:
                currency(country,uanswerarray,answer)
                
        elif j == [3]:
            three = three + 1
            if three > 1: #If already accessed with global country selected the change the name
                officialang(random.choice(cn),uanswerarray,answer)
                
            else:
                officialang(country,uanswerarray,answer)
                
        elif j == [4]:
            four = four + 1
            if four > 1: #If already accessed with global country selected the change the name
                headofgovt(random.choice(cn),uanswerarray,answer)
            
            else:
                headofgovt(country,uanswerarray,answer)
            
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









