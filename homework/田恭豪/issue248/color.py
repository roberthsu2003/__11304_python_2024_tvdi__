# 2. 矩形(線框和填色)
from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)
        self.initUI()


    def initUI(self):
        canvas = Canvas(self)
        canvas.create_rectangle(30, 10, 120, 80,
            outline="#fb6", fill="#fb6")
        canvas.create_rectangle(150, 10, 240, 80,
            outline="#f80", fill="#f80")
        canvas.create_rectangle(270, 10, 370, 80,
            outline="#55f", fill="#55f")
        canvas.pack(fill=BOTH, expand=1)
def main():

    root = Tk()
    ex = Example(root)
    root.geometry("400x100+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()