#for loops

# list1 = ["apples", "bananas", "cherries"]
# tup1 = (10, 11, 7)

# for item in list1:
#     print(item)

# for item in tup1:
#     print(item)

#range functions
#will print 1-9
#not inclusive
# for i in range(0,10):
#     print(i)

#will only print even numbers
# for i in range(0,11,2):
#     print(i)

#will print every 5
# for i in range(0,51,5):
#     print(i)

#nested for loops
# for i in range(0,5):
#     for j in range(0,3):
#         print(i*j)

#while loops

c = 0
# while c < 5:
#     print(c)
#     c = c + 1

#control statements
#break
#terminates the loop
# while c < 5:
#     print(c)
#     if c == 3:
#         break
#     c = c + 1

#continue
#use when you don't want the rest of code in your while loop to run
#but you want it to continue iterating
# while c < 5:
#     c = c + 1
#     if c == 3:
#         continue
#     print(c)

#pass
#filler null statement
#if you dont know what you need to write
#but you know code needs to be there
#use pass
while c < 5:
    c = c + 1
    if c == 3:
        pass
    print(c)


