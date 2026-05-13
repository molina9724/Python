import xml.etree.ElementTree as ET

import xmltodict

xml_string = """<person><name>Alice Doe</name><age>30</age>
<programmer>true</programmer><car xsi:nil="true" xmlns:xsi=
"http://www.w3.org/2001/XMLSchema-instance"/><address><street>
100 Larkin St.</street><city>San Francisco</city><zip>94102</zip>
</address><phone><phoneEntry><type>mobile</type><number>415-555-
7890</number></phoneEntry><phoneEntry><type>work</type><number>
415-555-1234</number></phoneEntry></phone></person>"""

root = ET.fromstring(xml_string)
print(root)
print(list(root))

tree = ET.parse(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/xml_test.xml"
)
root = tree.getroot()
print(root)
print(list(root))

print(root[0].tag)
print(root[0].text)
print(root[3].text)
print(root[3].tag)
print(root[3][0].text)
print(root[3][1].text)
print(root[3][2].text)

for element in root.iter():
    print(f"{element.tag} - {element.text}")


python_data = xmltodict.parse(xml_string)
print(python_data)
print(type(python_data))


person = ET.Element("person")

name = ET.SubElement(person, "name")
name.text = "Alice Doe"

age = ET.SubElement(person, "age")
age.text = "30"

programer = ET.SubElement(person, "programmer")
programer.text = "true"

car = ET.SubElement(person, "car")
car.set("xsi:nil", "http://www.w3.org/2001/XMLSchema-instance")

address = ET.SubElement(person, "address")

street = ET.SubElement(person, "street")
street.text = "100 Larkin St."

result = ET.tostring(person, encoding="utf-8").decode("utf-8")
print(result)

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

xml_string = """<car>
  <make>Toyota</make>
  <model>Camry</model>
  <year>2020</year>
  <color>Blue</color>
  <features>
    <feature>Bluetooth</feature>
    <feature>Backup Camera</feature>
    <feature>Navigation System</feature>
  </features>
</car>"""

root = ET.fromstring(xml_string)
print(root.tag)

make_el = root.find("make")
if make_el is not None:
    print(make_el.text)
else:
    print("Not found")

for el in root:
    print(f"{el.tag} - {el.text}")

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

FILE_PATH = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/xml_test.xml"

tree = ET.parse(FILE_PATH)
root = tree.getroot()
print(root.tag)

print(f"Total children: {len(root)}")

plus_sub_children = 0
for el in root.iter():
    plus_sub_children += 1

print(f" With subchildren: {plus_sub_children}")

addresses = root.find("address").find("previous_addresses").findall("address")

if addresses is not None:
    for address in addresses:
        print(address.find("street").text)

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


xml_string = """<book id="1" category="fiction">
  <title>The Great Gatsby</title>
  <author>F. Scott Fitzgerald</author>
</book>"""

root = ET.fromstring(xml_string)
print(root.attrib["id"])
print(root.attrib["category"])

print(root.get("id"))
print(root.get("category"))

print(root.get("MSO", default="null"))


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

tree = ET.parse(FILE_PATH)
root = tree.getroot()

print("------------------------")

grades = root.find("grades")
for el in grades:
    print(el.text)

previous_addresses = root.find("address").find("previous_addresses")
# Once you have the object you need to look inside of it
all_addresses = previous_addresses.findall("address")

print(all_addresses)

for address in all_addresses:
    print(address.find("zip").text)

for element in root.iter():
    print(element.tag, element.text)

print(root.find("name").text)

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

house = ET.Element("house")

color = ET.SubElement(house, "color")
color.text = "white"

floor = ET.SubElement(house, "floor")
floor.text = "second"

house.set("id", "1")
house.set("owner", "CJ")

print(house.attrib)
print(house.attrib["id"])
print(house.attrib["owner"])

print(ET.tostring(house))

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

my_string = ET.tostring(house)

root = ET.fromstring(my_string)

tree = ET.ElementTree(root)
tree.write(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/my_xml.xml",
    encoding="UTF-8",
    xml_declaration=True,
)

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

tree = ET.parse(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/my_xml.xml"
)
root = tree.getroot()

tree.find("color").text = "black"
tree.find("floor").text = "first"

tree.write(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/my_modified_xml.xml"
)

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

FILE_PATH = (
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/my_modified_xml.xml"
)

tree = ET.parse(FILE_PATH)
root = tree.getroot()

child = ET.Element("NewNode")
root.append(child)

ceiling = ET.Element("ceiling")
print(type(ceiling))
ceiling.text = "blue"
root.insert(0, ceiling)

floor = root.find("floor")
print(type(floor))
if floor is not None:
    root.remove(floor)
root.remove(ceiling)

tree.write(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/my_modified2_xml.xml"
)
