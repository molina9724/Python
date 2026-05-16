# ======================================================================
# ⏰ KEEPING TIME, SCHEDULING TASKS, AND LAUNCHING PROGRAMS
# ======================================================================
# Practice exercises - Write everything from scratch!
# Prerequisites: Python standard library (time, datetime, subprocess, threading)
# ======================================================================


# =====================================================================
#                    SECTION 1: THE TIME MODULE
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 1: GET THE CURRENT TIME (UNIX EPOCH)
#
# Learn: time.time()
#
# Tasks:
# 1. Import the time module
# 2. Call time.time() and store the result
# 3. Print the result (notice it's a large float)
# 4. Understand what "Unix epoch" means (seconds since Jan 1, 1970)
# 5. Call time.time() again and calculate the difference
# ----------------------------------------------------------------------

import time

start = time.time()
# time.sleep(2)
finish = time.time()

print(f"It took {finish-start} to run")

# ----------------------------------------------------------------------
# 🟢 2: PAUSE YOUR PROGRAM
#
# Learn: time.sleep()
#
# Tasks:
# 1. Print "Starting..."
# 2. Use time.sleep(3) to pause for 3 seconds
# 3. Print "Done!"
# 4. Try sleeping for 0.5 seconds (half a second)
# 5. Create a countdown from 5 to 1 with 1-second pauses
# ----------------------------------------------------------------------

# print("Starting")
# time.sleep(3)
# print("Done")
# time.sleep(0.5)
# print("Hero I go")

# for index in range(1, 6):
#     print(index)
#     time.sleep(1)

# ----------------------------------------------------------------------
# 🟢 3: MEASURE CODE EXECUTION TIME
#
# Learn: time.time() for timing, time.perf_counter()
#
# Tasks:
# 1. Record the start time using time.time()
# 2. Run some code (e.g., a loop that counts to 1,000,000)
# 3. Record the end time
# 4. Calculate and print the elapsed time
# 5. Try the same with time.perf_counter() (more precise)
# ----------------------------------------------------------------------

import datetime
from time import perf_counter

# start = time.time()
# perf_start = time.perf_counter()
# for _ in range(1000000):
#     pass
# finish = time.time()
# perf_finish = time.perf_counter()

# print(f"It took {finish-start}s to loop")
# print(f"It took {perf_finish-perf_start}s to loop")


# ----------------------------------------------------------------------
# 🟡 4: CONVERT EPOCH TO READABLE TIME
#
# Learn: time.ctime(), time.localtime(), time.gmtime()
#
# Tasks:
# 1. Get the current epoch time with time.time()
# 2. Convert it to a readable string using time.ctime()
# 3. Convert to a struct_time object using time.localtime()
# 4. Access individual components (year, month, day, hour, etc.)
# 5. Compare localtime() with gmtime() (local vs UTC)
# ----------------------------------------------------------------------


now = time.time()
readable_now = time.ctime(now)
print(readable_now)

readable_now2 = time.localtime(now)

my_datetime = datetime.datetime.fromtimestamp(now)
print(my_datetime.year)
print(my_datetime.month)
print(my_datetime.day)
print(my_datetime.hour)
print(my_datetime.second)

local = time.localtime()
gm = time.gmtime()

print(local)
print(gm)


# ----------------------------------------------------------------------
# 🟡 5: FORMAT TIME WITH STRFTIME
#
# Learn: time.strftime()
#
# Tasks:
# 1. Get the current local time as a struct_time
# 2. Format it as "YYYY-MM-DD" using strftime
# 3. Format it as "HH:MM:SS"
# 4. Format it as "Day, Month Date, Year" (e.g., "Monday, January 15, 2024")
# 5. Create your own custom format
# ----------------------------------------------------------------------

now = time.struct_time(local)

print(time.strftime("%Y-%m-%d", now))
print(time.strftime("%H:%M:%S", now))
print(time.strftime("%A, %B %d, %Y", now))

# =====================================================================
#                    SECTION 2: THE DATETIME MODULE
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 6: CREATE DATETIME OBJECTS
#
# Learn: datetime.datetime()
#
# Tasks:
# 1. Import the datetime module
# 2. Create a datetime for a specific date and time
# 3. Access year, month, day, hour, minute, second attributes
# 4. Print the datetime object
# 5. Create a datetime for your birthday
# ----------------------------------------------------------------------

import datetime

my_date = datetime.datetime(1997, 1, 24, 6, 6, 6)
print(my_date.year)
print(my_date.month)
print(my_date.day)
print(my_date.hour)
print(my_date.minute)
print(my_date.second)

print(my_date)

# ----------------------------------------------------------------------
# 🟢 7: GET CURRENT DATE AND TIME
#
# Learn: datetime.datetime.now(), datetime.datetime.today()
#
# Tasks:
# 1. Get the current datetime using datetime.now()
# 2. Print the full datetime
# 3. Print just the date part
# 4. Print just the time part
# 5. Compare now() with today() - what's the difference?
# ----------------------------------------------------------------------

now = datetime.datetime.now()
print(now)
print(now.date())
print(now.time())

today = datetime.datetime.today()
print(today)

print(type(now))
print(type(today))

# ----------------------------------------------------------------------
# 🟢 8: WORK WITH DATES ONLY
#
# Learn: datetime.date, datetime.date.today()
#
# Tasks:
# 1. Get today's date using datetime.date.today()
# 2. Create a specific date (e.g., New Year's Day 2025)
# 3. Access year, month, day attributes
# 4. Print the day of the week using weekday() (0=Monday)
# 5. Print the day name using strftime('%A')
# ----------------------------------------------------------------------

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

print(today.weekday())
print(datetime.date.strftime(today, "%A"))

# ----------------------------------------------------------------------
# 🟢 9: WORK WITH TIMES ONLY
#
# Learn: datetime.time
#
# Tasks:
# 1. Create a time object for 2:30 PM (14:30)
# 2. Create a time with hour, minute, second, microsecond
# 3. Access individual components
# 4. Compare two time objects (which is earlier?)
# 5. Format the time as "HH:MM AM/PM"
# ----------------------------------------------------------------------

my_time = datetime.time(14, 30)
full_time = datetime.time(1, 2, 3, 4)

print(my_time.hour)
print(my_time.minute)
print(my_time.second)
print(my_time.microsecond)

print(my_time >= full_time)

print(my_time.strftime("%I:%M:%S %p"))
print(full_time.strftime("%I:%M:%S %p"))

# ----------------------------------------------------------------------
# 🟡 10: FORMAT DATETIME WITH STRFTIME
#
# Learn: strftime() method on datetime objects
#
# Tasks:
# 1. Get the current datetime
# 2. Format as ISO format: "2024-01-15T14:30:00"
# 3. Format as US style: "01/15/2024 2:30 PM"
# 4. Format as European style: "15/01/2024 14:30"
# 5. Include day name and month name in your format
# ----------------------------------------------------------------------

now = datetime.datetime.now()
print(now.isoformat())
print(now.strftime("%m/%d/%y %H:%M %p"))

five_hours = datetime.timedelta(hours=10)
now = now + five_hours

print(now.strftime("%d/%m/%y %H:%M"))
print(now.strftime("%B %d(%A), %Y"))

# ----------------------------------------------------------------------
# 🟡 11: PARSE STRINGS TO DATETIME
#
# Learn: datetime.strptime()
#
# Tasks:
# 1. Create a date string: "2024-01-15"
# 2. Parse it into a datetime object using strptime()
# 3. Parse "January 15, 2024" with appropriate format
# 4. Parse "01/15/2024 2:30 PM"
# 5. Handle a parsing error with try/except
# ----------------------------------------------------------------------

string_date = "2024-01-15"
my_date = datetime.datetime.strptime(string_date, "%Y-%m-%d")
print(my_date)

string_date2 = "January 15, 2024"
my_date2 = datetime.datetime.strptime(string_date2, "%B %d, %Y")
print(my_date2)

string_date3 = "01/15/2024 2:30 PM"
my_date3 = datetime.datetime.strptime(string_date3, "%m/%d/%Y %I:%M %p")
print(my_date3)

# =====================================================================
#                    SECTION 3: TIMEDELTA AND DATE ARITHMETIC
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 12: CREATE TIMEDELTA OBJECTS
#
# Learn: datetime.timedelta()
#
# Tasks:
# 1. Create a timedelta of 7 days
# 2. Create a timedelta of 2 hours and 30 minutes
# 3. Create a timedelta of 1 week, 3 days, 4 hours
# 4. Print each timedelta
# 5. Access total_seconds() method
# ----------------------------------------------------------------------

seven_days = datetime.timedelta(days=7)
two_hours = datetime.timedelta(hours=2)
custom = datetime.timedelta(weeks=1, days=3, hours=4)

print(seven_days)
print(two_hours)
print(custom)

print(two_hours.total_seconds())

# ----------------------------------------------------------------------
# 🟢 13: ADD AND SUBTRACT TIME
#
# Learn: datetime + timedelta, datetime - timedelta
#
# Tasks:
# 1. Get today's date
# 2. Calculate the date 7 days from now
# 3. Calculate the date 30 days ago
# 4. Calculate datetime 2 hours and 30 minutes from now
# 5. Find what day of the week it will be in 100 days
# ----------------------------------------------------------------------

now = datetime.datetime.now()

seven_days = datetime.timedelta(days=7)
print(f"{now-seven_days}")

thirty_days = datetime.timedelta(days=30)
print(f"{now-thirty_days}")

custom = datetime.timedelta(hours=2, minutes=30)
print(f"{now-custom}")

hundred_days = datetime.timedelta(days=100)
print(datetime.datetime.strftime(now - hundred_days, "%A"))

# ----------------------------------------------------------------------
# 🟡 14: CALCULATE TIME DIFFERENCES
#
# Learn: datetime - datetime = timedelta
#
# Tasks:
# 1. Create two datetime objects (e.g., start and end of an event)
# 2. Subtract them to get a timedelta
# 3. Print the difference in days
# 4. Print the difference in total seconds
# 5. Calculate days until your next birthday
# ----------------------------------------------------------------------

start = datetime.datetime(1997, 1, 24)
end = datetime.datetime(2012, 12, 26)

delta = end - start
print(delta.days)
print(delta.total_seconds())

now = datetime.datetime.now()
next_birthday = datetime.datetime(2027, 1, 24)

print(next_birthday - now)

# ----------------------------------------------------------------------
# 🟡 15: COMPARE DATES AND TIMES
#
# Learn: Comparison operators with datetime
#
# Tasks:
# 1. Create two different datetime objects
# 2. Check if one is before the other (<)
# 3. Check if they're equal (==)
# 4. Check if a date is in the past or future
# 5. Sort a list of datetime objects
# ----------------------------------------------------------------------

custom1 = datetime.datetime(1800, 1, 1)
custom2 = datetime.datetime(1900, 1, 1)

print(custom1 <= custom2)
print(custom1 == custom2)

if custom1 < now:
    print("Forget it, it's the past")
elif custom1 > now:
    print("Relax, it's the future")
else:
    print("Get you ass to work right now")

dates = list()
dates.append(custom2)
dates.append(custom1)
dates.append(now)
print(dates)

print(custom1)
print(custom2)
print(now)

new_one = sorted(dates, reverse=True)
print(new_one)

# ----------------------------------------------------------------------
# 🟡 16: WORK WITH TIME ZONES (BASIC)
#
# Learn: datetime.timezone, timedelta for UTC offset
#
# Tasks:
# 1. Get the current UTC time using datetime.utcnow()
# 2. Create a timezone object with a UTC offset
# 3. Create a timezone-aware datetime
# 4. Convert between time zones
# 5. Print time with timezone information
# ----------------------------------------------------------------------

from datetime import datetime, timedelta, timezone

dt_utc = datetime.now(tz=timezone.utc)
tz_plus_2 = timezone(timedelta(hours=2))

dt_plus_2 = dt_utc.astimezone(tz_plus_2)
print(dt_utc)
print(dt_plus_2)

# =====================================================================
#                    SECTION 4: PRACTICAL TIME APPLICATIONS
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 17: BUILD A STOPWATCH
#
# Learn: Combining time functions
#
# Tasks:
# 1. Create a program that waits for Enter to start
# 2. Record the start time
# 3. Wait for Enter again to stop
# 4. Calculate and display elapsed time
# 5. Format as minutes:seconds.milliseconds
# ----------------------------------------------------------------------

# input("Press ENTER")
# start = time.time()
# input("Press ENTER to stop")
# finish = time.time()
# print(finish - start)


# ----------------------------------------------------------------------
# 🟡 18: CREATE A COUNTDOWN TIMER
#
# Learn: Loops with time.sleep()
#
# Tasks:
# 1. Ask the user for number of seconds to count down
# 2. Display the countdown (updating each second)
# 3. Use \r to overwrite the same line (optional)
# 4. Play a sound or print "TIME'S UP!" when done
# 5. Handle keyboard interrupt gracefully
# ----------------------------------------------------------------------

import subprocess

# count_down = 5

# for index in range(count_down):
#     print(count_down - index)
#     time.sleep(1)
# subprocess.run(
#     ["open", "/Users/daniel_molina/Downloads/Python/Python/Book/chapter19/alarm.wav"]
# )

# ----------------------------------------------------------------------
# 🟡 19: LOG TIMESTAMPS
#
# Learn: Creating timestamped log entries
#
# Tasks:
# 1. Create a function that returns a formatted timestamp
# 2. Create a function that logs a message with timestamp
# 3. Log several events with different messages
# 4. Save logs to a file with timestamps
# 5. Parse the log file and extract timestamps
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 20: SCHEDULE BASED ON TIME
#
# Learn: Time-based conditional execution
#
# Tasks:
# 1. Get the current hour
# 2. Print different greetings based on time of day
#    (morning, afternoon, evening, night)
# 3. Check if current time is within "business hours" (9-5)
# 4. Check if today is a weekend
# 5. Combine checks: "It's a weekday morning"
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 5: LAUNCHING PROGRAMS - SUBPROCESS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 21: RUN A SIMPLE COMMAND
#
# Learn: subprocess.run()
#
# Tasks:
# 1. Import subprocess
# 2. Run a simple command (e.g., 'echo Hello' or 'dir'/'ls')
# 3. Store the result (CompletedProcess object)
# 4. Check the return code (0 = success)
# 5. Print whether the command succeeded
# ----------------------------------------------------------------------

subprocess.run(["echo", "Hello"])
subprocess.run(["ls", "-l"])

result = subprocess.run(["echo", "Hello"])
if result.returncode == 0:
    print("You did it")

# ----------------------------------------------------------------------
# 🟢 22: CAPTURE COMMAND OUTPUT
#
# Learn: subprocess.run() with capture_output=True
#
# Tasks:
# 1. Run a command that produces output
# 2. Use capture_output=True to capture it
# 3. Access result.stdout (it's bytes by default)
# 4. Decode bytes to string using .decode()
# 5. Use text=True parameter instead of manual decoding
# ----------------------------------------------------------------------

result = subprocess.run(["ls", "-l"], capture_output=True, text=False)
# print(f"The command results are: {result.stdout}")
# print(f"The command results are: {result.stdout.decode('UTF-8')}")

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(f"The command results are: {result.stdout}")


# ----------------------------------------------------------------------
# 🟡 23: RUN COMMANDS WITH ARGUMENTS
#
# Learn: Passing arguments as a list
#
# Tasks:
# 1. Run 'echo' with multiple arguments as a list
# 2. Run a command that requires arguments (e.g., 'ping -c 1 google.com')
# 3. Understand why arguments should be a list (security)
# 4. Capture and print the output
# 5. Handle commands that might fail
# ----------------------------------------------------------------------

subprocess.run(["echo", "Hello", "\n", "\t", "world"])

# ----------------------------------------------------------------------
# 🟡 24: HANDLE COMMAND ERRORS
#
# Learn: returncode, stderr, check=True
#
# Tasks:
# 1. Run a command that will fail (e.g., 'ls nonexistentfile')
# 2. Check the returncode (non-zero = error)
# 3. Capture and print stderr
# 4. Use check=True to raise exception on error
# 5. Handle CalledProcessError with try/except
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 25: RUN PROGRAMS WITH POPEN
#
# Learn: subprocess.Popen()
#
# Tasks:
# 1. Start a long-running process with Popen
# 2. Let your Python code continue while it runs
# 3. Use poll() to check if the process is still running
# 4. Use wait() to wait for completion
# 5. Get the return code after completion
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 26: COMMUNICATE WITH PROCESSES
#
# Learn: Popen.communicate(), stdin
#
# Tasks:
# 1. Start a process that accepts input
# 2. Use communicate() to send input and get output
# 3. Set a timeout for communicate()
# 4. Handle TimeoutExpired exception
# 5. Terminate a process that's taking too long
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 27: OPEN FILES WITH DEFAULT APPLICATION
#
# Learn: Platform-specific commands
#
# Tasks:
# 1. Detect the operating system (sys.platform or os.name)
# 2. Open a file with the default application:
#    - Windows: 'start filename'
#    - macOS: 'open filename'
#    - Linux: 'xdg-open filename'
# 3. Create a cross-platform open_file() function
# 4. Open a text file, an image, or a URL
# 5. Handle the case where the file doesn't exist
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 28: OPEN WEBSITES
#
# Learn: webbrowser module (alternative to subprocess)
#
# Tasks:
# 1. Import the webbrowser module
# 2. Open a URL in the default browser
# 3. Open in a new window with new=1
# 4. Open in a new tab with new=2
# 5. Open multiple URLs in sequence
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 6: MULTITHREADING BASICS
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 29: CREATE A SIMPLE THREAD
#
# Learn: threading.Thread()
#
# Tasks:
# 1. Import threading
# 2. Create a function that prints messages with delays
# 3. Create a Thread object with target=your_function
# 4. Start the thread with .start()
# 5. Notice how the main program continues immediately
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 30: PASS ARGUMENTS TO THREADS
#
# Learn: args and kwargs parameters
#
# Tasks:
# 1. Create a function that takes parameters
# 2. Create a thread with args=(arg1, arg2)
# 3. Start the thread
# 4. Try using kwargs={'key': 'value'}
# 5. Create multiple threads with different arguments
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 31: WAIT FOR THREADS TO COMPLETE
#
# Learn: thread.join()
#
# Tasks:
# 1. Create a thread that takes several seconds
# 2. Start the thread
# 3. Use .join() to wait for it to complete
# 4. Print a message after the thread finishes
# 5. Use join with a timeout parameter
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 32: RUN MULTIPLE THREADS
#
# Learn: Managing multiple threads
#
# Tasks:
# 1. Create a function that simulates work (with sleep)
# 2. Create 5 threads, each running the function
# 3. Start all threads
# 4. Join all threads (wait for all to complete)
# 5. Measure total time vs sequential time
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 33: THREADS WITH RETURN VALUES
#
# Learn: Collecting results from threads
#
# Tasks:
# 1. Create a list to store results
# 2. Create a function that appends its result to the list
# 3. Run multiple threads
# 4. Wait for all threads to complete
# 5. Process the collected results
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 34: DAEMON THREADS
#
# Learn: thread.daemon property
#
# Tasks:
# 1. Create a thread that runs indefinitely (while True loop)
# 2. Set thread.daemon = True before starting
# 3. Start the thread
# 4. Notice the program exits even though thread is running
# 5. Compare behavior with daemon=False
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 7: SCHEDULING TASKS
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 35: SIMPLE SCHEDULER LOOP
#
# Learn: Building a basic scheduler
#
# Tasks:
# 1. Create a function to perform a task
# 2. Create a loop that runs the task every N seconds
# 3. Use time.sleep() between iterations
# 4. Add a way to stop the scheduler (e.g., after X iterations)
# 5. Handle KeyboardInterrupt to stop gracefully
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 36: SCHEDULE AT SPECIFIC TIMES
#
# Learn: Time-based scheduling logic
#
# Tasks:
# 1. Define a target time (e.g., run at 3:00 PM)
# 2. Create a loop that checks current time
# 3. Execute task when target time is reached
# 4. Sleep for short intervals between checks
# 5. Handle the case where target time has passed
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 37: SCHEDULE WITH THREADING
#
# Learn: threading.Timer()
#
# Tasks:
# 1. Create a function to execute
# 2. Create a Timer that runs the function after N seconds
# 3. Start the timer
# 4. Show that main program continues
# 5. Cancel the timer before it executes (optional)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 38: RECURRING TIMER
#
# Learn: Self-rescheduling timer pattern
#
# Tasks:
# 1. Create a function that does work AND reschedules itself
# 2. Use threading.Timer inside the function
# 3. Start the initial timer
# 4. Let it run several times
# 5. Add a way to stop the recurring timer
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 8: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 39: POMODORO TIMER
#
# Scenario: Build a productivity timer
#
# Tasks:
# 1. Create 25-minute work timer
# 2. Create 5-minute break timer
# 3. Alternate between work and break
# 4. Display countdown in console
# 5. Play a sound or show notification when timer ends
# 6. Track number of completed pomodoros
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 40: AUTOMATIC BACKUP SCHEDULER
#
# Scenario: Schedule file backups
#
# Tasks:
# 1. Create a function to copy files to backup folder
# 2. Add timestamp to backup folder name
# 3. Schedule backup to run every hour
# 4. Log each backup with timestamp
# 5. Keep only last 5 backups (delete older ones)
# 6. Run scheduler in background thread
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 41: WEBSITE MONITOR
#
# Scenario: Check if websites are up
#
# Tasks:
# 1. Create a list of URLs to monitor
# 2. Create function to check if URL is reachable (subprocess curl/ping)
# 3. Check all URLs periodically (every 5 minutes)
# 4. Log status with timestamps
# 5. Alert (print message) if a site is down
# 6. Use threads to check multiple sites concurrently
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 42: BATCH FILE PROCESSOR
#
# Scenario: Process files at scheduled times
#
# Tasks:
# 1. Watch a folder for new files
# 2. Process files (e.g., move to another folder, rename)
# 3. Run the check every 30 seconds
# 4. Log all processed files with timestamps
# 5. Handle errors for locked or missing files
# 6. Generate daily summary report
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 43: COMMAND-LINE AUTOMATION
#
# Scenario: Automate repetitive terminal tasks
#
# Tasks:
# 1. Create a list of commands to run in sequence
# 2. Run each command with subprocess
# 3. Capture and log output from each command
# 4. Stop if any command fails (or continue with flag)
# 5. Generate a report of all commands and their status
# 6. Add timing information for each command
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 44: MULTI-THREADED DOWNLOADER
#
# Scenario: Download multiple files concurrently
#
# Tasks:
# 1. Create a list of file URLs to download
# 2. Create a function to download a single file (use subprocess with curl/wget)
# 3. Create a thread for each download
# 4. Limit concurrent downloads (e.g., max 3 at a time)
# 5. Show progress (which files are downloading/complete)
# 6. Report total time saved vs sequential download
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 45: DAILY TASK AUTOMATOR
#
# Scenario: Run different tasks at different times
#
# Tasks:
# 1. Create a schedule dictionary:
#    {"09:00": task1, "12:00": task2, "17:00": task3}
# 2. Create task functions (e.g., open apps, run scripts)
# 3. Create a scheduler that checks time and runs tasks
# 4. Mark tasks as completed so they don't repeat same day
# 5. Reset completed tasks at midnight
# 6. Log all task executions
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 46: APPLICATION LAUNCHER
#
# Scenario: Quick launcher for common applications
#
# Tasks:
# 1. Create a dictionary of app names and their paths/commands
# 2. Create a menu to select an application
# 3. Launch the selected application with subprocess
# 4. Handle applications that don't exist
# 5. Add ability to launch multiple apps at once
# 6. Save frequently used combos (e.g., "work mode" opens email + browser + IDE)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 47: SYSTEM RESOURCE MONITOR
#
# Scenario: Monitor CPU, memory, disk usage over time
#
# Tasks:
# 1. Use subprocess to run system commands (top, wmic, etc.)
# 2. Parse the output to extract metrics
# 3. Log metrics with timestamps
# 4. Check metrics every minute
# 5. Alert if any metric exceeds threshold
# 6. Save data to CSV for later analysis
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 48: REMINDER APPLICATION
#
# Scenario: Set reminders that trigger at specific times
#
# Tasks:
# 1. Create a Reminder class with message and datetime
# 2. Store reminders in a list
# 3. Create a background thread that checks for due reminders
# 4. Display reminder when time is reached
# 5. Allow adding new reminders while running
# 6. Save/load reminders to/from a JSON file
# ----------------------------------------------------------------------


# ======================================================================
# ⏰ QUICK REFERENCE - time Module
# ======================================================================
#
# Getting time:
#   import time
#
#   time.time()           # Seconds since epoch (float)
#   time.ctime()          # Current time as readable string
#   time.localtime()      # Current local time as struct_time
#   time.gmtime()         # Current UTC time as struct_time
#
# Pausing:
#   time.sleep(5)         # Pause for 5 seconds
#   time.sleep(0.5)       # Pause for 500 milliseconds
#
# Precise timing:
#   time.perf_counter()   # High-resolution timer for benchmarking
#   time.monotonic()      # Clock that can't go backwards
#
# Formatting:
#   time.strftime('%Y-%m-%d', time.localtime())
#
# ======================================================================


# ======================================================================
# ⏰ QUICK REFERENCE - datetime Module
# ======================================================================
#
# Import:
#   from datetime import datetime, date, time, timedelta
#   # OR
#   import datetime
#
# Creating datetime objects:
#   datetime.datetime.now()           # Current local datetime
#   datetime.datetime.today()         # Current local datetime
#   datetime.datetime.utcnow()        # Current UTC datetime
#   datetime.datetime(2024, 1, 15, 14, 30, 0)  # Specific datetime
#
# Creating date objects:
#   datetime.date.today()             # Current date
#   datetime.date(2024, 1, 15)        # Specific date
#
# Creating time objects:
#   datetime.time(14, 30, 0)          # 2:30 PM
#
# Attributes:
#   dt.year, dt.month, dt.day
#   dt.hour, dt.minute, dt.second, dt.microsecond
#   dt.weekday()                      # 0=Monday, 6=Sunday
#
# ======================================================================


# ======================================================================
# ⏰ QUICK REFERENCE - timedelta
# ======================================================================
#
# Creating timedelta:
#   from datetime import timedelta
#
#   timedelta(days=7)
#   timedelta(hours=2, minutes=30)
#   timedelta(weeks=1, days=3, hours=4)
#
# Arithmetic:
#   future = datetime.now() + timedelta(days=7)
#   past = datetime.now() - timedelta(hours=2)
#   difference = datetime1 - datetime2  # Returns timedelta
#
# Timedelta attributes:
#   td.days                # Number of days
#   td.seconds             # Seconds (0-86399)
#   td.microseconds        # Microseconds (0-999999)
#   td.total_seconds()     # Total seconds as float
#
# ======================================================================


# ======================================================================
# ⏰ QUICK REFERENCE - strftime Format Codes
# ======================================================================
#
# Date:
#   %Y    Four-digit year       (2024)
#   %y    Two-digit year        (24)
#   %m    Month as number       (01-12)
#   %B    Full month name       (January)
#   %b    Abbreviated month     (Jan)
#   %d    Day of month          (01-31)
#   %j    Day of year           (001-366)
#
# Time:
#   %H    Hour (24-hour)        (00-23)
#   %I    Hour (12-hour)        (01-12)
#   %M    Minute                (00-59)
#   %S    Second                (00-59)
#   %p    AM/PM                 (AM, PM)
#
# Weekday:
#   %A    Full weekday name     (Monday)
#   %a    Abbreviated weekday   (Mon)
#   %w    Weekday number        (0=Sunday, 6=Saturday)
#
# Combined:
#   %c    Locale's date/time
#   %x    Locale's date
#   %X    Locale's time
#
# ======================================================================


# ======================================================================
# ⏰ QUICK REFERENCE - subprocess Module
# ======================================================================
#
# Running commands:
#   import subprocess
#
#   # Simple run
#   result = subprocess.run(['ls', '-l'])
#
#   # Capture output
#   result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
#   print(result.stdout)
#   print(result.stderr)
#   print(result.returncode)
#
#   # Raise exception on error
#   result = subprocess.run(['ls', '-l'], check=True)
#
# CompletedProcess attributes:
#   result.returncode     # 0 = success
#   result.stdout         # Captured stdout
#   result.stderr         # Captured stderr
#
# ======================================================================


# ======================================================================
# ⏰ QUICK REFERENCE - subprocess.Popen
# ======================================================================
#
# Starting processes:
#   proc = subprocess.Popen(['long', 'command'])
#
#   # Check if still running
#   if proc.poll() is None:
#       print("Still running")
#
#   # Wait for completion
#   proc.wait()
#
#   # Get return code
#   print(proc.returncode)
#
# Communication:
#   proc = subprocess.Popen(['cmd'], stdin=subprocess.PIPE,
#                          stdout=subprocess.PIPE, text=True)
#   stdout, stderr = proc.communicate(input='data', timeout=10)
#
# Termination:
#   proc.terminate()      # Graceful termination
#   proc.kill()           # Force kill
#
# ======================================================================


# ======================================================================
# ⏰ QUICK REFERENCE - threading Module
# ======================================================================
#
# Creating threads:
#   import threading
#
#   def my_function(arg1, arg2):
#       print(f"Running with {arg1}, {arg2}")
#
#   t = threading.Thread(target=my_function, args=('hello', 'world'))
#   t.start()             # Start the thread
#   t.join()              # Wait for thread to complete
#
# Thread properties:
#   t.is_alive()          # Check if thread is running
#   t.name                # Thread name
#   t.daemon = True       # Daemon thread (dies with main program)
#
# Timer (delayed execution):
#   timer = threading.Timer(5.0, my_function)  # Run after 5 seconds
#   timer.start()
#   timer.cancel()        # Cancel before it runs
#
# ======================================================================


# ======================================================================
# ⏰ QUICK REFERENCE - Platform-Specific Commands
# ======================================================================
#
# Open file with default app:
#   import subprocess
#   import sys
#
#   if sys.platform == 'win32':
#       subprocess.run(['start', '', filename], shell=True)
#   elif sys.platform == 'darwin':  # macOS
#       subprocess.run(['open', filename])
#   else:  # Linux
#       subprocess.run(['xdg-open', filename])
#
# Alternative - webbrowser module:
#   import webbrowser
#   webbrowser.open('https://google.com')
#   webbrowser.open('file:///path/to/file.html')
#
# ======================================================================


# ======================================================================
# 🚀 SETUP INSTRUCTIONS
# ======================================================================
#
# All modules are built into Python - no installation needed!
#   import time
#   import datetime
#   import subprocess
#   import threading
#   import webbrowser
#
# Platform notes:
#   - subprocess commands differ between Windows and Unix
#   - Use 'dir' on Windows, 'ls' on Unix
#   - Use 'type' on Windows, 'cat' on Unix
#   - shell=True is often needed on Windows for built-in commands
#
# Testing subprocess:
#   # Windows
#   subprocess.run(['cmd', '/c', 'echo', 'Hello'])
#   subprocess.run('dir', shell=True)
#
#   # Unix (macOS/Linux)
#   subprocess.run(['echo', 'Hello'])
#   subprocess.run(['ls', '-l'])
#
# Thread safety reminder:
#   - Don't modify shared data without locks
#   - Use threading.Lock() for shared resources
#   - Avoid race conditions
#
# ======================================================================
# ======================================================================
