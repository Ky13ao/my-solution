-- Lab 6.1 Tinh chỉnh mệnh đề SELECT: https://docs.google.com/document/d/1NILAtglv2IkWj1OfT0zDaljwYj5AGkYJ/edit

-- Yêu cầu 1: Viết truy vấn để tìm cuốn sách có số pages lớn nhất
SELECT * FROM books ORDER BY pages DESC LIMIT 1;
/*
+---------+-------------------------------------------+--------------+--------------+---------------+----------------+-------+
| book_id | title                                     | author_fname | author_lname | released_year | stock_quantity | pages |
+---------+-------------------------------------------+--------------+--------------+---------------+----------------+-------+
|       7 | The Amazing Adventures of Kavalier & Clay | Michael      | Chabon       |          2000 |             68 |   634 |
+---------+-------------------------------------------+--------------+--------------+---------------+----------------+-------+
1 row in set (0.01 sec)*/

-- Yêu cầu 2: Viết truy vấn để hiện thị title và released_year của 3 cuốn sách gần thời điểm hiện tại nhất
SELECT title, released_year FROM books ORDER BY released_year DESC LIMIT 3;
/*
+----------------------------------+---------------+
| title                            | released_year |
+----------------------------------+---------------+
| Norse Mythology                  |          2016 |
| The Circle                       |          2013 |
| A Hologram for the King: A Novel |          2012 |
+----------------------------------+---------------+
3 rows in set (0.00 sec)*/

-- Yêu cầu 3 : Viết truy vấn để hiển thị title và author_lname của tất cả các cuốn sách có author_lname chứa ký tự khoảng trắng (' ')
SELECT title, author_lname FROM books WHERE author_lname LIKE "% %";

-- Yêu cầu 4: Viết truy vấn để hiển thị title, released_year và stock của 3 cuốn sách có stock nhỏ nhất
SELECT title, released_year, stock_quantity FROM books ORDER BY stock_quantity ASC LIMIT 3;

-- Yêu cầu 5: Viết truy vấn để hiển thị title, author_lname và sắp xếp theo thứ tự ưu tiên là author_lname sau đó đến title
SELECT title, author_lname FROM books ORDER BY author_lname, title ASC;


