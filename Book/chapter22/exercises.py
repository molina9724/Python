import pytesseract as tess
from PIL import Image, ImageDraw, ImageFont

print("hello")

FILE = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/ocr-example.png"

image = Image.open(FILE)
text = tess.image_to_string(image)

print(text)

image = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/frankenstein.png"
)
text = tess.image_to_string(image)
print(text)

print(tess.get_languages())

image = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/frankenstein_jpn.png"
)
text = tess.image_to_string(image, lang="jpn+eng")
print(text)

import subprocess

FILE_PATH = (
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/frankenstein_jpn.png"
)

# Construct the command for NAPS2 OCR in console mode for clarity.
naps2_executable = "/Applications/NAPS2.app/Contents/MacOS/NAPS2"
output_pdf = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter22/output.pdf"

# fmt: off

naps2_command = [
    naps2_executable,
    "console",  # console mode
    "-i", FILE_PATH,    # input
    "-o", output_pdf,   # output
    "--install", "ocr-eng",
    "--ocrlang", "eng",
    "-n", "0",
    "-f",   # override
    "-v",
]

# fmt: off

# Run the OCR command and capture output
proc = subprocess.run(
    naps2_command,
    capture_output=False,
)
