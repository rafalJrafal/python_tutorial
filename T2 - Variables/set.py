#https://www.w3schools.com/python/python_sets.asp

myset_a = {"banana", "apple", "peach"}

print(myset_a, "number of elements is:", len(myset_a))
print("type is:", type(myset_a))

for element in myset_a:
    print(element)

print("banana" in myset_a)
print("banana" not in myset_a)

myset_a.add("orange")
print(myset_a)

tropical = {"pineapple", "mango", "papaya"}

myset_a.update(tropical)

print(myset_a)

myset_a.remove("banana")
print(myset_a)

myset_a.discard("banana")
print(myset_a)

numeric_set_a = {1, 4, 5, 29, 321, 2}
numeric_set_b = {1, 29, 33, 39}

numericSet_a = numeric_set_a & numeric_set_b
print(numericSet_a)

numericSet_b = numeric_set_a ^ numeric_set_b
print(numericSet_b)