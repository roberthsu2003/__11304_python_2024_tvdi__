# issue164

[HW_issue164 連結](https://github.com/NoktoX/__11304_python_2024_tvdi__/blob/main/homework/%E9%99%B3%E8%90%B1/issue164/hw.ipynb)

## 讀檔
```python
with open("data.json",mode="r",encoding="utf-8") as file:
    data:str=file.read()
```

## 資料結構
```python
class Project(BaseModel):
    name:str
    status:str

class Address(BaseModel):
    street:str
    city:str
    zipcode:str

class Root(BaseModel):
    name:str
    age:int
    address:Address
    projects:list[Project]
```

## 轉檔
```python
try:
    r1:Root=Root.model_validate_json(data)
except ValidationError as e:
    print(e)
else:
    print(r1.model_dump())
```