import tkinter as tk
from tkinter import Toplevel, ttk, Canvas
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("繪圖")
        self. geometry("300x200")
        # title
        style = ttk.Style()
        style.configure("Top.TLabel",font=('微軟正黑體', 25, "bold"))
        title_frame = ttk.Frame(self, style='Top.TFrame')
        ttk.Label(title_frame, text="繪圖", style='Top.TLabel').pack(expand=True, fill='y')
        title_frame.pack(pady=(10, 0))
        # 按鈕
        button_frame = ttk.Frame(self, borderwidth=1, relief='groove')
        button_frame.pack(padx=10, pady=(5, 10), ipadx=20, ipady=10)
        ttk.Button(button_frame, text="畫線", command=self.draw_line).pack(side='top', expand=True)
        ttk.Button(button_frame, text="矩形(線框和填色)", command=self.draw_rectangle).pack(side='top', expand=True)
        ttk.Button(button_frame, text="橢圓,圓形,圓弧形,不規則形狀", command=self.draw_diff_types_polygon).pack(side='top', expand=True)
        ttk.Button(button_frame, text="畫圖片", command=self.draw_img).pack(side='top', expand=True)
    
    # Toplevel, Canvas
    def draw_on_toplevel(self, title, width, height):
        self.canvas_window = Toplevel(self)
        self.canvas_window.title(title)
        self.canvas = Canvas(self.canvas_window, width=width , height=height, background='gray')
        self.canvas.pack()

    def draw_line(self):
        self.draw_on_toplevel("畫線", 230, 155)
        # 實體平行直線
        self.canvas.create_line(10, 20, 80, 20)
        # 方形
        self.canvas.create_line(10, 50, 80, 50, 80, 120, 10, 120, 10, 50, width=1, fill='red')
        # 垂直直線(虛線)
        self.canvas.create_line(110,10, 110, 150, width=3, fill='orange', dash=(5, 3))
        # 六邊型
        self.canvas.create_line(150, 50, 200, 50, 225, 85, 200, 120, 150, 120, 125, 85, 150, 50, fill='blue')

    def draw_rectangle(self):
        self.draw_on_toplevel("矩形(線框和填色)", 330, 110)
        self.canvas.create_rectangle(10, 10, 100, 100, fill='#FF359A', outline='#000000')
        self.canvas.create_rectangle(120, 10, 210, 100, width=5, fill='#FFEEDD', outline='#DCB5FF')
        self.canvas.create_rectangle(230, 10, 320, 100, width=3, fill='#FF8000', outline='#FFFF37', dash=(5, 5)) 

    def draw_diff_types_polygon(self):
        self.draw_on_toplevel("橢圓, 圓形, 圓弧形, 不規則形狀",340, 170)
        # 橢圓 & 圓型
        self.canvas.create_oval(10, 10, 60, 100, width=5, fill='#0066CC', outline='#AE0000')
        self.canvas.create_oval(10, 120, 50, 160, width=3, fill='#FF8000', outline='#FFFF37', dash=(5, 5))
        # 圓弧
        self.canvas.create_arc(60, 10, 130, 80, fill='#FFEEDD')
        self.canvas.create_arc(140, 10, 190, 80, extent=180, fill='#FF8000', outline='#FFFF37')
        self.canvas.create_arc(60, 120, 120, 190, start=45, extent=135, width=3, fill='#0066CC', outline='#AE0000', dash=(5, 5))
        self.canvas.create_arc(140, 120, 200, 190, start=115, extent=-110, width=2, outline='#FF359A', dash=(5, 5), style='arc')
        # 多邊形
        self.canvas.create_polygon([210,10, 330, 60, 210, 150, 270, 65], width=2, dash=(5, 5), outline='#A6FFA6', fill='#B766AD')
    
    def draw_img(self):
        img = Image.open("./images/github.png")
        self.imggithub_icon = ImageTk.PhotoImage(img)
        self.draw_on_toplevel("畫圖片GitHub",img.width+30, img.height+20)
        self.canvas.create_image(20, 10, anchor=tk.NW, image=self.imggithub_icon)

def main():
    window= Window()
    window.mainloop()

if __name__ == '__main__':
    main()