variable_a = "string"
print(type(variable_a))

variable_b = 2 + 3j
variable_c = 3 + 6j
variable_d = variable_b + variable_c
print(type(variable_d), variable_d)

varStr = "5"
print("String ", type(varStr))

varStr = 5
print("Int ", type(varStr))

varInt = 5
varStr = str(varInt)
print("str(int) ", type(varStr))