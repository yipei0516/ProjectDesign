import openpyxl
import pandas as pd
wb = openpyxl.load_workbook('Result.xlsx')
ws = wb['try']
A_col = ws['A']

# df = pd.read_excel("Result.xlsx", sheet_name='try')
# print(df)
print(type(A_col))
print()
print(type(A_col[1]))
print()
print(A_col[:])
print()
for i in A_col:
    print(i.value)