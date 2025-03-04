#https://www.w3schools.com/python/numpy/numpy_array_slicing.asp

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("arr[1:3]", arr[1:3])
print("arr[1:2]", arr[1:2])
print("arr[1:1]", arr[1:1])
print("arr[:4]", arr[:4])
print("arr[4:]", arr[4:])
print("arr[::2]", arr[::2], "every other")