import math

class Geometric_Shapes():
    def __init__(self, xPoint: float, yPoint: float) -> None:
        self.xPoint = xPoint
        self.yPoint = yPoint
        if not isinstance(self.xPoint, (float, int)):
            raise ValueError(f"xPoint needs to be a float or an int not {type(self.xPoint)}")
        if not isinstance(self.yPoint, (float, int)):
            raise ValueError(f"yPoint needs to be a float or an int not {type(self.yPoint)}")

        if not -25 <= self.xPoint <= 25:
            raise ValueError(f"The X coordinate needs to be between -25 and 25 not {self.xPoint}")
        if not -25 <= self.yPoint <= 25:
            raise ValueError(f"The Y coordinate needs to be between -25 and 25 not {self.yPoint}")

    def translate(self, newXpoint, newYpoint) -> float:
        self.xPoint = newXpoint
        self.yPoint = newYpoint

    def __repr__(self) -> str:
        return (f"x-coordinate = {self.xPoint}, y-coordinate = {self.yPoint}")

class Rectangle(Geometric_Shapes):
    def __init__(self, xPoint, yPoint, width, height) -> None:
        super().__init__(xPoint, yPoint)
        self.width = width
        self.height = height

    def area_calulator(self) -> float:
        return self.width * self.height

    def circumference_calulator(self) -> float:
        return self.width*2 + self.height*2

    def translate(self) -> float:
        return super().translate()

    def __eq__(self, other: "Rectangle") -> bool:
        return other.width == self.width and other.height == self.height
    
    def is_inside_point(self, xParameter, yParameter) -> True:
        return self.width <= xParameter and self.width <= yParameter and self.height <= xParameter and self.height <= yParameter

    def __repr__(self) -> str:
        return (f"x-coordinate = {self.xPoint}, y-coordinate = {self.yPoint}, width = {self.width}, height = {self.height}")

class Circle(Geometric_Shapes):
    def __init__(self, xPoint: float, yPoint: float, radius: float) -> None:
        super().__init__(xPoint, yPoint)
        self.radius = radius
    
    def area_calulator(self) -> float:
        return (self.radius**2)*math.pi

    def circumference_calulator(self) -> float:
        return (2*self.radius) * math.pi

    def translate(self, newXpoint, newYpoint) -> float:
        return super().translate(newXpoint, newYpoint)

    def __eq__(self, other: "Circle") -> bool:
        return other.radius == self.radius

    def is_inside(self, xParameter, yParameter) -> True:
        return self.radius <= xParameter and self.radius <= yParameter
        
    def __repr__(self) -> str:
        return super().__repr__()