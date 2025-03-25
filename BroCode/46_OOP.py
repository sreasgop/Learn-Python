# Object: A "bundle" of related attributes (variables) and methods (functions) 
#         Ex. phone, cup, book
#         We need a "class" to create objects of it's type. Using a class we can create many objects

# Class: A blueprint used to design the structure and layout of an object.      



class Car: 
    
    # Constructor method: It is a dunder method and we need this method to create/instantiate objects. 
    # This method behaves similary to a function, self refers to the current instance of the class. When we create an object, self refers to that very object. 
    def __init__(self, model, year, color, for_sale):
        # These variables are called instance variables, i.e. when an object is created each of them is going to have separate values for them. 
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    
    # Methods 


    # Overwriting the __str__ dunder method for the print() to be able to print the object
    def __str__(self):
        return f"{self.model}, {self.year}, {self.color}, {self.for_sale}"


# Instantiating an Object of class Car. 
car1 = Car("BMW", 2025, "Black", False)

# We can access the attribues of Car using . operator: 
print("model:",car1.model)
print("year:",car1.year)
print("color:",car1.color)
print("for_sale:",car1.for_sale)
print()
print(car1)
print()






