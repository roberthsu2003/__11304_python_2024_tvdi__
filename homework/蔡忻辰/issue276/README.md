# 0624_作業11_issue276

## 下載youbike的資料,進入postgreSQL的youbike的table (updatetime + sna的2個欄位的值不可以重覆)

### UNIQUE(sna, updateTime)
### ON CONFLICT (sna, updateTime) DO NOTHING
## [程式碼連接](./index.py)

### postgreSQL
![pgSQL](./image/pgSQL.png)