import requests
from json import JSONDecodeError 
from pprint import pprint
from datetime import datetime
import json

def download_youbike_data():
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json'
    
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

def main():
    youbike_data = download_youbike_data()
    
    if youbike_data:
        print("台北市 YouBike 即時資料下載成功！")
        
        # 獲取當前日期時間
        current_datetime = datetime.now()
        
        # 格式化日期時間為您想要的格式
        datetime_str = current_datetime.strftime("%Y%m%d_%H%M%S")
        
        # 構建檔案名稱
        filename = f"youbike_{datetime_str}.json"
        
        # 存儲 YouBike 資料至 JSON 檔案
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(youbike_data, file, ensure_ascii=False, indent=4)
        
        print(f"資料已儲存至 {filename}")
        
        # 解析並顯示所需數據
        stations = youbike_data.get('retVal', {})
        for station_id, station_info in stations.items():
            print(f"站點編號 (sno): {station_info.get('sno', 'N/A')}")
            print(f"站點名稱 (sna): {station_info.get('sna', 'N/A')}")
            print(f"站點區域 (sarea): {station_info.get('sarea', 'N/A')}")
            print(f"更新時間 (mday): {station_info.get('mday', 'N/A')}")
            print(f"站點地址 (ar): {station_info.get('ar', 'N/A')}")
            print(f"站點區域英文 (sareaen): {station_info.get('sareaen', 'N/A')}")
            print(f"站點名稱英文 (snaen): {station_info.get('snaen', 'N/A')}")
            print(f"站點地址英文 (aren): {station_info.get('aren', 'N/A')}")
            print(f"是否可借 (act): {station_info.get('act', 'N/A')}")
            print(f"資料更新時間 (srcUpdateTime): {station_info.get('srcUpdateTime', 'N/A')}")
            print(f"即時更新時間 (updateTime): {station_info.get('updateTime', 'N/A')}")
            print(f"資料記錄時間 (infoTime): {station_info.get('infoTime', 'N/A')}")
            print(f"資料記錄日期 (infoDate): {station_info.get('infoDate', 'N/A')}")
            print(f"總車位數 (total): {station_info.get('tot', 'N/A')}")
            print(f"可借車輛數 (available_rent_bikes): {station_info.get('sbi', 'N/A')}")
            print(f"可還空位數 (available_return_bikes): {station_info.get('bemp', 'N/A')}")
            print(f"緯度 (latitude): {station_info.get('lat', 'N/A')}")
            print(f"經度 (longitude): {station_info.get('lng', 'N/A')}")
            print('-' * 40)

if __name__ == "__main__":
    main()
