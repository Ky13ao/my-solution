-- Lab9.1 https://docs.google.com/document/d/16EUwOIESlXDbjlXPc75sBVzBt_bndApW/edit

-- Yêu cầu 1: Tạo bảng dữ liệu	
CREATE TABLE students(
  id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(150) NOT NULL
);
CREATE TABLE papers(
  id INT PRIMARY KEY AUTO_INCREMENT,
  student_id INT,
  title VARCHAR(150),
  grade INT,
  FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Yêu cầu 2: Insert dữ liệu vào các bảng students và papers	
INSERT INTO students (first_name) VALUES 
('Caleb'), ('Samantha'), ('Raj'), ('Carlos'), ('Lisa');

INSERT INTO papers (student_id, title, grade ) VALUES
(1, 'My First Book Report', 60),
(1, 'My Second Book Report', 75),
(2, 'Russian Lit Through The Ages', 94),
(2, 'De Montaigne and The Art of The Essay', 98),
(4, 'Borges and Magical Realism', 89);

-- Yêu cầu 3: Viết truy vấn tất cả bản ghi (các hàng dữ liệu) của bảng students và papers:	
SELECT id, first_name FROM students;
SELECT student_id, title, grade FROM papers;

-- Yêu cầu 4: Sử dụng phép các Join hợp lý của bảng students và papers để tạo được kết quả như dưới đây
SELECT s.first_name first_name, p.title title, p.grade grade 
FROM students s
LEFT OUTER JOIN papers p ON s.id=p.student_id;

SELECT s.first_name first_name, IFNULL(title, 'MISSING'), IFNULL(grade, 0)
FROM students s
LEFT OUTER JOIN papers ON s.id=student_id;

SELECT 
s.first_name first_name, 
(SELECT IFNULL(AVG(p.grade), 0) FROM papers p WHERE p.student_id=s.id) average
FROM students s ORDER BY average DESC;

SELECT 
s.first_name first_name, 
(SELECT IFNULL(AVG(p.grade), 0) FROM papers p WHERE p.student_id=s.id) average,
CASE
WHEN (SELECT IFNULL(AVG(p.grade), 0) FROM papers p WHERE p.student_id=s.id)>=80 THEN 'PASSING'
ELSE 'FAILING'
END passing_status
FROM students s ORDER BY average DESC;

-- Lab 9.2 https://docs.google.com/document/d/1BKbAfHeXutZVIg4w5wtOZS7jMgBR2gX9/edit

-- Yêu cầu 1: Tạo bảng dữ liệu
CREATE TABLE Reviewers(
  id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(100),
  last_name VARCHAR(100)
);
CREATE TABLE Series (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  released_year YEAR(4),
  genre VARCHAR(100)
);
CREATE TABLE Reviews(
  id INT PRIMARY KEY AUTO_INCREMENT,
  rating FLOAT,
  series_id INT, 
  FOREIGN KEY (series_id) REFERENCES Series(id),
  reviewer_id INT, 
  FOREIGN KEY (reviewer_id) REFERENCES Reviewers(id)
);
-- Yêu cầu 2: Insert dữ liệu vào các bảng Reviewers, Series và Reviews
INSERT INTO Series (title, released_year, genre) VALUES
  ('Archer', 2009, 'Animation'),
  ('Arrested Development', 2003, 'Comedy'),
  ("Bob's Burgers", 2011, 'Animation'),
  ('Bojack Horseman', 2014, 'Animation'),
  ("Breaking Bad", 2008, 'Drama'),
  ('Curb Your Enthusiasm', 2000, 'Comedy'),
  ("Fargo", 2014, 'Drama'),
  ('Freaks and Geeks', 1999, 'Comedy'),
  ('General Hospital', 1963, 'Drama'),
  ('Halt and Catch Fire', 2014, 'Drama'),
  ('Malcolm In The Middle', 2000, 'Comedy'),
  ('Pushing Daisies', 2007, 'Comedy'),
  ('Seinfeld', 1989, 'Comedy'),
  ('Stranger Things', 2016, 'Drama');


INSERT INTO Reviewers (first_name, last_name) VALUES
  ('Thomas', 'Stoneman'),
  ('Wyatt', 'Skaggs'),
  ('Kimbra', 'Masters'),
  ('Domingo', 'Cortes'),
  ('Colt', 'Steele'),
  ('Pinkie', 'Petit'),
  ('Marlon', 'Crafford');
  

INSERT INTO Reviews(series_id, reviewer_id, rating) VALUES
  (1,1,8.0),(1,2,7.5),(1,3,8.5),(1,4,7.7),(1,5,8.9),
  (2,1,8.1),(2,4,6.0),(2,3,8.0),(2,6,8.4),(2,5,9.9),
  (3,1,7.0),(3,6,7.5),(3,4,8.0),(3,3,7.1),(3,5,8.0),
  (4,1,7.5),(4,3,7.8),(4,4,8.3),(4,2,7.6),(4,5,8.5),
  (5,1,9.5),(5,3,9.0),(5,4,9.1),(5,2,9.3),(5,5,9.9),
  (6,2,6.5),(6,3,7.8),(6,4,8.8),(6,2,8.4),(6,5,9.1),
  (7,2,9.1),(7,5,9.7),(8,4,8.5),(8,2,7.8),(8,6,8.8),
  (8,5,9.3),(9,2,5.5),(9,3,6.8),(9,4,5.8),(9,6,4.3),
  (9,5,4.5),(10,5,9.9),(13,3,8.0),(13,4,7.2),
  (14,2,8.5),(14,3,8.9),(14,4,8.9);

-- Yêu cầu 3: Viết truy vấn tất cả bản ghi (các hàng dữ liệu) của bảng reviewers, series và reviews:
SELECT * FROM Reviewers;
SELECT * FROM Series;
SELECT * FROM Reviews;

-- Yêu cầu 4: Sử dụng phép join bảng series và reviews
SELECT s.title title, ROUND(rating, 1) rating
FROM Reviews
INNER JOIN Series s ON s.id = series_id;

-- Yêu cầu 5: Viết truy vấn để tính trung bình rating của mỗi series trong bảng series
SELECT s.title title, ROUND(AVG(rating), 5) avg_rating
FROM Series s
INNER JOIN Reviews r ON s.id=r.series_id
GROUP BY s.title
ORDER BY rating;

-- Yêu cầu 6: Viết truy vấn để tìm trung bình rating của mỗi thể loại (genre) trong bảng series
SELECT s.genre genre, ROUND(AVG(r.rating), 2) avg_rating
FROM Series s
INNER JOIN Reviews r ON s.id=r.series_id
GROUP BY s.genre;

-- Yêu cầu 7: Viết truy vấn để tính trung bình rating của mỗi người review trong bảng reviewers
SELECT u.first_name, u.last_name, ROUND(rating, 1) rating
FROM Reviews
INNER JOIN Reviewers u ON u.id = reviewer_id;

-- Yêu cầu 8: Viết truy vấn để tìm những series chưa được review trong bảng series	
SELECT s.title unreviewed_series
FROM Series s
LEFT JOIN Reviews ON series_id=s.id
GROUP BY s.title
HAVING count(series_id) = 0;

-- Yêu cầu 9: Viết truy vấn để thống kê số review của mỗi người reviewers	
SELECT u.first_name, u.last_name, 
COUNT(r.id) count, 
ROUND(IFNULL(MIN(r.rating), 0), 1) MIN, 
ROUND(IFNULL(MAX(r.rating), 0), 1) MAX, 
ROUND(IFNULL(AVG(r.rating),0),1) AVG, CASE WHEN COUNT(r.id)>0 THEN 'ACTIVE' ELSE 'INACTIVE' END AS STATUS
FROM Reviewers u
LEFT JOIN Reviews r ON r.reviewer_id=u.id
GROUP BY u.first_name, u.last_name
ORDER BY STATUS ASC;

-- Yêu cầu 10: Viết truy vấn để join ba bảng reviewers, reviews, serie
SELECT s.title, r.rating, CONCAT_WS(' ', u.first_name, u.last_name) reviewer
FROM Reviews r
INNER JOIN Series s ON s.id=r.series_id
INNER JOIN Reviewers u ON u.id=r.reviewer_id
ORDER BY s.title;
