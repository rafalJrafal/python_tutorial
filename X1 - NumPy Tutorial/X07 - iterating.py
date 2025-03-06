#https://www.w3schools.com/python/numpy/numpy_array_iterating.asp


import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

for number in arr:
    print(number)

print(np.nditer(arr))

for number in np.nditer(arr):
    print(number)

for it, number in np.ndenumerate(arr):
    print("it", it, "number", number)

