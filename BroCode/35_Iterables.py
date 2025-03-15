# Iterables: An iterable is an object or collection that can return it's element one at a time, allowing it to be iterated over in a loop
# e.g. Lists, Tuples, Sets, String, etc. 

numbers = [1, 2, 3, 4, 5]

print("Iterating Forward: ")
for number in numbers:
    print(number)
print()

print("Iterating Backwards: ")
for number in reversed(numbers):
    print(number)
print()



# The set iterable isn't reversible as it doesn't persist it's order. As a result if we try to reverse a set we encounter a TypeError that states that set is not reversible. 

fruits = {"apple", "banana", "Cherry", "Dragonfruit"}

print("Set of fruits: ")
for fruit in fruits: 
    print(fruit)
print()


# This will raise a TypeError 
# print("Set of fruits reversed: ")
# for fruit in reversed(fruits): 
#     print(fruit)
# print()


name = "Xionex"
for character in name: 
    print(character)
print()


my_dict = {"name": "Xionex", "age": 20, "roll":2451, "section":"2F"}
for key, value in my_dict.items():
    print(f"{key}: {value}")