#https://www.w3schools.com/python/matplotlib_pyplot.asp

import matplotlib.pyplot as plt
import numpy as np

yVal = np.array([0, 100, 50, 1, 3])
xVal = np.array([-100, -50, 0, 10, 100])

plt.plot(xVal, yVal)
#plt.show()

plt.plot(xVal, yVal, 'o')
#plt.show()

plt.plot(xVal, yVal, marker='X', color = "#F00000")
plt.ylabel("y label")
plt.xlabel("x label")

plt.grid(color = "#0000FF")
plt.show()