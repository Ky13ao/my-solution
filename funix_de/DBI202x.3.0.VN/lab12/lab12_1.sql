-- Một transaction sẽ có 4 tính chất quan trọng (ACID):
  -- Tính nguyên tố (Atomicity). Một transaction bao gồm các hoạt động khác nhau phải thỏa mãn điều kiện hoặc là tất cả thành công hoặc là không một hành động nào thành công.
  -- Tính nhất quán (Consistency). Một transaction sẽ có trạng thái bất biến về dữ liệu có nghĩa là dữ liệu luôn được bảo toàn. Nếu có lỗi quay về trạng thái trước đó.
  -- Tính độc lập (Isolation). Một transaction đang thực thi và chưa được xác nhận phải bảo đảm tính độc lập với các transaction khác.
  -- Tính bền vững (Durability). Khi một transaction được commit thành công dữ liệu sẽ được lưu lại một cách chuẩn xác.

-- Để kiểm soát dữ liệu của các transaction, có 4 kiểu lock dữ liệu:
  -- Table locking: Transaction T1 đang dùng bảng A, thì các transaction khác sẽ không thể sử dụng bảng A.
  -- Row level locking: Transaction T1 sử dụng hàng dữ liệu r trong bảng A thì các transaction khác sẽ không thể sử dụng (ví dụ như update hay delete) hàng r.
  -- Read lock (shared): Tất cả transaction sẽ không thể ghi dữ liệu được vào bảng, kể cả transaction đang sử dụng bảng.
  -- Write lock (excusive): Transaction đang sử dụng bảng dữ liệu có thể đọc và ghi dữ liệu vào bảng nhưng các transaction khác không thể ghi dữ liệu vào bảng mà chỉ có thể đọc dữ liệu từ bảng.

-- Trong tính chất Isolation của transtion sẽ có 4 cấp độ (isolation level):
  -- Read uncommitted: Một transaction lấy dữ liệu từ một transaction khác ngay cả khi transaction đó chưa được commit. 
  -- Read committed: Đây là level default của một transaction nếu như chúng ta không config gì thêm. Tại level này thì Transaction sẽ không thể đọc dữ liệu từ từ một Transaction đang trong quá trình cập nhật hay sửa đổi mà phải đợi transacction đó hoàn tất. Như vậy thì chúng ta có thể tránh được Dirty Read và Dirty Write nhưng các Transaction sẽ phải chờ nhau làm cho Perfoman của hệ thống thấp.
  -- Repeatable read: Gần giống như mức độ của Read Committed, tại mức độ này thì các transaction sẽ không thể đọc hoặc ghi đè dữ liệu từ một transaction đang tiến hành cập nhật trên bản ghi đó.
  -- Serializable: Level cao nhất của Isolation, khi transaction tiến hành thực thi nó sẽ khóa các bản ghi liên quan và sẽ unlock cho tới khi rollback hoặc commit dữ liệu.

SELECT * FROM INFORMATION_SCHEMA.USER_PRIVILEGES WHERE GRANTEE="'user1'@'localhost'";
SELECT * FROM INFORMATION_SCHEMA.USER_PRIVILEGES WHERE GRANTEE="'user2'@'localhost'";

-- YC1: hien thi cac ACID
  SELECT @session.tx_tsolation;

-- YC2: read uncommitted ISOLATION LEVEL
  -- switch user1
  USE online_shop;
  SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
  START TRANSACTION;
  SELECT * FROM customers;

  -- switch user2
  USE online_shop;
  UPDATE customers SET name = 'name C ' WHERE id = 2;

  -- switch user1
  SELECT * FROM customers;

  -- mặc dù transaction chưa commit nhưng isolation level là read uncommitted nên vẫn đọc được 

-- YC3: read committed ISOLATION LEVEL
  -- switch user1
  USE online_shop;
  SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
  START TRANSACTION;
  INSERT INTO customers(name, email) VALUES('name D', 'A@gmail.com');
  SELECT * FROM customers;

  --switch user2
  USE online_shop;
  SELECT * FROM customers;

  --switch user1
  COMMIT;

