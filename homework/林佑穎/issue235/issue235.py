import MLproject_Solar_Irradiance.weather.data as data
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


# 建立window視窗
class Window(ThemedTk):
    def __init__(self, theme: str = None, **kwargs):     #**kwargs:沒有限定名稱的呼叫
        super().__init__(theme=theme, **kwargs)
        '''
        try:
            ubike:list[dict] = data.load_data()
        except Exception as error:
            print(error)
        else:
            print(ubike)
        '''    
        self.title("YouBike2.0 臺北市公共自行車即時資訊")
        self.geometry('500x200')
        
        # 建立treeview
        treeview_frame = ttk.Frame(self)
        treeview_frame.pack(fill=tk.BOTH, expand=True)

        # 設定欄位
        columns = ('sna', 'sarea', 'mday', 'ar', 'act', 'updateTime', 'total', 'rent_bikes', 'lat', 'lng', 'return_bikes')
        self.treeview = ttk.Treeview(treeview_frame, columns=columns, show='headings')

        # 設定欄位名稱
        self.treeview.heading('sna', text='站名')
        self.treeview.heading('sarea', text='行政區')
        self.treeview.heading('mday', text='及時更新時間')
        self.treeview.heading('ar', text='地址')
        self.treeview.heading('act', text='車輛狀態')
        self.treeview.heading('updateTime', text='資料更新時間')
        self.treeview.heading('total', text='車輛總數')
        self.treeview.heading('rent_bikes', text='可借車數')
        self.treeview.heading('lat', text='緯度')
        self.treeview.heading('lng', text='經度')
        self.treeview.heading('return_bikes', text='可還車數')

        # 垂直和水平滾動條
        verticalsb = ttk.Scrollbar(treeview_frame, orient="vertical", command=self.treeview.yview)
        verticalsb.pack(side='left', fill='y')
        horizontalsb = ttk.Scrollbar(treeview_frame, orient="horizontal", command=self.treeview.xview)
        horizontalsb.pack(side='bottom', fill='x')

        # 配置Treeview滾動條
        self.treeview.configure(xscroll=horizontalsb.set, yscroll=verticalsb.set)
        self.treeview.pack(fill=tk.BOTH, expand=True)
        self.show_data()

    def show_data(self):
        try:
            ubike = data.load_data()
        except Exception as error:
            print(error)
        else:
            for item in ubike:
                sna_value = item.sna.split("_")[1]
                act_value = "營業中" if item.act == '1' else "維護中"
                self.treeview.insert('', 'end', values=(sna_value, item.sarea, item.mday, item.ar, act_value, item.updateTime, item.total, item.rent_bikes, item.lat, item.lng, item.return_bikes))
        
# 主函數
def main():
    window = Window(theme='arc')
    window.mainloop()

if __name__ == '__main__':
    main()