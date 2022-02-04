DROP TABLE IF EXISTS users;
--初期化
CREATE TABLE IF NOT EXISTS users(
            name TEXT,
            age INTEGER
            );
--テーブル作る
INSERT INTO users
VALUES
    ('Bob',15),
    ('Tom',57),
    ('Ken',73)
