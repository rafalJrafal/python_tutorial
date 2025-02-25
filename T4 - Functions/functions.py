#https://www.w3schools.com/python/python_functions.asp
#https://www.w3schools.com/python/python_lambda.asp

def singleParamFunction(param):
    print(param)

singleParamFunction(3)

def tupleArgumentFunction(*param):
    print(len(param))
    for x in param:
        print("param", x)

def dictionaryArgumentFunction(**param):
    print("keys:", param.keys())
    print("values:", param.values())

tupleArgumentFunction(1, 3, 4, 5, 12)
dictionaryArgumentFunction(one = "aaa", two = "bbb")

if 1 > 2:
    pass
elif 2 > 3:
    pass
else:
    print("a")

setX = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a, b, c, d, e, f, *g = setX
print(a, b, c, d, e, f, g)

print("a") if 22>9 else print("c")

nameOfLambda = lambda a, b :  a * b

print(nameOfLambda(2, 3))

def multiplier(n):
    lambdaFunc = lambda a : n * a
    return lambdaFunc

tripler = multiplier(3)

print(tripler(3))

def dividableBy(n):
    return lambda a : (a % n) == 0

isEven = dividableBy(2)
isDivByThree = dividableBy(3)

print("is even", isEven(12))
print("is mod 3", isDivByThree(91))
