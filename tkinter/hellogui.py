from Tkinter import Label
from Tkinter import Tk


if __name__ == '__main__':

    root = Tk()
    label = Label(root,text='hello')
    label.pack()
    root.mainloop()