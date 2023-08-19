-- mysql-ctl cli : cau lenh dung de dang nhap vao mysql cli

SHOW DATABASES;
CREATE DATABASE soap_store;
USE soap_store;
SELECT DATABASE();
DROP DATABASE soap_store;

-- Lab 2.2 Drop database

-- Thực hiện lần lượt các câu truy vấn dưới đây trong giao GoormIDE:
DROP DATABASE data_name; -- (Xoá một database hiện có)
CREATE DATABASE dog_walking_app;
USE dog_walking_app;
SELECT DATABASE(); -- (In ra database đang được sử dụng)


-- Lab 2.3 Create Table – Drop Table
-- Yêu cầu 1: Tạo database tên cat_app.
CREATE DATABASE cat_app;
-- Yêu cầu 2: Trong database cat_app, tạo bảng pastries có hai trường (cột) như sau:
USE cat_app;
CREATE TABLE pastries(
  name VARCHAR(50),
  quantity INT
);
-- Trường name có kiểu dữ liệu VARCHAR(50)
-- Trường quantity có kiểu dữ liệu int
-- Yêu cầu 3: Sau khi tạo xong bảng pastries, hãy hiển thị các bảng hiện có trong cơ sở dữ liệu cat_app
SHOW TABLES;

-- Yêu cầu 4: Xoá table pastries
DROP TABLE pastries;
-- Yêu cầu 5: Hiển thị lại các table hiện có trong database cat_app.
SHOW TABLES;