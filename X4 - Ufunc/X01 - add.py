#https://www.w3schools.com/python/numpy/numpy_ufunc.asp

import numpy as np

array_a = np.array([1,2,3,4])
array_b = np.array([4,5,6,7])

array_ab = np.add(array_a,array_b)
array_c = np.append(array_b, array_a)

print(array_ab)

print(array_c)