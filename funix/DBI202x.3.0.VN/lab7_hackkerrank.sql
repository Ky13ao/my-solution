-- Lab 7.2: https://docs.google.com/document/d/1BMhUF3EYdcnXVSPO6Pl_I4zlibAiyW6q/edit

-- Bai 1. https://www.hackerrank.com/challenges/revising-aggregations-sum/problem?isFullScreen=true
SELECT SUM(POPULATION) FROM CITY WHERE DISTRICT = 'California';

-- Bai 2. https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem?isFullScreen=true
SELECT AVG(POPULATION) FROM CITY WHERE DISTRICT = 'California';

-- Bai 3. https://www.hackerrank.com/challenges/average-population/problem?isFullScreen=true
SELECT ROUND(AVG(POPULATION),0) FROM CITY; 

-- Bai 4. https://www.hackerrank.com/challenges/japan-population/problem?isFullScreen=true
SELECT SUM(POPULATION) FROM CITY WHERE COUNTRYCODE = 'JPN';

-- Bai 5. https://www.hackerrank.com/challenges/population-density-difference/problem?isFullScreen=true
SELECT MAX(POPULATION)-MIN(POPULATION) FROM CITY;

-- Bai 6. https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true
-- She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.
SELECT CEIL(AVG(salary)-AVG(REPLACE(salary,0,''))) FROM employees;


-- Bai 7. https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true
SELECT months*salary earnings, COUNT(employee_id) FROM employee GROUP BY earnings ORDER BY earnings DESC LIMIT 1;


-- Bai 8. https://www.hackerrank.com/challenges/weather-observation-station-2/problem?isFullScreen=true
SELECT ROUND(SUM(LAT_N),2), ROUND(SUM(LONG_W),2) FROM STATION;

-- Bai 9. https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true
SELECT COUNT(city) - COUNT(DISTINCT city) FROM STATION;

-- Bai 10. https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true
SELECT city, CHAR_LENGTH(city) len_city_name FROM station ORDER BY len_city_name, city ASC LIMIT 1;
SELECT city, CHAR_LENGTH(city) len_city_name FROM station ORDER BY len_city_name DESC, city ASC LIMIT 1;


-- Bai 11. https://www.hackerrank.com/challenges/weather-observation-station-13/problem?isFullScreen=true
SELECT ROUND(SUM(lat_n),4) FROM station WHERE lat_n > 38.788 and lat_n < 137.2345;

-- Bai 12. https://www.hackerrank.com/challenges/weather-observation-station-14/problem?isFullScreen=true
SELECT ROUND(MAX(lat_n),4) FROM station WHERE lat_n < 137.2345;

-- Bai 13. https://www.hackerrank.com/challenges/weather-observation-station-15/problem?isFullScreen=true
SELECT ROUND(LONG_W, 4) FROM station WHERE LAT_N<137.2345 ORDER BY LAT_N DESC LIMIT 1;

-- Bai 14. https://www.hackerrank.com/challenges/weather-observation-station-16/problem?isFullScreen=true
SELECT ROUND(MIN(lat_n), 4) FROM station WHERE lat_n > 38.778;

-- Bai 15. https://www.hackerrank.com/challenges/weather-observation-station-17/problem?isFullScreen=true
SELECT ROUND(LONG_W, 4) FROM station WHERE LAT_N>38.778 ORDER BY LAT_N ASC LIMIT 1;

-- Bai 16. https://www.hackerrank.com/challenges/weather-observation-station-18/problem?isFullScreen=true
SELECT ROUND(MAX(lat_n)-MIN(lat_n)+MAX(long_w)-MIN(long_w),4) FROM station;

-- Bai 17. https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true
SELECT e.company_code company_code, (SELECT c.founder FROM company c WHERE c.company_code=e.company_code) founder, COUNT(DISTINCT e.lead_manager_code) no_of_lead_mgr, COUNT(DISTINCT e.senior_manager_code) no_of_sr_mgr, COUNT(DISTINCT e.manager_code) no_of_mgr, COUNT(DISTINCT e.employee_code) no_of_emp FROM employee e GROUP BY e.company_code;

-- Bai 18. https://www.hackerrank.com/challenges/weather-observation-station-19/problem?isFullScreen=true
SELECT ROUND(SQRT(POWER(MAX(lat_n)-MIN(lat_n),2)+POWER(MAX(long_w)-MIN(long_w),2)),4) FROM station;
