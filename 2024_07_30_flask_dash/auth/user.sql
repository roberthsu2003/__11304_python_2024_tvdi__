CREATE TABLE IF NOT EXISTS 使用者(
	user_id SERIAL PRIMARY KEY,
	姓名 VARCHAR(20),
	性別 VARCHAR(20),
	聯絡電話 VARCHAR(20),
	電子郵件 VARCHAR(40),
	isGetEmail Bool,
	出生年月日 VARCHAR(20),
	自我介紹 VARCHAR(200),
	密碼 VARCHAR(100),
	連線密碼 VARCHAR(20)
);

INSERT INTO 使用者(姓名,電子郵件,密碼) 
VALUES('robert','roberthsu@gmail.com','12345')


SELECT *
FROM 使用者

SELECT 密碼,姓名
FROM 使用者
WHERE 電子郵件 = 'roberthsu@gmail.com'