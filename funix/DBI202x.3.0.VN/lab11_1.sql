-- Lab 11.1 https://docs.google.com/document/d/1oNCQ4Phj8v6zxlrfrbn7-Ev83XaZRBP_/edit


CREATE USER user1@localhost IDENTIFIED BY '1';
CREATE USER user2@localhost IDENTIFIED BY '1';
GRANT ALL PRIVILEGES ON *.* TO user1@localhost WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO user2@localhost WITH GRANT OPTION;

-- Quest3:
create database lab;
use lab;
create table student(
id int primary key auto_increment,
name varchar(100)
);
insert into student(name) values('name A'),('name B');
-- user1 all OK

-- Quest4:
use lab;
lock tables student write;
-- user1 OK
use lab;
select * from student;
-- user1 OK
use lab;
insert into student(name) values('name C');
-- user1 OK
use lab;
select * from student;
-- user2 Hang
use lab;
insert into student(name) values('name D');
-- user2 Hang, OK after user1 unlock table
use lab;
unlock table;
-- user1


-- Quest5:
use lab;
lock tables student read;
-- user1 OK
use lab;
select * from student;
-- user1 OK
use lab;
insert into student(name) values('name E');
-- user1 ERROR 1099 (HY000): Table 'student' was locked with a READ lock and can't be updated
use lab;
select * from student;
-- user 2 OK
use lab;
insert into student(name) values('name F');
-- user 2 Hang
use lab;
unlock table;
-- user 1 OK
use lab;
select * from student;
-- user 1 OK, chi co 'name F' duoc insert tu 'user2', 'name E' khong insert boi user1 duoc vi user1 dang lock table 'student'