# input() function prompts the user to enter data. And it returns the entered data as a string. 

name = input("What's your name? :")
print(f"Hello, {name}!\nIt's nice to meet you.")

# No matter what we enter in the prompt, the input will return a string only.
print(type(name))