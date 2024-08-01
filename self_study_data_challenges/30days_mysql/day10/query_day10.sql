mysql> show tables;
+-----------------------+
| Tables_in_mysql_day10 |
+-----------------------+
| emails                |
| employees_info        |
| players               |
| stores                |
+-----------------------+
4 rows in set (0.03 sec)

-- -- query 7
-- Table name stores
-- Write a query that returns all of the stores whose average yearly revenue is greater than one million dollars.
-- Output the store ID and average revenue. Round the average to 2 decimal places.
-- Order by store ID.
-- What is avg yearly revenue of store_id 2?
select store_id, round(avg(revenue), 2) avg_revenue from stores group by store_id having avg_
revenue > 1000000;
-- > 1766666.67


-- -- query 8
-- Table name players
-- Scouts often go to Amateur Baseball games to find potential players to bring up to the big leagues. They want to categorize the players to determine what skill level they're currently at.
-- If a player has a batting average of .38 or higher they are a "Great Hitter". If a player has a batting average between .27 and .37 they're "Average". Anything below a .27 is "Below Average"
-- Return each players ID, Batting Average, and skill level as "skill_level".
-- What is skill_level of player_id 104?



-- -- query 9
-- Table name employees_info
-- It's been a tough year and the CEO has tasked you to trim the low performers so they can save face with the stakeholders. It's just good business.
-- A low performer is someone who was given a rating of 5 or less in their end of year review and has completed less than 75% of the tasks assigned to them.
-- Return the names of the low performers in the output (and hope your name isn't on the list).
-- Order output alphabetically.
-- How many low performers in the output?
-- > 2
select *, tasks_completed/tasks_assigned tasks_completed_perc from employees_info having end_of_year_review_rating <= 5 and tasks_completed_perc < 0.75 order by name;


-- -- query 10
-- Table name emails
-- There's recently been an error on our server where some emails were duplicated. We need to identify those emails so we can remove the duplicates.
-- Write an SQL query to report all the duplicate emails and how many times they are in the database.
-- Output should be in alphabetical order.
-- How many duplicated emails in total?
select email, count(*) duplicates from emails group by email having duplicates > 1;
-- > 1