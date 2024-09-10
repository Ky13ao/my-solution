MySQL Interview Question

- MySQL là gì và tại sao nó được sử dụng rộng rãi?
  > MySQL là một hệ thống quản lý dữ liệu mã nguồn mở. Nó được sử dụng vì tính nhất quán, hiệu suất cao, khả năng mở rộng, khả năng tương thích đa nền tảng và cộng đồng hỗ trợ lớn. Sự phổ biến của MySQL cũng xuất phát từ việc nó không tốn chi phí, dễ cài đặt và sử dụng, có khả năng quản lý các dự án cả nhỏ và lớn
- Khác nhau giữa MySQL và SQL Server là gì?
  > MySQL và SQL Server đề là hệ thống quản trị cơ sở dữ liệu.
  > MySQL hiện tại được quản lý bởi Oracle và là mã nguồn mở còn SQL Server thì được phát triển bởi Microsoft và là 1 DBMS thương mại.
  > 2 hệ thống này có các tính năng và tùy chọn quản lý riêng, phụ thuộc vào mục tiêu và nhu cầu của dự án
- Khái niệm về cơ sở dữ liệu quan hệ và hệ quản trị cơ sở dữ liệu quan hệ (RDBMS).
  >
- Các loại kiểu dữ liệu cơ bản trong MySQL và ứng dụng của chúng.

  > - INT là dạng lưu trữ số nguyên có bộ nhớ 32 bit và thường được lưu trữ những thuộc tính số đếm, tuổi
  > - VARCHAR là dạng lưu trữ chuỗi với độ dài được định nghĩa bởi lập trình viên thường được lưu trữ thuộc tính tên, từ khóa
  > - DATE là dạng lưu trữ ngày, tháng, năm
  > - TIME là dạng lưu trữ giờ, phút, giây
  > - DATETIME là lưu trữ cả DATE và TIME
  > - BIT là dạng lưu trữ logic đúng/ sai

- Khái niệm về khóa chính (Primary Key) và khóa ngoại (Foreign Key). Sự khác nhau giữa chúng.

  > - Khóa chính là 1 hoặc 1 tập hợp thuộc tính đảm bảo tính duy nhất trong bảng dùng để xác định 1 bản ghi (1 dòng) trong bảng
  > - Khóa ngoại là 1 cột hoặc 1 tập hợp cột trong bảng tham chiếu để khóa chính của bảng khác, dùng để xác định mối liên quan của bản ghi (trong bảng) với các mối liên quan của bản ghi đó

- Khái niệm về chỉ số (Index) trong MySQL và lợi ích của việc sử dụng chỉ số.

  > - chỉ mục Index để đánh dấu lại thứ tự các dòng trong bảng giúp tối ưu tốc độ tìm kiếm và sắp xếp trong bảng

- Các câu lệnh SQL cơ bản như SELECT, INSERT, UPDATE, DELETE và trình bày cách sử dụng chúng.

  > - câu lệnh SELECT dùng để thực thi một tác vụ liệt kê
  > - câu lệnh SELECT thường được dùng chung với WHERE để lọc các bản ghi giúp chúng ta nhận được những bản ghi mong muốn
  > - câu lệnh INSERT được dùng để thêm 1 hoặc nhiều bản ghi vào bảng
  > - câu lệnh UPDATE được update các bản ghi có điều kiện định nghĩa bởi WHERE, DELETE được dùng để loại bỏ các bản ghi trong bản với điều kiện định nghĩa sau WHERE

- Cách tạo bảng (CREATE TABLE) trong MySQL, bao gồm định nghĩa các cột, khóa chính và khóa ngoại.
- Phân biệt giữa TRUNCATE và DELETE trong MySQL.
  > TRUNCATE và DELETE thường được dùng để xóa dòng trong bảng
- Câu lệnh SQL ORDER BY dùng để làm gì và cách sử dụng nó.
  > Câu lệnh ORDER BY dùng để sắp xếp bảng theo các tên cột với thứ tự lớn dần, nếu muốn nhỏ dần thì thêm DESC
  > cách sử dụng SELECT ten, tuoi FROM nhan_vien ORDER BY tuoi DESC;
- Câu lệnh SQL GROUP BY và HAVING dùng để làm gì và cách sử dụng chúng.
  > Câu lệnh GROUP BY dùng để nhóm các dữ liệu và thực hiện tính toán trên các nhóm đó với các hàm aggregate như SUM, AVERAGE, COUNT, hàm HAVING cũng giống như hàm WHERE nhưng WHERE để đặt điều kiện cho bản ghi còn HAVING thì đặt điều kiện cho từng GROUP
- Cách tạo các ràng buộc dữ liệu như NOT NULL, UNIQUE, CHECK và DEFAULT trong MySQL.
  > để tạo ràng buộc trong bảng dữ liệu ta có 2 cách:
  >
  > - tạo cùng lúc với bảng
  >
  > ```sql
  >   CREATE TABLE `table` (
  >     `id` int(10) NOT NULL UNIQUE AUTO_INCREMENT,
  >     `name` varchar(50),
  >     CONSTRAINT chk_name_longer_than_6_chrs CHECK(CHAR_LENGTH(`name`)>6));
  > ```
  >
  > - ALTER bảng với constraint
  >
  > ```sql
  >   ALTER TABLE `table`
  >   ADD CONSTRAINT default_name `name` DEFAULT `SYSTEM`;
  > ```
- Câu lệnh SQL JOIN và các loại JOIN (INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN) trong MySQL.
- Cách thực hiện gộp bảng (Table Join) và cách xử lý khi có trùng lặp dữ liệu trong MySQL.
- Các hàm cơ bản trong MySQL như COUNT, SUM, AVG, MIN, MAX và cách sử dụng chúng.
- Cách tạo View trong MySQL và ứng dụng của việc sử dụng View.
- Cách sử dụng TRIGGER để thực hiện các hành động tự động trong MySQL.
- Khái niệm về chuẩn hóa dữ liệu (Normalization) và lợi ích của việc thực hiện chuẩn hóa.
  > Chuẩn hóa dữ liệu là những giải pháp để giảm dữ liệu dư thừa trong các bảng, mục đích của việc chuẩn hóa dữ liệu là tối ưu hóa bảng dữ liệu giúp hoạt động nhanh hơn tránh việc dư thừa dữ liệu
- Sự khác nhau giữa các chuẩn hóa NF1, NF2 và NF3 trong cơ sở dữ liệu.
  > - Chuẩn hóa NF1 giúp chúng ta có 1 bảng dữ liệu không có bất kỳ thuộc tính đa trị hay phức hợp nào
  > - Chuẩn hóa NF2 giúp chúng ta có 1 bảng dữ liệu mà khóa ko chứa các thuộc tính ko khóa
  > - Chuẩn hóa NF3 giúp chúng ta có được bảng dữ liệu mà các thuộc tính không khóa ko suy dẫn ra thuộc tính không khóa khác
- Cách sử dụng INDEX để cải thiện hiệu suất truy vấn trong MySQL và điểm cần lưu ý khi tạo chỉ số.
  > Để tạo ra chỉ mục INDEX ta dùng câu lệnh `CREATE INDEX column_name ON table_name`
  > không nên đánh INDEX trên các cột hay dùng lệnh INSERT UPDATE
