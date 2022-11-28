
import openpyxl
# to load the workbook with its path
bk = openpyxl.load_workbook(“D:\Python Programs\Book1.xlsx”)
# to identify active worksheet
s = bk.active
# to identify the cell
c = s.cell (row = 3, column = 1)
# to retrieve the cell value and print
print ( c.value)