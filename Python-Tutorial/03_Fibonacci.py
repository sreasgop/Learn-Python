# Fibonacci Number: 

n = int(input("Enter nth term: "))
a, b = 0, 1
while a < n:
    print(a, end=' ')
    a, b = b, a+b
print()
