#https://www.w3schools.com/python/numpy/numpy_array_search.asp
#https://www.w3schools.com/python/numpy/numpy_array_sort.asp


import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1])

found = np.where(arr == 3)

print(found)

print(np.where(arr % 2 == 0))

print(np.sort(arr))

arr = np.array([[55, 43, 21], [99, 0, 12],[3, 22, 35],[22, 22, 1]])

print(arr)
print(np.sort(arr))