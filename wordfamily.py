from xlrd import open_workbook
import pandas as pd
import numpy as np
import csv

import collections
dataset = pd.read_csv('trywf.csv')
ftCol = dataset.iloc[:, 0].values

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
print("fn")
for j in range(10):
   array.append([rowval(i) for i in ftCol])

print(array)
