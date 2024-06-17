from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)
        self.initUI()


    def initUI(self):
        canvas = Canvas(self)
        canvas.create_rectangle(40, 20, 120, 100,
            outline="#B68E55", fill="#B68E55")
        canvas.create_rectangle(150, 20, 240, 60,
            outline="#838A2D", fill="#838A2D")
        canvas.create_rectangle(270, 10, 370, 80,
            outline="#78C2C4", fill="#78C2C4")
        canvas.pack(fill=BOTH, expand=1)
def main():

    root = Tk()
    ex = Example(root)
    root.geometry("400x100+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()