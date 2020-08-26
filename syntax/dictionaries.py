#like hash tables
#has key value pairs
students = { "Bob": 12, "Rachel": 13, "Emily": 15}

#to access an item in a dictionary
print(students["Rachel"])

#to change the value of an itme in the dictionary
students["Rachel"] = 13.5
print(students["Rachel"])

#to delete item from dictionary
#del function
del students["Emily"]
print(students)

#to find the length of a dictionary
print(len(students))

#each key should be unique 
#if not it will use the last key entered
