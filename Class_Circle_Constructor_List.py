class Circle:   # Class blueprint of Circle is given
    def __init__(self, List):  # constrcutor method is called
        self.name = List     # New object "List" is initiated

    def display(self):
        print(f"Given Circle List :{self.name}")


# Arguement List given
List = [10, 501, 22, 37, 100, 999, 87, 351]


construct_Circle = Circle(List)  # Create an instance of the Circle class
construct_Circle.display()       # display the given circle list