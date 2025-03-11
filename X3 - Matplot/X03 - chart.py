#https://www.w3schools.com/python/matplotlib_pie_charts.asp

import matplotlib.pyplot as plt

labels = ["label one", "label 2", "label three"]
percentage = [33, 22, 45]

plt.pie(percentage, labels=labels)
plt.show()