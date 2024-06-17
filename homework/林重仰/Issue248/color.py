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
            outline="#75AB81", fill="#1B7680")
        canvas.create_rectangle(150, 10, 240, 80,
            outline="#7057B5", fill="#B55757")
        canvas.create_rectangle(270, 10, 370, 80,
            outline="#2A126B", fill="#581556")
        canvas.pack(fill=BOTH, expand=1)
def main():

    root = Tk()
    ex = Example(root)
    root.geometry("400x100+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()