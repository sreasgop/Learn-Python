# List Comprehension: A concise way to create lists in Python. Compact and easier to read than traditional loops. 

# Numeric List Comprehensions 
doubles = [x * 2 for x in range(1, 11)]
triples = [x * 3 for x in range(1, 11)]
sqaures = [x * x for x in range(1, 11)]
cubes = [x*x*x for x in range(1, 11)]

print(doubles)
print(triples)
print(sqaures)
print(cubes)


# String List Comprehension
fruits = ["apple", "banana", "cherry", "coconut", "orange", "guava"]
fruits_upper = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]
fruit_capatalized = [fruit.capitalize() for fruit in fruits]
c_fruits = [fruit.capitalize() for fruit in fruits if fruit[0].lower() == 'c']

print(fruit_chars)
print(fruit_capatalized)
print(fruits_upper)
print(c_fruits)