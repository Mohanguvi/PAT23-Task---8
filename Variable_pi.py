class Circle:   # Class blueprint of Circle is given
    
    def __init__(self, List):  # constrcutor method is called
        self.circle = List     # New object "List" is initiated

    def Pi(self): # Class Pi created
        self.Value = pi
        print(f"The Pi value is :{pi}")
        
    def display(self):
        print(f"Given Circle List :{self.circle}")

# Arguement List given
List = [10, 501, 22, 37, 100, 999, 87, 351]
pi = 3.141  #private class 'pi=3.141' variable added

construct_Circle = Circle(List)  # Create an instance of the Circle class
Pi_value = Circle(pi)            # Create an instance of the Circle class

construct_Circle.display()       # display the given circle list
Pi_value.Pi()                    # display the variable pi
