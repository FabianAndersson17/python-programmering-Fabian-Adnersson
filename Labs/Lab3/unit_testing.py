from geometric_shapes import Rectangle
import unittest

class Test_Geometric_Shapes(unittest.TestCase):
    def setUp(self) -> None:
        self.xPoint, self.yPoint, self.width, self.height = 0, 0, 3, 4

    def creat_Rectangle(self) -> "Rectangle":
        return Rectangle(self.xPoint, self.yPoint, self.width, self.height)

    ## Testing starts here - all tests must start with test_

    ## Test: creat rectangles
    def test_creat_rectangle(self):
        rec = self.creat_Rectangle()

    def test_empty_rectangle(self):
        with self.assertRaises(TypeError):
            rec = Rectangle()
    
    def test_creat_invalid_rectangle(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(0, 0, "Two", 5)

    ## Test __eq__ ==
    def test_equal_rectangles(self):
        rec1 = self.creat_Rectangle()
        rec2 = Rectangle(2, 6, 3, 4)
        self.assertEqual(rec1, rec2)

    def test_not_equal_rectangles(self):
        rec1 = self.creat_Rectangle()
        rec2 = Rectangle(2, 6, 1, 7)
        self.assertNotEqual(rec1, rec2)

    ## Test rectangle area and circumference
    def test_rectangle_area(self):
        rec1 = Rectangle(0, 0, 5, 6)
        rec1.area_calulator()

    def test_rectangle_circumference(self):
        rec1 = Rectangle(0, 0, 5, 6)
        rec1.circumference_calulator()


if __name__ == "__main__":
    unittest.main()