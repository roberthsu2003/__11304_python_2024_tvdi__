# 1. 畫線
from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.initUI()
        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)


    def initUI(self):
        canvas = Canvas(self)
        canvas.create_line(15, 30, 200, 30)
        canvas.create_line(200, 35, 200, 200, dash=(6, 2))
        canvas.create_line(55, 100, 180, 70, 115, 190, 55, 70)
        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("400x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()