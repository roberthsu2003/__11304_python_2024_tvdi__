#--畫線
from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.initUI()
        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)

    def initUI(self):
        # 建立 Canvas 小工具
        canvas = Canvas(self)
        
        # 繪製一條水平線
        canvas.create_line(15, 30, 200, 30) #(行第15點畫到200點 ,直30)
        
        # # 繪製一條垂直虛線dash
        canvas.create_line(300, 35, 300, 200, dash=(4, 2)) #(行300,直35點畫到200點 )虛線dash
        
        # # 繪製一個三角形
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        
        # 設定畫布填充視窗並允許擴展
        canvas.pack(fill=BOTH, expand=1)

def main():
    # 建立主 Tkinter 視窗
    root = Tk()
    
    # 建立 Example 類別的實例
    ex = Example(root)
    
    # 設定視窗幾何形狀（大小和位置）
    root.geometry("400x250+300+300")
    
    # 開始 Tkinter 事件循環
    root.mainloop()

if __name__ == '__main__':
    main()
