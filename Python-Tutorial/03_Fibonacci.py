# Fibonacci Number: 

# n = int(input("Enter nth term: "))
# a, b = 0, 1
# while a < n:
#     print(a, end=' ')
#     a, b = b, a+b
# print()


# In this program we are generating the fibonacci series till the term is less than the entered value n. However if we want to create the fibonacci series till nth term we are supposed to do it in this manner. 

# Genrating Fibonacci Series till nth term: 
n = int(input("Enter nth term: "))
a, b = 0, 1     # Setting the value of first two terms using multiple assignment of Python
while n:
    print(a, end=" ")
    a, b = b, a+b
    n -= 1
print()


