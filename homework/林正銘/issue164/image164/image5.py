from tkinter import Tk,Canvas

class RedBall(Canvas):
    def __init__(self,master,**kw):
        super().__init__(master=master,**kw)
        self.configure(width=300)
        self.configure(height=120)
        self.create_oval(125,25,195,95,fill='#FFFF00')

class Window(Tk):
    def __init__(self):
        super().__init__()
        redball = RedBall(self)
        redball.pack()

if __name__ == "__main__":
    root = Window()
    root.title("自訂類別_18_林正銘")
    #root.geometry("200x200")
    root.mainloop()