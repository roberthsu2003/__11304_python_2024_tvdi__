from tkinter import Tk, Canvas, Frame, BOTH, NW
from PIL import Image, ImageTk

class Example(Frame):

    def __init__(self,master):
        super().__init__(master)
        master.title("Home icon_18_林正銘")
        self.pack(fill=BOTH, expand=1)
        self.initUI()


    def initUI(self):

        self.img = Image.open("home.png")
        self.tatras = ImageTk.PhotoImage(self.img)
        canvas = Canvas(self, width=self.img.size[0]+20,
           height=self.img.size[1]+20)
        canvas.create_image(140, 70, anchor=NW, image=self.tatras)
        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example(root)
    root.geometry("330x220")
    root.mainloop()


if __name__ == '__main__':
    main()