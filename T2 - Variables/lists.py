#https://www.w3schools.com/python/python_lists.asp

fruits = ["banana", "apple", "cherry", "apple", "peach"]

print("list:", fruits)
print("len(list):", len(fruits))
print("type:", type(fruits))

print("1st element:", fruits[0])
print("last element:", fruits[-1])

print("first three:", fruits[:3])
print("last three", fruits[-3:])

print("second to second to last", fruits[1:-1])

if "apple" in fruits:
    print("apple is in fruit list")

fruits[1:3] = "blackberry", "orange"

print("list after update:", fruits)

fruits[1:1] = "apple", "apple", "apple"

print("list after another update:", fruits)

fruits.insert(3, "warermelon")

print("list after inserting watermelon", fruits)

fruits.append("yellow orange")

print("after adding wierd orange:", fruits)

fruits.extend(fruits[3:6])

print("after extending:", fruits)

fruits.remove("apple")

print("removed one apple", fruits)

element = fruits.pop(3)

print(f"removed {element} from {fruits}")

del fruits[-3]

print("removed 3rd last element", fruits)

newList = [value.upper() for value in fruits]

print("new list selected from fruit list", newList)

newList = [value.upper() for value in fruits if "apple" == value.lower()]

print("new list selected from fruit list", newList)

newList = [value if value != "banana" else "new orange" for value in fruits if "a" in value]

print("new list selected from fruit list", newList)

#https://www.w3schools.com/python/python_lists_sort.asp

fruits.sort()

print("sorted list:", fruits)

def sortFunction(parameter):
    return len(parameter)

fruits.sort(key=sortFunction)

print("sorted by key:", fruits)

anotherFruits = fruits

print(fruits, anotherFruits)

fruits[0:5] = ["not a fruit"]

print(anotherFruits)