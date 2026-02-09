# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

# def list_to_string(my_list):
#     if len(my_list) == 1:
#         return str(my_list[0])
#     string = ""
#     for index in range(len(my_list)-1):
#         string += str(my_list[index]) + ", "
#     string += "and " + str(my_list[len(my_list)-1])
#     return string


# print(list_to_string(['apples', 'bananas', 'tofu', 'cats']))
# print(list_to_string(["hello", 3, 4]))
# print(list_to_string(["hello"]))
# print(list_to_string(["hello", "you"]))
# print(list_to_string([None, "you"]))
# print(list_to_string(["", "you"]))
# print(list_to_string([True, False, "you"]))

# try:
#     test = []
#     if len(test) == 0:
#         raise Exception("Add a value into that shit, man")
#     list_to_string(test)
# except Exception as e:
#     print(str(e))

import random

# coin_flip = list()
# for index in range(100):
#     coin_flip.append(random.randint(0, 1))

test1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

results = []
for index in range(len(test1)-5):
    if all(test1[index:index+6]):
        results.append(test1[index:index+6])


x = list(test1[i] for i in range(len(test1)-5))
