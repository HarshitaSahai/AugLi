from xlrd import open_workbook
import pandas as pd
import numpy as np
import csv

import collections
df_csv = pd.read_csv('level1 + syllable.csv')
ftCol = df_csv.iloc[:, 0].values
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
var = len(array)
print(array) 
list1 = {'Names':array}
df = pd.DataFrame(list1)
df_csv = pd.DataFrame(columns=['Word family'])
for i in range(var) :
     df_csv.loc[i] = [array[i][i]]
df_csv.to_csv('oooo.csv', index=False, mode= 'w')

