USE `asm02_web`;

DELIMITER $$
CREATE PROCEDURE `all_published_posts`()
-- Tạo thủ tục để lấy được những bài viết đã được duyệt
BEGIN
	SELECT * FROM `post` WHERE `xet_duyet` = 1;
END$$
CREATE PROCEDURE `all_unreviewal_posts_before_2018_02_01`()
-- Tạo thủ tục để lấy những bài viết chưa được duyệt trước ngày 01-02-2018.
BEGIN
	SELECT * FROM `post` 
    WHERE NOT ISNULL(`xet_duyet`) AND `thoi_gian_dang` < '2018-02-01';
END$$

DROP FUNCTION IF EXISTS `largest_month_of_aged_posts_to_2019_03_01`$$
CREATE FUNCTION `largest_month_of_aged_posts_to_2019_03_01`() RETURNS INT
-- tạo function để tìm số tháng lớn nhất của các bài post đến ngày 01/03/2019
BEGIN
	DECLARE _result INT DEFAULT 0;
    SELECT MAX(TIMESTAMPDIFF(MONTH, `thoi_gian_dang`, '2019-03-01'))
    FROM `post` INTO _result;
    RETURN _result;
END$$
DELIMITER ;

CALL `all_published_posts`();
CALL `all_unreviewal_posts_before_2018_02_01`();
SELECT `largest_month_of_aged_posts_to_2019_03_01`();
SELECT TIMESTAMPDIFF(MONTH, `thoi_gian_dang`, '2019-03-01'), `thoi_gian_dang`
    FROM `post`;