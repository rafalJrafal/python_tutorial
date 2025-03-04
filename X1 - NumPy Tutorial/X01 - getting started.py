#https://www.w3schools.com/python/numpy/numpy_getting_started.asp

import numpy


print("Numpy version", numpy.__version__)

arr = numpy.array([1, 2, 3, 4])

print(arr)
print(type(arr))

arr = numpy.array([[1,2,3],[4,5,6]])
print(arr, "number of dimentions", arr.ndim)

arr = numpy.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr, "number of dimentions", arr.ndim)