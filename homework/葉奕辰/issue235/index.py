import tkinter as tk
from tkinter import ttk
import requests
import json

# 下載並解析 JSON 資料
url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
response = requests.get(url)
data = response.json()

# 建立主視窗
root = tk.Tk()
root.title("YouBike 即時資料")
root.geometry("1000x600")

# 設置 Treeview
columns = ("sna", "sarea", "ar", "updateTime", "total", "available_rent_bikes","available_return_bikes","latitude", "longitude")
tree = ttk.Treeview(root, columns=columns, show="headings")

# 設置每個欄位的標題
for col in columns:
    tree.heading("sna", text="站點名稱")
    tree.heading("sarea", text="站點區域")
    tree.heading("ar", text="地址")
    tree.heading('updateTime',text='更新時間')
    tree.heading("total", text="車位總數")
    tree.heading("available_rent_bikes", text="可借車數")
    tree.heading("available_return_bikes", text="可還空位數")
    tree.heading("latitude", text="緯度")
    tree.heading("longitude", text="經度")

# 設置欄位寬度
tree.column("sna", width=280)
tree.column("ar", width=350)


# 插入資料到 Treeview
for item in data:
    tree.insert("", "end", values=(
        item.get("sna"),
        item.get("sarea"),
        item.get("ar"),
        item.get("updateTime"),
        item.get("total"),
        item.get("available_rent_bikes"),
        item.get("available_return_bikes"),
        item.get("latitude"),
        item.get("longitude")
    ))

# 設置滾動條
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

scrollbar_x = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
tree.configure(xscroll=scrollbar_x.set)
scrollbar_x.pack(side="bottom", fill="x")

# 顯示 Treeview
tree.pack(expand=True, fill='both')

# 啟動主迴圈
root.mainloop()
