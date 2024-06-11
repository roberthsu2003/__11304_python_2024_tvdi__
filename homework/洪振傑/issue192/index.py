import requests 
from requests import Response,JSONDecodeError
import tools

def GetDownloadJson():
    ubike_url="https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    try:
        res=requests.get(ubike_url)
    except Exception :
        raise("連線失敗")
    else:
        if res.status_code == 200:
            try:
                #此已經是普通字串 雖然是json格式
                all_data:dict[any]= res.json()
                return all_data
            except JSONDecodeError:
                raise Exception("api_key為測試用,連線已至上限,請稍後再試,josn格式錯誤")
        else:
            raise Exception("下載狀態不是200")
        
def main():
    alldata=GetDownloadJson()
    data = tools.GetData(alldata)

    print(data)
        
if __name__ =="__main__":
    main()