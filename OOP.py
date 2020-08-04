#classes
#broad --> can be anything
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print("Your name is " + self.name)
    
    def getAge(self):
        print("Your age is " + self.age)


#objects
#an instance of a class
# p = Person()
# print(p)
p1 = Person("Hope", "23")

#self refers to 
#the current object you have 
p1.getName()
p1.getAge()

#init function 
#see above