-- Lab4.1: https://docs.google.com/document/d/1f_QrxKLYR_9xkBEXG6hDVH0IUXWUnONf/edit

CREATE DATABASE book_shop;
USE book_shop;
SOURCE book_data.sql;
SELECT * FROM books;

-- Lab4.2: https://docs.google.com/document/d/1jbHhMOR61CoD79D_r3SdN6et5UrG3tAE/edit
SELECT CONCAT(author_fname, author_lname) AS 'full_name' FROM books; --> fname lname
SELECT CONCAT_WS(' - ',author_fname, author_lname) AS 'full_name' FROM books; --> fname - lname
SELECT SUBSTRING('data analyst', 6, 7) s; --> analyst
SELECT REPLACE('data analyst', 'analyst', 'science') s; --> data science
SELECT REVERSE('data analyst'); --> tsylana atad
SELECT CHAR_LENGTH('database') l; --> 8
SELECT UPPER('database') s; --> DATABASE
SELECT UPPER(b.title) upperTitle FROM books b;
SELECT LOWER('DATABASE') s; --> database
SELECT LOWER(b.title) lowerTitle FROM books b;
