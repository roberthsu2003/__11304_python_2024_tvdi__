#畫圖片

from tkinter import Tk, Canvas, Frame, BOTH, NW
from PIL import Image, ImageTk

class Example(Frame):

    def __init__(self, master):
        # 初始化父類別 Frame
        super().__init__(master)
        # 設定主視窗標題
        master.title("Home icon")
        # 設定元件填滿整個視窗
        self.pack(fill=BOTH, expand=1)
        # 初始化使用者介面
        self.initUI()

    def initUI(self):
        # 開啟圖像
        self.img = Image.open("home.png")
        # 轉換圖像為 Tkinter 可使用的格式
        self.tatras = ImageTk.PhotoImage(self.img)
        # 建立畫布元件，設定寬度和高度為圖像尺寸加上20像素
        canvas = Canvas(self, width=self.img.size[0] + 20,
                        height=self.img.size[1] + 20)
        # 在畫布上繪製圖像，位置在 (10, 10)，錨點為 NW (西北)
        canvas.create_image(10, 10, anchor=NW, image=self.tatras)
        # 將畫布元件填滿整個視窗
        canvas.pack(fill=BOTH, expand=1)

def main():
    # 建立主視窗
    root = Tk()
    # 建立 Example 類別的實例
    ex = Example(root)
    # 開始主迴圈
    root.mainloop()

if __name__ == '__main__':
    main()
