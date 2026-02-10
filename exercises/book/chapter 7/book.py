# Fantasy Game Inventory

# Say you’re creating a medieval fantasy video game. The data structure to model the player’s inventory is a dictionary whose keys are strings describing the item in the inventory and whose values are integers detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has one rope, six torches, 42 gold coins, and so on.

# Write a function named display_inventory() that would take any possible “inventory” and display it like the following:

# inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# total_items = 0
# for key, value in inventory.items():
#     print(f"{value} {key}")
#     total_items += value
# print(f"Total number of items: {total_items}")

# List-to-Dictionary Loot Conversion

# Imagine that the same fantasy video game represents a vanquished dragon’s loot as a list of strings, like this:

# dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Write a function named add_to_inventory(inventory, added_items). The inventory parameter is a dictionary representing the player’s inventory (as in the previous project) and the added_items parameter is a list, like dragon_loot. The add_to_inventory() function should return a dictionary that represents the player’s updated inventory. Note that the added_items list can contain multiples of the same item. Your code could look something like this:

# dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


# def add_to_inventory(inventory, added_items):
#     for element in added_items:
#         inventory[element] = inventory.setdefault(element, 0) + 1
#     return inventory


# print(add_to_inventory(inventory, dragon_loot))

# A school has the students Alice, Bob, and Carol, who are all in the seventh grade. Another student, David, is in the sixth grade. Write a list of dictionaries that can model this information. The dictionaries should have keys 'name' and 'grade'. The value for the 'grade' key should be an integer. The order of the dictionaries in the list doesn’t matter.

# students = [{"name": "Alice", "grade": 7},
#             {"name": "Bob", "grade": 7},
#             {"name": "Carol", "grade": 7},
#             {"name": "David", "grade": 6}]

# students = ["sixth_grade", {"name": "Alice", "grade": 1}, {"name": "Bob", "grade": 2}, {
#     "name": "Carol", "grade": 3}, {"name": "David", "grade": 4}]

# spam = [{'name': 'Alice', 'age': 3}, {'name': 'Zophie', 'age': 17}]
# print(spam[1]["name"])
# print(spam[0]["age"])

# spam = {'humans': ['Alice', 'Bob'],
#         'pets': ['Zophie', 'Pookah']}
# print(spam['pets'][0])

# 34. Say that the first line in a small program is pet_owners = {'Alice': ['Spot', 'Mittens'], 'Al': ['Zophie']}. Write a for loop that prints all of Alice’s pets’ names.

# pet_owners = {'Alice': ['Spot', 'Mittens'], 'Al': ['Zophie']}
# for pet in pet_owners['Alice']:
#     print(pet)
