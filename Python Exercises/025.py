class Person:
    # define the class parameter "name"
    name = "Person"

    
    def __init__(self, name = None):
        #self.name is the instance parameter
        self.name = name


jeffrey = Person("Jeffrey")
print(f"{Person.name} name is {jeffrey.name}")

nico = Person()
nico.name = "Nico"
print(f"{Person.name} name is {nico.name}")
