#https://www.w3schools.com/python/numpy/numpy_copy_vs_view.asp
#https://www.w3schools.com/python/numpy/numpy_array_reshape.asp

import numpy as np

arr = np.array([[1,2,3], [4,5,6]])

print(arr.shape)

arr_2 = np.array([1,2,3,4,5], ndmin=4)

print("array", arr_2)
print("shape", arr_2.shape)

arr_big = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

print("array", arr_big)
print("shape", arr_big.shape)
print("reshaped 8,2\n", arr_big.reshape(8, 2))
print("reshaped 4,4\n", arr_big.reshape(4, 4))
#print("reshaped 4,6\n", arr_big.reshape(4, 6)) // error

print("is reshaped a copy", arr_big.reshape(4, 4).base)

arr_unknown_dim = arr_big.reshape(2, 2, -1)

print("unknown dimension\n", arr_unknown_dim)

arr_flat = arr_unknown_dim.reshape(-1)
print("flattened 1\n", arr_flat)
arr_flat = arr_unknown_dim.reshape(2, -1)
print("flattened 2\n", arr_flat)
