# Inheritance allows a class to inherit attributes and method from another class (it's parent class)
# It is one of the four main pillars of OOPs and it helps with code reusability and extensibility 

class Animal: 
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# We pass the name of the class that we want to inherit from, within the parenthesis of the child class. 
# We can then extend on the inherited qualities and add new methods to our child classes. 
class Dog(Animal):
    def speak(self):
        return "WOOF!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Mouse(Animal):
    def speak(self):
        return "SQUEEK!"


# Instantiating Objects of Dog(), Cat() amd Mouse() class
# We haven't defined anything for any of these classes but as we have made them all inherit from the Animal class, we can instantiate objects of these class using the constructor of the parent class Animal(). Also we can use all the methods defined in the parent class as well. 
dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Jerry")

# Calling methods of the parent class:
print(f"Name of our dog is: {dog.name}\nOur dog says, {dog.speak()}")
dog.eat()

print()

print(f"{cat.name} the cat says {cat.speak()} and {mouse.name} the mouse says {mouse.speak()}")
cat.eat()
mouse.sleep()