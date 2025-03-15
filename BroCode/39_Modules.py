# Module: A file containing code we would want to inlcude in our programs. We use the import keyword to include a module in Python. 
# Modules are useful to break up large program into reuseable separate files. 

# To get a list of all the available built in modules we can use this command. 
# print(help("modules"))

# We can print the description of a module using the help keyword as well 
# print(help("math"))

# import math
# import math as m          # Importing using as keyword to set an alias (nickname)
# from math import pi       # using from keyword along with import to import a specific thing from a module

# print(pi)


# print(help("keywords"))


# A = 0o020
# Hex = 0xF
# print(A)
# print(Hex)

# from fractions import Fraction
# from decimal import Decimal

# value1 = Fraction(10,3)
# num1 = Decimal("10.0")
# num2 = Decimal("3.0")

# print(num1/num2)

a = 10 
b = 15
c = 20
d = 25
e = 30

b, a = a, b

val = a, b, c, d, e

print(f"A: {a}")
print(f"B: {b}")
print(type(val))

print("Soutrika", "Sreas", "Sanjib", "Sneha", sep=" ", end="\n")


print(type(10/3))