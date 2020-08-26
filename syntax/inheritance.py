#might have a class person
#then sub classes of teens, adults, kids, etc.

#parent class
#has child classes
#that will inherit the parent's methods

class Parent:
    def __init__(self):
        print("This is the parent class")

    def parentFunc(self):
        print("This is the parent func")
    
    def test(self):
        print("parent")

p = Parent()
p.parentFunc()

#child inherits parent
class Child(Parent): 
    def __init__(self):
        print("This is the child class")
    
    def childFunc(self):
        print("This is the child function")
    
    def test(self):
        print("child")

c = Child()
c.childFunc()
#children inherit the methods/functions of their parents!
c.parentFunc()

#overwriting methods
#test method above
#when you reinitialize a function in a child class
#you will overwrite it
#and thus the one in the child one will run (when called by the child)
c.test()

