-- Lab 10.3 https://docs.google.com/document/d/1NqtG7ENu6rYkjXwp5AdHUO9SMqfZMIow/edit

create view customer_sale1 as select * from sales s join customers c on c.id = s.customer_id;
-- ERROR 1060 (42S21): Duplicate column name 'id'
/*
-Câu lệnh tạo view trong MySQL gặp lỗi vì bạn đang join bảng `sales` và `customers` trong câu truy vấn SELECT, nhưng không đặt tên cột cụ thể cho các cột được chọn từ các bảng. Khi tạo view, MySQL yêu cầu tên cột được xác định rõ ràng để tạo các cột trong view.

-Để sửa lỗi này, ta cần chỉ định danh sách các cột cụ thể muốn lấy từ bảng `sales` và `customers` trong câu truy vấn SELECT của view. Ví dụ, nếu muốn lấy tất cả các cột từ cả hai bảng, ta có thể thay đổi câu lệnh tạo view như sau:

```sql
CREATE VIEW customer_sale1 AS
SELECT s.*, c.*
FROM sales s
JOIN customers c ON c.id = s.customer_id;
```

-Trong câu lệnh trên, `s.*` và `c.*` đại diện cho tất cả các cột trong bảng `sales` và `customers`, giúp đảm bảo rằng view sẽ có đầy đủ các cột từ cả hai bảng. Tuy nhiên, nếu chỉ muốn lấy một số cột cụ thể, thay thế `s.*` và `c.*` bằng danh sách các cột ta muốn lấy.
*/

create  algorithm=merge view customer_sale2 as select c.id  from sales s join customers c on c.id = s.customer_id;
-- Query OK, 0 rows affected (0.02 sec)

create  algorithm=temptable view customer_sale3 as select c.id  from sales s join customers c on c.id = s.customer_id;
-- Query OK, 0 rows affected (0.00 sec)

create  algorithm=merge view customer_sale4 as select count(*), c.id  from sales s join customers c on c.id = s.customer_id;
-- Query OK, 0 rows affected, 1 warning (0.01 sec)

create  algorithm=undefined view customer_sale5 as select count(*), c.id  from sales s join customers c on c.id = s.customer_id;
-- Query OK, 0 rows affected (0.02 sec)


-- Explain:
--MERGE: Khi thao tác qua view, MySQL sẽ truy vấn trực tiếp đến bảng chính, view chỉ là một trung gian.  
--TEMPTABLE: Khi thao tác qua view, MySQL sẽ truy vấn qua view mà không cần truy vấn đến bảng gốc.  

/*
Trong MySQL, thuật toán được sử dụng trong câu lệnh tạo view có thể được xác định bằng cú pháp `ALGORITHM=algorithm_name`. Dưới đây là một số thuật toán thường được sử dụng trong MySQL:

1. `ALGORITHM=UNDEFINED` (Mặc định):
   - MySQL sẽ chọn thuật toán tối ưu dựa trên tính năng và cấu trúc của câu truy vấn.
   - Đây là lựa chọn đơn giản và cho phép MySQL tự động xác định thuật toán tốt nhất.

2. `ALGORITHM=MERGE`:
   - Thuật toán sáp nhập (merge) sử dụng các câu lệnh SELECT gốc của view và các bảng nguồn để tạo câu lệnh truy vấn tối ưu.
   - Có thể được sử dụng khi câu truy vấn SELECT trong view không chứa các phép toán phức tạp hoặc các chức năng đặc biệt.

3. `ALGORITHM=TEMPTABLE`:
   - Thuật toán tạo một bảng tạm thời (temporary table) và sử dụng nó để đánh giá câu truy vấn SELECT của view.
   - Đây là thuật toán phổ biến nhưng có thể tốn nhiều tài nguyên và thời gian, đặc biệt là khi view có dữ liệu lớn hoặc câu truy vấn SELECT phức tạp.

4. `ALGORITHM=MERGE` hoặc `ALGORITHM=TEMPTABLE`:
   - Khi view chứa UNION, DISTINCT, GROUP BY, HAVING, LIMIT, hoặc các chức năng như các hàm đặc biệt (UDF), các câu lệnh con SELECT có thể được xử lý bằng thuật toán sáp nhập (merge) hoặc tạo bảng tạm thời (temporary table) tùy thuộc vào trường hợp cụ thể.

5. `ALGORITHM=VIEW`:
   - MySQL sẽ tạo một view vật lý mới từ câu truy vấn SELECT của view, và sử dụng view mới này để đánh giá câu truy vấn.
   - Đây là thuật toán phổ biến nhưng có thể tốn nhiều tài nguyên và thời gian, đặc biệt là khi view có dữ liệu lớn hoặc câu truy vấn SELECT phức tạp.

Lưu ý rằng sự lựa chọn của thuật toán có thể ảnh hưởng đến hiệu suất và tài nguyên tiêu thụ của câu truy vấn trên view. Việc chọn thuật toán phù hợp phụ thuộc
*/

-- Performance:
/*
Hiệu năng của từng thuật toán trong MySQL có thể khác nhau và phụ thuộc vào đặc điểm của câu truy vấn và cấu trúc dữ liệu được sử dụng. Dưới đây là một số thông tin tổng quan về hiệu năng của một số thuật toán:

1. `ALGORITHM=UNDEFINED`:
   - Hiệu năng sẽ phụ thuộc vào thuật toán được MySQL tự động chọn dựa trên câu truy vấn và dữ liệu.
   - Có thể đạt hiệu năng tốt nếu MySQL chọn thuật toán phù hợp cho câu truy vấn cụ thể.

2. `ALGORITHM=MERGE`:
   - Thuật toán sáp nhập (merge) thường cho hiệu năng tốt trong các trường hợp đơn giản, khi câu truy vấn SELECT không có các phép toán phức tạp.
   - Nếu câu truy vấn SELECT trong view đơn giản, thuật toán sáp nhập có thể tạo ra câu lệnh truy vấn tối ưu hơn.

3. `ALGORITHM=TEMPTABLE`:
   - Thuật toán tạo bảng tạm thời (temporary table) thường được sử dụng trong các trường hợp phức tạp hơn, khi câu truy vấn SELECT trong view chứa UNION, DISTINCT, GROUP BY, HAVING, LIMIT, hoặc các chức năng đặc biệt.
   - Đôi khi thuật toán tạo bảng tạm thời có thể tốn nhiều tài nguyên và thời gian hơn, đặc biệt là khi view có dữ liệu lớn hoặc câu truy vấn SELECT phức tạp.

4. `ALGORITHM=VIEW`:
   - Thuật toán tạo view vật lý mới có thể được sử dụng trong các trường hợp phức tạp, khi view chứa các phép toán phức tạp và câu truy vấn SELECT phức tạp.
   - Tuy nhiên, thuật toán tạo view vật lý mới có thể tốn nhiều tài nguyên và thời gian hơn, đặc biệt là khi view có dữ liệu lớn hoặc câu truy vấn SELECT phức tạp.

Lưu ý rằng hiệu năng của từng thuật toán có thể bị ảnh hưởng bởi nhiều yếu tố khác nhau, bao gồm kích thước dữ liệu, chỉ mục, số lượng bảng liên kết, phức tạp của câu truy vấn, và cấu hình hệ thống. Để đạt được hiệu suất tối ưu, cần phải xem xét các yếu tố này và*/