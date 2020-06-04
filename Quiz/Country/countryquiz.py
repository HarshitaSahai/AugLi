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
    
    print("what is the capital of "  + str(country))
    cnl = cn.tolist()
    countryi =cnl.index(country)
    ans = cc[countryi]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
   
    ques = "what is the capital of " + country
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
    print("what is the currency of " + str(country))
    ques = "what is the currency of " + country
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
    print("what is the official language of " + str(country))
    ques = "what is the official language of " + country
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
    print("who is the head of government of " + str(country))
    ques = "who is the head of government of " + country
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
   
    for i in range(5): # Can change number of questions from here
        j = random.sample(funcnum,1)
        country = random.choice(ceasy)
        flag = 0
        #print(j)
        if j == [1]:
            flag = flag + 2
            if flag  > 1: #If already accessed with global country selected the change the name
                capital(random.choice(ceasy),uanswerarray,answer,"EASY")
                
            else:
                capital(country,uanswerarray,answer,"EASY")
            

        elif j == [2]:
            flag  = flag  + 2
            if flag > 1 : #If already accessed with global country selected the change the name
                currency(random.choice(ceasy),uanswerarray,answer,"EASY")
                
            else:
                currency(country,uanswerarray,answer,"EASY")
                
        elif j == [3]:
            flag  = flag  + 2
            if flag > 1: #If already accessed with global country selected the change the name
                officialang(random.choice(ceasy),uanswerarray,answer,"EASY")
                
            else:
                officialang(country,uanswerarray,answer,"EASY")
                
        elif j == [4]:
            flag  = flag  + 2
            if flag > 1: #If already accessed with global country selected the change the name
                headofgovt(random.choice(ceasy),uanswerarray,answer,"EASY")
            
            else:
                headofgovt(country,uanswerarray,answer,"EASY")
            
    return answer,uanswerarray

def questionslevelmedium(): # Function will create 5 questions randomly
   
    answer = [ ] # Storing correct answer
    uanswerarray = [ ] # Storing user answer
    
    for i in range(5): # Can change number of questions from here
        j = random.sample(funcnum,1)
        country = random.choice(cmedium)
        flag = 0
        #print(j)
        if j == [1]:
            flag  = flag  + 2
            if flag  > 1: #If already accessed with global country selected the change the name
                capital(random.choice(cmedium),uanswerarray,answer,"MEDIUM")
                
            else:
                capital(country,uanswerarray,answer,"MEDIUM")
            

        elif j == [2]:
            flag  = flag  + 2
           
            if flag>1: #If already accessed with global country selected the change the name
                currency(random.choice(cmedium),uanswerarray,answer,"MEDIUM")
                
            else:
                currency(country,uanswerarray,answer,"MEDIUM")
                
        elif j == [3]:
            flag  = flag  + 2
            if flag > 1: #If already accessed with global country selected the change the name
                officialang(random.choice(cmedium),uanswerarray,answer,"MEDIUM")
                
            else:
                officialang(country,uanswerarray,answer,"MEDIUM")
                
        elif j == [4]:
            flag  = flag  + 2
            if flag > 1: #If already accessed with global country selected the change the name
                headofgovt(random.choice(cmedium),uanswerarray,answer,"MEDIUM")
            
            else:
                headofgovt(country,uanswerarray,answer,"MEDIUM")
            
    return answer,uanswerarray

def questionslevelhard(): # Function will create 5 questions randomly
   
    answer = [ ] # Storing correct answer
    uanswerarray = [ ] # Storing user answer
    
    for i in range(5): # Can change number of questions from here
        j = random.sample(funcnum,1)
        country = random.choice(chard)
        flag = 0
        #print(j)
        if j == [1]:
            flag = flag + 2
            if flag  > 1: #If already accessed with global country selected the change the name
                capital(random.choice(chard),uanswerarray,answer,"HARD")
                
            else:
                capital(country,uanswerarray,answer,"HARD")
            

        elif j == [2]:
            flag  = flag  + 2
            if flag > 1: #If already accessed with global country selected the change the name
                currency(random.choice(cmedium),uanswerarray,answer,"HARD")
                
            else:
                currency(country,uanswerarray,answer,"HARD")
                
        elif j == [3]:
            flag  = flag  + 2
            if flag  > 1: #If already accessed with global country selected the change the name
                officialang(random.choice(cmedium),uanswerarray,answer,"HARD")
                
            else:
                officialang(country,uanswerarray,answer,"HARD")
                
        elif j == [4]:
            flag  = flag  + 2
            if flag > 1: #If already accessed with global country selected the change the name
                headofgovt(random.choice(cmedium),uanswerarray,answer,"HARD")
            
            else:
                headofgovt(country,uanswerarray,answer,"HARD")
            
    return answer,uanswerarray


def calleasy():
          score = 0
          answer=[]
          unanswerarray= []
          answer,unanswerarray = questionsleveleasy() # Return array of user and actual answer 
          for j in range(5):
           
                a = unanswerarray[j]
                b = answer[j]
                
                if a == b: # Comparing user answer and actual answer
                    score += 1
          print("\n{0}, you scored {1} out of {2}.".format(name, score,5)) # printing the score
          return score

def callmedium():
                print("Welcome to medium level")
                score = 0
                answer=[]
                unanswerarray= []
                answer,unanswerarray = questionslevelmedium() # Return array of user and actual answer 
                for j in range(5):
                
                    a = unanswerarray[j]
                    b = answer[j]
                    
                    if a == b: # Comparing user answer and actual answer
                        score += 1
                print("\n{0}, you scored {1} out of {2}.".format(name, score,5)) # printing the score        
                return score

def callhard():
                print("Welcome to hard level")
                score = 0
                answer=[]
                unanswerarray= []
                answer,unanswerarray = questionslevelhard() # Return array of user and actual answer 
                for j in range(5):
                
                    a = unanswerarray[j]
                    b = answer[j]
                    
                    if a == b: # Comparing user answer and actual answer
                        score += 1
                print("\n{0}, you scored {1} out of {2}.".format(name, score,5)) # printing the score
                return score
curscore =0

def easy():
    curscore = calleasy()
    if(curscore > 3):
            medium()
    else:
        easy()
 
def medium():  
    curscore =  callmedium()
    if curscore > 3:
            hard()
    else:
            medium()
def hard():
    curscore = callhard()
    if(curscore < 4):
        medium()


name = input("Please enter your name: ").title()
aq = input("Please enter number of times you like to play the quiz: ") # Number of times you want to attempt the quiz

lenq = 5
def run_quiz(aq):
    
     x = 0
     while (x < int(aq)):
          easy()
          


          print("\nAttempt: " + str(x+1)) # Printing number of attempt 
         #print("\n{0}, you scored {1} out of {2}.".format(name, score,5)) # printing the score
          x = x + 1
          
          
           



run_quiz(aq) # Starting the quiz









