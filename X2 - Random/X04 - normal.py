#https://www.w3schools.com/python/numpy/numpy_random_normal.asp

from numpy import random

import matplotlib.pyplot as plt

numbers = random.normal(50, 20, 10000)

print(numbers)
