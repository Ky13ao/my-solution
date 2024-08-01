-- EDA worldlifexpectancy
-- Here are 14 tasks to practice your MySQL skills and perform exploratory data analysis (EDA) to extract meaningful insights:


-- 1. **Basic Descriptive Statistics**: 
--    - Query to get the avg, mean, median, minimum, and maximum of the `Lifeexpectancy` for each `Country`.
WITH MedianCalc AS 
   (SELECT `Country`, AVG(wle.val) median
    FROM (SELECT `Country`, 
                 `Lifeexpectancy` val, 
                 ROW_NUMBER() OVER (PARTITION BY `Lifeexpectancy` ORDER BY `Lifeexpectancy`) idx,
                 COUNT(*) OVER (PARTITION BY `Country`) total_count
          FROM `worldlifexpectancy`) AS wle
    WHERE idx >= FLOOR((total_count +1)/2) 
        AND idx <= CEIL((total_count +1)/2)
    GROUP BY `Country`) 
SELECT w.`Country`,
       AVG(w.`Lifeexpectancy`) mean,
       mc.median,
       MIN(w.`Lifeexpectancy`) min,
       MAX(w.`Lifeexpectancy`) max
FROM `worldlifexpectancy` w
JOIN MedianCalc mc ON mc.`Country` = w.`Country`
GROUP BY w.`Country`;


-- 2. **Trend Analysis**:
--    - Query to find the trend of `Lifeexpectancy` over the years for a specific country (e.g., Afghanistan). 
SELECT `Year`, `Lifeexpectancy`
FROM `worldlifexpectancy`
WHERE `Country` = 'Afghanistan'
ORDER BY `Year`;


-- 3. **Comparative Analysis**:
--    - Query to compare the average `Lifeexpectancy` between `Developed` and `Developing` countries for the latest available year.
SELECT `Year`
       , AVG(IF(`Status`='Developed', `Lifeexpectancy`, NULL)) AVG_Developed
       , AVG(IF(`Status`='Developing', `Lifeexpectancy`, NULL)) AVG_Developing
FROM `worldlifexpectancy`
GROUP BY `Year`
ORDER BY `Year` DESC
LIMIT 1;


-- 4. **Mortality Analysis**:
--    - Query to calculate the correlation between `AdultMortality` and `Lifeexpectancy` for all countries. 
SELECT
    (COUNT(*) * SUM(`AdultMortality` * `Lifeexpectancy`) - SUM(`AdultMortality`) * SUM(`Lifeexpectancy`)) /
    SQRT(
        (COUNT(*) * SUM(`AdultMortality` * `AdultMortality`) - SUM(`AdultMortality`) * SUM(`AdultMortality`)) *
        (COUNT(*) * SUM(`Lifeexpectancy` * `Lifeexpectancy`) - SUM(`Lifeexpectancy`) * SUM(`Lifeexpectancy`))
    ) correlation_coefficient
FROM `worldlifexpectancy`;


-- 5. **Impact of GDP**:
--    - Query to find the average `Lifeexpectancy` of countries grouped by their GDP ranges (e.g., low, medium, high which is you decided).
SELECT CASE 
         WHEN `GDP` < 1000 THEN 'Low'
         WHEN `GDP` < 10000 THEN 'Medium'
         ELSE 'High'
       END AS gdp_range,
       ROUND(AVG(`Lifeexpectancy`),1) AS avg_lifeexpectancy
FROM `worldlifexpectancy`
GROUP BY gdp_range;


-- 6. **Disease Impact**:
--    - Query to analyze the impact of `Measles` and `Polio` on `Lifeexpectancy`. Calculate average life expectancy for countries with high and low incidence rates of these diseases.
SELECT 'High Measles' category
    , ROUND(AVG(`Lifeexpectancy`),1) avg_lifeexpectancy
FROM `worldlifexpectancy`
WHERE `Measles` > (SELECT AVG(`Measles`) FROM `worldlifexpectancy`)
UNION
SELECT 'Low Measles', ROUND(AVG(Lifeexpectancy),1)
FROM `worldlifexpectancy`
WHERE `Measles` <= (SELECT AVG(`Measles`) FROM `worldlifexpectancy`);

SELECT 'High Polio' category
    , ROUND(AVG(`Lifeexpectancy`),1) avg_lifeexpectancy
FROM `worldlifexpectancy`
WHERE `Polio` > (SELECT AVG(`Polio`) FROM `worldlifexpectancy`)
UNION
SELECT 'Low Polio', ROUND(AVG(Lifeexpectancy),1)
FROM `worldlifexpectancy`
WHERE `Polio` <= (SELECT AVG(`Polio`) FROM `worldlifexpectancy`);


-- 7. **Schooling and Health**:
--    - Query to determine the relationship between `Schooling` and `Lifeexpectancy`. Find countries with the highest and lowest schooling and their respective life expectancies.
SELECT `Country`
       , `Schooling`
       , `Lifeexpectancy`
       , '10 highest schooling' Category
FROM `worldlifexpectancy`
ORDER BY `Schooling` DESC
LIMIT 10;

SELECT `Country`
       , `Schooling`
       , `Lifeexpectancy`
       , '10 lowest schooling' Category
FROM `worldlifexpectancy`
WHERE `Schooling` <> 0
ORDER BY `Schooling` ASC
LIMIT 10;


-- 8. **BMI Trends**:
--    - Query to find the average BMI trend over the years for a particular country. 
SELECT `Country`
        , `Year`
        , AVG(`BMI`) avg_bmi
FROM `worldlifexpectancy`
WHERE `Country` = 'Viet Nam'
GROUP BY `Year`
ORDER BY `Year`;


-- 9. **Infant Mortality**:
--    - Query to find the average number of `infantdeaths` and `under-fivedeaths` for countries with the highest and lowest life expectancies.


-- 10. **Rolling Average of Adult Mortality**:
--     - Query to calculate the rolling average of `AdultMortality` over a 5-year window for each country. This will help in understanding the trend and smoothing out short-term fluctuations.
SELECT `Country`
       , `Year`
       , ROUND(AVG(`AdultMortality`) OVER (PARTITION BY `Country` ORDER BY `Year` ROWS BETWEEN 4 PRECEDING AND CURRENT ROW), 1) AS rolling_avg_adultmortality
FROM `worldlifexpectancy`
ORDER BY `Country`, `Year`;


-- 11. **Impact of Healthcare Expenditure**:
--     - Query to find the correlation between `percentageexpenditure` (healthcare expenditure) and `Lifeexpectancy`. Higher healthcare spending might correlate with higher life expectancy.
SELECT
    (COUNT(*) * SUM(`percentageexpenditure` * `Lifeexpectancy`) - SUM(`percentageexpenditure`) * SUM(`Lifeexpectancy`)) /
    SQRT(
        (COUNT(*) * SUM(`percentageexpenditure` * `percentageexpenditure`) - SUM(`percentageexpenditure`) * SUM(`percentageexpenditure`)) *
        (COUNT(*) * SUM(`Lifeexpectancy` * `Lifeexpectancy`) - SUM(`Lifeexpectancy`) * SUM(`Lifeexpectancy`))
    ) AS correlation_coefficient
FROM `worldlifexpectancy`;


-- 12. **BMI and Health Indicators**:
--     - Query to find the correlation between `BMI` and other health indicators like `Lifeexpectancy` and `AdultMortality`. Analyze the impact of BMI on overall health.
-- Correlation Between BMI and Lifeexpectancy
SELECT
    (COUNT(*) * SUM(`BMI` * `Lifeexpectancy`) - SUM(`BMI`) * SUM(`Lifeexpectancy`)) /
    SQRT(
        (COUNT(*) * SUM(`BMI` * `BMI`) - SUM(`BMI`) * SUM(`BMI`)) *
        (COUNT(*) * SUM(`Lifeexpectancy` * `Lifeexpectancy`) - SUM(`Lifeexpectancy`) * SUM(`Lifeexpectancy`))
    ) AS correlation_coefficient
FROM `worldlifexpectancy`;

-- Correlation Between BMI and AdultMortality
SELECT
    (COUNT(*) * SUM(`BMI` * `AdultMortality`) - SUM(`BMI`) * SUM(`AdultMortality`)) /
    SQRT(
        (COUNT(*) * SUM(`BMI` * `BMI`) - SUM(`BMI`) * SUM(`BMI`)) *
        (COUNT(*) * SUM(`AdultMortality` * `AdultMortality`) - SUM(`AdultMortality`) * SUM(`AdultMortality`))
    ) AS correlation_coefficient
FROM `worldlifexpectancy`;


-- 13. **GDP and Health Outcomes**:
--     - Query to analyze how `GDP` influences health outcomes such as `Lifeexpectancy`, `AdultMortality`, and `infantdeaths`. Compare high GDP and low GDP countries.
SELECT CASE 
         WHEN `GDP` < 1000 THEN 'Low'
         WHEN `GDP` < 10000 THEN 'Medium'
         ELSE 'High'
       END AS gdp_range,
       ROUND(AVG(`Lifeexpectancy`),1) AS avg_lifeexpectancy,
       ROUND(AVG(`AdultMortality`),1) AS avg_adultmortality,
       ROUND(AVG(`infantdeaths`),1) AS avg_infantdeaths
FROM `worldlifexpectancy`
GROUP BY gdp_range;


-- 14. **Subgroup Analysis of Life Expectancy**:
--     - Query to find the average `Lifeexpectancy` for specific subgroups, such as countries in different continents or regions. This can help in identifying regional health disparities.

-- These tasks will help you apply various SQL concepts and techniques you have learned, including grouping, joins, subqueries, window functions, and data cleaning techniques, to gain valuable insights from your dataset.