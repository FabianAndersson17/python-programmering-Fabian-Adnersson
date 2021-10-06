import math ## Imports the math module

class Geometric_Shapes(): 
    """A parent class that keeps track of the x and y coordinates of a shape"""
    def __init__(self, xPoint: float, yPoint: float) -> None:
        """Adds self, xPoint and yPoints as parameters"""
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
        """Creats new coordinates and changes the original coordinates to the new coordinates"""
        self.xPoint = newXpoint
        self.yPoint = newYpoint

    def __repr__(self) -> str:
        """Writes out a string if no other method is being used"""
        return (f"x-coordinate = {self.xPoint}, y-coordinate = {self.yPoint}")

class Rectangle(Geometric_Shapes):
    """A child class that inherits x and y from Geometric_Shapes and creats a width and a height"""
    def __init__(self, xPoint: float, yPoint: float, width: float, height: float) -> None:
        """Adds widht and height as parameters"""
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
        """Calculates the area of the rectangle with the given widht and height.
        Formula: widht*height"""
        return self.width * self.height
        

    def circumference_calulator(self) -> float:
        """Calculates the circumference of the rectagle with the given widht and height
        Formula: widht*2 + height*2"""
        return self.width*2 + self.height*2

    def translate(self) -> float:
        return super().translate()

    def __eq__(self, other: "Rectangle") -> bool:
        """Overloads the == operator to check if two given rectangle are equal"""
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
        """Adds radius as a parameter"""
        super().__init__(xPoint, yPoint)
        self.radius = radius

        if not isinstance(self.radius, (float, int)): ## Checks if radius is of type float or int
            raise ValueError(f"The radius must be a float or and int. Not: {type(self.radius)}")

        if not 0 < self.radius <= 10: ## Checks if above 0 but below 10
            raise ValueError(f"The radius needs to be above 0 but below 10. Not: {self.radius}")
        
    
    def area_calulator(self) -> float:
        """Calulates the area of the circle with the given.
        Formula: r^2*pi"""
        return (self.radius**2)*math.pi

    def circumference_calulator(self) -> float:
        """Calulates the circumference of the cirlce with the given radius. 
        Formula: 2*r*pi"""
        return (2*self.radius) * math.pi 

    def translate(self, newXpoint: float, newYpoint: float) -> float:
        return super().translate(newXpoint, newYpoint) ## Uses the inherited  parameters

    def __eq__(self, other: "Circle") -> bool:
        """Overloads the == to check if the two given Circles are equal"""
        return other.radius == self.radius

    def is_inside(self, xParameter, yParameter) -> True:
        """Checks if the given Circle is within the given parameters"""
        return self.radius <= xParameter and self.radius <= yParameter ## Checks if a circle is within given parameters
        
    def __repr__(self) -> str:
        return (f"x-coordinate: {self.xPoint}, y-coordinate: {self.yPoint}, radius: {self.radius}") ## String that overwrites the inherited methodes string

class Cube(Rectangle):
    """Grandchild class that inherits from Rectangle and from Geometric_Shapes"""
    def __init__(self, xPoint: float, yPoint: float, zPoint: float, width: float, height: float, depth: float) -> None:
        """Adds depth and zPoints as new parameters"""
        super().__init__(xPoint, yPoint, width, height)

        self.zPoint = zPoint
        self.depth = depth

        if not isinstance(self.depth, (float, int)): ## Checks if depth is a float or an int
            raise ValueError(f"The height must be a float or an int. Not: {type(self.depth)}")

        if not 0 < self.depth <= 10: ## Checks if depth is above 0 but below 10
            raise ValueError(f"The width needs to be above 1 but below 10. Not: {self.depth}")

        if not isinstance(self.zPoint, (float, int)):
            raise ValueError(f"yPoint needs to be a float or an int not {type(self.zPoint)}")

        if not -25 <= self.zPoint <= 25: ## Checks if the z parameter is above -25 and 25
            raise ValueError(f"The X coordinate needs to be between -25 and 25 not {self.zPoint}")

    def volume_calulator(self):
        """Calulates the volume of a Cube
        Formula: widht*height*depth"""
        return self.width * self.height * self.depth
        
    def surface_calculator(self):
        """Calulates the surface area of a Cube
        Fomula 2*(widht*height + widht*depth + height*depth)"""
        return 2*(self.width*self.height + self.width*self.depth + self.height*self.depth)

    def translate(self, newXpoint, newYpoint, newZpoint) -> float:
        self.xPoint = newXpoint
        self.yPoint = newYpoint
        self.zPoint = newZpoint

    def __eq__(self, other: "Cube"):
        """Overloads == operator to check if two given Cubes are equal"""
        return other.width == self.width and other.height == self.height and other.depth == self.depth

    def is_inside_point(self, xParameter: float, yParameter: float, zParameter: float) -> True:
        """Takes in a x, y and z parameter and checks if the widht, height and depth are within the parameters"""
        return self.width <= xParameter and self.width <= yParameter and self.width <= zParameter and self.height <= xParameter and self.height <= yParameter and self.height <= zParameter and self.depth <= xParameter and self.depth <= yParameter and self.depth <= zParameter
    
    def __repr__(self) -> str:
        return (f"x-coordinate: {self.xPoint}, y-coordinate: {self.yPoint}, z-coordinate: {self.zPoint}, widht: {self.width}, height: {self.height}, depth: {self.depth}")

class Sphere(Circle):
    """Grandchild class that inherits from cirlce and Geometric_Shapes"""
    def __init__(self, xPoint: float, yPoint: float, zPoint: float, radius: float) -> None:
        """Adds zPoint as a parameter"""
        super().__init__(xPoint, yPoint, radius)

        self.zPoint = zPoint
        
        if not isinstance(self.zPoint, (float, int)): ## Checks if the given zPoint is a float or an int
            raise ValueError(f"yPoint needs to be a float or an int not {type(self.zPoint)}")

        if not -25 <= self.zPoint <= 25: ## Checks if the z parameter is above -25 and 25
            raise ValueError(f"The X coordinate needs to be between -25 and 25 not {self.zPoint}")

    def volume_calulator(self):
        """Calulates the volume of the sphere
        Formula: (4/3)*pi*r^3"""
        return (4/3)*math.pi*(self.radius**3)

    def surface_calculator(self):
        """Calulates the surface area of the sphere
        Formula: 4*pi*r^2"""
        return 4*math.pi*(self.radius**2)
    
    def translate(self, newXpoint: float, newYpoint: float, newZpoint: float) -> float:
        self.xPoint = newXpoint
        self.yPoint = newYpoint
        self.zPoint = newZpoint

    def  __eq__(self, other: "Sphere") -> bool:
        """Overloads the == operator and checks if two spheres are equal"""
        return super().__eq__(other)
    
    def is_inside(self, xParameter, yParameter, zParameter) -> True:
        """Checks if given Sphere's radius is with in a x, y and z parameter"""
        return self.radius <= xParameter and self.radius <= yParameter and self.radius <= zParameter

    def __repr__(self) -> str:
        return (f"x-coordinate: {self.xPoint}, y-coordinate: {self.yPoint}, z-coordinate: {self.zPoint}, radius: {self.radius}")