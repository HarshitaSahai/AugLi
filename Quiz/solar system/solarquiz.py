import random 
import pandas as pd
import numpy as np
import cgi
import sys
import csv
import gspread 

df_csv1 = pd.read_csv('solarsystem.csv',encoding='cp1252',sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
pn = df_csv1.iloc[0:8,0].values # planet names
pnfor = df_csv1.iloc[0:9,1].values # Named for
pdiameter = df_csv1.iloc[0:9,2].values # Diameter
psat = df_csv1.iloc[0:9,3].values # Number of satellites (moons)
protp = df_csv1.iloc[0:9,4].values # Rotation period (planet rotates on its axis)
prevop = df_csv1.iloc[0:9,5].values # Revolution period (planet completes one orbit)
ptemp = df_csv1.iloc[0:9,6].values # Revolution period (planet completes one orbit)
patomc = df_csv1.iloc[0:9,7].values # Atmospheric composition (air surrounding planet made of)
prings = df_csv1.iloc[0:9,8].values # Number of rings
porderfromsun = df_csv1.iloc[0:9,9].values # Sequential order from the sun.
porderfromsize = df_csv1.iloc[0:9,10].values # Order by size (largest to smallest)
pcomp = df_csv1.iloc[0:9,11].values # Composition (planet made of)

df_csv = pd.DataFrame(columns=['Questions'])


file = open('solarsystemans.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(["Question", "Option 1", "Option 2","Option 3","Option 4","Correct answer","Question type"])
def datawrite(ques,f,s,t,f4,cans,qtype):
    

        
        writer.writerow([ques, f, s,t,f4,cans,qtype])
    


def namedfor(planet,uanswerarray,answer): #Function to find name for
 
    print("what is " + planet + " named for ? ")
    qtype = "static"
    pnl = pn.tolist()
    planeti =pnl.index(planet)
    ans = pnfor[planeti]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
   
    ques = "what is " + planet + " named for ? "
    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if planeti - 1 != 0 :
            f = pnfor[planeti-1]
            print("A) " + f)
        else:
            f = pnfor[planeti+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if planeti - 2 != 0 :
            s = pnfor[planeti-2]
            print("B) " + s)
        else:
            s = pnfor[planeti+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if planeti - 3 != 0 :
            t = pnfor[planeti-3]
            print("C) " + t)
        else:
            t = pnfor[planeti+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if planeti - 4!= 0 :
            f4 = pnfor[planeti-4]
            print("D) " + f4)
        else:
            f4 = pnfor[planeti+4]
            print("D) " + f4)
    cans = ans
    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def diameter(planet,uanswerarray,answer): #Function to find diameter
   
    print("what is the diameter of " + planet + " ? ")
    ques = "what is the diameter of " + planet + " ? "
    pdiameterl = pn.tolist()
    qtype = "static"
    diameteri =pdiameterl.index(planet)
    ans  = pdiameter[diameteri]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
  

    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if diameteri - 1 != 0 :
            f = pdiameter[diameteri-1]
            print("A) " + f)
        else:
            f = pdiameter[diameteri+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if diameteri - 2 != 0 :
            s = pdiameter[diameteri-2]
            print("B) " + s)
        else:
            s = pdiameter[diameteri+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if diameteri - 3 != 0 :
            t = pdiameter[diameteri-3]
            print("C) " + t)
        else:
            t = pdiameter[diameteri+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if diameteri - 4!= 0 :
            f4 = pdiameter[diameteri-4]
            print("D) " + f4)
        else:
            f4 = pdiameter[diameteri+4]
            print("D) " + f4)
    cans = ans

    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def satellite(planet,uanswerarray,answer): #Function to find satellite
    
    print("what is the diameter of "  + planet + " ? ")
    pnl = pn.tolist()
    planeti =pnl.index(planet)
    ans = psat[planeti]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
   
    ques = "what is the diameter of " + planet + " ? "
    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if planeti - 1 != 0 :
            f = psat[planeti-1]
            print("A) " + f)
        else:
            f = psat[planeti+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if planeti - 2 != 0 :
            s = psat[planeti-2]
            print("B) " + s)
        else:
            s = psat[planeti+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if planeti - 3 != 0 :
            t = psat[planeti-3]
            print("C) " + t)
        else:
            t = psat[planeti+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if planeti - 4!= 0 :
            f4 = psat[planeti-4]
            print("D) " + f4)
        else:
            f4 = psat[planeti+4]
            print("D) " + f4)
    qtype = "dynamic"
    cans = ans
    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 




def rotation(planet,uanswerarray,answer): #Function to find rotation
    
    print("what is the rotation period of "  + planet + " ? ")
    pnl = pn.tolist()
    planeti =pnl.index(planet)
    ans = protp[planeti]
    options = ['A','B','C','D']
    qtype = "static"
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
   
    ques = "what is the rotation period of " + planet + " ? "
    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if planeti - 1 != 0 :
            f = protp[planeti-1]
            print("A) " + f)
        else:
            f = protp[planeti+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if planeti - 2 != 0 :
            s = protp[planeti-2]
            print("B) " + s)
        else:
            s = protp[planeti+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if planeti - 3 != 0 :
            t = protp[planeti-3]
            print("C) " + t)
        else:
            t = protp[planeti+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if planeti - 4!= 0 :
            f4 = protp[planeti-4]
            print("D) " + f4)
        else:
            f4 = protp[planeti+4]
            print("D) " + f4)
    cans = ans
    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def revolution(planet,uanswerarray,answer): #Function to find revolution
    
    print("what is the revolution period of "  + planet + " ? ")
    pnl = pn.tolist()
    planeti =pnl.index(planet)
    qtype = "static"
    ans = prevop[planeti]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
   
    ques = "what is the revolution period of " + planet + " ? "
    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if planeti - 1 != 0 :
            f = prevop[planeti-1]
            print("A) " + f)
        else:
            f = prevop[planeti+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if planeti - 2 != 0 :
            s = prevop[planeti-2]
            print("B) " + s)
        else:
            s = prevop[planeti+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if planeti - 3 != 0 :
            t = prevop[planeti-3]
            print("C) " + t)
        else:
            t = prevop[planeti+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if planeti - 4!= 0 :
            f4 = prevop[planeti-4]
            print("D) " + f4)
        else:
            f4 = prevop[planeti+4]
            print("D) " + f4)
    cans = ans
    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def temperature(planet,uanswerarray,answer): #Function to find temperature
    
    print("what is the minimum and maximum tempertaure (F°) for "  + planet + " ? ")
    pnl = pn.tolist()
    planeti =pnl.index(planet)
    ans = ptemp[planeti]
    options = ['A','B','C','D']
    qtype = "dynamic"
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
   
    ques = "what is the minimum and maximum tempertaure (F°) for " + planet + " ? "
    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if planeti - 1 != 0 :
            f = ptemp[planeti-1]
            print("A) " + f)
        else:
            f = ptemp[planeti+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if planeti - 2 != 0 :
            s = ptemp[planeti-2]
            print("B) " + s)
        else:
            s = ptemp[planeti+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if planeti - 3 != 0 :
            t = ptemp[planeti-3]
            print("C) " + t)
        else:
            t = ptemp[planeti+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if planeti - 4!= 0 :
            f4 = ptemp[planeti-4]
            print("D) " + f4)
        else:
            f4 = ptemp[planeti+4]
            print("D) " + f4)
    cans = ans
    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def atomcomposition(planet,uanswerarray,answer): #Function to find atmospheric composition
    
    print("what is the atmospheric compostion for "  + planet + " ? ")
    pnl = pn.tolist()
    planeti =pnl.index(planet)
    ans = patomc[planeti]
    options = ['A','B','C','D']
    qtype = "static"
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
   
    ques = "what is the atmospheric compostion for " + planet + " ? "
    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if planeti - 1 != 0 :
            f = patomc[planeti-1]
            print("A) " + f)
        else:
            f = patomc[planeti+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if planeti - 2 != 0 :
            s = patomc[planeti-2]
            print("B) " + s)
        else:
            s = patomc[planeti+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if planeti - 3 != 0 :
            t = patomc[planeti-3]
            print("C) " + t)
        else:
            t = patomc[planeti+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if planeti - 4!= 0 :
            f4 = patomc[planeti-4]
            print("D) " + f4)
        else:
            f4 = patomc[planeti+4]
            print("D) " + f4)
    cans = ans
    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def rings(planet,uanswerarray,answer): #Function to find number of rings
    
    qtype = "static"
    print("What are the number of rings in "  + planet + " ? ")
    pnl = pn.tolist()
    planeti =pnl.index(planet)
    ans = prings[planeti]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
   
    ques = "What are the number of rings in "  + planet + " ? "
    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if planeti - 1 != 0 :
            f = "4"
            print("A) " + f)
        else:
            f = "4"
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if planeti - 2 != 0 :
            s = "2"
            print("B) " + s)
        else:
            s = "2"
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if planeti - 3 != 0 :
            t = "10"
            print("C) " + t)
        else:
            t = "10"
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if planeti - 4!= 0 :
            f4 = "3"
            print("D) " + f4)
        else:
            f4 = "3"
            print("D) " + f4)
    cans = ans
    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def orderfromsun(planet,uanswerarray,answer): #Function to find position from sun
    
    print("What is the position of " + planet + " from the sun ? ")
    qtype = "dynamic"
    pnl = pn.tolist()
    planeti =pnl.index(planet)
    ans = porderfromsun[planeti]
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
   
    ques = "What is the position of " + planet + " from the sun ? "
    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if planeti - 1 != 0 :
            f = porderfromsun[planeti-1]
            print("A) " + f)
        else:
            f = porderfromsun[planeti+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if planeti - 2 != 0 :
            s = porderfromsun[planeti-2]
            print("B) " + s)
        else:
            s = porderfromsun[planeti+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if planeti - 3 != 0 :
            t = porderfromsun[planeti-3]
            print("C) " + t)
        else:
            t = porderfromsun[planeti+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if planeti - 4!= 0 :
            f4 = porderfromsun[planeti-4]
            print("D) " + f4)
        else:
            f4 = porderfromsun[planeti+4]
            print("D) " + f4)
    cans = ans
    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def orderfromsize(planet,uanswerarray,answer): #Function to order of planets by size 
    
    print("What is the rank of " + planet + " when planets are arranged largest to smallest in size ? ")
    pnl = pn.tolist()
    planeti =pnl.index(planet)
    ans = porderfromsize[planeti]
    qtype = "static"
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
   
    ques = "What is the rank of " + planet + " when planets are arranged largest to smallest in size ? "
    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if planeti - 1 != 0 :
            f = porderfromsize[planeti-1]
            print("A) " + f)
        else:
            f = porderfromsize[planeti+1]
            print("A) " + f)
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if planeti - 2 != 0 :
            s = porderfromsize[planeti-2]
            print("B) " + s)
        else:
            s = porderfromsize[planeti+2]
            print("B) " + s)
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if planeti - 3 != 0 :
            t = porderfromsize[planeti-3]
            print("C) " + t)
        else:
            t = porderfromsize[planeti+3]
            print("C) " + t)
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if planeti - 4!= 0 :
            f4 = porderfromsize[planeti-4]
            print("D) " + f4)
        else:
            f4 = porderfromsize[planeti+4]
            print("D) " + f4)
    cans = ans
    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 

def composition(planet,uanswerarray,answer): #Function to composition 
    print("What is the composition of " + planet + " ? ")
    pnl = pn.tolist()
    planeti =pnl.index(planet)
    ans = pcomp[planeti]
    qtype = "static"
    options = ['A','B','C','D']
    ansv = random.choice(options) # selecting option for answer
    #print(ansv)
    ansi = options.index(ansv) # finding its index in options
    del options[ansi] # deleting that option
   
    ques = "What is the composition of " + planet + " ? "
    if ansv == 'A':
        print("A) " + ans)
        f = ans
    else:
        if planeti - 1 != 0 :
            f = "Only metal"
            print("A) " + str(f))
        else:
            f = "Only metal"
            print("A) " + str(f))
    if ansv == 'B':
        print("B) " + ans)
        s = ans
    else:
        if planeti - 2 != 0 :
            s = "Only rock"
            print("B) " + str(s))
        else:
            s = "Only rock"
            print("B) " + str(s))
    if ansv == 'C':
        print("C) " + ans)
        t = ans
    else:
        if planeti - 3 != 0 :
            t = "Only hydrogen"
            print("C) " + str(t))
        else:
            t = "Only hydrogen"
            print("C) " + str(t))
    if ansv == 'D':
        f4 = ans
        print("D) " + ans)
    else:
        if planeti - 4!= 0 :
            f4 = "Only helium"
            print("D) " + str(f4))
        else:
            f4 = "Only helium"
            print("D) " + str(f4))
    cans = ans
    uanswer = input()
    datawrite(ques,f,s,t,f4,cans,qtype)
    uanswerarray.append(uanswer)
    answer.append(ansv)         # Appending the answer option in array 









funpnum = [1,2,3,4,5,6,7,8,9,10,11]

def questions(): # Function will create 5 questions randomly
 
    one = 0
    two = 0
    three = 0
    four = 0
    five  = 0
    six =0
    seven = 0
    eight = 0
    nine = 0
    ten = 0 
    eleven = 0
    answer = [ ] # Storing correct answer
    uanswerarray = [ ] # Storing user answer
    planet = random.choice(pn)
    for i in range(5): # Can change number of questions from here
        j = random.sample(funpnum,1)
        #print(j)
        if j == [1]:
            one = one + 1
            if one > 1: #If already accessed with global planet selected the change the name
                namedfor(random.choice(pn),uanswerarray,answer)
                
            else:
                namedfor(planet,uanswerarray,answer)
            

        elif j == [2]:
            two = two + 1
            if two > 1: #If already accessed with global planet selected the change the name
                diameter(random.choice(pn),uanswerarray,answer)
                
            else:
                diameter(planet,uanswerarray,answer)
        elif j == [3]:
            three = three + 1
            if three > 1: #If already accessed with global planet selected the change the name
                satellite(random.choice(pn),uanswerarray,answer)
                
            else:
                satellite(planet,uanswerarray,answer)
        elif j == [4]:
            four = four + 1
            if four > 1: #If already accessed with global planet selected the change the name
                rotation(random.choice(pn),uanswerarray,answer)
                
            else:
                rotation(planet,uanswerarray,answer)
        elif j == [5]:
            five = five + 1
            if five > 1: #If already accessed with global planet selected the change the name
                revolution(random.choice(pn),uanswerarray,answer)
                
            else:
                revolution(planet,uanswerarray,answer)
        elif j == [6]:
            six = six + 1
            if six > 1: #If already accessed with global planet selected the change the name
                temperature(random.choice(pn),uanswerarray,answer)
                
            else:
                temperature(planet,uanswerarray,answer)
        elif j == [7]:
            seven = seven + 1
            if seven > 1: #If already accessed with global planet selected the change the name
                atomcomposition(random.choice(pn),uanswerarray,answer)
                
            else:
                atomcomposition(planet,uanswerarray,answer)
        elif j == [8]:
            eight = eight + 1
            if eight > 1: #If already accessed with global planet selected the change the name
                rings(random.choice(pn),uanswerarray,answer)
                
            else:
                rings(planet,uanswerarray,answer)
        elif j == [9]:
            nine = nine + 1
            if nine > 1: #If already accessed with global planet selected the change the name
                orderfromsun(random.choice(pn),uanswerarray,answer)
                
            else:
                orderfromsun(planet,uanswerarray,answer)
        elif j == [10]:
            ten = ten + 1
            if ten > 1: #If already accessed with global planet selected the change the name
                orderfromsize(random.choice(pn),uanswerarray,answer)
                
            else:
                orderfromsize(planet,uanswerarray,answer)
        elif j == [11]:
            eleven = eleven + 1
            if eleven > 1: #If already accessed with global planet selected the change the name
                composition(random.choice(pn),uanswerarray,answer)
                
            else:
                composition(planet,uanswerarray,answer)
            
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
