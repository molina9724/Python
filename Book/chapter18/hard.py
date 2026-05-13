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

import csv
import json

CSV_WITH_HEADERS = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/13.csv"
with open(CSV_WITH_HEADERS, "r") as csv_file:
    # reader = csv.reader(csv_file)
    # data = list(reader)
    # print(data)

    # my_list = list()
    # for index, row in enumerate(data):
    #     print(index, row)
    #     my_dict = dict()
    #     my_dict[index] = row
    #     my_list.append(my_dict)
    # print(my_list)

    with open(CSV_WITH_HEADERS, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]

my_dict = {"Items": data}

JSON_HARD = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/hard.json"
with open(JSON_HARD, "w", encoding="UTF-8") as json_file:
    json_file.write(json.dumps(my_dict, default=str, indent=2, sort_keys=True))

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
