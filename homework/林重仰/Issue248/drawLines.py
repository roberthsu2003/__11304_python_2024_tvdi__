from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.initUI()
        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)


    def initUI(self):
        canvas = Canvas(self)
        canvas.create_line(90, 90, 10, 10)
        canvas.create_line(300, 35, 300, 200, dash=(1, 5))
        canvas.create_line(15, 55, 95, 55, 45, 110, 15, 55)
        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("400x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()