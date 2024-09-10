USE `asm02_web`;

DROP TABLE IF EXISTS `CommentCountDayByDayAndUser`;
CREATE TABLE `CommentCountDayByDayAndUser`(
	`date_of_comment` DATE,
    `user_id` INT,
    `comment_count` INT DEFAULT 0,
    PRIMARY KEY (`date_of_comment`, `user_id`),
    FOREIGN KEY (`user_id`) REFERENCES `user`(`id_user`)
);

DELIMITER $$
DROP TRIGGER IF EXISTS `TRG_BEFORE_INSERT_COMMENT`$$
CREATE TRIGGER `TRG_BEFORE_INSERT_COMMENT`
BEFORE INSERT ON `comment` FOR EACH ROW
BEGIN
	DECLARE `_comment_count` INT;
    DECLARE `_comment_date` DATE DEFAULT DATE(NEW.`time_comment`);
    SELECT COUNT(*) FROM `comment` WHERE `user_id` = NEW.`user_id` and DATE(`time_comment`) = `_comment_date` INTO `_comment_count`;
    IF (`_comment_count`)>0 THEN
		SET `_comment_count`:=`_comment_count`+1;
        UPDATE `CommentCountDayByDayAndUser`
        SET `comment_count`=`comment_count`
        WHERE `user_id`=NEW.`user_id` AND `date_of_comment`=`_comment_date`;
    ELSE
		INSERT INTO `CommentCountDayByDayAndUser` 
			(`comment_count`, `user_id`, `date_of_comment`) 
		VALUES (1, NEW.`user_id`, `_comment_date`);
    END IF;
END$$
DELIMITER ;

SELECT * FROM `CommentCountDayByDayAndUser`;
-- compare trigger with group by date and user query from comment
SELECT DATE(`time_comment`) `date_of_comment`, `user_id`, COUNT(*) `comment_count`
FROM `comment`
GROUP BY `user_id`, DATE(`time_comment`);

-- Đánh index bảng user
-- 		tối ưu hóa tìm kiếm user bằng account_name bằng index account_name_idx
-- 		tối ưu hóa tìm kiếm user bằng email_user bằng index email_user_idx
ALTER TABLE `user`
ADD INDEX `account_name_idx` (`account_name`),
ADD INDEX `email_user_idx` (`email_user`);

-- Đánh index bảng post
--		tối ưu hóa tìm kiếm post bằng tác giả bằng index tac_gia_idx
-- 		tối ưu hóa tìm kiếm post bằng người duyệt bằng index nguoi_duyet_idx
--		tối ưu hóa tìm kiếm và sắp xếp bảng post bằng thời gian đăng bằng index thoi_gian_dang_idx
ALTER TABLE `post`
ADD INDEX `tac_gia_idx` (`tac_gia`),
ADD INDEX `nguoi_duyet_idx` (`nguoi_duyet`),
ADD INDEX `thoi_gian_dang_idx` (`thoi_gian_dang`);

-- Đánh index bảng comment và share
-- 		tối ưu hóa tìm kiếm và liên kết quan hệ N-M comment/share với post và user bằng user qua index user_idx
-- 		tối ưu hóa tìm kiếm và liên kết quan hệ N-M comment/share với post và user bằng post qua index post_idx
ALTER TABLE `comment`
ADD INDEX `user_idx` (`user_id`),
ADD INDEX `post_idx` (`post_id`);

ALTER TABLE `share`
ADD INDEX `user_idx` (`user_id`),
ADD INDEX `post_idx` (`post_id`);