from points import Point2D,Point3D


if __name__ == '__main__':

    p1 = Point2D(0,0)
    print p1

    p2 = Point3D(2,3,4)
    print p2

    p3 = Point2D(-3,-3)

    print p1.distance()
    print p2.distance()
    print p3.distance()

    assert p3.distance() == 18