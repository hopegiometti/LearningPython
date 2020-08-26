import datetime

print("The date and time is", datetime.datetime.now())
# print(datetime.datetime.now())

#list comprehension
temps = [221, 234, 340, 230]

fixed_temps = []

for temp in temps:
    fixed_temps.append(temp / 10)

print(fixed_temps)
