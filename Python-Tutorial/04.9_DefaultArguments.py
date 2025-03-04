# NOTE: Default Argument Values
# While creating a function we can specify a default value for one or more argument, this creates a function that can be called with fewer arguments than it is defined to allow. 

def fibonacci(term=10):
    a, b = 0, 1
    fib_sequence = []
    while term:
        fib_sequence.append(a)
        a, b = b, a+b
        term -= 1
    return fib_sequence

# Calling the function without any value explicitly mentioned, which will use the default value
print(fibonacci())

# Calling the function with a specific value, it will use the newly mentioned value
print(fibonacci(4))


# NOTE: The default values are evaluated at the point of function definition in the defining scope

i = 5
def f(arg=i):
    print(arg)

i = 6
f()     # Output: 5
