import subprocess
import time

# subprocess.run(["open", "-a", "Calculator"])

# calculator_process = subprocess.Popen(["open", "/System/Applications/Calculator.app"])
# print("It's still open")
# time.sleep(5)
# calculator_process.kill()
# print("It's over and done")

proc = subprocess.run(
    ["ping", "-c", "4", "nostarch.com"], capture_output=True, text=True
)
print(proc.stdout)

# subprocess.run(
#     [
#         "open",
#         "/Users/daniel_molina/Downloads/Python/Python/Book/chapter10/unzipping/file1-extracted.txt",
#     ]
# )
