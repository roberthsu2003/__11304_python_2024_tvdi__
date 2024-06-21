#不規則形狀,圓形,圓弧形
from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self, master):
        # 初始化父類別 Frame
        super().__init__()
        # 設定主視窗標題
        master.title("形狀")
        # 設定元件填滿整個視窗
        self.pack(fill=BOTH, expand=1)
        # 初始化使用者介面
        self.initUI()

    def initUI(self):
        # 建立畫布元件，設定寬度和高度
        canvas = Canvas(self, width=400, height=400)
        
        # 繪製第一個橢圓形
        canvas.create_oval(10, 10, 100, 100, outline="#594099",
                           fill="#809940", width=2)
        # 繪製第二個橢圓形
        canvas.create_oval(110, 10, 210, 80, outline="#594099",
                           fill="#809940", width=2)
        # 繪製第一個矩形
        canvas.create_rectangle(230, 10, 290, 60,
                                outline="#594099", fill="#809940", width=2)
        
        # 繪製第二個矩形
        canvas.create_rectangle(30, 200, 90, 100,
                                outline="#594099", fill="#809940", width=2)

        # 繪製弧形
        canvas.create_arc(30, 200, 90, 100, start=0,
                          extent=180, outline="#594099", fill="#809940", width=2)

        #定義多邊形的頂點座標
        points = [150, 100, 200, 120, 240, 180, 210,
                  200, 150, 150, 100, 200]
        # 繪製多邊形
        canvas.create_polygon(points, outline='#594099',
                              fill='#809940', width=2)
        # canvas.create_polygon([110,110, 200,110, 150,150, 120,200], outline='#594099', fill='', width=3, dash=(5,5))
        # 將畫布元件填滿整個視窗
        canvas.pack(fill=BOTH, expand=1)

def main():
    # 建立主視窗
    root = Tk()
    # 建立 Example 類別的實例
    ex = Example(root)
    # 設定主視窗的大小與位置
    root.geometry("330x220+300+300")
    # 開始主迴圈
    root.mainloop()

if __name__ == '__main__':
    main()
