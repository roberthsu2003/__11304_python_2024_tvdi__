import requests
import tkinter as tk
from tkinter import ttk

def download_youbike_data():
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    
    try:
        response = requests.get(youbike_url)
        response.raise_for_status()  # 檢查請求是否成功
        youbike_data = response.json()
        return youbike_data
    except requests.RequestException as e:
        print(f"下載失敗: {e}")
        return None
    except JSONDecodeError:
        print("JSON 解碼錯誤")
        return None

def populate_treeview(tree, data):
    for station_info in data:
        tree.insert('', 'end', values=(
            station_info.get('sno', ''),
            station_info.get('sna', ''),
            station_info.get('sarea', ''),
            station_info.get('mday', ''),
            station_info.get('ar', ''),
            station_info.get('sareaen', ''),
            station_info.get('snaen', ''),
            station_info.get('aren', ''),
            station_info.get('act', ''),
            station_info.get('srcUpdateTime', ''),
            station_info.get('updateTime', ''),
            station_info.get('infoTime', ''),
            station_info.get('infoDate', ''),
            station_info.get('tot', ''),
            station_info.get('sbi', ''),
            station_info.get('bemp', ''),
            station_info.get('lat', ''),
            station_info.get('lng', '')
        ))
    # 設置列的最小寬度
    for col in tree['columns']:
        tree.column(col, minwidth=0, width=150, anchor=tk.CENTER)

def main():
    youbike_data = download_youbike_data()
    
    if youbike_data:
        print("台北市 YouBike 即時資料下載成功！")
        # 創建Tkinter視窗
        root = tk.Tk()
        root.title("台北市 YouBike 即時資料")
        
        # 創建Treeview
        tree = ttk.Treeview(root, columns=(
            'sno', 'sna', 'sarea', 'mday', 'ar', 'sareaen', 'snaen', 'aren', 
            'act', 'srcUpdateTime', 'updateTime', 'infoTime', 'infoDate', 
            'total', 'available_rent_bikes', 'available_return_bikes', 'latitude', 'longitude'
        ), show='headings')
        
        # 定義每列的標題和寬度
        tree.heading('sno', text='站點編號 (sno)')
        tree.heading('sna', text='站點名稱 (sna)')
        tree.heading('sarea', text='站點區域 (sarea)')
        tree.heading('mday', text='更新時間 (mday)')
        tree.heading('ar', text='站點地址 (ar)')
        tree.heading('sareaen', text='站點區域英文 (sareaen)')
        tree.heading('snaen', text='站點名稱英文 (snaen)')
        tree.heading('aren', text='站點地址英文 (aren)')
        tree.heading('act', text='是否可借 (act)')
        tree.heading('srcUpdateTime', text='資料更新時間 (srcUpdateTime)')
        tree.heading('updateTime', text='即時更新時間 (updateTime)')
        tree.heading('infoTime', text='資料記錄時間 (infoTime)')
        tree.heading('infoDate', text='資料記錄日期 (infoDate)')
        tree.heading('total', text='總車位數 (total)')
        tree.heading('available_rent_bikes', text='可借車輛數 (available_rent_bikes)')
        tree.heading('available_return_bikes', text='可還空位數 (available_return_bikes)')
        tree.heading('latitude', text='緯度 (latitude)')
        tree.heading('longitude', text='經度 (longitude)')
        
        # 填充數據
        #populate_treeview(tree, youbike_data[-1140:-1040]) //士林區
        populate_treeview(tree, youbike_data[-520:-420])
        # Treeview滾動條
        scrollbar = ttk.Scrollbar(root, orient='vertical', command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar1 = ttk.Scrollbar(root, orient='horizontal', command=tree.xview)
        tree.configure(xscroll=scrollbar1.set)
        
        # 布局
        tree.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')
        
        # 調整窗口大小
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        
        # 進入Tkinter主循環
        root.mainloop()

if __name__ == "__main__":
    main()