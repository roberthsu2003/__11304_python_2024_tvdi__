# 4. 畫圖片
from tkinter import Tk, Canvas, Frame, BOTH, NW
from PIL import Image, ImageTk

class Example(Frame):

    def __init__(self, master):
        super().__init__(master)
        master.title("Delete icon")
        self.pack(fill=BOTH, expand=1)
        self.initUI()

    def initUI(self):
        # 圖片路徑使用原始字串或雙反斜線
        self.img = Image.open(r"C:\Git hub\Ted_window\類別\HW\issue248\icon\delete.png")
        self.tatras = ImageTk.PhotoImage(self.img)
        
        # Canvas 的寬度設置為圖片寬度加上一些額外空間
        canvas = Canvas(self, width=self.img.size[0] + 20, height=self.img.size[1] + 20)
        canvas.create_image(10, 10, anchor=NW, image=self.tatras)
        canvas.pack(fill=BOTH, expand=1)

def main():
    root = Tk()
    ex = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()

