import ezsheets

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

ss = ezsheets.Spreadsheet(
    "https://docs.google.com/spreadsheets/d/1BC7dD0cajZLOs7XTD0Q2nRV7zKhZGDUxV_Il8AQbvcQ/edit?gid=0#gid=0"
)

sheet: ezsheets.Sheet = ss["Sheet1"]
header = ["Name", "Email", "Phone", "City"]
sheet.updateRow(1, header)

data = [
    ["name1", "email1@test.com", "1", "city1"],
    ["name2", "email2@test.com", "2", "city2"],
    ["name3", "email3@test.com", "3", "city3"],
    ["name4", "email4@test.com", "4", "city4"],
    ["name5", "email5@test.com", "5", "city5"],
]

sheet.updateRows(rows=data, startRow=2)

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
