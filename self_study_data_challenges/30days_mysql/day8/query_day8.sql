---- query 6
-- Herschel's Manufacturing Plant has hit some hard times with the economy and unfortunately they need to let some people go.
-- They figure the younger employees need their jobs more as they are growing families so they decide to let go of their 3 oldest employees. They have more experience and will be able to land on their feet easier (and they had to pay them more).
-- Write a query to identify the ids of the three oldest employees.
-- Order output from oldest to youngest.
-- What is the correct answer in 2nd line of the result?
-- > 11
select * from employees order by birth_date;

---- query 7
-- American Football is a thing of beauty, but some teams fly above the rest.
-- Identify the Football teams that scored over 400 points and had 80 or less fouls last season.
-- What is the correct answer in the 1st line of the result?
-- > Green Bay Packers
select * from football where points_scored > 400 and penalties <=80;

---- query 8
-- If a patient has a BMI of 30 or over they are considered obese.
-- The calculation for BMI is as follows:
---- (Formula: weight (lb) / [height (in)]^2 x 703)
-- Find the patients who are considered "obese" and provide the patient ID and their BMI. Round BMI to 1 decimal point.
-- What is the correct answer in 3rd of the result?
-- > 1007
select *, round(weight_pounds / (height_inches * height_inches) * 703, 1) as bmi from patients where round(weight_pounds / (height_inches * height_inches) * 703, 1) >= 30;

---- query 9
-- Cars need to be inspected every year in order to pass inspection and be street legal. If a car has any critical issues it will fail inspection or if it has more than 3 minor issues it will also fail.
-- Write a query to identify all of the cars that passed inspection.
-- Output should include the owner name and vehicle name. Order by the owner name alphabetically.
-- What is the correct answer in 1st line of the result?
-- > David
 select * from inspections where critical_issues = 0 and minor_issues <=3 order by owner_name;

-- query 10
-- If our company hits its yearly targets, every employee receives a salary increase depending on what level you are in the company.
-- Give each Employee who is a level 1 a 10% increase, level 2 a 15% increase, and level 3 a 200% increase.
-- Include this new column in your output as "new_salary"
-- What is the correct answer in 3rd line of the result?
-- > 66000
select *, (CASE pay_level WHEN 1 THEN 0.1 WHEN 2 THEN 0.15 ELSE 2 END)*salary + salary as new_salary from employees2;

