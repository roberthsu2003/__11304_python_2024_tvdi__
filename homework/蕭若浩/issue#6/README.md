# 第二次作業
### [hw.ipynb](./hw.ipynb)

- 作業內容：請將以下網址,儲存為aqi.json檔
>url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON'

- 方法：使用內建的model requests, 設定為json檔  
```
with open("aqi.json","wb") as fd:  
    for chunk in response.iter_content(chunk_size=128):  
       fd.write(chunk)
```
### [python code連結](./hwcode.py)
### [json檔連結](./aqi.json)