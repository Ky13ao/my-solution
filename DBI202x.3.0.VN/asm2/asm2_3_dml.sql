USE `asm02_web`;

-- table managers insert
INSERT INTO `managers`(`ten`, `nam_sinh`)
VALUES ('HOANG ANH', '1998'),
       ('VIET ANH', '1990' ),
	   ('QUYNH NGUYEN', '1995'),
	   ('THANH THAO', '1996' );

-- table reposter insert
INSERT INTO `reposter`(`ten`, `nam_sinh`, `to_chuc`)
VALUES ('TRANG NGUYEN', '1980', 'BAO THANH NIEN'),
		('TUAN ANH', '1999', 'BAO THE THAO'),
		('TRINH DUONG', '1995', 'BAO PHAP LUAT'),
		('THU THAO', '1997', 'DAI TRUYEN HINH VTC'),
		('VIET NGUYEN', '1990', 'BAO VOV GIAO THONG');

-- table user insert
INSERT INTO `user` (`account_name`, `password`, `facebook_user` , `email_user`)
VALUES ('THANG TRINH', '12341235', NULL, 'TRINHVANTHANG@GMAIL.COM'),
	   ('HOAI AN', '12356789', NULL, 'HOAIAN@GMAIL.COM'),
	   ('NGUYEN NAM', '12345676', 'NGUYEN NAM ' , 'NGUYENNAM@GMAIL.COM'),
	   ('DUNG NGUYEN', '45678453', 'DUNG CHERRY' , 'DUNGNGUYEN@GMAIL.COM'),
	   ('HOAN ANH TUAN', '66668888', 'TUAN ANH HOANG' , 'TUANANH@GMAIL.COM'), 
	   ('NGUYEN HAI ANH', '11112222', NULL, NULL),
	   ('TRINH LONG', '22221111', NULL, NULL),
	   ('NGUYEN LONG', '00001111', NULL, 'NGUYENLONG@GMAIL.COM'),
	   ('TRUONG THU THAO', '88889999', NULL, NULL),
	   ('LINH ANH', '11116666', 'ANH BLACKPINK', NULL);

-- table post insert
-- phần sét duyệt thì 1 là đã đươc duyệt, 0 là không được duyệt, null thì là chưa được duyệt.
INSERT INTO `post` (`tieu_de`, `noi_dung`, `image`, `luot_xem`, `xet_duyet`, `thoi_gian_dang`, `nguoi_duyet`, `tac_gia`)
VALUES ('LAO DONG', 'NGUOI LAO ĐONG ĐANG THAT NGHIEP NHIEU........', NULL, 20, 1, '2018-01-20', 1, 3),
	   ('TIN AN NINH', 'VAO HOI 12H....', NULL,  10, 1, '2018-01-20', 1, 4),
	   ('GIAO THONG VÀ BAI TOAN KET XE', 'HOM NAY....', NULL, 16, 0, '2018-01-21', 1, 1),
	  ('LUAT HON NHAN GIA DINH', 'THEO NGHI QUYET....', NULL, 30, 1, '2018-01-22', 4, 5),
	  ('GIAO DUC', 'KI THI THPT QUOC GIA NAM NAY....', NULL, 50, 1, '2018-02-22', 3, 2), 
	  ('GIAO THONG ', 'HOM NAY CÓ MO VU TAI NAN XE HOI....', NULL, 10, 1, '2018-02-24', 1, 1),
	  ('TIN QUOC TE', 'BÔ NGOAI GIAO VIET NAM SANG THAM CHINH PHU CAMPUCHIA....', NULL, 100, 1, '2018-01-24', 4, 5),
	  ('SUC KHOE NGUOI DAN', 'HOM NAY, BO CONG AN PHONG CHONG THUC PHAM DOC HAI ĐÃ....', NULL, 10, 1, '2018-03-25', 2, 5),
	  ('PHAP LUAT ', 'DU AN ALIBABA DA BỊ DNH CHI VI NGHI NGO CHU DOANH NGIEP NAY....', NULL, 50, 1, '2018-5-26', 1, 1),
	  ('AN NINH ', 'VAO HOI 15H CHIEU NGAY HOM NAY, CONG AN DA BAT QUA TANG....', NULL, 40, 1, '2018-06-24', 4, 1);


-- table comment insert
INSERT INTO `comment` (`time_comment`, `noi_dung`, `user_id`, `post_id`)
VALUES ('2018-01-22-12-20', 'TOI CUNG NGHI NHU VAY', 1, 1),
	   ('2018-01-22-12-21', 'KHONG THE CHAP NHAN DUOC', 4, 5),
	   ('2018-01-23-20-19', 'QUAN DIM CUA TOI VAN LÀ 1 VO 1 CHONG', 10, 5),
	   ('2018-03-24-20-13', 'RA LA VAY', 6, 5),
	   ('2018-03-25-12-01', 'GIAO THONG DAO NAY CHAN QUA', 8, 5),
	   ('2018-03-22-12-21', 'BUON THAT SU', 3, 1),
	   ('2018-03-24-12-20', 'XA HOI GIO LOAN LAM MOI NGUOI A', 8, 1),
	   ('2018-03-26-12-20', 'CHAN.......', 9, 4),
	   ('2018-03-12-12-20', 'MOI NGUOI CO LEN', 5, 4),
	   ('2018-03-12-12-20', 'CAC CHIEN SI TUYET VOI', 7, 4),
	   ('2018-03-12-12-20', 'CHUC CAC CHIEN SI LUON KHO MANH DE PHUC VU DAN', 2, 2),
	   ('2018-04-10-12-20', 'SAP TOI NGAY THUONG BINH LIET SI ROI', 3, 8),
	   ('2018-04-10-12-20', 'NAM NAY DE THI SE KHO DAY', 4, 2),
	   ('2018-04-20-12-20', 'KHONG BIET VAN SE RA DE GI DAY', 8, 9);
       
-- table share insert
-- DỮ LIỆU NÀY GIỜ DẠNG YY-MM-DD-MM-HH
INSERT INTO `share`(`time_share`, `user_id`, `post_id`)
VALUES ('2018-01-23-12-23', 1, 2),
	   ('2018-01-22-12-21', 4, 2),
	   ('2018-01-25-12-19', 5, 4),
	   ('2018-01-23-12-23', 3, 3),
	   ('2018-01-23-12-23', 5, 5),
	   ('2018-01-23-12-23', 6, 8),
	   ('2018-01-23-12-23', 8, 2),
	   ('2018-01-23-12-23', 10, 1),
	   ('2018-01-23-11-21', 8, 3),
	   ('2019-01-23-02-13', 9, 4),
	   ('2019-01-23-01-04', 1, 5),
	   ('2019-01-23-01-09', 5, 5),
	   ('2018-01-23-12-02', 2, 6),
	   ('2018-01-23-12-21', 2, 7),
	   ('2019-01-23-01-21', 4, 10),
	   ('2019-01-23-01-21', 3, 1),
	   ('2019-01-23-01-21', 6, 8),
	   ('2019-01-23-01-21', 5, 9);

