import datetime

print("The date and time is", datetime.datetime.now())
# print(datetime.datetime.now())

#list comprehension
# temps = [221, 234, 340, 230]

# fixed_temps = []

# for temp in temps:
#     fixed_temps.append(temp / 10)

# print(fixed_temps)

# new_temps = [temp / 10 for temp in temps]
# print(new_temps)

#just if
# temps = [221, 234, 340, -9999, 230]
# new_temps = [temp / 10 for temp in temps if temp!= -9999]
# print(new_temps)

#need to change order for if/else!
# temps = [221, 234, 340, -9999, 230]
# new_temps = [temp / 10 if temp!= -9999 else 0 for temp in temps ]
# print(new_temps)

#functions w/ multiple args
def area(a, b):
    return a * b

#non keyword args
#position matters
print(area(4, 5))

#keyword args
#position doesn't matter!
print(area(a=4, b=5))

#funs w/ arbitrary number of non-keyword arg
#can be anything after *, but practice is args
def mean(*args):
    return sum(args) / len(args)

#with keyword argss
def mean(**kwargs):
    return kwargs

print(mean(a=2, b=7, c=5))