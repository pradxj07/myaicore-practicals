import datetime

class Person:
    def __init__(self,firstName, lastName, nickName, birthDate):
        self.firstName = firstName
        self.lastName = lastName
        self.nickName = nickName
        self.occupations = []
        self.hobbies = NotImplemented
        self.birthDate = birthDate
        self.isActive = True
        self.deathDate = None
        self.maritalStatus = None 
    
    def __eq__(self,another):
        same =  ((self.firstName == another.firstName) and (self.lastName == another.lastName) 
                and (self.birthDate == another.birthDate)
                )      
        return same
    
    def __getattr__(self,attr):
        if AttributeError:
            print(f"Value not set for {attr}")
        return None

    def __getattribute__(self, attr):
        print("Looking for " + attr)
        if attr == "isActive":
            return object.__getattribute__(self,"deathDate") == None and object.__getattribute__(self,"isActive") == True
        else:
            return object.__getattribute__(self,attr)

p1 = Person("P", "J", None, datetime.datetime(1980,1,1))
p2 = Person("P", "J", None, datetime.datetime(1970,1,1))
p3 = Person("P", "J", None, datetime.datetime(1980,1,1))

# Comparing objects 
checkp1p2 = (p1 == p2)
print(f"Is p1 same as p2? {checkp1p2}" )
# Not sure why this is not equal 
print(f"p1 is p3? {p1 is p3}" )
checkp1p3 = (p1 == p3)
print(f"Is p1 same as p3? {checkp1p3}" )
print(p3.__repr__())
# above line calls __getattribute__ 

#Another person 
p4 = Person("P", "J", "Pr", datetime.datetime(1980,1,1))
checkp1p4 = True if p1 is p4 else False

print(f"Is p1 same as p4? {checkp1p4}" )

# get attribute and set attibute 
print(p1)
print("Checking attr ====>")
print("p1 firstname " + str(p1.firstName))
## overriding getattribute for isactive 
print("p1 isalive with no deathdate?" + str(p1.isActive))
# changing death date 
p1.deathDate = datetime.date(2020,5,5) 
print("p1 isalive after deathdate? " + str(p1.isActive))
