import json

json_string = '{"name": "Alice Doe", "age": 30, "car": null, "programmer": true, "address": {"street": "100 Larkin St.", "city": "San Francisco", "zip": "94102"}, "phone": [{"type": "mobile", "number": "415-555-7890"}, {"type":  "work", "number": "415-555-1234"}]}'
python_data = json.loads(json_string)

print(python_data)

python_data = {
    "name": "Alice Doe",
    "age": 30,
    "car": None,
    "programmer": None,
    "address": {
        "street": "100 Larkin St.",
        "city": "San Francisco",
        "zip": "94102",
    },
    "phone": [
        {
            "type": "mobile",
            "number": "415-555-7890",
        },
        {
            "type": "work",
            "number": "415-555-1234",
        },
    ],
}

json_string = json.dumps(python_data, indent=2)
print(json_string)

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

json_string = '{"Name":"Pepe", "Age":20}'
python_data = json.loads(json_string)
print(python_data)
print(type(python_data))

print(python_data["Name"])
print(python_data["Age"])

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

FILE_PATH = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/my_json.json"
with open(FILE_PATH, "r") as file:
    data = json.load(file)

print(data)
print(data["address"]["street"])
print(data["address"]["zip"])
print(data["address"]["coordinates"])
print(data["address"]["coordinates"]["latitude"])
print(data["address"]["previous_addresses"][0]["street"])

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

data = {
    "person": {
        "name": "John",
        "address": {"city": "NYC"},
    }
}
with open("18test.json", "w") as file:
    file.write(json.dumps(data))

with open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/18test.json", "r"
) as file:
    data = json.load(file)
    print(data["person"]["name"])
    print(data["person"]["address"]["city"])

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
