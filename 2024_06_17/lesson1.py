import tkinter as tk
from tkinter import ttk
from tkinter import Misc


class Example(ttk.Frame):
    def __init__(self,master:Misc,**kwargs):
        super().__init__(master=master,**kwargs)
        master.title('Lines')
        self.configure({'borderwidth':2,'relief':'groove'})
        #self.config({'borderwidth':2,'relief':'groove'})        
        #self['borderwidth'] = 2
        #self['relief'] = 'groove'       
        self.pack(expand=True,fill='both')



def main():
    window = tk.Tk()
    
    Example(window)
    window.geometry("400x250")
    window.mainloop()

if __name__ == "__main__":
    main()