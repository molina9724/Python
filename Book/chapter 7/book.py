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

# 35. Two teams, 'Home' and 'Visitor', played a game of baseball across nine innings, numbered 1 through 9. (Programmers did not invent baseball, so the first inning is not zero.) To model this game, create a dictionary with the keys 'Home' and 'Visitor'. The values for these two keys should also be dictionaries, with integer keys 1 through 9, to represent each inning. The values for each of the inning keys should be the score for the inning. The score was 0 in all innings except for the third, when the Home team scored one run. (It wasn’t an exciting game.) Write the code for this dictionary.

# baseball = {"Home": {1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
#             "Visitor": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}}

# 36. Instead of manually writing the dictionary in the previous question, write a for loop that can automatically generate it. You can work from the following template:

# game = {'Home': {}, 'Visitor': {}}
# for inning in range(1, 10):  # Loop from 1 to 9.
#     game['Home'][inning] = 0
#     game['Visitor'][inning] = 0
# game['Home'][3] = 1  # Set one run in third inning.

# print(game)

# 37. A deranged billionaire has purchased the entire baseball league so that they can make the following rule change: All baseball games will now have 9,999 innings instead of 9 innings. Change the code in your previous answer to reflect this new game. Again, the only run scored was by the Home team in the third inning. (The teams were too tired to score any more runs later in the game.)

# game = {'Home': {}, 'Visitor': {}}
# for inning in range(1, 10000):  # Loop from 1 to 9999.
#     game['Home'][inning] = 0
#     game['Visitor'][inning] = 0
# game['Home'][3] = 1  # Set one run in third inning.

# print(game)

# Random Weather Data Generator

# Random Weather Data Generator

# Write a function named get_random_weather_data() that returns a dictionary of random weather data. The dictionary should have the keys and values in Table 7-1.
# Table 7-1: Keys and Values for the Weather Dictionary

# Key
# Value
# 'temp'
# A random float from -50 to 50
# 'feels_like'
# A float that is within 10 degrees of the 'temp' value
# 'humidity'
# A random integer between 0 and 100
# 'pressure'
# A random integer between 990 and 1010

# The program should then call this function from a loop 100 times, storing the returned dictionaries in a list. Finally, it should print the list. Save this program in a file named weatherDataGen.py.

import random


def get_random_weather_data():
    temp = random.uniform(-50, 50)
    feels_like = random.uniform(temp-10, temp+10)
    temperature = {'temp': temp,
                   'feels_like': feels_like,
                   'humidity': random.randint(0, 100),
                   'pressure': random.randint(990, 1010)}
    return temperature


temperature_recorder = []
for iteration in range(100):
    temperature_recorder.append(get_random_weather_data())
# print(temperature_recorder)

# Add a function named get_average_temperature(weather_data) to the program in the previous practice project. This function should accept a list of the weather data dictionaries described in the previous project and return the average temperature in their 'temp' keys. To calculate the average, add all of the temperature numbers in the dictionaries and divide the result by the number of dictionaries.

# The list passed to get_average_temperature() can contain any number of dictionaries but should always contain at least one. Generate a list of 100 weather dictionaries by calling get_random_weather_data(), then pass this list to get_average_temperature() and print the average it returns.

# Add this new function to your weatherDataGen.py program and save this new program as avgTemp.py.


def get_average_temperature(weather_data):
    total_records = len(weather_data)
    if total_records > 0:
        total_temperature = 0
        for record in weather_data:
            total_temperature += record["temp"]
    else:
        return "Take that empty shit somewhere else"
    return total_temperature/total_records


print(get_average_temperature(temperature_recorder))
