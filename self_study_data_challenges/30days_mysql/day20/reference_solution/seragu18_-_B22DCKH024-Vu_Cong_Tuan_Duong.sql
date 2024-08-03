USE day20;
select *
from day20.worldlifexpectancy
;

--  search for duplicates
select country, year, count(concat(country, year)) as occurances
FROM day20.worldlifexpectancy
GROUP BY Country, Year
HAVING COUNT(CONCAT(Country, Year)) > 1
;

-- remove duplicates
select *
from (
	select row_id,
    concat(country, year),
    row_number() over(partition by concat(country, year) order by concat(country, year)) as row_num
    from day20.worldlifexpectancy
) as row_table
where row_num  > 1
;

--  delete
delete from day20.worldlifexpectancy
where row_id in(
	select row_id
from (
	select row_id,
    concat(country, year),
    row_number() over(partition by concat(country, year) order by concat(country, year)) as row_num
    from day20.worldlifexpectancy
) as row_table
where row_num  > 1
)
;

--  missing values
select *
from day20.worldlifexpectancy
where status = ''
;

--  check status

select t1.country, t1.status, t2.status
from day20.worldlifexpectancy t1
JOIN day20.worldlifexpectancy t2
     ON t1.Country = t2.Country
where t1.status = '' and t2.status != '' and t2.status = 'Developing'
;

update day20.worldlifexpectancy t1
JOIN day20.worldlifexpectancy t2
     ON t1.Country = t2.Country
set t1.status = 'Developing'
where t1.status = '' and t2.status != '' and t2.status = 'Developing'
;

--  only america left
update day20.worldlifexpectancy t1
JOIN day20.worldlifexpectancy t2
     ON t1.Country = t2.Country
set t1.status = 'Developed'
where t1.status = '' and t2.status != '' and t2.status = 'Developed'
;

--  life expectancy have missing values
select *
from day20.worldlifexpectancy
where Lifeexpectancy = ''
;


select t1.country, t1.year, t1.lifeexpectancy,
t2.country, t2.year, t2.lifeexpectancy,
t3.country, t3.year, t3.lifeexpectancy,
round((t2.lifeexpectancy + t3.lifeexpectancy) / 2, 1) as new_lifeexpectancy
from day20.worldlifexpectancy t1
join day20.worldlifexpectancy t2
	on t1.country = t2.country
    and t1.year = t2.year - 1
join day20.worldlifexpectancy t3
	on t1.country = t3.country
    and t1.year = t3.year + 1
where t1.Lifeexpectancy = ''
;
		
-- update
update day20.worldlifexpectancy t1
join day20.worldlifexpectancy t2
	on t1.country = t2.country
    and t1.year = t2.year - 1
join day20.worldlifexpectancy t3
	on t1.country = t3.country
    and t1.year = t3.year + 1
set t1.lifeexpectancy = round((t2.lifeexpectancy + t3.lifeexpectancy) / 2, 1)
where t1.Lifeexpectancy = ''
;

-- outliers

-- Identify outliers in Lifeexpectancy
SELECT *
FROM day20.worldlifexpectancy
WHERE Lifeexpectancy > (SELECT AVG(Lifeexpectancy) + 3 * STD(Lifeexpectancy) FROM day20.worldlifexpectancy)
   OR Lifeexpectancy < (SELECT AVG(Lifeexpectancy) - 3 * STD(Lifeexpectancy) FROM day20.worldlifexpectancy);

-- Replace outliers with average values
-- For Lifeexpectancy
CREATE TEMPORARY TABLE IF NOT EXISTS temp1 AS (
    SELECT AVG(Lifeexpectancy) as avgLifeExpectancy,
           AVG(Lifeexpectancy) + 3 * STD(Lifeexpectancy) as upperLimit,
           AVG(Lifeexpectancy) - 3 * STD(Lifeexpectancy) as lowerLimit
    FROM day20.worldlifexpectancy
);

UPDATE day20.worldlifexpectancy, temp1
SET day20.worldlifexpectancy.Lifeexpectancy = temp1.avgLifeExpectancy
WHERE day20.worldlifexpectancy.Lifeexpectancy > temp1.upperLimit
   OR day20.worldlifexpectancy.Lifeexpectancy < temp1.lowerLimit;

DROP TEMPORARY TABLE IF EXISTS temp1;

-- For AdultMortality
CREATE TEMPORARY TABLE IF NOT EXISTS temp2 AS (
    SELECT AVG(AdultMortality) as avgAdultMortality,
           AVG(AdultMortality) + 3 * STD(AdultMortality) as upperLimit,
           AVG(AdultMortality) - 3 * STD(AdultMortality) as lowerLimit
    FROM day20.worldlifexpectancy
);

UPDATE day20.worldlifexpectancy, temp2
SET day20.worldlifexpectancy.AdultMortality = temp2.avgAdultMortality
WHERE day20.worldlifexpectancy.AdultMortality > temp2.upperLimit
   OR day20.worldlifexpectancy.AdultMortality < temp2.lowerLimit;

DROP TEMPORARY TABLE IF EXISTS temp2;

-- For GDP
CREATE TEMPORARY TABLE IF NOT EXISTS temp3 AS (
    SELECT AVG(GDP) as avgGDP,
           AVG(GDP) + 3 * STD(GDP) as upperLimit,
           AVG(GDP) - 3 * STD(GDP) as lowerLimit
    FROM day20.worldlifexpectancy
);

UPDATE day20.worldlifexpectancy, temp3
SET day20.worldlifexpectancy.GDP = temp3.avgGDP
WHERE day20.worldlifexpectancy.GDP > temp3.upperLimit
   OR day20.worldlifexpectancy.GDP < temp3.lowerLimit;

DROP TEMPORARY TABLE IF EXISTS temp3;


--  1 EDA
SELECT 
    country,
    ROUND(AVG(Lifeexpectancy), 1) AS avg_life_expectancy,
    MIN(Lifeexpectancy) AS min_life_expectancy,
    MAX(Lifeexpectancy) AS max_life_expectancy
FROM 
    day20.worldlifexpectancy
GROUP BY 
    country;
-- 2
select country, lifeexpectancy, year,
row_number() over(partition by country ) as row_num
from day20.worldlifexpectancy
where country = 'Viet Nam'
;
--  tuoi tho tang dan theo tung nam


--  3
select status, avg(lifeexpectancy) as avg_life_expectancy
from day20.worldlifexpectancy
where year = (
	select max(year) from day20.worldlifexpectancy
)
group by status
;
--  tuoi tho trung binh cua cac nuoc phat trien cao hon cac nuoc dang phat trien

-- 4 
-- Correlation between AdultMortality and Lifeexpectancy
SELECT
    SUM((Lifeexpectancy - (SELECT AVG(Lifeexpectancy) FROM day20.worldlifexpectancy)) * 
        (AdultMortality - (SELECT AVG(AdultMortality) FROM day20.worldlifexpectancy))) / 
    (COUNT(*) * STD(Lifeexpectancy) * STD(AdultMortality)) AS Correlation
FROM day20.worldlifexpectancy;

-- 5
select case
when gdp < 1000 then 'Low'
when gdp between 1000 and 10000 then 'Medium'
else 'High'
end as gdp_range,
avg(lifeexpectancy) as avg_life_expectancy
from day20.worldlifexpectancy
group by gdp_range
;
--  gdp cang cao thi tuoi tho trung binh cang lon
--  6
select 
	case when measles > 100 then 'High Measles' else 'Low Measles' end as measles_impact,
    case when polio > 50 then 'High Polio' else 'Low Measles' end as polio_impact,
    avg(lifeexpectancy) as avg_life_expectancy
from day20.worldlifexpectancy
group by measles_impact, polio_impact
;
-- 7
SELECT 
    country,
    Schooling,
    Lifeexpectancy
FROM 
    day20.worldlifexpectancy
WHERE 
    Schooling = (SELECT MAX(Schooling) FROM day20.worldlifexpectancy)
    OR Schooling = (SELECT MIN(Schooling) FROM day20.worldlifexpectancy);
-- top 10
SELECT Country, Schooling, Lifeexpectancy
FROM day20.worldlifexpectancy
ORDER BY Schooling DESC
LIMIT 10;
-- last 10
SELECT Country, Schooling, Lifeexpectancy
FROM day20.worldlifexpectancy
ORDER BY Schooling ASC
LIMIT 10;
    
--  8
select country, year, avg(bmi) as avg_bmi
from day20.worldlifexpectancy
where country = 'Viet Nam'
group by year
order by year
;
-- 9
SELECT 
    country, 
    Lifeexpectancy, 
    infantdeaths, 
    `under-fivedeaths` AS under5_deaths,
    ROW_NUMBER() OVER(PARTITION BY country) AS row_num
FROM 
    day20.worldlifexpectancy
WHERE 
    Lifeexpectancy = (SELECT MAX(Lifeexpectancy) FROM day20.worldlifexpectancy);
-- min
SELECT 
    country, 
    Lifeexpectancy, 
    infantdeaths, 
    `under-fivedeaths` AS under5_deaths,
    ROW_NUMBER() OVER(PARTITION BY country) AS row_num
FROM 
    day20.worldlifexpectancy
WHERE 
    Lifeexpectancy = (SELECT MIN(Lifeexpectancy) FROM day20.worldlifexpectancy);
    
    
--  10
-- Rolling average of AdultMortality over 5 years
SELECT Country, Year, AVG(AdultMortality) OVER (PARTITION BY Country ORDER BY Year ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS RollingAvgAdultMortality
FROM day20.worldlifexpectancy;

-- cach khac
SELECT 
    t1.Country, 
    t1.Year, 
    AVG(t2.AdultMortality) as RollingAvgAdultMortality
FROM 
    day20.worldlifexpectancy t1
JOIN 
    day20.worldlifexpectancy t2
ON 
    t1.Country = t2.Country AND 
    t2.Year BETWEEN t1.Year - 4 AND t1.Year
GROUP BY 
    t1.Country, 
    t1.Year
ORDER BY 
    t1.Country, 
    t1.Year;
--  11
select
	sum((lifeexpectancy - (select avg(lifeexpectancy) from day20.worldlifexpectancy)) * (percentageexpenditure - (select avg(percentageexpenditure) from day20.worldlifexpectancy))) / 
    (count(*) * std(lifeexpectancy) * std(percentageexpenditure)) as correlation
from day20.worldlifexpectancy
;
-- low correlation

--  12
-- Correlation between BMI and Lifeexpectancy
SELECT
    SUM((Lifeexpectancy - (SELECT AVG(Lifeexpectancy) FROM day20.worldlifexpectancy)) * 
        (BMI - (SELECT AVG(BMI) FROM day20.worldlifexpectancy))) / 
    (COUNT(*) * STD(Lifeexpectancy) * STD(BMI)) AS CorrelationWithLifeexpectancy
FROM day20.worldlifexpectancy;

-- Correlation between BMI and AdultMortality
SELECT
    SUM((AdultMortality - (SELECT AVG(AdultMortality) FROM day20.worldlifexpectancy)) * 
        (BMI - (SELECT AVG(BMI) FROM day20.worldlifexpectancy))) / 
    (COUNT(*) * STD(AdultMortality) * STD(BMI)) AS CorrelationWithAdultMortality
FROM day20.worldlifexpectancy;

-- 	13
select
	case
		when gdp < 1000 then 'Low GDP'
        when gdp between 1000 and 10000 then 'Medium GDP'
        else 'High GDP'
    end as gdp_range,
    avg(lifeexpectancy) as avg_life_expectancy,
    avg(adultMortality) as avg_adult_mortality,
    avg(infantdeaths) as avg_infant_deaths
from day20.worldlifexpectancy
group by gdp_range;
-- higher gdp result in longer life expectancy, lower adult mortality and lower infant deaths
    
--  14

    