#https://www.w3schools.com/python/python_tuples.asp

mytuple_a = ("apple", "banana", "cherry", "plum", "banana")

print(mytuple_a)

mytuple_b = ("not a banana", )

print(mytuple_b)
print(type(mytuple_b))

if "banana" in mytuple_a:
    print("banana is in this tuple")

if "wood" not in mytuple_a:
    print("wood is not in the tuple")

print("element[2]: ", mytuple_a[2])

#error: mytuple_a[2] = "ssss"

mytuple_a += ("another banana", )

print(mytuple_a)

mylist_a = list(mytuple_a)
mylist_a.remove("banana")
print(mylist_a)
mytuple_c = tuple(mylist_a)
print(mytuple_c)

first, second, *rest = mytuple_c

print("first = ", first, " second = ", second, " other = ", rest)

for element in mytuple_a:
    print(element.upper())

mytupe_d = mytuple_a * 2

print(mytupe_d)