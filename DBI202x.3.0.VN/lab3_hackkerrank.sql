-- Lab3.6: https://docs.google.com/document/d/11-pqOaRuzYoubnq-OMOiaunblQ3uWYvk/edit

-- Bai 1. https://www.hackerrank.com/challenges/revising-the-select-query/problem?isFullScreen=true
SELECT * FROM CITY WHERE POPULATION > 100000 AND COUNTRYCODE = 'USA';

-- Bai 2. https://www.hackerrank.com/challenges/revising-the-select-query-2/problem?isFullScreen=true
SELECT NAME FROM CITY WHERE POPULATION > 120000 AND COUNTRYCODE = 'USA';

-- Bai 3. https://www.hackerrank.com/challenges/select-all-sql/problem?isFullScreen=true
SELECT * FROM CITY;

-- Bai 4. https://www.hackerrank.com/challenges/japanese-cities-attributes/problem?isFullScreen=true
SELECT * FROM CITY WHERE COUNTRYCODE = 'JPN';

-- Bai 5. https://www.hackerrank.com/challenges/japanese-cities-name/problem?isFullScreen=true
SELECT c.NAME FROM CITY c WHERE c.COUNTRYCODE = 'JPN';

-- Bai 6. https://www.hackerrank.com/challenges/weather-observation-station-1/problem?isFullScreen=true
SELECT s.CITY, s.STATE FROM STATION s;

