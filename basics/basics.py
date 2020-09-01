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

temps = [221, 234, 340, -9999, 230]
new_temps = [temp / 10 for temp in temps if temp!= -9999]
print(new_temps)
