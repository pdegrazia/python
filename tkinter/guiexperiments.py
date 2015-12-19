from Tkinter import Label,Tk,Button,Frame, Canvas


class CustomLabel(Label):

    def __init__(self):
        Label.__init__(self,text='Label')


class CustomFrame(Frame):

    def __init__(self,root):
        Frame.__init__(self,root)
        self.create_button()
        self.create_label()
        self.create_canvas()
        self.pack()

    def print_hello(self):
        print 'hello'

    def create_button(self):
        hello_button = Button(self,text='print hello!',command=self.print_hello)
        hello_button.pack(side='top')
        quit_button = Button(self,text='quit',command=self.quit)
        quit_button.pack(side='bottom')

    def create_canvas(self):
        canvas = Canvas(self,width=100,height=100)
        canvas.pack()

    def create_label(self):
        mylabel=CustomLabel()
        mylabel.pack()

if __name__ == '__main__':

    root = Tk()
    customFrame = CustomFrame(root)
    root.mainloop()