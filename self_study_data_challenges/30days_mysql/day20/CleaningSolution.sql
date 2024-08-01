USE Project;

SELECT *
FROM worldlifexpectancy;

-- Check duplicate values
 SELECT Country, Year, CONCAT(Country, Year), COUNT(CONCAT(Country,Year))
 FROM worldlifexpectancy
 GROUP BY Country, Year, CONCAT(Country,Year)
 HAVING COUNT(CONCAT(Country, Year)) > 1
 ;
 
 -- Identify Row_ID of duplicate values
 SELECT *
 FROM
 (
    SELECT Row_ID, CONCAT(Country, Year), ROW_NUMBER() OVER(PARTITION BY CONCAT(Country, Year) ORDER BY CONCAT(Country, Year)) as Row_Num
    FROM worldlifexpectancy
) AS Row_Table
WHERE Row_Num > 1
;

-- Remove duplicate values
DELETE FROM worldlifexpectancy
WHERE Row_ID IN (
        SELECT Row_ID
        FROM (
            SELECT Row_ID, CONCAT(Country, Year), ROW_NUMBER() OVER(PARTITION BY CONCAT(Country, Year) ORDER BY CONCAT(Country, Year)) as Row_Num
            FROM worldlifexpectancy
            ) as Row_Table
        WHERE Row_Num > 1
        );
    
-- Check country
SELECT DISTINCT(Country), COUNT(Country) as Count_Country
FROM worldlifexpectancy
GROUP BY Country
HAVING Count_Country = 1
;

-- Remove country with only 1 rows
DELETE FROM worldlifexpectancy
WHERE Country IN (
                SELECT Country
                FROM (
                    SELECT Country
                    FROM worldlifexpectancy
                    GROUP BY Country
                    HAVING COUNT(*) = 1
                    ) AS subquery
);

-- Check status
SELECT DISTINCT(Country)
FROM worldlifexpectancy
WHERE Status = 'Developing'
;

-- Check blank status
SELECT Country, Status
FROM worldlifexpectancy
WHERE Status = ''
;

-- Update Status Developing using Subquery
UPDATE worldlifexpectancy w
JOIN (
    SELECT DISTINCT Country
    FROM worldlifexpectancy
    WHERE Status = 'Developing'
) d ON w.Country = d.Country
SET w.Status = 'Developing'
WHERE w.Status = '' OR w.Status IS NULL
;

-- Update Status Developed using Subquery
UPDATE worldlifexpectancy w
JOIN (
    SELECT DISTINCT Country
    FROM worldlifexpectancy
    WHERE Status = 'Developed'
) d ON w.Country = d.Country
SET w.Status = 'Developed'
WHERE w.Status = '' OR w.Status IS NULL
;


-- Check blank value in Lifeexpectancy column
SELECT Country, Year, Lifeexpectancy
FROM worldlifexpectancy
WHERE Lifeexpectancy = ''
;

-- Update blank values in Lifeexpectancy column with Correlated Subqueries
UPDATE worldlifexpectancy w
SET Lifeexpectancy = (
    SELECT ROUND((prev.Lifeexpectancy + next.Lifeexpectancy) / 2,1)
    FROM (
        SELECT Country, Year, Lifeexpectancy
        FROM worldlifexpectancy
    ) AS prev
    JOIN (
        SELECT Country, Year, Lifeexpectancy
        FROM worldlifexpectancy
    ) AS next
    ON prev.Country = next.Country
    WHERE prev.Country = w.Country
    AND prev.Year = w.Year - 1
    AND next.Year = w.Year + 1
)
WHERE Lifeexpectancy IS NULL OR Lifeexpectancy = '';

-- Check outliner in BMI
SELECT w.Country, w.Year, w.BMI, stats.mean_bmi, stats.stddev_bmi,
       ABS(w.BMI - stats.mean_bmi) / NULLIF(stats.stddev_bmi, 0) AS deviation
FROM worldlifexpectancy w
JOIN (
    SELECT Country,
           AVG(BMI) AS mean_bmi,
           STDDEV(BMI) AS stddev_bmi
    FROM worldlifexpectancy
    GROUP BY Country
) AS stats ON w.Country = stats.Country
HAVING ABS(w.BMI - stats.mean_bmi) / NULLIF(stats.stddev_bmi, 0) > 3 -- threshold for outliers
ORDER BY w.Country, w.Year;


-- Update outlier BMI values
UPDATE worldlifexpectancy w
JOIN (
    SELECT w1.Country, w1.Year, 
           (SELECT AVG(w2.BMI)
            FROM worldlifexpectancy w2
            WHERE w2.Country = w1.Country
              AND w2.Year IN (w1.Year - 1, w1.Year + 1)
           ) AS new_bmi
    FROM worldlifexpectancy w1
    JOIN (
        SELECT w.Country, w.Year, w.BMI,
               stats.mean_bmi, stats.stddev_bmi,
               ABS(w.BMI - stats.mean_bmi) / NULLIF(stats.stddev_bmi, 0) AS deviation
        FROM worldlifexpectancy w
        JOIN (
            SELECT Country,
                   AVG(BMI) AS mean_bmi,
                   STDDEV(BMI) AS stddev_bmi
            FROM worldlifexpectancy
            GROUP BY Country
        ) AS stats ON w.Country = stats.Country
        HAVING ABS(w.BMI - stats.mean_bmi) / NULLIF(stats.stddev_bmi, 0) > 3 -- threshold for outliers
    ) AS outliers ON w1.Country = outliers.Country AND w1.Year = outliers.Year
) AS updates ON w.Country = updates.Country AND w.Year = updates.Year
SET w.BMI = ROUND(updates.new_bmi, 1);











