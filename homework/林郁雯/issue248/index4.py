#自訂Canvas類別
from tkinter import Tk, Canvas

class RedBall(Canvas):
    def __init__(self, master, **kw):
        # 初始化父類別 Canvas
        super().__init__(master=master, **kw)
        # 設定畫布寬度為 20
        self.configure(width=50)
        # 設定畫布高度為 20
        self.configure(height=20)
        # 在畫布上繪製一個紅色球體（橢圓形），位置和大小由 (5, 5) 到 (15, 15)
        self.create_oval(5, 5, 15, 15, fill='#333333')


        

class Window(Tk):
    def __init__(self):
        # 初始化父類別 Tk
        super().__init__()
        # 建立 RedBall 類別的實例
        redball = RedBall(self)
        # 將 RedBall 元件加入到主視窗
        redball.pack()

if __name__ == "__main__":
    # 建立主視窗
    root = Window()
    # 設定主視窗的標題
    root.title("自訂類別")
    # 開始主迴圈
    root.mainloop()
