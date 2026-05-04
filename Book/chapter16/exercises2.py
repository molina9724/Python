# ======================================================================
# 🗄️ SQLITE EXERCISES - Database Programming with Python
# ======================================================================
# Practice exercises - Write everything from scratch!
# Prerequisites: Python 3.x, sqlite3 module (built-in)
# ======================================================================


# =====================================================================
#                    SECTION 1: DATABASE CONNECTION BASICS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 1: CREATE AND CONNECT TO A DATABASE
#
# Learn: sqlite3.connect()
#
# Tasks:
# 1. Import the sqlite3 module
# 2. Create a connection to a new database file called 'practice.db'
# 3. Print the connection object to verify it was created
# 4. Close the connection properly
# 5. Check your folder - the .db file should now exist
# ----------------------------------------------------------------------

import sqlite3

db_path = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter16/practice.db"

conn_practice = sqlite3.connect(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter16/practice.db",
    isolation_level=None,
)
print(conn_practice)
conn_practice.close()

# ----------------------------------------------------------------------
# 🟢 2: USE AN IN-MEMORY DATABASE
#
# Learn: In-memory databases with ':memory:'
#
# Tasks:
# 1. Create a connection to an in-memory database
# 2. Print a message confirming connection
# 3. Note: This database disappears when connection closes
# 4. Close the connection
# 5. Explain when you might use an in-memory database
# ----------------------------------------------------------------------

in_memory_database = sqlite3.connect(":memory:", isolation_level=None)
print(in_memory_database)

in_memory_database.close()

# ----------------------------------------------------------------------
# 🟢 3: USE CONTEXT MANAGER FOR CONNECTIONS
#
# Learn: 'with' statement for database connections
#
# Tasks:
# 1. Use 'with sqlite3.connect()' to open a database
# 2. Print a message while inside the with block
# 3. Note how the connection auto-closes after the block
# 4. Try to use the connection after the with block - what happens?
# 5. Explain why context managers are safer
# ----------------------------------------------------------------------

# with sqlite3.connect(db_path) as with_conn:
#     print("Inside the with")
#     with_conn.execute(
#         "CREATE TABLE IF NOT EXISTS students (id INT PRIMARY KEY, name TEXT, age INT) STRICT"
#     )

# print(
#     with_conn.execute("SELECT name FROM sqlite_schema WHERE type = 'table'").fetchall()
# )

# ----------------------------------------------------------------------
# 🟢 4: CREATE A CURSOR OBJECT
#
# Learn: connection.cursor()
#
# Tasks:
# 1. Connect to a database
# 2. Create a cursor object using .cursor()
# 3. Print the cursor object
# 4. Understand: cursors execute SQL and fetch results
# 5. Close both cursor and connection
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 2: CREATING TABLES
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 5: CREATE YOUR FIRST TABLE
#
# Learn: CREATE TABLE, execute()
#
# Tasks:
# 1. Connect to a database
# 2. Create a cursor
# 3. Write SQL to create a table 'students' with columns:
#    - id (INTEGER PRIMARY KEY)
#    - name (TEXT)
#    - age (INTEGER)
# 4. Execute the SQL using cursor.execute()
# 5. Commit the changes using connection.commit()
# ----------------------------------------------------------------------

# conn_practice = sqlite3.connect(
#     "/Users/daniel_molina/Downloads/Python/Python/Book/chapter16/practice.db",
#     isolation_level=None,
# )

conn_practice = sqlite3.connect(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter16/practice.db",
    isolation_level=None,
)

conn_practice.execute(
    "CREATE TABLE IF NOT EXISTS students (id INT PRIMARY KEY, name TEXT, age INT) STRICT"
)

# ----------------------------------------------------------------------
# 🟢 6: CREATE TABLE IF NOT EXISTS
#
# Learn: IF NOT EXISTS clause
#
# Tasks:
# 1. Modify your CREATE TABLE to include IF NOT EXISTS
# 2. Run the code twice
# 3. Without IF NOT EXISTS, the second run would error
# 4. Verify no error occurs with IF NOT EXISTS
# 5. Explain why this is useful for scripts that run multiple times
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 7: CREATE TABLE WITH MULTIPLE DATA TYPES
#
# Learn: SQLite data types (TEXT, INTEGER, REAL, BLOB, NULL)
#
# Tasks:
# 1. Create a table 'products' with columns:
#    - id (INTEGER PRIMARY KEY)
#    - name (TEXT NOT NULL)
#    - price (REAL)
#    - quantity (INTEGER DEFAULT 0)
#    - description (TEXT)
# 2. Execute and commit
# 3. Note the NOT NULL and DEFAULT constraints
# 4. Try inserting a row without a name - what happens?
# 5. Try inserting a row without quantity - what's the value?
# ----------------------------------------------------------------------

conn_practice = sqlite3.connect(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter16/practice.db",
    isolation_level=None,
)

conn_practice.execute(
    "CREATE TABLE IF NOT EXISTS products (id INT PRIMARY KEY, name TEXT, price REAL, quantity int DEFAULT 0, description TEXT) STRICT"
)

try:
    conn_practice.execute("INSERT INTO products VALUES (1, , 50, 1, 'last gen')")
except Exception as e:
    print("Getting this one because you didn't insert a name", e)

# conn_practice.execute(
#     "INSERT INTO products (id, name, price, description) VALUES (1, 'PS5', 50, 'last gen')"
# )

# ----------------------------------------------------------------------
# 🟡 8: DROP A TABLE
# R
# Learn: DROP TABLE
#
# Tasks:
# 1. Create a temporary table called 'temp_data'
# 2. Verify it was created
# 3. Drop the table using DROP TABLE
# 4. Use IF EXISTS to avoid errors if table doesn't exist
# 5. Verify the table no longer exists
# ----------------------------------------------------------------------

conn_practice.execute("CREATE TABLE IF NOT EXISTS temp_data (id INT)")

all_tables = conn_practice.execute(
    "SELECT name FROM sqlite_schema WHERE type='table'"
).fetchall()
assert "temp_data" in [table[0] for table in all_tables]

conn_practice.execute("DROP TABLE IF EXISTS temp_data")
all_tables = conn_practice.execute(
    "SELECT name FROM sqlite_schema WHERE type='table'"
).fetchall()
assert "temp_data" not in [table[0] for table in all_tables]


# =====================================================================
#                    SECTION 3: INSERTING DATA
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 9: INSERT A SINGLE ROW
#
# Learn: INSERT INTO, VALUES
#
# Tasks:
# 1. Connect to your database with the students table
# 2. Write an INSERT statement to add one student
# 3. Execute the INSERT
# 4. Commit the transaction
# 5. Print a confirmation message
# ----------------------------------------------------------------------

# conn_practice.execute("INSERT INTO students VALUES (1, 'CJ', 26)")

# ----------------------------------------------------------------------
# 🟢 10: INSERT WITH PLACEHOLDERS (SAFE WAY)
#
# Learn: ? placeholders, parameterized queries
#
# Tasks:
# 1. Use ? placeholders instead of string formatting
# 2. Pass values as a tuple to execute()
# 3. Insert a student: ('Alice', 22)
# 4. Commit and verify
# 5. Explain why placeholders prevent SQL injection
# ----------------------------------------------------------------------

id = 2
name = "Alice"
age = 22

# conn_practice.execute("INSERT INTO students VALUES (?, ?, ?)", (id, name, age))

# ----------------------------------------------------------------------
# 🟡 11: INSERT MULTIPLE ROWS
#
# Learn: executemany()
#
# Tasks:
# 1. Create a list of tuples with student data
#    [(name1, age1), (name2, age2), (name3, age3)]
# 2. Use cursor.executemany() with placeholders
# 3. Insert at least 5 students at once
# 4. Commit the transaction
# 5. Print how many rows were inserted using cursor.rowcount
# ----------------------------------------------------------------------

students = [
    (3, "Carl", 50),
    (4, "Tomas", 50),
    (5, "Pacheco", 23),
    (6, "Andrea", 21),
    (7, "Carla", 33),
]

# conn_practice.executemany("INSERT INTO students VALUES (?, ?, ?)", students)
# print(conn_practice.execute("SELECT COUNT(*) FROM students").fetchall())

# ----------------------------------------------------------------------
# 🟡 12: INSERT AND GET THE NEW ROW'S ID
#
# Learn: cursor.lastrowid
#
# Tasks:
# 1. Insert a new student
# 2. After execute(), access cursor.lastrowid
# 3. Print the ID of the newly inserted row
# 4. Insert another student and get their ID
# 5. Explain why this is useful (e.g., for related tables)
# ----------------------------------------------------------------------

# Always use the cursor, not the connection for operations
cursor = conn_practice.cursor()

# cursor.execute("INSERT INTO students VALUES (8, 'Jay', 6)")
print(cursor.lastrowid)

# cursor.execute("INSERT INTO students VALUES (9, 'Tea', 44)")
id = cursor.lastrowid

# print(cursor.execute(f"SELECT * FROM students WHERE id = {id}").fetchall())

# ----------------------------------------------------------------------
# 🟡 13: INSERT OR REPLACE
#
# Learn: INSERT OR REPLACE, INSERT OR IGNORE
#
# Tasks:
# 1. Create a table with a UNIQUE constraint on a column
# 2. Insert a row
# 3. Try inserting a duplicate - observe the error
# 4. Use INSERT OR REPLACE to update on conflict
# 5. Use INSERT OR IGNORE to skip on conflict
# ----------------------------------------------------------------------

# cursor.execute("INSERT INTO students VALUES (20, 'CJ', 35)")
# cursor.execute("INSERT OR REPLACE INTO students VALUES (20, 'CJ', 35)")
cursor.execute("INSERT OR IGNORE INTO students VALUES (20, 'CJ', 35)")

# =====================================================================
#                    SECTION 4: QUERYING DATA
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 14: SELECT ALL ROWS
#
# Learn: SELECT *, fetchall()
#
# Tasks:
# 1. Write a SELECT * FROM students query
# 2. Execute the query
# 3. Use cursor.fetchall() to get all results
# 4. Loop through results and print each row
# 5. Note that each row is a tuple
# ----------------------------------------------------------------------

print(cursor.execute("SELECT * FROM students").fetchall())
all_results = cursor.execute("SELECT * FROM students").fetchall()

for person in all_results:
    print(type(person))
    print(person)

# ----------------------------------------------------------------------
# 🟢 15: SELECT SPECIFIC COLUMNS
#
# Learn: SELECT column1, column2
#
# Tasks:
# 1. Select only name and age columns from students
# 2. Fetch and print the results
# 3. Compare output to SELECT * - what's different?
# 4. Select columns in different order (age, name)
# 5. Print formatted output: "Name: X, Age: Y"
# ----------------------------------------------------------------------

print(cursor.execute("SELECT name,age FROM students").fetchall())
print(cursor.execute("SELECT age,name FROM students").fetchall())
print(cursor.execute("SELECT 'Name: '||name||', Age: '|| age FROM students").fetchall())

# ----------------------------------------------------------------------
# 🟢 16: FETCH ONE ROW AT A TIME
#
# Learn: fetchone()
#
# Tasks:
# 1. Execute a SELECT query
# 2. Use fetchone() to get the first row
# 3. Call fetchone() again to get the next row
# 4. Keep calling until it returns None
# 5. Explain when fetchone() is better than fetchall()
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 17: FETCH A SPECIFIC NUMBER OF ROWS
#
# Learn: fetchmany(size)
#
# Tasks:
# 1. Insert at least 10 rows into a table
# 2. Execute a SELECT query
# 3. Use fetchmany(3) to get 3 rows
# 4. Call fetchmany(3) again to get the next 3
# 5. Explain when this is useful (large datasets)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 18: USE WHERE CLAUSE
#
# Learn: WHERE, comparison operators
#
# Tasks:
# 1. Select students where age > 20
# 2. Select students where name = 'Alice' (use placeholder!)
# 3. Select students where age BETWEEN 18 AND 25
# 4. Select students where name LIKE 'A%'
# 5. Print results for each query
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 19: USE AND, OR, NOT IN WHERE
#
# Learn: Logical operators in WHERE
#
# Tasks:
# 1. Select students where age > 18 AND age < 25
# 2. Select students where name = 'Alice' OR name = 'Bob'
# 3. Select students where NOT age = 20
# 4. Combine AND and OR with parentheses
# 5. Print results for each query
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 20: ORDER RESULTS
#
# Learn: ORDER BY, ASC, DESC
#
# Tasks:
# 1. Select all students ordered by name (ascending)
# 2. Select all students ordered by age (descending)
# 3. Order by multiple columns: age DESC, name ASC
# 4. Print results showing the order
# 5. Try ordering by a column that doesn't exist - what happens?
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 21: LIMIT RESULTS
#
# Learn: LIMIT, OFFSET
#
# Tasks:
# 1. Select only the first 5 students
# 2. Select 5 students starting from row 10 (OFFSET)
# 3. Combine LIMIT with ORDER BY for "top N"
# 4. Get the 3 oldest students
# 5. Implement basic pagination (page 1, page 2, etc.)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 22: USE AGGREGATE FUNCTIONS
#
# Learn: COUNT, SUM, AVG, MIN, MAX
#
# Tasks:
# 1. Count total number of students
# 2. Find the average age of students
# 3. Find the minimum and maximum age
# 4. Sum a numeric column (use products table with price)
# 5. Use COUNT with WHERE to count filtered results
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 23: GROUP BY AND HAVING
#
# Learn: GROUP BY, HAVING
#
# Tasks:
# 1. Add a 'grade' column to students (A, B, C, etc.)
# 2. Count students per grade using GROUP BY
# 3. Get average age per grade
# 4. Use HAVING to show only grades with more than 2 students
# 5. Explain difference between WHERE and HAVING
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 5: UPDATING AND DELETING DATA
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 24: UPDATE SINGLE ROW
#
# Learn: UPDATE, SET, WHERE
#
# Tasks:
# 1. Update a specific student's age (use WHERE with id)
# 2. Always use WHERE to avoid updating all rows!
# 3. Commit the change
# 4. Select the row to verify the update
# 5. Print before and after values
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 25: UPDATE MULTIPLE ROWS
#
# Learn: UPDATE with broader WHERE
#
# Tasks:
# 1. Update all students with age < 18, set age = 18
# 2. Check cursor.rowcount to see how many rows changed
# 3. Update multiple columns at once
# 4. Commit and verify changes
# 5. WARNING: Run UPDATE without WHERE to see what happens (on test data!)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 26: DELETE SINGLE ROW
#
# Learn: DELETE FROM, WHERE
#
# Tasks:
# 1. Delete a specific student by id
# 2. Always use WHERE to avoid deleting all rows!
# 3. Commit the deletion
# 4. Verify the row is gone with SELECT
# 5. Check cursor.rowcount for rows deleted
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 27: DELETE MULTIPLE ROWS
#
# Learn: DELETE with conditions
#
# Tasks:
# 1. Delete all students with age > 30
# 2. Delete all students whose name starts with 'T'
# 3. Print how many rows were deleted
# 4. Commit and verify
# 5. WARNING: Test DELETE without WHERE on test data!
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 28: DELETE ALL ROWS (TRUNCATE EQUIVALENT)
#
# Learn: DELETE FROM table (without WHERE)
#
# Tasks:
# 1. Create a test table with some data
# 2. Delete all rows using DELETE FROM (no WHERE)
# 3. Verify table is empty but still exists
# 4. Compare to DROP TABLE - what's the difference?
# 5. Re-insert data to prove table structure remains
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 6: ADVANCED QUERIES
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 29: USE DISTINCT
#
# Learn: SELECT DISTINCT
#
# Tasks:
# 1. Add duplicate values to a column
# 2. Select all values - see duplicates
# 3. Select DISTINCT values - duplicates removed
# 4. Use DISTINCT with multiple columns
# 5. Count distinct values using COUNT(DISTINCT column)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 30: USE NULL VALUES
#
# Learn: NULL, IS NULL, IS NOT NULL
#
# Tasks:
# 1. Insert rows with NULL values in some columns
# 2. Select rows WHERE column IS NULL
# 3. Select rows WHERE column IS NOT NULL
# 4. Note: NULL = NULL doesn't work! Use IS NULL
# 5. Use COALESCE to replace NULL with default value
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 31: SUBQUERIES
#
# Learn: Nested SELECT statements
#
# Tasks:
# 1. Find students older than the average age
#    (use subquery to calculate average)
# 2. Find students in specific grades using IN (subquery)
# 3. Use subquery in INSERT to copy data
# 4. Use subquery in UPDATE
# 5. Print results explaining the subquery logic
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 32: JOIN TABLES
#
# Learn: INNER JOIN, related tables
#
# Tasks:
# 1. Create two related tables:
#    - students (id, name, class_id)
#    - classes (id, class_name, teacher)
# 2. Insert data into both tables
# 3. Use INNER JOIN to combine data
# 4. Select student name with their class name
# 5. Filter joined results with WHERE
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 33: LEFT JOIN
#
# Learn: LEFT JOIN for optional relationships
#
# Tasks:
# 1. Use the tables from exercise 32
# 2. Add students without a class (class_id = NULL)
# 3. Use LEFT JOIN to get all students, even without class
# 4. Compare results of INNER JOIN vs LEFT JOIN
# 5. Find students who don't have a class assigned
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 7: ROW FACTORY AND DATA ACCESS
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 34: ACCESS COLUMNS BY NAME WITH ROW_FACTORY
#
# Learn: sqlite3.Row, row_factory
#
# Tasks:
# 1. Set connection.row_factory = sqlite3.Row
# 2. Execute a SELECT query
# 3. Access columns by name: row['name'], row['age']
# 4. Also access by index: row[0], row[1]
# 5. Compare to default tuple access
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 35: CREATE CUSTOM ROW FACTORY
#
# Learn: Custom row_factory functions
#
# Tasks:
# 1. Create a function that returns dictionaries
# 2. Set it as the row_factory
# 3. Execute query and verify rows are dictionaries
# 4. Create a row factory that returns namedtuples
# 5. Compare different row factories
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 8: TRANSACTIONS AND ERROR HANDLING
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 36: UNDERSTAND TRANSACTIONS
#
# Learn: commit(), rollback()
#
# Tasks:
# 1. Start a transaction (happens automatically)
# 2. Insert several rows
# 3. Commit to save changes permanently
# 4. Insert more rows but DON'T commit
# 5. Close connection and reopen - uncommitted data is lost!
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 37: USE ROLLBACK
#
# Learn: Undoing changes with rollback()
#
# Tasks:
# 1. Insert some data
# 2. Before committing, use rollback()
# 3. Verify the data was NOT saved
# 4. Insert again and this time commit
# 5. Verify the data WAS saved
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 38: HANDLE DATABASE ERRORS
#
# Learn: try/except with sqlite3 exceptions
#
# Tasks:
# 1. Use try/except around database operations
# 2. Catch sqlite3.Error as the general exception
# 3. Catch sqlite3.IntegrityError for constraint violations
# 4. Catch sqlite3.OperationalError for SQL errors
# 5. Always rollback in except block, commit in try block
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 39: USE CONTEXT MANAGER FOR TRANSACTIONS
#
# Learn: 'with connection' for auto-commit/rollback
#
# Tasks:
# 1. Use 'with connection:' for transaction management
# 2. If block succeeds, changes are committed
# 3. If exception occurs, changes are rolled back
# 4. Test both success and failure cases
# 5. Compare to manual commit/rollback
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 9: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 40: BUILD A CONTACT BOOK APPLICATION
#
# Scenario: Create a contact management system
#
# Tasks:
# 1. Create table: contacts (id, name, phone, email, created_date)
# 2. Write function: add_contact(name, phone, email)
# 3. Write function: search_contacts(search_term)
# 4. Write function: update_contact(id, **kwargs)
# 5. Write function: delete_contact(id)
# 6. Write function: list_all_contacts()
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 41: BUILD A TODO LIST APPLICATION
#
# Scenario: Create a task management system
#
# Tasks:
# 1. Create table: tasks (id, title, description, due_date, completed, priority)
# 2. Write function: add_task(title, description, due_date, priority)
# 3. Write function: complete_task(id)
# 4. Write function: get_pending_tasks()
# 5. Write function: get_overdue_tasks()
# 6. Write function: delete_completed_tasks()
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 42: BUILD AN INVENTORY SYSTEM
#
# Scenario: Track product inventory
#
# Tasks:
# 1. Create tables: products, categories, transactions
# 2. Products: id, name, category_id, quantity, price, reorder_level
# 3. Write function: add_product(name, category, quantity, price)
# 4. Write function: update_stock(product_id, quantity_change)
# 5. Write function: get_low_stock_products()
# 6. Write function: get_inventory_value()
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 43: BUILD A SIMPLE BLOG DATABASE
#
# Scenario: Store blog posts and comments
#
# Tasks:
# 1. Create tables: authors, posts, comments
# 2. Posts: id, author_id, title, content, published_date
# 3. Comments: id, post_id, commenter_name, comment_text, date
# 4. Write function: create_post(author_id, title, content)
# 5. Write function: add_comment(post_id, name, comment)
# 6. Write function: get_post_with_comments(post_id) using JOIN
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 44: BUILD A GRADEBOOK SYSTEM
#
# Scenario: Manage student grades
#
# Tasks:
# 1. Create tables: students, courses, enrollments, grades
# 2. Enrollments links students to courses (many-to-many)
# 3. Write function: enroll_student(student_id, course_id)
# 4. Write function: record_grade(student_id, course_id, grade)
# 5. Write function: get_student_gpa(student_id)
# 6. Write function: get_course_average(course_id)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 45: BUILD A SIMPLE BANKING SYSTEM
#
# Scenario: Track accounts and transactions
#
# Tasks:
# 1. Create tables: accounts, transactions
# 2. Accounts: id, holder_name, balance, account_type
# 3. Transactions: id, account_id, type, amount, date, description
# 4. Write function: deposit(account_id, amount) - update balance, log transaction
# 5. Write function: withdraw(account_id, amount) - check balance first!
# 6. Write function: transfer(from_id, to_id, amount) - use transaction!
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 46: DATA IMPORT/EXPORT
#
# Scenario: Move data between CSV and SQLite
#
# Tasks:
# 1. Write function: import_csv_to_table(csv_file, table_name)
# 2. Handle creating the table from CSV headers
# 3. Write function: export_table_to_csv(table_name, csv_file)
# 4. Handle large files efficiently (batch inserts)
# 5. Add progress reporting for large imports
# 6. Handle data type detection
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 47: DATABASE BACKUP AND RESTORE
#
# Scenario: Create backups of your database
#
# Tasks:
# 1. Write function: backup_database(source_db, backup_file)
# 2. Use connection.backup() method for efficient backup
# 3. Write function: restore_database(backup_file, target_db)
# 4. Add timestamp to backup filenames
# 5. Write function: list_backups(backup_folder)
# 6. Implement rotation (keep only last N backups)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 48: SEARCH AND REPORTING
#
# Scenario: Advanced queries and reports
#
# Tasks:
# 1. Create a sales table with dates, products, quantities, prices
# 2. Write function: daily_sales_report(date)
# 3. Write function: monthly_summary(year, month)
# 4. Write function: top_products(n, start_date, end_date)
# 5. Write function: search_sales(keyword) - search in product names
# 6. Write function: export_report_to_csv(report_data, filename)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 49: MULTI-USER SIMULATION
#
# Scenario: Handle concurrent access patterns
#
# Tasks:
# 1. Set up database with timeout parameter
# 2. Use isolation_level parameter
# 3. Implement optimistic locking with version column
# 4. Write function that handles "database locked" errors
# 5. Implement retry logic for failed operations
# 6. Test with simulated concurrent access
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 50: COMPLETE LIBRARY MANAGEMENT SYSTEM
#
# Scenario: Full CRUD application for a library
#
# Tasks:
# 1. Create tables: books, members, loans
# 2. Books: id, title, author, isbn, copies_available
# 3. Members: id, name, email, membership_date
# 4. Loans: id, book_id, member_id, loan_date, due_date, return_date
# 5. Implement: add_book, add_member, checkout_book, return_book
# 6. Implement: get_overdue_loans, get_member_history, search_books
# ----------------------------------------------------------------------


# ======================================================================
# 🗄️ QUICK REFERENCE - Connection & Cursor
# ======================================================================
#
# Connect to database:
#   conn = sqlite3.connect('database.db')  # File database
#   conn = sqlite3.connect(':memory:')     # In-memory database
#
# Create cursor:
#   cursor = conn.cursor()
#
# Execute SQL:
#   cursor.execute("SQL HERE")
#   cursor.execute("SQL WITH ?", (value,))  # Single placeholder
#   cursor.execute("SQL", (val1, val2))     # Multiple placeholders
#   cursor.executemany("SQL", list_of_tuples)  # Multiple rows
#
# Save changes:
#   conn.commit()
#
# Undo changes:
#   conn.rollback()
#
# Close:
#   cursor.close()
#   conn.close()
#
# ======================================================================


# ======================================================================
# 🗄️ QUICK REFERENCE - Fetching Results
# ======================================================================
#
# After SELECT query:
#   cursor.fetchone()      # Get one row (or None)
#   cursor.fetchall()      # Get all rows as list
#   cursor.fetchmany(n)    # Get n rows
#
# Iterate directly:
#   for row in cursor:
#       print(row)
#
# Row count (for INSERT/UPDATE/DELETE):
#   cursor.rowcount
#
# Last inserted ID:
#   cursor.lastrowid
#
# ======================================================================


# ======================================================================
# 🗄️ QUICK REFERENCE - Common SQL
# ======================================================================
#
# CREATE TABLE:
#   CREATE TABLE IF NOT EXISTS tablename (
#       id INTEGER PRIMARY KEY,
#       name TEXT NOT NULL,
#       value REAL DEFAULT 0
#   )
#
# INSERT:
#   INSERT INTO table (col1, col2) VALUES (?, ?)
#
# SELECT:
#   SELECT * FROM table WHERE condition ORDER BY col LIMIT n
#
# UPDATE:
#   UPDATE table SET col1 = ?, col2 = ? WHERE id = ?
#
# DELETE:
#   DELETE FROM table WHERE id = ?
#
# ======================================================================


# ======================================================================
# 🗄️ QUICK REFERENCE - SQLite Data Types
# ======================================================================
#
# NULL     - NULL value
# INTEGER  - Signed integer (1, 2, 3, 4, 6, or 8 bytes)
# REAL     - Floating point (8 bytes)
# TEXT     - Text string (UTF-8, UTF-16BE or UTF-16LE)
# BLOB     - Binary data (stored exactly as input)
#
# ======================================================================


# ======================================================================
# 🗄️ QUICK REFERENCE - Row Factory
# ======================================================================
#
# Access columns by name:
#   conn.row_factory = sqlite3.Row
#   cursor = conn.cursor()
#   cursor.execute("SELECT * FROM table")
#   row = cursor.fetchone()
#   print(row['column_name'])  # Access by name
#   print(row[0])              # Still works by index
#
# Custom dictionary factory:
#   def dict_factory(cursor, row):
#       return {col[0]: row[idx] for idx, col in enumerate(cursor.description)}
#   conn.row_factory = dict_factory
#
# ======================================================================
