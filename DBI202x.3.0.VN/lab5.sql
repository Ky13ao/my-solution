-- Lab 5.1 https://docs.google.com/document/d/1rCvwQlukgDUhM_WN-lIKwvqAA9998FNG/edit

SELECT 10 != 10; -- not equals
SELECT 15 > 14 && 99 - 5 <= 94; -- greater than and less than or equals
SELECT 1 IN (5,3) || 9 BETWEEN 8 AND 10; -- 1 in [5,3] or 9 in range(8,10)

-- Truy vấn tất cả cuốn sách được xuất bản (released_year) trước năm 1980
SELECT * FROM books WHERE released_year < 1980;

-- Truy vấn tất cả cuốn sách được viết bởi Eggers và Chabon.
SELECT * FROM books WHERE author_lname IN ('Eggers', 'Chabon');
/*
+---------+-------------------------------------------+--------------+--------------+---------------+----------------+-------+
| book_id | title                                     | author_fname | author_lname | released_year | stock_quantity | pages |
+---------+-------------------------------------------+--------------+--------------+---------------+----------------+-------+
|       5 | A Hologram for the King: A Novel          | Dave         | Eggers       |          2012 |            154 |   352 |
|       6 | The Circle                                | Dave         | Eggers       |          2013 |             26 |   504 |
|       7 | The Amazing Adventures of Kavalier & Clay | Michael      | Chabon       |          2000 |             68 |   634 |
|       9 | A Heartbreaking Work of Staggering Genius | Dave         | Eggers       |          2001 |            104 |   437 |
+---------+-------------------------------------------+--------------+--------------+---------------+----------------+-------+
4 rows in set (0.00 sec) */

-- Truy vấn tất cả cuốn sách được viết bởi Lahiri và được xuất bản trước năm 2000
SELECT * FROM books WHERE author_lname = 'Lahiri' && released_year < 2000;
/*
+---------+-------------------------+--------------+--------------+---------------+----------------+-------+
| book_id | title                   | author_fname | author_lname | released_year | stock_quantity | pages |
+---------+-------------------------+--------------+--------------+---------------+----------------+-------+
|       4 | Interpreter of Maladies | Jhumpa       | Lahiri       |          1996 |             97 |   198 |
+---------+-------------------------+--------------+--------------+---------------+----------------+-------+
1 row in set (0.00 sec) */

-- Truy vấn tất cả cuốn sách có số trang (pages) nằm trong khoảng từ 100 đến 200 trang
SELECT * FROM books WHERE pages BETWEEN 100 AND 200;
/*
+---------+-----------------------------------------------------+--------------+--------------+---------------+----------------+-------+
| book_id | title                                               | author_fname | author_lname | released_year | stock_quantity | pages |
+---------+-----------------------------------------------------+--------------+--------------+---------------+----------------+-------+
|       4 | Interpreter of Maladies                             | Jhumpa       | Lahiri       |          1996 |             97 |   198 |
|      11 | What We Talk About When We Talk About Love: Stories | Raymond      | Carver       |          1981 |             23 |   176 |
|      14 | Cannery Row                                         | John         | Steinbeck    |          1945 |             95 |   181 |
+---------+-----------------------------------------------------+--------------+--------------+---------------+----------------+-------+
3 rows in set (0.01 sec) */

--
SELECT title, author_lname,
CASE
  WHEN title LIKE '%stories%' THEN 'Short Stories'
  WHEN title LIKE '%Just Kids%' THEN 'Memoir'
  WHEN title = 'A Heartbreaking Work of Staggering Genius' THEN 'Memoir'
  ELSE 'Novel' END AS 'Type'
FROM books;