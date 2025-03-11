#https://www.w3schools.com/python/numpy/numpy_ufunc_create_function.asp

import numpy as np

def usedFunction(param1, param2):
    return param1 * 2 + param2

array_a = np.array([1,2,3,4,5])
array_b = np.array([0,9,8,7,6])

generatedFunc = np.frompyfunc(usedFunction, 2, 1)
resultArray = generatedFunc(array_a, array_b)

print(resultArray)