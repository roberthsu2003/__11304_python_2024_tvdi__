with open('names.txt',encoding='utf-8') as file:
    content:str = file.read()
names:list[str] = content.split()
for name in names:
    print(name)