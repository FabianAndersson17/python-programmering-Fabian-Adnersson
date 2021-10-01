import unittest
from geometric_shapes import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y, self.width, self.height = 0, 0, 3, 4

    def creat_Rectangle(self) -> "Rectangle":
        return Rectangle(self.x, self.y, self.width, self.height)

    ## Testing starts here - all tests must start with rectangle_test_

    ## Test: creat rectangles

    def rectangle_test_creat(self) -> None:
        pass