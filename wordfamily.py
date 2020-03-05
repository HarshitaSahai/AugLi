from xlrd import open_workbook
import pandas as pd
import numpy as np
import csv

import collections

df_csv = pd.read_csv('level2 + syllable + word filter.csv')
ftCol = df_csv.iloc[:, 0].values
var = len(ftCol)
book = open_workbook("families.xlsx")
worksheet = book.sheet_by_name('view')
array = np.array(var)
def rowval(word):
    result = 0
    for sheet in book.sheets():

        for rowidx in range(sheet.nrows):
        
                row = sheet.row(rowidx)
                for colidx, cell in enumerate(row):
                    if cell.value == word :
                        for j in range(var):
                            result = rowidx
                            
    return result
print(ftCol)
print("Calling function")
new_array =   np.append(array,[rowval(i) for i in ftCol])
print(new_array)
new_array[0] = 0
df_csv = pd.DataFrame(columns=['Word family'])
for i in range(var) :
     row = worksheet.row(new_array[i])
    
     df_csv.loc[i] = row[0].value
df_csv.to_csv('oooo.csv', index=False, mode= 'w')

