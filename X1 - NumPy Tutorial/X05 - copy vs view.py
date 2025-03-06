#https://www.w3schools.com/python/numpy/numpy_copy_vs_view.asp

import numpy as np

arr = np.array([1, 3, 4, 5, 2, 6, 4, 5, 1])

print("original         ", arr)

arr_copy = arr.copy()
arr_copy[-1] = 884561

print("after copy change", arr)

arr_view = arr.view()
arr_view[3] = 8

print("after view change", arr)

arr[4] = 8

print("after orig change", arr)
print("view after change", arr_view)
print("copy after change", arr_copy)

print("array base", arr.base)
print("view base", arr_view.base)