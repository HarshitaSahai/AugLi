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
writer.writerow(["Question", "Option 1", "Option 2","Option 3","Option 4","Correct answer","Ques Type","Question Level"])
def datawrite(ques,f,s,t,f4,cans,qtype,qlevel):
    

        
        writer.writerow([ques, f, s,t,f4,cans,qtype,qlevel])
    







df_csv1 = pd.read_csv('countrylangcurrencyhoc.csv',encoding='cp1252')
cn = df_csv1.iloc[:,0].values
cc = df_csv1.iloc[:,1].values
ccu = df_csv1.iloc[:,2].values
col = df_csv1.iloc[:,3].values
chog = df_csv1.iloc[:,4].values
df_csv2 = pd.read_csv('countrylevel.csv',encoding='cp1252')
ceasy = df_csv2.iloc[1:28,0].values 
cmedium = df_csv2.iloc[1:36,1].values
chard = df_csv2.iloc[1:109,2].values  

def capital(country,uanswerarray,answer,qlevel): #Function to find capital
    
    print("What is the capital of "  + str(country) +  "?")
    cnl = cn.tolist()
    countryi =cnl.index(country)
    ans = cc[countryi]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
   
    ques = "What is the capital of " + country +  "?"
    qtype = "static"
    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if countryi - 1 != 0 :
            f = cc[countryi-1]
            print("A) " + f)
        else:
            f = cc[countryi+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if countryi - 2 != 0 :
            s = cc[countryi-2]
            print("B) " + s)
        else:
            s = cc[countryi+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if countryi - 3 != 0 :
            t = cc[countryi-3]
            print("C) " + t)
        else:
            t = cc[countryi+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if countryi - 4!= 0 :
            f4 = cc[countryi-4]
            print("D) " + f4)
        else:
            f4 = cc[countryi+4]
            print("D) " + f4)
    cans = ans
    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype,qlevel)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def currency(country,uanswerarray,answer,qlevel): #Function to find currency 
    print("What is the currency of " + str(country) +  "?")
    ques = "What is the currency of " + country + "?"
    qtype = "static"
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
            f = ccu[currencyi-1]
            print("A) " + f)
        else:
            f = ccu[currencyi+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if currencyi - 2 != 0 :
            s = ccu[currencyi-2]
            print("B) " + s)
        else:
            s = ccu[currencyi+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if currencyi - 3 != 0 :
            t = ccu[currencyi-3]
            print("C) " + t)
        else:
            t = ccu[currencyi+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if currencyi - 4!= 0 :
            f4 = ccu[currencyi-4]
            print("D) " + f4)
        else:
            f4 = ccu[currencyi+4]
            print("D) " + f4)
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype,qlevel)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

    
def officialang(country,uanswerarray,answer,qlevel): #Function to find language
    print("What is the official language of " + str(country) +  "?")
    ques = "What is the official language of " + country +  "?"
    coll = cn.tolist()
    languagei =coll.index(country)
    ans = col[languagei]
    qtype = "static"
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
            f = col[languagei-1]
            print("A) " + f)
        else:
            f = col[languagei+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if languagei - 2 != 0 :
            s = col[languagei-2]
            print("B) " + s)
        else:
            s = col[languagei+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if languagei - 3 != 0 :
            t = col[languagei-3]
            print("C) " + t)
        else:
            t = col[languagei+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if languagei - 4!= 0 :
            f4 = col[languagei-4]
            print("D) " + f4)
        else:
            f4 = col[languagei+4]
            print("D) " + f4)
    cans = ans

    uanswer = input()

    uanswerarray.append(uanswer)
    datawrite(ques,f,s,t,f4,cans,qtype,qlevel)
    answer.append(ansv)

def headofgovt(country,uanswerarray,answer,qlevel): #Function to find head of government
    print("Who is the head of government of " + str(country) +  "?")
    ques = "Who is the head of government of " + country +  "?"
    chogl = cn.tolist()
    headi =chogl.index(country)
    ans = chog[headi]
    qtype = "dynamic"
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
            f = chog[headi-1]
            print("A) " + f)
        else:
            f = chog[headi+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if headi - 2 != 0 :
            s = chog[headi-2]
            print("B) " + s)
        else:
            s = chog[headi+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if headi - 3 != 0 :
            t = chog[headi-3]
            print("C) " + t)
        else:
            t = chog[headi+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if headi - 4!= 0 :
            f4 = chog[headi-4]
            print("D) " + f4)
        else:
            f4 = chogl[headi+4]
            print("D) " + f4)
    cans = ans

    uanswer = input()
    uanswerarray.append(uanswer)
    datawrite(ques,f,s,t,f4,cans,qtype,qlevel)
    answer.append(ansv)         # Appending the answer option in array 


funcnum = [1,2,3,4] # 1. Capital 2. Currency 3. Language 4. Head og govt.





def questionsleveleasy(): # Function will create 5 questions randomly
    answer = [ ] # Storing correct answer
    uanswerarray = [ ] # Storing user answer
   
    for i in chard: # Can change number of questions from here
        
        
            
            
                capital(i,uanswerarray,answer,"HARD")
                

           
                currency(i,uanswerarray,answer,"HARD")
                    
            
                officialang(i,uanswerarray,answer,"HARD")
                    
            
                headofgovt(i,uanswerarray,answer,"HARD")
                
  



name = input("Please enter your name: ").title()
aq = input("Please enter number of times you like to play the quiz: ") # Number of times you want to attempt the quiz

lenq = 5
def run_quiz(aq):
    
   
          questionsleveleasy()
          


          
           



run_quiz(aq) # Starting the quiz









