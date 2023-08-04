CREATE DATABASE lab13;
USE lab13;
CREATE TABLE word_table(
    id INT AUTO_INCREMENT PRIMARY KEY,
    noun VARCHAR(255),
    adjective VARCHAR(255)
);
-- yeu cau 1
INSERT INTO word_table(noun, adjective)
VALUES  
    ('anger', 'angry'), 
    ('beauty', 'beautiful'),
    ('craziness', 'crazy'),
    ('danger', 'dangerous'),
    ('ease', 'easy'),
    ('happiness', 'happy'),
    ('juice', 'juicy'),
    ('kindness', 'kind'),
    ('pain', 'painful'),
    ('truth', 'true'),
    ('question', 'questionable');

-- yeu cau 2
-- MySQL khong can DELIMITER;
DELIMITER //
CREATE PROCEDURE getwords(INOUT nouns VARCHAR(255), INOUT adjectives VARCHAR(255))
BEGIN
    DECLARE all_nouns VARCHAR(255);
    DECLARE all_adjs VARCHAR(255);

    SELECT GROUP_CONCAT(noun) INTO all_nouns FROM word_table;
    SELECT GROUP_CONCAT(adjective) INTO all_adjs FROM word_table;

    SET nouns:= all_nouns;
    SET adjectives:=all_adjs;
END //
DELIMITER; 
SET @cac_danh_tu := '';
SET @cac_tinh_tu := '';
CALL getwords(@cac_danh_tu, @cac_tinh_tu);

SELECT @cac_danh_tu AS cac_danh_tu, @cac_tinh_tu AS cac_tinh_tu;

-- yeu cau 3
DROP FUNCTION IF EXISTS getstar;
DELIMITER //
CREATE FUNCTION getstar() RETURNS TEXT
BEGIN
    DECLARE words_count INT;
    DECLARE index_rand INT;
    DECLARE noun_word VARCHAR(255);
    DECLARE adjective_word VARCHAR(255);
    DECLARE words TEXT;

    SELECT COUNT(*) INTO words_count FROM word_table;
    SET index_rand := FLOOR(RAND() * words_count); 
    SET noun_word := (SELECT noun FROM word_table LIMIT index_rand, 1);
    SET index_rand := FLOOR(RAND() * words_count); 
    SET adjective_word := (SELECT adjective FROM word_table LIMIT index_rand, 1);
    SELECT CONCAT_WS(' ', noun_word, adjective_word) INTO words; 

    RETURN words; 

END //
DELIMITER ;

DROP PROCEDURE IF EXISTS getstars;
DELIMITER //
CREATE PROCEDURE getstars()
BEGIN
    DECLARE counter INT DEFAULT 0;
    DECLARE star VARCHAR(255);

    CREATE TEMPORARY TABLE stars(word VARCHAR(255));

    WHILE counter < 10 DO
        INSERT INTO stars (word) SELECT getstar();
        SET counter = counter + 1;
    END WHILE;
    
    SELECT * FROM stars;
    DROP TEMPORARY TABLE stars;
END //
DELIMITER ;

-- yeu cau 4
DELIMITER //
CREATE PROCEDURE rand_hw(INOUT height INT, INOUT weight INT)
BEGIN
    DECLARE lowerlim_weight DECIMAL;
    DECLARE higherlim_weight DECIMAL;
    SET height:= FLOOR(RAND() * 90 + 100);
    SET lowerlim_weight:= height/3;
    SET higherlim_weight:= height/2;
    SET weight:=FLOOR(RAND() * (higherlim_weight-lowerlim_weight) + lowerlim_weight);
END//
DELIMITER;

DROP PROCEDURE IF EXISTS get_hw;
DELIMITER //
CREATE PROCEDURE get_hw()
BEGIN
    DECLARE counter INT DEFAULT 0;
    CREATE TEMPORARY TABLE height_and_weight(
        height INT, 
        weight INT
    );
    SET @height := 0;
    SET @weight := 0;
    WHILE counter<10 DO
        CALL rand_hw(@height, @weight);
        INSERT INTO height_and_weight(height, weight) SELECT @height, @weight;
        SET counter:=counter+1;
    END WHILE;
    SELECT * FROM height_and_weight;
    DROP TEMPORARY TABLE height_and_weight;
END//
DELIMITER;