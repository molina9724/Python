import bext

bext.fg("red")
print("Red text on default background")

bext.fg("red")
bext.bg("blue")
print("Red text on blue background")

bext.fg("reset")
bext.bg("reset")
