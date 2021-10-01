from geometric_shapes import Rectangle
import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.x, self.y, self.width, self.height = 0, 0, 3, 4

    def creat_Rectangle(self) -> "Rectangle":
        return Rectangle(self.xPoint, self.yPoint, self.width, self.height)

    ## Testing starts here - all tests must start with test_

    ## Test: creat rectangles

    def test_creat_rectangle(self) -> None:
        rec = self.creat_Rectangle()
        self.assertEqual(rec(self.xPoint, self.yPoint, self.width, self.height), (1, 2, 3, 4))

    def test_empty_rectangle(self):
        with self.assertEqual(ValueError):
            rec = Rectangle()
    
    def test_creat_invalid_rectangle(self):
        with self.assertEqual(TypeError):
            rec = Rectangle(0, 0, "Two", 5)