# =====================================================================
#                    SECTION 3: WORD DOCUMENTS - BASICS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 13: CREATE A NEW WORD DOCUMENT
#
# Learn: Document(), save()
#
# Tasks:
# 1. Create a new Document object
# 2. Save it with a filename
# 3. Verify the file was created
# 4. Open it manually to confirm it works
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 14: ADD PARAGRAPHS
#
# Learn: add_paragraph()
#
# Tasks:
# 1. Create a new document
# 2. Add a paragraph with some text
# 3. Add two more paragraphs
# 4. Save the document
# 5. Open and verify content
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 15: ADD HEADINGS
#
# Learn: add_heading()
#
# Tasks:
# 1. Create a new document
# 2. Add a main heading (level 0 or 1)
# 3. Add a subheading (level 2)
# 4. Add a paragraph under each heading
# 5. Save and verify the structure
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 16: READ AN EXISTING DOCUMENT
#
# Learn: Document(filename), paragraphs
#
# Tasks:
# 1. Open an existing Word document
# 2. Access the paragraphs attribute
# 3. Print the number of paragraphs
# 4. Loop through and print each paragraph's text
# 5. Find a specific paragraph by content
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 17: ACCESS PARAGRAPH PROPERTIES
#
# Learn: paragraph.text, paragraph.style
#
# Tasks:
# 1. Open a Word document
# 2. Get the first paragraph
# 3. Print its text content
# 4. Print its style name
# 5. Check if it's a heading style
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 4: WORD FORMATTING
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 18: WORK WITH RUNS
#
# Learn: paragraph.runs, run.text
#
# Tasks:
# 1. Open or create a Word document
# 2. Access a paragraph
# 3. Get all runs in that paragraph
# 4. Print each run's text separately
# 5. Count the number of runs
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 19: FORMAT TEXT WITH RUNS
#
# Learn: run.bold, run.italic, run.underline
#
# Tasks:
# 1. Create a new document
# 2. Add a paragraph
# 3. Add a run with bold text
# 4. Add a run with italic text
# 5. Add a run with underlined text
# 6. Save and verify formatting
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 20: ADD FORMATTED PARAGRAPH
#
# Learn: add_run() method
#
# Tasks:
# 1. Create a document
# 2. Add a paragraph with mixed formatting:
#    - Normal text, then bold, then italic
# 3. Use add_run() to add each formatted section
# 4. Save and check the result
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 21: CHANGE FONT PROPERTIES
#
# Learn: run.font.size, run.font.name, run.font.color
#
# Tasks:
# 1. Create a document with a paragraph
# 2. Add a run
# 3. Change the font name (e.g., "Arial")
# 4. Change the font size (use Pt() from docx.shared)
# 5. Change the font color (use RGBColor from docx.shared)
# 6. Save and verify
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 22: APPLY PARAGRAPH STYLES
#
# Learn: Built-in styles
#
# Tasks:
# 1. Create a document
# 2. Add a paragraph with style='Title'
# 3. Add a paragraph with style='Heading 1'
# 4. Add a paragraph with style='Normal'
# 5. Add a paragraph with style='Quote'
# 6. Explore other available styles
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 5: WORD DOCUMENT STRUCTURE
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 23: ADD A TABLE
#
# Learn: add_table(), rows, columns, cell()
#
# Tasks:
# 1. Create a document
# 2. Add a table with 3 rows and 4 columns
# 3. Access cells and add text to them
# 4. Add header row content
# 5. Add data to remaining rows
# 6. Save and verify table structure
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 24: MODIFY TABLE CONTENT
#
# Learn: table.rows, table.columns, cell.text
#
# Tasks:
# 1. Open a document with a table
# 2. Access the first table
# 3. Loop through all rows and print content
# 4. Modify a specific cell's content
# 5. Add a new row to the table
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 25: ADD IMAGES
#
# Learn: add_picture()
#
# Tasks:
# 1. Create a document
# 2. Add a heading
# 3. Add a paragraph
# 4. Add an image from a file
# 5. Set image width (use Inches() from docx.shared)
# 6. Save and verify image appears
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 26: ADD PAGE BREAKS
#
# Learn: add_page_break()
#
# Tasks:
# 1. Create a document
# 2. Add some content to page 1
# 3. Add a page break
# 4. Add content that should appear on page 2
# 5. Add another page break and more content
# 6. Save and verify page breaks work
# ----------------------------------------------------------------------
