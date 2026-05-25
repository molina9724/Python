import pytesseract as tess
from PIL import Image

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
text = tess.image_to_string(image, lang="jpn")
print(text)
