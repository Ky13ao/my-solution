-- Lab8.1: https://docs.google.com/document/d/10ao9JIIxN0c5E5NathdaKikk_z7QYuOW/edit

-- Yêu cầu 1: Thực hiện các truy vấn

SELECT CURTIME();
SELECT CURDATE();
SELECT DAYOFWEEK(CURDATE());
SELECT DAYOFWEEK(NOW());
SELECT DATE_FORMAT(NOW(), '%w') + 1;
SELECT DAYNAME(NOW());
SELECT DATE_FORMAT(NOW(), '%W');
SELECT DATE_FORMAT(CURDATE(), '%m/%d/%Y');
SELECT DATE_FORMAT(NOW(), '%M %D at %h:%i');

-- Yêu cầu 2: INSERT dữ liệu thời gian

CREATE TABLE tweets(
  content VARCHAR(140),
  username VARCHAR(20),
  created_at TIMESTAMP default NOW()
);

INSERT INTO tweets(content, username) 
VALUES
('this is my first tweet', 'coltscat'),
('this is my second tweet', 'coltscat');

SELECT created_at FROM tweets;