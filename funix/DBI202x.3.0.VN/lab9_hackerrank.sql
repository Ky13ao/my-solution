-- Lab 9.3: https://docs.google.com/document/d/1yqkmwI9pdYhPulxcmPDRpAeexCbEhrMz/edit

-- Cau 1. https://www.hackerrank.com/challenges/asian-population/problem?isFullScreen=true
SELECT SUM(CITY.POPULATION)
FROM CITY
INNER JOIN COUNTRY ON CITY.CountryCode =COUNTRY.Code
GROUP BY COUNTRY.CONTINENT
HAVING COUNTRY.CONTINENT='Asia';

-- Cau 2. https://www.hackerrank.com/challenges/african-cities/problem?isFullScreen=true
SELECT CITY.NAME
FROM CITY
INNER JOIN COUNTRY ON CITY.CountryCode =COUNTRY.Code
WHERE COUNTRY.CONTINENT='Africa';

-- Cau 3. https://www.hackerrank.com/challenges/average-population-of-each-continent/problem?isFullScreen=true
SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION))
FROM CITY
INNER JOIN COUNTRY ON CITY.CountryCode =COUNTRY.Code
GROUP BY COUNTRY.CONTINENT;

-- Cau 4. https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true
SELECT h.hacker_id, h.name
FROM Hackers h
JOIN Submissions s ON s.hacker_id=h.hacker_id
JOIN Challenges c ON c.challenge_id =s.challenge_id
JOIN Difficulty d ON c.difficulty_level=d.difficulty_level
WHERE s.score=d.score
GROUP BY h.hacker_id, h.name
HAVING COUNT(DISTINCT s.challenge_id )>1
ORDER BY COUNT(s.challenge_id ) DESC, h.hacker_id;

-- Cau 5. https://www.hackerrank.com/challenges/the-pads/problem
SELECT CONCAT(Name,'(',LEFT(Occupation,1),')')
FROM OCCUPATIONS
ORDER BY Name;
SELECT CONCAT('There are a total of ',count(occupation),' ',LOWER(occupation),'s.')
FROM OCCUPATIONS
GROUP BY occupation
ORDER BY count(occupation), occupation;

-- Cau 6. https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true
SELECT w.id, p.age, w.coins_needed, w.power
FROM Wands w
JOIN Wands_Property p ON w.code=p.code
WHERE p.is_evil=0 AND w.coins_needed=
(SELECT MIN(w1.coins_needed) FROM Wands w1
 JOIN Wands_Property p1 ON w1.code=p1.code 
 WHERE w.power=w1.power AND p.age=p1.age)
ORDER BY w.power DESC, p.age DESC;

-- Cau 7. https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true
SELECT h.hacker_id, h.name, COUNT(c.challenge_id) challenge_count
FROM Hackers h
JOIN Challenges c ON c.hacker_id=h.hacker_id
GROUP BY h.hacker_id, h.name
HAVING challenge_count=
(SELECT MAX(t.ch_count) 
 FROM (SELECT c1.hacker_id, COUNT(c1.hacker_id) ch_count 
       FROM Challenges c1 
       GROUP BY c1.hacker_id) t)
OR challenge_count IN 
(SELECT t.ch_count 
 FROM (SELECT c1.hacker_id, COUNT(c1.hacker_id) ch_count 
       FROM Challenges c1 GROUP BY c1.hacker_id) t 
 GROUP BY t.ch_count 
 HAVING COUNT(t.ch_count)=1)
ORDER BY challenge_count DESC, h.hacker_id;

-- Cau 8. https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true
SELECT s.hacker_id, h.name, SUM(s.max_score) sum_max_score
FROM (SELECT s1.hacker_id, MAX(s1.score) max_score
      FROM Submissions s1
      GROUP BY s1.hacker_id, s1.challenge_id) s
JOIN Hackers h ON s.hacker_id=h.hacker_id
GROUP BY s.hacker_id, h.name
HAVING sum_max_score!=0
ORDER BY sum_max_score DESC, s.hacker_id ASC;


-- Cau 9. https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true
    -- NULL       2015-10-01 2015-10-02 2015-10-02
    -- 2015-10-02 2015-10-02 2015-10-03 2015-10-03
    -- 2015-10-03 2015-10-03 2015-10-04 2015-10-04
    -- 2015-10-04 2015-10-04 2015-10-05 NULL
    -- NULL       2015-10-11 2015-10-12 2015-10-12
    -- 2015-10-12 2015-10-12 2015-10-13 NULL
    -- NULL       2015-10-19 2015-10-20 NULL
    -- NULL       2015-10-15 2015-10-16 NULL
    -- NULL       2015-10-17 2015-10-18 NULL
    -- NULL       2015-10-21 2015-10-22 NULL
    -- NULL       2015-10-25 2015-10-26 2015-10-26
    -- 2015-10-27 2015-10-27 2015-10-28 2015-10-28
    -- 2015-10-26 2015-10-26 2015-10-27 2015-10-27
    -- 2015-10-28 2015-10-28 2015-10-29 2015-10-29
    -- 2015-10-29 2015-10-29 2015-10-30 2015-10-30
    -- 2015-10-30 2015-10-30 2015-10-31 NULL
    -- NULL       2015-11-01 2015-11-02 NULL
    -- NULL       2015-11-04 2015-11-05 2015-11-05
    -- 2015-11-07 2015-11-07 2015-11-08 NULL
    -- 2015-11-05 2015-11-05 2015-11-06 2015-11-06
    -- 2015-11-06 2015-11-06 2015-11-07 2015-11-07
    -- NULL       2015-11-11 2015-11-12 2015-11-12
    -- 2015-11-12 2015-11-12 2015-11-13 NULL
    -- NULL       2015-11-17 2015-11-18 NULL
SELECT t0.Start_Date, MIN(t1.End_Date) end_date
FROM (SELECT p1.Start_Date, p1.End_Date
      FROM Projects p1
      LEFT JOIN Projects p0 ON p0.End_Date = p1.Start_Date
      WHERE ISNULL(p0.task_id)
      ORDER BY p1.End_Date ASC) t0
JOIN (SELECT p1.Start_Date, p1.End_Date
      FROM Projects p1
      LEFT JOIN Projects p2 ON p1.End_Date = p2.Start_Date
      WHERE ISNULL(p2.task_id)
      ORDER BY p1.End_Date DESC) t1 ON t0.End_Date<=t1.End_Date
GROUP BY t0.Start_Date
ORDER BY DATEDIFF(MIN(t1.End_Date), t0.Start_Date) ASC, t0.Start_Date ASC;

-- Cau 10. https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true
SELECT s.Name
FROM Students s
JOIN Packages p ON s.id=p.id
JOIN Friends f ON s.id=f.id
JOIN Packages pf ON f.friend_id=pf.id
WHERE p.Salary < pf.Salary
ORDER BY pf.Salary;


-- Cau 11. https://www.hackerrank.com/challenges/symmetric-pairs/problem?isFullScreen=true
SELECT f0.X, f0.Y
FROM Functions f0
INNER JOIN Functions f1 ON f0.X=f1.Y AND f0.Y=f1.X
GROUP BY f0.X, f0.Y
HAVING f0.X<f0.Y OR (f0.X=f0.Y AND COUNT(f1.X)>1)
ORDER BY f0.X;

-- Cau 12. https://www.hackerrank.com/challenges/interviews/problem?isFullScreen=true
SELECT c.contest_id, c.hacker_id, c.name, t0.s1, t0.s2, t1.s1, t1.s2
FROM Contests c
JOIN (SELECT u.contest_id, sum(ss.total_submissions) s1, sum(ss.total_accepted_submissions) s2
     FROM Colleges u
     JOIN Challenges ch ON ch.college_id=u.college_id
     JOIN Submission_Stats ss ON ss.challenge_id=ch.challenge_id
     GROUP BY u.contest_id) t0 ON t0.contest_id=c.contest_id
JOIN (SELECT u.contest_id, sum(vs.total_views) s1, sum(vs.total_unique_views) s2
     FROM Colleges u
     JOIN Challenges ch ON ch.college_id=u.college_id
     JOIN View_Stats vs ON vs.challenge_id=ch.challenge_id
     GROUP BY u.contest_id) t1 ON t1.contest_id=c.contest_id
GROUP BY c.contest_id, c.hacker_id, c.name
HAVING t0.s1+t1.s1>0;