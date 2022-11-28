# import pandas lib as pd
# import pandas as pd

# read by default 1st sheet of an excel file
# dataframe1 = pd.read_excel('Book1.xlsx')

# print(dataframe1)

# Python3 code to select
# data from excel
import xlwings as xw

# Specifying a sheet
ws = xw.Book("Book1.xlsx").sheets['Sheet1']

# Selecting data from
# a single cell
v1 = ws.range("A1:A4").value
v2 = ws.range("B2").value
print("Result:", v1, v2)

#import xlrd
#location = "D:\\Python Programs\\Book1.xlsx"
#wb = xlrd.open_workbook(location)
#sheet = wb.sheet_by_index(1)
#print(sheet.cell_value(1, 1))


