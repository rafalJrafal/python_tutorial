#https://www.w3schools.com/python/numpy/numpy_data_types.asp

import numpy as np

arr = np.array([1, 2, 3, 4, 5], dtype='S')

print(arr.dtype)
for element in arr:
    print(type(element), " - ", element)

arr_new = arr.astype('i')

print(arr_new.dtype)
for element in arr_new:
    print(type(element), " - ", element)


arr = np.array([1.1, 1.2, 1.3])
print(arr)
print(arr.astype('i'))
