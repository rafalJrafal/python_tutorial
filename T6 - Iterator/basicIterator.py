tuple_x = (432, 567, 997)

iterator_x = iter(tuple_x)

print(next(iterator_x))
print(next(iterator_x))
print(next(iterator_x))

class Iterable:
    def __init__(self):
        self.val = 0
        
    def __iter__(self):
        self.val = 0
        return self

    def __next__(self):
        self.val+=1
        return self.val
    
x = Iterable()
print(type(x))
iterator_it = iter(x)

print(next(iterator_it))
print(next(iterator_it))
print(next(iterator_it))

