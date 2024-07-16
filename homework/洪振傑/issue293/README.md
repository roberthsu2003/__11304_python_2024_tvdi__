> ## sql語法

[sql_code](./0709.sql)

```
select *
from ubike_data
where(updatetime,sna) in(
	SELECT MAX(updatetime),sna
	FROM ubike_data
	GROUP BY sna
)
```