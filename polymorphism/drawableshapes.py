import shapes
import turtle


class Drawable:
    def goto(self,x,y):
        turtle.up()
        turtle.goto(x,y)
        turtle.down()

    def draw(self,x,y):
        pass


class DrawableRectangle(Drawable,shapes.Rectangle):
    def __init__(self,width,height):
        shapes.Rectangle.__init__(self,width,height)

    def draw(self,x,y):
        self.goto(x,y)
        turtle.goto(x+self.width,y)
        turtle.goto(x+self.width,y+self.height)
        turtle.goto(x,y+self.height)
        turtle.goto(x,y)

class DrawableTriangle(Drawable,shapes.Triangle):
    def __init__(self,side):
        shapes.Triangle.__init__(self,side)
        self.origin_x = 0
        self.origin_y = 0

    def draw(self,x,y):
        self.goto(self.origin_x,self.origin_y)
        turtle.forward(self.side)
        turtle.left(45)
        turtle.forward(self.side)
        turtle.left(45)
        turtle.forward(self.side)
        



if __name__ == '__main__':
    rect = DrawableRectangle(300,400)
    rect.draw(3,4)
    triangle = DrawableTriangle(300)
    triangle.draw(0,0)