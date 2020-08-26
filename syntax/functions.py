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

#in-built functions

#abs
#call it on any positive or negative number
#will get the absolute value of that number
abs(34)

#bool
#bool of zero is false
#bool of any other number is true
#bool of none is false
bool(0)

#dir
#gives you a list of anything you can do with a specific data type
#will show you built-in functions of that data type
dir("hello")

#help
#takes in a function name
#will show you what that function does
ex = "hello"
help(ex.upper)
help(ex.splitlines)

#eval
#run python code in a string format
ex2 = 'print("hi")'
eval(ex2)

#exec
#similar to eval
#for more complicated code
exec(ex2)

#converting data types
a = 1
str(a)
#"a"
float(a)
#1.0
int(a)
#1

