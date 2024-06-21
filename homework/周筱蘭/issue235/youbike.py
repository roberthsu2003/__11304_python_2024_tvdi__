import tkinter as tk
from tkinter import ttk
import requests
from pydantic import BaseModel, Field

# 定義資料模型
class YouBikeStation(BaseModel):
    sna: str
    sarea: str
    mday: str
    ar: str
    act: str
    updateTime: str
    total: int
    rent_bikes: int = Field(alias="available_rent_bikes")
    lat: float = Field(alias="latitude")
    lng: float = Field(alias="longitude")
    return_bikes: int = Field(alias="available_return_bikes")

class YouBikeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouBike 即時資訊")
        self.create_widgets()
        self.fetch_data()

    def create_widgets(self):
        columns = ("sna", "sarea", "mday", "ar", "act", "updateTime", "total", "rent_bikes", "lat", "lng", "return_bikes")
        
        # 創建 Treeview 和滾動條
        self.tree_frame = ttk.Frame(self.root)
        self.tree_frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(self.tree_frame, columns=columns, show="headings")
        
        vsb = ttk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(self.tree_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")

        self.tree_frame.grid_rowconfigure(0, weight=1)
        self.tree_frame.grid_columnconfigure(0, weight=1)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

    def fetch_data(self):
        url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
        response = requests.get(url)
        stations = response.json()

        # 清空 Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # 解析資料並顯示在 Treeview
        for station_data in stations:
            station = YouBikeStation(**station_data)
            self.tree.insert("", tk.END, values=(station.sna, station.sarea, station.mday, station.ar, station.act, station.updateTime, station.total, station.rent_bikes, station.lat, station.lng, station.return_bikes))

if __name__ == "__main__":
    root = tk.Tk()
    app = YouBikeApp(root)
    root.mainloop()
