# ======================================================================
# 🖱️ CONTROLLING THE KEYBOARD AND MOUSE WITH GUI AUTOMATION
# ======================================================================
# Practice exercises - Write everything from scratch!
# Prerequisites: pyautogui installed, macOS accessibility enabled
# ======================================================================

# pip install pyautogui pyperclip pillow

import time

import pyautogui

# =====================================================================
#                    SECTION 1: PYAUTOGUI BASICS AND SAFETY
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 1: INSTALL AND IMPORT PYAUTOGUI
#
# Learn: Installing pyautogui, basic imports
#
# Tasks:
# 1. Install pyautogui: pip install pyautogui
# 2. Import pyautogui
# 3. Check version with pyautogui.__version__
# 4. On macOS: Enable accessibility for your terminal/IDE
#    (System Preferences > Security & Privacy > Accessibility)
# 5. Test that import works without errors
# ----------------------------------------------------------------------

print(pyautogui.__version__)  # type: ignore

# ----------------------------------------------------------------------
# 🟢 2: UNDERSTAND THE FAIL-SAFE
#
# Learn: pyautogui.FAILSAFE, pyautogui.PAUSE
#
# Tasks:
# 1. Check that pyautogui.FAILSAFE is True (default)
# 2. Understand: moving mouse to corner stops the program
# 3. Check pyautogui.PAUSE value (default 0.1 seconds)
# 4. Try setting pyautogui.PAUSE = 0.5 for slower execution
# 5. Practice moving mouse to corner to trigger fail-safe
# ----------------------------------------------------------------------

print(pyautogui.FAILSAFE)
print(pyautogui.PAUSE)
pyautogui.PAUSE = 0.5
print(pyautogui.PAUSE)
# pyautogui.sleep(5)

# for _ in range(5):
#     pyautogui.sleep(2)
#     pyautogui.click()

# ----------------------------------------------------------------------
# 🟢 3: GET SCREEN SIZE
#
# Learn: pyautogui.size()
#
# Tasks:
# 1. Call pyautogui.size() to get screen dimensions
# 2. The return is a Size named tuple
# 3. Access width and height: size.width, size.height
# 4. Also access via index: size[0], size[1]
# 5. Calculate the center of your screen
# ----------------------------------------------------------------------

print(pyautogui.size())
print(pyautogui.size().width)
print(pyautogui.size().height)

width, height = pyautogui.size()

center = (width // 2, height // 2)
print(center)

# ----------------------------------------------------------------------
# 🟢 4: USE SLEEP AND COUNTDOWN
#
# Learn: pyautogui.sleep(), pyautogui.countdown()
#
# Tasks:
# 1. Use pyautogui.sleep(3) to pause for 3 seconds
# 2. Use pyautogui.countdown(5) to show a countdown
# 3. Combine: print('Starting in ', end=''); pyautogui.countdown(3)
# 4. These are useful at the start of scripts
# 5. Give yourself time to position windows before automation starts
# ----------------------------------------------------------------------

# pyautogui.sleep(3)
# pyautogui.countdown(5)

# print(pyautogui.countdown(3))
# print("Starting in: ", end="")
# for _ in range(3, 0, -1):
#     print(_, end=" ")
#     time.sleep(1)

# =====================================================================
#                    SECTION 2: MOUSE MOVEMENT
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 5: GET CURRENT MOUSE POSITION
#
# Learn: pyautogui.position()
#
# Tasks:
# 1. Call pyautogui.position() to get current mouse location
# 2. The return is a Point named tuple (x, y)
# 3. Access coordinates: pos.x, pos.y or pos[0], pos[1]
# 4. Move your mouse and call position() again
# 5. Write a loop that prints position every second
# ----------------------------------------------------------------------

current_point = pyautogui.position()
print(current_point)
print(current_point.x, current_point.y)

# for _ in range(10):
#     pyautogui.sleep(1)
#     print(pyautogui.position())

# ----------------------------------------------------------------------
# 🟢 6: MOVE MOUSE TO ABSOLUTE POSITION
#
# Learn: pyautogui.moveTo()
#
# Tasks:
# 1. Move mouse to top-left: pyautogui.moveTo(0, 0)
# 2. Move to center of screen (calculate from size)
# 3. Use duration parameter: moveTo(500, 500, duration=1)
# 4. Watch the mouse move smoothly over 1 second
# 5. Try different durations to see the effect
# ----------------------------------------------------------------------

# pyautogui.moveTo(50, 50, duration=0.2)
# pyautogui.moveTo(center[0], center[1], duration=0.2)
# pyautogui.moveTo(500, 500, duration=0.2)
# pyautogui.moveTo(1000, 1000, duration=10)

# ----------------------------------------------------------------------
# 🟢 7: MOVE MOUSE RELATIVE TO CURRENT POSITION
#
# Learn: pyautogui.move()
#
# Tasks:
# 1. Move right 100 pixels: pyautogui.move(100, 0)
# 2. Move down 100 pixels: pyautogui.move(0, 100)
# 3. Move left (negative x): pyautogui.move(-100, 0)
# 4. Move up (negative y): pyautogui.move(0, -100)
# 5. Add duration for smooth movement
# ----------------------------------------------------------------------

x, y = center
# pyautogui.moveTo(x, y)
# pyautogui.move(90, 0, duration=0.2)
# pyautogui.move(0, 90, duration=0.2)
# pyautogui.move(-90, 0, duration=0.2)
# pyautogui.move(0, -90, duration=0.2)

# ----------------------------------------------------------------------
# 🟡 8: DRAW A SQUARE WITH MOUSE MOVEMENT
#
# Learn: Combining moveTo() and move()
#
# Tasks:
# 1. Move to starting position with moveTo()
# 2. Use move() to go right, down, left, up
# 3. Use duration for visible movement
# 4. Create a loop to draw the square multiple times
# 5. Experiment with different square sizes
# ----------------------------------------------------------------------

pyautogui.sleep(2)
pyautogui.moveTo(x, y)
pyautogui.click()

distance = 500
change = 20

# for index in range(0, distance, change):
#     pyautogui.drag(distance, 0, button="left")
#     pyautogui.drag(0, distance, button="left")
#     pyautogui.drag(-distance, 0, button="left")
#     pyautogui.drag(0, -distance, button="left")
#     distance -= change

# ----------------------------------------------------------------------
# 🟡 9: CREATE MOUSE MOVEMENT PATTERNS
#
# Learn: Complex mouse movements
#
# Tasks:
# 1. Create a function that draws a triangle
# 2. Create a function that draws a circle (approximate with many points)
# 3. Create a zigzag pattern
# 4. Use math module for circle: x = center_x + radius * cos(angle)
# 5. Make patterns customizable (size, position, speed)
# ----------------------------------------------------------------------


# pyautogui.drag(-50, 0, button="left")
# pyautogui.drag(50, -50, button="left")
# pyautogui.drag(50, 50, button="left")
# pyautogui.drag(-50, 0, button="left")

# for i in range(50):
#     pyautogui.drag(20, 0, button="left")
#     pyautogui.drag(0, 20, button="left")

# =====================================================================
#                    SECTION 3: MOUSE CLICKING
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 10: BASIC MOUSE CLICK
#
# Learn: pyautogui.click()
#
# Tasks:
# 1. Click at current position: pyautogui.click()
# 2. Click at specific coordinates: pyautogui.click(100, 200)
# 3. Specify button: pyautogui.click(button='left')
# 4. Try button='right' and button='middle'
# 5. Combine position and button parameters
# ----------------------------------------------------------------------

# pyautogui.click(x, y, button="right")

# ----------------------------------------------------------------------
# 🟢 11: DOUBLE CLICK AND RIGHT CLICK
#
# Learn: pyautogui.doubleClick(), rightClick(), middleClick()
#
# Tasks:
# 1. Double-click at current position: pyautogui.doubleClick()
# 2. Double-click at coordinates: pyautogui.doubleClick(x, y)
# 3. Right-click: pyautogui.rightClick()
# 4. Middle-click: pyautogui.middleClick()
# 5. Test each click type and observe the effect
# ----------------------------------------------------------------------

# pyautogui.doubleClick(x, y)
# pyautogui.middleClick(x, y)

# ----------------------------------------------------------------------
# 🟢 12: MOUSE DOWN AND MOUSE UP
#
# Learn: pyautogui.mouseDown(), mouseUp()
#
# Tasks:
# 1. Press mouse button: pyautogui.mouseDown()
# 2. Release mouse button: pyautogui.mouseUp()
# 3. Specify button: mouseDown(button='left')
# 4. Understand that click() = mouseDown() + mouseUp()
# 5. Useful for drag operations or holding buttons
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
# 🟡 13: CLICK MULTIPLE TIMES
#
# Learn: clicks parameter, interval parameter
#
# Tasks:
# 1. Triple-click: pyautogui.click(clicks=3)
# 2. Add interval between clicks: click(clicks=3, interval=0.5)
# 3. Create a function that clicks n times with delay
# 4. Use this to select a paragraph (triple-click)
# 5. Experiment with different click counts and intervals
# ----------------------------------------------------------------------

# pyautogui.click(clicks=3, interval=0.5, button="right")

# =====================================================================
#                    SECTION 4: DRAGGING
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 14: DRAG TO ABSOLUTE POSITION
#
# Learn: pyautogui.dragTo()
#
# Tasks:
# 1. Position mouse over something draggable
# 2. Drag to position: pyautogui.dragTo(500, 500, duration=1)
# 3. On macOS, duration is recommended for proper dragging
# 4. Try dragging a file icon or window
# 5. Experiment with different durations
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 15: DRAG RELATIVE TO CURRENT POSITION
#
# Learn: pyautogui.drag()
#
# Tasks:
# 1. Drag right: pyautogui.drag(100, 0, duration=0.5)
# 2. Drag down: pyautogui.drag(0, 100, duration=0.5)
# 3. Drag diagonally: pyautogui.drag(100, 100, duration=0.5)
# 4. Always use duration on macOS for reliable dragging
# 5. Create a function to drag in a specific direction
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 16: DRAW A SPIRAL IN A DRAWING APP
#
# Learn: Complex drag patterns
#
# Tasks:
# 1. Open a drawing app (Paintbrush, Preview, or online like sumopaint.com)
# 2. Select the brush/pencil tool
# 3. Use pyautogui.sleep(5) to give time to position
# 4. Click to activate the canvas
# 5. Use drag() in a loop with decreasing distances to make a spiral
# 6. Reference the spiralDraw.py example from the chapter
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 5: SCROLLING
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 17: BASIC SCROLLING
#
# Learn: pyautogui.scroll()
#
# Tasks:
# 1. Scroll up: pyautogui.scroll(5)  # Positive = up
# 2. Scroll down: pyautogui.scroll(-5)  # Negative = down
# 3. Scroll at specific position: pyautogui.scroll(5, x=100, y=200)
# 4. Note: scroll amount varies by application
# 5. Experiment to find the right scroll amount
# ----------------------------------------------------------------------

# pyautogui.scroll(150)
# pyautogui.scroll(-150)

# ----------------------------------------------------------------------
# 🟡 18: HORIZONTAL SCROLLING
#
# Learn: pyautogui.hscroll() (if available)
#
# Tasks:
# 1. Try pyautogui.hscroll(5) for horizontal scroll
# 2. Note: Not all systems/applications support this
# 3. Alternative: Use keyboard shortcuts (Shift+scroll)
# 4. Test in a horizontally scrollable area
# 5. Create a function that scrolls in any direction
# ----------------------------------------------------------------------

# pyautogui.hscroll(-500)
# pyautogui.hscroll(800)

# ----------------------------------------------------------------------
# 🟡 19: SMOOTH SCROLLING
#
# Learn: Scroll in increments with delays
#
# Tasks:
# 1. Create a function for smooth scrolling
# 2. Scroll small amounts with short delays
# 3. for _ in range(10): pyautogui.scroll(1); time.sleep(0.1)
# 4. Adjust increment and delay for desired smoothness
# 5. Create both smooth_scroll_up() and smooth_scroll_down()
# ----------------------------------------------------------------------

# for i in range(10):
#     pyautogui.sleep(0.2)
#     pyautogui.scroll(-10)

# =====================================================================
#                    SECTION 6: SCREENSHOTS AND PIXELS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 20: TAKE A SCREENSHOT
#
# Learn: pyautogui.screenshot()
#
# Tasks:
# 1. Take screenshot: img = pyautogui.screenshot()
# 2. The result is a Pillow Image object
# 3. Save it: img.save('screenshot.png')
# 4. Take screenshot of region: screenshot(region=(x, y, width, height))
# 5. View your saved screenshot
# ----------------------------------------------------------------------

img = pyautogui.screenshot()
img.save("/Users/daniel_molina/Downloads/Python/Python/Book/chapter23/20.png")

img = pyautogui.screenshot(region=(500, 1000, 800, 800))
# img.show()

# ----------------------------------------------------------------------
# 🟢 21: GET PIXEL COLOR
#
# Learn: pyautogui.pixel()
#
# Tasks:
# 1. Get color at position: pyautogui.pixel(100, 200)
# 2. Returns RGB tuple like (255, 128, 64)
# 3. Get color at current mouse position using position()
# 4. Create a loop that prints color as you move the mouse
# 5. Identify colors of UI elements on your screen
# ----------------------------------------------------------------------

pixel = pyautogui.pixel(2560, 600)
print(pixel)

pixel = pyautogui.pixel(pyautogui.position().x, pyautogui.position().y)
print(pixel)

# for index in range(10):
#     pyautogui.sleep(0.5)
#     print(pyautogui.pixel(pyautogui.position().x, pyautogui.position().y))

# ----------------------------------------------------------------------
# 🟡 22: CHECK IF PIXEL MATCHES COLOR
#
# Learn: pyautogui.pixelMatchesColor()
#
# Tasks:
# 1. Get a pixel's color with pixel()
# 2. Check if it matches: pixelMatchesColor(x, y, (r, g, b))
# 3. Returns True if exact match, False otherwise
# 4. Use this before clicking to verify correct location
# 5. Create a function that waits until a pixel changes color
# ----------------------------------------------------------------------

color = pyautogui.pixel(2520, 600)
print(pyautogui.pixelMatchesColor(100, 100, color))

# ----------------------------------------------------------------------
# 🟡 23: USE MOUSEINFO FOR COORDINATES
#
# Learn: pyautogui.mouseInfo()
#
# Tasks:
# 1. Call pyautogui.mouseInfo() to launch the MouseInfo app
# 2. Move your mouse and observe coordinates update
# 3. Use F1-F8 keys or buttons to log positions
# 4. The color under the cursor is also shown
# 5. Use this tool to plan your automation scripts
# ----------------------------------------------------------------------

# pyautogui.mouseInfo()

# =====================================================================
#                    SECTION 7: IMAGE RECOGNITION
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 24: LOCATE IMAGE ON SCREEN
#
# Learn: pyautogui.locateOnScreen()
#
# Tasks:
# 1. Take a screenshot of a button or icon
# 2. Save it as a small PNG file
# 3. Find it: box = pyautogui.locateOnScreen('button.png')
# 4. Returns Box(left, top, width, height) or raises exception
# 5. Use try/except to handle ImageNotFoundException
# ----------------------------------------------------------------------

screenshot = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter23/icon.png"
box = pyautogui.locateAllOnScreen(screenshot)
print(list(box))


# ----------------------------------------------------------------------
# 🟡 25: CLICK ON LOCATED IMAGE
#
# Learn: Clicking found images
#
# Tasks:
# 1. Locate an image on screen
# 2. Click the center of the found region
# 3. Shortcut: pyautogui.click('button.png')
# 4. This combines locateOnScreen() and click()
# 5. Always use try/except for robustness
# ----------------------------------------------------------------------

# pyautogui.click(screenshot)

# ----------------------------------------------------------------------
# 🟡 26: FIND ALL INSTANCES OF AN IMAGE
#
# Learn: pyautogui.locateAllOnScreen()
#
# Tasks:
# 1. Use locateAllOnScreen() to find all matches
# 2. Returns a generator - convert to list: list(locateAllOnScreen())
# 3. Each item is a Box with location info
# 4. Click on each found instance
# 5. Useful for repetitive UI elements
# ----------------------------------------------------------------------

all_icons = list(pyautogui.locateAllOnScreen(screenshot))

# for icon in all_icons:
#     pyautogui.click(icon)

# ----------------------------------------------------------------------
# 🟡 27: LOCATE WITH CONFIDENCE
#
# Learn: confidence parameter (requires opencv-python)
#
# Tasks:
# 1. Install opencv-python: pip install opencv-python
# 2. Use confidence parameter: locateOnScreen('img.png', confidence=0.9)
# 3. Value 0-1, where 1 is exact match
# 4. Lower confidence allows slight variations
# 5. Useful when images aren't pixel-perfect matches
# ----------------------------------------------------------------------

import cv2

icon = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter23/icon.png"
generator = list(pyautogui.locateAllOnScreen(icon, confidence=0.999))
print(len(list(generator)))

# for i in generator:
#     pyautogui.doubleClick(i)

# ----------------------------------------------------------------------
# 🟡 28: LOCATE CENTER OF IMAGE
#
# Learn: pyautogui.locateCenterOnScreen()
#
# Tasks:
# 1. Find center directly: center = locateCenterOnScreen('button.png')
# 2. Returns Point(x, y) of the center
# 3. Useful when you just need click coordinates
# 4. Combine with click(): click(locateCenterOnScreen('button.png'))
# 5. Handle exceptions appropriately
# ----------------------------------------------------------------------

center = pyautogui.locateCenterOnScreen(icon)
# pyautogui.click(center)
print(center)

# =====================================================================
#                    SECTION 8: KEYBOARD CONTROL
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 29: TYPE A STRING
#
# Learn: pyautogui.write()
#
# Tasks:
# 1. Click a text field first
# 2. Type text: pyautogui.write('Hello, world!')
# 3. Add delay between keys: write('Hello', interval=0.1)
# 4. Note: write() works with standard characters
# 5. For special keys, use different functions
# ----------------------------------------------------------------------

pyautogui.click(300, 300)
# pyautogui.write("Heeeeeeello", interval=0.25)

# pyautogui.write(["a", "b", "left", "left", "X", "Y"], interval=0.25)
# pyautogui.write(["\n", "\n", "\n", "\t"], interval=0.25)
# pyautogui.write("This is me?", interval=0.25)
# print(pyautogui.KEYBOARD_KEYS)

# ----------------------------------------------------------------------
# 🟢 30: PRESS INDIVIDUAL KEYS
#
# Learn: pyautogui.press()
#

# Tasks:
# 1. Press enter: pyautogui.press('enter')
# 2. Press escape: pyautogui.press('esc')
# 3. Press arrow keys: press('up'), press('down'), press('left'), press('right')
# 4. Press function keys: press('f1'), press('f5')
# 5. See pyautogui.KEYBOARD_KEYS for all valid key names
# ----------------------------------------------------------------------

pyautogui.press("enter")
pyautogui.press("esc")
pyautogui.press("up")
pyautogui.press("down")
pyautogui.press("left")
pyautogui.press("right")

# ----------------------------------------------------------------------
# 🟢 31: TYPE WITH SPECIAL KEYS
#
# Learn: write() with key name list
#
# Tasks:
# 1. Type with keys: pyautogui.write(['a', 'b', 'c', 'enter'])
# 2. Mix text and special keys
# 3. Example: write(['H', 'i', 'enter', 'enter', 'B', 'y', 'e'])
# 4. Use arrow keys: write(['a', 'b', 'left', 'left', 'X'])
# 5. Understand how arrow keys affect cursor position
# ----------------------------------------------------------------------

pyautogui.write(["a", "b", "c", "enter", "enter", "\t"], interval=0.25)

# ----------------------------------------------------------------------
# 🟡 32: KEY DOWN AND KEY UP
#
# Learn: pyautogui.keyDown(), keyUp()
#
# Tasks:
# 1. Hold shift: pyautogui.keyDown('shift')
# 2. Press a key while shift is held
# 3. Release shift: pyautogui.keyUp('shift')
# 4. This allows typing capitals or symbols
# 5. Example: keyDown('shift'); press('a'); keyUp('shift')  # Types 'A'
# ----------------------------------------------------------------------

pyautogui.keyDown("shift")
pyautogui.write("this are big and not small")
pyautogui.keyUp("shift")
pyautogui.write("\n")
pyautogui.write("back to normal")

# copy
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("c")
# pyautogui.keyUp("c")
# pyautogui.keyUp("ctrl")

# pyautogui.hotkey("ctrl", "c")
# pyautogui.hotkey("ctrl", "v")

# ----------------------------------------------------------------------
# 🟡 33: HOTKEY COMBINATIONS
#
# Learn: pyautogui.hotkey()
#
# Tasks:
# 1. Copy: pyautogui.hotkey('command', 'c')  # macOS uses 'command'
# 2. Paste: pyautogui.hotkey('command', 'v')
# 3. Select all: pyautogui.hotkey('command', 'a')
# 4. Save: pyautogui.hotkey('command', 's')
# 5. Undo: pyautogui.hotkey('command', 'z')
# 6. Note: On macOS use 'command', not 'ctrl'
# ----------------------------------------------------------------------

# pyautogui.hotkey("command", "c")
# pyautogui.hotkey("command", "v")
# pyautogui.hotkey("command", "a")
# pyautogui.hotkey("command", "s")
# pyautogui.hotkey("command", "z")


# ----------------------------------------------------------------------
# 🟡 34: COMMON MACOS HOTKEYS
#
# Learn: macOS-specific keyboard shortcuts
#
# Tasks:
# 1. New window: hotkey('command', 'n')
# 2. Close window: hotkey('command', 'w')
# 3. Quit app: hotkey('command', 'q')
# 4. Find: hotkey('command', 'f')
# 5. Switch apps: hotkey('command', 'tab')
# 6. Screenshot: hotkey('command', 'shift', '3')
# 7. Create a reference dict of common macOS hotkeys
# ----------------------------------------------------------------------

# pyautogui.hotkey("command", "n")
# pyautogui.hotkey("command", "w")
# pyautogui.hotkey("command", "q")
# pyautogui.hotkey("command", "f")
# pyautogui.hotkey("command", "tab")
# pyautogui.hotkey("command", "shift", "3")

# =====================================================================
#                    SECTION 9: MESSAGE BOXES
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 35: ALERT BOX
#
# Learn: pyautogui.alert()
#
# Tasks:
# 1. Show alert: pyautogui.alert('Hello!')
# 2. Add title: alert(text='Message', title='My Title')
# 3. Custom button: alert(text='Done!', button='OK')
# 4. Alert blocks until user clicks OK
# 5. Use for notifications to the user
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 36: CONFIRM BOX
#
# Learn: pyautogui.confirm()
#
# Tasks:
# 1. Show confirm: result = pyautogui.confirm('Continue?')
# 2. Returns 'OK' or 'Cancel' based on user choice
# 3. Add custom buttons: confirm(buttons=['Yes', 'No', 'Maybe'])
# 4. Check the result and act accordingly
# 5. Use for yes/no decisions in scripts
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 37: PROMPT FOR INPUT
#
# Learn: pyautogui.prompt()
#
# Tasks:
# 1. Get text input: name = pyautogui.prompt('Enter your name:')
# 2. Returns the entered string, or None if cancelled
# 3. Add default value: prompt('Name:', default='John')
# 4. Always check for None (user cancelled)
# 5. Use for getting user input during automation
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 38: PASSWORD INPUT
#
# Learn: pyautogui.password()
#
# Tasks:
# 1. Get password: pwd = pyautogui.password('Enter password:')
# 2. Input is masked with asterisks
# 3. Returns the entered string, or None if cancelled
# 4. Add custom mask: password(mask='●')
# 5. Use for sensitive input (but be careful with storage!)
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 10: PRACTICAL AUTOMATION
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 39: AUTOMATE FORM FILLING
#
# Learn: Combining clicks and typing
#
# Tasks:
# 1. Open a web form or document
# 2. Use click() to select the first field
# 3. Use write() to enter data
# 4. Use press('tab') to move to next field
# 5. Repeat for all fields
# 6. Use hotkey() to submit if needed
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 40: CREATE A TYPING AUTOMATION
#
# Learn: Automated typing with delays
#
# Tasks:
# 1. Read text from a file
# 2. Click in a text editor
# 3. Type the text with interval parameter
# 4. Add pauses between paragraphs
# 5. Handle special characters appropriately
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 41: CLICK-BASED NAVIGATION
#
# Learn: Automating UI navigation
#
# Tasks:
# 1. Plan a sequence of clicks for a task
# 2. Use MouseInfo to record coordinates
# 3. Add appropriate delays between clicks
# 4. Use sleep() to wait for windows/pages to load
# 5. Add verification using pixel colors or images
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 42: SAFE AUTOMATION WITH CHECKS
#
# Learn: Building robust automation
#
# Tasks:
# 1. Before clicking, verify the target using locateOnScreen()
# 2. If not found, show an alert to the user
# 3. Use confirm() to ask before destructive actions
# 4. Add try/except around all PyAutoGUI calls
# 5. Use the fail-safe (don't disable it!)
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 11: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 43: AUTOMATED SCREENSHOT TAKER
#
# Scenario: Take screenshots at regular intervals
#
# Tasks:
# 1. Create a function that takes timestamped screenshots
# 2. Save to a specific folder with date/time in filename
# 3. Run in a loop with configurable interval
# 4. Add a way to stop (keyboard interrupt or message box)
# 5. Create option for full screen or region
# 6. Add a countdown before first screenshot
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 44: CLICK RECORDER
#
# Scenario: Record mouse clicks for playback
#
# Tasks:
# 1. Create a script that records click positions
# 2. Save positions and click types to a list
# 3. Use keyboard to start/stop recording
# 4. Save recording to a JSON file
# 5. Create a playback function
# 6. Allow adjustable playback speed
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 45: AUTO-CLICKER WITH CONTROLS
#
# Scenario: Click repeatedly until stopped
#
# Tasks:
# 1. Ask user for click interval with prompt()
# 2. Ask for click position (current or specific)
# 3. Start clicking in a loop
# 4. Use confirm() periodically to ask "Continue?"
# 5. Stop when user says no or moves mouse to corner
# 6. Report total clicks when done
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 46: COLOR PICKER TOOL
#
# Scenario: Get colors from anywhere on screen
#
# Tasks:
# 1. Display instructions with alert()
# 2. Wait for user to position mouse
# 3. Get pixel color at current position
# 4. Convert RGB to hex format
# 5. Show color info with alert()
# 6. Ask if user wants to pick another color
# 7. Save all picked colors to a file
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 47: DRAWING AUTOMATION
#
# Scenario: Draw shapes in a graphics program
#
# Tasks:
# 1. Open a drawing app (give user time to set up)
# 2. Create functions for basic shapes (line, rectangle, circle)
# 3. Accept position, size, and optional duration
# 4. Draw a simple picture using your shape functions
# 5. Add variety with different starting positions
# 6. Optional: Add color selection if app supports it
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 48: DATA ENTRY AUTOMATION
#
# Scenario: Enter data from a spreadsheet into a form
#
# Tasks:
# 1. Read data from a CSV file
# 2. For each row, fill out a form
# 3. Click fields, enter data, tab between fields
# 4. Submit each form
# 5. Wait for confirmation before next entry
# 6. Log successful and failed entries
# 7. Handle errors gracefully
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 49: BUTTON FINDER
#
# Scenario: Find and click UI elements by image
#
# Tasks:
# 1. Take screenshots of buttons you want to find
# 2. Create a function that finds and clicks a button by image
# 3. Wait and retry if not immediately found
# 4. Set a timeout for how long to wait
# 5. Return success/failure status
# 6. Create a library of common button images
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 50: SCREEN WATCHER
#
# Scenario: Monitor screen for changes
#
# Tasks:
# 1. Take a reference screenshot of an area
# 2. Periodically check if the area has changed
# 3. Compare pixel colors or use image comparison
# 4. Alert user when change is detected
# 5. Useful for: waiting for downloads, notifications, etc.
# 6. Save before/after screenshots when change detected
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 51: TEXT EXTRACTION AUTOMATION
#
# Scenario: Extract text from non-copyable sources
#
# Tasks:
# 1. Take a screenshot of text region
# 2. Crop to just the text area
# 3. Use pytesseract (OCR) to extract text (Chapter 22)
# 4. Save or copy to clipboard
# 5. Create a function: screen_region_to_text(region)
# 6. Allow user to specify region or use coordinates
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 52: MULTI-STEP WORKFLOW AUTOMATION
#
# Scenario: Automate a complex multi-step process
#
# Tasks:
# 1. Define steps as a list of actions
# 2. Each step: click, type, wait, verify
# 3. Execute steps in sequence
# 4. Verify each step succeeded before continuing
# 5. Log all actions taken
# 6. Allow resuming from a specific step
# 7. Create a simple "macro recorder" format
# ----------------------------------------------------------------------


# ======================================================================
# 🖱️ QUICK REFERENCE - Mouse Functions
# ======================================================================
#
# Get info:
#   pyautogui.size()           # Screen dimensions (width, height)
#   pyautogui.position()       # Current mouse position (x, y)
#
# Move:
#   pyautogui.moveTo(x, y)                    # Absolute position
#   pyautogui.moveTo(x, y, duration=1)        # With animation
#   pyautogui.move(dx, dy)                    # Relative movement
#
# Click:
#   pyautogui.click()                         # Left click at current pos
#   pyautogui.click(x, y)                     # Click at position
#   pyautogui.click(button='right')           # Right click
#   pyautogui.click(clicks=2)                 # Double click
#   pyautogui.click(clicks=2, interval=0.1)   # With delay between
#   pyautogui.doubleClick()                   # Double left click
#   pyautogui.rightClick()                    # Right click
#   pyautogui.middleClick()                   # Middle click
#
# Mouse buttons:
#   pyautogui.mouseDown()                     # Press button
#   pyautogui.mouseUp()                       # Release button
#
# Drag:
#   pyautogui.dragTo(x, y, duration=0.5)      # Drag to position
#   pyautogui.drag(dx, dy, duration=0.5)      # Drag relative
#   # Note: Always use duration on macOS!
#
# Scroll:
#   pyautogui.scroll(units)                   # + up, - down
#   pyautogui.scroll(5, x=100, y=200)         # Scroll at position
#
# ======================================================================


# ======================================================================
# 🖱️ QUICK REFERENCE - Keyboard Functions
# ======================================================================
#
# Type text:
#   pyautogui.write('Hello')                  # Type string
#   pyautogui.write('Hello', interval=0.1)    # With delay
#   pyautogui.write(['a', 'b', 'enter'])      # Key names
#
# Press keys:
#   pyautogui.press('enter')                  # Press and release
#   pyautogui.press('tab')
#   pyautogui.press('escape')
#
# Hold keys:
#   pyautogui.keyDown('shift')                # Press down
#   pyautogui.keyUp('shift')                  # Release
#
# Hotkeys:
#   pyautogui.hotkey('command', 'c')          # Copy (macOS)
#   pyautogui.hotkey('command', 'v')          # Paste (macOS)
#   pyautogui.hotkey('command', 'a')          # Select all
#   pyautogui.hotkey('command', 'z')          # Undo
#   pyautogui.hotkey('command', 's')          # Save
#
# Common key names:
#   'enter', 'tab', 'escape', 'space', 'backspace', 'delete'
#   'up', 'down', 'left', 'right'
#   'home', 'end', 'pageup', 'pagedown'
#   'f1' through 'f12'
#   'command' (macOS), 'option' (macOS)
#   'shift', 'ctrl', 'alt'
#
# ======================================================================


# ======================================================================
# 🖱️ QUICK REFERENCE - Screenshots and Pixels
# ======================================================================
#
# Screenshots:
#   img = pyautogui.screenshot()                          # Full screen
#   img = pyautogui.screenshot('file.png')                # Save directly
#   img = pyautogui.screenshot(region=(x, y, w, h))       # Region only
#
# Pixel colors:
#   pyautogui.pixel(x, y)                     # Returns (R, G, B)
#   pyautogui.pixelMatchesColor(x, y, (R, G, B))    # True/False
#
# ======================================================================


# ======================================================================
# 🖱️ QUICK REFERENCE - Image Recognition
# ======================================================================
#
# Find image:
#   box = pyautogui.locateOnScreen('button.png')
#   # Returns Box(left, top, width, height) or raises exception
#
# Find center:
#   point = pyautogui.locateCenterOnScreen('button.png')
#   # Returns Point(x, y)
#
# Find all:
#   boxes = list(pyautogui.locateAllOnScreen('icon.png'))
#   # Returns list of Box objects
#
# With confidence (needs opencv-python):
#   box = pyautogui.locateOnScreen('button.png', confidence=0.9)
#
# Click on image:
#   pyautogui.click('button.png')             # Find and click
#
# Handle not found:
#   try:
#       box = pyautogui.locateOnScreen('button.png')
#   except pyautogui.ImageNotFoundException:
#       print('Image not found')
#
# ======================================================================


# ======================================================================
# 🖱️ QUICK REFERENCE - Message Boxes
# ======================================================================
#
# Alert (OK button only):
#   pyautogui.alert('Message here')
#   pyautogui.alert(text='Message', title='Title')
#
# Confirm (OK/Cancel):
#   result = pyautogui.confirm('Continue?')    # Returns 'OK' or 'Cancel'
#   result = pyautogui.confirm(buttons=['Yes', 'No', 'Cancel'])
#
# Prompt (text input):
#   text = pyautogui.prompt('Enter value:')    # Returns string or None
#   text = pyautogui.prompt('Name:', default='Default')
#
# Password (masked input):
#   pwd = pyautogui.password('Enter password:')
#   pwd = pyautogui.password('Password:', mask='*')
#
# ======================================================================


# ======================================================================
# 🖱️ QUICK REFERENCE - Safety and Timing
# ======================================================================
#
# Fail-safe:
#   pyautogui.FAILSAFE = True    # Move mouse to corner to stop (default)
#   # DON'T disable this!
#
# Pause between actions:
#   pyautogui.PAUSE = 0.1        # Seconds (default)
#   pyautogui.PAUSE = 0.5        # Slower, safer
#
# Sleep:
#   pyautogui.sleep(seconds)     # Same as time.sleep()
#
# Countdown:
#   pyautogui.countdown(5)       # Prints 5 4 3 2 1
#
# MouseInfo tool:
#   pyautogui.mouseInfo()        # Opens coordinate helper app
#
# ======================================================================


# ======================================================================
# 🚀 MACOS SETUP INSTRUCTIONS
# ======================================================================
#
# 1. Install PyAutoGUI:
#    pip install pyautogui
#
# 2. Enable Accessibility:
#    - Open System Preferences (or System Settings on newer macOS)
#    - Go to Security & Privacy > Privacy > Accessibility
#    - Click the lock to make changes
#    - Add and check your Terminal, IDE (PyCharm, VS Code), or Mu
#    - You may need to restart the application
#
# 3. For image recognition:
#    pip install opencv-python
#
# 4. Test in interactive shell:
#    >>> import pyautogui
#    >>> pyautogui.position()
#    >>> pyautogui.size()
#
# 5. Important macOS notes:
#    - Use 'command' instead of 'ctrl' for hotkeys
#    - Use 'option' for the Option key
#    - Always use duration with drag functions
#    - Accessibility must be enabled or actions have no effect
#
# ======================================================================


# ======================================================================
# 🖱️ QUICK REFERENCE - macOS Keyboard Keys
# ======================================================================
#
# macOS-specific keys:
#   'command'       # ⌘ Command key
#   'option'        # ⌥ Option key
#
# Common macOS hotkeys in PyAutoGUI:
#   hotkey('command', 'c')          # Copy
#   hotkey('command', 'v')          # Paste
#   hotkey('command', 'x')          # Cut
#   hotkey('command', 'a')          # Select All
#   hotkey('command', 'z')          # Undo
#   hotkey('command', 'shift', 'z') # Redo
#   hotkey('command', 's')          # Save
#   hotkey('command', 'n')          # New
#   hotkey('command', 'o')          # Open
#   hotkey('command', 'w')          # Close Window
#   hotkey('command', 'q')          # Quit App
#   hotkey('command', 'tab')        # Switch Apps
#   hotkey('command', 'space')      # Spotlight
#   hotkey('command', 'shift', '3') # Screenshot (full)
#   hotkey('command', 'shift', '4') # Screenshot (selection)
#
# ======================================================================
# ======================================================================
