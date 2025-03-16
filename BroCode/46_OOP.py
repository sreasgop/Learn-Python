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


# WHAT IS A CLASS VARIABLE?
# A class variable is a variable that doesn't only belong to one of the objects of a class. Unlike instance variables a class variable is shared among all the instances of a class
# A class variable is defined outside the constructor. 
# It allows us to share data among all the objects created from the same class. 

class Student:

    # Class Variable for the Student class, belongs to this class and is shared among all the instances of this class.
    class_year = 2025
    num_of_students = 0

    def __init__(self, name, age):
        self.name = name 
        self.age = age
        Student.num_of_students += 1    # In case of modifying a class variable in place of self, we use the name of the class.

   
stud1 = Student("Xonex", 20)
stud2 = Student("Sanjib", 21)
stud3 = Student("Ankit", 19)
stud4 = Student("Mohit", 22)

# We can very well call the class variable using an object of that class because a class variable belongs to all objects of a class. 
# But this is not the recommened way to use a class variable, we should call a class variable using the name of the class rather. 
print("Graduating year of stud1:",stud1.class_year)
print("Graduating Year of the Class:", Student.class_year)  #Recommended usage of class variable
print("Total number of students:", Student.num_of_students)
print(f"Class of year {Student.class_year} has {Student.num_of_students} students:")
print(stud1.name)
print(stud2.name)
print(stud3.name)
print(stud4.name)
print()

# A variable name simply is a pointer or a reference to the memory. 
# The id() method prints the memory location in integer format.
print(hex(id(stud1)))

# And simply trying to print an object, class the object.__repr__() dunder method. 
# The __repr__() dunder method prints the memory address in hexadecimal
print(stud1)                # Both are the same thing.
print(stud1.__repr__())




