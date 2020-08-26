#comma separated values
#allows us to access any value
#based of off index 
#uses []
#index starts at 0 

shopping = ["oat milk", "bananas", "strawberries", "bloobs"]
# print(shopping[3])

#adding to a list
#append function
#adds to the end
shopping.append("nooch")

#replaces the item in the beginning
shopping[0] = "spaghetti"

#delete items
#del function
#give index
del shopping[2]
# print(shopping)

#get length of list
# print(len(shopping))

shop2 = ["bread", "jelly", "pb"]

#can add lists together
# print(shopping + shop2)
#can multiply lists
# print(shopping * 2)

#number lists
listNum = [1, 3, 7, 9, 11]
#find max
print(max(listNum))
#find min
print(min(listNum))

#is there a difference b/w lists in python and arrays in JS?
