# NOTE: Functions can also be called using keyword arguments of the form kwarg=value


def printStudent(name, roll, section, department):
    print(f"Hello, {name}. \n\nHere are your details:")
    print(f"Roll: {roll}")
    print(f"Section: {section}")
    print(f"Department: {department}")

printStudent(roll=2451, name="Sreas", section="BCA 2F", department="Computer Application")