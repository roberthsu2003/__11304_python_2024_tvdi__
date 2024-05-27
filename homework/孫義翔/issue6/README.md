# 第二次作業
## 作業程式碼
'https://github.com/Ian092/Ian_window/blob/main/homework/Issues6/Issues%206.ipynb'


## 請將以下網址的json,儲存為aqi.json檔
'https://github.com/Ian092/Ian_window/blob/main/homework/Issues6/Issues%206.JOSN'

## 將位址使用requests.get 賦值response
response:Response = requests.get(url)

## 使用model requests的內建功能
with open("aqi1.json","wb") as fd:
    for chunk in response.iter_content(chunk_size=128):
        fd.write(chunk)