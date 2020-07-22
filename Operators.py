#arithmetic
age1 = 12
age2 = 18

#sum
age1 + age2
#subtraction
age1 - age2
#multiplication
age1 * age2
#division
age1/age2

#modulos
#gives us the remainder
print(age2 % age1)

#strings
firstname = "Hope"
lastname = "Giometti"
print(firstname + " " + lastname)

#can't subtract (or divide) strings
#can multiply
print("Hi" * 10)

#every character in a string gets an index
#starting with 0 
sentence = "Hope was watching The Office"
#splicing
#doesn't include the ending position --> will only show you from 0 to 3
print(sentence[0:4])
#can use negative numbers
#will show you everything but last two characters
print(sentence[0:-2])