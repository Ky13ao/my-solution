# Relational Database Management Systems

RDBMS

## MySQL - open source
### Cài đặt Server
#### GroomIDE - online
#### Standalone server - MySQL official
### Database
#### Database

- create database: `CREATE DATABASE <database_name>`;
- obsolete database: `DROP DATABASE IF EXISTS <database_name>`;
- list down all databases: `SHOW DATABASES;`
- switch database: `USE <database name>`;
- print current database: `SELECT DATABASE();`

#### DBMS - Database Management System
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
```sql
DELIMITER $$
CREATE PROCEDURE spName()
BEGIN
  SELECT * FROM <tablename>; -- đây là câu lệnh truy vấn
END
DELIMITER;
```

- cú pháp 2:
```sql
DELIMITER //
CREATE PROCEDURE spName()
BEGIN
  SELECT * FROM <tablename>; -- đây là câu lệnh truy vấn
END //
DELIMITER;
```

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
```sql
DELIMITER  $$
CREATE definer=<user>@<serveraddress> PROCEDURE ShowCustomer() --user1@localhost là ví dụ cho user1 ở server localhost
SQL SECURITY DEFINER
BEGIN
SELECT * FROM <tablename>;
END$$
DELIMITER ;
```

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

### `TRIGGER`

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
  > END$$
  > DELIMITER ;
  > ```

### `INDEX`

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

## Data Model

### Các khái niệm cơ bản

- Data: là bất cứ sự kiện nào chúng ta có thể lưu trữ lại
- Database: là nơi để lưu trữ data
- DBMS: là phần mềm để quản lý các database có một số các DBMS rất phổ biến như MySQL, Microsoft SQL,..

### Các loại data model

#### ER Model (Entity Relational Model)

- là Mô hình thực thể quan hệ: được biểu diễn qua sơ đồ
- có 3 đối tượng
  - Entity:
    Đối tượng/ thực thể quan hệ
  - Relationship
    Mối quan hệ giữa các đối tượng
  - Attribute
    Là thuộc tính của đối tượng
- là kiểu thực thể yếu **(Weak Entity)**
  - sự tồn tại phụ thuộc vào thực thể khác ( thực thể làm chủ hay còn gọi là xác định nó)
  - kiểu thực thể yếu không có khóa
  - kiểu thực thể yếu luôn có lực lượng tham gia liên kết toàn bộ
- Ưu điểm:
  - rất dễ hiểu
  - thể hiện được thông tin một cách tổng quát
- nhược điểm
  - không thể biểu diễn giá trị cụ thể của các đối tượng
- được biểu diễn bằng các hình khối:
  - Hình chữ nhật
    Thường được biểu diễn đối tượng
  - Hình thoi
    Thường để biểu diễn hành động của 1 đối tượng lên một đối tượng khác
  - Hình elip
    Thường được biểu diễn các thuộc tính của đối tượng
- ER model sẽ được biểu thị thông qua qua các đối tượng, mối quan hệ hay thuộc tính
  nhưng để lưu trữ hoặc triển khai trong cơ sở dữ liệu thực tế chúng ta cần một mô hình dạng bảng đó là Relational Model
- các **thuộc tính** có thể thuộc 1 hoặc nhiều **nhóm** sau:
  - **Thuộc tính nguyên tố (Simple attribute)**
    Là thuộc tính ko thể chia nhỏ hơn
  - **Thuộc tính phức hợp (Composite atribute)**
    Là thuộc tính có thể chia nhỏ hơn giống như Họ và Tên có thể chia thành họ, tên đệm, tên
  - **Thuộc tính đơn trị (Single valued attribute)**
    Là thuộc tính có giá trị duy nhất. ví dụ "thẻ căn cước" của 1 đối tượng người
  - **Thuộc tính đa trị (Multi valued attribute)**
    Là thuộc tính có thể có nhiều giá trị. ví dụ như "bằng cấp" của 1 đối người
  - **Thuộc tính lưu trữ (Stored attribute)**
    những thuộc tính được tự động cập nhật vào khi cài đặt cơ sở dữ liệu. vd ngày cập nhật
  - **Thuộc tính suy dẫn (Derived attribute)**
    là thuộc tính có thể suy ra từ thuộc tính khác liên quan theo 1 quy tắc nào đó ( không phải nhập trước). vd năm sinh được lưu trữ, còn tuổi thì tính theo năm sinh
  - **Thuộc tính khóa (Key attribute)**
    là thuộc tính duy nhất cho mỗi thực thể, giúp phân biệt thực thể này và thực thể khác trong cùng 1 kiểu thực thể
    một kiểu thực thể có thể có nhiều khóa, ví dụ căn cước công dân sẽ là thuộc tính khóa vì thuộc tính này sẽ xác định duy nhất các thực thể là 'Người'
- **Các ràng buộc liên kết**
  - ràng buộc về sự tham gia liên kết được xác định trên từng thực thể
    trong từng kiểu liên kết mà thực thể đó tham gia, bao gồm:
    - lực lượng tham gia toàn bộ (total participant)
    - lực lượng tham gia bộ phận (partial participant)
  - vd: Kiểu liên kết Manages giữa 2 kiểu thực thể EMPLOYEE và DEPARTMENT
    lực lượng của kiểu tham gia DEPARTMENT là toàn bộ vì department nào cũng có người quản lý
    còn lực lượng tham gia của kiểu thực thể EMPLOYEE là bộ phận vì ko phải EMPLOYEE nào cũng là quản lý (manages) của DEPARTMENT
- **Các kiểu quan hệ**
  - **_Quan hệ one-to-one (1-1)_** vd. bang SINHVIEN va THONGTINCANCUOC, mỗi sinh viên chỉ có 1 thông tin căn cước
  - **_Quan hệ one-to-many (1-N)_** vd. bang LOP va SINHVIEN, mỗi lớp thì có nhiều sinh viên
  - **_Quan hệ many-to-many(N-N)_** vd. bảng SINHVIEN và MONHOC thì mỗi sinh viên sẽ học nhiều môn học và ngược lại, một môn học sẽ được học bởi nhiều sinh viên
- **Bậc của kiểu liên kết** là số lượng các kiểu thực thể tham gia vào liên kết, có các kiểu liên kết sau
  - **_kiểu liên kết bậc 1 (đệ quy)_** là mối quan hệ giữa cùng 1 kiểu thực thể
  - **_kiểu liên kết bậc 2_** là mối liên kết giữa 2 kiểu thực thể
  - **_kiểu liên kết bậc 3_** là mối liên kết giữa 3 kiểu thực thể

#### Relational Model

- Được biểu diễn bằng cách sử dụng các bảng
- ưu điểm:
  - biểu diễn được giá trị các đối tượng
- nhược điểm:
  - không thể hiện được rõ ràng thông tin tổng quát
- các đối tượng:
  - Relation: đối tượng bảng
  - Tuple: một hàng trong Relation(table), chúng ta cũng có thể gọi là 1 bản ghi (record)
  - Attribute (thuộc tính): Một cột trong relation(table), chúng ta cũng có thể thêm 1 trường (field)
  - Domain of attribute (miền thuộc tính): một tập hợp các giá trị của cột
- ER Model trong Relational Model, Entity chỉ đóng vai 1 bản ghi, còn các thuộc tính là loại thực thể (Entity Type)
- Mức độ của 1 Relation
  - là mối quan hệ của các thuộc tinh trong 1 mối quan hệ được gọi là mức độ của quan hệ
  - Intension: Schema hoặc Entity Type được gọi là Intension
  - Extension: Một thể hiện của Schema, ví dụ 1 Entity của table được gọi là Extension
- Quy tắc quan trọng trong Relational Model
  - không có bản sao nào nên tồn tại trong 1 Relation (quan hệ)
    hay nói cách khác chúng ta sẽ ko có Tuple nào trùng nhau trong một Relation
  - mặc dù miền của một thuộc tính không chứa Null
    Null vẫn có thể được đưa vào Tuple
    Null có nghĩa là không tồn tại
- các loại ràng buộc trong Relational Model
  - **Domain contraints (ràng buộc miền)**:
    trong mỗi Tuple, giá trị của mỗi thuộc tính phải là giá trị nguyên tử (không thể chia nhỏ hơn)
    chúng ta ko thể sử dụng thuộc tính phức hợp hoặc đa giá trị
  - **Key contraints (ràng buộc khóa)**
    không có tuple nào trùng nhau ( giá trị của tất cả các thuộc tính giống nhau).
    một relation không được có tuple nào trùng nhau
    đối với loại ràng buộc này chúng ta sẽ có 4 loại key
    - **super key**
      là tập hợp các thuộc tính xác định duy nhất 1 Tuple trong 1 Relation (quan hệ)
    - **key**
      là tập nhỏ nhất của Super key
      - vd chúng ta có tập hợp {a, b, c} là 1 super key, nếu bỏ "c" đi thì {a, b} vẫn là Super Key
        trong trường hợp ko bỏ đi a hoặc b, lúc này {a, b} được gọi là key
    - **candidate key**
      nếu có nhiều hơn 1 Key trong một Relation, chúng ta có thể Key là các Candidate Keys
    - **primary key**
      Candidate Key được sử dụng để triển khai trong cơ sở dữ liệu thì chúng ta gọi là Primary Key
  - **Entity Integrity Contraints** (ràng buộc tính toàn vẹn thực thể)
    - một primary key sẽ ko thể có giá trị Null
  - **Referential integrity contraints** (ràng buộc toàn vẹn tham chiếu)
    - trong một mô hình quan hệ, chúng ta sẽ có nhiều Relation
      và giữa các Relation sẽ có quan hệ với nhau được liên kết qua khóa ngoại Foreign Key
      Giả sử có 2 Relation R1 và R2, nếu R1,
      chứa 1 trường có vai trò là khóa chính của B ( khóa ngoại của A )
      khi B thay đổi hoặc chỉnh sửa dữ liệu thì sẽ ảnh hưởng đến A.
      Sự ràng buộc này, chúng ta gọi là tính toàn vẹn tham chiếu
    - có thể xảy ra xung đột dữ liệu bởi các hành động:
      - INSERT
        - Xảy ra khi FK ID ko có ID tồn tại trong bảng REFERENCE
      - DELETE
        - xảy ra khi xóa ID có FK ID từ các bảng tham chiếu đến
      - UPDATE
        - xảy ra khi update FK ID nhưng trong bảng tham chiếu ko có ID được tham chiếu

#### Chuyển đổi

- 4 nguyên tắc cần thiết để chuyển đổi
  ER model sang Relational Model

  - Mỗi entity trong ER Model sẽ là 1 Relation (table) trong Relation Model
  - Thuộc tính nguyên tố trong ER model sẽ là 1 thuộc tính trong Relational Model
  - Nếu 1 thuộc tính trong ER model là 1 khóa chính thì nó sẽ là 1 PK trong Relational Model
  - Nếu thuộc tính trong ER model là 1 thuộc tính phức hợp thì thuộc tính đó sẽ được chia thành các thuộc tính nguyên tố sau đó mỗi thuộc tính nguyên tố sẽ là 1 Column trong Relational Model

- 3 quy tắc đối với các Relationship

  - _**Quan hệ 1-N (one-to-many)**_
    Chúng ta sẽ lấy khóa của Entity bên 1 đặt làm FK của Relation bên N
  - _**Quan hệ 1-1 (one-to-one)**_
    Ở mỗi Relation sẽ chứa Khóa của các Entity còn lại
    tức là sau khi chuyển đổi
    ở mỗi Relation đều có FK của Relation còn lại
  - _**Quan hệ N-M (many-to-many)**_
    Ngoài việc mỗi Entity sang 1 Relation,
    chúng ta cần tạo 1 Relation mới để chứa khóa của cả 2 Entity.
    ví dụ chúng ta có Entity A có khóa P1 và Entity B có khóa là P2
    lúc này chúng ta cần tạo ra một relation X chứa cả P1 và P2 trong mỗi Tuple (hàng).

- Thuộc tính đa thị và phức hợp trong ER model **ko hợp lệ** đối với Relational Model
  Do vậy, khi gặp thuộc tính đa trị
  chúng ta cần tạo ra **một Relation mới có 2 cột**
  - **cột thứ 1**: chứa khóa của Entity cha (Entity chứa thuộc tính đa trị)
  - **cột thứ 2**: sẽ lấy tên của thuộc tính đa trị làm khóa

#### Tìm số lượng bảng phù hợp

công thức tìm số bảng:

- Số bảng tối thiểu:
  `No. of Entities` + `No. of N-M Relations` + `No. of MultiValued Attributes`
- Số bảng tối đa:
  `No. of Entities` + `No. of Relations` + `No. of MultiValued Attributes`

#### Làm thực thể yếu mạnh hơn

- **thực thể mạnh
  strong entity**
  - là thực thể có thuộc tính khóa
  - chuyển đổi như thông thường
- **thực thể yếu
  weak entity**
  - là thực thể không có thuộc tính khóa
  - để chuyển đổi sang Relational Model như thông thường
    chúng ta dùng khóa chính bao gồm:
    `khóa của thực thể liên kết cùng` + `thuộc tính bất kỳ trong thực thể`

#### mối quan hệ bậc N

- ngoài việc mỗi Entity sẽ chuyển đổi sang 1 Relation thì chúng ta sẽ tạo thêm một bảng chứa khóa của tất cả các Entity đó

## Function Dependency - FD

- là một ràng buộc xác định mối quan hệ của một thuộc tính này với 1 thuộc tính khác trong quan hệ cơ sở dữ liệu (DBMS)
- phụ thuộc hàm giúp duy trì chất lượng dữ liệu trong cơ sở dữ liệu
- đóng vai trò quan trọng để tìm ra sự khác biệt giữa thiết kế cơ sở dữ liệu tốt và xấu
- các khái niệm liên quan đến các phụ thuộc hàm
  - _giới thiệu về phụ thuộc chức năng_
    - FD dùng để xác định mối quan hệ của 1 thuộc tính này
      với 1 thuộc tính khác trong quản trị cơ sở dữ liệu
  - _phụ thuộc hàm thông thường - **trivial FD**_
    $X\to Y$ la mot Trivial FD neu $Y$ la mot tap con cua $X$.
    $X$ & $Y$ là các tập hợp thuộc tính, vi du
    - $ AB \to  A $
      $ X = \{A, B\}, Y = \{A\} $
    - $ A \to  A $
      $ X = \{A\}, Y = \{A\} $
    - $ ABC \to  BC $
      $ X = \{A, B, C\}, Y = \{B, C\} $
    - $ AB \to  A $
      $ X = \{A, B\}, Y = \{A\} $
  - _phụ thuộc hàm bất thường - **non-trivial**_
    $X\to Y$ là 1 Non-Trivial FD nếu $Y$ không phải là một tập con của $X$
    $X$ và $Y$ là các tập hợp thuộc tính, ví dụ
    - $A\to B $
      $X = \{A\}, Y = \{B\} $
    - $AB \to  C $
      $X = \{A, B\}, Y = \{C\} $
  - _phụ thuộc hàm bán thông thường - **semi-trivial**_
    $X\to Y$ là 1 Semi-Trivial FD nếu tập $X$ giao $Y$ khác rỗng và $Y$ là tập con của $X$
    $X$ và $Y$ là các tập hợp thuộc tính
    - $ AB \to  AC $
    - $ BC \to  BCD $
  - _các tính chất của tập thuộc tính_
    - _**phản xạ**_: nếu $Y \to  X$ thì $X \to  Y$
    - _**tăng trưởng**_: nếu $Z \to  U$ và $X \to  Y$ thì $XZ \to  YZ$ (ký hiệu: $X\cap Z$)
    - _**bắc cầu**_: nếu $X\to Y$ và $Y\to Z$ thì $X\to Z$
    - _**giả bắc cầu**_: nếu $X\to Y$ và $WY\to Z$ thì $XW\to Z$
    - _**luật hợp**_: nếu $X\to Y$ và $X\to Z$ thì $X\to YZ$
    - _**luật phân rã**_:
      - nếu $X\to Y$ và $Z\to Y$ thì $X\to Z$
      - nếu $A\to BC$ thì $A\to B$ và $A\to C$
  - _tập bao đóng của thuộc tính_
    - có thể định nghĩa là 1 tập hợp các thuộc tính
      có thể được xác định từ nó
    - cho $R(ABCDE)$ là 1 lược đồ quan hệ với các phụ thuộc hàm
      - $A\to B$
      - $B\to D$
      - $C\to DE$
      - $CD\to AB$
    - thì sẽ có các tập hợp đóng
      - đối với $A^+$
        - do $A\to A$, nên $A$ sẽ $\in$ A+
        - do $A\to B$, nên $B$ sẽ $\in$ A+
        - do $A\to B$ và $B\to D$ nên theo tính chất của phụ thuộc hàm
          $A\to D$ nên $D$ sẽ $\in$ A+
      - từ đó ta có A+ = ${A, B, D}$
      - tương tự như vậy
        - $B^+ = {B, D}$
        - $C^+ = {C, D, E, A, B}$
        - $D^+ = {D}$
        - $E^+ = {E}$
        - $(AB)^+ = {A, B, D}$
        - $(ABD)^+ = {A, B, D}$
    - xác định key
      - $(AB)^+ = \{A, B, C\}$
      - vì $(AB)^+$ có thể xác định cả 3 giá trị $A, B, C$
        nên chúng ta có thể sử dụng $AB$ làm key
        nhưng điều đấy không có nghĩa $AB$ luôn là key
        bởi vì $(AB)^+ = \{A, B, C\}$ có thể do $(A)^+ = \{A, B, C\}$
        ($(B)^+$ có thể không xác định được hết $A, B, C$)
  - _ứng dụng của tính bao đóng_
    tính bao đóng có các ứng dụng sau
    - xác định khóa
    - xác định sự tương đương của 2 tập FD
    - tìm tập hợp FD tối thiểu
- tìm khóa dựa vào tính bao đóng
  - thông thường nếu chúng ta chuyển đổi từ ER Model sang Relational Model thì chúng ta sẽ lấy thuộc tính khóa làm Primary Key
    nhưng trong trường hợp chúng ta ko có ER Model hoặc ko thể xác định được khóa cho 1 Relation
    mà chúng ta chỉ có các phụ thuộc hàm thì lúc này chúng ta sẽ đi xác định khóa dựa trên các phụ thuộc hàm
    lưu ý: 1 Relation có thể có một hoặc nhiều Key, Super Key
  - ôn lại các loại khóa trong relational model:
    - **super key**
      là tập hợp các thuộc tính xác định duy nhất một tuple trong 1 Relation
    - **key**
      là tập nhỏ nhất của _super key_
      ví dụ chúng ta có tập hợp $\{a, b, c\}$ là 1 _super key_
      nếu bỏ $c$ đi thì $\{a, b\}$ vẫn là super key
      (trong trường hợp ko thể bỏ đi $a$ hoặc $b$)
      lúc này $\{a, b\}$ được gọi là Key
    - **candidate key**
      nếu có nhiều hơn một key trong 1 relation
      chúng ta có thể hiểu Key là các candidate keys
    - **primary key**
      _candidate key_ được sử dụng để triển khai trong CSDL thì chúng ta sẽ gọi là Primary Key
  - ví dụ:
    - ta có quan hệ $R(ABCEF)$ và các hàm phụ thuộc sau
      - $C\to  F$
      - $E\to  A$
      - $EC\to  D$
      - $A\to  B$
    - $C$ và $E$ ko thể suy dẫn từ bất kỳ thuộc tính nào nên chắc chắn Key sẽ chứa $C$ và $E$
    - lúc này chúng ta sẽ thử kiểm tra và thấy rằng
      từ $CE$ chúng ta có thể suy dẫn ra bất kì thuộc tính nào
      tức ta có: $$(CE)^+ = \{C, E, A, F, D, B\}$$
    - $CE$ còn được gọi là tập bao đóng thuộc tính và là một _super key_
    - $CE$ cũng ko thể chia nhỏ hơn mà vẫn là 1 super key
      nên lúc này $CE$ sẽ là 1 key của quan hệ R
- tìm hiểu tính phân rã
  - cho $R(ABC)$ với các tập phụ thuộc hàm F: $F=(A\to B, B\to C)$
  - về tập đóng của thuộc tính, ta có `tập đóng của A` là ${A,B,C}$
  - ở đây ta sẽ tìm hiểu về tập đóng của phụ thuộc hàm
    tập đóng của FD sẽ chứa tất cả các FD có thể suy ra từ tập phụ thuộc hàm gốc
    ví dụ sử dụng quan hệ như ở trên ta có tập đóng của tập phụ thuộc hàm F sẽ là $$F^+ = \{A\to B, B\to C, A\to C, AB\to C, ...\}$$
  - khi tạo các bảng dữ liệu, chúng ta rất dễ làm dư thừa dữ liệu
    khi đó chúng ta sẽ cần chuẩn hóa lại các bảng
    để giảm dư thừa dữ liệu
    một ví dụ, như ảnh dưới từ 1 tháng đầu có dữ liệu dư thừa
    ![image](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FDBI202x_03%2FContent%2FDBI202x_L21_H%C3%ACnh%202.png?alt=media&token=0e7dbb39-0520-4b6e-89bf-589cea415860)
    chúng ta sẽ tách thành 2 bảng chứa dữ liệu không dư thừa
  - trong quá trình chuẩn hóa chúng ta có thể sẽ phân rã các bảng
    3 vấn đề cần đảm bảo trong quá trình phân rã:
    - **phân rã không được mất thông tin (lossless decomposition)**
      khi ghép cặp đôi một các mối quan hệ thì 1 trong hai mối quan hệ phải chứa 1 key
    - **phân rã phải bảo toàn thuộc tính (attribute preversing)**
      mỗi thuộc tính có ít nhất 1 trong các mối quan hệ
      (ko có thuộc tính nào không có trong các quan hệ)
    - **phân rã phải bảo toàn phụ thuộc hàm (dependency preversing decomposition)**
      đảm bảo các phụ thuộc hàm ban đầu phải có trong hợp của các phụ thuộc hàm của các mối quan hệ con
      giả sử ta có tập các phụ thuộc hàm ban đầu là F và các mối quan hệ con là R1, R2, R3
      như vậy phân rã bảo toàn phụ thuộc hàm có nghĩa là
      $$ F \subset (F_{R_1} \cup F_{R_2} \cup F_{R_3})^+ $$
  - cho ví dụ: quan hệ $R(ABC)$
    - có tập phụ thuộc hàm sau: $F=\{A\to B, B\to C, C\to A \}$
    - 2 quan hệ được phân rã từ $R$ là $R_1(AB)$ và $R_2(BC)$
      việc chúng ta là kiểm tra xem sự phân rã này có hợp lệ ko 
      - kiểm tra **lossless decomp.**
        kiểm tra $R_1(AB)$, ta thấy $B^+=\{A,B,C\}$ nên $B$ sẽ là 1 _key_ của $R_1$
        lúc này chúng ta ko cần kiểm tra thêm $R_2(BC)$ 
        mà sẽ khẳng định sự phân rã từ $R$ thành $R_1$ và $R_2$ đã đảm bảo ko mất thông tin
      - kiểm tra **attribute preversing**
        từ quan hệ $R_1$ và $R_2$, chúng ta có thể dễ dàng thấy được mỗi thuộc tính trong quan hệ $R$
        đều có ít nhất 1 trong 2 quan hệ $R_1$ và $R_2$
      - kiểm tra **dependency decomp.**
        - từ $R_1(AB)$ chúng ta có thuộc tính $A,B$
          từ thuộc tính $A,B$ chúng ta sẽ có các phụ thuộc hàm
          $$F_1 = \{A\to B, B\to A\}$$
        - từ $R_2(BC)$ chúng ta có thuộc tính $B,C$
          từ thuộc tính $B,C$ chúng ta sẽ có các phụ thuộc hàm
          $$F_2 = \{B\to C, C\to B\}$$
        - như vậy, ta có:
          $$F\subseteq (F_1 \cup F_2)^+ = \{A\to B,B\to C,C\to A\}$$
        - từ các phân tích trên chúng ta có thể kết luận quan hệ $R$ có thể phân rã được thành $R_1$ và $R_2$
## Chuẩn hóa dữ liệu - Normal Form

### Chuẩn hóa NF1
- Nếu quan hệ R ko có các thuộc tính đa trị hoặc phức hợp 
  thì ta gọi quan hệ R đã đạt chuẩn hóa NF1
### Chuẩn hóa NF2
- quan hệ R đạt chuẩn NF2 khi thỏa mãn 2 điều kiện:
  - quan hệ R cũng phải đạt chuẩn NF1
  - ko có sự phụ thuộc từng phần của thuộc tính không khóa bất kỳ nào trong quan hệ R
    khóa ko được chứa các thuộc tính dẫn xuất ra thuộc tính không khóa (dựa vào phụ thuộc hàm để xác định)
- ví dụ:
  - ta có $R(MNO)$ với các phụ thuộc hàm 
    (các thuộc tính đều là thuộc tính đơn trị)
    $$F=\{MN\to O,M\to O\}$$
    Do $(MN)^+=\{M,N,O\}\Rightarrow (MN)^+$ là 1 khóa
  - điều kiện 1:
    các thuộc tính đều là thuộc tính đơn trị => thỏa
  - điều kiện 2:
    - M, N là các thuộc tính nguyên tố và O là thuộc tính không khóa
    kiểm tra N: N là 1 phần của key nhưng ko dẫn xuất ra thuộc tính khác => đạt
    kiểm tra M: M là 1 phần của key và M->O => ko đạt
    - do đó quan hệ R(MNO) không đạt chuẩn NF2
    - giả sử chúng ta có key là MN thì M, N lần lượt là các thuộc tính thành phần 
      => cần kiểm tra có dẫn xuất ra thuộc tính không khóa nào không
    - giả sử chúng ta có key là M, thì M là 1 key hoàn chỉnh
      không phải thuộc tính thành phần nên ko cần kiểm tra M có dẫn xuất ra thuộc tính ko khóa nào ko
### Chuẩn hóa NF3
- Quan hệ R đã đạt chuẩn hóa NF2
- các thuộc tính ko khóa sẽ **ko xác định** thuộc tính ko khóa khác
- bài viết tham khảo [tại đây](https://viblo.asia/p/tim-hieu-ve-chuan-hoa-co-so-du-lieu-RQqKLNgpl7z)