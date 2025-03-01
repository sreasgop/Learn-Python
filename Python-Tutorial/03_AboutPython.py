from decimal import Decimal
from fractions import Fraction


# Data Types in Python
num0 = 7
num1 = 17
num2 = 3.1
num3 = 5 + 2j
num4 = Decimal('3.14159')
num5 = Fraction(16, 10)
string = "Python"

print("Python Data Types: ")
print(type(num1),"e.g.",num1)
print(type(num2),"e.g.", num2)
print(type(num3),"e.g.", num3)
print(type(num4),"e.g.",num4)
print(type(num5),"e.g.", num5)
print(type(string), "e.g.", string)
print()

print("Numeric Operations in Python:")
print("Addition:", num0 + num1)
print("Subtration:", num0 - num1)
print("Multiplication:", num0 * num1)
print("Normal Division:", num1/num2)
print("Floor Division:", num1//num2)
print("Modulus:", num1%num2)
print("Exponents:", num2**2)
print()

print("Basic String Operations in Python:")
print("Strings can be declared using single quotes, double quotes, and triple quotes.")
print('Python')
print("is")
print('''a lot
    FUN!''')
print("Python""Programming")    # Two strings placed next to each other will be concatenated.
print("")
