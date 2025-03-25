# Magic Methods: Dunder (double underscore) methods like, __init__, __str__, __eq__ are special methods that are automatically called by many of Python's built-in functions and opeartions. These methods allow developers to define or write custom behavior of objects. 

class Book: 
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # Overloads the operator "=="
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return  f"{self.num_pages + other.num_pages} pages"

    # Overloading membership operator 'in' for objects of this class.
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    # Overloading indexing operator [] for objects of this class.
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"key '{key}' was not found!" 

    def __str__(self):
        return f"'{self.title}' by {self.author} consists of {self.num_pages}"
    


b1 = Book("Sapiens", "Yuval Noah Harari", 350)
b2 = Book("Sapien", "Yuval Noah Harari", 400)
b3 = Book("The Mid Night Library", "Matt Haig", 320)

print(b1)
print(b3)

print("b1 is equal to b2:",b1==b2)
print("b1 is greater than b3:",b1 > b3)
print("b1 is less than b3:",b1 < b3)
print(b1+b3)
print("Library" in b3)
print("Title of b3 object:",b3["title"])
print("Publisher of b3:", b3["publisher"])