-- 1. Approved Transactions
-- Using table Transactions
-- Banks have the ability to approve or deny transactions made depending on several factors.

-- The bank wants you to come in and create a report for them that gives them the following information:

-- Month, Country, Approved_Transactions, Approved_Amount, Chargebacks, Chargeback_Amount.

-- They want to look at historic trends for months, not years. They want all of one months data on one line. For example, all of January's data for the above columns should be output on one row.

-- A chargeback is the amount sent back to a bank account if a transaction is declined.

-- Return the output table order based off earliest month.
SELECT DATE_FORMAT(transaction_date, '%m') `Month`
       , `Country`
       , SUM(IF(`state`='Approved', 1, 0)) `Approved_Transactions`
       , SUM(IF(`state`='Approved', `amount`, 0)) `Approved_Amount`
       , SUM(IF(`state`='Declined', 1, 0)) `Chargebacks`
       , SUM(IF(`state`='Declined', `amount`, 0)) `Chargeback_Amount`
FROM `transactions`
GROUP BY DATE_FORMAT(transaction_date, '%m'), `Country`
ORDER BY DATE_FORMAT(transaction_date, '%m');

-- Q: What is month 9 look like?
-- 09 Canada 1 250000 0 0
-- 09 Canada 2 6100 0 0
-- >> 09 Canada 2 585000 3 10124000
-- 09 Canada 1 1500 1 87000


-- 2. Highest Grade
-- Using table highest_grade
-- Write a query to find the highest grade with its corresponding course for each student. In case of a tie, you should find the course with the smallest course_id.

-- Output the name, class_id, and grade for those classes.

-- Order on the name alphabetically.
WITH highest_grades AS (
    SELECT `student_name`
            , MAX(`grade`) highest_grade
    FROM `highest_grade`
    GROUP BY `student_name`
)
SELECT hgdim.`student_name`
       , MIN(hg.`class_id`) `course_id`
       , hgdim.`highest_grade`
FROM `highest_grades` hgdim
JOIN `highest_grade` hg
    ON hg.student_name = hgdim.student_name
                AND hg.grade = hgdim.highest_grade
GROUP BY hgdim.student_name, hgdim.highest_grade
ORDER BY hgdim.student_name;


-- Q: What is the result in line 3rd look like?
-- Ron    1 95
-- >> Leslie 1 95
-- Ben   2 97
-- Ben   1 95


-- 3. Right Twix vs Left Twix
-- Using table candy_poll
-- In a marketing promotion by Twix, they created two ficitional sides of the Twix candy bar. They asked fans of the candy bar to choose sides.

-- In a recent poll, consumers voted for either left Twix or right Twix.

-- Write a query to return the percentage of all consumers who chose right or left Twix.

-- You should have 2 columns in your output: "Right_Twix_Percentage" and "Left_Twix_Percentage" with the corresponding percentages.

-- Round to 2 decimal places.
SELECT ROUND(right_vote / total_votes * 100, 2) Right_Twix_Percentage
       , ROUND(left_vote / total_votes * 100, 2) Left_Twix_Percentage
FROM (
    SELECT right_vote + left_vote AS total_votes
           , right_vote
           , left_vote
    FROM candy_poll) total_votes;

-- Q: What is the result look like?
-- >> 46.17  53.83
-- 45.17  54.83
-- 46.25  53.32
-- 45.25  54.32


-- 4. Basketball Greatness
-- Using table player_totals
-- Write a query to rank Points scored by all time greats in basketball. The ranking should be calculated according to the following rules:

-- The scores should be ranked from the highest to the lowest.

-- If there is a tie between two scores, both should have the same ranking.

-- After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.

-- Return the result table ordered by score and name in descending order.
SELECT *
    , DENSE_RANK() OVER ( ORDER BY points DESC) ranking
FROM player_totals;


-- Q: Who ranking at number 5?
-- Dirk Nowitzki
-- Wilt Chamberlain
-- Kobe Bryant
-- >> Michael Jordan


-- 5. Twitter Addiction (Very Hard)
-- Using table twitter_addiction
-- Twitter (now known as "X"), is known for being addicting. Scrolling and Tweeting (or "X-ing"?) has become synonymous with social media.

-- Find the average time (in minutes) that each user waits until their next Tweet.
WITH tweet_intervals AS (
    SELECT
        twitter_id,
        tweet_time,
        TIMESTAMPDIFF(MINUTE, LAG(tweet_time) OVER (PARTITION BY twitter_id ORDER BY tweet_time), tweet_time) AS minutes_until_next_tweet
    FROM `twitter_addiction`
)
SELECT
    twitter_id,
    AVG(minutes_until_next_tweet) AS avg_minutes_until_next_tweet
FROM tweet_intervals
WHERE minutes_until_next_tweet IS NOT NULL
GROUP BY twitter_id;


-- Q: What is the result of twitter_id 1002 ?
-- 1002 240
-- 1002 22.5
-- 1002 202
-- >> 1002 435