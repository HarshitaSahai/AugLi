import random 
import pandas as pd
import numpy as np

df_csv1 = pd.read_csv('countrylangcurrencyhoc.csv',encoding='cp1252')
cn = df_csv1.iloc[:,0].values
cc = df_csv1.iloc[:,1].values
ccu = df_csv1.iloc[:,2].values
col = df_csv1.iloc[:,3].values
chog = df_csv1.iloc[:,4].values


def capital(country,uanswerarray,answer): #Function to find capital
    
    print("what is the capital of " + country)
    cnl = cn.tolist()
    countryi =cnl.index(country)
    ans = cc[countryi]
    print("A) " + ans)
    if countryi - 1 != 0:
        print("B) " + cc[countryi - 1])
    else:
        print("B) " + cc[countryi + 1]) 
    uanswer = input()
    uanswerarray.append(uanswer)
    answer.append('A')

def currency(country,uanswerarray,answer): #Function to find currency 
    print("what is the currency of " + country)
    ccul = cn.tolist()
    currencyi =ccul.index(country)
    ans  = ccu[currencyi]
    print("A) " + ans)
    if currencyi - 1 != 0:
        print("B) " + cc[currencyi - 1])
    else:
        print("B) " + cc[currencyi + 1]) 
    uanswer = input()
    uanswerarray.append(uanswer)
    answer.append('A')

    
def officialang(country,uanswerarray,answer): #Function to find language
    print("what is the official language of " + country)
    coll = cn.tolist()
    languagei =coll.index(country)
    ans = col[languagei]
    print("A) " + ans)
    if languagei - 1 != 0:
        print("B) " + cc[languagei - 1])
    else:
        print("B) " + cc[languagei  + 1]) 
    uanswer = input()
    uanswerarray.append(uanswer)
    answer.append('A')

def headofgovt(country,uanswerarray,answer): #Function to find head of government
    print("who is the head of govt of " + country)
    chogl = cn.tolist()
    headi =chogl.index(country)
    ans = chog[headi]
    print("A) " + ans)
    if headi - 1 != 0:
        print("B) " + cc[headi - 1])
    else:
        print("B) " + cc[headi + 1]) 
    uanswer = input()
    uanswerarray.append(uanswer)
    answer.append('A')


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









