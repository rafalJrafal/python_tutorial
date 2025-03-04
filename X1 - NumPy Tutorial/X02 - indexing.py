#https://www.w3schools.com/python/numpy/numpy_array_indexing.asp

import numpy as np

arr = np.array([1,2,3,4,5,6])

print(arr[3])

print(arr[3] + arr[0])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr, "dimension", arr.ndim)
print(arr[1, 3])

arr = np.array([
    [[1, 2, 3],[4, 5, 6]], 
    [[7,8,9],[10,11,12]],
    [[13,14,15],[16,17,18]]
    ])

print(arr, "dimentions", arr.ndim, "element", arr[2, 0, 2])
print("last", arr[-1,-1,-1])

