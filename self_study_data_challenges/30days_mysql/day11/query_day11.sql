-- -- query 8
-- Table name boss
-- My Boss wants a report that shows each employee and their bosses name so he can try to memorize it before our quarterly social event.
-- Provide an output that includes the employee name matched with the name of their boss.
-- If they don't have a boss still include them in the output.
-- Order output on employee name alphabetically.
-- What is the correct answer in the 3rd line of the result?
-- Carol Danvers
-- Carolina Fancis
-- > Donald Glover
-- Gerald Butler
select b1.employee_name, b2.employee_name as boss_name from boss b1 left join boss b2 on b1.boss_id = b2.employee_id order by b1.employee_name;

-- -- query 9
-- Table name employee_name, employee_location
-- Join these two tables together to return the first name, last name, and state for each person.
-- If there is no matching employee in the location table the state should be Null for that person.
-- Order the output alphabetically on their first names.
-- Who has a NULL location?
-- > Sally
-- Luke
-- John
-- Kurt
select first_name, last_name, state from employee_name emn left join employee_location eml on emn.person_id = eml.employee_id;

-- -- query 10
-- Table name bread_table, meat_table
-- Yan is a sandwich enthusiast and is determined to try every combination of sandwich possible. He wants to start with every combination of bread and meats and then move on from there, but he wants to do it in a systematic way.
-- Below we have 2 tables, bread and meats
-- Output every possible combination of bread and meats to help Yan in his endeavors.
-- Order by the bread and then meat alphabetically. This is what Yan prefers.
-- What's line of 'Sourdough Bacon' in the result?
-- 7
-- 6
-- > 8
-- 9