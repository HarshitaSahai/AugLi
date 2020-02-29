from xlrd import open_workbook
import pandas as pd
import numpy as np
import csv

import collections
dataset = pd.read_csv('level1 + syllable.csv')# The respective file names
ftCol = dataset.iloc[:, 0].values
df = pd.read_excel("families.xlsx") # The dataset
print("enter")
book = open_workbook("families.xlsx")
array=[]
def rowval(word):
    result = 0
    for sheet in book.sheets():

        for rowidx in range(sheet.nrows):
        
                row = sheet.row(rowidx)
                for colidx, cell in enumerate(row):
                    if cell.value == word :
                        for j in range(1):
                            result = rowidx
                            
    return result
                
           
print(ftCol)
print("Calling function")

array.append([rowval(i) for i in ftCol])

print(array) # Array containing the row value in the dataset 


