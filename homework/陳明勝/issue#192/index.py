import requests

def download_youbike_data():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to download YouBike data")
        return None

youbike_data = download_youbike_data()
if youbike_data:
    # 在这里可以对数据进行进一步处理和分析
    print(youbike_data)