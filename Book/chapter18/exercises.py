import csv

NEW_FILE = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/new_file.csv"
PATH_FILE = (
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter18/exampleWithHeader3.csv"
)

file = open(PATH_FILE)
reader = csv.reader(file)
data = list(reader)
print(data)

for row in data:
    print(row)
    for cell in row:
        print(cell)

example_file = open(PATH_FILE)
example_reader = csv.reader(example_file)
for row in example_reader:
    print("Row #" + str(example_reader.line_num) + " " + str(row))

file.close()

new_file = open(NEW_FILE, "w", newline="")
writer = csv.writer(new_file)
writer.writerow(["Carlos", 28, 50, 3.2])
writer.writerow(["Tamara", 46, 25, 2])

new_file.close()
