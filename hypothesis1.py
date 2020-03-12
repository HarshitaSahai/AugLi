from nltk.corpus import words
import pandas as pd
import numpy as np
df_csv1 = pd.read_csv('hypoexample5.csv')# Meaning of level mentioned
ftCol = df_csv1.iloc[:, 0].values
df_csv2 = pd.read_csv('hyposample.csv')# Extracted 5 words from each level
ftCol2 = df_csv2.iloc[:, 0].values



for l in ftCol:
 
    for j in ftCol2:
      
        if(l.find(j)!= -1): # Checking if our word is found and then seeing the level number
            print(j) #Printing the value which was found
            print(l) #Printing the meaning in which the word was found
            print ("found")

















