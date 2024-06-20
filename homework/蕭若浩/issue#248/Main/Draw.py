from tkinter import Tk,Canvas

class YellowDiamond(Canvas):
    def __init__(self,master,**kw):
        super().__init__(master=master,**kw)
        self.configure(width=40)
        self.configure(height=40)
        self.create_polygon(10, 20, 20, 10, 30, 20, 20, 30, outline='black', fill='yellow')
class Window(Tk):
    def __init__(self):
        super().__init__()
        yellowdiamond = YellowDiamond(self)
        yellowdiamond.pack()

if __name__ == "__main__":
    root = Window()
    root.title("自訂類別")
    root.mainloop()
