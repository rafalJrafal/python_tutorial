class MyClass:
    def __init__(self):
        self.value = 77
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "The value stored is: " + str(self.value)
    def __eq__(self, value):
        return self.value == value.value

    value = 15

class MyClass2:
    def __str__(self):
        return str(self.data)
    data = (1, 3)

class MyBiggerClass(MyClass, MyClass2):
    def __init__(self, value, string_value):
        super().__init__(value)
        self.string_value = string_value
    string_value = "ala ma kota"

    def __str__(self):
        return "String is " + self.string_value + " " + MyClass.__str__(self) + " and " + MyClass2.__str__(self)
    
    def __eq__(self, value):
        return super().__eq__(value) or self.string_value.__eq__(value.string_value)

cls = MyClass(3)
cls_2 = MyClass(2)

print(cls.value)
print(cls)
print(type(cls))

print(cls == cls_2)

cls_3 = MyBiggerClass(value = 33, string_value="nothing")
cls_4 = MyBiggerClass(value = 44, string_value="nothing")

print(cls_3)
print(cls_4)
print(cls_3 == cls_4)