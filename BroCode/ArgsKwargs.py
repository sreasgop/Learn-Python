# Arbitrary Arguments: Refers to the concept of passing a variable number of arguments to a function. 
# Arbitrary Positional Arguments (*args) : allows us to pass multiple non-keyword arguments
# Arbitrary Keyword Arguments (*kwargs): allows us to pass multiple keyword-arguments
#  * is called the unpacking opeartor. 



#################################
#             *args             #
#################################

# Whenever we use the * operator in the formal argument while defining a function, it makes a tuple out of the arguments passed while the function is called. The most important bit over here is the keep in mind the * unpacking operator, the formal argument can have any names but it's a convention to use "args" in this case.

# Example: 1
# def add(*args):
#     "Add any number of integers passed to the function"
#     total = 0
#     for arg in args: 
#         total += arg
#     return total

# # We can pass any number of arguments in a function that has *args in it's formal parameter during function definition.
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4, 5))
# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Example: 2
# def greet_user(*args):
#     print("Hello, ", end="")
#     for name in args:
#         print(name.capitalize(), end=" ")
#     return 0

# greet_user("chandra", "sreas", "gop")



################################
#            *kwargs           #
################################

# # Example:
# def print_address(**kwargs):
#     print("Address:")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(building_no="221B", landmark="Near Madison Housing Complex", street="Baker Street", city="London", country="Britain")