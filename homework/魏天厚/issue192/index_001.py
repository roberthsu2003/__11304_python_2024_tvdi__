import requests
from pprint import pprint

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
        # 解析並顯示部分數據
        stations = youbike_data.get('retVal', {})
        for station_id, station_info in stations.items():
            print(f"站點名稱: {station_info['sna']}")
            print(f"可借車輛數: {station_info['sbi']}")
            print(f"可還空位數: {station_info['bemp']}")
            print(f"更新時間: {station_info['mday']}")
            print('-' * 40)
            break  # 只顯示一個站點的數據

if __name__ == "__main__":
    main()
