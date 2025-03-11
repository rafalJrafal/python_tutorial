import matplotlib.pyplot as plt
import numpy as np

array = np.random.normal(170, 20, 500)

print(array)

plt.hist(array)
plt.show()