import ezsheets

print(ezsheets.listSpreadsheets())

ss = ezsheets.Spreadsheet("1ONNc2NBAWBcVS5Jd9x7wRYQ5zfg62wZ_sO2OqrRbvtE")
print(ss.title)
print(ss.id)
print(ss.url)

print(ss.sheetTitles)
print(ss.sheets)


sheet: ezsheets.Sheet = ss.sheets[0]
sheet["A1"] = "Name"
sheet["B1"] = "Age"
sheet["C1"] = "Favorite Movie"

print(sheet[3, 1])

print(ezsheets.convertAddress("A2"))
print(ezsheets.convertAddress(1, 2))

print(ezsheets.getColumnLetterOf(2))
print(ezsheets.getColumnNumberOf("B"))

print(ezsheets.getColumnLetterOf(999))
print(ezsheets.getColumnNumberOf("XXX"))

sheet.updateRow(2, ["Carlos", 20, "Scarface"])

row_one = sheet.getRow(1)
print(row_one)

print(sheet.rowCount)
print(sheet.columnCount)

sheet.rowCount = 2
sheet.columnCount = 3

sheet.updateRow(3, ["Trent", 26, "Gol"])

if "second sheet" not in ss.sheetTitles:
    second_sheet: ezsheets.Sheet = ss.Sheet("second sheet", 1, 5, 5)
else:
    second_sheet: ezsheets.Sheet = ss.sheets[1]

print("----------------------------")
print(second_sheet.title)

header = sheet.getRow(1)

for index, value in enumerate(header):
    header[index] = value.upper()

sheet.updateRow(1, header)

column_one = sheet.getColumn(1)

for index, value in enumerate(column_one):
    column_one[index] = value.upper()

sheet.updateColumn(1, column_one)
