class BaseClass:
    def __init__(self, name):
        self.name = name

    def shout(self):
        print("Base shout")
    

class Child_A(BaseClass):
    def __init__(self, name):
        BaseClass.__init__(self, name)
    
    def shout(self):
        print("Child_A shout", self.name)

class Child_B(BaseClass):
    def __init__(self, name):
        BaseClass.__init__(self, name)

    def shout(self):
        print("Child_B shout", self.name)

class Child_C(BaseClass):
    def __init__(self, name):
        BaseClass.__init__(self, name)

    def shout(self):
        print("Child_C shout", self.name)

for element in (Child_A("ala"), Child_B("ola"), Child_C("ela")):
    element.shout()