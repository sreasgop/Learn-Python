# Duck Typing (Dynamic Polymorphism): Python follows "Duck Typing," meaning the actual class of an object is not as important as its behavior.
# "If it walks like a duck and quacks like a duck, then it must be a duck." 

# All these classes aren't related to each other, or in other words these classes aren't inherting anything from a common class. 
# They are all standalone classes and has nothing to do with the functioning of other classes. 

class Dog:
    alive = True 
    def __init__(self, name):
        self.name = name 
    
    def speak(self):
        print("WOOF!")


class Cat:
    alive = True 
    def __init__(self, name):
        self.name = name 
    
    def speak(self):
        print("MEOW!")


class Car: 
    alive = False
    def __init__(self, brand):
        self.name = brand 

    def speak(self):
        print("HONK!")


# This function isn't a method of any of the classes. It's a stand alone function. 
def ping_object(object):
    print(f"It is an object of {type(object).__name__} class.")
    print(f"It's name is: {object.name}")
    # print(f"It speaks like: {object.speak()}")
    print(f"It is alive: {object.alive}")
    print()



dog1 = Dog("Rocky")
cat1 = Cat("Tom")
car1 = Car("BMW")

ping_object(dog1)
ping_object(cat1)
ping_object(car1)
