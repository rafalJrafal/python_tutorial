import numpy as np

array_a = np.array([1,2,3,4,5])
array_b = np.array([6,7,8,9,0])

array = np.concatenate((array_a, array_b))

print(array)

print(np.split(array, 5))

print(np.array_split(array, 3))