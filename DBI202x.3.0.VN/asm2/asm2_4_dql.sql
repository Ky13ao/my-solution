USE `asm02_web`;

-- Truy vấn tất cả bảng `post` và `managers`:
SELECT * FROM `post`;
SELECT * FROM `managers`;

-- Truy vấn tất cả các post bảng `post` có `luot_xem` lớn hơn 20:
SELECT * FROM `post` WHERE `luot_xem`>20;

-- Trong bảng POST, viết truy vấn những bài viết đã được xét duyệt
-- và sắp xếp kết quả theo thứ tự bảng chữ cái của cột tiêu đề:
SELECT `tieu_de`, `noi_dung`, `luot_xem`, `xet_duyet`, `nguoi_duyet`, `thoi_gian_dang` 
FROM `post` WHERE `xet_duyet`=1 ORDER BY `tieu_de` ASC;

-- Viết truy vấn để lấy tên các acount_name của user comment vào POST: 
SELECT c.`user_id` `nguoi_comment`, u.`account_name` `account_name`, c.`noi_dung` `noi_dung`
FROM `comment` c
INNER JOIN `user` u ON c.`user_id` = u.`id_user`;

-- Viết truy vấn để tìm nội dung bài viết bắt đầu bằng chữ ‘n’:
SELECT * FROM `post`
WHERE `noi_dung` LIKE 'n%';

-- Tạo VIEW để lấy ra những bài viết đã được duyệt bởi những người quản lý:
CREATE VIEW `approved_posts_by_managers`
AS 
SELECT m.`id_mng`, m.`ten` `nguoi_duyet`, p.`tieu_de`, p.`noi_dung`, p.`xet_duyet`, p.`thoi_gian_dang`
FROM `managers` m
INNER JOIN `post` p ON p.`nguoi_duyet` = m.`id_mng`
WHERE p.`xet_duyet` = 1;
SELECT * FROM `approved_posts_by_managers`;

-- Tạo VIEW để lấy ra các comment của user:
CREATE VIEW `all_comments_by_users`
AS
SELECT c.`noi_dung` `noi_dung_comment`, u.`id_user`, u.`account_name`, p.`tieu_de` `tieu_de_bai_viet`, p.`noi_dung` `noi_dung_bai_viet`
FROM `user` u
INNER JOIN `comment` c ON c.`user_id` = u.`id_user`
INNER JOIN `post` p ON p.`id_post` = c.`post_id`;
SELECT * FROM `all_comments_by_users`;
