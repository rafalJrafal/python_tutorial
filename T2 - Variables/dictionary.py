#https://www.w3schools.com/python/python_dictionaries.asp

my_dict = { "brand": "Ford",
           "model": "Mustag",
           "year": 1964}

print("type", type(my_dict), "values", my_dict)

print(my_dict["brand"], my_dict.get("model"))

print(my_dict.keys())

keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print(keys, values, items)

for key in my_dict.keys():
    print(key)

my_dict["color"] = "red"
my_dict["year"] = 2020

print(keys, values, items)

print("model in dict -", "model" in my_dict)

addRemoveVal = "generation"
my_dict[addRemoveVal] = 2

print(keys, values, items)

removed_item = my_dict.pop(addRemoveVal)
print("Removed item", removed_item)

print(keys, values, items)

dict_cpy = my_dict.copy()

print(dict_cpy)
dict_cpy.clear()
print(dict_cpy)
print(my_dict)
