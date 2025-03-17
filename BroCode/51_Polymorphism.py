# Polymorphism : Greek work that means to "have many forms or faces"
#                Poly means many
#                Morphe means form

#                Two ways to achieve polymorphism:
#                1. Inheritance: An object could be treated of the same type as a parent class. 
#                2. "Duck Typing": Object must have necessary attributes/methods

from abc import abstractmethod

class Shape():
    # @abstractclassmethod is deprecated. 
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    

list_of_shapes = [Circle(4), Square(5), Triangle(6, 7)]
 
for shape in list_of_shapes:
    print(f"{shape.area()} cm²")