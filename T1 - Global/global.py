variable = "global version"

def someFunction_a():
    global variable
    variable = "local version updating global value"
    print(variable)


def someFunction_b():
    print(variable)

def someFunction_c():
    variable = "local version"
    print(variable)

someFunction_c()
someFunction_b()
someFunction_a()
someFunction_b()