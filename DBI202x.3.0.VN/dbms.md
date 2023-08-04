# Relational Database Management Systems

RDBMS

## MySQL - open source

### Transactions

- 4 Đặc điểm của transaction:

  - Tính nguyên tố (**Atomicity**)
    Một transaction bao gồm các hoạt động khác nhau phải thỏa mãn điều kiện
    - tất cả thành công
    - hoặc không có hoạt động nào thành công
  - Tính nhất quán (**Consitency**)
    Trạng thái bất biến về dữ liệu có nghĩa là dữ liệu luôn được bảo toàn
    Nếu có lỗi quay về trạng thái trước đó
  - Tính độc lập (**Isolation**)
    Một transaction đang được thực thi và chưa được xác nhận phải đảm bảo tính độc lập với các transaction khác
  - Tính bền vững (**Durability**)
    Khi một transaction được commit thành công dữ liệu sẽ được lưu lại 1 cách chuẩn xác

- có 4 kiểu lock dữ liệu:

  - **Table locking**:
    Transaction `T1` đang dùng _bảng A_ thì các transaction khác không thể sử dụng _bảng A_
  - **Row level locking**:
    Transaction `T1` sử dụng hàng dữ liệu `r` trong _bảng A_
    thì các transaction khác sẽ không thể sử dụng (update/delete...) hàng `r`
  - **Read lock (shared)**
    Tất cả transaction đều không thể ghi dữ liệu được vào bảng kể cả transaction đang sử dụng bảng
  - **Write lock (exclusive)**
    Transaction đang sử dụng bảng dữ liệu có thể đọc và ghi dữ liệu vào bảng
    nhưng các transaction khác ko thể ghi dữ liệu vào bảng mà chỉ có thể đọc dữ liệu từ bảng

- Isolation của transaction sẽ có 4 cấp độ:
  - **Read uncommited**
    1 transaction đọc dữ liệu từ 1 transaction khác dù chưa hoàn thành
  - **Read committed** (cấp độ mặc định)
    Chỉ có thể đọc được transaction khác khi nó đã được thực thi hoàn tất.
    Chúng ta có thể tránh được _Dirty Read_ và _Dirty Write_
    nhưng các Transaction sẽ phải chờ nhau làm hệ thống chậm đi.
  - **Repeatable read**
    Gần giống _Read committed_
    Tại mức độ này, transaction ko đọc hoặc ghi đè dữ liệu từ 1 transaction đang tiến hành cập nhật trên bảng ghi đó
  - **Serializable**
    Level cao nhất của Isolation
    Khi transation thực thi nó sẽ lock tất cả bản ghi liên quan và sẽ unlock khi dữ liệu rollback hoặc được commit

#### `SAVEPOINT`

#### `ROLLBACK`

### Proc & Func

#### Stored Procedure

- cú pháp 1:
  > ```sql
  > DELIMITER $$
  > CREATE PROCEDURE spName()
  > BEGIN
  >   SELECT * FROM <tablename>; -- đây là câu lệnh truy vấn
  > END
  > DELIMITER;
  > ```
- cú pháp 2:

  > ```sql
  > DELIMITER //
  > CREATE PROCEDURE spName()
  > BEGIN
  >   SELECT * FROM <tablename>; -- đây là câu lệnh truy vấn
  > END //
  > DELIMITER;
  > ```

- `DELIMITER` là lệnh có tác dụng để khai báo mở đầu và kết thúc của 1 Stored Procedure
- để gọi 1 thủ tục, ta sẽ sử dụng lệnh `CALL`:
  > `CALL spName(parameter);`

#### Function

- Tương tự như Stored Procedure nhưng có trả về giá trị
- trong hệ thống có các function như `MAX()`, `MIN()`

- ví dụ

```sql
SET GLOBAL log_bin_trust_function_creators = 1;
delimiter $$
create function test_function(threshhold int) returns int
-- function tìm location_id lớn nhất bé với điều kiện department_id < @threshhold tham số truyền vào
begin
 declare result int;
    select max(location_id) from departments where department_id < threshhold into result;
    return result;
end$$
delimiter ;
```

- để gọi 1 function ta sử dụng lệnh `SELECT`: `select test_function(100);`

#### `DEFINER` - Quyền procedure

- cú pháp
  > ```sql
  > DELIMITER  $$
  > CREATE definer=<user>@<serveraddress> PROCEDURE ShowCustomer() --user1@localhost là ví dụ cho user1 ở server localhost
  > SQL SECURITY DEFINER
  > BEGIN
  > SELECT * FROM <tablename>;
  > END$$
  > DELIMITER ;
  > ```

#### Vòng lặp và con trỏ

##### `WHILE` loop

- Cú pháp

```sql
WHILE <bieu_thuc_so_sanh> DO
  <cac_phep_tinh>
END WHILE;
```

- Ví dụ

```sql
DELIMITER $$
CREATE PROCEDURE whiledemo()
BEGIN
  DECLARE count int DEFAULT 0;
  DECLARE numbers varchar(30) DEFAULT "";
  WHILE count < 10 do
    SET numbers:= concat(numbers, count);
    SET count:= count + 1;
  END WHILE;
  SELECT numbers;
END$$
DELIMITER;
```

- ket qua `CALL whiledemo();` : 0123456789 (string)

##### `LOOP` loop

- chúng phải đặt tên cho LOOP và điều kiện để LEAVE the loop

- ví dụ

```sql
USE test;
DELIMITER $$
CREATE PROCEDURE loopdemo()
BEGIN
DECLARE count int DEFAULT 0;
DECLARE numberlist varchar(30) DEFAULT "";
the_loop: LOOP
 if count = 10 then leave the_loop;
    end if;
    set numberlist := concat(numberlist, ". ", count);
    set count := count + 1;
END LOOP;
SELECT numberlist;
END$$
DELIMITER ;
```

- ket qua `CALL loopdemo();` : . 0. 1. 2. 3. 4. 5. 6. 7. 8. 9 (string)

##### `CURSOR` con trỏ

- 3 thuộc tính của con trỏ:

  - **Read-only (chỉ đọc)**
    có nghĩa là chúng ta ko thể thay đổi giá trị
  - **Non-scrollable (Không thể quay lại)**
    con trỏ chỉ đi theo 1 hướng
    không thể bỏ qua hay quay lại những dòng đã duyệt trong tập kết quả
  - **Sensitive**
    tránh cập nhật bảng dữ liệu khi đang mở con trỏ trên chính bảng dữ liệu đó
    nếu ko rất có thể xảy ra xung đột trên hệ thống

- quy trình sử dụng:
  1. Khai báo con trỏ:
     `DECLARE <ten_con_tro> CURSOR FOR <SELECT_statement>;`
  2. Mở con trỏ để sử dụng:
     `OPEN <ten_con_tro>;`
  3. Lấy ra một dòng để xử lý và chuyển con trỏ sang dòng kế tiếp:
     `FETCH <ten_con_tro> INTO <bien_luu_tru>;`
  4. Đóng con trỏ và giải phóng bộ nhớ:
     `CLOSE <ten_con_tro>;`

### TRIGGER

- TRIGGER được kích hoạt khi một hành động xác định được thực thi cho bảng
- Thường được ứng dụng để: kiểm tra dữ liệu, đồng bộ dữ liệu, đảm bảo các mối quan hệ được đồng nhất
- Ưu điểm:
  - Dễ dàng kiểm tra tính toàn vẹn CSDL. Trigger có thể bắt lỗi nghiệp vụ (business logic) ở mức CSDL.
  - Có thể dùng TRIGGER là một cách khác để thay thế việc thực hiện những công việc hẹn giờ theo lịch.
  - Trigger rất hiệu quả khi được sử dụng để kiểm soát những thay đổi của dữ liệu trong bảng.
- Nhược điểm:
  - Trigger chỉ là một phần mở rộng của việc kiểm tra tính hợp lệ của dữ liệu chứ không thay thế được hoàn toàn công việc này.
  - Trigger hoạt động ngầm ở trong CSDL, ko hiển thị ở tầng giao diện. Do đó, khó chỉ ra được điều gì xảy ra trong CSDL.
  - Trigger sẽ được gọi bất cứ khi nào ở bảng liên kết có một hành động thay đổi dữ liệu. Do đó có thể làm hệ thống chạy chậm
- Giới hạn:
  - Không thể gọi thủ tục từ TRIGGER
  - Không thể tạo ra TRIGGER theo dõi bảng ảo hay bảng tạm (VIEW)
  - Không thể sử dụng transaction trong TRIGGER
  - TRIGGER không cho phép sử dụng lệnh RETURN
  - Sử dụng TRIGGER sẽ làm ảnh hưởng đến bộ nhớ tạm dành cho lệnh truy vấn
  - Tất cả các TRIGGER của 1 cơ sở dữ liệu không được tên
- cú pháp:
  > ```sql
  > DELIMITER $$
  > CREATE TRIGGER <ten_trigger>
  > {BEFORE | AFTER} {INSERT | UPDATE| DELETE }
  > ON <ten_bang> FOR EACH ROW
  > BEGIN
  > <noi_dung_trigger>;
  > END $$
  > DELIMITER ;
  > ```

### INDEX

- là chỉ mục dùng để tìm các hàng có giá trị cột cụ thể một cách nhanh chóng.
  không có chỉ mục, MySQL phải bắt đầu với hàng đầu tiên và sau đó đọc qua toàn bộ bảng để tìm các hàng có liên quan.
  bảng càng lớn, chi phí này càng cao
  nếu bảng có chỉ mục cho các cột được đề cập,
  mysql có thể nhanh chóng xác định vị trí cần tìm ở giũa tập dữ liệu mà ko cần phải xem tất cả dữ liệu
  điều này nhanh hơn nhiều so với đọc từng hàng một cách tuần tự
- thực chất INDEX cũng là 1 bảng, bảng này đặc biệt ở chỗ có các key để trỏ đến từng bảng ghi cụ thể của các bảng
- index giúp tăng tốc độ tìm kiếm
- tuy nhiên, nhược điểm của INDEX là phải tạo 1 bảng để chứa INDEX, đòi hỏi hệ thống phải thêm quá trình tính toán
- không nên đánh INDEX các cột hay được INSERT, UPDATE
  vì khi INSERT hoặc UPDATE ngoài việc thêm mới hoặc thay đổi giá trị cho một bảng thì hệ thống cũng phải thêm mới hoặc thay đổi giá trị của bảng INDEX
- những cột hay được sử dụng để tìm kiếm thì nên đánh INDEX bởi vì sẽ làm tăng tốc độ tìm kiếm
- 3 kiểu cấp INDEX:
  - B-Tree
    Loại index default khi ko được chỉ định
    Độ phức tạp O(log(n))
    - dữ liệu được lưu trữ theo dạng tree, có root, branch, leaf
    - cách sắp xếp ko theo dạng nhị phân tìm kiếm vì số lá của mỗi node ko bị giới hạn là 2
    - cấu trúc chỉ mục cơ bản cho hầu hết các công cụ lưu trữ MySQL
    - mỗi node trong B-Tree có số giá trị (key) từ d đến 2d
    - các giá trị của mỗi node sẽ được sắp xếp tăng dần từ trái qua phải
    - mỗi node có từ 0 đến 2d+1 node code
    - mỗi node được đính kèm từ trước, sau hoặc giữa các giá trị
    - các giá trị trong B-Tree được sắp xếp tương tự như các giá trị trong cây tìm kiếm nhị phân
    - các node con bên trái giá trị 'X' có giá trị nhỏ hơn 'X', các node con bên phải có giá trị lớn hơn 'X'
    - Btree là 1 cây cân bằng tức là tất cả các nhánh của cây sẽ có cùng chiều dài
    - để tìm kiếm trong B-Tree trước tiên chúng ta sẽ kiểm tra giá trị đó có trong node gốc hay ko, nếu ko thì sẽ chọn node con thích hợp
      > ```sql
      > -- cú pháp:
      > -- Tạo index
      > CREATE INDEX ten_index ON ten_bang(cot1, cot2, ...) USING BTREE;
      > -- alter index
      > ALTER TABLE ten_bang ADD INDEX ten_index(cot1, cot2, ...) USING BTREE;
      > -- tao index khi tao bang
      > CREATE TABLE test(
      >   id INT NOT NULL,
      >   last_name CHAR(30) NOT NULL,
      >   first_name CHAR(30) NOT NULL,
      >   PRIMARY KEY (id),
      >   INDEX name (last_name,first_name) USING BTREE
      > );
      > -- xoa index
      > DROP INDEX ten_index ON ten_bang;
      > ```
    - Storage Enginee hỗ trợ: InnoDB, MyISAM, MEMORY/ HEAP, NDB
  - Hash
    Hash index sử dụng kỹ thuật băm để tạo bảng index
    Độ phức tạp O(1)
    > ```sql
    > -- cú pháp:
    > -- Tạo index
    > CREATE INDEX ten_index ON ten_bang(cot1, cot2, ...) USING HASH;
    > -- alter index
    > ALTER TABLE ten_bang ADD INDEX ten_index(cot1, cot2, ...) USING HASH;
    > -- tao index khi tao bang
    > CREATE TABLE test(
    >   id INT NOT NULL,
    >   last_name CHAR(30) NOT NULL,
    >   first_name CHAR(30) NOT NULL,
    >   PRIMARY KEY (id),
    >   INDEX name (last_name,first_name) USING HASH
    > );
    > -- xoa index
    > DROP INDEX ten_index ON ten_bang;
    > ```
    - Storage Enginee hỗ trợ: MEMORY/ HEAP, NDB
  - R-Tree
    Được sử dụng cho các dạng Spatial data và thường ít gặp
- các cột là PRIMARY KEY hoặc UNIQUE khi tạo sẽ mặc định luôn được MySQL đánh INDEX BTREE

## SQL Server - license
