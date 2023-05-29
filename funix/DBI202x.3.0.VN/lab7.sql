-- Lab7.1: https://docs.google.com/document/d/1yMXJ_OO_pEuvbXbhIRXU-3e3jK55WsEy/edit

-- Yêu cầu 1: Viết truy vấn để đếm số lượng cuốn sách trong bảng books	
SELECT COUNT(*) number_book FROM books;

-- Yêu cầu 2: Viết truy vấn để tìm số lượng cuốn sách được xuất bản trong mỗi năm	
SELECT COUNT(*) number_book, released_year FROM books GROUP BY released_year;

-- Yêu cầu 3: Viết truy vấn để tìm tổng số lượng cuốn sách tồn kho (sử dụng cột stock_quantity)	
SELECT SUM(stock_quantity) sum_stock FROM books;

-- Yêu cầu 4: Viết truy vấn để tìm số năm trung bình xuất bản các cuốn sách của mỗi tác giả	
SELECT AVG(released_year) avg_released_year FROM books GROUP BY author_lname;

-- Yêu cầu 5: Viết truy vấn để tìm tên đầy đủ của tác giả đã viết cuốn sách có số trang nhiều nhất
SELECT CONCAT_WS(' ',author_fname, author_lname) fullname, pages FROM books WHERE pages = (
SELECT MAX(pages) FROM books);