import gpsd-py3

def get_gps_coordinates():
    try:
        # 連接到 GPS 服務
        gpsd.connect()

        # 獲取 GPS 資料
        packet = gpsd.get_current()

        # 確保我們已獲取到了有效的 GPS 資料
        if packet.mode >= 2:
            latitude = packet.lat
            longitude = packet.lon
            return latitude, longitude
        else:
            print("GPS 資料無效。")
            return None, None
    except Exception as e:
        print("發生錯誤：", e)
        return None, None



def main():
    # 獲取 GPS 座標
    latitude, longitude = get_gps_coordinates()

    if latitude is not None and longitude is not None:
    
    window = Window(theme='breeze')
    window.mainloop()

if __name__ == '__main__':
    main()