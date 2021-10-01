import math ## Imports the math module

## TODO add docsstrings and typeInting
class Geometric_Shapes(): 
    """A parent class that keeps track of the x and y coordinates of a shape"""
    def __init__(self, xPoint: float, yPoint: float) -> None: ## Gives Geometric_Shapes. Self, xPoint and yPoint parameters
        self.xPoint = xPoint ## Creats self.xPoint as a variable and gives it the value of the xPoint parameter
        self.yPoint = yPoint
        if not isinstance(self.xPoint, (float, int)): ## Checks if the input x and y parameters are floats of ints
            raise ValueError(f"xPoint needs to be a float or an int not {type(self.xPoint)}")
        if not isinstance(self.yPoint, (float, int)):
            raise ValueError(f"yPoint needs to be a float or an int not {type(self.yPoint)}")

        if not -25 <= self.xPoint <= 25: ## Checks if the x and y parameters are above -25 and 25
            raise ValueError(f"The X coordinate needs to be between -25 and 25 not {self.xPoint}")
        if not -25 <= self.yPoint <= 25:
            raise ValueError(f"The Y coordinate needs to be between -25 and 25 not {self.yPoint}")

    def translate(self, newXpoint, newYpoint) -> float:
        """Creats a new x and y parameter that changes the main x and y points to the new given values"""
        self.xPoint = newXpoint
        self.yPoint = newYpoint

    def __repr__(self) -> str:
        """Writes out a string with x and y points if no other method is being used"""
        return (f"x-coordinate = {self.xPoint}, y-coordinate = {self.yPoint}")

class Rectangle(Geometric_Shapes):
    """A child class that inherits x and y from Geometric_Shapes and creats a width and a height"""
    def __init__(self, xPoint: float, yPoint: float, width: float, height: float) -> None: ## Adds widht and height as parameters.
        super().__init__(xPoint, yPoint)
        self.width = width
        self.height = height
        if not isinstance(self.width, (float, int)): ## Checks if widht and height are of type float or type string
            raise ValueError(f"The widht must be a float or an int. Not: {type(self.width)}")
        if not isinstance(self.height, (float, int)):
            raise ValueError(f"The height must be a float or an int. Not: {type(self.height)}")

        if not 0 < self.width <= 10: ## Checks if width and height are above 0 but below 10
            raise ValueError(f"The width needs to be above 1 but below 10. Not: {self.width}")
        if not 0 < self.height <= 10:
            raise ValueError(f"The height needs to be above 1 but below 10. Not: {self.height}")


    def area_calulator(self) -> float:
        """Takes the width times the height to calulate the area of the rectangle"""
        return self.width * self.height
        

    def circumference_calulator(self) -> float: ## Calulates the circumference of a rectangle
        """Takes the width multiplied by two and the height multiplied two and adds them together"""
        return self.width*2 + self.height*2

    def translate(self) -> float:
        """Inherits the translate method from Geometric_Shapes"""
        return super().translate()

    def __eq__(self, other: "Rectangle") -> bool:
        """Overloads the == operator to check if one rectangle is equal to another"""
        return other.width == self.width and other.height == self.height
    
    def is_inside_point(self, xParameter: float, yParameter: float) -> True:
        """Takes in a x and a y parameter and checks if the given rectangle is with in the two parameters"""
        return self.width <= xParameter and self.width <= yParameter and self.height <= xParameter and self.height <= yParameter

    def __repr__(self) -> str:
        """Prints a string with the given values if no other method is being used"""
        return (f"x-coordinate = {self.xPoint}, y-coordinate = {self.yPoint}, width = {self.width}, height = {self.height}")

class Circle(Geometric_Shapes):
    """Child class circle that inherits from Geometric_Shapes"""
    def __init__(self, xPoint: float, yPoint: float, radius: float) -> None:
        """Inherits x and y point from Geometric_Shapes and adds radius as a parameter"""
        super().__init__(xPoint, yPoint)
        self.radius = radius

        if not isinstance(self.radius, (float, int)): ## Checks if radius is of type float or int
            raise ValueError(f"The radius must be a float or and int. Not: {type(self.radius)}")

        if not 0 < self.radius <= 10: ## Checks if above 0 but below 10
            raise ValueError(f"The radius needs to be above 0 but below 10. Not: {self.radius}")
        
    
    def area_calulator(self) -> float:
        """Calulates the area of the circle with the given radius^2 multiplied by pi"""
        return (self.radius**2)*math.pi

    def circumference_calulator(self) -> float:
        """Calulates the aea of the cirlce with the radius multipied by two then multiplied by pi"""
        return (2*self.radius) * math.pi 

    def translate(self, newXpoint: float, newYpoint: float) -> float:
        return super().translate(newXpoint, newYpoint) ## Uses the inherited values and parameters

    def __eq__(self, other: "Circle") -> bool:
        """Overloads the == to check if a two circles are the same"""
        return other.radius == self.radius

    def is_inside(self, xParameter, yParameter) -> True:
        return self.radius <= xParameter and self.radius <= yParameter ## Checks if a circle is within given parameters
        
    def __repr__(self) -> str: ## Returns a string if no other method is in use
        return (f"x-coordinate: {self.xPoint}, y-coordinate: {self.yPoint}, radius: {self.radius}")