# ======================================================================
# 📊 MAKING GRAPHS AND MANIPULATING IMAGES EXERCISES
# ======================================================================
# Practice exercises - Write everything from scratch!
# Prerequisites: matplotlib and pillow installed
# ======================================================================

# pip install matplotlib pillow

from PIL import Image, ImageColor, ImageDraw, ImageEnhance, ImageFilter, ImageFont

# =====================================================================
#                    SECTION 3: PILLOW BASICS - OPENING IMAGES
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 18: OPEN AND DISPLAY AN IMAGE
#
# Learn: Image.open(), show()
#
# Tasks:
# 1. Import Image from PIL
# 2. Open an image file with Image.open('filename.jpg')
# 3. Store the returned Image object
# 4. Display the image with .show()
# 5. The image opens in your default image viewer
# ----------------------------------------------------------------------

ROOT_FILE = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/zophie.png"
ROOT = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/"

image = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/zophie.png"
)
# image.show()

# ----------------------------------------------------------------------
# 🟢 19: GET IMAGE PROPERTIES
#
# Learn: size, width, height, format, mode attributes
#
# Tasks:
# 1. Open an image
# 2. Print the size attribute (returns tuple)
# 3. Print width and height separately
# 4. Print the format (JPEG, PNG, etc.)
# 5. Print the mode (RGB, RGBA, L for grayscale)
# ----------------------------------------------------------------------

print(image.size)
width, height = image.size
print(width)
print(height)
print(image.format)
print(image.mode)

image.close()

# ----------------------------------------------------------------------
# 🟢 20: SAVE AN IMAGE
#
# Learn: save() method
#
# Tasks:
# 1. Open an image
# 2. Save it with a new filename using .save('newname.png')
# 3. Save in a different format (e.g., JPEG to PNG)
# 4. Verify the new file was created
# 5. Note: Format is determined by file extension
# ----------------------------------------------------------------------

image = Image.open(ROOT_FILE)
image.save(ROOT + "my_saved_file.png")

# ----------------------------------------------------------------------
# 🟢 21: CREATE A NEW IMAGE
#
# Learn: Image.new()
#
# Tasks:
# 1. Create a new RGB image: Image.new('RGB', (width, height))
# 2. Specify a background color: Image.new('RGB', (200, 200), 'red')
# 3. Try different color names: 'blue', 'white', 'black'
# 4. Try RGB tuple: (255, 128, 0) for orange
# 5. Save your new image
# ----------------------------------------------------------------------

new_image = Image.new("RGB", (600, 600))

red = Image.new("RGBA", (250, 250), "red")
blue = Image.new("RGBA", (250, 250), "blue")
white = Image.new("RGBA", (250, 250), "white")
black = Image.new("RGBA", (250, 250), "black")

black.save(ROOT + "black.png")

# =====================================================================
#                    SECTION 4: IMAGE MANIPULATION
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 22: CROP AN IMAGE
#
# Learn: crop() method
#
# Tasks:
# 1. Open an image
# 2. Define a box tuple: (left, top, right, bottom)
# 3. Crop the image: cropped = image.crop(box)
# 4. Save the cropped image
# 5. Experiment with different crop regions
# 6. Remember: coordinates start at top-left (0, 0)
# ----------------------------------------------------------------------

black = Image.open(ROOT + "black.png")
small_black = black.crop((0, 0, 3, 3))

small_black.save(ROOT + "small_black.png")

# ----------------------------------------------------------------------
# 🟡 23: RESIZE AN IMAGE
#
# Learn: resize() method
#
# Tasks:
# 1. Open an image
# 2. Resize to specific dimensions: image.resize((new_width, new_height))
# 3. Resize to half the original size
# 4. Resize to double the size
# 5. Note: resize() doesn't preserve aspect ratio by default
# 6. Calculate new dimensions to preserve aspect ratio
# ----------------------------------------------------------------------

half = black.resize((450, 450))
double = black.resize((750, 750))

# ----------------------------------------------------------------------
# 🟡 24: RESIZE WITH ASPECT RATIO
#
# Learn: Calculating dimensions, thumbnail() method
#
# Tasks:
# 1. Open an image and get its dimensions
# 2. Calculate new height based on desired width (maintaining ratio)
# 3. Resize using calculated dimensions
# 4. Alternative: use thumbnail() which preserves aspect ratio
# 5. Note: thumbnail() modifies in place and only shrinks
# ----------------------------------------------------------------------

copy = Image.new("RGBA", (1920, 1080), color="red")

copy.thumbnail((1280, 720), reducing_gap=True)
print(copy.size)

# ----------------------------------------------------------------------
# 🟡 25: ROTATE AN IMAGE
#
# Learn: rotate() method
#
# Tasks:
# 1. Open an image
# 2. Rotate 90 degrees: image.rotate(90)
# 3. Rotate 180 degrees
# 4. Rotate 45 degrees (note the black corners)
# 5. Use expand=True to resize canvas for rotated image
# 6. Save rotated images
# ----------------------------------------------------------------------

copy.rotate(90)
copy.rotate(180)
copy.rotate(250)
# copy.rotate(285, expand=True)

# copy.show()

# ----------------------------------------------------------------------
# 🟡 26: FLIP AN IMAGE
#
# Learn: transpose() method
#
# Tasks:
# 1. Open an image
# 2. Flip horizontally: image.transpose(Image.FLIP_LEFT_RIGHT)
# 3. Flip vertically: image.transpose(Image.FLIP_TOP_BOTTOM)
# 4. Rotate 90°: image.transpose(Image.ROTATE_90)
# 5. Save and compare all transformations
# ----------------------------------------------------------------------

copy.transpose(Image.FLIP_LEFT_RIGHT)
copy.transpose(Image.FLIP_TOP_BOTTOM)
copy.transpose(Image.ROTATE_90)

# ----------------------------------------------------------------------
# 🟡 27: CONVERT IMAGE MODE
#
# Learn: convert() method
#
# Tasks:
# 1. Open a color image (RGB)
# 2. Convert to grayscale: image.convert('L')
# 3. Convert to RGBA (with alpha channel)
# 4. Convert to 1-bit black and white: image.convert('1')
# 5. Save and compare the different modes
# ----------------------------------------------------------------------

copy.convert("L")
copy.convert("RGBA")
copy.convert("1")

# =====================================================================
#                    SECTION 5: PIXEL MANIPULATION
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 28: GET PIXEL VALUES
#
# Learn: getpixel() method
#
# Tasks:
# 1. Open an image
# 2. Get the pixel at (0, 0): image.getpixel((0, 0))
# 3. The result is an RGB tuple like (255, 128, 64)
# 4. Get pixels at several different coordinates
# 5. Print the red, green, blue values separately
# ----------------------------------------------------------------------

print(image.size)

pixel = image.getpixel((0, 0))
print(pixel)

pixel = image.getpixel((100, 100))
print(pixel)

pixel = image.getpixel((24, 24))
print(pixel)

pixel = image.getpixel((808, 888))
print(pixel)

# ----------------------------------------------------------------------
# 🟡 29: SET PIXEL VALUES
#
# Learn: putpixel() method
#
# Tasks:
# 1. Open or create an image
# 2. Set a pixel to red: image.putpixel((x, y), (255, 0, 0))
# 3. Set several pixels in a row to create a line
# 4. Create a small pattern by setting multiple pixels
# 5. Save and view the result
# ----------------------------------------------------------------------

image = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/black.png"
)

# image.putpixel((0, 0), ImageColor.getrgb("white"))
# print(image.size)

# width, height = image.size
# all_colors = ImageColor.colormap
# all_colors = list(all_colors)
# print(len(all_colors))

# for x in range(width):
#     for y in range(height):
#         if x == y:
#             image.putpixel((x, y), ImageColor.getrgb("white"))
#         if x + y == 249:
#             image.putpixel((x, y), ImageColor.getrgb("red"))
#         if x > y:
#             image.putpixel((x, y), ImageColor.getrgb("yellow"))
#         if x > y + y:
#             image.putpixel((x, y), ImageColor.getrgb("orange"))
#         if x > y:
#             image.putpixel((x, y), ImageColor.getrgb(all_colors[x - 145]))

# print(all_colors)
# print(list(all_colors))

# image.save("/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/go_crazy.png")

# ----------------------------------------------------------------------
# 🟡 30: MODIFY PIXELS IN A LOOP
#
# Learn: Iterating through pixels
#
# Tasks:
# 1. Open a small image (or resize a large one)
# 2. Loop through all x and y coordinates
# 3. Get each pixel value
# 4. Modify it (e.g., increase red channel)
# 5. Put the modified pixel back
# 6. Note: This is slow for large images!
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 31: CREATE A GRADIENT IMAGE
#
# Learn: Creating images pixel by pixel
#
# Tasks:
# 1. Create a new blank image
# 2. Loop through each pixel
# 3. Calculate color based on position (e.g., x position = red value)
# 4. Create a horizontal gradient from black to white
# 5. Create a diagonal gradient with multiple colors
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 6: COPYING AND PASTING
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 32: COPY AND PASTE IMAGE REGIONS
#
# Learn: copy(), paste() methods
#
# Tasks:
# 1. Open an image
# 2. Crop a region to copy it
# 3. Paste it elsewhere: image.paste(cropped_region, (x, y))
# 4. Paste the same region multiple times
# 5. Create a tiled pattern by pasting repeatedly
# ----------------------------------------------------------------------

cat_image = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/zophie.png"
)

a_part = cat_image.crop((485, 419, 525, 459))

eyes = Image.new(
    "RGBA",
    (400, 400),
    color="white",
)

width, height = a_part.size
print(width, height)

size = 400
patch_size = a_part.width  # or .height, whichever is bigger
# For main diagonal
for d in range(-patch_size + 1, size):
    x, y = d, d
    eyes.paste(
        a_part,
        (x, y),
    )  # mask to respect transparency
# For anti-diagonal
for x in range(-patch_size + 1, size):
    y = 360 - x
    eyes.paste(
        a_part,
        (x, y),
    )

eyes.save("/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/eyes.png")


# ----------------------------------------------------------------------
# 🟡 33: PASTE WITH TRANSPARENCY
#
# Learn: paste() with mask parameter
#
# Tasks:
# 1. Open two images (one with transparency - PNG with alpha)
# 2. Get the alpha channel of the overlay image
# 3. Paste using the alpha as mask: base.paste(overlay, (x,y), overlay)
# 4. This preserves transparency
# 5. Experiment with different positions
# ----------------------------------------------------------------------

image_1 = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/zophie.jpg"
)
image_2 = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/catlogo.png"
)

alpha_channel = image_2.getchannel("A")

image_1.paste(image_2, (0, 0), image_2)
# image_1.show()


# ----------------------------------------------------------------------
# 🟡 34: COMBINE MULTIPLE IMAGES
#
# Learn: Creating collages
#
# Tasks:
# 1. Open several images
# 2. Create a new blank image large enough for all
# 3. Paste each image at calculated positions
# 4. Create a 2x2 grid of images
# 5. Save the combined image
# ----------------------------------------------------------------------

image_1 = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/zophie.jpg"
)
image_2 = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/catlogo.png"
)
image_3 = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/go_crazy.png"
)
image_4 = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/eyes.png"
)

width, height = image_1.size
print(width, height)


new_image = Image.new("RGBA", (1800, 1800))
new_image.paste(image_1, (0, 0))
new_image.paste(image_2, (816, 0))
new_image.paste(image_3, (0, 1088))
new_image.paste(image_4, (816, 1088))

# new_image.show()

new_image_2 = Image.new("RGBA", (480, 480))
image_1 = image_1.resize((240, 240))
image_2 = image_2.resize((240, 240))
image_3 = image_3.resize((240, 240))
image_4 = image_4.resize((240, 240))

new_image_2.paste(image_1, (0, 0))
new_image_2.paste(image_2, (240, 0))
new_image_2.paste(image_3, (0, 240))
new_image_2.paste(image_4, (240, 240))

# new_image_2.show()

# =====================================================================
#                    SECTION 7: DRAWING ON IMAGES
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 35: DRAW BASIC SHAPES
#
# Learn: ImageDraw module, line, rectangle, ellipse
#
# Tasks:
# 1. Import ImageDraw from PIL
# 2. Create or open an image
# 3. Create a draw object: draw = ImageDraw.Draw(image)
# 4. Draw a line: draw.line([(x1,y1), (x2,y2)], fill='red', width=2)
# 5. Draw a rectangle: draw.rectangle([x1,y1,x2,y2], outline='blue')
# 6. Draw an ellipse (circle): draw.ellipse([x1,y1,x2,y2], fill='green')
# ----------------------------------------------------------------------

image = Image.open(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/zophie.png"
)

print(image.size)

draw = ImageDraw.Draw(image)
draw.line(
    [
        (0, 0),
        (815, 1087),
    ],
    fill="red",
    width=5,
)

draw.line(
    [
        (815, 0),
        (0, 1087),
    ],
    fill="red",
    width=5,
)

draw.rectangle((387, 523, 427, 563), outline="blue", fill="black")
draw.circle((408, 543), 5, outline="yellow", width=5)

# image.show()

# ----------------------------------------------------------------------
# 🟡 36: DRAW POLYGONS AND ARCS
#
# Learn: polygon(), arc(), pieslice()
#
# Tasks:
# 1. Create a draw object
# 2. Draw a polygon: draw.polygon([(x1,y1), (x2,y2), (x3,y3)], fill='yellow')
# 3. Draw a triangle, pentagon, hexagon
# 4. Draw an arc: draw.arc([x1,y1,x2,y2], start=0, end=180, fill='red')
# 5. Draw a pie slice: draw.pieslice()
# ----------------------------------------------------------------------

draw.polygon([(387, 522), (407, 503), (427, 522)], fill="orange", width=5)
draw.polygon([(387, 564), (407, 584), (427, 564)], fill="orange", width=5)

draw.arc((428, 520, 478, 563), start=0, end=180, fill="white", width=5)

# image.show()

# ----------------------------------------------------------------------
# 🟡 37: ADD TEXT TO IMAGES
#
# Learn: ImageDraw.text(), ImageFont
#
# Tasks:
# 1. Create a draw object
# 2. Add text: draw.text((x, y), 'Hello World', fill='black')
# 3. The default font is small - let's use a custom font
# 4. Load a font: font = ImageFont.truetype('arial.ttf', size=36)
# 5. Add text with custom font: draw.text((x,y), 'Hello', font=font)
# 6. Note: Font file must exist on your system
# ----------------------------------------------------------------------

draw.text(
    (407, 0),
    "This is the center",
    fill="Black",
    align="left",
    font=ImageFont.truetype("SFNSItalic.ttf", 36),
)
draw.text(
    (407, 500),
    "Look at me!",
    fill="green",
    align="center",
    font=ImageFont.truetype("SFArmenian.ttf", 38),
)
# image.show()

# ----------------------------------------------------------------------
# 🟡 38: USE DEFAULT FONT WITH SIZE
#
# Learn: ImageFont.load_default()
#
# Tasks:
# 1. Load default font: font = ImageFont.load_default()
# 2. Draw text with default font
# 3. For newer Pillow: ImageFont.load_default(size=24)
# 4. Calculate text size for centering (if needed)
# 5. Create an image with centered text
# ----------------------------------------------------------------------


# =====================================================================
#                    SECTION 8: IMAGE FILTERS
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 39: APPLY BLUR FILTER
#
# Learn: ImageFilter module, BLUR, GaussianBlur
#
# Tasks:
# 1. Import ImageFilter from PIL
# 2. Open an image
# 3. Apply blur: image.filter(ImageFilter.BLUR)
# 4. Apply Gaussian blur with radius: ImageFilter.GaussianBlur(radius=5)
# 5. Save and compare different blur amounts
# ----------------------------------------------------------------------

blur = image.filter(ImageFilter.BLUR)
gauss = image.filter(ImageFilter.FIND_EDGES)
# gauss.show()

# ----------------------------------------------------------------------
# 🟡 40: APPLY SHARPEN AND DETAIL FILTERS
#
# Learn: SHARPEN, DETAIL, EDGE_ENHANCE
#
# Tasks:
# 1. Open a slightly blurry image
# 2. Apply sharpen: image.filter(ImageFilter.SHARPEN)
# 3. Apply detail: image.filter(ImageFilter.DETAIL)
# 4. Apply edge enhance: image.filter(ImageFilter.EDGE_ENHANCE)
# 5. Compare the results
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 41: APPLY CONTOUR AND EMBOSS
#
# Learn: CONTOUR, EMBOSS, FIND_EDGES
#
# Tasks:
# 1. Open an image
# 2. Apply contour: image.filter(ImageFilter.CONTOUR)
# 3. Apply emboss: image.filter(ImageFilter.EMBOSS)
# 4. Apply find edges: image.filter(ImageFilter.FIND_EDGES)
# 5. These create artistic effects - save and compare
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🟡 42: ADJUST BRIGHTNESS AND CONTRAST
#
# Learn: ImageEnhance module
#
# Tasks:
# 1. Import ImageEnhance from PIL
# 2. Create enhancer: enhancer = ImageEnhance.Brightness(image)
# 3. Adjust brightness: enhancer.enhance(1.5) for brighter
# 4. Use factor < 1 for darker, > 1 for brighter
# 5. Try ImageEnhance.Contrast(), ImageEnhance.Color()
# ----------------------------------------------------------------------

enhancer = ImageEnhance.Brightness(image)
# image = enhancer.enhance(0.5)

enhancer = ImageEnhance.Contrast(image)
# image = enhancer.enhance(2)

enhancer = ImageEnhance.Color(image)
# image = enhancer.enhance(2.5)

# image.show()

# =====================================================================
#                    SECTION 9: REAL-WORLD SCENARIOS
# =====================================================================


# ----------------------------------------------------------------------
# 🔴 43: SALES DATA VISUALIZATION
#
# Scenario: Create graphs from sales data
#
# Tasks:
# 1. Create sample sales data (months and amounts)
# 2. Create a line graph showing sales trend
# 3. Create a bar chart comparing monthly sales
# 4. Create a pie chart showing sales by category
# 5. Add proper titles, labels, and legends
# 6. Save all graphs as PNG files
# 7. Create a function that generates all graphs from data
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 44: IMAGE THUMBNAIL GENERATOR
#
# Scenario: Create thumbnails for a folder of images
#
# Tasks:
# 1. Get list of all image files in a folder
# 2. For each image, create a thumbnail (e.g., 128x128)
# 3. Maintain aspect ratio
# 4. Save thumbnails with prefix 'thumb_'
# 5. Handle different image formats
# 6. Skip files that aren't images
# 7. Report how many thumbnails were created
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 45: ADD WATERMARK TO IMAGES
#
# Scenario: Add a text watermark to photos
#
# Tasks:
# 1. Open an image
# 2. Create a text watermark (e.g., "© 2024 Your Name")
# 3. Position it in the corner
# 4. Make it semi-transparent
# 5. Use a reasonable font size based on image size
# 6. Process multiple images in a folder
# 7. Save watermarked images with new names
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 46: IMAGE COLLAGE MAKER
#
# Scenario: Create a photo collage
#
# Tasks:
# 1. Accept a list of image filenames
# 2. Determine grid size (e.g., 2x3 for 6 images)
# 3. Resize all images to the same dimensions
# 4. Create a new image large enough for the grid
# 5. Paste images in grid positions
# 6. Add optional spacing/borders between images
# 7. Save the final collage
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 47: GRAPH DASHBOARD
#
# Scenario: Create a multi-graph dashboard image
#
# Tasks:
# 1. Create multiple graphs using subplots
# 2. Include: line chart, bar chart, pie chart, scatter plot
# 3. Use consistent styling across all graphs
# 4. Add a main title for the dashboard
# 5. Save as a single image file
# 6. Make it suitable for a presentation
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 48: BATCH IMAGE PROCESSOR
#
# Scenario: Apply transformations to multiple images
#
# Tasks:
# 1. Create a function that applies a series of transformations
# 2. Transformations: resize, convert to grayscale, add border
# 3. Process all images in a folder
# 4. Save processed images to an output folder
# 5. Handle errors for corrupted images
# 6. Log all processing steps
# 7. Report statistics (processed, failed, skipped)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 49: MEME GENERATOR
#
# Scenario: Add top and bottom text to images
#
# Tasks:
# 1. Open a base image
# 2. Add white text with black outline at top
# 3. Add white text with black outline at bottom
# 4. Use a bold, impact-style font
# 5. Auto-size text to fit image width
# 6. Create function: make_meme(image, top_text, bottom_text)
# 7. Handle long text (word wrap or shrink)
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 50: DATA-DRIVEN IMAGE GENERATION
#
# Scenario: Generate images from data
#
# Tasks:
# 1. Read data from a CSV file (e.g., product info)
# 2. Create product cards as images
# 3. Include: product name, price, description
# 4. Add a placeholder image or icon
# 5. Generate multiple product cards
# 6. Create a catalog page combining all cards
# 7. Save individual cards and the combined catalog
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 51: CHART IMAGE EXPORTER
#
# Scenario: Create a module for easy chart creation
#
# Tasks:
# 1. Create functions for each chart type:
#    - create_line_chart(data, title, filename)
#    - create_bar_chart(data, title, filename)
#    - create_pie_chart(data, title, filename)
# 2. Add consistent styling to all functions
# 3. Handle various data formats (lists, dicts)
# 4. Add error handling for invalid data
# 5. Return success/failure status
# 6. Create a demo that uses all functions
# ----------------------------------------------------------------------


# ----------------------------------------------------------------------
# 🔴 52: IMAGE COMPARISON TOOL
#
# Scenario: Create side-by-side image comparisons
#
# Tasks:
# 1. Open two images
# 2. Resize both to the same height (preserve aspect ratio)
# 3. Create a new image combining them side by side
# 4. Add labels below each image
# 5. Add a dividing line between them
# 6. Create function: compare_images(img1, img2, label1, label2)
# 7. Support before/after comparisons
# ----------------------------------------------------------------------


# ======================================================================
# 📊 QUICK REFERENCE - Matplotlib Basics
# ======================================================================
#
# Import:
#   import matplotlib.pyplot as plt
#
# Basic plotting:
#   plt.plot(x, y)                    # Line graph
#   plt.bar(x, y)                     # Bar chart
#   plt.barh(x, y)                    # Horizontal bar chart
#   plt.scatter(x, y)                 # Scatter plot
#   plt.pie(values, labels=labels)   # Pie chart
#   plt.hist(data, bins=10)          # Histogram
#
# Display and save:
#   plt.show()                        # Display graph
#   plt.savefig('filename.png')       # Save to file
#
# Labels and title:
#   plt.title('Title')
#   plt.xlabel('X Label')
#   plt.ylabel('Y Label')
#   plt.legend(['Line 1', 'Line 2'])
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - Matplotlib Customization
# ======================================================================
#
# Line customization:
#   plt.plot(x, y, color='red')
#   plt.plot(x, y, linestyle='--')    # dashed
#   plt.plot(x, y, linestyle=':')     # dotted
#   plt.plot(x, y, linewidth=2)
#   plt.plot(x, y, marker='o')        # circle markers
#   plt.plot(x, y, marker='s')        # square markers
#
# Axis limits:
#   plt.xlim(0, 10)
#   plt.ylim(0, 100)
#   plt.axis([xmin, xmax, ymin, ymax])
#
# Grid and ticks:
#   plt.grid(True)
#   plt.xticks([0, 1, 2], ['A', 'B', 'C'])
#   plt.yticks(rotation=45)
#
# Figure size:
#   plt.figure(figsize=(10, 6))       # Width, height in inches
#
# Styles:
#   plt.style.use('seaborn-v0_8')
#   print(plt.style.available)        # List all styles
#
# ======================================================================


# ======================================================================
# 📊 QUICK REFERENCE - Matplotlib Subplots
# ======================================================================
#
# Using subplot:
#   plt.subplot(rows, cols, index)    # index starts at 1
#   plt.subplot(2, 1, 1)              # First of 2 rows
#   plt.plot(x, y)
#   plt.subplot(2, 1, 2)              # Second of 2 rows
#   plt.plot(x, z)
#
# Using subplots (recommended):
#   fig, axes = plt.subplots(2, 2)    # 2x2 grid
#   axes[0, 0].plot(x, y)
#   axes[0, 1].bar(x, y)
#   axes[1, 0].scatter(x, y)
#   axes[1, 1].pie(values)
#
# Prevent overlap:
#   plt.tight_layout()
#
# ======================================================================


# ======================================================================
# 🖼️ QUICK REFERENCE - Pillow Basics
# ======================================================================
#
# Import:
#   from PIL import Image
#
# Open and save:
#   img = Image.open('photo.jpg')
#   img.save('new_photo.png')
#
# Create new image:
#   img = Image.new('RGB', (width, height), 'white')
#   img = Image.new('RGB', (200, 200), (255, 0, 0))  # Red
#
# Image properties:
#   img.size                          # (width, height) tuple
#   img.width                         # Width in pixels
#   img.height                        # Height in pixels
#   img.format                        # 'JPEG', 'PNG', etc.
#   img.mode                          # 'RGB', 'RGBA', 'L', etc.
#
# Display:
#   img.show()                        # Opens in default viewer
#
# ======================================================================


# ======================================================================
# 🖼️ QUICK REFERENCE - Pillow Transformations
# ======================================================================
#
# Resize:
#   img.resize((new_width, new_height))
#   img.thumbnail((max_width, max_height))  # Preserves ratio, in-place
#
# Crop (left, top, right, bottom):
#   img.crop((100, 100, 400, 400))
#
# Rotate:
#   img.rotate(90)                    # 90 degrees counter-clockwise
#   img.rotate(45, expand=True)       # Expand canvas for corners
#
# Flip/Transpose:
#   img.transpose(Image.FLIP_LEFT_RIGHT)
#   img.transpose(Image.FLIP_TOP_BOTTOM)
#   img.transpose(Image.ROTATE_90)
#   img.transpose(Image.ROTATE_180)
#   img.transpose(Image.ROTATE_270)
#
# Convert mode:
#   img.convert('L')                  # Grayscale
#   img.convert('RGB')                # Color
#   img.convert('RGBA')               # Color with alpha
#
# ======================================================================


# ======================================================================
# 🖼️ QUICK REFERENCE - Pillow Pixels
# ======================================================================
#
# Get pixel:
#   pixel = img.getpixel((x, y))      # Returns (R, G, B) tuple
#   red, green, blue = pixel
#
# Set pixel:
#   img.putpixel((x, y), (255, 0, 0)) # Set to red
#
# Copy and paste:
#   region = img.crop((0, 0, 100, 100))
#   img.paste(region, (200, 200))
#   img.paste(overlay, (x, y), overlay)  # With transparency mask
#
# ======================================================================


# ======================================================================
# 🖼️ QUICK REFERENCE - Pillow Drawing
# ======================================================================
#
# Import:
#   from PIL import ImageDraw, ImageFont
#
# Create draw object:
#   draw = ImageDraw.Draw(img)
#
# Draw shapes:
#   draw.line([(x1,y1), (x2,y2)], fill='red', width=2)
#   draw.rectangle([x1, y1, x2, y2], fill='blue', outline='black')
#   draw.ellipse([x1, y1, x2, y2], fill='green')
#   draw.polygon([(x1,y1), (x2,y2), (x3,y3)], fill='yellow')
#   draw.arc([x1, y1, x2, y2], start=0, end=180, fill='red')
#
# Draw text:
#   draw.text((x, y), 'Hello', fill='black')
#   font = ImageFont.truetype('arial.ttf', 36)
#   draw.text((x, y), 'Hello', fill='white', font=font)
#
# ======================================================================


# ======================================================================
# 🖼️ QUICK REFERENCE - Pillow Filters
# ======================================================================
#
# Import:
#   from PIL import ImageFilter, ImageEnhance
#
# Apply filters:
#   img.filter(ImageFilter.BLUR)
#   img.filter(ImageFilter.GaussianBlur(radius=5))
#   img.filter(ImageFilter.SHARPEN)
#   img.filter(ImageFilter.DETAIL)
#   img.filter(ImageFilter.EDGE_ENHANCE)
#   img.filter(ImageFilter.CONTOUR)
#   img.filter(ImageFilter.EMBOSS)
#   img.filter(ImageFilter.FIND_EDGES)
#
# Enhance:
#   enhancer = ImageEnhance.Brightness(img)
#   img = enhancer.enhance(1.5)       # 1.5x brighter
#
#   enhancer = ImageEnhance.Contrast(img)
#   img = enhancer.enhance(1.2)       # More contrast
#
#   enhancer = ImageEnhance.Color(img)
#   img = enhancer.enhance(0.5)       # Less saturated
#
# ======================================================================


# ======================================================================
# 🚀 SETUP INSTRUCTIONS
# ======================================================================
#
# Installation:
#   pip install matplotlib pillow
#
# Verify installation:
#   import matplotlib
#   print(matplotlib.__version__)
#
#   from PIL import Image
#   print(Image.__version__)
#
# Sample images for practice:
#   - Use any images from your computer
#   - Download free images from unsplash.com
#   - Create simple test images with Image.new()
#
# Matplotlib backends:
#   - If plt.show() doesn't work, try:
#     import matplotlib
#     matplotlib.use('TkAgg')  # or 'Qt5Agg'
#
# Font for text drawing:
#   - Windows: 'arial.ttf', 'times.ttf'
#   - macOS: '/Library/Fonts/Arial.ttf'
#   - Linux: '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
#   - Or use ImageFont.load_default()
#
# ======================================================================
