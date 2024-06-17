from tkinter import Tk, Canvas, Frame, BOTH

class Example(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.initUI()
        self.master.title("Lines")
        self.pack(fill=BOTH, expand=1)


    def initUI(self):
        canvas = Canvas(self)
        canvas.create_line(15, 30, 200, 30)
        canvas.create_line(200, 30, 200, 80) 
        canvas.create_line(200, 80, 15, 80)  
        canvas.create_line(15, 80, 15, 30) 

        canvas.create_line(300, 35, 300, 200, dash=(6, 3))
        
        canvas.create_line(100, 85, 155, 85) 
        canvas.create_line(155, 85, 205, 130)  
        canvas.create_line(205, 130, 135, 180) 
        canvas.create_line(135, 180, 85, 130)  
        canvas.create_line(85, 130, 100, 85) 
        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example(root)
    root.geometry("400x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()