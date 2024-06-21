#矩形(線框和填色)
from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):

    def __init__(self, master):
        # 初始化父類別 Frame
        super().__init__(master)
        # 設定主視窗標題
        self.master.title("顏色")
        # 設定元件填滿整個視窗
        self.pack(fill=BOTH, expand=1)
        # 初始化使用者介面
        self.initUI()

    def initUI(self):
        # 建立畫布元件
        canvas = Canvas(self)
        # 繪製第一個矩形
        canvas.create_rectangle(30, 10, 120, 80,
                                outline="#fb0", fill="#fb0")
        # 繪製第二個矩形
        canvas.create_rectangle(150, 10, 240, 80,
                                outline="#f50", fill="#f50")
        # 繪製第三個矩形
        canvas.create_rectangle(270, 10, 370, 80,
                                outline="#05f", fill="#05f")
        # 將畫布元件填滿整個視窗
        canvas.pack(fill=BOTH, expand=1)

def main():
    # 建立主視窗
    root = Tk()
    # 建立 Example 類別的實例
    ex = Example(root)
    # 設定主視窗的大小與位置
    root.geometry("400x100+300+300")
    # 開始主迴圈
    root.mainloop()


if __name__ == '__main__':
    main()