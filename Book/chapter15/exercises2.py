# ======================================================================
# 📊 EZSHEETS EXERCISES - Google Sheets Automation
# ======================================================================
# Practice exercises - Write everything from scratch!
# Prerequisites: ezsheets installed, Google account configured
# ======================================================================

import ezsheets

# =====================================================================
#                    SECTION 1: SPREADSHEET BASICS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 1: CREATE A NEW SPREADSHEET
#
# Learn: ezsheets.createSpreadsheet()
#
# Tasks:
# 1. Create a new spreadsheet with a title
# 2. Print the spreadsheet ID
# 3. Print the spreadsheet URL
# 4. Verify it appears in your Google Drive
# ----------------------------------------------------------------------

# ss = ezsheets.Spreadsheet()
# if "exercises2" not in ss.sheetTitles:
#     ss.title = "exercises2"
# print(ss.id)
# print(ss.url)

# ----------------------------------------------------------------------
# 🟢 2: OPEN AN EXISTING SPREADSHEET
#
# Learn: ezsheets.Spreadsheet()
#
# Tasks:
# 1. Open a spreadsheet using its ID
# 2. Open a spreadsheet using its URL
# 3. Print the spreadsheet title
# 4. Print how many sheets it contains
# ----------------------------------------------------------------------

ss = ezsheets.Spreadsheet("1mNyMKZtmzbVPD4TFPeGyGhAw3-kZn61FszxcWnHEaXw")
print(ss.title)

ss = ezsheets.Spreadsheet(
    "https://docs.google.com/spreadsheets/d/1mNyMKZtmzbVPD4TFPeGyGhAw3-kZn61FszxcWnHEaXw/edit?gid=0#gid=0"
)
print(ss.title)

print(f"{ss.title} contains {len(ss.sheetTitles)} sheets")

# ----------------------------------------------------------------------
# 🟢 3: SPREADSHEET PROPERTIES
#
# Learn: Spreadsheet attributes
#
# Tasks:
# 1. Open a spreadsheet
# 2. Access and print the title
# 3. Change the title to something new
# 4. Print the spreadsheet ID
# 5. List all sheet names in the spreadsheet
# ----------------------------------------------------------------------

# print(ss.title)
# ss.title = "titled_changed"
# print(ss.title)
# print(ss.id)
# print(ss.sheetTitles)

# ----------------------------------------------------------------------
# 🟡 4: LIST ALL SPREADSHEETS
#
# Learn: ezsheets.listSpreadsheets()
#
# Tasks:
# 1. Get a dictionary of all spreadsheets in your account
# 2. Print each spreadsheet ID and title
# 3. Count total number of spreadsheets
# 4. Find a specific spreadsheet by title
# ----------------------------------------------------------------------

all_spreadsheets = ezsheets.listSpreadsheets()

for id, title in all_spreadsheets.items():
    print(f"Spreadsheet with ID:{id} and title:{title}")

print(
    f"You have {len(all_spreadsheets)} of spreadsheets on your account (the ones in trash are counted, too)"
)

assert "titled_changed" in all_spreadsheets.values()

# =====================================================================
#                    SECTION 2: WORKING WITH SHEETS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 5: ACCESS SHEETS
#
# Learn: Accessing sheets by index and name
#
# Tasks:
# 1. Open a spreadsheet
# 2. Access the first sheet using index [0]
# 3. Access a sheet by its name
# 4. Print the sheet title
# 5. Print sheet dimensions (rows and columns)
# ----------------------------------------------------------------------

sheet: ezsheets.Sheet = ss.sheets[0]
print(sheet.title)
print(sheet.id)

sheet = ss["new_title"]
print(sheet.title)
print(sheet.id)

print(
    f"The sheet {sheet.title} has dimensions: {sheet.rowCount} rows and {sheet.columnCount} columns"
)

# ----------------------------------------------------------------------
# 🟡 6: CREATE AND DELETE SHEETS
#
# Learn: createSheet(), delete()
#
# Tasks:
# 1. Open a spreadsheet
# 2. Create a new sheet with a specific name
# 3. Create a sheet at a specific index position
# 4. List all sheets to verify
# 5. Delete a sheet by name or index
# ----------------------------------------------------------------------

if "created_sheet" not in ss.sheetTitles:
    ss.createSheet(title="created_sheet")
if "another_sheet" not in ss.sheetTitles:
    ss.createSheet(title="another_sheet", index=0)

print(ss.sheets)

ss["another_sheet"].delete()
ss.sheets[1].delete()

# ----------------------------------------------------------------------
# 🟡 7: SHEET PROPERTIES
#
# Learn: Sheet attributes and methods
#
# Tasks:
# 1. Access a sheet
# 2. Get and print the sheet title
# 3. Change the sheet title
# 4. Get row count and column count
# 5. Resize the sheet (change row/column count)
# ----------------------------------------------------------------------

print("SEVEN")
print(sheet.title)

if "new_title" not in ss.sheetTitles:
    sheet.title = "new_title"

print(f"Dimensions before change: {sheet.rowCount}X{sheet.columnCount}")

sheet.rowCount = 8
sheet.columnCount = 8

print(f"Dimensions after change: {sheet.rowCount}X{sheet.columnCount}")

# ----------------------------------------------------------------------
# 🟡 8: COPY SHEETS
#
# Learn: Copying sheets within and between spreadsheets
#
# Tasks:
# 1. Open a spreadsheet with data
# 2. Copy a sheet to create a backup within same spreadsheet
# 3. Copy a sheet to a different spreadsheet
# 4. Verify the copy contains the same data
# ----------------------------------------------------------------------

als_ss = ezsheets.Spreadsheet("https://autbor.com/examplegs")
als_sheet: ezsheets.Sheet = als_ss[0]

if "Copy of Books" not in ss.sheetTitles:
    als_sheet.copyTo(ss)

copy_sheet: ezsheets.Sheet = ss["Copy of Books"]

for copy_sheet_row, als_sheet_row in zip(copy_sheet.getRows(), als_sheet.getRows()):
    for copy_sheet_cell, als_sheet_cell in zip(copy_sheet_row, als_sheet_row):
        if copy_sheet_cell != als_sheet_cell:
            print("The backup is broken")
            break

# =====================================================================
#                    SECTION 3: READING DATA
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 9: READ SINGLE CELLS
#
# Learn: Accessing individual cells
#
# Tasks:
# 1. Access a sheet with data
# 2. Read cell A1 using index notation
# 3. Read cell B2 using index notation
# 4. Read using column letter and row number
# 5. Print the values
# ----------------------------------------------------------------------

print(als_sheet["A1"])
print(als_sheet[1, 1])

print(als_sheet["B2"])
print(als_sheet[2, 2])

# ----------------------------------------------------------------------
# 🟢 10: READ ROWS AND COLUMNS
#
# Learn: getRow(), getColumn()
#
# Tasks:
# 1. Access a sheet with data
# 2. Get entire row 1 as a list
# 3. Get entire column A as a list
# 4. Get row 5
# 5. Print the data from each
# ----------------------------------------------------------------------

copy_sheet.rowCount = 11
copy_sheet.columnCount = 4

row_1 = copy_sheet.getRow(1)
column_a = copy_sheet.getColumn(ezsheets.getColumnNumberOf("a"))

row_5 = copy_sheet.getRow(5)

print(row_1)
print(column_a)
print(row_5)

# ----------------------------------------------------------------------
# 🟡 11: READ ALL DATA
#
# Learn: getRows(), getColumns()
#
# Tasks:
# 1. Access a sheet with multiple rows of data
# 2. Get all rows as a list of lists
# 3. Get all columns as a list of lists
# 4. Iterate through and print all data
# 5. Count total cells with data
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 12: FIND SPECIFIC DATA
#
# Learn: Searching through sheet data
#
# Tasks:
# 1. Access a sheet with data
# 2. Find all cells containing a specific value
# 3. Find the row number where a value exists
# 4. Find all rows matching a criteria
# 5. Print the locations of found data
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 4: WRITING DATA
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 13: WRITE SINGLE CELLS
#
# Learn: Writing to individual cells
#
# Tasks:
# 1. Access a sheet
# 2. Write a string to cell A1
# 3. Write a number to cell B1
# 4. Write to cell C1 using different notation
# 5. Verify the values were written
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 14: WRITE ROWS AND COLUMNS
#
# Learn: updateRow(), updateColumn()
#
# Tasks:
# 1. Access a sheet
# 2. Update entire row 1 with a list of values
# 3. Update entire column A with a list of values
# 4. Update row 3 with different data
# 5. Verify all updates
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 15: WRITE MULTIPLE ROWS
#
# Learn: updateRows()
#
# Tasks:
# 1. Create a list of lists (table data)
# 2. Write all rows to the sheet at once
# 3. Verify the data was written correctly
# 4. Clear and rewrite with different data
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 16: CLEAR DATA
#
# Learn: Clearing cells and sheets
#
# Tasks:
# 1. Access a sheet with data
# 2. Clear a single cell
# 3. Clear an entire row
# 4. Clear an entire column
# 5. Clear all data from the sheet
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 5: ROWS AND COLUMNS OPERATIONS
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 17: INSERT AND DELETE ROWS
#
# Learn: Row manipulation
#
# Tasks:
# 1. Access a sheet with data
# 2. Insert a blank row at position 2
# 3. Insert multiple blank rows
# 4. Delete a specific row
# 5. Verify data shifted correctly
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 18: INSERT AND DELETE COLUMNS
#
# Learn: Column manipulation
#
# Tasks:
# 1. Access a sheet with data
# 2. Insert a blank column at position B
# 3. Insert multiple blank columns
# 4. Delete a specific column
# 5. Verify data shifted correctly
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 19: RESIZE SHEET
#
# Learn: Changing sheet dimensions
#
# Tasks:
# 1. Access a sheet
# 2. Get current row and column count
# 3. Increase the number of rows
# 4. Increase the number of columns
# 5. Decrease the size (be careful with data!)
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 6: DOWNLOAD AND UPLOAD
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 20: DOWNLOAD AS EXCEL
#
# Learn: downloadAsExcel()
#
# Tasks:
# 1. Open a spreadsheet with data
# 2. Download as Excel file (.xlsx)
# 3. Specify a custom filename
# 4. Verify the file was created locally
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 21: DOWNLOAD AS CSV
#
# Learn: downloadAsCSV()
#
# Tasks:
# 1. Open a spreadsheet with multiple sheets
# 2. Download a specific sheet as CSV
# 3. Download with custom filename
# 4. Open and verify CSV contents
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 22: DOWNLOAD OTHER FORMATS
#
# Learn: downloadAsODS(), downloadAsTSV()
#
# Tasks:
# 1. Open a spreadsheet
# 2. Download as ODS (OpenDocument Spreadsheet)
# 3. Download as TSV (Tab Separated Values)
# 4. Compare the different file formats
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 23: UPLOAD SPREADSHEET
#
# Learn: ezsheets.upload()
#
# Tasks:
# 1. Create a local Excel or CSV file with data
# 2. Upload it to Google Sheets using ezsheets
# 3. Verify the spreadsheet was created
# 4. Read the data to confirm it uploaded correctly
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 7: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 24: BUILD A CONTACT LIST
#
# Scenario: Create and manage a contact database
#
# Tasks:
# 1. Create a new spreadsheet "Contacts"
# 2. Set up headers: Name, Email, Phone, City
# 3. Add 5 sample contacts
# 4. Write a function to add a new contact
# 5. Write a function to find contact by name
# 6. Write a function to update a contact's info
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 25: EXPENSE TRACKER
#
# Scenario: Track monthly expenses
#
# Tasks:
# 1. Create spreadsheet with sheets for each month
# 2. Headers: Date, Category, Description, Amount
# 3. Write function to add an expense
# 4. Write function to calculate total by category
# 5. Write function to get monthly total
# 6. Create a summary sheet with totals from all months
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 26: INVENTORY MANAGEMENT
#
# Scenario: Track product inventory
#
# Tasks:
# 1. Create spreadsheet with product inventory
# 2. Headers: ProductID, Name, Quantity, Price, ReorderLevel
# 3. Write function to update quantity (add/remove stock)
# 4. Write function to find low stock items
# 5. Write function to calculate total inventory value
# 6. Generate a low-stock alert report
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 27: GRADE BOOK
#
# Scenario: Manage student grades
#
# Tasks:
# 1. Create spreadsheet with student grades
# 2. Headers: StudentName, Assignment1, Assignment2, Midterm, Final
# 3. Write function to add a new student
# 4. Write function to record a grade
# 5. Write function to calculate student average
# 6. Write function to calculate class average per assignment
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 28: DATA SYNC
#
# Scenario: Sync data between local file and Google Sheets
#
# Tasks:
# 1. Create a local CSV file with data
# 2. Upload to Google Sheets
# 3. Make changes in Google Sheets
# 4. Download and compare with original
# 5. Write function to sync changes both ways
# 6. Handle conflicts (data changed in both places)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 29: REPORT GENERATOR
#
# Scenario: Generate formatted reports from data
#
# Tasks:
# 1. Create a spreadsheet with raw sales data
# 2. Create a separate "Report" sheet
# 3. Write function to calculate summary statistics
# 4. Write function to populate report sheet
# 5. Download report as Excel for distribution
# 6. Schedule automatic report generation
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 30: MULTI-SHEET DATA PROCESSING
#
# Scenario: Process data across multiple sheets
#
# Tasks:
# 1. Create spreadsheet with regional data (one sheet per region)
# 2. Each sheet has same structure: Product, Sales, Returns
# 3. Write function to aggregate data from all sheets
# 4. Create a "Combined" sheet with all regional data
# 5. Create a "Summary" sheet with totals per region
# 6. Compare performance across regions
# ----------------------------------------------------------------------


# ======================================================================
# 📊 QUICK REFERENCE - Spreadsheet Object
# ======================================================================
#
# Creating/Opening:
#   ss = ezsheets.createSpreadsheet("Title")
#   ss = ezsheets.Spreadsheet("spreadsheet_id")
#   ss = ezsheets.Spreadsheet("full_url")
#
# Properties:
#   ss.title              # Get/set title
#   ss.spreadsheetId      # Get ID
#   ss.url                # Get URL
#   ss.sheetTitles        # List of sheet names
#   len(ss)               # Number of sheets
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - Sheet Object
# ======================================================================
#
# Accessing:
#   sheet = ss[0]              # By index
#   sheet = ss["SheetName"]    # By name
#
# Properties:
#   sheet.title                # Get/set title
#   sheet.rowCount             # Get/set row count
#   sheet.columnCount          # Get/set column count
#
# Reading:
#   sheet["A1"]                # Single cell
#   sheet.getRow(1)            # Entire row (1-indexed)
#   sheet.getColumn(1)         # Entire column (1-indexed)
#   sheet.getRows()            # All rows as list of lists
#
# Writing:
#   sheet["A1"] = "value"      # Single cell
#   sheet.updateRow(1, [...])  # Entire row
#   sheet.updateColumn(1, [...])  # Entire column
#   sheet.updateRows([...])    # Multiple rows
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - Sheet Operations
# ======================================================================
#
# Create/Delete Sheets:
#   ss.createSheet("Name")        # Create new sheet
#   ss.createSheet("Name", 0)     # Create at index
#   ss["SheetName"].delete()      # Delete sheet
#
# Download:
#   ss.downloadAsExcel("file.xlsx")
#   ss.downloadAsCSV("file.csv")
#   ss.downloadAsODS("file.ods")
#   ss.downloadAsTSV("file.tsv")
#
# Upload:
#   ezsheets.upload("file.xlsx")
#   ezsheets.upload("file.csv")
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - Utilities
# ======================================================================
#
# List all spreadsheets:
#   ezsheets.listSpreadsheets()  # Returns dict {id: title}
#
# Column conversions:
#   ezsheets.getColumnLetterOf(1)     # Returns 'A'
#   ezsheets.getColumnNumberOf('A')   # Returns 1
#
# ======================================================================


# ======================================================================
# 🚀 SETUP INSTRUCTIONS
# ======================================================================
#
# 1. pip install ezsheets
#
# 2. Enable Google Sheets API:
#    - Go to Google Cloud Console
#    - Create project or select existing
#    - Enable Google Sheets API
#    - Enable Google Drive API
#
# 3. Create credentials:
#    - Create OAuth 2.0 credentials
#    - Download credentials.json
#    - Place in your working directory
#
# 4. First run:
#    - Run any ezsheets code
#    - Browser opens for authentication
#    - Authorize access
#    - token.json created automatically
#
# ======================================================================
