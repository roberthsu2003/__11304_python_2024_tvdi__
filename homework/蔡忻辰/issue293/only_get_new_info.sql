SELECT * FROM youbike


SELECT * FROM youbike
WHERE (sarea) IN ('大安區', '士林區')

SELECT MAX (updatetime), sna
FROM youbike
GROUP BY sna

-- 抓特定資料
SELECT * FROM youbike
WHERE (updatetime, sna) IN (
		('2024-07-05 15:22:51', '三民公園(塔悠路)'),
		('2024-07-05 15:22:51','三民國小(撫遠街)')
	)

SELECT * FROM youbike
WHERE (updatetime, sna) IN (
		SELECT MAX (updatetime), sna 
		FROM youbike
		GROUP BY sna
	)

