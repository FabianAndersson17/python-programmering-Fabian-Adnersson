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

    def area_calulator(self) -> float:
        return(self.diameter * self.diameter)
    
    def circumference_calulator(self) -> float:
        return self.diameter*4

    def __eq__(self, other: "Geometric_Shapes") -> bool:
        return other.radius == self.radius and other.diameter == self.diameter

    def translate(self) -> float:
        pass

    def is_inside_point(self) -> True:
        pass

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
    
    def is_inside_point(self) -> True:
        return super().is_inside_point()

    def __repr__(self) -> str:
        return (f"x-coordinate = {self.xPoint}, y-coordinate = {self.yPoint}, height = {self.height}, widht = {self.diameter}")