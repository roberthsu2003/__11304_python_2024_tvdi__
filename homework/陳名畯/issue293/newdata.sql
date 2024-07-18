SELECT *
FROM youbike
WHERE (updatetime,sna) IN (
	    SELECT MAX(updatetime), sna
        FROM youbike
        GROUP BY sna
)