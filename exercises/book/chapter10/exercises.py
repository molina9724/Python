# ======================================================================
# 🐍 CHAPTER 10: WORKING WITH FILES AND DIRECTORIES
# ======================================================================
# Based on: Automate the Boring Stuff with Python, 3rd Edition
# Topics: os module, pathlib module, file operations (read, write, delete),
#         directories (create, move, search), shutil, zipfile, exception handling
# ======================================================================

import os
import pathlib
import shutil
import zipfile


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