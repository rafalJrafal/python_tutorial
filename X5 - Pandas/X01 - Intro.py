import pandas

dataSet = {
    'car' : ["Merc", "BMW", "Tesla"],
    'seen' : [1, 4, 12]
}

print(type(dataSet))
myVariable = pandas.DataFrame(dataSet)

print(myVariable)