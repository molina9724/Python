# ----------------------------------------------------------------------
# Exercise 1: Creating Sets - Different Ways
#
# 1. Create a set using set() function with a tuple: my_set1 = set((1, 2, 3, 4, 5))
# 2. Create a set using curly braces: my_set2 = {10, 20, 30, 40, 50}
# 3. Create a set with mixed types: my_set3 = {1, "hello", 3.14, True}
# 4. Print all three sets and their types
# 5. Try to create an empty set with {} and check its type (it will be dict!)
# 6. Create an empty set the correct way using set()
# 7. Print both and compare their types
#
# Write your code for Exercise 1 below:


# ----------------------------------------------------------------------
# Exercise 2: Sets Remove Duplicates Automatically
#
# 1. Create a list with duplicates: numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6, 4]
# 2. Convert it to a set
# 3. Print the original list
# 4. Print the set (notice duplicates are gone!)
# 5. Convert the set back to a list
# 6. Print the new list (sorted if you want)
# 7. Create a set from a string: set("hello") - what happens?
#
# Write your code for Exercise 2 below:


# ----------------------------------------------------------------------
# Exercise 3: Set Operations - Cannot Index!
#
# 1. Create a set: my_set = {1, 2, 3, 4, 5}
# 2. Try to access my_set[0] (this will error - comment it out!)
# 3. Try to slice my_set[1:3] (this will error - comment it out!)
# 4. Check if 3 is in the set using 'in' operator
# 5. Print the length of the set
# 6. Iterate over the set and print each element
# 7. Notice the order might not be what you expect!
#
# Write your code for Exercise 3 below:


# ----------------------------------------------------------------------
# Exercise 4: Hashable vs Unhashable
#
# 1. Try hash(5) - works! (int is hashable)
# 2. Try hash("hello") - works! (str is hashable)
# 3. Try hash((1, 2, 3)) - works! (tuple is hashable)
# 4. Try hash([1, 2, 3]) - error! (list is unhashable - comment out!)
# 5. Try hash({1, 2, 3}) - error! (set is unhashable - comment out!)
# 6. Create a set containing: {1, "hello", (1, 2), 3.14} - works!
# 7. Try to create a set with a list inside: {1, [2, 3]} - error! (comment out!)
#
# Write your code for Exercise 4 below:


# ----------------------------------------------------------------------
# Exercise 5: Union Operation (Combining Sets)
#
# 1. Create three sets:
#    s1 = {"a", "b", "c"}
#    s2 = {"c", "d", "e"}
#    s3 = {"e", "f", "g"}
# 2. Use the | operator to get union: union1 = s1 | s2 | s3
# 3. Use the .union() method: union2 = s1.union(s2, s3)
# 4. Print both results (should be the same!)
# 5. Try union with a list using operator: s1 | ["x", "y"] (error - comment out!)
# 6. Try union with a list using method: s1.union(["x", "y"]) (works!)
# 7. Print the result
#
# Write your code for Exercise 5 below:


# ----------------------------------------------------------------------
# Exercise 6: Intersection Operation (Common Elements)
#
# 1. Create three sets:
#    s1 = {1, 2, 3, 4, 5}
#    s2 = {3, 4, 5, 6, 7}
#    s3 = {4, 5, 6, 7, 8}
# 2. Use & operator: intersection1 = s1 & s2 & s3
# 3. Use .intersection() method: intersection2 = s1.intersection(s2, s3)
# 4. Print both (should be the same - only elements in ALL sets)
# 5. Find intersection of s1 and s2 only
# 6. Find intersection of s2 and s3 only
# 7. Compare the results
#
# Write your code for Exercise 6 below:


# ----------------------------------------------------------------------
# Exercise 7: Difference Operation (Elements NOT in Other Sets)
#
# 1. Create sets:
#    s1 = {1, 2, 3, 4, 5}
#    s2 = {4, 5, 6, 7}
#    s3 = {3, 6, 9}
# 2. Use - operator: diff1 = s1 - s2 - s3
# 3. Use .difference() method: diff2 = s1.difference(s2, s3)
# 4. Print both (elements in s1 but NOT in s2 or s3)
# 5. Try s2 - s1 (different result!)
# 6. Try s1 - s2 vs s2 - s1 - understand the difference!
# 7. Print all results with labels
#
# Write your code for Exercise 7 below:


# ----------------------------------------------------------------------
# Exercise 8: Modifying Sets - add, remove, update
#
# 1. Create a set: my_set = {1, 2, 3}
# 2. Add element 4 using .add()
# 3. Print the set
# 4. Add element 2 again (nothing happens - already exists!)
# 5. Print the set
# 6. Remove element 2 using .remove()
# 7. Print the set
# 8. Try to remove element 99 (error - comment out!)
# 9. Use .discard(99) instead (no error if not found!)
#
# Write your code for Exercise 8 below:


# ----------------------------------------------------------------------
# Exercise 9: Update Methods (Modify in Place)
#
# 1. Create sets:
#    s1 = {"a", "b", "c"}
#    s2 = {"c", "d", "e"}
#    s3 = {"e", "f", "g"}
# 2. Print original s1
# 3. Use s1.update(s2, s3) to add elements from s2 and s3 to s1
# 4. Print s1 (it changed!)
# 5. Create new sets and try intersection_update()
# 6. Create new sets and try difference_update()
# 7. Observe how the original set changes each time
#
# Write your code for Exercise 9 below:


# ----------------------------------------------------------------------
# Exercise 10: Clear and Copy Sets
#
# 1. Create a set: my_set = {1, 2, 3, 4, 5}
# 2. Create a copy: my_copy = my_set.copy()
# 3. Clear the original: my_set.clear()
# 4. Print both sets (original is empty, copy still has elements!)
# 5. Verify that my_set is now set() (empty set)
# 6. Verify that my_copy still has the original elements
# 7. Check their ids - they're different objects!
#
# Write your code for Exercise 10 below:


# ----------------------------------------------------------------------
# Exercise 11: Set Membership Testing (Fast!)
#
# 1. Create a large set: big_set = set(range(1000000))
# 2. Check if 500000 is in the set (very fast!)
# 3. Check if 1000001 is in the set (also very fast!)
# 4. Create a large list: big_list = list(range(1000000))
# 5. Compare the speed conceptually (sets are much faster for 'in' checks)
# 6. Use a set to check for duplicates in a list:
#    numbers = [1, 2, 3, 2, 4, 1, 5]
#    has_duplicates = len(numbers) != len(set(numbers))
# 7. Print whether there are duplicates
#
# Write your code for Exercise 11 below:


# ----------------------------------------------------------------------
# Exercise 12: Symmetric Difference
#
# 1. Create sets:
#    s1 = {1, 2, 3, 4}
#    s2 = {3, 4, 5, 6}
# 2. Use ^ operator: sym_diff1 = s1 ^ s2
# 3. Use .symmetric_difference() method: sym_diff2 = s1.symmetric_difference(s2)
# 4. Print both (elements in s1 OR s2, but NOT in both!)
# 5. This is like (s1 - s2) | (s2 - s1)
# 6. Verify this by calculating it manually
# 7. Compare the results
#
# Write your code for Exercise 12 below:


# ----------------------------------------------------------------------
# Exercise 13: Subset and Superset Checks
#
# 1. Create sets:
#    s1 = {1, 2, 3}
#    s2 = {1, 2, 3, 4, 5}
#    s3 = {1, 2}
# 2. Check if s1 is subset of s2: s1.issubset(s2) or s1 <= s2
# 3. Check if s2 is superset of s1: s2.issuperset(s1) or s2 >= s1
# 4. Check if s3 is subset of s1
# 5. Check if sets are disjoint (no common elements): s1.isdisjoint({6, 7, 8})
# 6. Print all results with labels
# 7. Understand the relationships between sets
#
# Write your code for Exercise 13 below:


# ----------------------------------------------------------------------
# Exercise 14: Practical Use Case - Remove Duplicates from List
#
# 1. Create a list with duplicates:
#    words = ["apple", "banana", "apple", "cherry", "banana", "date"]
# 2. Convert to set to remove duplicates
# 3. Convert back to list
# 4. Print original and deduplicated list
# 5. Notice: order is NOT preserved!
# 6. If you need to preserve order, use a different approach (dict.fromkeys())
# 7. Compare both methods
#
# Write your code for Exercise 14 below:


# ----------------------------------------------------------------------
# Exercise 15: Practical Use Case - Finding Common Elements
#
# 1. Create sets representing students in different classes:
#    math_class = {"Alice", "Bob", "Charlie", "David"}
#    science_class = {"Bob", "David", "Eve", "Frank"}
#    english_class = {"Alice", "David", "Frank", "Grace"}
# 2. Find students in both math AND science
# 3. Find students in math OR science OR english (union)
# 4. Find students ONLY in math (not in other classes)
# 5. Find students in all three classes
# 6. Find students in exactly one class
# 7. Print all results with descriptive labels
#
# Write your code for Exercise 15 below:


# ----------------------------------------------------------------------
# Advanced Exercise 16: Set Comprehension
#
# 1. Create a set of squares using set comprehension:
#    squares = {x**2 for x in range(10)}
# 2. Create a set of even numbers from 1 to 20
# 3. Create a set of vowels from a string:
#    text = "hello world"
#    vowels = {char for char in text if char in 'aeiou'}
# 4. Create a set of word lengths:
#    words = ["apple", "banana", "cherry", "date"]
#    lengths = {len(word) for word in words}
# 5. Print all sets
# 6. Notice: set comprehension is like list comprehension but with {}
#
# Write your code for Advanced Exercise 16 below:


# ----------------------------------------------------------------------
# Advanced Exercise 17: Frozen Sets (Immutable Sets)
#
# 1. Create a frozenset: fs = frozenset([1, 2, 3, 4, 5])
# 2. Print it and its type
# 3. Try to add an element (error - comment out!)
# 4. Try to remove an element (error - comment out!)
# 5. Use frozenset as a dictionary key (works! sets can't be keys)
# 6. Create a set of frozensets (nested sets!)
# 7. Understand when frozensets are useful
#
# Write your code for Advanced Exercise 17 below:


# ----------------------------------------------------------------------
# Advanced Exercise 18: Performance Comparison
#
# 1. Create a large list: big_list = list(range(10000))
# 2. Create a large set: big_set = set(range(10000))
# 3. Conceptually understand:
#    - Checking if 9999 in big_list: O(n) - slow
#    - Checking if 9999 in big_set: O(1) - fast!
# 4. Use sets when you need fast membership testing
# 5. Use lists when you need order or duplicates
# 6. Write comments explaining when to use each
#
# Write your code for Advanced Exercise 18 below:
