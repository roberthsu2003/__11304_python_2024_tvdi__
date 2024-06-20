from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.master.title("Colours_18_林正銘")
        self.pack(fill=BOTH, expand=1)
        self.initUI()


    def initUI(self):
        canvas = Canvas(self)
        canvas.create_rectangle(30, 10, 120, 80,
            outline="#fb0", fill="#fb0")
        canvas.create_rectangle(150, 10, 240, 80,
            outline="#f50", fill="#f50")
        canvas.create_rectangle(270, 10, 370, 80,
            outline="#05f", fill="#05f")
        canvas.create_rectangle(430, 10, 520, 80,
            outline="#000", fill="#fb0")
        canvas.create_rectangle(550, 10, 640, 80,
            outline="#000", fill="#f50")
        canvas.create_rectangle(670, 10, 770, 80,
            outline="#000", fill="#05f")
        canvas.pack(fill=BOTH, expand=1)
def main():

    root = Tk()
    ex = Example(root)
    root.geometry("800x100+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()