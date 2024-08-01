CREATE DATABASE mysql_bonus1;
USE mysql_bonus1;

-- 1. Salary By Department
-- Using table Employee_Salary
-- Compare each employee's salary with the average salary of their department. Include the department, first name, last name, salary, and average salary of department in your output
-- Average salary should be called "dept_avg" in your output.
-- Order by the department and salary from highest to lowest.
WITH depts AS 
    (SELECT department
            , AVG(salary) dept_avg
    FROM Employee_Salary
    GROUP BY department)
SELECT CONCAT(last_name, ' ', first_name) name
    , es.department
    , salary
    , dept_avg 
FROM Employee_Salary es
JOIN depts d ON d.department = es.department
ORDER BY es.department DESC, es.salary DESC;
-- Q: What is the result in line 3rd look like?
-- >> Bernard Bailey IT 75000 63333.3333
-- Lambowitz Luke Accounting 55000 48333.3333
-- John IT 50000 63333.3333
-- Michael Sales 75000 43000

-- 2. Temperature Fluctuations
-- Using table Temperatures
-- Write a query to find all dates with higher temperatures compared to the previous dates (yesterday).

-- Order dates in ascending order.
SELECT * 
FROM Temperatures cur
JOIN Temperatures pre ON DATE_ADD(cur.`date`, INTERVAL -1 DAY )=pre.`date`
WHERE cur.temperature > pre.temperature
ORDER BY cur.`date`;
-- Q: What is the result in line 5th look like?
-- 2022-01-02
-- >> 2022-01-09
-- 2022-01-05
-- 2022-01-08

-- 3. Contact Information

-- Using tables Contacts, People
-- Write a query to report the first and last name of each person in the people table. Join to the contacts table and return the email for each person as well.
-- If they don't have an email we need to create one for them. Use their first and last name to create a gmail for them.
-- Example: Jenny Fisher's email would become jenny.fisher@gmail.com
-- Output should include first name, last name, and email. All emails should be populated.
-- Order the output on email address alphabetically.
SELECT CONCAT(first_name, ' ', last_name) full_name
        , IFNULL(email, CONCAT(LOWER(first_name), '.', LOWER(last_name), '@gmail.com')) email
FROM People p
LEFT JOIN Contacts c ON c.id = p.id
ORDER BY email;

-- Q: What is the result in line 5th look like?
-- Emma Walker emma.walker@gmail.com
-- Liam Wright liam.wright@gmail.com
-- Brandon Lee brandon.lee@gmail.com
-- >> Benjamin Hill benjamin.hill@gmail.com


-- 4. Using table Desserts
-- Marcie's Bakery is having a contest at her store. Whichever dessert sells more each day will be on discount tomorrow. She needs to identify which dessert is selling more.
-- Write a query to report the difference between the number of Cakes and Pies sold each day.
-- Output should include the date sold, the difference between cakes and pies, and which one sold more (cake or pie). The difference should be a positive number.
-- Return the result table ordered by Date_Sold.
SELECT DATE_FORMAT(date_sold, '%Y-%m-%d') date_sold
    , ABS(pie_sold - cake_sold) diff
    , CASE WHEN pie_sold > cake_sold THEN 'Pie'
           WHEN pie_sold < cake_sold THEN 'Cake'
     END product
FROM (SELECT date_sold, 
       SUM(IF(product='Pie', amount_sold, 0)) pie_sold,
       SUM(IF(product='Cake', amount_sold, 0)) cake_sold
FROM desserts
GROUP BY date_sold) AS ds
ORDER BY date_sold;

-- Q: What is the result in line 4th look like?
-- >> 2022-06-04 9 Pie
-- 2022-06-03 1 Cake
-- 2022-06-05 16 Cake
-- 2022-06-01 12 Pie


-- 5. Consecutive Visits (Very Hard)

-- Using tables Names, Dates
-- Write a query to return the ID and Name, and the number of consecutive visits of the person who has gone to Waffle House the most days in a row.
WITH visits AS (
    SELECT n.id, n.name, d.visit_date,
           ROW_NUMBER() OVER (PARTITION BY n.id ORDER BY d.visit_date) AS row_num
    FROM Names n
    JOIN Dates d ON d.id = n.id
),
streaks AS (
    SELECT id, name, visit_date, 
           visit_date - INTERVAL row_num DAY AS streak_group
    FROM visits
),
consecutive_visits AS (
    SELECT id, name, COUNT(*) AS streak_length
    FROM streaks
    GROUP BY id, name, streak_group
)
SELECT id, name, streak_length
FROM consecutive_visits
ORDER BY streak_length DESC;

-- Q: What is the result look like?
-- 1 Ron 3
-- >> 1 Ron 4
-- 2 Leslie 3
-- 2 Leslie 4