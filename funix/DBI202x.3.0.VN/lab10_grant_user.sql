-- tao user 'teo' voi password la '1'
create user teo@localhost identified by '1';

-- tao 1 terminal khac de dang nhap user voi cli nhu sau
-- mysql -u teo -p
-- sau do moi nhap password theo prompt cua cli

-- cap quyen cho user teo tren user root
grant all privileges on *.* to teo@localhost with grant option;

-- loại bỏ các quyền trước khi xóa user
revoke all privileges on *.* to teo@localhost;
drop user teo@localhost;
flush privileges;
