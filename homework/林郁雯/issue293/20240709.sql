SELECT count(*) as 數量
FROM youbike;

SELECT *
FROM youbike
WHERE sarea IN ('大安區','士林區')

DROP TABLE IF EXISTS youbike;

SELECT MAX(updatetime), sna
FROM youbike
GROUP BY sna


SELECT *
FROM youbike
WHERE (updatetime,sna) IN (
	SELECT MAX(updatetime), sna
FROM youbike
GROUP BY sna
	
	)
