from tkinter import Tk,Canvas

class RedBall(Canvas):
    def __init__(self,master,**kw):
        super().__init__(master=master,**kw)
        self.configure(width=200)
        self.configure(height=200)
        self.create_oval(55,55,115,115,fill='#F3A60C')

class Window(Tk):
    def __init__(self):
        super().__init__()
        redball = RedBall(self)
        redball.pack()

if __name__ == "__main__":
    root = Window()
    root.title("Inheritance")
    root.mainloop()