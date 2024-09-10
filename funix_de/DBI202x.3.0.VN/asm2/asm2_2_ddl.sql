CREATE DATABASE IF NOT EXISTS asm02_web;
USE asm02_web;

-- table managers
CREATE TABLE IF NOT EXISTS `managers` (
  `id_mng` INT NOT NULL AUTO_INCREMENT,
  `ten` VARCHAR(45),
  `nam_sinh` YEAR,
  CONSTRAINT `pk_id` PRIMARY KEY (`id_mng`)
);

-- table reposter
CREATE TABLE IF NOT EXISTS `reposter` (
  `id_reposter` INT NOT NULL AUTO_INCREMENT,
  `ten` VARCHAR(45),
  `nam_sinh` YEAR,
  `to_chuc` VARCHAR(255),
  CONSTRAINT `pk_id` PRIMARY KEY (`id_reposter`)
);

-- table user
CREATE TABLE IF NOT EXISTS `user` (
  `id_user` INT NOT NULL AUTO_INCREMENT,
  `account_name` VARCHAR(45),
  `password` VARCHAR(32),
  `facebook_user` VARCHAR(45),
  `email_user` VARCHAR(255),
  CONSTRAINT `pk_id` PRIMARY KEY (`id_user`),
  CONSTRAINT `chk_password_6_characters_plus` CHECK (LENGTH(`password`) >= 6)
);

-- table post
CREATE TABLE IF NOT EXISTS `post` (
  `id_post` INT NOT NULL AUTO_INCREMENT,
  `tieu_de` VARCHAR(100),
  `noi_dung` TEXT,
  `image` BLOB,
  `tac_gia` INT,
  `luot_xem` INT DEFAULT 0,
  `xet_duyet` BIT DEFAULT NULL,
  `nguoi_duyet` INT,
  `thoi_gian_dang` DATETIME DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT `pk_id` PRIMARY KEY (`id_post`),
  CONSTRAINT `fk_tac_gia_id` 
	FOREIGN KEY (`tac_gia`) REFERENCES `reposter`(`id_reposter`)
    ON DELETE SET NULL
    ON UPDATE CASCADE
  ,
  CONSTRAINT `fk_nguoi_duyet_id` 
	FOREIGN KEY (`nguoi_duyet`)  REFERENCES `managers`(`id_mng`)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);

-- table share
CREATE TABLE IF NOT EXISTS `share` (
  `id_share` INT NOT NULL AUTO_INCREMENT,
  `time_share` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `user_id` INT,
  `post_id` INT,
  CONSTRAINT `pk_id` PRIMARY KEY (`id_share`),
  CONSTRAINT `fk_share_user_id` 
	FOREIGN KEY (`user_id`) REFERENCES `user`(`id_user`)
    ON DELETE SET NULL
    ON UPDATE CASCADE
	,
  CONSTRAINT `fk_share_post_id` 
	FOREIGN KEY (`post_id`) REFERENCES `post`(`id_post`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

-- table comment
CREATE TABLE IF NOT EXISTS `comment` (
  `id_comment` INT NOT NULL AUTO_INCREMENT,
  `time_comment` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `noi_dung` TEXT,
  `user_id` INT,
  `post_id` INT,
  CONSTRAINT `pk_id` PRIMARY KEY (`id_comment`),
  CONSTRAINT `fk_comment_user_id`
	FOREIGN KEY (`user_id`) REFERENCES `user`(`id_user`)
    ON DELETE SET NULL
    ON UPDATE CASCADE
    ,
  CONSTRAINT `fk_comment_post_id` 
	FOREIGN KEY (`post_id`) REFERENCES `post`(`id_post`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);