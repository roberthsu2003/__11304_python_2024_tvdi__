from tkinter import Tk, Canvas

class BlueSquare(Canvas):
    def __init__(self, master, **kw):
        super().__init__(master=master, **kw)
        self.configure(width=80, height=80)  # 調整畫布寬度和高度
        self.create_rectangle(20, 20, 60, 60, fill='blue')  # 繪製藍色正方形

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")  # 調整視窗大小
        bluesquare = BlueSquare(self)
        bluesquare.pack()

if __name__ == "__main__":
    root = Window()
    root.title("自訂類別")
    root.mainloop()
