import MLproject_Solar_Irradiance.weather.data as data
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.ttk as ttk

class Window(ThemedTk):
      def __init__(self,theme:str|None,**kwargs):
        global sitename1, sitename2, sitename3, sitename4, sitename5
        global county1, county2, county3, county4, county5
        #global ubike:list[dict]
        super().__init__(**kwargs)
        #global ubike:list[dict]
        try:
            ubike:list[dict] = data.load_data()
        except Exception as error:
            print(error)
        else:
            print(ubike[-1])
            sitename1 = ubike[-1]['sna']
            sitename2 = ubike[-2]['sna']
            sitename3 = ubike[-3]['sna']
            sitename4 = ubike[-4]['sna']
            sitename5 = ubike[-5]['sna']
            county1 = ubike[-1]['sarea']
            county2 = ubike[-2]['sarea']
            county3 = ubike[-3]['sarea']
            county4 = ubike[-4]['sarea']
            county5 = ubike[-5]['sarea']



def main():   
    window = Window(theme='arc')
    #window.mainloop()
    window = tk.Tk()
    window.title('ubike 2.0')
    window.configure(bg="#7AFEC6")
    #root.iconbitmap('heart_green.ico')
    window.geometry('500x200')

    tree=ttk.Treeview(window,columns=("ubike"))
    tree.heading("#0",text="sitename")
    tree.heading("#1",text="county")

    tree.insert("",index="end",text= sitename1,values=county1)
    tree.insert("",index="end",text= sitename2,values=county1)
    tree.insert("",index="end",text= sitename3,values=county1)
    tree.insert("",index="end",text= sitename4,values=county1)
    tree.insert("",index="end",text= sitename5,values=county1)

    tree.pack()
    window.mainloop()

if __name__ == '__main__':
    main()