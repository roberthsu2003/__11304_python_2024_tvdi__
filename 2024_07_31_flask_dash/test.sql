SELECT * 
FROM youbike;


SELECT DISTINCT sarea
FROM youbike;

SELECT sna as 站點,total as 總車輛數,rent_bikes as 可借,return_bikes as 可還, mday as 時間,act as 狀態
FROM youbike
WHERE (updatetime,sna) IN (
	SELECT MAX(updatetime),sna
	FROM youbike
	WHERE sarea = '大同區'
	GROUP BY sna
)


SELECT MAX(updatetime),sna
FROM youbike
WHERE sarea = '士林區'
GROUP BY sna