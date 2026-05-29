# ======================================================================
# 🔍 RECOGNIZING TEXT IN IMAGES (OCR) EXERCISES
# ======================================================================
# Practice exercises - Write everything from scratch!
# Prerequisites: tesseract installed, pytesseract and pillow packages
# ======================================================================

# pip install pytesseract pillow

import pytesseract as tess
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps

# =====================================================================
#                    SECTION 1: PYTESSERACT BASICS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 1: INSTALL AND VERIFY TESSERACT
#
# Learn: Installing Tesseract OCR engine
#
# Tasks:
# 1. Install Tesseract on your system:
#    - Windows: Download from UB-Mannheim GitHub, add to PATH
#    - macOS: brew install tesseract
#    - Linux: sudo apt install tesseract-ocr
# 2. Install pytesseract: pip install pytesseract
# 3. Import pytesseract as tess
# 4. Verify installation by importing without errors
# 5. On Windows, you may need to set tess.pytesseract.tesseract_cmd
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟢 2: EXTRACT TEXT FROM AN IMAGE
#
# Learn: tess.image_to_string(), Image.open()
#
# Tasks:
# 1. Import pytesseract as tess and Image from PIL
# 2. Open an image containing text with Image.open()
# 3. Pass the image to tess.image_to_string()
# 4. Print the extracted text
# 5. Observe how accurately the text was recognized
# ----------------------------------------------------------------------

image = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/frankenstein.png"
)
text = tess.image_to_string(image, lang="eng")
print(text)

# ----------------------------------------------------------------------
# 🟢 3: CREATE A TEST IMAGE WITH TEXT
#
# Learn: Creating images for OCR testing
#
# Tasks:
# 1. Use Pillow to create a new white image
# 2. Use ImageDraw to add black text to the image
# 3. Save the image
# 4. Run OCR on your created image
# 5. Verify the text was recognized correctly
# ----------------------------------------------------------------------

image = Image.new("RGBA", (1920, 1080), color="white")

draw = ImageDraw.Draw(image)
draw.text((0, 0), "Look at me", fill="black")
draw.text((0, 1069), "Here I am", fill="black")
# image.show()

text = tess.image_to_string(image)
print(text)

# ----------------------------------------------------------------------
# 🟢 4: CHECK INSTALLED LANGUAGES
#
# Learn: tess.get_languages()
#
# Tasks:
# 1. Call tess.get_languages() to see installed language packs
# 2. Print the list of available languages
# 3. Note that 'eng' is English (default)
# 4. Check if any non-English languages are installed
# 5. Understand the three-letter ISO 639 language codes
# ----------------------------------------------------------------------

print(tess.get_languages())

# ----------------------------------------------------------------------
# 🟡 5: EXTRACT TEXT FROM A SCREENSHOT
#
# Learn: OCR on screenshots
#
# Tasks:
# 1. Take a screenshot of some text on your screen
# 2. Save the screenshot as an image file
# 3. Open the screenshot with Pillow
# 4. Extract text using pytesseract
# 5. Compare the extracted text to the original
# 6. Note any errors or differences
# ----------------------------------------------------------------------

image = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/screenshot.png"
)
text = tess.image_to_string(image)
print(text)

# =====================================================================
#                    SECTION 2: IMAGE PREPROCESSING
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 6: CONVERT IMAGE TO GRAYSCALE
#
# Learn: Image.convert('L')
#
# Tasks:
# 1. Open a color image containing text
# 2. Convert to grayscale: img.convert('L')
# 3. Run OCR on both original and grayscale
# 4. Compare the results
# 5. Grayscale often improves OCR accuracy
# ----------------------------------------------------------------------

image = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/frankenstein.png",
)
greyscale = image.convert("L")
# greyscale.show()

text = tess.image_to_string(greyscale)
print(text)

# ----------------------------------------------------------------------
# 🟡 7: ADJUST BRIGHTNESS AND CONTRAST
#
# Learn: ImageEnhance.Brightness, ImageEnhance.Contrast
#
# Tasks:
# 1. Open an image with faded or low-contrast text
# 2. Increase contrast: ImageEnhance.Contrast(img).enhance(2.0)
# 3. Adjust brightness if needed
# 4. Run OCR on original and enhanced versions
# 5. Compare which produces better results
# ----------------------------------------------------------------------

copy = image.convert("RGB")

more_contrast = ImageEnhance.Contrast(copy).enhance(2)
text = tess.image_to_string(more_contrast)
# more_contrast.show()
print(text)

# ----------------------------------------------------------------------
# 🟡 8: RESIZE IMAGE FOR BETTER OCR
#
# Learn: Image.resize() for OCR improvement
#
# Tasks:
# 1. Open a small image with text
# 2. Resize to 2x or 3x the original size
# 3. Use Image.LANCZOS resampling for quality
# 4. Run OCR on original and resized versions
# 5. Note if larger images produce better results
# ----------------------------------------------------------------------

resize = copy.crop((91, 89, 986, 664))
# resize.show()

width, height = resize.size

high = resize.resize((width * 2, height * 2), Image.LANCZOS)
text = tess.image_to_string(high)
print("----------------------------------")
print(text)

# high.show()

# ----------------------------------------------------------------------
# 🟡 9: CONVERT TO BLACK AND WHITE
#
# Learn: Image.convert('1'), thresholding
#
# Tasks:
# 1. Open an image with text
# 2. Convert to pure black and white: img.convert('1')
# 3. Alternatively, use ImageOps.autocontrast() first
# 4. Run OCR on the black and white version
# 5. Compare with grayscale results
# ----------------------------------------------------------------------

black = copy.convert("1")
# black.show()

autocontrast = ImageOps.autocontrast(copy)
# autocontrast.show()

print("After autocontrast")
text = tess.image_to_string(autocontrast)
print(text)

# ----------------------------------------------------------------------
# 🟡 10: REMOVE NOISE WITH FILTERS
#
# Learn: ImageFilter for noise reduction
#
# Tasks:
# 1. Open a noisy image (or add noise to a clean one)
# 2. Apply median filter: img.filter(ImageFilter.MedianFilter(3))
# 3. Try Gaussian blur for smoothing
# 4. Run OCR before and after filtering
# 5. Find the best filter settings for your image
# ----------------------------------------------------------------------

median = copy.filter(ImageFilter.MedianFilter(3))
# median.show()

gaussian = copy.filter(ImageFilter.GaussianBlur(1.5))
# gaussian.show()

# ----------------------------------------------------------------------
# 🟡 11: INVERT COLORS
#
# Learn: ImageOps.invert()
#
# Tasks:
# 1. Create or find an image with white text on dark background
# 2. Tesseract prefers dark text on light background
# 3. Invert the image: ImageOps.invert(img)
# 4. Run OCR on both original and inverted
# 5. Compare the results
# ----------------------------------------------------------------------

black = Image.new("RGBA", (720, 480), color="black")

draw = ImageDraw.Draw(black)
draw.text((0, 0), "Hello there")
draw.text((100, 100), "How are you  today?")
draw.text((0, 340), "Doing well")
draw.text((480, 400), "That's my boy right theee")

# black.show()

black_copy = black.convert("RGB")

invert = ImageOps.invert(black_copy)
# invert.show()

print("------------------------------------")
text = tess.image_to_string(black)
print(text)
print("------------------------------------")

text = tess.image_to_string(invert)
print(text)

invert.save("/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/invert.png")

# ----------------------------------------------------------------------
# 🟡 12: CROP IMAGE TO TEXT REGION
#
# Learn: Image.crop() for focusing OCR
#
# Tasks:
# 1. Open an image with text in only part of it
# 2. Identify the coordinates of the text region
# 3. Crop to just the text area: img.crop((left, top, right, bottom))
# 4. Run OCR on the cropped image
# 5. Note how removing non-text areas improves results
# ----------------------------------------------------------------------

crop_image = invert.crop((478, 398, 600, 414))

text = tess.image_to_string(crop_image)
print(text)

# ----------------------------------------------------------------------
# 🟡 13: ADD BORDER/PADDING
#
# Learn: ImageOps.expand()
#
# Tasks:
# 1. Open an image where text runs to the edge
# 2. Add a white border: ImageOps.expand(img, border=20, fill='white')
# 3. Run OCR before and after adding the border
# 4. Compare results
# 5. Borders can help Tesseract recognize edge text
# ----------------------------------------------------------------------

# invert.show()

border = ImageOps.expand(invert, border=20, fill="red")
# border.show()

text = tess.image_to_string(border)
print("----------------------------------------")
print(text)

# ----------------------------------------------------------------------
# 🟡 14: ROTATE SKEWED TEXT
#
# Learn: Image.rotate() for alignment
#
# Tasks:
# 1. Create or find an image with slightly tilted text
# 2. Rotate the image to straighten the text
# 3. Use expand=True to prevent cropping
# 4. Run OCR before and after rotation
# 5. Note how alignment affects recognition accuracy
# ----------------------------------------------------------------------

rotated = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/image.png"
)

print("----------------------------------------")
text = tess.image_to_string(rotated)
print(text)

unrotating = rotated.rotate(-10, expand=True)
# unrotating.show()

text = tess.image_to_string(unrotating)
print(text)

# =====================================================================
#                    SECTION 3: ADVANCED OCR OPTIONS
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 15: SPECIFY LANGUAGE FOR OCR
#
# Learn: lang parameter
#
# Tasks:
# 1. Install a non-English language pack for Tesseract
# 2. Open an image with non-English text
# 3. Use lang parameter: tess.image_to_string(img, lang='deu')
# 4. Compare results with and without language specification
# 5. Try with wrong language to see the difference
# ----------------------------------------------------------------------

image = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/english_spanish.png"
)

text = tess.image_to_string(image, lang="spa+eng")
print(text)

text = tess.image_to_string(image, lang="jpn+afr+fra")
print(text)

# ----------------------------------------------------------------------
# 🟡 16: MULTIPLE LANGUAGES
#
# Learn: Combining languages with '+'
#
# Tasks:
# 1. Create or find an image with text in two languages
# 2. Specify both languages: lang='eng+fra'
# 3. Run OCR with combined language setting
# 4. Compare to single-language results
# 5. Note that order may matter for mixed-language text
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 17: GET BOUNDING BOXES
#
# Learn: tess.image_to_boxes()
#
# Tasks:
# 1. Open an image with text
# 2. Use tess.image_to_boxes(img) to get character positions
# 3. Parse the output to understand the format
# 4. Each line contains: character, x1, y1, x2, y2, page
# 5. Use this data to highlight recognized characters
# ----------------------------------------------------------------------

text = tess.image_to_boxes(image, "eng+spa")
print(text)
print(type(text))

data = text.split("\n")
print(data)

more_data = []

for row in data:
    more_data.append(row.split(" "))

print(more_data)

for row in more_data:
    if len(row) == 6:
        char, x1, y1, x2, y2, page = row
        print(char, x1, y1, x2, y2, page)
    else:
        print("Skipping row (bad format):", row)

# ----------------------------------------------------------------------
# 🟡 18: GET DETAILED DATA
#
# Learn: tess.image_to_data()
#
# Tasks:
# 1. Open an image with text
# 2. Use tess.image_to_data(img, output_type=tess.Output.DICT)
# 3. Explore the returned dictionary structure
# 4. Access word text, confidence levels, positions
# 5. Filter results by confidence threshold
# ----------------------------------------------------------------------

text = tess.image_to_data(image, "eng+spa", output_type=tess.Output.DICT)
print(text)

text_confidence = list()

for index in range(len(text["conf"])):
    if text["conf"][index] != -1:
        text_confidence.append((text["text"][index], text["conf"][index]))

print(text_confidence)

# ----------------------------------------------------------------------
# 🟡 19: CHECK CONFIDENCE LEVELS
#
# Learn: Confidence scores in OCR output
#
# Tasks:
# 1. Run image_to_data() on an image
# 2. Access the 'conf' (confidence) field
# 3. Print words with their confidence scores
# 4. Identify low-confidence words (potential errors)
# 5. Create a function that flags uncertain recognitions
# ----------------------------------------------------------------------

x: str = tess.image_to_data(image)
print(type(x))
print(x)

data = x.split("\n")
print(data)

import csv

reader = csv.DictReader(data, delimiter="\t")

low_conf = list()

for row in reader:
    if float(row["conf"]) < 95 and float(row["conf"]) != -1:
        low_conf.append([row["text"], row["conf"]])

print(low_conf)

# ----------------------------------------------------------------------
# 🟡 20: EXTRACT ONLY DIGITS
#
# Learn: config parameter, character whitelist
#
# Tasks:
# 1. Open an image containing numbers
# 2. Use config to limit to digits:
#    tess.image_to_string(img, config='digits')
# 3. Or use: config='--psm 6 -c tessedit_char_whitelist=0123456789'
# 4. Compare with unrestricted OCR
# 5. Useful for reading prices, phone numbers, etc.
# ----------------------------------------------------------------------

only_digits = Image.new("RGBA", (1920, 1080), color="white")

writer = ImageDraw.Draw(only_digits)
writer.text((0, 0), "123", fill="black")
writer.text((0, 500), "456", fill="black")
writer.text((0, 900), "789", fill="black")
writer.text((500, 0), "ABC", fill="black")
writer.text((900, 0), "DEF", fill="black")
writer.text((1500, 0), "G000H", fill="black")

# only_digits.show()

text = tess.image_to_string(only_digits)
print(text)

# =====================================================================
#                    SECTION 4: NAPS2 FOR PDF OCR
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 21: INSTALL AND LOCATE NAPS2
#
# Learn: NAPS2 installation
#
# Tasks:
# 1. Download NAPS2 from https://www.naps2.com/download
# 2. Install for your operating system
# 3. Find the path to NAPS2 executable:
#    - Windows: C:\Program Files\NAPS2\NAPS2.Console.exe
#    - macOS: /Applications/NAPS2.app/Contents/MacOS/NAPS2
#    - Linux: flatpak run com.naps2.Naps2
# 4. Store the path in a variable for later use
# 5. Test that the path is correct
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 22: CREATE PDF FROM IMAGE WITH OCR
#
# Learn: subprocess.run() with NAPS2
#
# Tasks:
# 1. Import subprocess module
# 2. Set up the NAPS2 path for your OS
# 3. Run NAPS2 with: -i input.png -o output.pdf --ocrlang eng
# 4. Add -n 0 to skip scanner, -f to force overwrite
# 5. Verify the PDF was created with searchable text
# ----------------------------------------------------------------------

import subprocess

NAPS2_PATH = "/Applications/NAPS2.app/Contents/MacOS/NAPS2"
INPUT = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/invert.png"
OUTPUT = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/my_ps2.pdf"

# fmt: off

command = [
    NAPS2_PATH,
    "console",
    "-i", INPUT,
    "-o", OUTPUT,
    "-n", "0",
    "-f",
    "-v"
]

# fmt: on

proc = subprocess.run(command, capture_output=False)

# ----------------------------------------------------------------------
# 🟡 23: INSTALL OCR LANGUAGE PACK VIA NAPS2
#
# Learn: --install argument
#
# Tasks:
# 1. Use --install ocr-eng to install English OCR
# 2. Try installing other languages: ocr-fra, ocr-deu, etc.
# 3. The installation happens automatically if not present
# 4. Include this in your script for portability
# 5. Note: Only needs to run once per language
# ----------------------------------------------------------------------


# fmt: off

command = [
    NAPS2_PATH,
    "console",
    "-i", INPUT,
    "-o", OUTPUT,
    "--install", "ocr-spa",
    # "--ocrlang", "ocr-spa"
    "-n", "0",
    "-f",
    "-v"
]

# fmt: on

proc = subprocess.run(command, capture_output=False)

# ----------------------------------------------------------------------
# 🟡 24: COMBINE MULTIPLE IMAGES INTO PDF
#
# Learn: Multiple inputs with semicolon separator
#
# Tasks:
# 1. Prepare several image files
# 2. Use -i with semicolon-separated filenames:
#    '-i', 'page1.png;page2.png;page3.png'
# 3. Run NAPS2 to create a multi-page PDF
# 4. Verify all pages are in the output PDF
# 5. Check that OCR text is searchable on all pages
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 25: SELECT SPECIFIC PDF PAGES
#
# Learn: Page selection with slice notation
#
# Tasks:
# 1. Use an existing multi-page PDF as input
# 2. Select first page: '-i', 'document.pdf[0]'
# 3. Select range: '-i', 'document.pdf[0:3]'
# 4. Select from end: '-i', 'document.pdf[-1]'
# 5. Combine selections from multiple PDFs
# ----------------------------------------------------------------------

INPUT = (
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter17/first_five_pages.pdf"
)

OUTPUT = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/exercise25.pdf"

# fmt: off

command = [
    NAPS2_PATH,
    "console",
    "-i", "/Users/daniel_molina/Downloads/Python/Python/Book/chapter17/first_five_pages.pdf[0];/Users/daniel_molina/Downloads/Python/Python/Book/chapter17/first_five_pages.pdf[1]",
    "-o", OUTPUT,
    "-n", "0",
    "-f",
    "-v",
]

# fmt: on

proc = subprocess.run(command, capture_output=True)
print(command)

# ----------------------------------------------------------------------
# 🟡 26: CAPTURE NAPS2 OUTPUT
#
# Learn: capture_output and verbose mode
#
# Tasks:
# 1. Run NAPS2 with -v (verbose) flag
# 2. Use capture_output=True in subprocess.run()
# 3. Access proc.stdout and proc.stderr
# 4. Decode bytes to string: proc.stdout.decode()
# 5. Parse output to track progress or errors
# ----------------------------------------------------------------------

wrong_command = [
    NAPS2_PATH,
    "console",
    "-i",
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter17/first_five_pages.pdf[0];/Users/daniel_molina/Downloads/Python/Python/Book/chapter17/first_five_pages.pdf[1]",
    "-o",
    OUTPUT,
    "-n",
    "0",
    "-f",
    "-v",
    "-non_existant_flag!!!",
]
proc = subprocess.run(wrong_command, capture_output=True)

xxx = proc.stdout.decode(encoding="utf-8")
yyy = proc.stderr.decode(encoding="utf-8")

print("-----------------------------------")

print(xxx)
print(yyy)

# =====================================================================
#                    SECTION 5: ERROR HANDLING AND CLEANUP
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 27: HANDLE OCR ERRORS
#
# Learn: Try/except for OCR operations
#
# Tasks:
# 1. Try to run OCR on a non-image file
# 2. Catch the exception that occurs
# 3. Try OCR on a corrupted image
# 4. Create a safe_ocr() function with error handling
# 5. Return empty string or error message on failure
# ----------------------------------------------------------------------

non_image = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/exercises.py"

try:
    data = tess.image_to_string(non_image)
    print(data)
except tess.pytesseract.TesseractError:
    print("This shit is going to blow up")


# ----------------------------------------------------------------------
# 🟡 28: VALIDATE IMAGE BEFORE OCR
#
# Learn: Checking image properties
#
# Tasks:
# 1. Create a function that validates images before OCR
# 2. Check if file exists
# 3. Check if it's a valid image format
# 4. Check minimum size (very small images won't OCR well)
# 5. Return boolean or raise descriptive error
# ----------------------------------------------------------------------

from pathlib import Path

valid_formats = [".png", ".jpg"]
file = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/english_spanish.png"


def validate_image(file_path: str):
    path_file = Path(file_path)

    if path_file.exists():
        if path_file.suffix in valid_formats:
            image = Image.open(file_path)
            return image.size
        else:
            return f"Wrong format, supported formats: {valid_formats}"
    else:
        return "File doesn't exist"


print(validate_image(file))
print(validate_image("non existing file"))
print(
    validate_image(
        "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/exercises2.py"
    )
)


# ----------------------------------------------------------------------
# 🟡 29: CLEAN UP OCR TEXT
#
# Learn: Post-processing OCR output
#
# Tasks:
# 1. Run OCR and get raw text
# 2. Remove extra whitespace: ' '.join(text.split())
# 3. Remove empty lines
# 4. Fix common OCR errors (e.g., 'l' vs '1', 'O' vs '0')
# 5. Create a clean_ocr_text() function
# ----------------------------------------------------------------------

data = tess.image_to_string(file)
print(data)

# ----------------------------------------------------------------------
# 🟡 30: REMOVE HYPHENATION
#
# Learn: Fixing line-break hyphens
#
# Tasks:
# 1. OCR often preserves end-of-line hyphenation
# 2. Find patterns like "word-\n" followed by continuation
# 3. Use regex to rejoin hyphenated words
# 4. Handle cases where hyphen is legitimate
# 5. Test with multi-line text blocks
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 6: BATCH PROCESSING
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 31: OCR MULTIPLE IMAGES
#
# Learn: Processing a folder of images
#
# Tasks:
# 1. Get list of all image files in a folder
# 2. Loop through each image
# 3. Run OCR on each image
# 4. Save extracted text to corresponding .txt files
# 5. Report progress and any errors
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 32: CREATE SEARCHABLE PDF FROM FOLDER
#
# Learn: Batch PDF creation with NAPS2
#
# Tasks:
# 1. Get all images in a folder sorted by name
# 2. Build the -i argument with semicolons
# 3. Run NAPS2 to create a single PDF
# 4. Handle folders with many images (command line limits)
# 5. Verify the PDF page order matches file order
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 33: PARALLEL OCR PROCESSING
#
# Learn: Using threading for faster OCR
#
# Tasks:
# 1. Import threading module
# 2. Create a function to OCR a single image
# 3. Create threads for multiple images
# 4. Store results in a thread-safe way
# 5. Compare time with sequential processing
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 7: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 34: RECEIPT SCANNER
#
# Scenario: Extract text from receipt photos
#
# Tasks:
# 1. Open a receipt image
# 2. Preprocess: convert to grayscale, increase contrast
# 3. Run OCR to extract text
# 4. Parse the text to find:
#    - Store name
#    - Date
#    - Items and prices
#    - Total amount
# 5. Handle common receipt OCR challenges
# 6. Output structured data (dict or JSON)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 35: BUSINESS CARD READER
#
# Scenario: Extract contact info from business cards
#
# Tasks:
# 1. Open a business card image
# 2. Preprocess appropriately
# 3. Run OCR to extract all text
# 4. Use regex to identify:
#    - Name
#    - Phone numbers
#    - Email addresses
#    - Website URLs
# 5. Handle multiple phone/email formats
# 6. Return structured contact information
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 36: DOCUMENT DIGITIZER
#
# Scenario: Convert paper documents to searchable PDFs
#
# Tasks:
# 1. Accept a folder of scanned document images
# 2. Preprocess each image for optimal OCR
# 3. Use NAPS2 to create searchable PDF
# 4. Organize output PDFs by date or category
# 5. Generate a summary report of processed documents
# 6. Handle errors and log problematic files
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 37: SCREENSHOT TEXT EXTRACTOR
#
# Scenario: Extract text from a screen region
#
# Tasks:
# 1. Use pyautogui to take a screenshot
# 2. Define coordinates for the text region
# 3. Crop the screenshot to the region
# 4. Run OCR on the cropped image
# 5. Optionally copy result to clipboard with pyperclip
# 6. Create a reusable function with configurable region
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 38: PDF TEXT EXTRACTOR
#
# Scenario: Extract text from scanned PDFs
#
# Tasks:
# 1. Convert PDF pages to images (use pdf2image or similar)
# 2. Process each page image
# 3. Run OCR on each page
# 4. Combine all text with page markers
# 5. Save to a text file
# 6. Handle multi-page documents efficiently
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 39: MULTILINGUAL DOCUMENT PROCESSOR
#
# Scenario: Handle documents with multiple languages
#
# Tasks:
# 1. Create a function that detects likely languages
# 2. Use multiple language packs in OCR
# 3. Process document sections separately if needed
# 4. Combine results maintaining document structure
# 5. Flag sections with low confidence
# 6. Allow user to specify expected languages
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 40: OCR QUALITY CHECKER
#
# Scenario: Assess and report OCR quality
#
# Tasks:
# 1. Run OCR with detailed output (image_to_data)
# 2. Calculate average confidence score
# 3. Count words below confidence threshold
# 4. Identify problem areas in the image
# 5. Generate a quality report
# 6. Suggest preprocessing improvements based on results
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 41: TABLE EXTRACTOR
#
# Scenario: Extract tabular data from images
#
# Tasks:
# 1. Open an image containing a table
# 2. Use image_to_data() to get positions
# 3. Group text by row (similar Y coordinates)
# 4. Group text by column (similar X coordinates)
# 5. Reconstruct the table structure
# 6. Output as CSV or list of lists
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 42: CAPTCHA READER (EDUCATIONAL)
#
# Scenario: Understand OCR limitations with distorted text
#
# Tasks:
# 1. Create a simple distorted text image
# 2. Try various preprocessing techniques
# 3. Run OCR and note the poor results
# 4. Understand why CAPTCHAs defeat OCR
# 5. Document what makes text hard to OCR
# 6. Note: This is for learning, not bypassing security!
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 43: BOOK PAGE SCANNER
#
# Scenario: Digitize book pages to text
#
# Tasks:
# 1. Open scanned book page images
# 2. Detect and remove dark borders
# 3. Handle two-column layouts (process separately)
# 4. Remove page numbers and headers/footers
# 5. Rejoin hyphenated words
# 6. Output clean, flowing text
# 7. Process multiple pages maintaining order
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 44: LICENSE PLATE READER (SIMPLIFIED)
#
# Scenario: Extract text from cropped plate images
#
# Tasks:
# 1. Start with a pre-cropped license plate image
# 2. Convert to grayscale
# 3. Apply thresholding for high contrast
# 4. Resize to larger dimensions
# 5. Use character whitelist for plate characters
# 6. Note: Real plate reading requires image detection
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 45: OCR PREPROCESSING PIPELINE
#
# Scenario: Create a customizable preprocessing system
#
# Tasks:
# 1. Create functions for each preprocessing step
# 2. Allow users to specify which steps to apply
# 3. Apply steps in optimal order
# 4. Compare OCR results with different combinations
# 5. Find the best pipeline for a given image type
# 6. Save and reuse successful pipelines
# ----------------------------------------------------------------------


# ======================================================================
# 🔍 QUICK REFERENCE - PyTesseract Basics
# ======================================================================
#
# Installation:
#   1. Install Tesseract OCR engine on your system
#   2. pip install pytesseract pillow
#
# Import:
#   import pytesseract as tess
#   from PIL import Image
#
# Basic OCR:
#   img = Image.open('image.png')
#   text = tess.image_to_string(img)
#
# Windows path (if needed):
#   tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
# Check languages:
#   tess.get_languages()           # Returns list of installed languages
#
# ======================================================================


# ======================================================================
# 🔍 QUICK REFERENCE - OCR Options
# ======================================================================
#
# Specify language:
#   tess.image_to_string(img, lang='eng')     # English (default)
#   tess.image_to_string(img, lang='deu')     # German
#   tess.image_to_string(img, lang='fra')     # French
#   tess.image_to_string(img, lang='jpn')     # Japanese
#   tess.image_to_string(img, lang='eng+fra') # Multiple languages
#
# Get detailed data:
#   tess.image_to_boxes(img)       # Character positions
#   tess.image_to_data(img)        # Detailed word info
#   tess.image_to_data(img, output_type=tess.Output.DICT)
#
# Configuration:
#   tess.image_to_string(img, config='digits')
#   tess.image_to_string(img, config='--psm 6')
#   tess.image_to_string(img, config='-c tessedit_char_whitelist=ABC123')
#
# ======================================================================


# ======================================================================
# 🔍 QUICK REFERENCE - Image Preprocessing
# ======================================================================
#
# Grayscale:
#   img = img.convert('L')
#
# Black and white:
#   img = img.convert('1')
#
# Resize (enlarge small images):
#   img = img.resize((width * 2, height * 2), Image.LANCZOS)
#
# Contrast:
#   from PIL import ImageEnhance
#   enhancer = ImageEnhance.Contrast(img)
#   img = enhancer.enhance(2.0)
#
# Brightness:
#   enhancer = ImageEnhance.Brightness(img)
#   img = enhancer.enhance(1.5)
#
# Invert (for white text on dark):
#   from PIL import ImageOps
#   img = ImageOps.invert(img)
#
# Add border:
#   img = ImageOps.expand(img, border=20, fill='white')
#
# Noise reduction:
#   img = img.filter(ImageFilter.MedianFilter(3))
#
# Crop:
#   img = img.crop((left, top, right, bottom))
#
# Rotate:
#   img = img.rotate(angle, expand=True, fillcolor='white')
#
# ======================================================================


# ======================================================================
# 🔍 QUICK REFERENCE - NAPS2 Command Line
# ======================================================================
#
# Basic PDF creation:
#   subprocess.run([naps2_path, '-i', 'input.png', '-o', 'output.pdf',
#                   '--ocrlang', 'eng', '-n', '0', '-f'])
#
# Arguments:
#   -i input           Input file(s)
#   -o output.pdf      Output PDF filename
#   --install ocr-eng  Install language pack (if needed)
#   --ocrlang eng      OCR language (eng, fra, deu, etc.)
#   -n 0               No scanner scans (use 0 for images only)
#   -f                 Force overwrite existing file
#   -v                 Verbose output
#
# Multiple inputs:
#   '-i', 'page1.png;page2.png;page3.png'
#
# PDF page selection:
#   '-i', 'doc.pdf[0]'           # First page
#   '-i', 'doc.pdf[0:3]'         # Pages 1-3
#   '-i', 'doc.pdf[-1]'          # Last page
#
# NAPS2 paths:
#   Windows: r'C:\Program Files\NAPS2\NAPS2.Console.exe'
#   macOS:   ['/Applications/NAPS2.app/Contents/MacOS/NAPS2', 'console']
#   Linux:   ['flatpak', 'run', 'com.naps2.Naps2', 'console']
#
# ======================================================================


# ======================================================================
# 🔍 QUICK REFERENCE - Common OCR Issues
# ======================================================================
#
# Problems that cause poor OCR:
#   - Low resolution images
#   - Skewed/rotated text
#   - White text on dark background
#   - Decorative or cursive fonts
#   - Handwritten text
#   - Multiple columns (text gets mixed)
#   - Noise, artifacts, stains
#   - Dark borders
#   - Text at image edges
#
# Solutions:
#   - Enlarge small images
#   - Rotate to straighten text
#   - Invert dark backgrounds
#   - Use standard fonts when possible
#   - Process columns separately
#   - Apply noise filters
#   - Crop out borders
#   - Add white padding
#   - Increase contrast
#
# ======================================================================


# ======================================================================
# 🔍 QUICK REFERENCE - Post-Processing OCR Text
# ======================================================================
#
# Remove extra whitespace:
#   text = ' '.join(text.split())
#
# Remove empty lines:
#   lines = [line for line in text.split('\n') if line.strip()]
#   text = '\n'.join(lines)
#
# Fix common OCR errors:
#   text = text.replace('|', 'l')     # Pipe to lowercase L
#   text = text.replace('0', 'O')     # Context-dependent!
#
# Remove hyphenation (basic):
#   import re
#   text = re.sub(r'-\n', '', text)   # Join hyphenated words
#
# Use LLM for cleanup:
#   - Feed OCR output to ChatGPT, Gemini, etc.
#   - Ask it to fix OCR errors while preserving content
#   - Always verify LLM output manually
#
# ======================================================================


# ======================================================================
# 🚀 SETUP INSTRUCTIONS
# ======================================================================
#
# 1. Install Tesseract OCR Engine:
#
#    Windows:
#      - Download from https://github.com/UB-Mannheim/tesseract/wiki
#      - Run installer
#      - Add to PATH: C:\Program Files\Tesseract-OCR
#
#    macOS:
#      brew install tesseract
#      brew install tesseract-lang    # For additional languages
#
#    Linux:
#      sudo apt install tesseract-ocr
#      sudo apt install tesseract-ocr-all  # For all languages
#
# 2. Install Python packages:
#    pip install pytesseract pillow
#
# 3. Test installation:
#    import pytesseract as tess
#    from PIL import Image
#    print(tess.get_languages())
#
# 4. Install NAPS2 (optional, for PDF creation):
#    Download from https://www.naps2.com/download
#
# 5. Sample images:
#    - Use screenshots of text
#    - Download from book resources
#    - Create with Pillow ImageDraw
#
# ===========================Víctor Muñoz===========================================
