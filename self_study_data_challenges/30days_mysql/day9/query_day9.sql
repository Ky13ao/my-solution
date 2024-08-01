-- -- query 6
-- Table name purchases
-- Write a query to determine the Average Purchase price for Males and Females.
-- Round to 2 decimal places and order by Gender.
-- What is the correct answer of M gender?
select gender, round(avg(total_purchase), 25) avg_purchase from purchases group by gender;
-- > 92.25

-- -- query 7
-- Table name ice_cream
-- The National Ice Cream Association recently released their Ranking for Ice Cream flavors for 2023.
-- One disgruntled ice cream lover was not happy with the official rankings and decided to create his own community sourced rankings.
-- He wanted to send the ice cream flavors that the community ranked higher than the judges to hopefully persuade them to raise their scores.
-- Write a query to return ice cream flavors that were ranked higher by the community than the official ratings.
-- Order the flavors alphabetically.
-- What is the correct answer in the 2nd line of the result
select * from ice_cream where official_rating < community_rating order by flavor;
-- > Chocolate

-- -- query 8
-- Table name classes
-- Write a query to determine which classes have the highest average grade.
-- Output the class and average grade.
-- Order average grade from highest to lowest.
-- What is the correct answer in the 3rd line of the result?
select class, avg(grade) avg_grade from classes group by class order by avg_grade desc;
-- > English

-- -- query 9
-- Table name devices
-- Write a query to return the device IDs that play League of Legends and include in the first time that device played that game in your output.
-- Order by the oldest to newest time played.
-- How many devices?
select device_id, min(date_played) first_time from devices where game = 'League of Legends' group by device_id order by first_time;
-- > 2

-- -- query 10
-- Table name sessions
-- What was the average time spent, per user, gaming on their computer?
-- Which user_id has a biggest average time gaming?
-- > 4
select user_id, avg(minutes_per_session) avg_time_spent from sessions where activity = 'Gaming' group by user_id order by avg_time_spent desc;