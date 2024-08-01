-- Data Cleaning worldlifexpectancy
-- 1. **Handling Missing Values**:
-- - Identify missing values in the dataset.

SELECT
SUM(IF(`Country` IS NULL OR `Country`='', 1, 0)) `Country`,
SUM(IF(`Year` IS NULL, 1, 0)) `Year`,
SUM(IF(`Status` IS NULL OR `Status` = '', 1, 0)) `Status`,
SUM(IF(`Lifeexpectancy` IS NULL OR `Lifeexpectancy` = '', 1, 0)) `Lifeexpectancy`,
SUM(IF(`AdultMortality` IS NULL, 1, 0)) `AdultMortality`,
SUM(IF(`infantdeaths` IS NULL, 1, 0)) `infantdeaths`,
SUM(IF(`percentageexpenditure` IS NULL, 1, 0)) `percentageexpenditure`,
SUM(IF(`Measles` IS NULL, 1, 0)) `Measles`,
SUM(IF(`BMI` IS NULL, 1, 0)) `BMI`,
SUM(IF(`under-fivedeaths` IS NULL, 1, 0)) `under-fivedeaths`,
SUM(IF(`Polio` IS NULL, 1, 0)) `Polio`,
SUM(IF(`Diphtheria` IS NULL, 1, 0)) `Diphtheria`,
SUM(IF(`HIVAIDS` IS NULL, 1, 0)) `HIVAIDS`,
SUM(IF(`GDP` IS NULL, 1, 0)) `GDP`,
SUM(IF(`thinness1-19years` IS NULL, 1, 0)) `thinness1-19years`,
SUM(IF(`thinness5-9years` IS NULL, 1, 0)) `thinness5-9years`,
SUM(IF(`Schooling` IS NULL, 1, 0)) `Schooling`,
SUM(IF(`Row_ID` IS NULL, 1, 0)) `Row_ID`
 FROM `worldlifexpectancy`;

-- - Decide on strategies to handle missing values.
-- -- Handling missing values of status with exists status by country
SELECT * FROM `worldlifexpectancy` WHERE `Status` = '';
SELECT DISTINCT `Status` FROM `worldlifexpectancy` WHERE `Status` != '';


-- -- Handling missing values Lifeexpectancy
SELECT * FROM `worldlifexpectancy` WHERE `Lifeexpectancy` = '';
-- --- Missing data on 2 countries: Afghanistan and Albania
SELECT `Country`, `Year`, `Lifeexpectancy` 
FROM `worldlifexpectancy` 
WHERE `Country` REGEXP 'Afghanistan|Albania';
/*
It is evident that the life expectancy of Afghanistan and Albania is consistently
increasing over time. Therefore, to address the null values, we can consider utilizing 
the median value between the preceding and succeeding life expectancy values.
*/
UPDATE `worldlifexpectancy` AS w
JOIN (
    SELECT AVG(CAST(`Lifeexpectancy` AS DOUBLE)) AS `avg_lifeexpectancy`
    FROM `worldlifexpectancy`
    WHERE Lifeexpectancy IS NOT NULL AND LENGTH(TRIM(`Lifeexpectancy`)) > 0
) AS avg_table
SET w.`Lifeexpectancy` = avg_table.`avg_lifeexpectancy`
WHERE w.`Lifeexpectancy` IS NULL OR LENGTH(TRIM(w.`Lifeexpectancy`)) = 0;
-- 2. **Data Consistency**:
-- - Check for and correct inconsistencies in categorical columns like `Country` and `Status`.
-- - Check for inconsistencies in `Country` columns:
SELECT DISTINCT `Country` FROM `worldlifexpectancy`;
-- -- Update the C├┤te d'Ivoire country to 'Côte d''Ivoire'
UPDATE `worldlifexpectancy`
SET `Country` = 'Côte d''Ivoire'
WHERE `Country` = 'C├┤te d''Ivoire';

-- - Correct inconsistencies in `Status` columns:
UPDATE `worldlifexpectancy` w
JOIN (
  SELECT `Country`, MAX(`Status`) nonBlankStatus
  FROM `worldlifexpectancy` 
  WHERE `Status` != '' GROUP BY `Country`) AS sub 
ON w.`Country` = sub.`Country`
SET w.`Status` = sub.nonBlankStatus
WHERE w.`Status` = '';

-- - Check inconsistencies in `Lifeexpectancy` columns:
SELECT w1.`Country`, w3.`Year`, w3.`Lifeexpectancy`, w1.`Year`, w1.`Lifeexpectancy`, ROUND((w3.Lifeexpectancy+w2.Lifeexpectancy)/2,1) new_le, w2.`Year`, w2.`Lifeexpectancy`
FROM `worldlifexpectancy` w1
JOIN `worldlifexpectancy` w2 ON w1.`Country`=w2.`Country` AND w1.`Year` =w2.`Year`-1
JOIN `worldlifexpectancy` w3 ON w1.`Country`=w3.`Country` AND w1.`Year` =w3.`Year`+1
WHERE w1.`Lifeexpectancy` = '';
-- - Correct
UPDATE `worldlifexpectancy` w1
JOIN `worldlifexpectancy` w2 ON w1.`Country`=w2.`Country` AND w1.`Year` =w2.`Year`-1
JOIN `worldlifexpectancy` w3 ON w1.`Country`=w3.`Country` AND w1.`Year` =w3.`Year`+1
SET w1.`Lifeexpectancy` = ROUND((w3.Lifeexpectancy+w2.Lifeexpectancy)/2,1)
WHERE w1.`Lifeexpectancy` = '';

-- 3. **Removing Duplicates**:
-- - Identify and remove duplicate rows if any.
-- -- Ensure no duplicates on `Row_ID` column
SELECT `Row_ID`, COUNT(*) as countrows FROM `worldlifexpectancy` GROUP BY `Row_ID` HAVING countrows>1;
-- -- Identify Row_ID unique paired `Country`, `Year` columns
SELECT MIN(`Row_ID`) FROM `worldlifexpectancy` GROUP BY `Country`, `Year`;
-- -- Remove duplicates
DELETE FROM `worldlifexpectancy`
WHERE `Row_ID` NOT IN (SELECT MIN(`Row_ID`) FROM `worldlifexpectancy` GROUP BY `Country`, `Year`);

-- 4. **Outlier Detection and Treatment**:
-- -  Identify and treat outliers in columns like `Lifeexpectancy`, `AdultMortality`, and `GDP`.
SELECT MIN(`Q`) `Q1`, MAX(`Q`) `Q3` FROM (
  SELECT MAX(`Lifeexpectancy`) `Q`
  FROM (
    SELECT `Lifeexpectancy`, 
          ntile(4) OVER (ORDER BY `Lifeexpectancy`) quartile 
    FROM `worldlifexpectancy`) as quartile_le 
  WHERE quartile IN (1,3) 
  GROUP BY quartile) AS IQR;

SELECT w.`Country`, w.`Year`, w.`Lifeexpectancy`,(w.`Lifeexpectancy` - z.mean)/z.stdd `Zscore`
FROM `worldlifexpectancy` w
CROSS JOIN (SELECT AVG(`Lifeexpectancy`) mean, STDDEV(`Lifeexpectancy`) stdd 
            FROM `worldlifexpectancy` WHERE `Lifeexpectancy` != '0') z
HAVING `Zscore`<-3 OR `Zscore`>3;

-- - Decide on strategies to handle outlier (eg. avg)