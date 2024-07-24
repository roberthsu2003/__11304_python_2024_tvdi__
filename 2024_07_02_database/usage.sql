SELECT count(*) as 數量
FROM youbike;

SELECT *
FROM youbike;

DROP TABLE IF EXISTS youbike;

CREATE TABLE IF NOT EXISTS youbike(
                _id Serial Primary Key,
                sna VARCHAR(50) NOT NULL,
                sarea VARCHAR(50),
                ar VARCHAR(100),
                mday timestamp,
                updateTime timestamp,
                total SMALLINT,
                rent_bikes SMALLINT,
                return_bikes SMALLINT,
                lat REAL,
                lng REAL,
                act boolean,
				UNIQUE (sna, updateTime));

INSERT INTO youbike(sna, sarea, ar, mday, updatetime, total, rent_bikes,return_bikes,lat,lng,act)
            VALUES ('YouBike2.0_捷運科技大樓站',
			'大安區',
			'全家旁邊',
			'2035-03-01',
			'2024-07-02 09:37:20',
			100,100,100,100,100,true)
			ON CONFLICT (sna, updateTime) 
			DO NOTHING;