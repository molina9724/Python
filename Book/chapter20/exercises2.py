# ======================================================================
# 📧 SENDING EMAIL, TEXTS, AND PUSH NOTIFICATIONS EXERCISES
# ======================================================================
# Practice exercises - Write everything from scratch!
# Prerequisites: ezgmail installed, Gmail API configured, requests installed
# ======================================================================

# pip install ezgmail requests

import json

import ezgmail
import requests

# =====================================================================
#                    SECTION 1: EZGMAIL SETUP AND SENDING
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 1: INITIALIZE EZGMAIL
#
# Learn: ezgmail.init(), ezgmail.EMAIL_ADDRESS
#
# Tasks:
# 1. Import the ezgmail module
# 2. Call ezgmail.init() to initialize (first time opens browser)
# 3. Print ezgmail.EMAIL_ADDRESS to see which account is configured
# 4. Verify no errors appear
# 5. Understand the role of credentials.json and token.json
# ----------------------------------------------------------------------

print(ezgmail.EMAIL_ADDRESS)

# ----------------------------------------------------------------------
# 🟢 2: SEND A SIMPLE EMAIL
#
# Learn: ezgmail.send()
#
# Tasks:
# 1. Use ezgmail.send() with recipient, subject, and body
# 2. Send a test email to yourself (or a test account)
# 3. Check your inbox to verify the email arrived
# 4. Try sending to a different email address
# 5. Note: Gmail may block repeated identical emails (spam protection)
# ----------------------------------------------------------------------

# ezgmail.send(
#     "molina9724@gmail.com",
#     "Hello",
#     "Hello",
# )
# ezgmail.send(
#     "antigravityhack25@gmail.com",
#     "From me",
#     "To you",
# )

# ----------------------------------------------------------------------
# 🟢 3: SEND EMAIL WITH CC AND BCC
#
# Learn: cc and bcc keyword arguments
#
# Tasks:
# 1. Send an email with a cc (carbon copy) recipient
# 2. Send an email with a bcc (blind carbon copy) recipient
# 3. Send an email with multiple cc recipients (comma-separated)
# 4. Verify recipients received the emails
# 5. Note the difference between cc (visible) and bcc (hidden)
# ----------------------------------------------------------------------

# ezgmail.send(
#     "molina9724@gmail.com",
#     "With CC and BCC",
#     "Fucker",
#     cc="antigravityhack25@gmail.com",
#     bcc="dmcuentaps5@gmail.com",
# )

# ----------------------------------------------------------------------
# 🟡 4: SEND EMAIL WITH ATTACHMENTS
#
# Learn: Attachment list parameter
#
# Tasks:
# 1. Create a simple text file to attach
# 2. Send an email with one attachment
# 3. Send an email with multiple attachments (list of filenames)
# 4. Verify attachments arrive correctly
# 5. Note: Gmail blocks .exe and .zip files for security
# ----------------------------------------------------------------------

# multiple_emails = "molina9724@gmail.com,antigravityhack25@gmail.com"

# ezgmail.send(
#     recipient=multiple_emails,
#     subject="Email with attachment",
#     body="Nothing to say my boy",
#     attachments=[
#         "/Users/daniel_molina/Downloads/keyboard-shortcuts-macos.pdf",
#         "/Users/daniel_molina/Downloads/alarm.wav",
#     ],
# )

# ----------------------------------------------------------------------
# 🟡 5: BUILD AN EMAIL FROM VARIABLES
#
# Learn: Constructing emails programmatically
#
# Tasks:
# 1. Create variables for recipient, subject, and body
# 2. Build the email body using string formatting or f-strings
# 3. Include dynamic content (e.g., current date, user's name)
# 4. Send the constructed email
# 5. Create a function: send_greeting(name, email)
# ----------------------------------------------------------------------


def send_greeting(name: str, email: str):
    ezgmail.send(
        email,
        f"Important things to discuss {name}",
        f"We know who you are {name} and where you live",
    )


# send_greeting("Carlos", "molina9724@gmail.com")

# =====================================================================
#                    SECTION 2: READING EMAIL
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 6: GET UNREAD EMAILS
#
# Learn: ezgmail.unread()
#
# Tasks:
# 1. Call ezgmail.unread() to get unread email threads
# 2. Print the number of unread threads
# 3. Use ezgmail.summary() to display a summary
# 4. Access the first unread thread
# 5. Understand that unread() returns GmailThread objects
# ----------------------------------------------------------------------

from ezgmail import GmailMessage, GmailThread

unread_threads: list[GmailThread] = ezgmail.unread(maxResults=5)
print(len(unread_threads))
print(ezgmail.summary(unread_threads))

first_unread_thread: GmailThread = unread_threads[0]
print(first_unread_thread.senders())

first_message: GmailMessage = first_unread_thread.messages[0]
print(first_message)
print(first_message.recipient)
print(first_message.sender)

# ----------------------------------------------------------------------
# 🟢 7: GET RECENT EMAILS
#
# Learn: ezgmail.recent(), maxResults parameter
#
# Tasks:
# 1. Call ezgmail.recent() to get the 25 most recent threads
# 2. Print the number of threads returned
# 3. Use maxResults to get more threads (e.g., maxResults=100)
# 4. Display a summary of recent threads
# 5. Compare recent() with unread()
# ----------------------------------------------------------------------

recent_threads: list[GmailThread] = ezgmail.recent()
print(len(recent_threads))

recent_threads = ezgmail.recent(maxResults=3)
print(ezgmail.summary(recent_threads))

unread_threads = ezgmail.unread(maxResults=3)
print(ezgmail.summary(unread_threads))

# ----------------------------------------------------------------------
# 🟡 8: ACCESS THREAD PROPERTIES
#
# Learn: GmailThread object, messages attribute
#
# Tasks:
# 1. Get a list of threads (unread or recent)
# 2. Access the first thread
# 3. Print the thread using str() to see its representation
# 4. Access the messages attribute (list of GmailMessage objects)
# 5. Print how many messages are in the thread
# ----------------------------------------------------------------------

first_recent_thread: GmailThread = recent_threads[0]
print(str(first_recent_thread))

my_list: list[GmailMessage] = first_recent_thread.messages

print("---------------------------------------------")

print(len(my_list))
print(my_list[0].body)
# print(messages[1].body)

# ----------------------------------------------------------------------
# 🟡 9: ACCESS MESSAGE PROPERTIES
#
# Learn: GmailMessage attributes (subject, body, sender, recipient, timestamp)
#
# Tasks:
# 1. Get a thread and access its first message
# 2. Print the message's subject
# 3. Print the message's body
# 4. Print the sender's email address
# 5. Print the timestamp (it's a datetime object)
# ----------------------------------------------------------------------

first_message = my_list[0]
print(first_message.subject)
print(first_message.body)
print(first_message.sender)
print(first_message.timestamp)

# ----------------------------------------------------------------------
# 🟡 10: ITERATE THROUGH ALL MESSAGES
#
# Learn: Looping through threads and messages
#
# Tasks:
# 1. Get recent threads
# 2. Loop through each thread
# 3. For each thread, loop through its messages
# 4. Print subject and sender for each message
# 5. Count total messages across all threads
# ----------------------------------------------------------------------

print("-----------------------------------------------------")

total_messages = 0
for thread in recent_threads:
    for my_message in thread.messages:
        print(my_message.subject, my_message.sender)
        total_messages += 1

print(total_messages)

# =====================================================================
#                    SECTION 3: SEARCHING EMAIL
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 11: SEARCH FOR EMAILS BY KEYWORD
#
# Learn: ezgmail.search()
#
# Tasks:
# 1. Search for emails containing a specific word
# 2. Print the number of matching threads
# 3. Display a summary of search results
# 4. Access messages in the search results
# 5. Try different search terms
# ----------------------------------------------------------------------

print("-------------------------------------------------")

free_threads = ezgmail.search("free")
print(len(free_threads))
print(ezgmail.summary(free_threads))

for thread in free_threads:
    for my_message in thread.messages:
        print(my_message.subject, my_message.timestamp)

# ----------------------------------------------------------------------
# 🟡 12: USE SEARCH OPERATORS
#
# Learn: Gmail search operators
#
# Tasks:
# 1. Search for unread emails: 'label:UNREAD'
# 2. Search by sender: 'from:someone@example.com'
# 3. Search by subject: 'subject:hello'
# 4. Search for emails with attachments: 'has:attachment'
# 5. Combine operators: 'from:someone@example.com subject:meeting'
# ----------------------------------------------------------------------

unread_threads = ezgmail.search("label:UNREAD")
print(len(unread_threads))

google_threads = ezgmail.search("from:no-reply@google.com")
print(len(google_threads))

topic_thread = ezgmail.search("subject:Hello from hell")
print(len(topic_thread))

with_attch = ezgmail.search("has:attachment")
print(len(with_attch))

mixed_operators = ezgmail.search("label:UNREAD subject:Say less")
print(len(mixed_operators))

# ----------------------------------------------------------------------
# 🟡 13: SEARCH BY DATE
#
# Learn: Date-based search operators
#
# Tasks:
# 1. Search for emails after a date: 'after:2024/01/01'
# 2. Search for emails before a date: 'before:2024/12/31'
# 3. Search for emails within a date range
# 4. Search for emails from the last week
# 5. Combine date operators with other criteria
# ----------------------------------------------------------------------

after = ezgmail.search("after:2024/01/01")
print(len(after))

before = ezgmail.search("before:2024/12/31")
print(len(before))

before_after = ezgmail.search("before:2026/12/31 after:2026/05/01")
print(len(before_after))

last_week = ezgmail.search("newer_than:7d")
print(len(last_week))

# ----------------------------------------------------------------------
# 🟡 14: DOWNLOAD ATTACHMENTS
#
# Learn: attachments, downloadAttachment(), downloadAllAttachments()
#
# Tasks:
# 1. Search for emails with attachments
# 2. Access the attachments attribute of a message
# 3. Print the list of attachment filenames
# 4. Download a single attachment with downloadAttachment()
# 5. Download all attachments with downloadAllAttachments()
# 6. Use downloadFolder parameter to specify destination
# ----------------------------------------------------------------------

with_attch = ezgmail.search("has:attachment")
for thread in with_attch:
    for my_message in thread.messages:
        if my_message.attachments:
            print(my_message.attachments)
            my_message.downloadAllAttachments("/Users/daniel_molina/Downloads/test")

# =====================================================================
#                    SECTION 4: SMS EMAIL GATEWAYS
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 15: UNDERSTAND SMS GATEWAYS
#
# Learn: SMS email gateway concept
#
# Tasks:
# 1. Review the SMS gateway table for different carriers
# 2. Understand the format: phonenumber@gateway.com
# 3. Create the email address for a Verizon number: 2125551234@vtext.com
# 4. Create addresses for AT&T, T-Mobile numbers
# 5. Understand SMS (160 char limit) vs MMS (no limit) gateways
# ----------------------------------------------------------------------

# verizon = "0123456789@vtext.com"
# att = "0123456789@txt.att.net"
# tmobile = "0123456789@tmomail.net"

# ezgmail.send(verizon, "NoSubject", body="This is your body")
# ezgmail.send(att, "NoSubject", body="This is your body")
# ezgmail.send(tmobile, "NoSubject", body="This is your body")

# ----------------------------------------------------------------------
# 🟡 16: SEND A TEXT MESSAGE VIA EMAIL
#
# Learn: Using ezgmail.send() for SMS
#
# Tasks:
# 1. Format a phone number as an SMS gateway email
# 2. Create a short message (under 160 characters)
# 3. Send using ezgmail.send() (subject becomes part of body)
# 4. Note: This may not be reliable and could be blocked
# 5. Consider limitations: no delivery confirmation, may be blocked
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 17: CREATE AN SMS SENDING FUNCTION
#
# Learn: Building a reusable SMS function
#
# Tasks:
# 1. Create a dictionary of carrier names to gateway domains
# 2. Create function: send_sms(phone_number, carrier, message)
# 3. Format the phone number (remove dashes, spaces)
# 4. Build the gateway email address
# 5. Send the message using ezgmail
# 6. Handle unknown carriers gracefully
# ----------------------------------------------------------------------

carriers = {
    "verizon": {
        "@vtext.com": [
            "cellhpone1",
            "cellhpone2",
            "cellhpone3",
        ]
    },
    "AT&T": {
        "@txt.att.net": [
            "cellhpone1",
            "cellhpone2",
            "cellhpone3",
        ]
    },
    "T-Mobile": {
        "@tmomail.net": [
            "cellhpone1",
            "cellhpone2",
            "cellhpone3",
        ]
    },
}

for operator, domain in carriers.items():
    for phones in domain.values():
        for phone in phones:
            my_domain = list(domain.keys())
            # print(f"{phone}{my_domain[0]}", "NoSubject", "NoBody")
            # ezgmail.send(f"{phone}{my_domain[0]}", "NoSubject", "NoBody")


# =====================================================================
#                    SECTION 5: PUSH NOTIFICATIONS WITH NTFY
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 18: SEND A SIMPLE NOTIFICATION
#
# Learn: requests.post() to ntfy.sh
#
# Tasks:
# 1. Import the requests module
# 2. Choose a secret topic name (e.g., 'YourNameRandomLetters123')
# 3. Send a notification with requests.post()
# 4. Check for <Response [200]> success
# 5. View the message at https://ntfy.sh/YourTopic
# ----------------------------------------------------------------------

import requests

notification = requests.post("https://ntfy.sh/python_learning", "I did it")
print(notification.status_code)

# ----------------------------------------------------------------------
# 🟢 19: SUBSCRIBE AND RECEIVE NOTIFICATIONS
#
# Learn: Installing ntfy app, subscribing to topics
#
# Tasks:
# 1. Install the ntfy app on your phone (or use web app)
# 2. Subscribe to your secret topic
# 3. Send a notification from Python
# 4. Verify you receive it on your phone
# 5. Understand why topics should be kept secret
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 20: ADD TITLE TO NOTIFICATIONS
#
# Learn: Title header
#
# Tasks:
# 1. Create a headers dictionary with 'Title' key
# 2. Send a notification with a title
# 3. Observe how the title appears above the message
# 4. Send multiple notifications with different titles
# 5. Use titles to categorize your notifications
# ----------------------------------------------------------------------

import time

headers = {
    "Title": "Title1",
    "Priority": "5",
    "Tags": "no_entry,no_entry,no_entry,squid",
}

titles = [title for title in headers.values()]

# for _ in range(3):
#     requests.post(
#         "https://ntfy.sh/python_learning",
#         "I did it once again",
#         headers=headers,
#     )
#     time.sleep(2)

# ----------------------------------------------------------------------
# 🟡 21: SET NOTIFICATION PRIORITY
#
# Learn: Priority header (1-5)
#
# Tasks:
# 1. Send a notification with Priority: '1' (minimum)
# 2. Send a notification with Priority: '5' (urgent)
# 3. Send with default priority (3)
# 4. Observe how priority affects display in the app
# 5. Understand that priority is for filtering, not delivery speed
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 22: ADD TAGS AND EMOJIS
#
# Learn: Tags header
#
# Tasks:
# 1. Send a notification with a single tag
# 2. Send with multiple tags (comma-separated)
# 3. Use emoji names as tags: 'warning', 'white_check_mark', 'rocket'
# 4. Observe emoji appearing next to the title
# 5. Find more emoji names at https://docs.ntfy.sh/publish/#tags-emojis
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 23: COMBINE ALL METADATA
#
# Learn: Using multiple headers together
#
# Tasks:
# 1. Create a headers dictionary with Title, Priority, and Tags
# 2. Send a fully formatted notification
# 3. Create a function: send_notification(topic, message, title, priority, tags)
# 4. Test the function with various parameters
# 5. Make parameters optional with default values
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 6: RECEIVING NOTIFICATIONS IN PYTHON
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 24: POLL FOR NOTIFICATIONS
#
# Learn: requests.get() with /json?poll=1
#
# Tasks:
# 1. First send a few test notifications to your topic
# 2. Use requests.get() with URL ending in /json?poll=1
# 3. Print resp.text to see the raw response
# 4. Notice each notification is a JSON object on its own line
# 5. Understand this retrieves all cached messages
# ----------------------------------------------------------------------

print("--------------------------------")

resp: requests.Response = requests.get("https://ntfy.sh/python_learning/json?poll=1")
print(resp.text)

# ----------------------------------------------------------------------
# 🟡 25: PARSE NOTIFICATION RESPONSES
#
# Learn: Parsing multi-line JSON with splitlines()
#
# Tasks:
# 1. Get the response text from polling
# 2. Use splitlines() to separate each JSON object
# 3. Parse each line with json.loads()
# 4. Store parsed notifications in a list
# 5. Access the 'message' key from each notification
# ----------------------------------------------------------------------

from datetime import datetime

notifications = list()
for single_response in resp.text.splitlines():
    notifications.append(json.loads(single_response))

for notification in notifications:
    print(
        notification["message"],
        print(
            notification["id"],
            datetime.fromtimestamp(notification["time"]),
            notification.get("title", "No title"),
            notification.get("Priority", "No priorities"),
            notification.get("Tags", "No tags"),
        ),
    )

# ----------------------------------------------------------------------
# 🟡 26: ACCESS NOTIFICATION PROPERTIES
#
# Learn: Notification JSON structure
#
# Tasks:
# 1. Parse a notification response
# 2. Access the 'id' field (unique identifier)
# 3. Access the 'time' field (Unix timestamp)
# 4. Access 'title', 'priority', and 'tags' if present
# 5. Convert the timestamp to readable datetime
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 27: FILTER NOTIFICATIONS BY TIME
#
# Learn: since parameter
#
# Tasks:
# 1. Poll with since=10m (last 10 minutes)
# 2. Poll with since=1h (last hour)
# 3. Poll with a Unix timestamp
# 4. Poll with a message ID (all messages after that ID)
# 5. Combine poll=1 and since with & in URL
# ----------------------------------------------------------------------

print("---------------------------------------")

resp = requests.get("https://ntfy.sh/python_learning?poll=1?since=10m")
print(resp.text)


resp = requests.get("https://ntfy.sh/python_learning?poll=1?since=1h")
print(resp.text)

# ----------------------------------------------------------------------
# 🟡 28: FILTER BY EVENT TYPE
#
# Learn: 'event' field in notifications
#
# Tasks:
# 1. Poll for notifications
# 2. Check the 'event' field of each notification
# 3. Filter to only process 'message' events
# 4. Ignore 'open', 'keepalive', 'poll_request' events
# 5. Create a function that returns only message notifications
# ----------------------------------------------------------------------

my_list = list()

print("----------------------------")
resp = requests.get("https://ntfy.sh/python_learning/json?poll=1")
print(resp.text)

for json_text in resp.text.splitlines():
    if json.loads(json_text).get("event") == "message":
        my_list.append(json.loads(json_text))

print("---------------------------------")
for x in my_list:
    print(x["message"])  # type: ignore

# =====================================================================
#                    SECTION 7: PRACTICAL APPLICATIONS
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 29: CREATE A NOTIFICATION HELPER MODULE
#
# Learn: Building reusable code
#
# Tasks:
# 1. Create functions for sending notifications with various options
# 2. Create function for receiving/parsing notifications
# 3. Include your secret topic as a configurable constant
# 4. Add docstrings to explain each function
# 5. Handle errors (network issues, invalid responses)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 30: PROGRAM COMPLETION NOTIFIER
#
# Learn: Notifying yourself when a task finishes
#
# Tasks:
# 1. Create a function that simulates a long-running task
# 2. Send a notification when the task starts
# 3. Send a notification when the task completes
# 4. Include the elapsed time in the completion message
# 5. Send an error notification if the task fails
# ----------------------------------------------------------------------

import time


def my_wait():
    time.sleep(5)
    # time.sleep(a)


requests.post("https://ntfy.sh/python_learning", f"{my_wait.__name__} has begun")

try:
    start = time.time()
    finish = time.time()
    total_time = finish - start
    requests.post(
        "https://ntfy.sh/python_learning",
        f"{my_wait.__name__} has finished, it took {total_time}s to complete",
    )
except Exception as e:
    requests.post(
        "https://ntfy.sh/python_learning",
        f"The was an error, {e}",
    )


# ----------------------------------------------------------------------
# 🟡 31: EMAIL SUMMARY NOTIFIER
#
# Learn: Combining EZGmail and ntfy
#
# Tasks:
# 1. Check for unread emails using ezgmail
# 2. If there are unread emails, send a push notification
# 3. Include the count and subjects in the notification
# 4. Run this check periodically
# 5. Only notify if there are NEW unread emails since last check
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 8: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 32: BULK EMAIL SENDER
#
# Scenario: Send personalized emails to a list of contacts
#
# Tasks:
# 1. Create a CSV file with: Name, Email, CustomField
# 2. Read the CSV file
# 3. Create an email template with placeholders
# 4. For each contact, fill in the template
# 5. Send the personalized email
# 6. Log sent emails and handle failures
# 7. Add a delay between sends to avoid spam filters
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 33: EMAIL AUTO-RESPONDER
#
# Scenario: Automatically reply to emails matching criteria
#
# Tasks:
# 1. Search for unread emails with specific criteria
# 2. For each matching email, compose a reply
# 3. Send the auto-reply
# 4. Mark the original as read (or use a label to track)
# 5. Log all auto-replies sent
# 6. Run periodically to check for new emails
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 34: ATTACHMENT ORGANIZER
#
# Scenario: Download and organize email attachments
#
# Tasks:
# 1. Search for emails with attachments
# 2. Download all attachments
# 3. Organize into folders by sender or date
# 4. Rename files to include sender and date
# 5. Skip already-downloaded attachments
# 6. Generate a report of downloaded files
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 35: NOTIFICATION-BASED REMOTE CONTROL
#
# Scenario: Control a Python script via notifications
#
# Tasks:
# 1. Define command notifications (e.g., "STATUS", "STOP", "REPORT")
# 2. Poll for notifications periodically
# 3. Parse incoming messages for commands
# 4. Execute the appropriate action for each command
# 5. Send a response notification with results
# 6. Implement authentication (check for secret keyword)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 36: SYSTEM MONITOR WITH ALERTS
#
# Scenario: Monitor system and send alerts
#
# Tasks:
# 1. Create functions to check system metrics (disk space, etc.)
# 2. Define alert thresholds
# 3. Check metrics periodically
# 4. Send push notification if threshold exceeded
# 5. Use priority levels based on severity
# 6. Include relevant emojis (warning, error symbols)
# 7. Avoid sending duplicate alerts for the same issue
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 37: DAILY EMAIL DIGEST
#
# Scenario: Send yourself a daily summary email
#
# Tasks:
# 1. Collect data throughout the day (logs, metrics, etc.)
# 2. At a scheduled time, compile the data
# 3. Format it into a nice HTML or plain text email
# 4. Send the digest email to yourself
# 5. Clear the collected data for the next day
# 6. Include charts or summaries of key metrics
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 38: TWO-WAY NOTIFICATION CHAT
#
# Scenario: Simple chat between two Python scripts
#
# Tasks:
# 1. Create a "sender" script that posts to a topic
# 2. Create a "receiver" script that polls the topic
# 3. Add message IDs to track which messages are new
# 4. Display received messages in real-time
# 5. Allow both scripts to send AND receive (bidirectional)
# 6. Handle message ordering and duplicates
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 39: EMAIL-TRIGGERED AUTOMATION
#
# Scenario: Trigger actions based on incoming emails
#
# Tasks:
# 1. Define email patterns that trigger actions
#    (e.g., subject contains "URGENT")
# 2. Periodically check for matching emails
# 3. When found, execute the corresponding action
# 4. Send a confirmation email or notification
# 5. Mark processed emails to avoid reprocessing
# 6. Log all triggered actions
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 40: NOTIFICATION QUEUE SYSTEM
#
# Scenario: Build a task queue using ntfy
#
# Tasks:
# 1. Create a "producer" that sends task notifications
# 2. Include task data in JSON format in the message
# 3. Create a "worker" that polls for tasks
# 4. Parse and execute each task
# 5. Send completion notification with results
# 6. Handle failed tasks (retry or report)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 41: MAILING LIST MANAGER
#
# Scenario: Manage and send to a mailing list
#
# Tasks:
# 1. Store subscriber emails in a JSON file
# 2. Create function to add/remove subscribers
# 3. Create function to send email to all subscribers
# 4. Handle bounced emails (track failures)
# 5. Add unsubscribe link/instructions in emails
# 6. Create an admin notification for new subscribers
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 42: SCHEDULED NOTIFICATION SYSTEM
#
# Scenario: Schedule notifications for future delivery
#
# Tasks:
# 1. Create a JSON file to store scheduled notifications
# 2. Each entry has: time, topic, message, metadata
# 3. Create function to schedule a new notification
# 4. Create a checker that runs periodically
# 5. Send notifications whose time has arrived
# 6. Remove sent notifications from the schedule
# 7. Handle notifications that were missed (past due)
# ----------------------------------------------------------------------


# ======================================================================
# 📧 QUICK REFERENCE - EZGmail Setup
# ======================================================================
#
# Installation:
#   pip install ezgmail
#
# Setup Steps:
#   1. Create Gmail account at https://gmail.com
#   2. Go to https://console.cloud.google.com
#   3. Create a new project
#   4. Enable Gmail API
#   5. Configure OAuth consent screen
#   6. Add scope: https://mail.google.com
#   7. Create OAuth credentials
#   8. Download credentials.json
#   9. Run ezgmail.init() (opens browser for auth)
#   10. token.json is created automatically
#
# Security:
#   - Keep token.json secure (like a password)
#   - Use a separate email account for scripts
#   - Test with print() before actual sending
#
# ======================================================================


# ======================================================================
# 📧 QUICK REFERENCE - EZGmail Sending
# ======================================================================
#
# Import:
#   import ezgmail
#   ezgmail.init()
#
# Simple send:
#   ezgmail.send('to@example.com', 'Subject', 'Body text')
#
# With attachments:
#   ezgmail.send('to@example.com', 'Subject', 'Body',
#                ['file1.txt', 'file2.jpg'])
#
# With CC and BCC:
#   ezgmail.send('to@example.com', 'Subject', 'Body',
#                cc='cc@example.com',
#                bcc='bcc1@example.com,bcc2@example.com')
#
# Check configured email:
#   print(ezgmail.EMAIL_ADDRESS)
#
# ======================================================================


# ======================================================================
# 📧 QUICK REFERENCE - EZGmail Reading
# ======================================================================
#
# Get unread threads:
#   threads = ezgmail.unread()
#   threads = ezgmail.unread(maxResults=50)
#
# Get recent threads:
#   threads = ezgmail.recent()
#   threads = ezgmail.recent(maxResults=100)
#
# Display summary:
#   ezgmail.summary(threads)
#
# Access thread:
#   thread = threads[0]
#   messages = thread.messages    # List of GmailMessage
#
# Access message properties:
#   msg = thread.messages[0]
#   msg.subject                   # Email subject
#   msg.body                      # Email body text
#   msg.sender                    # Sender email
#   msg.recipient                 # Recipient email
#   msg.timestamp                 # datetime object
#
# ======================================================================


# ======================================================================
# 📧 QUICK REFERENCE - EZGmail Searching
# ======================================================================
#
# Basic search:
#   results = ezgmail.search('keyword')
#
# Search operators:
#   'label:UNREAD'                      # Unread emails
#   'from:someone@example.com'          # From specific sender
#   'to:someone@example.com'            # To specific recipient
#   'subject:hello'                     # Subject contains
#   'has:attachment'                    # Has attachments
#   'after:2024/01/01'                  # After date
#   'before:2024/12/31'                 # Before date
#   'is:starred'                        # Starred emails
#
# Combine operators:
#   'from:boss@work.com subject:urgent has:attachment'
#
# Download attachments:
#   msg.attachments                     # List of filenames
#   msg.downloadAttachment('file.pdf')
#   msg.downloadAllAttachments(downloadFolder='downloads')
#
# ======================================================================


# ======================================================================
# 📧 QUICK REFERENCE - SMS Email Gateways
# ======================================================================
#
# Format: phonenumber@gateway (no dashes in number)
#
# Common Gateways (SMS):
#   AT&T:           number@txt.att.net
#   T-Mobile:       number@tmomail.net
#   Verizon:        number@vtext.com
#   Sprint:         number@messaging.sprintpcs.com
#   Google Fi:      number@msg.fi.google.com
#
# Common Gateways (MMS - for images/longer texts):
#   AT&T:           number@mms.att.net
#   Verizon:        number@vzwpix.com
#   T-Mobile:       number@tmomail.net (same as SMS)
#
# Example:
#   ezgmail.send('2125551234@vtext.com', '', 'Hello via SMS!')
#
# Limitations:
#   - No delivery confirmation
#   - May be blocked as spam
#   - Recipient cannot reply
#   - Not reliable for urgent messages
#
# ======================================================================


# ======================================================================
# 📧 QUICK REFERENCE - ntfy Push Notifications
# ======================================================================
#
# Send notification:
#   import requests
#   requests.post('https://ntfy.sh/YOUR_TOPIC', 'Message text')
#
# Send with metadata:
#   requests.post('https://ntfy.sh/YOUR_TOPIC', 'Message',
#       headers={
#           'Title': 'Notification Title',
#           'Priority': '5',          # 1-5 (5=urgent)
#           'Tags': 'warning,skull'   # emoji names
#       })
#
# Receive notifications (polling):
#   resp = requests.get('https://ntfy.sh/YOUR_TOPIC/json?poll=1')
#
# Filter by time:
#   ?poll=1&since=10m                 # Last 10 minutes
#   ?poll=1&since=1h                  # Last hour
#   ?poll=1&since=1737866912          # Since Unix timestamp
#
# Parse response:
#   for line in resp.text.splitlines():
#       notification = json.loads(line)
#       print(notification['message'])
#
# ======================================================================


# ======================================================================
# 📧 QUICK REFERENCE - ntfy Notification Structure
# ======================================================================
#
# Notification JSON fields:
#   'id'          Unique identifier string
#   'time'        Unix epoch timestamp (when created)
#   'expires'     Unix epoch timestamp (when deleted)
#   'event'       'message', 'open', 'keepalive', 'poll_request'
#   'topic'       Topic name
#   'message'     Message text
#   'title'       Title (if set)
#   'priority'    1-5 (if set)
#   'tags'        List of tag strings (if set)
#
# Convert timestamp to datetime:
#   import datetime
#   dt = datetime.datetime.fromtimestamp(notification['time'])
#
# Filter message events:
#   if notification['event'] == 'message':
#       process(notification)
#
# ======================================================================


# ======================================================================
# 📧 QUICK REFERENCE - Common Emoji Tags for ntfy
# ======================================================================
#
# Status:
#   'white_check_mark'    ✅  Success
#   'x'                   ❌  Failure
#   'warning'             ⚠️  Warning
#   'rotating_light'      🚨  Alert
#
# Actions:
#   'rocket'              🚀  Launch/Start
#   'stop_sign'           🛑  Stop
#   'hourglass'           ⏳  Waiting
#   'tada'                🎉  Celebration
#
# Objects:
#   'email'               📧  Email related
#   'computer'            💻  Computer related
#   'file_folder'         📁  File related
#   'calendar'            📅  Schedule related
#
# Full list: https://docs.ntfy.sh/publish/#tags-emojis
#
# ======================================================================


# ======================================================================
# 🚀 SETUP INSTRUCTIONS
# ======================================================================
#
# EZGmail Setup:
#   1. pip install ezgmail
#   2. Set up Google Cloud project and Gmail API
#   3. Download credentials.json to working directory
#   4. Run: import ezgmail; ezgmail.init()
#   5. Complete browser authentication
#   6. token.json will be created
#
# ntfy Setup:
#   1. pip install requests (if not already installed)
#   2. Install ntfy app on phone (Android/iOS)
#   3. Or use web app: https://ntfy.sh/app
#   4. Choose a secret topic name (like a password)
#   5. Subscribe to your topic in the app
#   6. No account registration required!
#
# Testing Tips:
#   - Use a separate email account for testing
#   - Use print() to verify before actual sending
#   - Add delays between sends to avoid spam filters
#   - Keep topic names secret for ntfy
#   - Check ntfy web interface to verify messages
#
# Limits:
#   - ntfy: 250 messages/day (free), 4096 bytes/message
#   - Gmail: Has sending limits, blocks spam-like patterns
#   - SMS gateways: Unreliable, may block frequent sends
#
# ======================================================================
# ======================================================================
