-- Data Cleaning
-- 1. **Data Consistency**:
--    - Check for and correct inconsistencies.
--- correct Type field
SELECT MAX(`Type`), COUNT(*)
FROM us_household_income
GROUP BY BINARY `Type`
ORDER BY 1;

UPDATE us_household_income
SET `Type` = 'CDP'
WHERE `Type` = 'CPD';

UPDATE us_household_income
SET `Type` = 'City'
WHERE `Type` = 'CITY';

UPDATE us_household_income
SET `Type` = 'Borough'
WHERE `Type` = 'Boroughs';

UPDATE us_household_income
SET `Type` = 'Village'
WHERE `Type` = 'village';

--- correct State_Name field
SELECT MAX(`State_Name`), COUNT(*)
FROM us_household_income
GROUP BY BINARY `State_Name`
ORDER BY 1;

UPDATE us_household_income
SET `State_Name` = 'Georgia'
WHERE `State_Name` = 'georia';

UPDATE us_household_income
SET `State_Name` = 'Alabama'
WHERE `State_Name` = 'alabama';

-- correct County field
SELECT MAX(`County`), COUNT(*)
FROM us_household_income
GROUP BY BINARY `County`
ORDER BY 1;

UPDATE us_household_income
SET County = 'Doña Ana County'
WHERE County REGEXP 'Do.+a Ana County';

-- 2. **Removing Duplicates**:
--    - Identify and remove duplicate rows if any.
----- Identify duplicate rows
--- method 1
SELECT `id`, count(*), min(`row_id`)
FROM us_household_income
GROUP BY `id`
HAVING count(*)>1;
--- method 2
SELECT * FROM (SELECT row_id
    , id
    , ROW_NUMBER() OVER (PARTITION BY `id` ORDER BY `id`) row_num
FROM us_household_income) as duplicates
WHERE row_num > 1;

WITH duplicate_rows AS (
    SELECT MIN(row_id) AS first_row_id
    FROM us_household_income
    GROUP BY id
    HAVING COUNT(*) > 1
)
DELETE FROM us_household_income
WHERE row_id IN (SELECT first_row_id FROM duplicate_rows);


-- EDA

-- Here are 23 tasks to practice your MySQL skills and perform exploratory data analysis (EDA) to extract meaningful insights:

-- - Tasks 1 - 9: 0.5 points each.
-- - Tasks 10 - 22: 1 point each.
-- - Task 0: 2 point.
-- Task 0: Summarizing Data by State (Special)
-- Question:
-- Assume that you will have new data each week. Can you please create store procedure and create event to active procedure every weeks to update and clean new data (From Cleaning Tasks)?
-- Hint: TimeStamp
DROP PROCEDURE IF EXISTS task0_cleanup_weekly;
DELIMITER $$
CREATE PROCEDURE task0_cleanup_weekly()
BEGIN
    -- correcting tasks
   UPDATE us_household_income
   SET `Type` = 'CDP'
   WHERE `Type` = 'CPD';

   UPDATE us_household_income
   SET `Type` = 'City'
   WHERE `Type` = 'CITY';

   UPDATE us_household_income
   SET `Type` = 'Borough'
   WHERE `Type` = 'Boroughs';

   UPDATE us_household_income
   SET `Type` = 'Village'
   WHERE `Type` = 'village';

   UPDATE us_household_income
   SET `State_Name` = 'Georgia'
   WHERE `State_Name` = 'georia';

   UPDATE us_household_income
   SET `State_Name` = 'Alabama'
   WHERE `State_Name` = 'alabama';

   UPDATE us_household_income
   SET County = 'Doña Ana County'
   WHERE County REGEXP 'Do.+a Ana County';

    -- remove duplicate tasks
   WITH duplicate_rows AS (
      SELECT MIN(row_id) AS first_row_id
      FROM us_household_income
      GROUP BY id
      HAVING COUNT(*) > 1
   )
   DELETE FROM us_household_income
   WHERE row_id IN (SELECT first_row_id FROM duplicate_rows);
END$$
DELIMITER ;

DROP EVENT IF EXISTS task0_cleanup_weekly_event;
CREATE EVENT task0_cleanup_weekly_event
ON SCHEDULE EVERY 1 WEEK
DO
CALL task0_cleanup_weekly();

-- Task 1: Summarizing Data by State
-- Question:
-- Can you provide a summary report that shows the average land area and average water area for each state? Please include the state name and abbreviation, and order the results by the average land area in descending order.
SELECT `State_Name`
       , `State_ab`
       , AVG(ALand) avg_land_area
       , AVG(AWater) avg_water_area
FROM us_household_income
GROUP BY `State_Name`, `State_ab`
ORDER BY avg_land_area;

-- Task 2: Filtering Cities by Population Range
-- Question:
-- We need a list of all cities where the land area is between 50,000,000 and 100,000,000 square meters. Include the city name, state name, and county in the results, and order the list alphabetically by city name.
SELECT `State_Name`
       , `City`
       , ALand land_area
FROM us_household_income
WHERE ALand >= 50000000 AND ALand <= 100000000
ORDER BY `City`;

-- Task 3: Counting Cities per State
-- Question:
-- Can you generate a report that counts the number of cities in each state? The report should include the state name and abbreviation and be ordered by the number of cities in descending order.
SELECT `State_Name`
       , `State_ab`
       , COUNT(`City`) Number_of_cities
FROM us_household_income
GROUP BY `State_Name`, `State_ab`
ORDER BY `Number_of_cities` DESC;

-- Task 4: Identifying Counties with Significant Water Area
-- Question:

-- Please identify the top 10 counties with the highest total water area. The report should include the county name, state name, and total water area, ordered by total water area in descending order.
SELECT `State_Name`
       , `State_ab`
       , `County`
       , SUM(`AWater`) Total_water_area
FROM us_household_income
GROUP BY `State_Name`, `State_ab`, `County`
ORDER BY `Total_water_area` DESC
LIMIT 10;

-- Task 5: Finding Cities Near Specific Coordinates
-- Question:
-- We are looking for a list of all cities within a specific latitude and longitude range (latitude between 30 and 35, longitude between -90 and -85). Include the city name, state name, county, and coordinates, and order the results by latitude and then by longitude.
SELECT `City`
       , `State_Name`
       , `County`
       , `Lat` latitude
       , `Lon` longitude
FROM us_household_income
WHERE `Lat` >= 30 AND `Lat` <= 35
    AND `Lon` >= -90 AND `Lon` <=-85
ORDER BY `Lat`, `Lon`;

-- Task 6: Using Window Functions for Ranking
-- Question:
-- We need to rank cities within each state based on their land area. Please use a window function to assign ranks and include the city name, state name, land area, and rank in your results. The report should be ordered by state name and rank.
SELECT `City`
       , `State_Name`
       , ALand
       , RANK() OVER (PARTITION BY `State_Name` ORDER BY `ALand`) `rank`
FROM us_household_income
ORDER BY `State_Name`, `rank`;


-- Task 7: Creating Aggregate Reports
-- Question:
-- Can you generate a report showing the total land area and water area for each state, along with the number of cities in each state? Include the state name and abbreviation, and order the results by the total land area in descending order.
SELECT `State_Name`
       , `State_ab`
       , SUM(`ALand`) Total_land_area
       , SUM(`AWater`) Total_water_area
       , COUNT(`City`) Number_of_cities
FROM us_household_income
GROUP BY `State_Name`, `State_ab`
ORDER BY `Total_land_area` DESC;


-- Task 8: Subqueries for Detailed Analysis
-- Question:
-- Can you provide a list of all cities where the land area is above the average land area of all cities? Use a subquery to calculate the average land area. The report should include the city name, state name, and land area, ordered by land area in descending order.
SELECT `City`
       , `State_Name`
       , `ALand` land_area
FROM us_household_income
WHERE ALand > (SELECT AVG(ALand) FROM us_household_income)
ORDER BY `land_area` DESC;


-- Task 9: Identifying Cities with High Water to Land Ratios
-- Question:
-- Can you identify cities where the water area is greater than 50% of the land area? Include the city name, state name, land area, water area, and the calculated water to land ratio, and order the results by the water to land ratio in descending order.
SELECT `City`
       , `State_Name`
       , `ALand` land_area
       , `AWater` water_area
       , ROUND((`AWater`/`ALand`)*100,2) land_area_ratio
FROM us_household_income
WHERE `AWater` > (`ALand`/2)
ORDER BY `land_area_ratio` DESC;


-- Task 10: Dynamic SQL for Custom Reports
-- Question:

-- Can you create a stored procedure that accepts a state abbreviation as input and returns a detailed report for that state? The report should include the total number of cities, average land area, average water area, and a list of all cities with their respective land and water areas.
DROP PROCEDURE IF EXISTS task10_get_state_report;
DELIMITER $$
CREATE PROCEDURE task10_get_state_report (IN stateAb CHAR(2))
BEGIN
    SELECT `State_Name`
           , `State_ab`
           , COUNT(`City`) number_of_cities
           , AVG(`ALand`) Avg_land_area
           , AVG(`AWater`) Avg_water_area
    FROM us_household_income
    WHERE `State_ab` = stateAb
    GROUP BY `State_Name`, `State_ab`;

    SELECT `City`
           , `ALand` Land_area
           , `AWater` Water_area
    FROM us_household_income
    WHERE `State_ab` = stateAb
    ORDER BY `City`;
END $$
DELIMITER ;

-- example for Florida
CALL task10_get_state_report('FL');

-- Task 11: Creating and Using Temporary Tables
-- Question:

-- We need to create a temporary table that stores the top 20 cities by land area for further analysis. Use this temporary table to calculate the average water area of these top 20 cities, and include the city name, state name, land area, and water area in your final report.
DROP TEMPORARY TABLE IF EXISTS task11_20_largest_land_area_cities;
CREATE TEMPORARY TABLE task11_20_largest_land_area_cities
AS SELECT `City`
          , `State_Name`
          , `ALand` Land_area
          , `AWater` Water_area
   FROM us_household_income
   ORDER BY `ALand` DESC
   LIMIT 20;

SELECT `City`
       , `State_Name`
       , Land_area
       , Water_area
FROM task11_20_largest_land_area_cities;


-- Task 12: Complex Multi-Level Subqueries
-- Question:
-- Can you list all states where the average land area of cities is greater than the overall average land area across all cities in the dataset? Use multiple subqueries to calculate the overall average land area and the state-wise average land areas. Include the state name and average land area in your results.

SELECT `State_Name`
       , AVG(`ALand`) AS avg_land_area
FROM us_household_income
GROUP BY `State_Name`
HAVING avg_land_area > (SELECT AVG(ALand) FROM us_household_income);


-- Task 13: Optimizing Indexes for Query Performance
-- Question:
-- Can you analyze the impact of indexing on query performance? Create indexes on the columns State_Name, City, and County, and compare the execution time of a complex query before and after indexing. Provide insights into how indexing improved (or did not improve) the query performance, including execution times and query plans.

SELECT `City`
       , `State_Name`
       , `County`
       , `ALand`
       , `AWater`
FROM us_household_income
WHERE `State_Name` = 'Alabama'
    AND `City` = 'Birmingham'
    AND `County` = 'Autauga County';
-- query before indexing
-- OK, 36 records retrieved in 15.584ms

CREATE INDEX idx_state_name ON us_household_income(`State_Name`);
CREATE INDEX idx_city ON us_household_income(`City`);
CREATE INDEX idx_county ON us_household_income(`County`);

-- query after indexing
-- OK, 36 records retrieved in 1.163ms
-- --> improved


-- Task 14: Recursive Common Table Expressions (CTEs)
-- Question:
-- Can you create a recursive CTE that calculates the cumulative land area for cities within each state, ordered by city name? Include the city name, state name, individual land area, and cumulative land area in your results.

-- set max recursion depth by count rows
SELECT COUNT(*) FROM us_household_income;
SET @@cte_max_recursion_depth = 35000;

-- proceed
WITH RECURSIVE city_ranks AS (
    SELECT `City`
           , `State_Name`
           , `ALand`
           , `ALand` AS cumulative_area
           , ROW_NUMBER() OVER (PARTITION BY `State_Name` ORDER BY `City`) AS rn
    FROM us_household_income
), 
cumulative_land_area AS (
    SELECT `City`
           , `State_Name`
           , `ALand`
           , `ALand` AS cumulative_area
           , rn
    FROM city_ranks
    WHERE rn=1
    UNION ALL
    SELECT cr.`City`
           , cr.`State_Name`
           , cr.`ALand`
           , cla.cumulative_area + cr.`ALand`
           , cr.rn
    FROM cumulative_land_area cla
    JOIN city_ranks cr
        ON cla.rn + 1 = cr.rn
        AND cla.`State_Name` = cr.`State_Name`
)
SELECT `City`
       , `State_Name`
       , `ALand`
       , cumulative_area
FROM cumulative_land_area
ORDER BY `State_Name`, `City`;

-- set max recursion depth to default
SET @@cte_max_recursion_depth = 1000;


-- EDA
-- Task 15: Data Anomalies Detection
-- Question:

-- Can you detect anomalies in the dataset, such as cities with unusually high or low land areas compared to the state average? Use statistical methods like Z-score or standard deviation to identify these anomalies. Include the city name, state name, land area, state average land area, and anomaly score in your results, ordered by the anomaly score in descending order.

-- detect anomalies using Z-score method
SELECT `City`
       , `State_Name`
       , `ALand`
       , AVG(`ALand`) OVER (PARTITION BY `State_Name`) AS state_avg_land_area
       , (`ALand` - AVG(`ALand`) OVER (PARTITION BY `State_Name`)) / STDDEV(`ALand`) OVER (PARTITION BY `State_Name`) AS anomaly_score
FROM us_household_income
ORDER BY anomaly_score DESC;


-- Task 16: Stored Procedures for Complex Calculations
-- Question:

-- Can you write a stored procedure that performs complex calculations, such as predicting future land and water area based on historical trends? The stored procedure should accept parameters for the city and state and return predicted values. Test the stored procedure with different inputs and document the results.

DROP PROCEDURE IF EXISTS task16_predict_area;
DELIMITER $$
CREATE PROCEDURE task16_predict_area(
      IN cityName VARCHAR(255)
      , IN stateName VARCHAR(255))
BEGIN
    
   SELECT cityName AS City
         , stateName AS State_Name
         , (interceptLand + landSlope) * 5 AS predicted_land_area_5_years
         , (interceptWater + waterSlope) * 5 AS predicted_water_area_5_years
   FROM (SELECT AVG(`ALand`) interceptLand
         , AVG(`AWater`) interceptWater
         ,(MAX(`ALand`) - MIN(`ALand`)) / COUNT(*) landSlope
         , (MAX(`AWater`) - MIN(`AWater`)) / COUNT(*) waterSlope
   FROM us_household_income
   WHERE `City` = cityName
      AND `State_Name` = stateName) AS t;
END$$
DELIMITER ;

CALL task16_predict_area('Constableville', 'New York');
-- predicted_land_area_5_years  4808460290.0000
-- predicted_water_area_5_years 18723440.0000
CALL task16_predict_area('New Castle', 'Virginia');
-- predicted_land_area_5_years  4267453215.0000
-- predicted_water_area_5_years 13988620.0000
CALL task16_predict_area('Bridgeville', 'California');
-- predicted_land_area_5_years  10762802900.0000
-- predicted_water_area_5_years 22389335.0000


-- Task 17: Implementing Triggers for Data Integrity
-- Question:
-- Can you write a trigger that automatically updates a summary table whenever new data is inserted, updated, or deleted in the main dataset? The summary table should include aggregated information such as total land area and water area by state. Test the trigger to ensure it correctly updates the summary table in response to changes in the main dataset.
DROP TABLE IF EXISTS us_state_summary;
CREATE TABLE us_state_summary (
   `State_Name` VARCHAR(20),
   total_land_area DOUBLE DEFAULT 0,
   total_water_area DOUBLE DEFAULT 0,
   CONSTRAINT pk_state_summary PRIMARY KEY (`State_Name`)
);

DROP PROCEDURE IF EXISTS task17_upsert_state_summary;
DELIMITER $$
CREATE PROCEDURE task17_upsert_state_summary(
      IN stateName VARCHAR(20)
      , IN varALand BIGINT
      , IN varAWater BIGINT
)
BEGIN
   INSERT INTO us_state_summary(`State_Name`, `total_land_area`, `total_water_area`)
   VALUES (stateName, varALand, varAWater)
   ON DUPLICATE KEY UPDATE
      `total_land_area` = varALand,
      `total_water_area` = varAWater;
END$$
DELIMITER ;

DROP TRIGGER IF EXISTS task17_after_insert;
DROP TRIGGER IF EXISTS task17_after_update;
DROP TRIGGER IF EXISTS task17_after_delete;
DELIMITER $$
CREATE TRIGGER task17_after_insert
AFTER INSERT ON us_household_income
FOR EACH ROW
BEGIN
   CALL task17_upsert_state_summary(
      NEW.`State_Name`
      , NEW.ALand
      , NEW.AWater
   );
END$$

CREATE TRIGGER task17_after_update
AFTER UPDATE ON us_household_income
FOR EACH ROW
BEGIN
   IF OLD.`State_Name` = NEW.`State_Name` THEN
      CALL task17_upsert_state_summary(
         NEW.`State_Name`
         , NEW.ALand - OLD.ALand
         , NEW.AWater - OLD.AWater
      );
   ELSE
      CALL task17_upsert_state_summary(
         OLD.`State_Name`
         , - OLD.ALand
         , - OLD.AWater
      );
      CALL task17_upsert_state_summary(
         NEW.`State_Name`
         , NEW.ALand
         , NEW.AWater
      );
   END IF;
END$$

CREATE TRIGGER task17_after_delete
AFTER DELETE ON us_household_income
FOR EACH ROW
BEGIN
   CALL task17_upsert_state_summary(
      OLD.`State_Name`
      , - OLD.ALand
      , - OLD.AWater
   );
END$$

DELIMITER ;

-- test insert
INSERT INTO US_Household_Income(id,State_Code,State_Name,State_ab,County,City,Place,Type,Primary_,Zip_Code,Area_Code,ALand,AWater,Lat,Lon) VALUES
 (35000,9999,'New_State','ZZ','Autauga County','Elmore','Autaugaville','Track','Track',36025,'334',8020338,60048,32.4473511,-86.4768097)
 , (35000,9999,'New_State','ZZ','Autauga County','Elmore','Autaugaville','Track','Track',36025,'334',8020341,60012,32.4473511,-86.4768097);

 SELECT * FROM us_state_summary;
--  total_land_area: 16040679
--  total_water_area: 120060

-- test update
UPDATE us_household_income
SET ALand=8990000, AWater=65000
WHERE State_Name = 'New_State' AND ALand=8020338;
SELECT * FROM us_state_summary;
--  total_land_area: 17010341
--  total_water_area: 125012

-- test delete
DELETE FROM us_household_income
WHERE State_Name = 'New_State';

SELECT * FROM us_state_summary;
--  total_land_area: 0
--  total_water_area: 0




-- Task 18: Advanced Data Encryption and Security
-- Question:

-- We need to implement data encryption and ensure secure access to sensitive information in the dataset. Use MySQL encryption functions to encrypt columns such as Zip_Code and Area_Code. Demonstrate how to decrypt the data for authorized users and discuss the implications for data security.

-- get key from SELECT UUID();
SET @app_secret_key = '3b48b9e8-2213-11ef-a766-e073e7d08178';

DROP FUNCTION IF EXISTS encrypted_component;
CREATE FUNCTION encrypted_component(
   input VARCHAR(255)
) RETURNS VARBINARY(255)
DETERMINISTIC
RETURN AES_ENCRYPT(input, @app_secret_key);

DROP FUNCTION IF EXISTS decrypted_component;
CREATE FUNCTION decrypted_component(
   input VARBINARY(255)
) RETURNS VARCHAR(255)
DETERMINISTIC
RETURN AES_DECRYPT(input, @app_secret_key);

SELECT decrypted_component(encrypted_zip_code) zip_code
   , decrypted_component(encrypted_area_code) area_code
FROM
   (SELECT encrypted_component(`Zip_Code`) encrypted_zip_code
      , encrypted_component(`Area_Code`) encrypted_area_code
   FROM us_household_income) AS encrypted_codes;


-- Task 19: Geospatial Analysis
-- Question:

-- We need to identify cities that fall within a specified radius from a given point (latitude and longitude). Include calculations to determine the distance between the given point and each city. Return the city name, state name, county, and calculated distance.
SET @latitude = 30;
SET @longitude = -66;
SELECT `City`
       , `State_Name`
       , `County`
       , ST_Distance_Sphere(point(@longitude, @latitude)
                  , point(`Lon`, `Lat`)) `distance(meter)`
FROM us_household_income;


-- Task 20: Analyzing Correlations
-- Question:

-- Can you calculate the correlation between land area (ALand) and water area (AWater) for each state? Use statistical functions to determine the strength of the correlation. Include the state name and the correlation coefficient in your results.
SELECT `State_Name`
       , (numbers * total_mul_area - total_land_area * total_water_area) 
         / SQRT(numbers * total_mul_land_area - total_land_area * total_land_area)
         / SQRT(numbers * total_mul_water_area - total_water_area * total_water_area) AS corr
FROM (SELECT `State_Name`
             , COUNT(*) numbers
             , SUM(CAST(ALand AS DOUBLE) * CAST(AWater AS DOUBLE)) total_mul_area
             , SUM(CAST(ALand AS DOUBLE) * CAST(ALand AS DOUBLE)) total_mul_land_area
             , SUM(CAST(AWater AS DOUBLE) * CAST(AWater AS DOUBLE)) total_mul_water_area
             , SUM(ALand) total_land_area
             , SUM(AWater) total_water_area
      FROM us_household_income
      GROUP BY `State_Name`) _cals;



-- Task 21: Hotspot Detection
-- Question:

-- Can you identify “hotspots” where the combination of land area and water area significantly deviates from the norm? Use statistical methods such as Z-scores or clustering to detect these hotspots. Include city name, state name, land area, water area, and the deviation score in your report.

SELECT `City`
       , `State_Name`
       , `ALand` land_area
       , `AWater` water_area
       , ((`ALand` - AVG(`ALand`) OVER ()) / STDDEV(`ALand`) OVER ()) AS z_score_land
       , ((`AWater` - AVG(`AWater`) OVER ()) / STDDEV(`AWater`) OVER ()) AS z_score_water
FROM us_household_income
ORDER BY GREATEST(ABS(z_score_land), ABS(z_score_water)) DESC;

-- Task 22: Resource Allocation Optimization
-- Question:

-- We need to optimize the allocation of resources (e.g., funding) based on the land and water area of each city. Create a model to distribute resources in a way that maximizes efficiency and equity. Include the city name, state name, land area, water area, and allocated resources in your results.

-- The weights (0.5 for land and 0.5 for water) are chosen for simplicity
SELECT `City`
       , `State_Name`
       , `ALand` land_area
       , `AWater` water_area
       , (`ALand` + `AWater`) * 0.5 AS allocated_resources
FROM us_household_income
ORDER BY allocated_resources DESC;