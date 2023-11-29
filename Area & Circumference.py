class Circle:  # Base class of Circle insantiated 
    # Private class variable
    pi = 3.141

    def __init__(self, List): # Constructor method is used to set the ojects
        self.radius_list = List

    @classmethod              # Class method for area of circle 
    def Area_circle(cls, radius):
        return cls.pi * (radius**2)

    @classmethod              # Class method for Perimeter of circle 
    def Perimeter_circle(cls, radius):
        return 2 * cls.pi * radius

    def display(self, m, values):   # display function used to call and the get the values
        Values = ', '.join(map(str, values))
        print(f"{m}:{Values}")

# Given List
List = [10, 501, 22, 37, 100, 999, 87, 351]

# Constructing the circle in the list
circle_Construct = Circle(List)

# Calculate and display area of a circle in the list
areas = [Circle.Area_circle(r) for r in circle_Construct.radius_list]
circle_Construct.display("Areas", areas)

# Calculate and display Perimeter of a circle in the list
circumferences = [Circle.Perimeter_circle(r) for r in circle_Construct.radius_list]
circle_Construct.display("Circumferences", circumferences)

