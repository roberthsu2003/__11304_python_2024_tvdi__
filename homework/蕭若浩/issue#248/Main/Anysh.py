from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self,master):
        super().__init__()
        master.title("Shapes")
        self.pack(fill=BOTH, expand=1)
        self.initUI()


    def initUI(self):

        canvas = Canvas(self,width=400,height=400)
        canvas.create_oval(30, 30, 120, 120, outline="#f11", fill="#1f1", width=2)
        canvas.create_oval(150, 30, 270, 120, outline="#f11", fill="#1f1", width=2)
        canvas.create_polygon(300, 200, 350, 150, 400, 200, 350, 250, outline="#f11", fill="#1f1", width=2)
        canvas.create_rectangle(30, 150, 180, 250, outline="#f11", fill="#1f1", width=2)
        canvas.create_arc(30, 150, 180, 300, start=0, extent=180, outline="#f11", fill="#1f1", width=2)

        points = [150, 200, 200, 220, 240, 280, 210, 300, 150, 250, 100, 200]
        canvas.create_polygon(points, outline='#f11', fill='#1f1', width=2)

        canvas.pack(fill=BOTH, expand=1)

def main():

    root = Tk()
    ex = Example(root)
    root.geometry("330x220+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()