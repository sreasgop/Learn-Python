# Static method is a type of method that belongs to a class rather than any object from that class. A static method is shared among all the objects
# Such kind of method isn't dependent on any attributes of the class as a result doesn't need an instance of the object to be called. 
# Static methods are used for general utility functions. 

# Instance methods: Best for operations on instances of the class 
# Static method: Best for utility functions that do not need access to class data


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
    def __str__(self):
        return f"Employee [name: {self.name}, position: {self.position}]"
    
emp1 = Employee("Sanjib", "Janitor")
emp2 = Employee("Neeraj", "Cashier")
emp3 = Employee("Xonex", "Manager")

print(emp1)
print(Employee.is_valid_position("Programmer"))