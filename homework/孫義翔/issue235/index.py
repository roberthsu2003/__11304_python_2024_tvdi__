import MLproject_Solar_Irradiance.weather.data as data
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk  # type: ignore


class Window(ThemedTk):
    def __init__(self, theme: str | None, **kwargs):
        super().__init__(**kwargs)
        self.title('YouBike 即時資料')

        try:
            ubike_data: list[dict] = data.load_data()
            self.show_data(ubike_data)
        except Exception as error:
            print(error)

    def show_data(self, data):
        self.treeview = ttk.Treeview(self, columns=('sna', 'sarea', 'mday', 'ar', 'act', 'updateTime', 'total'))

        self.treeview.heading('#1', text='站名')
        self.treeview.heading('#2', text='地區')
        self.treeview.heading('#3', text='日期')
        self.treeview.heading('#4', text='地址')
        self.treeview.heading('#5', text='狀態')
        self.treeview.heading('#6', text='更新時間')
        self.treeview.heading('#7', text='數量')

        for item in data:
            self.treeview.insert('', tk.END, values=list(item.values()))

        self.treeview.pack(fill=tk.BOTH, expand=True)


if __name__ == '__main__':
    window = Window(theme='arc')
    window.mainloop()
