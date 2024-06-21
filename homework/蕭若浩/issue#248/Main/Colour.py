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
            outline="#fff", fill="#f05")
        canvas.create_rectangle(150, 10, 240, 80,
            outline="#f0f", fill="#f50")
        canvas.create_rectangle(270, 10, 360, 80,
            outline="#0ff", fill="#05f")
        canvas.create_rectangle(390, 10, 480, 80,
                                outline="#0ff", fill="#055")
        canvas.create_rectangle(510, 10, 600, 80,
                                outline="#0ff", fill="#3F2")
        canvas.pack(fill=BOTH, expand=1)
def main():

    root = Tk()
    ex = Example(root)
    root.geometry("650x100+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()