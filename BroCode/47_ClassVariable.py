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
