class Person:
    def getGender(self):
        return "Unknow"


class Male(Person):
    def getGender(self):
        return "Male"


class Female(Person):
    def getGender(self):
        return "Female"


# aPerson = Person()
aMale = Male()
aFemale = Female()
# print(aPerson.getGender())
print(aMale.getGender())
print(aFemale.getGender())
