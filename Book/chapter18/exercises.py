import csv

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
