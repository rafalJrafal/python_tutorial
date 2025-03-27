import pandas

a = [1, 5, 7]

ser = pandas.Series(a)

print(ser)

ser = pandas.Series(a, index=['first', 'second', 'third'])

print(ser)

data = { 'day1': 11, 'day2': 34, 'day3':31, 'day4':9}

ser = pandas.Series(data, index=['day2', 'day4'])

print(ser)