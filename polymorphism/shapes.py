import turtle


class Shape:
    def calculate_area(self):return 0.0


class Rectangle(Shape):
    '''
    inherits from Shapes
    '''
    def __init__(self, height, width):
        '''
        initialise rectangle
        :param height: height of the rectangle
        :param width: width of the rectangle
        '''
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.width*self.height


class Square(Rectangle):
    def __init__(self,side):
        Rectangle.__init__(self,side,side)

class Triangle(Shape):
    def __init__(self,side):
        self.side = side

if __name__ == '__main__':

    rect1=Rectangle(3,4)
    print rect1.calculate_area()
    square1 = Square(5)
    print square1.calculate_area()