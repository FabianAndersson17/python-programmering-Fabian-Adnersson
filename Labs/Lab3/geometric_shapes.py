import math

class Geometric_Shapes():
    def __init__(self, xPoint: float, yPoint: float, radius: float) -> None:
        self.xPoint = xPoint
        self.yPoint = yPoint
        self.radius = radius
        self.diameter = radius*2
        if not isinstance(self.xPoint, (float, int)):
            raise ValueError(f"xPoint needs to be a float or an int not {type(self.xPoint)}")
        if not isinstance(self.yPoint, (float, int)):
            raise ValueError(f"yPoint needs to be a float or an int not {type(self.yPoint)}")
        if not isinstance(self.radius, (float, int)):
            raise ValueError(f"radius needs to be a float or an int not {type(self.radius)}")
        if not -25 <= self.xPoint <= 25:
            raise ValueError(f"The X coordinate needs to be between -25 and 25 not {self.xPoint}")
        if not -25 <= self.yPoint <= 25:
            raise ValueError(f"The Y coordinate needs to be between -25 and 25 not {self.yPoint}")

    def area_calulator(self) -> float:
        return(self.diameter * self.diameter)
    
    def circumference_calulator(self) -> float:
        return self.diameter*4

    def __eq__(self, other: "Geometric_Shapes") -> bool:
        return other.radius == self.radius and other.diameter == self.diameter

    def translate(self, newXpoint, newYpoint) -> float:
        self.xPoint = newXpoint
        self.yPoint = newYpoint

    def is_inside(self) -> True:
        if self.xPoint <= self.radius and self.yPoint <= self.radius and self.xPoint <= self.diameter and self.yPoint <= self.diameter:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return (f"x-coordinate = {self.xPoint}, y-coordinate = {self.yPoint}, radius = {self.radius}, diameter = {self.diameter}")

class Square(Geometric_Shapes):
    def __init__(self, xPoint, yPoint, radius, height) -> None:
        super().__init__(xPoint, yPoint, radius)
        self.height = height

    def area_calulator(self) -> float:
        return self.diameter * self.height

    def circumference_calulator(self) -> float:
        return self.diameter*2 + self.height*2

    def translate(self) -> float:
        return super().translate()

    def __eq__(self, other: "Geometric_Shapes") -> bool:
        return super().__eq__(other)
    
    def is_inside_point(self) -> True:
        if self.xPoint <= self.diameter and self.xPoint <= self.height and self.yPoint <= self.diameter and self.yPoint <= self.height:
            return True
        else:
            return False 

    def __repr__(self) -> str:
        return (f"x-coordinate = {self.xPoint}, y-coordinate = {self.yPoint}, height = {self.height}, widht = {self.diameter}")

class Circle(Geometric_Shapes):
    def __init__(self, xPoint: float, yPoint: float, radius: float) -> None:
        super().__init__(xPoint, yPoint, radius)
    
    def area_calulator(self) -> float:
        return (self.radius**2)*math.pi

    def circumference_calulator(self) -> float:
        return self.diameter * math.pi

    def translate(self, newXpoint, newYpoint) -> float:
        return super().translate(newXpoint, newYpoint)

    def __eq__(self, other: "Geometric_Shapes") -> bool:
        return super().__eq__(other)

    def is_inside(self) -> True:
        return super().is_inside()
        
    def __repr__(self) -> str:
        return super().__repr__()