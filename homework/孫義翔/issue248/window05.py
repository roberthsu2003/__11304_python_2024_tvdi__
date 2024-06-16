from tkinter import Tk,Canvas

class RedBall(Canvas):
    def __init__(self,master,**kw):
        super().__init__(master=master,**kw)
        self.configure(width=100)
        self.configure(height=100)
        self.create_oval(10,10,20,20,fill='#A5A051')
        self.create_oval(50,50,30,30,fill='#81C7D4')
        self.create_oval(80,80,50,50,fill='#E16B8C')


class Window(Tk):
    def __init__(self):
        super().__init__()
        redball = RedBall(self)
        redball.pack()

if __name__ == "__main__":
    root = Window()
    root.title("三體")
    root.mainloop()
