# ======================================================================
# 📁 CSV, JSON, AND XML EXERCISES - Data File Automation
# ======================================================================
# Practice exercises - Write everything from scratch!
# Prerequisites: Python standard library (csv, json, xml modules)
# ======================================================================

import csv
import json
import xml.etree.ElementTree as ET

# =====================================================================
#                    SECTION 1: CSV BASICS - READING
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 1: READ A CSV FILE WITH READER
#
# Learn: csv.reader(), open()
#
# Tasks:
# 1. Create a sample CSV file manually (or use code) with 3 columns
# 2. Open the CSV file in read mode
# 3. Create a csv.reader object
# 4. Loop through and print each row
# 5. Notice that each row is a list of strings
# ----------------------------------------------------------------------

FILE_PATH = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/exercises.csv"

file = open(FILE_PATH, "w")
writer = csv.writer(file)

data = [
    ["Hacker", 25, "A+"],
    ["Player", 12, "A-"],
    ["Music", 40, "O+"],
]

writer.writerows(data)
file.close()

file = open(FILE_PATH, "r")
reader = csv.reader(file)

for row in reader:
    print(row)

# ----------------------------------------------------------------------
# 🟢 2: ACCESS SPECIFIC COLUMNS
#
# Learn: Indexing rows from csv.reader
#
# Tasks:
# 1. Open a CSV file with columns: Name, Age, City
# 2. Read with csv.reader
# 3. Skip the header row
# 4. Print only the Name column (index 0)
# 5. Print Name and City together for each row
# ----------------------------------------------------------------------

NAME_AGE_CITY = (
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/name_age_city.csv"
)
file = open(NAME_AGE_CITY, "w")
writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
writer.writeheader()
writer.writerow({"Name": "Alejo", "Age": 20, "City": "LA"})
writer.writerow({"Name": "Lu", "Age": 40, "City": "Miami"})
writer.writerow({"Name": "Alejo2", "Age": 44, "City": "EVG"})
file.close()

file = open(NAME_AGE_CITY)
reader = csv.DictReader(file)

for row in reader:
    print(row["Name"])
    print(row["Name"], row["City"])

# ----------------------------------------------------------------------
# 🟢 3: READ CSV INTO A LIST
#
# Learn: list() with reader object
#
# Tasks:
# 1. Open a CSV file
# 2. Create a reader object
# 3. Convert the reader to a list of lists
# 4. Print the total number of rows
# 5. Access a specific row by index (e.g., row 3)
# 6. Access a specific cell (e.g., row 2, column 1)
# ----------------------------------------------------------------------

file = open(NAME_AGE_CITY)
reader = csv.reader(file)

data = list(reader)
print(f"Total amount of rows:{len(data)}")
print(data[2])
print(data[1][0])

# ----------------------------------------------------------------------
# 🟡 4: USE DICTREADER
#
# Learn: csv.DictReader()
#
# Tasks:
# 1. Open a CSV file with headers
# 2. Create a DictReader object
# 3. Loop through and print each row (notice it's a dictionary)
# 4. Access values by column name instead of index
# 5. Print the fieldnames attribute
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 5: READ CSV WITH DIFFERENT DELIMITERS
#
# Learn: delimiter parameter
#
# Tasks:
# 1. Create a file with semicolon-separated values
# 2. Try reading it with default csv.reader (observe the problem)
# 3. Read it correctly using delimiter=';'
# 4. Try with tab-delimited data using delimiter='\t'
# 5. Print results to verify correct parsing
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 6: HANDLE CSV WITH QUOTES
#
# Learn: quotechar, quoting parameters
#
# Tasks:
# 1. Create a CSV where some fields contain commas
#    (e.g., "Smith, John", 25, "New York, NY")
# 2. Read the file and verify fields are parsed correctly
# 3. Understand how quotes protect commas within fields
# 4. Try different quotechar settings
# 5. Print each field separately to verify
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 2: CSV BASICS - WRITING
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 7: WRITE A CSV FILE WITH WRITER
#
# Learn: csv.writer(), writerow()
#
# Tasks:
# 1. Create data as a list of lists
# 2. Open a new file in write mode
# 3. Create a csv.writer object
# 4. Write a header row
# 5. Write data rows using writerow()
# 6. Close and verify the file contents
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 8: WRITE MULTIPLE ROWS AT ONCE
#
# Learn: writerows()
#
# Tasks:
# 1. Create a list containing multiple rows of data
# 2. Open a CSV file for writing
# 3. Create a writer object
# 4. Write all rows at once using writerows()
# 5. Open and verify the file was written correctly
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 9: USE DICTWRITER
#
# Learn: csv.DictWriter(), writeheader()
#
# Tasks:
# 1. Create a list of dictionaries (each dict is a row)
# 2. Define the fieldnames list
# 3. Create a DictWriter with fieldnames
# 4. Write the header using writeheader()
# 5. Write all data rows
# 6. Verify output file
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 10: CONTROL CSV FORMATTING
#
# Learn: lineterminator, quoting options
#
# Tasks:
# 1. Create data that includes special characters
# 2. Write CSV with csv.QUOTE_ALL (quote everything)
# 3. Write CSV with csv.QUOTE_MINIMAL (default)
# 4. Write CSV with csv.QUOTE_NONNUMERIC
# 5. Compare the output files
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 11: APPEND TO EXISTING CSV
#
# Learn: Opening in append mode ('a')
#
# Tasks:
# 1. Create a CSV file with some initial data
# 2. Close the file
# 3. Reopen in append mode
# 4. Add new rows without overwriting existing data
# 5. Read and print all data to verify
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 3: CSV DATA PROCESSING
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 12: FILTER CSV DATA
#
# Learn: Conditional processing of rows
#
# Tasks:
# 1. Create a CSV with: Product, Price, Quantity
# 2. Read all rows
# 3. Filter rows where Price > 50
# 4. Write filtered data to a new CSV
# 5. Print count of filtered vs original rows
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 13: TRANSFORM CSV DATA
#
# Learn: Modifying data while reading/writing
#
# Tasks:
# 1. Open a CSV with numeric data stored as strings
# 2. Convert specific columns to integers or floats
# 3. Perform calculations (e.g., add a Total column)
# 4. Write the transformed data to a new CSV
# 5. Verify the calculations are correct
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 14: SORT CSV DATA
#
# Learn: sorted() with key parameter
#
# Tasks:
# 1. Read a CSV into a list of lists (or list of dicts)
# 2. Sort by a specific column
# 3. Sort numerically vs alphabetically (understand the difference)
# 4. Sort in descending order
# 5. Write sorted data to a new file
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 15: MERGE CSV FILES
#
# Learn: Combining data from multiple files
#
# Tasks:
# 1. Create two CSV files with the same structure
# 2. Read both files
# 3. Combine all data (skip duplicate headers)
# 4. Write combined data to a new file
# 5. Verify row counts: file1 + file2 = merged (minus 1 header)
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 4: JSON BASICS - READING
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 16: PARSE JSON STRING
#
# Learn: json.loads()
#
# Tasks:
# 1. Create a JSON-formatted string
# 2. Use json.loads() to parse it into a Python object
# 3. Print the resulting Python object
# 4. Check the type of the result (dict or list)
# 5. Access values from the parsed data
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 17: READ JSON FROM FILE
#
# Learn: json.load()
#
# Tasks:
# 1. Create a JSON file manually (or with code)
# 2. Open the file in read mode
# 3. Use json.load() to parse the file contents
# 4. Print the Python object
# 5. Access nested values in the data
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 18: WORK WITH NESTED JSON
#
# Learn: Accessing nested dictionaries and lists
#
# Tasks:
# 1. Create a JSON file with nested structure:
#    {"person": {"name": "John", "address": {"city": "NYC"}}}
# 2. Load the JSON file
# 3. Access the person's name
# 4. Access the nested city value
# 5. Handle missing keys gracefully (use .get())
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 19: JSON WITH LISTS
#
# Learn: JSON arrays become Python lists
#
# Tasks:
# 1. Create JSON with an array of objects:
#    [{"name": "Alice"}, {"name": "Bob"}]
# 2. Load the JSON
# 3. Loop through the list of objects
# 4. Access properties of each object
# 5. Find a specific item in the list
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 20: HANDLE JSON ERRORS
#
# Learn: json.JSONDecodeError
#
# Tasks:
# 1. Create an invalid JSON string (missing quotes, etc.)
# 2. Try to parse it with json.loads()
# 3. Catch the JSONDecodeError exception
# 4. Print a helpful error message
# 5. Test with several types of invalid JSON
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 5: JSON BASICS - WRITING
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 21: CONVERT PYTHON TO JSON STRING
#
# Learn: json.dumps()
#
# Tasks:
# 1. Create a Python dictionary
# 2. Convert it to a JSON string using json.dumps()
# 3. Print the JSON string
# 4. Notice the difference between Python dict and JSON string
# 5. Try with a list of dictionaries
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 22: WRITE JSON TO FILE
#
# Learn: json.dump()
#
# Tasks:
# 1. Create a Python dictionary or list
# 2. Open a file in write mode
# 3. Use json.dump() to write the data
# 4. Close the file
# 5. Open the file in a text editor to verify
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 23: FORMAT JSON OUTPUT
#
# Learn: indent parameter
#
# Tasks:
# 1. Create a nested Python dictionary
# 2. Convert to JSON without formatting (default)
# 3. Convert to JSON with indent=2
# 4. Convert with indent=4
# 5. Compare readability of each output
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 24: CONTROL JSON OUTPUT
#
# Learn: sort_keys, separators parameters
#
# Tasks:
# 1. Create a dictionary with multiple keys
# 2. Output JSON with sort_keys=True
# 3. Output with custom separators
# 4. Create compact JSON (minimal whitespace)
# 5. Compare file sizes of formatted vs compact
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 25: HANDLE NON-SERIALIZABLE DATA
#
# Learn: default parameter, custom encoder
#
# Tasks:
# 1. Create a dictionary containing a datetime object
# 2. Try to convert to JSON (observe the error)
# 3. Create a custom function to handle datetime
# 4. Use the default parameter to fix serialization
# 5. Verify the JSON output contains the date as string
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 6: XML BASICS - READING
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 26: PARSE XML STRING
#
# Learn: ET.fromstring()
#
# Tasks:
# 1. Create an XML string with a root element and children
# 2. Parse it using ET.fromstring()
# 3. Print the root element's tag
# 4. Access child elements
# 5. Print child element tags and text
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 27: PARSE XML FILE
#
# Learn: ET.parse(), getroot()
#
# Tasks:
# 1. Create an XML file with sample data
# 2. Parse the file using ET.parse()
# 3. Get the root element with getroot()
# 4. Print the root tag name
# 5. Count the number of child elements
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 28: ACCESS ELEMENT ATTRIBUTES
#
# Learn: element.attrib, element.get()
#
# Tasks:
# 1. Create XML with elements that have attributes:
#    <book id="1" category="fiction">...</book>
# 2. Parse the XML
# 3. Access attributes using .attrib dictionary
# 4. Access a specific attribute with .get()
# 5. Handle missing attributes gracefully
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 29: FIND ELEMENTS
#
# Learn: find(), findall(), iter()
#
# Tasks:
# 1. Create XML with multiple levels of nesting
# 2. Use find() to get the first matching element
# 3. Use findall() to get all matching elements
# 4. Use iter() to iterate through all descendants
# 5. Find elements with specific tags at any depth
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 30: ACCESS ELEMENT TEXT
#
# Learn: element.text, element.tail
#
# Tasks:
# 1. Create XML with text content in elements
# 2. Parse and access element text
# 3. Handle elements with no text (None)
# 4. Understand the difference between text and tail
# 5. Extract all text content from the document
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 7: XML BASICS - WRITING
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 31: CREATE XML ELEMENTS
#
# Learn: ET.Element(), ET.SubElement()
#
# Tasks:
# 1. Create a root element
# 2. Add child elements using SubElement
# 3. Set text content for elements
# 4. Set attributes on elements
# 5. Print the XML structure
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 32: WRITE XML TO FILE
#
# Learn: ET.ElementTree(), write()
#
# Tasks:
# 1. Create an XML structure with Element and SubElement
# 2. Create an ElementTree from the root
# 3. Write to a file
# 4. Open and verify the XML file
# 5. Add XML declaration with encoding
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 33: MODIFY EXISTING XML
#
# Learn: Modifying elements in place
#
# Tasks:
# 1. Parse an existing XML file
# 2. Find a specific element
# 3. Change its text content
# 4. Change an attribute value
# 5. Save the modified XML to a new file
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 34: ADD AND REMOVE ELEMENTS
#
# Learn: append(), remove(), insert()
#
# Tasks:
# 1. Parse an existing XML file
# 2. Create a new element
# 3. Append it to a parent element
# 4. Insert an element at a specific position
# 5. Remove an element
# 6. Save the modified XML
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 8: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 35: CSV TO JSON CONVERTER
#
# Scenario: Convert CSV data to JSON format
#
# Tasks:
# 1. Read a CSV file with headers
# 2. Convert each row to a dictionary
# 3. Create a list of all row dictionaries
# 4. Write the list to a JSON file with nice formatting
# 5. Handle different data types (convert numbers)
# 6. Add error handling for file operations
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 36: JSON TO CSV CONVERTER
#
# Scenario: Convert JSON data to CSV format
#
# Tasks:
# 1. Read a JSON file containing a list of objects
# 2. Extract all unique keys for CSV headers
# 3. Handle nested JSON (flatten or skip)
# 4. Write data to CSV file
# 5. Handle missing keys in some objects
# 6. Add option to specify column order
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 37: XML TO CSV CONVERTER
#
# Scenario: Extract data from XML into CSV format
#
# Tasks:
# 1. Parse an XML file with repeating elements
# 2. Identify the record elements and their fields
# 3. Extract data from elements and attributes
# 4. Write to CSV with appropriate headers
# 5. Handle missing elements gracefully
# 6. Support nested element data
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 38: CONFIG FILE MANAGER
#
# Scenario: Manage application settings in JSON
#
# Tasks:
# 1. Create a default config dictionary
# 2. Write function to save config to JSON file
# 3. Write function to load config from JSON file
# 4. Write function to update a specific setting
# 5. Handle missing config file (create with defaults)
# 6. Validate config values when loading
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 39: CSV DATA ANALYZER
#
# Scenario: Analyze sales data from CSV
#
# Tasks:
# 1. Read a CSV with: Date, Product, Quantity, Price
# 2. Calculate total revenue (Quantity × Price)
# 3. Find the best-selling product
# 4. Group sales by date and show daily totals
# 5. Generate a summary report as JSON
# 6. Export filtered results to new CSV
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 40: ADDRESS BOOK (JSON)
#
# Scenario: Create a contact management system
#
# Tasks:
# 1. Design JSON structure for contacts
# 2. Write function to add a new contact
# 3. Write function to search contacts by name
# 4. Write function to update contact info
# 5. Write function to delete a contact
# 6. Save/load contacts from JSON file
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 41: LOG FILE PARSER
#
# Scenario: Parse and analyze log data
#
# Tasks:
# 1. Create a sample log file (CSV or custom format)
# 2. Read and parse each log entry
# 3. Convert to JSON structure with timestamp, level, message
# 4. Filter logs by level (ERROR, WARNING, INFO)
# 5. Count occurrences of each log level
# 6. Export filtered logs to JSON and CSV
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 42: RSS FEED PARSER (XML)
#
# Scenario: Parse an RSS feed and extract articles
#
# Tasks:
# 1. Obtain sample RSS XML (or create mock data)
# 2. Parse the XML structure
# 3. Extract title, link, description for each item
# 4. Store extracted data as list of dictionaries
# 5. Save to JSON file
# 6. Export to CSV with selected fields
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 43: DATA MIGRATION TOOL
#
# Scenario: Migrate data between formats
#
# Tasks:
# 1. Create a function that detects file format by extension
# 2. Create readers for CSV, JSON, and XML
# 3. Create writers for CSV, JSON, and XML
# 4. Build a convert function: convert(input_file, output_file)
# 5. Handle format-specific features (attributes in XML)
# 6. Add validation and error reporting
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 44: INVENTORY SYSTEM
#
# Scenario: Manage product inventory with file storage
#
# Tasks:
# 1. Design data structure for products
# 2. Store inventory in JSON file
# 3. Import new products from CSV
# 4. Export low-stock report to CSV
# 5. Generate XML report for external system
# 6. Implement backup (save timestamped copies)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 45: API RESPONSE PROCESSOR
#
# Scenario: Process JSON responses from a web API
#
# Tasks:
# 1. Create sample JSON responses (mock API data)
# 2. Parse the JSON response
# 3. Extract relevant fields from nested structure
# 4. Handle pagination (multiple response files)
# 5. Combine all data into single CSV
# 6. Generate summary statistics in JSON
# ----------------------------------------------------------------------


# ======================================================================
# 📁 QUICK REFERENCE - CSV Module
# ======================================================================
#
# Reading CSV:
#   import csv
#
#   with open('file.csv', 'r') as f:
#       reader = csv.reader(f)
#       for row in reader:
#           print(row)           # row is a list
#
#   with open('file.csv', 'r') as f:
#       reader = csv.DictReader(f)
#       for row in reader:
#           print(row)           # row is a dictionary
#           print(row['Name'])   # access by column name
#
# Writing CSV:
#   with open('file.csv', 'w', newline='') as f:
#       writer = csv.writer(f)
#       writer.writerow(['Name', 'Age'])    # single row
#       writer.writerows(list_of_lists)     # multiple rows
#
#   with open('file.csv', 'w', newline='') as f:
#       fieldnames = ['Name', 'Age']
#       writer = csv.DictWriter(f, fieldnames=fieldnames)
#       writer.writeheader()
#       writer.writerow({'Name': 'Alice', 'Age': 30})
#
# ======================================================================


# ======================================================================
# 📁 QUICK REFERENCE - CSV Parameters
# ======================================================================
#
# Common parameters:
#   delimiter=','           # Field separator (default comma)
#   quotechar='"'           # Quote character (default double-quote)
#   quoting=csv.QUOTE_MINIMAL    # When to quote fields
#
# Quoting options:
#   csv.QUOTE_MINIMAL       # Quote only when needed
#   csv.QUOTE_ALL           # Quote all fields
#   csv.QUOTE_NONNUMERIC    # Quote all non-numeric fields
#   csv.QUOTE_NONE          # Never quote (use escapechar)
#
# Windows line ending fix:
#   open('file.csv', 'w', newline='')   # Always use newline=''
#
# ======================================================================


# ======================================================================
# 📁 QUICK REFERENCE - JSON Module
# ======================================================================
#
# JSON string operations:
#   import json
#
#   # Parse JSON string to Python object
#   data = json.loads('{"name": "Alice"}')
#
#   # Convert Python object to JSON string
#   json_str = json.dumps({'name': 'Alice'})
#   json_str = json.dumps(data, indent=2)    # Pretty print
#
# JSON file operations:
#   # Read JSON file
#   with open('file.json', 'r') as f:
#       data = json.load(f)
#
#   # Write JSON file
#   with open('file.json', 'w') as f:
#       json.dump(data, f, indent=2)
#
# ======================================================================


# ======================================================================
# 📁 QUICK REFERENCE - JSON Parameters
# ======================================================================
#
# json.dumps() / json.dump() parameters:
#   indent=2                # Pretty print with indentation
#   sort_keys=True          # Sort dictionary keys
#   separators=(',', ': ')  # Custom separators
#   ensure_ascii=False      # Allow non-ASCII characters
#
# Compact JSON:
#   json.dumps(data, separators=(',', ':'))
#
# Error handling:
#   try:
#       data = json.loads(text)
#   except json.JSONDecodeError as e:
#       print(f"Invalid JSON: {e}")
#
# ======================================================================


# ======================================================================
# 📁 QUICK REFERENCE - XML ElementTree
# ======================================================================
#
# Parsing XML:
#   import xml.etree.ElementTree as ET
#
#   # From string
#   root = ET.fromstring(xml_string)
#
#   # From file
#   tree = ET.parse('file.xml')
#   root = tree.getroot()
#
# Element properties:
#   element.tag             # Element tag name
#   element.text            # Text content
#   element.attrib          # Dictionary of attributes
#   element.get('attr')     # Get specific attribute
#
# ======================================================================


# ======================================================================
# 📁 QUICK REFERENCE - XML Navigation
# ======================================================================
#
# Finding elements:
#   element.find('tag')         # First matching child
#   element.findall('tag')      # All matching children
#   element.iter('tag')         # All descendants with tag
#   element.iter()              # All descendants
#
# Iterating children:
#   for child in element:
#       print(child.tag, child.text)
#
# XPath-like searches:
#   root.findall('.//tag')      # Find anywhere in tree
#   root.findall('./parent/child')  # Specific path
#
# ======================================================================


# ======================================================================
# 📁 QUICK REFERENCE - XML Writing
# ======================================================================
#
# Creating elements:
#   root = ET.Element('root')
#   child = ET.SubElement(root, 'child')
#   child.text = 'content'
#   child.set('attribute', 'value')
#
# Modifying elements:
#   element.text = 'new text'
#   element.set('attr', 'new value')
#   parent.remove(child)
#   parent.append(new_element)
#   parent.insert(0, new_element)
#
# Writing to file:
#   tree = ET.ElementTree(root)
#   tree.write('file.xml', encoding='utf-8', xml_declaration=True)
#
# To string:
#   xml_string = ET.tostring(root, encoding='unicode')
#
# ======================================================================


# ======================================================================
# 📁 QUICK REFERENCE - Data Type Conversions
# ======================================================================
#
# JSON to Python:
#   object  → dict
#   array   → list
#   string  → str
#   number  → int/float
#   true    → True
#   false   → False
#   null    → None
#
# Python to JSON:
#   dict    → object
#   list    → array
#   str     → string
#   int     → number
#   float   → number
#   True    → true
#   False   → false
#   None    → null
#
# Not JSON serializable (need custom handling):
#   datetime, set, tuple, custom objects
#
# ======================================================================


# ======================================================================
# 🚀 SETUP INSTRUCTIONS
# ======================================================================
#
# No installation needed! All modules are built into Python:
#   import csv
#   import json
#   import xml.etree.ElementTree as ET
#
# Sample data for practice:
#   Create your own CSV, JSON, and XML files
#   Download public datasets
#   Use data generators online
#
# Sample CSV content (save as data.csv):
#   Name,Age,City
#   Alice,30,New York
#   Bob,25,Los Angeles
#   Charlie,35,Chicago
#
# Sample JSON content (save as data.json):
#   {
#     "people": [
#       {"name": "Alice", "age": 30},
#       {"name": "Bob", "age": 25}
#     ]
#   }
#
# Sample XML content (save as data.xml):
#   <?xml version="1.0"?>
#   <people>
#     <person id="1">
#       <name>Alice</name>
#       <age>30</age>
#     </person>
#   </people>
#
# ======================================================================
