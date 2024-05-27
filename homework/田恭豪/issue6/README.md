## 請將以下網址的json,儲存為aqi.json檔 #6
#### 1.
import requests
from requests import Response

url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON'

res:Response = requests.get(url=url)

#### 2.
with open ("aqi.json", 'wb') as fd:
    for chunk in res.iter_content(chunk_size=128):
        fd.write(chunk)

##### [田恭豪_0520_issue6.](https://github.com/TedTian0502/Ted_window/blob/main/%E9%A1%9E%E5%88%A5/HW/issue6/0520.ipynb)