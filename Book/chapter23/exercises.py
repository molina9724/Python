import pyautogui

screen_size = pyautogui.size()
print(screen_size)
print(screen_size.width, screen_size.height)

# absolute
# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

# relative
# for i in range(10):
#     pyautogui.move(100, 0, 0.25)
#     pyautogui.move(0, 100, 0.25)
#     pyautogui.move(-100, 0, 0.25)
#     pyautogui.move(0, -100, 0.25)

position = pyautogui.position()
print(position)
print(position.x)
print(position.y)

# pyautogui.click(2349, 660, button="left")
# pyautogui.click(2349, 660, button="right")
# pyautogui.doubleClick()
# pyautogui.rightClick()

# pyautogui.sleep(5)
# pyautogui.click()
# distance = 300
# change = 20

# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.2, button="left")
#     distance -= change
#     pyautogui.drag(0, distance, 0.2, button="left")
#     pyautogui.drag(-distance, 0, 0.2, button="left")
#     distance -= change
#     pyautogui.drag(0, -distance, 0.2, button="left")

# pyautogui.sleep(5)
# for index in range(5):
#     pyautogui.scroll(35)
#     pyautogui.sleep(1)
#     pyautogui.scroll(-35)
#     pyautogui.sleep(1)

from PIL import Image

image = pyautogui.screenshot()
# image.show()

print(pyautogui.pixel(150, 150))
print(pyautogui.pixelMatchesColor(150, 150, (44, 44, 44)))

print(pyautogui.pixel(300, 200))
print(pyautogui.pixelMatchesColor(300, 200, (36, 36, 36)))

print(pyautogui.pixel(450, 250))
print(pyautogui.pixelMatchesColor(450, 250, (44, 44, 44)))

button = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter23/image2.png"
box = pyautogui.locateOnScreen(button)
print(box)

another_image = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter23/image3.png"
full_image = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter23/full.png"

all_folders = list(pyautogui.locateAll(another_image, full_image))
