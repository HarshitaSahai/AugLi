from xlrd import open_workbook
import pandas as pd
import numpy as np
import csv
import collections

dataset = pd.read_csv('level6 + syllable + word family.csv')# The respective file names
ftCol = dataset.iloc[:, 0].values
print("enter")
book = open_workbook("badwordlist.xlsx")# badword dataset
array=[]
def badword(word):
    result = 0      #if 0 the word good else any value bad
    for sheet in book.sheets():

        for rowidx in range(sheet.nrows):
        
                row = sheet.row(rowidx)
                for colidx, cell in enumerate(row):
                    if cell.value == word :
                        for j in range(1):
                            result = rowidx
                            
    return result
                
print(ftCol)
var = len(ftCol)
print("Calling function")
array.append([badword(i) for i in ftCol])
print(array) 

    


