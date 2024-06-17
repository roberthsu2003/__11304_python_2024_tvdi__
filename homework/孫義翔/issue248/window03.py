from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self,master):
        super().__init__()
        master.title("Shapes")
        self.pack(fill=BOTH, expand=1)
        self.initUI()


    def initUI(self):

        canvas = Canvas(self,width=400,height=400)
        canvas.create_oval(10, 10, 80, 80, outline="#0089A7",
            fill="#0089A7", width=2)
        canvas.create_line(40, 10, 40, 80, fill="#81C7D4", width=2)
        canvas.create_oval(100, 10, 200, 60, outline="#B28FCE",
            fill="#8A6BBE", width=2)
        canvas.create_rectangle(10, 200, 60,100,
            outline="#554236", fill="#F17C67", width=2)


        points = [150, 80, 180, 160, 270, 100, 260,
            200, 150, 150]
        canvas.create_polygon(points, outline='#ADA142',
            fill='#E9CD4C', width=2)

        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("330x220+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()