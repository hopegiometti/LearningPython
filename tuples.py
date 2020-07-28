#similar to lists
#immutable
#cannot be changed (deleted, updated, etc.)

#example
tup1 = ("oranges", "apples", "bananas")
print(tup1)

#can access the values
print(tup1[0])

#can splice
print(tup1[0:2])

#can add tups together
tup2 = (12, 13, 14)
tup3 = tup1 + tup2
print(tup3)

#can delete an entire tup
tup4 = ("hi", "hello")
del tup4