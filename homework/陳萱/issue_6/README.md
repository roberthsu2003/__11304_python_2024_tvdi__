# 這是第二次作業


[JSON檔案](https://github.com/NoktoX/__python-test-0516__/blob/main/%E9%A1%9E%E5%88%A5/download/aqi.json)
> 請將以下網址的json,儲存為**aqi.json檔**
```python
url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON'
```
>將位址使用requests.get **賦值**response

```python
response:Response = requests.get(url)
```
[原始碼檔案](https://github.com/NoktoX/__python-test-0516__/blob/main/%E9%A1%9E%E5%88%A5/download/lesson2.ipynb)


>使用**model requests**的內建功能

```python
import requests
from requests import Response

url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON'
res:Response = requests.get(url=url)
```

```python
with open("aqi1.json","wb") as fd:
    for chunk in response.iter_content(chunk_size=128):
        fd.write(chunk)
```