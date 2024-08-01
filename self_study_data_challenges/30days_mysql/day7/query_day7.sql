---- query 6
-- A country is big if:
-- it has an area of at least three million (i.e., 3000000 km2), or
-- it has a population of at least one hundred million (i.e., 100,000,000).
-- Write a query to report the name, population, and area of the big countries.
-- Return the result table by country alphabetically.
-- What is the correct answer at 4th line of the result?
select country, square_kilometers, population from Country where square_kilometers > 3000000 or population > 100000000 order by country;

---- query 7
-- Write a query to report the IDs of low quality YouTube videos.
-- A video is considered low quality if the like percentage of the video (number of likes divided by the total number of votes) is less than 55%.
-- Return the result table ordered by ID in ascending order.
-- What is the correct answer at 2nd line of the result?
select * from youtube_videos where thumbs_up/(thumbs_up+thumbs_down) < 0.55 order by video_id;

---- query 8
-- Select customers IDs who bought "M&Ms", "Snickers", or "Twizzlers".
-- What is the correct answer at 2nd line of the result?
-- > 104
select * from customers where purchased_items REGEXP 'M&Ms|Snickers|Twizzlers';

---- query 9
-- I love chocolate and only want delicious baked goods that have chocolate in them!
-- Write a Query to return bakery items that contain the word "Chocolate".
-- What is the correct answer in the 1st line of the result?
-- > Double Chocolate Doughnut
select * from bakery_items where product_name regexp 'Chocolate';

---- query 10
-- Create a gamer tag for each player in the tournament.
-- Select the first 3 characters of their first name and combine that with the year they were born.
-- Your output should have their first name, last name, and gamer tag called "gamer_tag"
-- Order output on gamertag in alphabetical order.
-- What is the correct answer at 3rd line of the result?
-- > Kelly
select first_name, last_name, CONCAT(SUBSTR(first_name, 1, 3), SUBSTR(birth_date, 1, 4)) gamer_tag from gamer_tags order by gamer_tag;
