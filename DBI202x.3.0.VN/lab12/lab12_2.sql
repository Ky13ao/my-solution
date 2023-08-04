-- B1:
use online_shop;
start transaction;
insert into categories set name = 'name A';
select * from categories;
savepoint test1;