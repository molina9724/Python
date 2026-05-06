import pypdf
import pdfminer.high_level

reader = pypdf.PdfReader(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter17/Recursion_Chapter1.pdf"
)
print(len(reader.pages))
print(reader.pages)

PDF_FILENAME = (
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter17/Recursion_Chapter1.pdf"
)
TEXT_FILE = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter17/recursion.txt"
text = ""

try:
    reader = pypdf.PdfReader(PDF_FILENAME)
    for page in reader.pages:
        text += page.extract_text()
except Exception:
    text = pdfminer.high_level.extract_text(PDF_FILENAME)
with open(TEXT_FILE, "w") as file:
    file.write(text)

image_num = 0
for i, page in enumerate(reader.pages):
    print(f"Reading page {i+1} - {len(page.images)} images found...")
    try:
        for image in page.images:
            with open(
                f"/Users/daniel_molina/Downloads/Python/Python/Book/chapter17/{image_num}_page{i+1}_{image.name}",
                "wb",
            ) as file:
                file.write(image.data)
            print(f"Wrote {image_num}_page{i+1}_{image.name}...")
            image_num += 1
    except Exception as e:
        print(f"Skipped page {i+1} due to error {e}")
