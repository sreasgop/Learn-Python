# Implementing Match Case in Python
# Write a Python program that takes two numbers and an operator (+, -, *, /, %) as input from the user and performs the corresponding operation using match case.

# num1 = int(input("Enter the first number: "))
# char = input("Enter operator (+, -, *, /): ")
# num2 = int(input("Enter the second number: "))
#
# match char: 
#     case '+':
#         print("Sum:",num1+num2)
#     case '-':
#         print("Difference:", num1-num2) 
#     case '*':
#         print("Product:", num1*num2)
#     case '/':
#         print("Quotient:", num1/num2)
#     case _:
#         print("Invalid Operator, please try again!")


# Implementing the calculator program using Object Oriented Programming
class Calculator:
    def __init__(self, num1, num2, char):
        self.num1 = num1
        self.num2 = num2 
        self.char = char

    def calculate(self):
        match self.char:
            case '+':
                print("Sum:", self.num1+ self.num2)
            case '-':
                print("Difference:", self.num1 - self.num2) 
            case '*':
                print("Product:", self.num1 * self.num2)
            case '/':
                print("Quotient:", self.num1 / self.num2)
            case _:
                print("Invalid Operator, please try again!")


c1 = Calculator(10, 20, '+')
c1.calculate()
