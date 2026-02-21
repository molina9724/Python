# ======================================================================
# 🐍 REAL-WORLD LOOP EXERCISES - BEYOND THE BASICS
# ======================================================================
# No boring stuff. Actual scenarios you'll encounter.
# ======================================================================


# =====================================================================
#                    SECTION 1: EASY
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 1: Playlist Shuffle Pairs
# You're building a music app. Users want to see "Up Next" which shows
# the current song and the next song together.
#
# Given a playlist, yield pairs of (current_song, next_song)
# The last song pairs with the first (it loops)
#
# Input: ["Song A", "Song B", "Song C", "Song D"]
# Output: [("Song A", "Song B"), ("Song B", "Song C"),
#          ("Song C", "Song D"), ("Song D", "Song A")]
# ----------------------------------------------------------------------

import random
from datetime import datetime, timedelta
playlist = [
    "Bohemian Rhapsody",
    "Hotel California",
    "Stairway to Heaven",
    "Sweet Child O Mine",
]

# Write your code below:


# Test your solution:
# print("🟢 Pairs:")
# for pair in pairs:
#     print(f"  Now: {pair[0]} → Next: {pair[1]}")
# Expected:
# ('Bohemian Rhapsody', 'Hotel California')
# ('Hotel California', 'Stairway to Heaven')
# ('Stairway to Heaven', 'Sweet Child O Mine')
# ('Sweet Child O Mine', 'Bohemian Rhapsody')


# ----------------------------------------------------------------------
# 🟢 EASY 2: Price Comparison - Find Deals
# You scraped prices from 3 stores for the same products.
# Find which store has the cheapest price for each item.
#
# Data structure: {product: [store1_price, store2_price, store3_price]}
# Store names: ["Amazon", "Walmart", "Target"]
# ----------------------------------------------------------------------

prices = {
    "iPhone 15": [999, 979, 989],
    "AirPods Pro": [249, 239, 259],
    "MacBook Air": [1099, 1149, 1079],
    "iPad": [449, 429, 449],
}
stores = ["Amazon", "Walmart", "Target"]

# Write your code below:


# Test your solution:
# Expected:
# "iPhone 15: Best price $979 at Walmart (save $20 vs worst)"
# "AirPods Pro: Best price $239 at Walmart (save $20 vs worst)"
# "MacBook Air: Best price $1079 at Target (save $70 vs worst)"
# "iPad: Best price $429 at Walmart (save $20 vs worst)"


# ----------------------------------------------------------------------
# 🟢 EASY 3: Chat Log - Group Consecutive Messages
# In a chat app, consecutive messages from the same person should be
# grouped together (like WhatsApp/iMessage does)
#
# Input: List of (sender, message) tuples
# Output: Grouped messages
# ----------------------------------------------------------------------

chat_log = [
    ("Alice", "Hey!"),
    ("Alice", "You there?"),
    ("Alice", "Hello???"),
    ("Bob", "Sorry, was in a meeting"),
    ("Bob", "What's up?"),
    ("Alice", "Want to grab lunch?"),
    ("Bob", "Sure!"),
    ("Bob", "Where?"),
    ("Bob", "I'm thinking tacos"),
]

# Write your code below:


# Test your solution:
# Expected:
# Alice:
#   - Hey!
#   - You there?
#   - Hello???
# Bob:
#   - Sorry, was in a meeting
#   - What's up?
# Alice:
#   - Want to grab lunch?
# Bob:
#   - Sure!
#   - Where?
#   - I'm thinking tacos


# =====================================================================
#                    SECTION 2: MEDIUM
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 MEDIUM 4: Stock Price Analysis - Find Best Buy/Sell Days
# Given daily stock prices, find the best day to buy and sell
# to maximize profit. You must buy BEFORE you sell.
#
# This is a real interview question at FAANG companies.
#
# Hint: You need to track minimum price seen so far while iterating
# ----------------------------------------------------------------------

stock_prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# Days:          0    1    2    3    4    5    6    7    8    9

# Write your code below:


# Test your solution:
# Expected: Find the buy day, sell day, and max profit
# print("🟡 Buy on day X at $Y, sell on day A at $B")
# print("🟡 Profit: $Z")


# ----------------------------------------------------------------------
# 🟡 MEDIUM 5: Log File Analysis - Find Error Bursts
# Server logs: Find periods where errors happened in quick succession
# (3+ errors within 5 seconds = "error burst")
#
# Real scenario: Alert system for server monitoring
# ----------------------------------------------------------------------

# Timestamps in seconds since midnight when errors occurred
error_timestamps = [
    3600,  # 1:00:00 AM
    3601,  # 1:00:01 AM
    3602,  # 1:00:02 AM  <- burst 1 (3 errors in 2 sec)
    7200,  # 2:00:00 AM  (isolated error)
    9000,  # 2:30:00 AM
    9001,  # 2:30:01 AM
    9002,  # 2:30:02 AM
    9003,  # 2:30:03 AM  <- burst 2 (4 errors in 3 sec)
    14400,  # 4:00:00 AM  (isolated error)
]

# Write your code below:


# Test your solution:
# Expected:
# print("🟡 Burst at 1:00:00 AM - 3 errors in 2 seconds")
# print("🟡 Burst at 2:30:00 AM - 4 errors in 3 seconds")


# ----------------------------------------------------------------------
# 🟡 MEDIUM 6: Pagination - Process Data in Chunks
# You're fetching data from an API that returns 1000 users
# But you can only process 100 at a time (memory limits)
#
# Simulate batch processing with progress reporting
# ----------------------------------------------------------------------

# Simulated user IDs (imagine this came from a database)
all_user_ids = list(range(1, 1001))  # Users 1-1000
BATCH_SIZE = 100

# Write your code below:
# 1. Process in batches of 100
# 2. Print progress for each batch


# Test your solution:
# Expected:
# print("🟡 Processing batch 1: users 1-100 (10% complete)")
# print("🟡 Processing batch 2: users 101-200 (20% complete)")
# ... etc


# ----------------------------------------------------------------------
# 🟡 MEDIUM 7: Meeting Scheduler - Find Free Slots
# Given everyone's busy times, find when everyone is FREE
#
# Real scenario: Google Calendar's "Find a time" feature
# ----------------------------------------------------------------------

# Times are in 24h format (9 = 9:00 AM, 14 = 2:00 PM)
# Each person has list of (start, end) busy blocks

schedules = {
    "Alice": [(9, 10), (12, 13), (14, 16)],
    "Bob": [(10, 11), (12, 14), (16, 17)],
    "Charlie": [(9, 11), (13, 14), (15, 16)],
}

# Working hours: 9 AM to 6 PM (9-18)
# Find all 1-hour slots where everyone is free

# Write your code below:


# Test your solution:
# Expected:
# print("🟡 Free slots: 11:00, 17:00")


# ----------------------------------------------------------------------
# 🟡 MEDIUM 8: Text Wrapping - Word Wrap Algorithm
# Implement word wrap like text editors do
# Given text and max width, break into lines without cutting words
#
# Real scenario: Every text editor, terminal, messaging app
# ----------------------------------------------------------------------

text = "The quick brown fox jumps over the lazy dog. Pack my box with five dozen liquor jugs."
max_width = 30

# Write your code below:


# Test your solution:
# Expected:
# print("🟡 Wrapped text:")
# "The quick brown fox jumps"
# "over the lazy dog. Pack my"
# "box with five dozen liquor"
# "jugs."


# =====================================================================
#                    SECTION 3: HARD
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 HARD 9: Sliding Window - Network Traffic Analysis
# Calculate moving average of network requests per second
# Window size: 5 seconds
#
# Real scenario: DDoS detection, performance monitoring
# ----------------------------------------------------------------------

# Requests per second for 20 seconds
requests_per_second = [
    45,
    52,
    48,
    150,
    200,
    180,
    160,
    55,
    50,
    48,
    52,
    49,
    51,
    300,
    350,
    400,
    380,
    60,
    55,
    50,
]

# Write your code below:
# Calculate 5-second moving average
# Flag if average exceeds 150 (potential attack)


# Test your solution:
# Expected:
# print("🔴 Second 5: avg=119.0 - Normal")
# print("🔴 Second 6: avg=126.0 - Normal")
# ...
# print("🔴 Second 15: avg=160.4 - ⚠️ ALERT: High traffic!")


# ----------------------------------------------------------------------
# 🔴 HARD 10: Undo/Redo Stack - Text Editor Operations
# Implement undo/redo by iterating through history
# Backwards iteration for undo, forward for redo
#
# Real scenario: Every application with undo functionality
# ----------------------------------------------------------------------

# Action history: (action_type, data)
history = [
    ("insert", "Hello"),
    ("insert", " "),
    ("insert", "World"),
    ("delete", "World"),
    ("insert", "Python"),
    ("format", "bold"),
]

current_position = len(history)  # At the end (all actions applied)

# Write your code below:
# Implement:
# undo(n) - go back n steps, return the actions being undone
# redo(n) - go forward n steps, return the actions being redone
# get_current_state_description() - describe what's currently applied


# Test your solution:
# print("🔴 Current state:", get_current_state_description())
# print("🔴 Undo 2:", undo(2))
# print("🔴 State after undo:", get_current_state_description())
# print("🔴 Redo 1:", redo(1))


# ----------------------------------------------------------------------
# 🔴 HARD 11: Leaderboard - Ranking with Ties
# Gaming leaderboard: Handle ties properly
# Same score = same rank, next rank skips appropriately
#
# Real scenario: Any competitive platform (games, Kaggle, etc.)
# ----------------------------------------------------------------------

scores = [
    ("Alice", 2500),
    ("Bob", 2500),
    ("Charlie", 2400),
    ("Diana", 2400),
    ("Eve", 2400),
    ("Frank", 2200),
]

# Write your code below:


# Test your solution:
# Expected:
# print("🔴 Rank 1: Alice - 2500 pts")
# print("🔴 Rank 1: Bob - 2500 pts")
# print("🔴 Rank 3: Charlie - 2400 pts")   (rank 3, not 2!)
# print("🔴 Rank 3: Diana - 2400 pts")
# print("🔴 Rank 3: Eve - 2400 pts")
# print("🔴 Rank 6: Frank - 2200 pts")     (rank 6, not 4!)


# ----------------------------------------------------------------------
# 🔴 HARD 12: Dependency Resolution - Install Order
# Package manager: Install packages in correct order
# Must install dependencies before the package that needs them
#
# Real scenario: npm, pip, apt - package managers
# ----------------------------------------------------------------------

# package: [list of dependencies]
packages = {
    "web-app": ["react", "axios", "lodash"],
    "react": ["babel"],
    "axios": [],
    "lodash": [],
    "babel": ["core-js"],
    "core-js": [],
    "testing-lib": ["jest", "react"],
    "jest": [],
}

# User wants to install "web-app" and "testing-lib"
to_install = ["web-app", "testing-lib"]

# Write your code below:


# Test your solution:
# Expected install order:
# print("🔴 1. core-js (no deps)")
# print("🔴 2. babel (needs core-js ✓)")
# print("🔴 3. react (needs babel ✓)")
# print("🔴 4. axios (no deps)")
# print("🔴 5. lodash (no deps)")
# print("🔴 6. web-app (needs react ✓, axios ✓, lodash ✓)")
# print("🔴 7. jest (no deps)")
# print("🔴 8. testing-lib (needs jest ✓, react ✓)")


# ----------------------------------------------------------------------
# 🔴 HARD 13: A/B Test Analysis - Statistical Comparison
# Compare two versions of a website
# Iterate through paired data to calculate improvement
#
# Real scenario: Every tech company runs A/B tests
# ----------------------------------------------------------------------

# Daily conversion rates (%) for version A and B over 2 weeks
version_a = [2.1, 2.3, 2.0, 2.2, 2.4, 2.1,
             2.3, 2.2, 2.0, 2.1, 2.3, 2.2, 2.1, 2.2]
version_b = [2.4, 2.5, 2.3, 2.6, 2.4, 2.5,
             2.7, 2.4, 2.3, 2.5, 2.6, 2.4, 2.5, 2.6]

# Write your code below:
# Calculate:
# 1. Days where B beat A (and by how much)
# 2. Average improvement of B over A
# 3. Consistency (did B win every day?)
# 4. Verdict: "Version B is better with X% average improvement"


# Test your solution:
# print("🔴 Days B won: X/14")
# print("🔴 Average improvement: X%")
# print("🔴 Verdict: Version B is better with X% average improvement")


# ----------------------------------------------------------------------
# 🔴 HARD 14: Game Matchmaking - Pair Players by Skill
# Match players of similar skill levels
# Iterate through sorted players to find best pairs
#
# Real scenario: Any multiplayer game matchmaking
# ----------------------------------------------------------------------

players = [
    {"name": "xX_Destroyer_Xx", "skill": 2100, "waiting_since": 45},
    {"name": "CasualGamer42", "skill": 1200, "waiting_since": 120},
    {"name": "ProPlayer99", "skill": 2050, "waiting_since": 30},
    {"name": "Newbie123", "skill": 800, "waiting_since": 90},
    {"name": "AverageJoe", "skill": 1500, "waiting_since": 60},
    {"name": "SilverSurfer", "skill": 1550, "waiting_since": 55},
    {"name": "BronzeBeast", "skill": 850, "waiting_since": 80},
    {"name": "GoldGamer", "skill": 1800, "waiting_since": 40},
]

# Rules:
# - Skill difference should be < 300 for fair match
# - Prioritize players waiting longer
# - If no good match, player keeps waiting

# Write your code below:


# Test your solution:
# print("🔴 Matched pairs:")
# print("🔴 Unmatched players:")


# ----------------------------------------------------------------------
# 🔴 HARD 15: Calendar Heatmap - GitHub Style
# Generate contribution data for a year
# Iterate by weeks and days to create the grid
#
# Real scenario: GitHub contribution graph
# ----------------------------------------------------------------------

# Simulated commit data: {date_string: commit_count}

# Generate sample data for past year
commits = {}
start_date = datetime.now() - timedelta(days=365)
for i in range(365):
    date = start_date + timedelta(days=i)
    date_str = date.strftime("%Y-%m-%d")
    # Random commits (more on weekdays)
    if date.weekday() < 5:  # Weekday
        commits[date_str] = random.choices(
            [0, 1, 2, 3, 5, 8], weights=[20, 30, 25, 15, 7, 3]
        )[0]
    else:  # Weekend
        commits[date_str] = random.choices(
            [0, 1, 2, 3], weights=[50, 30, 15, 5])[0]

# Write your code below:
# Create a 7-row (days) x 52-col (weeks) grid representation
# Show activity levels: ░ (0) ▒ (1-2) ▓ (3-5) █ (6+)


# Test your solution:
# Expected:
# print("🔴 Mon: ░▒░▓██▒░...")
# print("🔴 Tue: ▒▒▓░░█▒▓...")
# etc.


# =====================================================================
#                    SECTION 4: BONUS CHALLENGES
# =====================================================================


# ----------------------------------------------------------------------
# 🔥 BONUS 1: Real-Time Feed Algorithm
# Social media feed: Combine multiple factors to rank posts
#
# Scoring: engagement + recency + personal relevance
# Iterate with multiple criteria
# ----------------------------------------------------------------------

posts = [
    {
        "id": 1,
        "author": "friend",
        "likes": 150,
        "comments": 45,
        "hours_ago": 2,
        "topic": "tech",
    },
    {
        "id": 2,
        "author": "celebrity",
        "likes": 5000,
        "comments": 500,
        "hours_ago": 5,
        "topic": "music",
    },
    {
        "id": 3,
        "author": "friend",
        "likes": 20,
        "comments": 8,
        "hours_ago": 0.5,
        "topic": "food",
    },
    {
        "id": 4,
        "author": "news",
        "likes": 1000,
        "comments": 200,
        "hours_ago": 1,
        "topic": "tech",
    },
    {
        "id": 5,
        "author": "friend",
        "likes": 80,
        "comments": 25,
        "hours_ago": 8,
        "topic": "travel",
    },
    {
        "id": 6,
        "author": "acquaintance",
        "likes": 300,
        "comments": 50,
        "hours_ago": 3,
        "topic": "tech",
    },
]

user_preferences = {
    "interests": ["tech", "food"],
    "close_friends": ["friend"],
    "weight_engagement": 0.3,
    "weight_recency": 0.4,
    "weight_relevance": 0.3,
}

# Write your code below:
# Calculate score for each post and return sorted feed


# Test your solution:
# print("🔥 Sorted feed:")
# for post in sorted_feed:
#     print(f"  Post {post['id']} by {post['author']} - Score: {post['score']:.2f}")


# ----------------------------------------------------------------------
# 🔥 BONUS 2: Diff Algorithm (Simplified)
# Find differences between two text versions
# Like Git diff - show what was added/removed
#
# Real scenario: Version control, Google Docs revision history
# ----------------------------------------------------------------------

old_text = """def hello():
    print("Hello")
    return True"""

new_text = """def hello(name):
    print(f"Hello {name}")
    print("Welcome!")
    return True"""

# Write your code below:


# Test your solution:
# Expected:
# print("🔥 Diff:")
# - def hello():
# + def hello(name):
# -     print("Hello")
# +     print(f"Hello {name}")
# +     print("Welcome!")
#       return True


# ======================================================================
# 📊 EXERCISE SUMMARY
# ======================================================================
# These exercises cover REAL patterns you'll use:
#
# Loop Patterns Used:
# - Pairwise iteration (current + next)
# - Parallel iteration (zip multiple lists)
# - Sliding window (moving average)
# - Reverse iteration (undo operations)
# - Chunk/batch processing (pagination)
# - Nested loops with early exit
# - Conditional accumulation
# - Gap finding between items
#
# Real Domains:
# - Music/Media apps
# - E-commerce
# - Chat applications
# - Stock/Financial analysis
# - Server monitoring
# - Calendar/Scheduling
# - Text processing
# - Gaming (leaderboards, matchmaking)
# - Package management
# - A/B testing
# - Social media algorithms
# ======================================================================
