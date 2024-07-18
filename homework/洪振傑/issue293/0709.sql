-- select *
-- from ubike_data

-- SELECT *
-- FROM ubike_data
-- WHERE sarea IN ('大安區')

-- SELECT MAX(updatetime),sna
-- FROM ubike_data
-- GROUP BY sna

-- select *
-- from ubike_data
-- where(updatetime,sna) in (('2024-07-09 09:07:52','康寧路三段189巷93弄口'),
-- 								('2024-07-09 09:07:52','建國和平路口西北側'))

-- select *
-- from ubike_data
-- where(updatetime,sna) in(
-- 	SELECT MAX(updatetime),sna
-- 	FROM ubike_data
-- 	GROUP BY sna
-- )