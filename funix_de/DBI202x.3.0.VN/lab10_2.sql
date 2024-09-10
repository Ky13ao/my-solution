-- Lab 10.2 

create database online_shop;
use online_shop;
create table book(id int primary key auto_increment, name varchar(50) not null, notes varchar(100));
create view bookview as select id, name from book;
insert into bookview(id, name) values (2, "War and Peace");
select * from bookview;
drop view bookview;
select * from book;