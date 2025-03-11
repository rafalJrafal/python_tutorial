#https://www.w3schools.com/python/numpy/numpy_random_permutation.asp

from numpy import random

x = random.choice([3, 5, 7], p=[0.1, 0.3, 0.6], size = (1000))

print(x)

x = random.choice([3, 5, 7], p=[0.1, 0.3, 0.6], size = (4,4))

print(x)

random.shuffle(x)

print(x)