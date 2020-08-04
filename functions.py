#this is the function
def HelloWord():
    print("Hello World")

#now you have to call it
HelloWord()

def Greeting(name):
    print("Hi " + name + "!")

Greeting("Hope")

def Add(num1, num2):
    print(num1 + num2)

Add(1, 4)

#return statement
#python will stop running once return is called!
def ReturnAdd(num1, num2):
    return (num1 + num2)

sum = ReturnAdd(12, 34)

print(sum)