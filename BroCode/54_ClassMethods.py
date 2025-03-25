# Class Methods: The Type of methods that allow operations related to the class itself. 
#                Such type of methods take (cls) as the first parameter, which represents the class itself. 


class Student: 

    count = 0
    total_sgpa = 0 

    def __init__(self, name, sgpa):
        self.name = name 
        self.sgpa = sgpa
        Student.count += 1
        Student.total_sgpa += sgpa     

    # Instance Method
    def get_info(self):
        return f"{self.name} {self.sgpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_sgpa(cls):
        if cls.count == 0:
            return 0
        return f"Average sgpa: {cls.total_sgpa/cls.count}"

s1 = Student("Sanjib", 6.2)
s2 = Student("Swati", 7.5)
s3 = Student("Xonex", 9.12)

print(Student.get_count())
print(Student.get_average_sgpa())