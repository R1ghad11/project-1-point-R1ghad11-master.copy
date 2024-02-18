"""
This file provide a set of unit tests. Each unit test will target
a specific functionality in your code that is explained in the
assignment requirements. 

For this test to work at all you have to create a file named
"point.py". Also, the file named point.py must have a class named
"Point".

Writing test cases before you write the code to be tested is
part of a method called "test-driven development", or "TDD".
It is widely used in industry. You should practice not only
using pre-written tests to gauge your progress, but also
writing your own test cases as part of your planning. Thus, 
you are encouraged to add your own test cases (although we will 
not grade them).
"""

import unittest
import point


class TestPoint(unittest.TestCase):

    def test_initializing_a_point(self):
        """This test should pass when you have defined the
        Point class with an __init__ method that initializes
        its x and y instance variables.
        """
        pt = point.Point(42, 89)
        self.assertEqual(pt.x, 42)
        self.assertEqual(pt.y, 89)

    def test_moving_a_point(self):
        """The 'move' method modifies the coordinates of a
        point.
        """
        pt = point.Point(13, 22)
        pt.move(17, 38)
        self.assertEqual(pt.x, 30)
        self.assertEqual(pt.y, 60)

    def test_points_equality(self):
        """The __eq__ method of Point should equate
        Point objects that have the same x and y coordinates.
        """
        p1 = point.Point(7, 12)
        p2 = point.Point(7, 12)
        self.assertEqual(p1, p2)

    def test_points_inequality(self):
        """Similarly __eq__ method of Point should return False
        when two Point objects do not have the same
        x and y coordinates.
        """
        p1 = point.Point(9, 13)
        p2 = point.Point(9, 20)
        p3 = point.Point(10, 13)
        self.assertNotEqual(p1, p2)
        self.assertNotEqual(p1, p3)
        self.assertNotEqual(p2, p3)

    def test_point_str(self):
        """A point should have a nice string representation
        as (x, y).
        """
        pt = point.Point(18, 34)
        pt_str = str(pt)
        self.assertEqual(pt_str, "(18, 34)")


if __name__ == '__main__':
    unittest.main()
