# =====================================================================
#                    SECTION 1: MATPLOTLIB BASICS
# =====================================================================

import matplotlib.pyplot as plt

PATH = "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/"


x_values = [0, 1, 2, 3, 4, 5]
y_values1 = [10, 13, 15, 18, 16, 20]
y_values2 = [9, 11, 18, 16, 17, 19]
plt.plot(x_values, y_values1)
plt.plot(x_values, y_values2)
plt.savefig(PATH + "linegraph.png")
# plt.show()
plt.clf()

plt.scatter(x_values, y_values1)
plt.scatter(x_values, y_values2)
plt.savefig(PATH + "scatterplot.png")
# plt.show()
plt.clf()

categories = ["Cats", "Dogs", "Mice", "Moose"]
values = [100, 200, 300, 400]
plt.bar(categories, values, align="center")
plt.savefig(PATH + "bargraph.png")
# plt.show()
plt.clf()

slices = values
labels = categories
plt.pie(slices, labels=labels, autopct="%.2f%%")
plt.savefig(PATH + "piechart.png")
# plt.show()
plt.clf()

plt.plot(x_values, y_values1, marker="o", color="b", label="Line 1")
plt.plot(x_values, y_values2, marker="s", color="r", label="Line 2")
plt.legend()
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Graph Title")
plt.grid(True)
# plt.show()

# ----------------------------------------------------------------------
# 🟢 1: CREATE A SIMPLE LINE GRAPH
#
# Learn: plt.plot(), plt.show()
#
# Tasks:
# 1. Import matplotlib.pyplot as plt
# 2. Create two lists: x values and y values
# 3. Call plt.plot(x, y) to create a line graph
# 4. Call plt.show() to display the graph
# 5. Observe the graph window that appears
# ----------------------------------------------------------------------

plt.clf()

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
# plt.show()
plt.clf()

# ----------------------------------------------------------------------
# 🟢 2: ADD TITLE AND AXIS LABELS
#
# Learn: plt.title(), plt.xlabel(), plt.ylabel()
#
# Tasks:
# 1. Create a simple line graph
# 2. Add a title using plt.title()
# 3. Add an x-axis label using plt.xlabel()
# 4. Add a y-axis label using plt.ylabel()
# 5. Display the graph and verify labels appear
# ----------------------------------------------------------------------

plt.plot(x, y)
plt.title("This my title", loc="center")
plt.xlabel("X")
plt.ylabel("Y")
# plt.show()
plt.clf()

# ----------------------------------------------------------------------
# 🟢 3: SAVE A GRAPH TO FILE
#
# Learn: plt.savefig()
#
# Tasks:
# 1. Create a graph with title and labels
# 2. Save as PNG using plt.savefig('graph.png')
# 3. Save as JPG with different filename
# 4. Save as PDF for high quality
# 5. Verify the files were created
# 6. Note: Call savefig() BEFORE show()
# ----------------------------------------------------------------------

plt.plot(x, y)
plt.title("Save this shit")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig(
    "/Users/daniel_molina/Downloads/Python/Python/Book/chapter21/saving_graph.png"
)

# ----------------------------------------------------------------------
# 🟡 4: CUSTOMIZE LINE STYLE AND COLOR
#
# Learn: color, linestyle, linewidth, marker parameters
#
# Tasks:
# 1. Create a line graph with color='red'
# 2. Try different colors: 'blue', 'green', '#FF5733' (hex)
# 3. Change line style: linestyle='--' (dashed), ':' (dotted)
# 4. Change line width: linewidth=2
# 5. Add markers: marker='o', marker='s' (square)
# ----------------------------------------------------------------------

z = [1, 3, 5, 7, 9]

plt.clf()
plt.plot(x, y, color="r", linestyle="--", marker="o")
plt.plot(y, x, color="green", linestyle=":", marker="s")
plt.plot(x, z, color="#28B1CA", linestyle="--", linewidth=3, marker="*")
# plt.show()

# ----------------------------------------------------------------------
# 🟡 5: PLOT MULTIPLE LINES
#
# Learn: Multiple plt.plot() calls
#
# Tasks:
# 1. Create x values list
# 2. Create two different y values lists
# 3. Plot first line with plt.plot(x, y1)
# 4. Plot second line with plt.plot(x, y2)
# 5. Add a legend using plt.legend(['Line 1', 'Line 2'])
# 6. Use different colors for each line
# ----------------------------------------------------------------------

plt.clf()
plt.plot(x, y, color="r")
plt.plot(x, z, color="g")
plt.legend(["Line 1", "Line 2"])
# plt.show()

# ----------------------------------------------------------------------
# 🟡 6: CREATE A BAR CHART
#
# Learn: plt.bar()
#
# Tasks:
# 1. Create a list of categories (e.g., ['A', 'B', 'C', 'D'])
# 2. Create a list of values for each category
# 3. Create a bar chart with plt.bar(categories, values)∫
# 4. Add title and axis labels
# 5. Customize bar colors with color parameter
# ----------------------------------------------------------------------

plt.clf()
categories = ["A", "B", "C", "D", "E"]
values = [1, 2, 3, 4, 5]
colors = ["black", "yellow", "blue", "green", "purple"]

plt.bar(
    categories,
    values,
    label=colors,
    color=colors,
    align="center",
    bottom=0,
    edgecolor="black",
    angle=12,
)
plt.legend(title="Colors")
plt.xlabel("Categories")
plt.ylabel("Values")
# plt.show()

# ----------------------------------------------------------------------
# 🟡 7: CREATE A HORIZONTAL BAR CHART
#
# Learn: plt.barh()
#
# Tasks:
# 1. Create categories and values lists
# 2. Create horizontal bar chart with plt.barh()
# 3. Add title and axis labels
# 4. Customize colors
# 5. Compare with vertical bar chart
# ----------------------------------------------------------------------

plt.clf()
plt.barh(categories, y, color=colors, label=categories)
plt.legend(title="Categories")
plt.xlabel("X")
plt.ylabel("Y")
# plt.show()
plt.clf()

# ----------------------------------------------------------------------
# 🟡 8: CREATE A SCATTER PLOT
#
# Learn: plt.scatter()
#
# Tasks:
# 1. Create x and y data points (can be random)
# 2. Create a scatter plot with plt.scatter(x, y)
# 3. Customize marker size with s parameter
# 4. Customize marker color with c parameter
# 5. Add transparency with alpha parameter
# ----------------------------------------------------------------------

plt.scatter(x, y, marker="1", color="Black", linestyle="-")
plt.scatter(x, z, marker="2", color="blue")
plt.scatter(y, x, marker="3", c="red")
plt.scatter(y, z, marker="4", c="#43ff64d9")
# plt.show()
plt.clf()

# ----------------------------------------------------------------------
# 🟡 9: CREATE A PIE CHART
#
# Learn: plt.pie()
#
# Tasks:
# 1. Create a list of values (slices of the pie)
# 2. Create a list of labels for each slice
# 3. Create pie chart with plt.pie(values, labels=labels)
# 4. Add percentage labels with autopct='%1.1f%%'
# 5. Explode a slice using explode parameter
# ----------------------------------------------------------------------

explode = [0, 0, 0, 0, 0.05]

plt.pie(x, labels=categories, autopct="%.1f%%", explode=explode)
# plt.show()
plt.clf()

# ----------------------------------------------------------------------
# 🟡 10: CREATE A HISTOGRAM
#
# Learn: plt.hist()
#
# Tasks:
# 1. Create a list of data values (many values)
# 2. Create histogram with plt.hist(data)
# 3. Customize number of bins with bins parameter
# 4. Add title and labels
# 5. Customize color and edge color
# ----------------------------------------------------------------------

x = [45, 50, 75, 80, 80, 82, 90, 98, 100, 65, 45, 55, 60] * 10

plt.hist(x, bins=10, edgecolor="k", facecolor="r", log=False)
plt.xlabel("Score")
plt.ylabel("# of students")
# plt.show()
plt.clf()

# =====================================================================
#                    SECTION 2: ADVANCED MATPLOTLIB
# =====================================================================


# ----------------------------------------------------------------------
# 🟡 11: SET AXIS LIMITS
#
# Learn: plt.xlim(), plt.ylim()
#
# Tasks:
# 1. Create a line graph
# 2. Set x-axis limits with plt.xlim(min, max)
# 3. Set y-axis limits with plt.ylim(min, max)
# 4. Observe how the graph changes
# 5. Try plt.axis([xmin, xmax, ymin, ymax]) as alternative
# ----------------------------------------------------------------------

x = [_ for _ in range(11)]
y = x

plt.plot(x, y)
plt.xlim(2, 8)
plt.ylim(5, 8)
plt.clf()

plt.plot(x, y)
plt.axis((5, 8, 5, 8))
# plt.show()

# ----------------------------------------------------------------------
# 🟡 12: ADD GRID LINES
#
# Learn: plt.grid()
#
# Tasks:
# 1. Create a graph
# 2. Add grid lines with plt.grid(True)
# 3. Customize grid with linestyle and color
# 4. Try grid on only x or y axis
# 5. Adjust grid transparency with alpha
# ----------------------------------------------------------------------

plt.clf()
plt.plot(x, y, linestyle="--", color="#29C4A5FF")
plt.axis((0, 10, 0, 10))
plt.grid(True)

# ----------------------------------------------------------------------
# 🟡 13: ADD TEXT ANNOTATIONS
#
# Learn: plt.text(), plt.annotate()
#
# Tasks:
# 1. Create a line graph
# 2. Add text at specific coordinates with plt.text(x, y, 'text')
# 3. Customize font size and color
# 4. Use plt.annotate() to add an arrow pointing to a data point
# 5. Annotate the maximum or minimum value
# ----------------------------------------------------------------------
plt.clf()
plt.plot(x, y)
plt.text(
    0,
    0,
    "Origin",
    color="b",
    fontsize="x-large",
)
plt.annotate(
    "Have a look at this", (2, 2), (3, 3), arrowprops=dict(facecolor="r", shrink=1)
)

plt.annotate("Min Value", (0, 0), (0, 2), arrowprops=dict(facecolor="g", shrink=0.1))
plt.annotate(
    "Max value",
    (10, 10),
    (8, 8),
    arrowprops=dict(
        facecolor="y",
        shrink=0.1,
    ),
)

# plt.show()


# ----------------------------------------------------------------------
# 🟡 14: CREATE SUBPLOTS
#
# Learn: plt.subplot(), plt.subplots()
#
# Tasks:
# 1. Create a figure with 2 rows and 1 column of subplots
# 2. Use plt.subplot(2, 1, 1) for first subplot
# 3. Plot data in the first subplot
# 4. Use plt.subplot(2, 1, 2) for second subplot
# 5. Plot different data in the second subplot
# 6. Use plt.tight_layout() to prevent overlap
# ----------------------------------------------------------------------


plt.clf()
plt.subplots(2, 1)

plt.subplot(
    2,
    1,
    1,
)
plt.plot(x, y)


a = [-1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21]

plt.subplot(2, 1, 2)
plt.plot(y, a)
plt.tight_layout()

# plt.show()


# ----------------------------------------------------------------------
# 🟡 15: CREATE FIGURE WITH CUSTOM SIZE
#
# Learn: plt.figure(figsize=())
#
# Tasks:
# 1. Create a figure with custom size: plt.figure(figsize=(10, 6))
# 2. Width and height are in inches
# 3. Create a graph on this figure
# 4. Save the figure and check the dimensions
# 5. Try different aspect ratios
# ----------------------------------------------------------------------

plt.clf()
# plt.figure(figsize=(2, 6))
plt.plot(x, y)
# plt.show()

# ----------------------------------------------------------------------
# 🟡 16: CUSTOMIZE TICKS
#
# Learn: plt.xticks(), plt.yticks()
#
# Tasks:
# 1. Create a graph
# 2. Set custom x-axis tick positions with plt.xticks([0, 2, 4, 6])
# 3. Set custom tick labels: plt.xticks([0, 1, 2], ['Low', 'Med', 'High'])
# 4. Rotate tick labels with rotation parameter
# 5. Customize tick font size
# ----------------------------------------------------------------------

plt.clf()
plt.plot(x, y)
plt.xticks([0, 2, 4, 6], ["Very Low", "Low", "Mid", "High"], rotation=45, fontsize=20)
plt.yticks([0, 2, 4, 6])
# plt.show()

# ----------------------------------------------------------------------
# 🟡 17: USE DIFFERENT STYLES
#
# Learn: plt.style.use()
#
# Tasks:
# 1. Print available styles: print(plt.style.available)
# 2. Try 'seaborn' style: plt.style.use('seaborn-v0_8')
# 3. Try 'ggplot' style
# 4. Try 'dark_background' style
# 5. Create the same graph with different styles and compare
# ----------------------------------------------------------------------

plt.clf()

print(plt.style.available)
plt.style.use("Solarize_Light2")
plt.plot(x, y)
plt.show()
