from geometric_shapes import Rectangle
from geometric_shapes import Circle
from geometric_shapes import Cube
from geometric_shapes import Sphere
import unittest

class Test_Geometric_Shapes(unittest.TestCase):
    def setUp(self) -> None:
        self.xPoint, self.yPoint, self.zPoint, self.width, self.height, self.depth, self.radius = 0, 0, 0, 3, 4, 5, 5

    def creat_Rectangle(self) -> "Rectangle":
        return Rectangle(self.xPoint, self.yPoint, self.width, self.height)

    def creat_Circle(self) -> "Circle":
        return Circle(self.xPoint, self.yPoint, self.radius)

    def creat_Cube(self) -> "Cube":
        return Cube(self.xPoint, self.xPoint, self.zPoint, self.width, self.height, self.depth)

    def creat_Sphere(self) -> "Sphere":
        return Sphere(self.xPoint, self.xPoint, self.zPoint, self.radius)

    ## Testing starts here - all tests must start with test_

    ## Test: creat rectangles
    def test_creat_rectangle(self):
        rec = self.creat_Rectangle()

    ## Test Rectangle errors
    def test_empty_rectangle(self):
        with self.assertRaises(TypeError):
            rec = Rectangle()
    
    def test_creat_invalid_rectangle(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(0, 0, "Two", 5)

    def test_to_large_width(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(0, 0, 42, 5)

    def test_to_large_height(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(0, 0, 4, 69)

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

    ## Test Creat circle

    def test_creat_circle(self):
        c = self.creat_Circle()

    ## Test Circle errors
    def test_creat_empty_circle(self):
        with self.assertRaises(TypeError):
            c = Circle()
    
    def test_creat_invalid_circle(self):
        with self.assertRaises(ValueError):
            c = Circle(0, 0, "Fem")

    def test_to_large_radius(self):
        with self.assertRaises(ValueError):
            c = Circle(0, 0, 48)

    ## Test __eq__ ==
    def test_equal_circle(self):
        c1 = self.creat_Circle()
        c2 = Circle(0, 0, 5)
        self.assertEqual(c1, c2)

    def test_not_equal_circle(self):
        c1 = self.creat_Circle()
        c2 = Circle(0, 0, 6)
        self.assertNotEqual(c1, c2)

    def test_circle_area(self):
        c1 = Circle(0, 0, 5)
        c1.area_calulator()

    def test_circle_circumference(self):
        c1 = Circle(0, 0, 5)
        c1.circumference_calulator()

    ## Test: Creat cube

    def test_creat_cube(self):
        cube = self.creat_Cube()

    ## Test: Cube errors

    def test_empty_cube(self):
        with self.assertRaises(TypeError):
            cube = Cube()

    def test_creat_invalid_cube(self):
        with self.assertRaises(ValueError):
            cube = Cube(0, 0, 0, 5, "Två", 6)

    ## Test __eq__ ==

    def test_equal_cubes(self):
        cube1 = self.creat_Cube()
        cube2 = Cube(0, 0, 0, 3, 4, 5)
        self.assertEqual(cube1, cube2)

    def test_not_equal_cubes(self):
        cube1 = self.creat_Cube()
        cube2 = Cube(0, 0, 0, 3, 6 ,2)
        self.assertNotEqual(cube1, cube2)

    ## Test: Volume and surface
    def test_cube_volume(self):
        cube = Cube(0, 0, 0, 2, 2, 2)
        cube.volume_calulator()

    def test_cube_surface(self):
        cube = Cube(0, 0, 0, 2, 2, 2)
        cube.surface_calculator()

    ## Test: Creat sphere
    
    def test_creat_sphere(self):
        sphere = self.creat_Sphere()

    ## Test: Sphere errors

    def test_empty_sphere(self):
        with self.assertRaises(TypeError):
            sphere = Sphere()

    def test_creat_invalid_sphere(self):
        with self.assertRaises(ValueError):
            sphere = Sphere(0, 0, 0, "Tre")

    ## Test __eq__ ==

    def test_equal_spheres(self):
        sphere1 = self.creat_Sphere()
        sphere2 = Sphere(0, 0, 0, 5)
        self.assertEqual(sphere1, sphere2)

    def test_not_equal_spheres(self):
        sphere1 = self.creat_Sphere()
        sphere2 = Sphere(0, 0, 0, 2)
        self.assertNotEqual(sphere1, sphere2)

    def test_sphere_volume(self):
        sphere = Sphere(0, 0, 0, 2)
        sphere.volume_calulator()

    def test_sphere_surface(self):
        sphere = Sphere(0, 0, 0, 5)
        sphere.surface_calculator()

if __name__ == "__main__":
    unittest.main()