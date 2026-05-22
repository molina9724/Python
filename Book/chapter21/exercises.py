import os

from PIL import Image, ImageColor, ImageDraw, ImageFont

print(ImageColor.getcolor("red", "RGBA"))
print(ImageColor.getcolor("blue", "RGB"))
print(ImageColor.getcolor("White", "RGB"))
print(ImageColor.getcolor("Black", "RGB"))
print(ImageColor.getcolor("purple", "RGB"))

print(ImageColor.getrgb("Blue"))
print(ImageColor.getrgb("Chocolate"))

all_colors = ImageColor.colormap
print(all_colors)

ROOT_PATH = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/"
FILE_PATH = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/zophie.png"

cat_image = Image.open(FILE_PATH)
# cat_image.show()

print(cat_image.size)
print(cat_image.format)
print(cat_image.format_description)
cat_image = cat_image.convert("RGB")
cat_image.save("/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/zophie.jpg")

new_image = Image.new(
    "RGBA",
    (250, 250),
    "blue",
)
new_image.save(ROOT_PATH + "new_image.png")

cropped_image = cat_image.crop((335, 345, 565, 560))
cropped_image.save("cropped.png")

cat_copy_image = cat_image.copy()

cat_copy_image.paste(cropped_image, (0, 0))
cat_copy_image.paste(cropped_image, (400, 500))
cat_copy_image.save("pasted.png")

black_image = Image.new("1", (10, 10))
cat_copy_image.paste(black_image, (806, 1078))
cat_copy_image.paste(black_image, (806, 0))
cat_copy_image.paste(black_image, (0, 1078))
cat_copy_image.paste(black_image, (0, 0))

cat_copy_image.save("pasted.png")

print(cat_copy_image.size)

cat_image_width, cat_image_height = cat_image.size
cropped_image_width, cropped_image_height = cropped_image.size

for left in range(0, cat_image_width, cropped_image_width):
    for top in range(0, cat_image_height, cropped_image_height):
        cat_copy_image.paste(cropped_image, (left, top))

cat_copy_image.save(ROOT_PATH + "cats.png")

quater_sized_image = cat_copy_image.resize(
    (
        int(cat_image_width / 2),
        int(cat_image_height / 2),
    )
)
quater_sized_image.save(ROOT_PATH + "quarter.png")

svelte_image = cat_image.resize((cat_image_width, cat_image_height + 300))
svelte_image.save(ROOT_PATH + "svelte.png")

cat_image.rotate(90).save(ROOT_PATH + "rotated90.png")
cat_image.rotate(180).save(ROOT_PATH + "rotated180.png")
cat_image.rotate(270, expand=True).save(ROOT_PATH + "rotated270.png")
cat_image.transpose(Image.FLIP_LEFT_RIGHT).save(ROOT_PATH + "transpose.png")

image = Image.new("RGBA", (100, 100))
print(image.getpixel((0, 0)))

for x in range(100):
    for y in range(50):
        image.putpixel((x, y), (210, 210, 210))

for x in range(100):
    for y in range(50, 100):
        image.putpixel((x, y), ImageColor.getcolor("darkgray", "RGBA"))

image.save(ROOT_PATH + "put_pixel.png")

image = Image.new("RGBA", (200, 200), "white")
draw = ImageDraw.Draw(image)

draw.line(
    [
        (0, 0),
        (199, 0),
        (199, 199),
        (0, 199),
        (0, 0),
    ],
    fill="red",
)

draw.line([(0, 0), (200, 200)], fill="green")
draw.line([(199, 0), (0, 199)], fill="green")

draw.rectangle(
    (20, 30, 60, 60),
    fill="blue",
)

draw.ellipse(
    (120, 30, 160, 60),
    "red",
)

draw.ellipse((70, 70, 130, 130), "black")

draw.polygon(
    (
        (57, 87),
        (79, 62),
        (94, 85),
        (120, 90),
        (103, 113),
    ),
    fill="brown",
)

draw.point([(100, 100)], fill="white")

for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill="green")

draw.text(
    (20, 150),
    "Hello",
    fill="purple",
)

arial_font = ImageFont.truetype("SFNSItalic.ttf", 32)
draw.text((100, 150), "Howdy", fill="gray", font=arial_font)

image.save(ROOT_PATH + "draw.png")
