import tkinter as tk
from tkinter import ttk
from tkinter import Misc


class Example(ttk.Frame):
    def __init__(self,master:Misc,**kwargs):
        super().__init__(master=master,**kwargs)
        master.title('Draw1')
        self.configure({'borderwidth':2,'relief':'groove'})
        #self.config({'borderwidth':2,'relief':'groove'})        
        #self['borderwidth'] = 2
        #self['relief'] = 'groove' 
        canvas = tk.Canvas(self)
        canvas.create_line(15, 30, 200,30)
        canvas.create_line(300,35, 300, 200,dash=(8,2))
        canvas.create_line(55,85,155,85,105,180,55,85)
        canvas.pack(expand=True,fill='both')      
        self.pack(expand=True,fill='both')



def main():
    window = tk.Tk()
    
    Example(window)
    window.geometry("400x250")
    window.mainloop()

if __name__ == "__main__":
    main()