# ======================================================================
# 🐍 CHAPTER 10: WORKING WITH FILES AND DIRECTORIES
# ======================================================================
# Based on: Automate the Boring Stuff with Python, 3rd Edition
# Topics: os module, pathlib module, file operations (read, write, delete),
#         directories (create, move, search), shutil, zipfile, exception handling
# ======================================================================

import os
from pathlib import Path
import shutil
import zipfile
from datetime import datetime


# =====================================================================
#                    SECTION 1: FILE OPERATIONS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 1: Understanding File Paths
# Write a script to:
# 1. Display the absolute path of the current working directory.
# 2. Check if a given file path exists.
# 3. Determine if the path is a file or directory.
#
# Test:
# - Test with a valid file path and a non-existing path.
# ----------------------------------------------------------------------

# # Write your code below:


# print(Path.cwd())
# os.chdir("/Users/daniel_molina/Downloads/platform-tools")
# print(Path.cwd())

# print(Path("/Users").is_dir())
# print(Path("/Users/NoExist").is_dir())
# print(Path("/Users/daniel_molina/Downloads/chromedriver_108").is_file())
# print(Path("/Users/NoExistFile").is_file())

# print(Path.home())
# print(Path.cwd().is_absolute())
# print(Path("notAbsoulte").is_absolute())

# test = Path(Path.cwd() / "spam.txt")
# print(test.anchor)
# print(test.parent)
# print(test.stem)
# print(test.suffix)
# print(test.name)
# print(test.parts)

# test2 = test.parents
# for parent in test2:
#     print(parent)

# print(test.stat().st_size)
# test3 = Path(Path.cwd())
# print(list(test3.glob("*")))
# print(list(test3.glob("*.??")))

# for file in test3.glob("*"):
#     print(file)

# txt = Path(f"{Path.cwd()}/spam.txt")
# print(txt.exists())
# txt.write_text("3")
# print(txt.read_text())

# ----------------------------------------------------------------------
# 🟢 EASY 2: Creating and Deleting Files
# Use Python to:
# 1. Create a file, write some content, and save it.
# 2. Rename the file.
# 3. Delete the file.
# 4. Add error handling for each operation.
#
# Test:
# - Confirm file existence at each step.
# - Test with attempts to rename/delete non-existing files.
# ----------------------------------------------------------------------

# # Write your code below:
# try:
#     my_file = Path("xxx.txt")
#     my_file.write_text("Hello, world!")

#     if my_file.exists():
#         print(f"File '{my_file}' created and contains: {my_file.read_text()}")

#     new_file = my_file.rename("yyy.txt")
#     print(f"File renamed to '{new_file}'")

#     if new_file.exists():
#         new_file.unlink()
#         print(f"File '{new_file}' deleted successfully")
#     else:
#         print(f"File '{new_file}' does not exist for deletion")
# except FileNotFoundError as e:
#     print("Error: File not found!", e)
# except PermissionError as e:
#     print("Error: Permission denied!", e)
# except Exception as e:
#     print("An unexpected error occurred:", e)


# ----------------------------------------------------------------------
# 🟢 EASY 3: Writing and Appending Files
# Write a script to:
# 1. Open a file.
# 2. Append text at the end of the file.
# 3. Validate content changes.
#
# Test:
# - Confirm that text has been appended correctly.
# ----------------------------------------------------------------------

# # Write your code below:

# file_path = Path("easy3.txt")
# first_line = "Line 1\n"
# last_line = "Line 2\n"

# with file_path.open("w") as file:
#     file.write(first_line)

# with file_path.open("a") as file:
#     file.write(last_line)

# with file_path.open("r") as file:
#     content = file.readlines()
#     if content[-1] == last_line:
#         print("You did it, you son of a bitch!")

# ----------------------------------------------------------------------
# 🟢 EASY 4: File Extension Validation
# Write a script to validate file extensions for `.txt`, `.csv`, `.log`, etc.
# Tasks:
# - Check if files have valid extensions.
# - Handle invalid or missing file names gracefully.
#
# Test:
# - Valid examples: "data.csv", "report.txt"
# - Invalid: "data.invalid" → Output error.
# ----------------------------------------------------------------------

# # Write your code below:

# valid_extensions = [".txt", ".csv", ".log"]
# valid_file = Path("valid_file.txt")
# invalid_file = Path("invalid_file.invalid")

# if valid_file.suffix in valid_extensions:
#     print("You have a valid extension right there")
# else:
#     print("Your file extension is invalid")

# ----------------------------------------------------------------------
# 🟢 EASY 5: File Size Calculation
# Write a script to determine:
# 1. The size of a file
# 2. Display size in bytes, KB, and MB.
#
# Test:
# - Test with small files and very large ones.
# ----------------------------------------------------------------------

# # Write your code below:

# my_file = Path("string.txt")
# with open(my_file, "a") as file:
#     file.write("Hello\n")
#     file.write("Hello you\n")
#     file.write("Are you there?\n")
# print(my_file.stat().st_size)
# print(my_file.stat().st_size / 1024)
# print(my_file.stat().st_size / 1024**2)


# ----------------------------------------------------------------------
# 🟡 MEDIUM 6: Counting Lines and Words
# Count the lines and words in a file programmatically.
# Tasks:
# - Open a file and count lines.
# - Count the total number of words in all lines.
#
# Test:
# - Use a file with multiple paragraphs to validate counts.
# ----------------------------------------------------------------------

# # Write your code below:

# file_path = Path("string.txt")
# words_total = 0
# lines_total = 0
# with open(file_path, "r") as file:
#     for single_line in file:
#         lines_total += 1
#         words_total += len(single_line.split())

# print(f"There are {lines_total} lines in your file")
# print(f"There are {words_total} words your file")

# ----------------------------------------------------------------------
# 🟡 MEDIUM 7: File Comparisons
# Compare the content of two files.
# Tasks:
# - Open both files and check if their contents match.
# - Highlight if the files differ in content.
#
# Test:
# - Use two identical files → Validate match output.
# - Use differing files → Highlight differences.
# ----------------------------------------------------------------------

# # Write your code below:

# string1 = Path("string1.txt")
# string2 = Path("string2.txt")

# with open(string1, "a") as file1, open(string2, "a") as file2:
#     file1.write("123456")
#     file2.write("12345")

# if string1.stat().st_size != string2.stat().st_size:
#     print(f"{string1} and {string2} are different files, their size are different")
# else:
#     with open(string1, "r") as file1, open(string2, "r") as file2:
#         for line_number, (line1, line2) in enumerate(zip(file1, file2), start=1):
#             if line1 != line2:
#                 print(f"The files are different in line number {line_number}")
#                 print(f"{file1} reads {line1}")
#                 print(f"{file2} reads {line2}")
#                 break
#         else:
#             if next(line1, None):
#                 print(f"Files are different, {file1} has more lines")
#             elif next(line2, None):
#                 print(f"Files are different, {file2} has more lines")
#             else:
#                 print("The files are identical")

# ----------------------------------------------------------------------
# 🟡 MEDIUM 8: File Permission Checks
# Validate the permission settings of a file.
# Tasks:
# - Check if the file has read, write, and execute permissions.
# - Return specific results for each permission state.
#
# Test:
# - Use accessible and restricted files for tests.
# ----------------------------------------------------------------------

# # Write your code below:

# file_path = Path("permissions.txt")
# # with open(file_path, "a") as file:
# #     file.write("Let's check the permissions")

# if os.access(file_path, os.R_OK):
#     print("You can read the file")
# else:
#     print("You can NOT read the file")
# if os.access(file_path, os.W_OK):
#     print("You can write the file")
# else:
#     print("You can NOT write the file")
# if os.access(file_path, os.X_OK):
#     print("You can execute the file")
# else:
#     print("You can NOT execute the file")

# # Changing all the permissions to No
# file_path.chmod(0o000)

# =====================================================================
#                    SECTION 2: DIRECTORY OPERATIONS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 9: Directory Basics
# Write a script to:
# 1. Create a new directory.
# 2. Rename the directory.
# 3. Delete the directory.
#
# Test:
# - Validate existence of the directory before and after each step.
# ----------------------------------------------------------------------

# # Write your code below:

# my_path = Path.cwd() / "folder"
# my_path.mkdir(parents=True, exist_ok=True)

# new_folder = my_path.rename("renamed_folder")

# if new_folder.exists():

# ----------------------------------------------------------------------
# 🟡 MEDIUM 10: Traversing Directories
# List all files and subdirectories in a given directory.
# Tasks:
# - Use a function that prints a tree-like format of contents.
# - Add the ability to filter by file extension.
#
# Test:
# - Use directories with nested subdirectories and mixed file types.
# ----------------------------------------------------------------------

# # Write your code below:


# def all_files(path, indent=""):
#     for item in path.iterdir():
#         if item.is_file():
#             print(f"{indent}📄 {item.name}")
#         elif item.is_dir():
#             print(f"{indent}📁 {item.name}")
#             all_files(item, indent + "    ")


# start_folder = Path("/Users/daniel_molina/Downloads/Python/Python/exercises")
# all_files(start_folder)

# ----------------------------------------------------------------------
# 🟡 MEDIUM 11: Directory File Count
# Count files grouped by file types in a directory.
# Tasks:
# - Group files based on their extensions (e.g., `.txt`, `.py`).
# - Print the type and count of files for each extension category.
#
# Test:
# - Validate outputs with directories that have a wide range of files.
# ----------------------------------------------------------------------

# # Write your code below:

# start_folder = Path("/Users/daniel_molina/Downloads/Python/Python")
# all_extensions = dict()


# def all_files(path):

#     for element in path.iterdir():
#         if element.is_file():
#             if element.suffix not in all_extensions.keys():
#                 all_extensions[element.suffix] = 1
#             else:
#                 all_extensions[element.suffix] += 1
#         elif element.is_dir():
#             all_files(element)
#     return all_extensions


# print(all_files(start_folder))

# ----------------------------------------------------------------------
# 🟡 MEDIUM 12: Directory Cleanup
# Move unwanted `.tmp` files to a "Trash" folder.
# Tasks:
# - Identify `.tmp` files in a directory.
# - Move them to a "Trash" subdirectory for later inspection.
#
# Test:
# - Create a mix of `.tmp` and `.txt` files for cleanup testing.
# ----------------------------------------------------------------------

# # Write your code below:

# trash = Path(
#     "/Users/daniel_molina/Downloads/Python/Python/exercises/book/chapter10/trash"
# )
# trash.mkdir(parents=True, exist_ok=True)

# test_cleanup = Path(
#     "/Users/daniel_molina/Downloads/Python/Python/exercises/book/chapter10/test_cleanup"
# )


# def all_files(path):
#     for file in path.iterdir():
#         if file.is_file():
#             if file.suffix == ".tmp" or file.suffix == ".txt":
#                 shutil.move(file, trash)
#         elif file.is_dir():
#             all_files(file)


# all_files(test_cleanup)

# >>> p.glob('*')
# <generator object Path.glob at 0x000002A6E389DED0>
# >>> list(p.glob('*'))


# ----------------------------------------------------------------------
# 🔴 HARD 13: Advanced Directory Traversal
# Search for keywords in `.txt` files recursively in a directory.
# Tasks:
# - Open and read all `.txt` files in the directory tree.
# - Return paths of files that contain the provided keyword.
#
# Test:
# - Use a nested directory structure with multiple `.txt` files.
# ----------------------------------------------------------------------

# # Write your code below:

# paths = []


# def all_files(path, keyword):

#     for file in path.iterdir():
#         if file.is_file():
#             if file.suffix == ".txt":
#                 with open(file, "r") as open_file:
#                     all_lines = open_file.readlines()
#                     for line in all_lines:
#                         words = line.split()
#                         if keyword in words:
#                             paths.append(str(file))
#         elif file.is_dir():
#             all_files(file, keyword)
#     return paths


# working_folder = Path(
#     "/Users/daniel_molina/Downloads/Python/Python/exercises/book/chapter10/test_search"
# )
# print(all_files(working_folder, "refactor"))

# ----------------------------------------------------------------------
# 🔴 HARD 14: Copy Directory Structure
# Replicate a directory's structure elsewhere.
# Tasks:
# - Create the same folder tree in a new location without file content.
# - Ensure all subfolders are replicated.
#
# Test:
# - Validate the accuracy of the replicated folder structure.
# ----------------------------------------------------------------------

# # Write your code below:

# file = Path("/Users/daniel_molina/Downloads/Python/Python/exercises/book/chapter10")
# destination = Path(
#     "/Users/daniel_molina/Downloads/Python/Python/exercises/book/chapter9"
# )


# def all_folders(path, copy_to):
#     """
#     The function `all_folders` recursively copies all folders and their contents from a given path to a
#     specified destination.

#     :param path: The `path` parameter in the `all_folders` function is expected to be a `Path` object
#     representing the directory from which you want to start copying folders. This function recursively
#     iterates through all folders and subfolders starting from this path
#     :param copy_to: The `copy_to` parameter in the `all_folders` function represents the destination
#     directory where the folders from the `path` directory will be copied to. This parameter should be a
#     `Path` object pointing to the directory where you want to copy the folders
#     """
#     for file in path.iterdir():
#         if file.is_dir():
#             new_folder_path = copy_to / file.name
#             new_folder_path.mkdir(parents=True, exist_ok=True)
#             all_folders(file, new_folder_path)


# all_folders(file, destination)


# ----------------------------------------------------------------------
# 🔴 HARD 15: Search Files by Criteria
# Implement a script to search for files based on:
# 1. File size threshold (e.g., > 1MB).
# 2. Last-modified date range.
# 3. Specific file extensions.
#
# Test:
# - Place test files in nested directories for validation.
# ----------------------------------------------------------------------

# # Write your code below:

# example = Path(
#     "/Users/daniel_molina/Downloads/Python/Python/exercises/book/chapter10/test_criteria"
# )
# all_extensions = [".txt", ".csv"]
# file_details = []


# def all_folders(path: Path, size_threshold: float, last_modified: str, extensions: str):
#     """
#     This Python function recursively searches through folders to find files that meet specified criteria
#     based on size, last modified date, and file extensions.

#     :param path: The `path` parameter in the `all_folders` function represents the directory path where
#     you want to search for files based on certain criteria. It should be of type `Path`, which is
#     typically a pathlib object representing a file system path. You can pass the directory path as an
#     argument when calling the
#     :type path: Path
#     :param size_threshold: The `size_threshold` parameter is a float value that represents the minimum
#     file size threshold in megabytes. Files larger than this threshold will be considered for further
#     processing in the `all_folders` function
#     :type size_threshold: float
#     :param last_modified: The `last_modified` parameter in the `all_folders` function is a string that
#     represents a specific date and time in ISO format (YYYY-MM-DDTHH:MM:SS). This parameter is used to
#     filter files based on their last modified timestamp. Files that have been modified after the
#     specified `
#     :type last_modified: str
#     :param extensions: extensions: This parameter should be a string containing the file extensions that
#     you want to filter for. For example, if you only want to consider files with extensions '.txt',
#     '.csv', and '.pdf', you would provide the string ".txt,.csv,.pdf"
#     :type extensions: str
#     :return: The function `all_folders` is returning a list of tuples containing details of files that
#     meet the specified criteria. Each tuple includes the file name, size in megabytes, and last modified
#     timestamp in string format.
#     """
#     for file in path.iterdir():
#         if file.is_file():
#             if (
#                 (size_mb := file.stat().st_size / (1024 * 1024)) > size_threshold
#                 and (modified := datetime.fromtimestamp(file.stat().st_mtime))
#                 > datetime.fromisoformat(last_modified)
#                 and (file.suffix in all_extensions)
#             ):
#                 file_details.append((file.name, f"{size_mb:.2f} MB", str(modified)))
#         elif file.is_dir():
#             # We are only going to work with files, not dirs
#             all_folders(file, size_threshold, last_modified, extensions)
#     return file_details


# print(all_folders(example, 1, "2025-01-01", ".txt"))

# =====================================================================
#                    SECTION 3: ZIP FILE OPERATIONS
# =====================================================================


# ----------------------------------------------------------------------
# 🟢 EASY 16: Creating ZIP Files
# Use Python to:
# 1. ZIP all `.txt` files in a directory.
# 2. Name the ZIP file with today’s date.
#
# Test:
# - Confirm the contents of the ZIP archive.
# ----------------------------------------------------------------------

# # Write your code below:

import zipfile

# current_date = datetime.today()
# my_first_zip = zipfile.ZipFile(f"{current_date}.zip", "w")


# def all_files(path: Path):

#     for file in path.iterdir():
#         if file.is_file() and file.suffix == ".txt":
#             my_first_zip.write(file, arcname=f"{file.name}")
#         elif file.is_dir():
#             all_files(file)


# example = Path(
#     "/Users/daniel_molina/Downloads/Python/Python/exercises/book/chapter10/test_zip"
# )
# print(all_files(example))
# my_first_zip.close()


# ----------------------------------------------------------------------
# 🟡 MEDIUM 17: Extracting and Modifying ZIPs
# Extract files from a ZIP archive.
# Tasks:
# - Unzip contents to an existing/new directory.
# - Rename files in the extracted folder.
#
# Test:
# - Validate ZIP extraction with files of mixed extensions.
# ----------------------------------------------------------------------

# # Write your code below:

# zip_file = Path(
#     "/Users/daniel_molina/Downloads/Python/Python/exercises/book/chapter10/2026-03-16 07:42:22.844819.zip"
# )

# unzipping = Path(
#     "/Users/daniel_molina/Downloads/Python/Python/exercises/book/chapter10/unzipping"
# )
# unzipping.mkdir(parents=True, exist_ok=True)

# with zipfile.ZipFile(zip_file, "r") as zip:
#     zip.extractall(unzipping)

# for root, dirs, files in os.walk(unzipping):
#     all_files = files
#     for element in all_files:
#         file = Path(Path(root) / element)
#         new_name = f"{file.stem}-extracted{file.suffix}"
#         file.rename(Path(root) / new_name)

# ----------------------------------------------------------------------
# 🔴 HARD 18: Combining File Operations
# Search for keywords in files stored inside ZIP archives.
# Tasks:
# - Open and analyze files directly from the archive.
# - Write a log of paths and matches found.
#
# Test:
# - Use multiple ZIPs with `.txt` files for comprehensive testing.
# ----------------------------------------------------------------------

# # Write your code below:


# ----------------------------------------------------------------------
# 🔴 HARD 19: Advanced ZIP Manipulation
# Build a program to:
# 1. Merge multiple ZIP archives into one archive.
# 2. Handle filename conflicts by appending unique identifiers.
#
# Test:
# - Test with ZIPs containing identical and conflicting files.
# ----------------------------------------------------------------------

# # Write your code below:


# ----------------------------------------------------------------------
# 🔴 HARD 20: ZIP File Size Reporting
# Create a script to:
# - List all files in a ZIP archive by size.
# - Summarize the total size of the archive.
#
# Test:
# - Use a ZIP with at least 5 files of varied sizes.
# ----------------------------------------------------------------------

# # Write your code below:


# ======================================================================
# 📊 EXERCISE SUMMARY
# ======================================================================
# Chapter 10 Concepts Covered:
#
# 1. File Operations: open, write, append, delete, permissions, comparisons.
# 2. Directory Operations: traversal, cleanup, tree replication, search.
# 3. ZIP File Operations: creation, extraction, merging, reporting.
# ======================================================================
