-- Lab 6.2: https://docs.google.com/document/d/1veRR8yCvha9xGTefIpf1UO5J62Lryi7R/edit

-- Cau1. https://www.hackerrank.com/challenges/weather-observation-station-3/problem?isFullScreen=true
SELECT DISTINCT CITY FROM STATION WHERE mod(ID, 2) =0;

-- Cau2. https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[a,e,i,o,u]';

-- Cau3. https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '[a,e,i,o,u]$';

-- Cau4. https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[a,e,i,o,u].*[a,e,i,o,u]$';

-- Cau5. https://www.hackerrank.com/challenges/weather-observation-station-9/problem?isFullScreen=true
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '^[^[a,e,i,o,u]]';

-- Cau6. https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true
SELECT DISTINCT CITY FROM STATION WHERE CITY REGEXP '(^[^[a,e,i,o,u]]|[^[a,e,i,o,u]]$)';

-- Cau7. https://www.hackerrank.com/challenges/more-than-75-marks/problem?isFullScreen=true
SELECT Name FROM STUDENTS WHERE Marks > 75 ORDER BY RIGHT(Name,3), ID ASC;

-- Cau8. https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true
SELECT
  CASE
    WHEN a + b <= c OR b + c <= a OR a + c <= b THEN 'Not A Triangle'
    WHEN a = b AND b = c THEN 'Equilateral'
    WHEN a = b OR b = c OR a = c THEN 'Isosceles'
    ELSE 'Scalene'
  END
FROM
  TRIANGLES;

-- Cau9: https://www.hackerrank.com/challenges/name-of-employees/problem?isFullScreen=true
SELECT name FROM Employee ORDER BY name ASC;