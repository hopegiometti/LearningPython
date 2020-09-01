#how to read a file in python
#open creates file objects
#arg is file path
myfile = open("fruits.txt")


#file cursor
#when you apply read method, cursor moves to end of text file
#before read, starts at beginning
#if you apply another read method, it will just print an empty string
#because read has already happened
#to fix
#save content in variable --> then you can print as much as you want
content = myfile.read()


#closing a file
#saves memory --> uses up memory when its open/when you are processing it
myfile.close()
#once closed, you cannot read

print(content)

#better way to do everything above?
#with 
with open("fruits.txt") as myfiletwo:
    contenttwo = myfiletwo.read()

print(contenttwo)
#with will apply close function implicitly

#different file paths
#make sure to specify complete path to your file, relative to whatever file you are working in!

#writing text to a file
with open("files/veggies.txt", "w") as anotherfile:
    anotherfile.write("tomato\ncucumber\nonion")

with open("files/veggies.txt") as myfilethree:
    contentthree = myfilethree.read()

print(contentthree)

#appending text to an existing file
#use 'a' method
#use seek method to return cursor back to beginning
#use + to make readable?

with open("files/veggies.txt", "a+") as myfilefour:
    myfilefour.write("\ngarlic")
    myfilefour.seek(0)
    contentfour = myfilefour.read()

print(contentfour)
