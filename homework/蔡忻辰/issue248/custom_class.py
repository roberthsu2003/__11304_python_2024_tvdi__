from tkinter import Tk,Canvas

class RedBall(Canvas):
    def __init__(self,master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(width=300, height=200, background='white')
        self.create_oval(200, 50, 100, 150, width=1, fill='red', outline='black')

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title("自訂類別")
        redball = RedBall(self)
        redball.pack()

if __name__ == "__main__":
    window = Window()
    window.mainloop()