class Point2D:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%s , %s )' % (self.x,self.y)

    def distance(self):
        return self.x**2 + self.y**2


class Point3D(Point2D):

    def __init__(self,x,y,z):
        Point2D.__init__(self,x,y)
        self.z = z

    def __str__(self):
        return '(%s , %s, %s )' % (self.x,self.y,self.z)

    def distance(self):
        return self.x**2 + self.y **2 + self.z**2