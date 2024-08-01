Use Project;

-- Task 1 Basic Descriptive Statistics
-- Calculate average, minimum, and maximum Lifeexpectancy for each country
SELECT Country,
       ROUND(AVG(Lifeexpectancy),1) AS avg_lifeexpectancy,
       MIN(Lifeexpectancy) AS min_lifeexpectancy,
       MAX(Lifeexpectancy) AS max_lifeexpectancy
FROM worldlifexpectancy
GROUP BY Country;

-- Calculate median Lifeexpectancy for each country using a subquery approach
SELECT Country, 
       Lifeexpectancy AS median_lifeexpectancy
FROM (
    SELECT Country, 
           Lifeexpectancy, 
           ROW_NUMBER() OVER (PARTITION BY Country ORDER BY Lifeexpectancy) AS row_num,
           COUNT(*) OVER (PARTITION BY Country) AS total_count
    FROM worldlifexpectancy
) AS subquery
WHERE row_num = FLOOR((total_count + 1) / 2);

-- Task 2 Trend Analysis
SELECT Year, Lifeexpectancy
FROM worldlifexpectancy
WHERE Country = 'Afghanistan'
ORDER BY Year;


-- Task 3 Comparative Analysis
SELECT Status, ROUND(AVG(Lifeexpectancy),1) AS avg_lifeexpectancy
FROM worldlifexpectancy
WHERE Year = (SELECT MAX(Year) FROM worldlifexpectancy)
GROUP BY Status;

-- Task 4 Mortality Analysis
SELECT
    (COUNT(*) * SUM(AdultMortality * Lifeexpectancy) - SUM(AdultMortality) * SUM(Lifeexpectancy)) /
    SQRT(
        (COUNT(*) * SUM(AdultMortality * AdultMortality) - SUM(AdultMortality) * SUM(AdultMortality)) *
        (COUNT(*) * SUM(Lifeexpectancy * Lifeexpectancy) - SUM(Lifeexpectancy) * SUM(Lifeexpectancy))
    ) AS correlation_coefficient
FROM worldlifexpectancy;
# The result of -0.6964 suggests a strong negative correlation between AdultMortality and Lifeexpectancy. This means that countries with higher adult mortality rates tend to have significantly lower life expectancies.

-- Task 5 Impact of GDP
SELECT CASE 
         WHEN GDP < 1000 THEN 'Low'
         WHEN GDP BETWEEN 1000 AND 10000 THEN 'Medium'
         ELSE 'High'
       END AS gdp_range,
       ROUND(AVG(Lifeexpectancy),1) AS avg_lifeexpectancy
FROM worldlifexpectancy
GROUP BY gdp_range;

-- Task 6 Disease Impact
SELECT 'High Measles' AS category, ROUND(AVG(Lifeexpectancy),1) AS avg_lifeexpectancy
FROM worldlifexpectancy
WHERE Measles > (SELECT AVG(Measles) FROM worldlifexpectancy)
UNION
SELECT 'Low Measles', ROUND(AVG(Lifeexpectancy),1)
FROM worldlifexpectancy
WHERE Measles <= (SELECT AVG(Measles) FROM worldlifexpectancy);

SELECT 'High Polio' AS category, ROUND(AVG(Lifeexpectancy),1) AS avg_lifeexpectancy
FROM worldlifexpectancy
WHERE Polio > (SELECT AVG(Polio) FROM worldlifexpectancy)
UNION
SELECT 'Low Polio', ROUND(AVG(Lifeexpectancy),1)
FROM worldlifexpectancy
WHERE Polio <= (SELECT AVG(Polio) FROM worldlifexpectancy);

-- Task 7 Schooling and Health
SELECT Country, Schooling, Lifeexpectancy
FROM worldlifexpectancy
ORDER BY Schooling DESC
LIMIT 10;

SELECT Country, Schooling, Lifeexpectancy
FROM worldlifexpectancy
WHERE Schooling <> 0
ORDER BY Schooling ASC
LIMIT 10;

-- Task 8 BMI Trends
SELECT Country, Year, AVG(BMI) AS avg_bmi
FROM worldlifexpectancy
WHERE Country = 'Viet nam'
GROUP BY Year
ORDER BY Year;

SELECT Country, Year, AVG(BMI) AS avg_bmi
FROM worldlifexpectancy
GROUP BY Country, Year
ORDER BY Country, Year;


-- Task 9 Infant Mortality
SET @row_number := 0;
SET @total_rows := (SELECT COUNT(*) FROM worldlifexpectancy);

-- Step 1: Assign row numbers to each record ordered by Lifeexpectancy
SELECT Country, Year, Lifeexpectancy,
       @row_number := @row_number + 1 AS row_num
FROM worldlifexpectancy
ORDER BY Lifeexpectancy;

-- Step 2: Calculate the positions for 10th and 90th percentiles
SET @p10 := FLOOR(0.1 * @total_rows);
SET @p90 := CEIL(0.9 * @total_rows);

-- Step 3: Get the 10th and 90th percentile values
SELECT MIN(Lifeexpectancy) AS p10_value
FROM (
    SELECT Country, Year, Lifeexpectancy,
           @row_number := @row_number + 1 AS row_num
    FROM worldlifexpectancy
    ORDER BY Lifeexpectancy
) AS ranked_life
WHERE row_num >= @p10;

SELECT MAX(Lifeexpectancy) AS p90_value
FROM (
    SELECT Country, Year, Lifeexpectancy,
           @row_number := @row_number + 1 AS row_num
    FROM worldlifexpectancy
    ORDER BY Lifeexpectancy
) AS ranked_life
WHERE row_num <= @p90;


-- Replace `p10_value` and `p90_value` with the actual 10th and 90th percentile values obtained earlier
SET @p10_value := 60; -- Example value, replace with actual value
SET @p90_value := 80; -- Example value, replace with actual value

-- Identify countries with the highest and lowest life expectancies
SELECT Country, AVG(infantdeaths) AS avg_infantdeaths, AVG(`under-fivedeaths`) AS avg_underfivedeaths
FROM worldlifexpectancy
WHERE Lifeexpectancy >= @p90_value
GROUP BY Country;

SELECT Country, AVG(infantdeaths) AS avg_infantdeaths, AVG(`under-fivedeaths`) AS avg_underfivedeaths
FROM worldlifexpectancy
WHERE Lifeexpectancy <= @p10_value
GROUP BY Country;

-- Calculate averages for high life expectancy countries
SELECT 'Highest Life Expectancy' AS category, 
       AVG(avg_infantdeaths) AS avg_infantdeaths, 
       AVG(avg_underfivedeaths) AS avg_underfivedeaths
FROM (
    SELECT Country, AVG(infantdeaths) AS avg_infantdeaths, AVG(`under-fivedeaths`) AS avg_underfivedeaths
    FROM worldlifexpectancy
    WHERE Lifeexpectancy >= @p90_value
    GROUP BY Country
) AS high_life_expectancy_countries;

-- Calculate averages for low life expectancy countries
SELECT 'Lowest Life Expectancy' AS category, 
       AVG(avg_infantdeaths) AS avg_infantdeaths, 
       AVG(avg_underfivedeaths) AS avg_underfivedeaths
FROM (
    SELECT Country, AVG(infantdeaths) AS avg_infantdeaths, AVG(`under-fivedeaths`) AS avg_underfivedeaths
    FROM worldlifexpectancy
    WHERE Lifeexpectancy <= @p10_value
    GROUP BY Country
) AS low_life_expectancy_countries;


-- Task 10 Rolling Average of Adult Mortality
SELECT Country, Year, 
       ROUND(AVG(AdultMortality) OVER (PARTITION BY Country ORDER BY Year ROWS BETWEEN 4 PRECEDING AND CURRENT ROW), 1) AS rolling_avg_adultmortality
FROM worldlifexpectancy
ORDER BY Country, Year;



-- Task 11 Impact of Healthcare Expenditure
SELECT
    (COUNT(*) * SUM(percentageexpenditure * Lifeexpectancy) - SUM(percentageexpenditure) * SUM(Lifeexpectancy)) /
    SQRT(
        (COUNT(*) * SUM(percentageexpenditure * percentageexpenditure) - SUM(percentageexpenditure) * SUM(percentageexpenditure)) *
        (COUNT(*) * SUM(Lifeexpectancy * Lifeexpectancy) - SUM(Lifeexpectancy) * SUM(Lifeexpectancy))
    ) AS correlation_coefficient
FROM worldlifexpectancy;
-- A Pearson correlation coefficient of approximately 0.382 suggests a moderate positive relationship between healthcare expenditure (as a percentage of GDP) and life expectancy. This means that, generally, countries that spend a higher percentage of their GDP on healthcare tend to have higher life expectancies. However, the relationship is not very strong, indicating that other factors also play a significant role in determining life expectancy.

-- Task 12 BMI and Health Indicators
-- Correlation Between BMI and Lifeexpectancy
SELECT
    (COUNT(*) * SUM(BMI * Lifeexpectancy) - SUM(BMI) * SUM(Lifeexpectancy)) /
    SQRT(
        (COUNT(*) * SUM(BMI * BMI) - SUM(BMI) * SUM(BMI)) *
        (COUNT(*) * SUM(Lifeexpectancy * Lifeexpectancy) - SUM(Lifeexpectancy) * SUM(Lifeexpectancy))
    ) AS correlation_coefficient
FROM worldlifexpectancy;

-- Correlation Between BMI and AdultMortality
SELECT
    (COUNT(*) * SUM(BMI * AdultMortality) - SUM(BMI) * SUM(AdultMortality)) /
    SQRT(
        (COUNT(*) * SUM(BMI * BMI) - SUM(BMI) * SUM(BMI)) *
        (COUNT(*) * SUM(AdultMortality * AdultMortality) - SUM(AdultMortality) * SUM(AdultMortality))
    ) AS correlation_coefficient
FROM worldlifexpectancy;



-- Task 13 GDP and Health Outcomes
SELECT CASE 
         WHEN GDP < 1000 THEN 'Low'
         WHEN GDP BETWEEN 1000 AND 10000 THEN 'Medium'
         ELSE 'High'
       END AS gdp_range,
       ROUND(AVG(Lifeexpectancy),1) AS avg_lifeexpectancy,
       ROUND(AVG(AdultMortality),1) AS avg_adultmortality,
       ROUND(AVG(infantdeaths),1) AS avg_infantdeaths
FROM worldlifexpectancy
GROUP BY gdp_range;

-- Task 14 Subgroup Analysis of Life Expectancy
-- Create table continent
CREATE TABLE Continent (
  Country VARCHAR(60),
  Continent VARCHAR(20));
 
INSERT INTO Continent (Country,Continent)
VALUES
('Afghanistan','Asia'), ('Albania','Europe'), ('Algeria','Africa'), ('Angola','Africa'),
('Antigua and Barbuda','North America'), ('Argentina','South America'), ('Armenia','Europe'),
('Australia','Oceania'), ('Austria','Europe'), ('Azerbaijan','Europe'),
('Bahamas','North America'), ('Bahrain','Asia'), ('Bangladesh','Asia'),
('Barbados','North America'), ('Belarus','Europe'), ('Belgium','Europe'),
('Belize','North America'), ('Benin','Africa'), ('Bhutan','Asia'),
('Bolivia (Plurinational State of)','South America'), ('Bosnia and Herzegovina','Europe'),
('Botswana','Africa'), ('Brazil','South America'), ('Brunei Darussalam','Asia'),
('Bulgaria','Europe'), ('Burkina Faso','Africa'), ('Burundi','Africa'),
('Cabo Verde','Africa'), ('Cambodia','Asia'), ('Cameroon','Africa'),
('Canada','North America'), ('Central African Republic','Africa'), ('Chad','Africa'),
('Chile','South America'), ('China','Asia'), ('Colombia','South America'),
('Comoros','Africa'), ('Congo','Africa'), ('Costa Rica','North America'),
('Côte d''Ivoire','Africa'), ('Croatia','Europe'),('Cuba','North America'),
('Cyprus','Europe'),('Czechia','Europe'),('Democratic People''s Republic of Korea','Asia'),
('Democratic Republic of the Congo','Africa'),('Denmark','Europe'),('Djibouti','Africa'),
('Dominican Republic','North America'),('Ecuador','South America'),('Egypt','Africa'),
('El Salvador','North America'),('Equatorial Guinea','Africa'),('Eritrea','Africa'),
('Estonia','Europe'),('Ethiopia','Africa'),('Fiji','Oceania'),('Finland','Europe'),
('France','Europe'),('Gabon','Africa'),('Gambia','Africa'),('Georgia','Europe'),
('Germany','Europe'),('Ghana','Africa'),('Greece','Europe'),('Grenada','North America'),
('Guatemala','North America'),('Guinea','Africa'),('Guinea-Bissau','Africa'),
('Guyana','South America'),('Haiti','North America'),('Honduras','North America'),
('Hungary','Europe'),('Iceland','Europe'),('India','Asia'),('Indonesia','Asia'),
('Iran (Islamic Republic of)','Asia'),('Iraq','Asia'),('Ireland','Europe'),
('Israel','Asia'),('Italy','Europe'),('Jamaica','North America'),('Japan','Asia'),
('Jordan','Asia'),('Kazakhstan','Asia'),('Kenya','Africa'),('Kiribati','Oceania'),
('Kuwait','Asia'),('Kyrgyzstan','Asia'),('Lao People''s Democratic Republic','Asia'),
('Latvia','Europe'),('Lebanon','Asia'),('Lesotho','Africa'),('Liberia','Africa'),
('Libya','Africa'),('Lithuania','Europe'),('Luxembourg','Europe'),('Madagascar','Africa'),
('Malawi','Africa'),('Malaysia','Asia'),('Maldives','Asia'),('Mali','Africa'),
('Malta','Europe'),('Mauritania','Africa'),('Mauritius','Africa'),('Mexico','North America'),
('Micronesia (Federated States of)','Oceania'),('Mongolia','Asia'),('Montenegro','Europe'),
('Morocco','Africa'),('Mozambique','Africa'),('Myanmar','Asia'),('Namibia','Africa'),
('Nepal','Asia'),('Netherlands','Europe'),('New Zealand','Oceania'),('Nicaragua','North America'),
('Niger','Africa'),('Nigeria','Africa'),('Norway','Europe'),('Oman','Asia'),
('Pakistan','Asia'),('Panama','North America'),('Papua New Guinea','Oceania'),
('Paraguay','South America'),('Peru','South America'),('Philippines','Asia'),('Poland','Europe'),
('Portugal','Europe'),('Qatar','Asia'),('Republic of Korea','Asia'),('Republic of Moldova','Europe'),
('Romania','Europe'),('Russian Federation','Asia'),('Rwanda','Africa'),('Saint Lucia','North America'),
('Saint Vincent and the Grenadines','North America'),('Samoa','Oceania'),('Sao Tome and Principe','Africa'),
('Saudi Arabia','Asia'),('Senegal','Africa'),('Serbia','Europe'),('Seychelles','Africa'),
('Sierra Leone','Africa'),('Singapore','Asia'),('Slovakia','Europe'),('Slovenia','Europe'),
('Solomon Islands','Oceania'),('Somalia','Africa'),('South Africa','Africa'),('South Sudan','Africa'),
('Spain','Europe'),('Sri Lanka','Asia'),('Sudan','Africa'),('Suriname','South America'),
('Swaziland','Africa'),('Sweden','Europe'),('Switzerland','Europe'),('Syrian Arab Republic','Asia'),
('Tajikistan','Asia'),('Thailand','Asia'),('The former Yugoslav republic of Macedonia','Europe'),
('Timor-Leste','Asia'),('Togo','Africa'),('Tonga','Oceania'),('Trinidad and Tobago','North America'),
('Tunisia','Africa'),('Turkey','Europe'),('Turkmenistan','Asia'),('Uganda','Africa'),
('Ukraine','Europe'),('United Arab Emirates','Asia'),('United Kingdom of Great Britain and Northern Ireland','Europe'),
('United Republic of Tanzania','Africa'),('United States of America','North America'),('Uruguay','South America'),
('Uzbekistan','Asia'),('Vanuatu','Oceania'),('Venezuela (Bolivarian Republic of)','South America'),
('Viet Nam','Asia'),('Yemen','Asia'),('Zambia','Africa'),('Zimbabwe','Africa');

-- Query to find the average Lifeexpectancy for specific subgroups
SELECT Continent, ROUND(AVG(Lifeexpectancy),1)
FROM worldlifexpectancy w
JOIN continent c ON w.Country = c.Country
GROUP BY Continent;