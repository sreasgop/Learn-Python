# super() : Super method is used in a child class to call methods from a parent class (superclass)
# It helps us to extend the functionality of the inherited methods. 

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self._is_filled = is_filled

    def show(self):
        print(f"It is a {self.color} colored {type(self).__name__} and {'filled' if self._is_filled else "not filled"}.",)



class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    # Overriding the show method: 
    def show(self):
        # We can also call other methods of the parent class using super() function
        super().show()
        print(f"It is a Circle with an area of {3.14 * (self.radius ** 2):.2f} cm^2")


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def show(self):
        # We can also call other methods of the parent class using super() function
        super().show()
        print(f"It is a Square with an area of {(self.width ** 2):.2f} cm^2")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def show(self):
        # We can also call other methods of the parent class using super() function
        super().show()
        print(f"It is a Square with an area of {1/2 * self.width * self.height:.2f}cm^2")

c1 = Circle("Red", True, 5.5)
s1 = Square("Blue", False, 10)
t1 = Triangle("Yellow", True, 5, 8)


c1.show()
print()
s1.show()
print()
t1.show()