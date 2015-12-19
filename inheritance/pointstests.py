import unittest
from points import Point2D,Point3D


class PointsTests(unittest.TestCase):

    def test_distance2d(self):
        p1=Point2D(3,4)
        assert p1.distance() == 25

    def test_distance3d(self):
        p2=Point3D(1,1,1)
        assert p2.distance() == 3

if __name__ == '__main__':
    unittest.main()