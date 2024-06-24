import MLproject_Solar_Irradiance.weather.data as data
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

class Window(ThemedTk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        try:
            ubike_data:list[dict]=data.load_data()
        except Exception as error:
            print(error)
        else:
            self.title_design()
            self.content_design(ubike_data)
            
    def title_design(self)->None:
        style=ttk.Style()
        style.configure("title.TLabel",font=('arial',12))
        self.title("ubike info")
        title_frame=ttk.Frame(self)
        ttk.Label(title_frame,text="ubike 狀態",style="title.TLabel").pack()
        title_frame.pack(pady=(10,30))

    def content_design(self,ubike_data:list[dict])->None:
        style=ttk.Style()
        style.configure("content.Treeview",font=('arial',10))
        content_frame=ttk.Frame(self)

        
        column_names:list=list(ubike_data[0].keys())
        tree=ttk.Treeview(content_frame,columns=column_names,show="headings",style="content.Treeview")
        # 將ubike_data[0].keys() 當作 index 和 內文寫入
        for column_name in column_names:
            if column_name == "latitude":
                tree.heading("latitude", text="緯度")
            elif column_name == "longitude":
                tree.heading("longitude", text="經度")
            else:
                tree.heading(column_name, text=column_name)

            tree.column(column_name ,anchor="center",minwidth=10,stretch=True)
        # 將ubike_data 資料寫入
        for data in ubike_data:
            data_value:list=list(data.values())
            tree.insert("",index=tk.END,values=data_value)
        
        #建立X 和 Y的拖動條
        scrollbary = ttk.Scrollbar(content_frame, orient='vertical', command=tree.yview)
        scrollbarx = ttk.Scrollbar(content_frame, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
        scrollbary.pack(side='right', fill='y')
        scrollbarx.pack(side='bottom', fill='x')
        tree.pack(expand=True,fill="x")

        content_frame.pack(expand=True,fill="x")

        