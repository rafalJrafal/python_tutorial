#https://www.w3schools.com/python/numpy/numpy_random.asp

from numpy import random as rnd

for i in range(20):
    value = rnd.randint(10)
    print(f"random value = {value}")


print(rnd.randint(100, size = 55))
print(rnd.randint(100, size = (5,5)))

print(rnd.choice([3, 4, 1, 19], (3,4)))