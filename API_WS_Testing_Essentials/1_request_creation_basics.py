# ======================================================================
# 🌐 HTTP METHODS WITH JSON-SERVER EXERCISES
# ======================================================================
# Practice exercises - Write everything from scratch!
# Prerequisites: json-server installed, requests library
# ======================================================================

# Terminal: npm install -g json-server
# Python: pip install requests

import json

import requests

# Base URL for json-server (default port)
BASE_URL = "http://localhost:3000"
USERS = BASE_URL + "/users"
POSTS = BASE_URL + "/posts"
COMMENTS = BASE_URL + "/comments"


# =====================================================================
#                    SECTION 1: JSON-SERVER SETUP
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 1: INSTALL JSON-SERVER
#
# Learn: Setting up json-server
#
# Tasks:
# 1. Install Node.js if not already installed (nodejs.org)
# 2. Install json-server: npm install -g json-server
# 3. Verify installation: json-server --version
# 4. Understand: json-server creates a REST API from a JSON file
# 5. No backend coding required - perfect for learning!
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 2: CREATE A DATABASE FILE
#
# Learn: db.json structure
#
# Tasks:
# 1. Create a file named db.json in your project folder
# 2. Add the following structure:
#    {
#      "users": [],
#      "posts": [],
#      "comments": []
#    }
# 3. Each key becomes an API endpoint (/users, /posts, /comments)
# 4. Save the file
# 5. This is your "database" that json-server will use
# ----------------------------------------------------------------------

# Save this as db.json:
DB_TEMPLATE = """
{
  "users": [
    { "id": 1, "name": "Alice", "email": "alice@example.com", "age": 28 },
    { "id": 2, "name": "Bob", "email": "bob@example.com", "age": 34 },
    { "id": 3, "name": "Charlie", "email": "charlie@example.com", "age": 22 }
  ],
  "posts": [
    { "id": 1, "title": "Hello World", "content": "My first post", "userId": 1 },
    { "id": 2, "title": "Learning Python", "content": "Python is great", "userId": 2 }
  ],
  "comments": [
    { "id": 1, "text": "Great post!", "postId": 1, "userId": 2 },
    { "id": 2, "text": "Thanks for sharing", "postId": 1, "userId": 3 }
  ]
}
"""


# ----------------------------------------------------------------------
# 🟢 3: START JSON-SERVER
#
# Learn: Running the server
#
# Tasks:
# 1. Open terminal in the folder with db.json
# 2. Run: json-server --watch db.json
# 3. Server starts at http://localhost:3000
# 4. You'll see available endpoints listed
# 5. Keep this terminal open while practicing
# 6. The --watch flag auto-reloads on db.json changes
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 4: INSTALL PYTHON REQUESTS LIBRARY
#
# Learn: requests module for HTTP
#
# Tasks:
# 1. Install: pip install requests
# 2. Import: import requests
# 3. This library makes HTTP requests easy
# 4. Works with any REST API, not just json-server
# 5. Verify: requests.__version__
# ----------------------------------------------------------------------

print(requests.__version__)

# ----------------------------------------------------------------------
# 🟢 5: TEST SERVER CONNECTION
#
# Learn: Basic GET request
#
# Tasks:
# 1. With json-server running, make a request
# 2. response = requests.get('http://localhost:3000/users')
# 3. Check response.status_code (should be 200)
# 4. Print response.json() to see the data
# 5. If it works, you're ready to practice!
# ----------------------------------------------------------------------

users_response = requests.get(BASE_URL + "/users")
print(users_response.status_code)
print(users_response.json())

posts_response = requests.get(BASE_URL + "/posts")
print(posts_response.status_code)
print(posts_response.json())

comments_response = requests.get(BASE_URL + "/comments")
print(comments_response.status_code)
print(comments_response.json())

# =====================================================================
#                    SECTION 2: GET REQUESTS (FETCH DATA)
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 6: GET ALL ITEMS FROM A RESOURCE
#
# Learn: requests.get() for fetching lists
#
# Tasks:
# 1. Make GET request: requests.get(f'{BASE_URL}/users')
# 2. Store the response in a variable
# 3. Check response.status_code == 200
# 4. Parse JSON: data = response.json()
# 5. Print all users
# ----------------------------------------------------------------------

response = requests.get(BASE_URL + "/users")
data = response.json()
print(data)

# ----------------------------------------------------------------------
# 🟢 7: GET A SINGLE ITEM BY ID
#
# Learn: GET with ID in URL
#
# Tasks:
# 1. Get user with ID 1: requests.get(f'{BASE_URL}/users/1')
# 2. This returns a single object, not a list
# 3. Parse the JSON response
# 4. Print the user's name and email
# 5. Try getting a non-existent ID and check status_code
# ----------------------------------------------------------------------

single_result = requests.get(BASE_URL + "/users/1")
data = single_result.json()
print(data)
print(single_result.status_code)

single_result = requests.get(BASE_URL + "/users/500")
data = single_result.json()
print(data)
print(single_result.status_code)

# ----------------------------------------------------------------------
# 🟡 8: FILTER RESULTS WITH QUERY PARAMETERS
#
# Learn: GET with query strings
#
# Tasks:
# 1. Filter by field: requests.get(f'{BASE_URL}/users?name=Alice')
# 2. Or use params dict: requests.get(url, params={'name': 'Alice'})
# 3. Filter by age: params={'age': 28}
# 4. Multiple filters: params={'age': 28, 'name': 'Alice'}
# 5. Returns a list of matching items
# ----------------------------------------------------------------------

bob = requests.get(USERS + "?name=Bob")
print(bob.json())

params = {"age": 34}
bob = requests.get(USERS, params=params)
print(bob.json())

params = {"name": "Alice", "age": 28}
response = requests.get(USERS, params=params)
print(response.json())

# ----------------------------------------------------------------------
# 🟡 9: SEARCH AND FULL-TEXT QUERIES
#
# Learn: json-server search features
#
# Tasks:
# 1. Full-text search: params={'q': 'python'}
# 2. This searches all fields for the term
# 3. Search users: requests.get(f'{BASE_URL}/users', params={'q': 'alice'})
# 4. Case-insensitive by default
# 5. Try searching posts for keywords
# ----------------------------------------------------------------------

params = {"q": "lie"}
response = requests.get(USERS, params=params)
print(response.json())

# ----------------------------------------------------------------------
# 🟡 10: PAGINATION
#
# Learn: _page and _limit parameters
#
# Tasks:
# 1. Get first page: params={'_page': 1, '_limit': 2}
# 2. Get second page: params={'_page': 2, '_limit': 2}
# 3. Check response headers for total count
# 4. response.headers.get('X-Total-Count')
# 5. Calculate total pages from count and limit
# ----------------------------------------------------------------------

params = {"_page": 1, "_limit": 2}
response = requests.get(USERS, params=params)
print(response.json())

params = {"_page": 2, "_limit": 2}
response = requests.get(USERS, params=params)
print(response.json())

print(response.headers.get("X-Total-Count"))

# ----------------------------------------------------------------------
# 🟡 11: SORTING RESULTS
#
# Learn: _sort and _order parameters
#
# Tasks:
# 1. Sort by name: params={'_sort': 'name'}
# 2. Sort descending: params={'_sort': 'name', '_order': 'desc'}
# 3. Sort by age ascending: params={'_sort': 'age', '_order': 'asc'}
# 4. Multiple sort fields: params={'_sort': 'age,name', '_order': 'desc,asc'}
# 5. Combine sorting with pagination
# ----------------------------------------------------------------------

params = {"_sort": "age", "_order": "desc"}
response = requests.get(USERS, params=params)
print(response.json())

params = {"_sort": "age", "_order": "asc"}
response = requests.get(USERS, params=params)
print(response.json())

params = {"_sort": "age,name", "_order": "desc,desc"}
response = requests.get(USERS, params=params)
print(response.json())

# ----------------------------------------------------------------------
# 🟡 12: SLICE RESULTS
#
# Learn: _start and _end parameters
#
# Tasks:
# 1. Get items 0-2: params={'_start': 0, '_end': 2}
# 2. Get items 2-4: params={'_start': 2, '_end': 4}
# 3. Alternative: params={'_start': 0, '_limit': 5}
# 4. _start is inclusive, _end is exclusive
# 5. Useful for custom pagination
# ----------------------------------------------------------------------

params = {"_start": 0, "_end": 2}
response = requests.get(USERS, params=params)
print(response.json())

params = {"_start": 2, "_end": 4}
response = requests.get(USERS, params=params)
print(response.json())

params = {"_start": 0, "_limit": 5}
response = requests.get(USERS, params=params)
print(response.json())

# ----------------------------------------------------------------------
# 🟡 13: GET NESTED RESOURCES
#
# Learn: _embed and _expand
#
# Tasks:
# 1. Get posts with comments: f'{BASE_URL}/posts?_embed=comments'
# 2. Get comments with post: f'{BASE_URL}/comments?_expand=post'
# 3. _embed gets child resources (one-to-many)
# 4. _expand gets parent resource (many-to-one)
# 5. Examine the nested structure in response
# ----------------------------------------------------------------------

# response = requests.get(BASE_URL + "/posts?_embed=comments")
# print(response.json())

# response = requests.get(BASE_URL + "/posts?_expand=post")
# print(response.json())

# ----------------------------------------------------------------------
# 🟡 14: OPERATORS FOR FILTERING
#
# Learn: _gte, _lte, _ne, _like
#
# Tasks:
# 1. Greater than or equal: params={'age_gte': 25}
# 2. Less than or equal: params={'age_lte': 30}
# 3. Not equal: params={'name_ne': 'Alice'}
# 4. Like (regex): params={'name_like': '^A'}  # Starts with A
# 5. Combine multiple operators
# ----------------------------------------------------------------------

params = {"age_gte": 25}
response = requests.get(USERS, params=params)
print(response.json())

params = {"age_lte": 25}
response = requests.get(USERS, params=params)
print(response.json())

params = {"name_ne": "Alice"}
response = requests.get(USERS, params=params)
print(response.json())

params = {"name_like": "^N"}
response = requests.get(USERS, params=params)
print(response.json())

# =====================================================================
#                    SECTION 3: POST REQUESTS (CREATE DATA)
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 15: CREATE A NEW ITEM
#
# Learn: requests.post() for creating data
#
# Tasks:
# 1. Prepare new user data as a dictionary
# 2. new_user = {'name': 'Diana', 'email': 'diana@example.com', 'age': 25}
# 3. POST request: requests.post(f'{BASE_URL}/users', json=new_user)
# 4. Check response.status_code == 201 (Created)
# 5. The response contains the created item with its new ID
# ----------------------------------------------------------------------


new_user = {
    "id": 13,
    "name": "Paul",
    "role": "user",
    "age": 29,
    "active": True,
    "city": "Envigado",
}

# response = requests.post(USERS, json=new_user)
# print(response.status_code)

# ----------------------------------------------------------------------
# 🟢 16: VERIFY CREATED ITEM
#
# Learn: Confirming POST success
#
# Tasks:
# 1. Create a new item with POST
# 2. Get the returned ID from response.json()['id']
# 3. Make a GET request for that ID
# 4. Verify the data matches what you sent
# 5. Also check db.json file - it's updated automatically!
# ----------------------------------------------------------------------

# id = response.json()["id"]
# print(id)

# params = {"id": 13}

# response = requests.get(USERS, params)
# print(response.json())


# ----------------------------------------------------------------------
# 🟡 17: CREATE MULTIPLE ITEMS
#
# Learn: Loop through POST requests
#
# Tasks:
# 1. Create a list of new users to add
# 2. Loop through each user
# 3. Make a POST request for each
# 4. Collect all new IDs
# 5. Verify all were created with a GET request
# ----------------------------------------------------------------------

users = [
    {
        "id": 13,
        "name": "Oscar",
        "role": "admin",
        "age": 45,
        "active": True,
        "city": "Stockholm",
    },
    {
        "id": 14,
        "name": "Peggy",
        "role": "user",
        "age": 32,
        "active": False,
        "city": "Zurich",
    },
    {
        "id": 15,
        "name": "Quentin",
        "role": "moderator",
        "age": 29,
        "active": True,
        "city": "Vienna",
    },
    {
        "id": 16,
        "name": "Rita",
        "role": "user",
        "age": 21,
        "active": False,
        "city": "Prague",
    },
    {
        "id": 17,
        "name": "Sybil",
        "role": "user",
        "age": 36,
        "active": True,
        "city": "Dublin",
    },
    {
        "id": 18,
        "name": "Trent",
        "role": "admin",
        "age": 39,
        "active": False,
        "city": "Budapest",
    },
    {
        "id": 19,
        "name": "Uma",
        "role": "moderator",
        "age": 25,
        "active": True,
        "city": "Rome",
    },
    {
        "id": 20,
        "name": "Victor",
        "role": "user",
        "age": 34,
        "active": True,
        "city": "Oslo",
    },
    {
        "id": 21,
        "name": "Wendy",
        "role": "user",
        "age": 28,
        "active": False,
        "city": "Madrid",
    },
    {
        "id": 22,
        "name": "Xavier",
        "role": "admin",
        "age": 50,
        "active": True,
        "city": "Berlin",
    },
]

# users_id = list()
# for user in users:
#     response = requests.post(USERS, json=user)
#     users_id.append(response.json()["id"])

# for id in users_id:
#     response = requests.get(USERS, json={"id": id})
#     print(response.status_code)

# ----------------------------------------------------------------------
# 🟡 18: CREATE WITH RELATIONSHIPS
#
# Learn: Foreign keys in json-server
#
# Tasks:
# 1. Create a new post for an existing user
# 2. Include userId in the post data
# 3. new_post = {'title': 'New Post', 'content': '...', 'userId': 1}
# 4. POST to /posts
# 5. Verify with GET /posts?_expand=user
# ----------------------------------------------------------------------

new_post = {
    "id": 10,
    "text": "This is crazy",
    "postId": 2,
    "userId": 4,
}

response = requests.post(POSTS, json=new_post)
print(response.status_code)

params = "?_expand=user"
response = requests.get(POSTS + params)
print(response.json())

# ----------------------------------------------------------------------
# 🟡 19: HANDLE POST ERRORS
#
# Learn: Error handling for create operations
#
# Tasks:
# 1. Try POST with missing required data
# 2. Try POST to non-existent endpoint
# 3. Check response.status_code for errors
# 4. json-server is lenient, but real APIs return 400/422
# 5. Create a function that validates before posting
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 20: SET CUSTOM HEADERS
#
# Learn: Content-Type and other headers
#
# Tasks:
# 1. requests.post() with json= sets Content-Type automatically
# 2. Manual way: headers={'Content-Type': 'application/json'}
# 3. Pass headers to request: requests.post(url, json=data, headers=headers)
# 4. View request headers: response.request.headers
# 5. Understand JSON vs form data
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 4: PUT REQUESTS (UPDATE DATA)
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 21: UPDATE AN ENTIRE ITEM
#
# Learn: requests.put() for full replacement
#
# Tasks:
# 1. Prepare complete updated data (all fields)
# 2. updated_user = {'name': 'Alice Smith', 'email': 'alice@new.com', 'age': 29}
# 3. PUT request: requests.put(f'{BASE_URL}/users/1', json=updated_user)
# 4. Check response.status_code == 200
# 5. PUT replaces the ENTIRE resource
# ----------------------------------------------------------------------

before_update = requests.get(USERS + "/1")

updated_user = {
    "name": "Alice Smith",
    "email": "alice@new.com",
    "age": 29,
}

response = requests.put(USERS + "/1", json=updated_user)
print(response.status_code)

# ----------------------------------------------------------------------
# 🟢 22: VERIFY UPDATE
#
# Learn: Confirming PUT success
#
# Tasks:
# 1. GET the item before updating
# 2. Make the PUT request
# 3. GET the item after updating
# 4. Compare before and after
# 5. Note: ID is preserved automatically
# ----------------------------------------------------------------------

after_update = requests.get(USERS + "/1")

# assert before_update.json() != after_update.json()

# ----------------------------------------------------------------------
# 🟡 23: PARTIAL UPDATE WITH PATCH
#
# Learn: requests.patch() for partial updates
#
# Tasks:
# 1. PATCH only updates specified fields
# 2. partial_update = {'age': 30}  # Only update age
# 3. requests.patch(f'{BASE_URL}/users/1', json=partial_update)
# 4. Other fields remain unchanged
# 5. Compare PUT (full replace) vs PATCH (partial update)
# ----------------------------------------------------------------------

partial_update = {"age": 30}
response = requests.patch(USERS + "/2", json=partial_update)
print(response.status_code)


# ----------------------------------------------------------------------
# 🟡 24: UPDATE NON-EXISTENT ITEM
#
# Learn: Handling update errors
#
# Tasks:
# 1. Try PUT to an ID that doesn't exist
# 2. Check the response status code
# 3. json-server returns 404 for missing resources
# 4. Create a function that checks existence before updating
# 5. Handle the error gracefully
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 25: UPDATE WITH VALIDATION
#
# Learn: Validate data before updating
#
# Tasks:
# 1. Create a validation function for user data
# 2. Check required fields are present
# 3. Check data types (age is int, email has @)
# 4. Only proceed with PUT if validation passes
# 5. Return helpful error messages for invalid data
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 5: DELETE REQUESTS (REMOVE DATA)
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 26: DELETE AN ITEM
#
# Learn: requests.delete()
#
# Tasks:
# 1. DELETE request: requests.delete(f'{BASE_URL}/users/3')
# 2. Check response.status_code == 200
# 3. Verify item is gone with GET request
# 4. GET should return 404 for deleted item
# 5. Check db.json - item is removed
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 27: CONFIRM BEFORE DELETE
#
# Learn: Safe delete patterns
#
# Tasks:
# 1. GET the item first to confirm it exists
# 2. Optionally show item details to user
# 3. Ask for confirmation (in real app)
# 4. Only then perform DELETE
# 5. Return success/failure message
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 28: DELETE NON-EXISTENT ITEM
#
# Learn: Handling delete errors
#
# Tasks:
# 1. Try DELETE on an ID that doesn't exist
# 2. Check the response status code (404)
# 3. Handle the error appropriately
# 4. Create a safe_delete() function
# 5. Return meaningful feedback
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 29: DELETE MULTIPLE ITEMS
#
# Learn: Batch delete operations
#
# Tasks:
# 1. Create a list of IDs to delete
# 2. Loop through and delete each
# 3. Track successes and failures
# 4. Report results at the end
# 5. Consider: what if some fail?
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 30: DELETE WITH CASCADE CONSIDERATION
#
# Learn: Handling related data
#
# Tasks:
# 1. Note: json-server doesn't auto-delete related items
# 2. If you delete a user, their posts remain (orphaned)
# 3. Before deleting user, find their posts
# 4. Delete posts first, then delete user
# 5. Create a function that handles this cascade
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 6: COMBINING OPERATIONS
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 31: CRUD FUNCTIONS
#
# Learn: Create reusable CRUD functions
#
# Tasks:
# 1. Create: create_user(name, email, age)
# 2. Read: get_user(id), get_all_users()
# 3. Update: update_user(id, data)
# 4. Delete: delete_user(id)
# 5. Each function should handle errors and return useful info
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 32: BUILD A USER CLASS
#
# Learn: OOP approach to API resources
#
# Tasks:
# 1. Create a User class
# 2. Methods: save() for create/update, delete(), refresh()
# 3. Class method: User.get(id), User.all()
# 4. Handle the API calls internally
# 5. Test all operations with instances
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 33: GENERIC RESOURCE CLASS
#
# Learn: Reusable API wrapper
#
# Tasks:
# 1. Create a Resource class that works with any endpoint
# 2. Initialize with endpoint name: Resource('users')
# 3. Methods: all(), get(id), create(data), update(id, data), delete(id)
# 4. Test with users, posts, and comments
# 5. Add error handling throughout
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 34: TRANSACTION-LIKE OPERATIONS
#
# Learn: Multiple operations that should succeed together
#
# Tasks:
# 1. Create a user and their first post together
# 2. If post creation fails, delete the user (rollback)
# 3. Create a function: create_user_with_post(user_data, post_data)
# 4. Return both created items or None if failed
# 5. Note: json-server has no real transactions
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 35: SYNC LOCAL DATA WITH SERVER
#
# Learn: Comparing and syncing data
#
# Tasks:
# 1. Have a local list of items
# 2. GET all items from server
# 3. Find items to add (in local, not on server)
# 4. Find items to remove (on server, not in local)
# 5. POST new items, DELETE removed items
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 7: ERROR HANDLING & BEST PRACTICES
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 36: CHECK RESPONSE STATUS
#
# Learn: Status code handling
#
# Tasks:
# 1. 200 OK - Success (GET, PUT, DELETE)
# 2. 201 Created - Success (POST)
# 3. 404 Not Found - Resource doesn't exist
# 4. 500 Server Error - Something went wrong
# 5. Create a function that handles all these cases
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 37: USE RAISE_FOR_STATUS
#
# Learn: response.raise_for_status()
#
# Tasks:
# 1. This method raises exception for 4xx/5xx status codes
# 2. Wrap in try/except: requests.exceptions.HTTPError
# 3. response.raise_for_status()
# 4. Cleaner than checking status_code manually
# 5. Combine with specific error handling
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 38: HANDLE CONNECTION ERRORS
#
# Learn: requests.exceptions
#
# Tasks:
# 1. What if json-server isn't running?
# 2. Catch: requests.exceptions.ConnectionError
# 3. What if request times out?
# 4. Use timeout parameter: requests.get(url, timeout=5)
# 5. Catch: requests.exceptions.Timeout
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 39: RETRY FAILED REQUESTS
#
# Learn: Implementing retry logic
#
# Tasks:
# 1. Create a function with retry capability
# 2. Parameters: max_retries, delay_between_retries
# 3. Retry on connection errors or timeouts
# 4. Don't retry on 404 (won't help)
# 5. Return result or raise after max retries
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 40: LOGGING API CALLS
#
# Learn: Tracking requests for debugging
#
# Tasks:
# 1. Create a wrapper function that logs each request
# 2. Log: method, URL, status code, response time
# 3. Use time module to measure response time
# 4. Write logs to a file
# 5. Helpful for debugging and monitoring
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 8: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 41: USER MANAGEMENT SYSTEM
#
# Scenario: Complete user CRUD with menu
#
# Tasks:
# 1. Display menu: List, Add, Edit, Delete, Search, Quit
# 2. List: Show all users in formatted table
# 3. Add: Prompt for name, email, age and POST
# 4. Edit: Choose user by ID, show current values, update
# 5. Delete: Choose user by ID, confirm, DELETE
# 6. Search: Search by name or email
# 7. Loop until Quit
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 42: BLOG POST MANAGER
#
# Scenario: Manage posts with comments
#
# Tasks:
# 1. List posts with comment counts
# 2. View single post with all comments
# 3. Create new post (assign to a user)
# 4. Add comment to a post
# 5. Delete post (and its comments)
# 6. Search posts by keyword
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 43: DATA IMPORT/EXPORT TOOL
#
# Scenario: Backup and restore data
#
# Tasks:
# 1. Export: GET all data, save to JSON file
# 2. Export should get users, posts, comments
# 3. Import: Read JSON file, POST all items
# 4. Handle ID conflicts (skip or overwrite)
# 5. Report: items exported/imported counts
# 6. Create timestamped backup files
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 44: API TESTING TOOL
#
# Scenario: Automated API endpoint testing
#
# Tasks:
# 1. Test all CRUD operations for each endpoint
# 2. Create test data, verify it, clean up after
# 3. Test error cases (404, invalid data)
# 4. Report pass/fail for each test
# 5. Calculate success rate
# 6. Save test results to file
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 45: DATA MIGRATION SCRIPT
#
# Scenario: Transform and migrate data
#
# Tasks:
# 1. Read users from old format (e.g., CSV)
# 2. Transform to new format (add fields, rename)
# 3. POST each transformed user
# 4. Handle duplicates (check email exists)
# 5. Log all migrations with status
# 6. Support rollback if errors occur
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 46: BULK OPERATIONS TOOL
#
# Scenario: Perform operations on many items
#
# Tasks:
# 1. Bulk update: Change field for multiple items
#    Example: Set all users' status to 'active'
# 2. Bulk delete: Delete items matching criteria
# 3. Show progress for large operations
# 4. Allow cancellation mid-operation
# 5. Report success/failure counts
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 47: RELATIONSHIP MANAGER
#
# Scenario: Handle complex relationships
#
# Tasks:
# 1. Show user with all their posts and comments
# 2. Show post with author info and all comments
# 3. Find all users who commented on a post
# 4. Find all posts a user has commented on
# 5. Create formatted reports of relationships
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 48: API MONITOR
#
# Scenario: Monitor API health over time
#
# Tasks:
# 1. Periodically check if server is responding
# 2. Measure response times
# 3. Track total items in each resource
# 4. Alert if response time > threshold
# 5. Log history to file
# 6. Show statistics over time
# ----------------------------------------------------------------------


# ======================================================================
# 🌐 QUICK REFERENCE - HTTP Methods
# ======================================================================
#
# GET - Fetch data
#   requests.get(url)                    # Get all
#   requests.get(f'{url}/1')             # Get by ID
#   requests.get(url, params={...})      # With query params
#
# POST - Create new data
#   requests.post(url, json={...})       # Create item
#   Returns 201 Created on success
#   Response contains created item with ID
#
# PUT - Replace entire item
#   requests.put(f'{url}/1', json={...}) # Full update
#   Must include ALL fields
#   Returns 200 OK on success
#
# PATCH - Partial update
#   requests.patch(f'{url}/1', json={...})  # Partial update
#   Only include fields to change
#   Returns 200 OK on success
#
# DELETE - Remove data
#   requests.delete(f'{url}/1')          # Delete by ID
#   Returns 200 OK on success
#
# ======================================================================


# ======================================================================
# 🌐 QUICK REFERENCE - Response Handling
# ======================================================================
#
# Status codes:
#   response.status_code                 # Numeric code
#   200 - OK (success for GET, PUT, PATCH, DELETE)
#   201 - Created (success for POST)
#   404 - Not Found
#   400 - Bad Request
#   500 - Server Error
#
# Get data:
#   response.json()                      # Parse JSON to dict/list
#   response.text                        # Raw text
#   response.content                     # Raw bytes
#
# Check success:
#   response.ok                          # True if status < 400
#   response.raise_for_status()          # Raises exception if error
#
# Headers:
#   response.headers                     # Response headers dict
#   response.headers['Content-Type']
#
# ======================================================================


# ======================================================================
# 🌐 QUICK REFERENCE - json-server Query Parameters
# ======================================================================
#
# Filtering:
#   ?name=Alice                          # Exact match
#   ?age_gte=25                          # Greater than or equal
#   ?age_lte=30                          # Less than or equal
#   ?name_ne=Bob                         # Not equal
#   ?name_like=^A                        # Regex match
#
# Full-text search:
#   ?q=keyword                           # Search all fields
#
# Pagination:
#   ?_page=1&_limit=10                   # Page-based
#   ?_start=0&_end=10                    # Slice-based
#
# Sorting:
#   ?_sort=name                          # Sort by field (asc)
#   ?_sort=name&_order=desc              # Sort descending
#   ?_sort=age,name&_order=desc,asc      # Multiple sorts
#
# Relationships:
#   ?_embed=comments                     # Include children
#   ?_expand=user                        # Include parent
#
# ======================================================================


# ======================================================================
# 🌐 QUICK REFERENCE - Common Patterns
# ======================================================================
#
# Pattern 1: Safe GET
# -------------------
#   def get_user(user_id):
#       response = requests.get(f'{BASE_URL}/users/{user_id}')
#       if response.status_code == 200:
#           return response.json()
#       elif response.status_code == 404:
#           return None
#       else:
#           response.raise_for_status()
#
# Pattern 2: Create with validation
# ---------------------------------
#   def create_user(name, email, age):
#       if not name or not email:
#           raise ValueError("Name and email required")
#       data = {'name': name, 'email': email, 'age': age}
#       response = requests.post(f'{BASE_URL}/users', json=data)
#       response.raise_for_status()
#       return response.json()
#
# Pattern 3: Update existing
# --------------------------
#   def update_user(user_id, **kwargs):
#       response = requests.patch(f'{BASE_URL}/users/{user_id}', json=kwargs)
#       if response.status_code == 404:
#           raise ValueError(f"User {user_id} not found")
#       response.raise_for_status()
#       return response.json()
#
# Pattern 4: Safe delete
# ----------------------
#   def delete_user(user_id):
#       # Check exists first
#       response = requests.get(f'{BASE_URL}/users/{user_id}')
#       if response.status_code == 404:
#           return False
#       # Delete
#       response = requests.delete(f'{BASE_URL}/users/{user_id}')
#       return response.status_code == 200
#
# ======================================================================


# ======================================================================
# 🚀 SETUP INSTRUCTIONS
# ======================================================================
#
# 1. Install Node.js:
#    Download from https://nodejs.org/
#
# 2. Install json-server globally:
#    npm install -g json-server
#
# 3. Create db.json file with initial data:
#    {
#      "users": [],
#      "posts": [],
#      "comments": []
#    }
#
# 4. Start json-server:
#    json-server --watch db.json
#    # Or with custom port:
#    json-server --watch db.json --port 3001
#
# 5. Install Python requests:
#    pip install requests
#
# 6. Test connection:
#    >>> import requests
#    >>> requests.get('http://localhost:3000/users')
#
# 7. Useful json-server options:
#    --watch       Auto-reload on db.json changes
#    --port 3001   Use different port
#    --delay 1000  Add 1 second delay (simulate slow network)
#    --routes      Custom routes file
#
# ======================================================================


# ======================================================================
# 🌐 EXAMPLE: COMPLETE CRUD OPERATIONS
# ======================================================================


def example_crud_operations():
    """Demonstrates all CRUD operations."""

    BASE = "http://localhost:3000"

    # CREATE - POST
    print("Creating new user...")
    new_user = {"name": "Test User", "email": "test@test.com", "age": 25}
    response = requests.post(f"{BASE}/users", json=new_user)
    created_user = response.json()
    user_id = created_user["id"]
    print(f"Created user with ID: {user_id}")

    # READ - GET
    print("\nReading user...")
    response = requests.get(f"{BASE}/users/{user_id}")
    user = response.json()
    print(f"User: {user}")

    # UPDATE - PUT (full replace)
    print("\nUpdating user (PUT)...")
    updated_data = {"name": "Updated User", "email": "updated@test.com", "age": 26}
    response = requests.put(f"{BASE}/users/{user_id}", json=updated_data)
    print(f"Updated: {response.json()}")

    # UPDATE - PATCH (partial)
    print("\nUpdating user (PATCH)...")
    partial_data = {"age": 27}
    response = requests.patch(f"{BASE}/users/{user_id}", json=partial_data)
    print(f"Patched: {response.json()}")

    # DELETE
    print("\nDeleting user...")
    response = requests.delete(f"{BASE}/users/{user_id}")
    print(f"Delete status: {response.status_code}")

    # Verify deletion
    response = requests.get(f"{BASE}/users/{user_id}")
    print(f"After delete, GET status: {response.status_code}")


# Uncomment to run:
# example_crud_operations()

# ======================================================================# ======================================================================
