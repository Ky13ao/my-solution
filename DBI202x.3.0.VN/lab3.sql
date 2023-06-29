-- Lab 3.1 : https://docs.google.com/document/d/1NPpRROOR0KWdOKVGidE1xA5gHH6qRPdL/edit

CREATE TABLE people (
  first_name VARCHAR(20),
  last_name VARCHAR(20),
  age INT
);

INSERT INTO people(first_name, last_name, age)
VALUES ('Tina', 'Belcher', 13),
  ('Bob', 'Belcher', 42),
  ('Linda', 'Belcher', 45),
  ('Phillip', 'Frond', 38),
  ('Calvin', 'Fischoeder', 70);

SELECT * FROM people;

DROP TABLE people;

-- Lab 3.2 *: https://docs.google.com/document/u/1/d/1u5OqA18vpD7V2lhyscSHJp9W30fBqXVd/edit

CREATE TABLE unique_cats (
  cat_id INT NOT NULL PRIMARY KEY,
  name VARCHAR(100),
  age INT
);

CREATE TABLE unique_cats2 (
  cat_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  age INT
);


CREATE TABLE employees (
  cat_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  middle_name VARCHAR(255),
  current_status VARCHAR(255) DEFAULT 'employed'
);

INSERT INTO 
employees ( first_name, last_name, age) 
VALUES
('Dora', 'Smith', 58);

-- Lab 3.3  : https://docs.google.com/document/d/1A2-fdjTtJpgyYYQxEmnhsGq9SEOfc9Oo/edit

CREATE TABLE cats (
  cat_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100),
  breed VARCHAR(100),
  age INT
);

INSERT INTO 
cats(name, breed, age)
VALUES
('Ringo', 'Tabby', 4),
('Cindy', 'Maine Coon', 10),
('Dumbledore', 'Maine Coon', 11),
('Egg', 'Persian', 4),
('Misty', 'Persian', 4),
('George Michael', 'Ragdoll', 9),
('Jackson', 'Sphynx', 7);

SELECT cat_id FROM cats;
SELECT name, breed FROM cats;
SELECT name, age FROM cats;
SELECT cat_id AS id FROM cats;
SELECT name AS 'cat name', breed AS 'kitty breed' FROM cats;

-- Lab 3.4 : https://docs.google.com/document/d/18KOZsvSdbr9wD8whoLVZUT9UtGl5QIug/edit

UPDATE cats SET name='jack' WHERE name='jackson';
UPDATE cats SET name='Bitish Shorthair' WHERE name='Ringo';
UPDATE cats SET age=12 WHERE breed='Maine Coon”';
DELETE FROM cats WHERE age=4;
DELETE FROM cats WHERE cat_id=age;
TRUNCATE TABLE cats;

-- Lab 3.5 : https://docs.google.com/document/d/1bblDMGb3V9ULWdI6-RImm5ZUsHkzGNCm/edit

CREATE DATABASE shirts_db;
USE shirts_db;
CREATE TABLE shirts(
  shirt_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  article VARCHAR(100),
  color VARCHAR(100),
  shirt_size VARCHAR(100),
  last_worn INT
);
INSERT INTO shirts(article, color, shirt_size, last_worn)
VALUES
('t-shirt', 'white', 'S', 10),
('t-shirt', 'green', 'S', 200),
('polo shirt', 'black', 'M', 10),
('tank top', 'blue', 'S', 50),
('t-shirt', 'pink', 'S', 0),
('polo shirt', 'red', 'M', 5),
('tank top', 'white', 'S', 200),
('tank top', 'blue', 'M', 15);
SELECT * FROM shirts;
SHOW TABLES;
INSERT INTO shirts(article, shirt_size, last_worn)
VALUES ('polo shirt', 'M', 50);
SELECT article, color FROM shirts;/
SELECT article, color, shirt_size, last_worn FROM shirts WHERE shirt_size='M';
UPDATE shirts SET shirt_size ='L' WHERE article='polo shirt';
DELETE FROM shirts WHERE last_worn = 200;

-- Lab 3.7
INSERT INTO Customers (CustomerName, City, Country)
SELECT SupplierName, City, Country FROM Suppliers
WHERE Country='Germany';