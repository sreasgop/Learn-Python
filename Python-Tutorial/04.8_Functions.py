# A function that doesn't return a value is known as a procedure.
# Functions in Python by default return the value None if no return value is explicitly mentioned. 

def product(num1, num2):
    '''
    This function calculate and prints the product of two entered numbers.
    '''
    print("Product:", num1 * num2)

# We can access the documentation, or docstrig of a function using the .__doc__ 
print(product.__doc__)
print("Return type of product() function: ", product(5, 10))   # Output: None


# A function definition associates the function name with the function object in the current symbol table. The interpreter recognizes the object pointed to by that name as a user-defined function. Other names can also point to that same function object and can also be used to access the function
p = product

p(8,9)

