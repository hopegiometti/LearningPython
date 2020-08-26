#placeholders in strings

name = "Jake"
# print(name + " is 15 years old")

#use placeholders to do this more easily
sent1 = "%s is 15 years old"
print(sent1%name)

#can use placeholder multiple times in a string
sent2 = "%s %s is the Manager of %s %s Paper Company"
print(sent2%("Michael", "Scott", "Dunder", "Mifflin"))

#using placeholders on integers
#use %d
sent3 = "%s is %d years old"
print(sent3%("Hope", 23))
