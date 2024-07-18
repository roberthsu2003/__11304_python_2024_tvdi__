[程式碼](lesson2.py)
[data模組](./data.py)

> ## 建立資料庫

```
def create_database(conn:psycopg2.extensions.connection):
    # sql操作
    with conn: #自動 commit
        with conn.cursor() as cursor:
            sql='''
    create table if not exists Ubike_Data(
        _id serial primary key,
        sna varchar(50) not null,
        sarea varchar(50),
        ar varchar(100),
        mday timestamp,
        updatetime timestamp,
        total smallint,
        retuen_bikes smallint,
        rent_bikes smallint,
        latitude real,
        longitude real,
	    act boolean,
        CONSTRAINT unique_updatetime_sarea UNIQUE (updatetime, sna)
    );
    '''
            cursor.execute(sql)
```

> ## 存入資料庫

```
def store_date(conn:psycopg2.extensions.connection,all_data:list[dict]):
    with conn:
        with conn.cursor() as cursor:
            insert_spl='''
        insert into Ubike_Data(sna,sarea,ar,mday,updatetime,total,retuen_bikes,rent_bikes,latitude,longitude,act)
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        )ON CONFLICT (updatetime, sna) DO NOTHING;
        '''
            for site in all_data:
                cursor.execute(insert_spl,(site['sna']
                                ,site['sarea'],
                                site['ar'],
                                site['mday'],
                                site['updateTime'],
                                site['total'],
                                site['rent_bikes'],
                                site['rent_bikes'],
                                site['latitude'],
                                site['longitude'],
                                site['act']))
```

