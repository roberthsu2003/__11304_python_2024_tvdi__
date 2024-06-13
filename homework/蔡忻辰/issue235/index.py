import ubikedata
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

class Window(ThemedTk):
    def __init__(self, theme:str|None, **kwargs):

        super().__init__(**kwargs)
        self.title("YouBike2.0 臺北市公共自行車即時資訊")
        self.geometry('1000x200')
        self.resizable(False, False)
        treeview_frame = ttk.Frame(self)
        treeview_frame.pack()

        # define columns
        columns = ('sna', 'sarea', 'mday', 'ar', 'act', 'updateTime', 'total', 'rent_bikes', 'lat', 'lng', 'retuen_bikes')
        treeview = ttk.Treeview(treeview_frame, columns=columns, show='headings')
        
        # define headings
        treeview.heading('sna', text='Station Name')
        treeview.heading('sarea', text='District')
        treeview.heading('mday', text='Mday')
        treeview.heading('ar', text='Address')
        treeview.heading('act', text='Operating Status')
        treeview.heading('updateTime', text='Update Time')
        treeview.heading('total', text='Total')
        treeview.heading('rent_bikes', text='Available Rent Bikes')
        treeview.heading('lat', text='Latitude')
        treeview.heading('lng', text='Longitude')
        treeview.heading('retuen_bikes', text='Available Return Bikes')
        
        # 垂直和水平捲軸
        verticalsb = ttk.Scrollbar(treeview_frame, orient="vertical", command=treeview.yview)
        verticalsb.pack(side='right', fill='y')
        horizontalsb = ttk.Scrollbar(treeview_frame, orient="horizontal", command=treeview.xview)
        horizontalsb.pack(side='bottom', fill='x')

        # 設定Treeview的xscroll和yscroll
        treeview.configure(xscroll=horizontalsb.set, yscroll=verticalsb.set)
        treeview.pack()

        # 將資歷寫入到 Treeview
        try:
            ubike:list[dict] = ubikedata.load_data()
        except Exception as error:
            print(error)
        else:
            for data in ubike:
                sna_value = data['sna'].split("_")[1]
                if data['act'] == '1':
                    act_value = "營業中" 
                else:
                    act_value = "維護中"
                treeview.insert('', 'end', values=(sna_value, data['sarea'], data['mday'], data['ar'], act_value, data['updateTime'], data['total'], data['rent_bikes'], data['lat'], data['lng'], data['retuen_bikes']))
        
def main():
    window = Window(theme='arc')
    window.mainloop()

if __name__ == '__main__':
    main()