from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self,master):
        super().__init__()
        master.title("Geometric")
        self.pack(fill=BOTH, expand=1)
        self.initUI()


    def initUI(self):

        canvas = Canvas(self,width=400,height=400)
        canvas.create_oval(20, 10, 40, 80, outline="#f11",
            fill="#7585AB", width=2)
        canvas.create_oval(60, 10, 100, 50, outline="#f11",
            fill="#7585AB", width=2)
        canvas.create_rectangle(130, 10, 250, 60,
            outline="#f11", fill="#7585AB", width=2)

        canvas.create_rectangle(30, 100, 80, 150,
                                outline="#f11", fill="#7585AB", width=2)

        canvas.create_arc(30, 250, 90, 150, start=0,
            extent=180, outline="#7585AB", fill="#7585AB", width=2)



        points = [550, 100, 250, 120, 240, 150, 210,
            200, 150, 150, 150, 200]
        canvas.create_polygon(points, outline='#f11',
            fill='#7585AB', width=2)

        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("330x220+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()