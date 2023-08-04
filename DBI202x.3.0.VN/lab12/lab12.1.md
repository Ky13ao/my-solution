[Lab 12.1](https://docs.google.com/document/d/1ymQZtX8lxIa30e0tyD-i3Ia7SiP7zm2n/edit)

# Transaction

>     Yêu cầu 1: Hiển thị các ACID 3
>     Yêu cầu 2: Isolation level read uncommitted 3
>     Yêu cầu 3: Isolation level read committed 4
>     Yêu cầu 4: Isolation level repeatable read 5
>     Yêu cầu 5: Isolation level Serializable – INSERT 6
>     Yêu cầu 6: Isolation level Serializable – UPDATE 7

Ở các Lab trước, các bạn đã được thực hành và làm quen với cách viết các câu truy vấn như sử dụng `SELECT`, `UPDATE` … Tuy nhiên những câu truy vấn các bạn đã từng viết chỉ là một câu truy vấn đơn và xuất phát từ cùng một user, tức chúng ta chưa quan tâm đến tính chính xác của dữ liệu khi có nhiều tài khoản, hoặc nhiều câu truy vấn tương tác đến cùng một đối tượng trong cùng một thời điểm. Để làm rõ hơn chúng ta sẽ có một ví dụ như sau:

- Khi chúng ta thực hiện giao dịch hay chuyển khoản ngân hàng từ tài khoản A sang tài khoản B, sẽ có hai bước mà ngân hàng cần xử lý:
  - **Bước 1**: Trừ tiền trong tài khoản A
  - **Bước 2**: Cộng tiền trong tài khoản B\
    Đây là một quá trình gồm hai bước, và quá trình thành công chỉ khi cả hai bước đều thành công và thất bại khi cả hai bước đều thất bại. Nếu chỉ một trong 2 bước trên thành công thì giao dịch sẽ có bất thường. Đây chính là một ví dụ điển hình về transaction và tại sao một transaction cần đảm bảo bốn tính chất ACID.
- Một transaction sẽ có 4 tính chất quan trọng (ACID):
  - **Tính nguyên tố (Atomicity)**. Một transaction bao gồm các hoạt động khác nhau phải thỏa mãn điều kiện hoặc là tất cả thành công hoặc là không một hành động nào thành công.
  - **Tính nhất quán (Consistency)**. Một transaction sẽ có trạng thái bất biến về dữ liệu có nghĩa là dữ liệu luôn được bảo toàn. Nếu có lỗi quay về trạng thái trước đó.
  - **Tính độc lập (Isolation)**. Một transaction đang thực thi và chưa được xác nhận phải bảo đảm tính độc lập với các transaction khác.
  - **Tính bền vững (Durability)**. Khi một transaction được commit thành công dữ liệu sẽ được lưu lại một cách chuẩn xác.
- Để kiểm soát dữ liệu của các transaction, có 4 kiểu lock dữ liệu:
  - **Table locking**: Transaction T1 đang dùng bảng A, thì các transaction khác sẽ không thể sử dụng bảng A.
  - **Row level locking**: Transaction T1 sử dụng hàng dữ liệu r trong bảng A thì các transaction khác sẽ không thể sử dụng (ví dụ như update hay delete) hàng r.
  - **Read lock (shared)**: Tất cả transaction sẽ không thể ghi dữ liệu được vào bảng, kể cả transaction đang sử dụng bảng.
  - **Write lock (excusive)**: Transaction đang sử dụng bảng dữ liệu có thể đọc và ghi dữ liệu vào bảng nhưng các transaction khác không thể ghi dữ liệu vào bảng mà chỉ có thể đọc dữ liệu từ bảng.
- Trong tính chất Isolation của transtion sẽ có 4 cấp độ (isolation level):
  - **Read uncommitted**: Một transaction lấy dữ liệu từ một transaction khác ngay cả khi transaction đó chưa được commit.
  - **Read committed**: Đây là level default của một transaction nếu như chúng ta không config gì thêm. Tại level này thì Transaction sẽ không thể đọc dữ liệu từ từ một Transaction đang trong quá trình cập nhật hay sửa đổi mà phải đợi transacction đó hoàn tất. Như vậy thì chúng ta có thể tránh được Dirty Read và Dirty Write nhưng các Transaction sẽ phải chờ nhau làm cho Perfoman của hệ thống thấp.
  - **Repeatable read**: Gần giống như mức độ của Read Committed, tại mức độ này thì các transaction sẽ không thể đọc hoặc ghi đè dữ liệu từ một transaction đang tiến hành cập nhật trên bản ghi đó.
  - **Serializable**: Level cao nhất của Isolation, khi transaction tiến hành thực thi nó sẽ khóa các bản ghi liên quan và sẽ unlock cho tới khi rollback hoặc commit dữ liệu.

| Transaction isolation level | Dirty reads | Nonrepeatable reads | Phantoms |
| --------------------------- | :---------: | :-----------------: | :------: |
| Read uncommitted            |      x      |          x          |    x     |
| Read committed              |             |          x          |    x     |
| Repeatable read             |             |                     |    x     |
| Serializable                |             |                     |          |

- _**Yêu cầu 1**_: Hiển thị các ACID

  Chạy câu truy vấn dưới đây để kiểm tra các transaction hiện có trong cơ sở dữ liệu

  > ```sql
  > select @session.tx_tsolation;
  > ```

- _**Yêu cầu 2**_: Isolation level read uncommitted

  - **Bước 1**: Các bạn sẽ mở hai kết nối của `user1` và `user2` tương tự như lab11
  - **Bước 2**: Tại tab `user1`, các bạn thực hiện truy vấn sau:
    > ```sql
    > use online_shop;
    > set transaction isolation level read uncommitted;
    > start transaction;
    > select * from customers;
    > ```
  - **Bước 3**: Tại tab `user2`, các bạn thực hiện truy vấn sau:

    > ```sql
    > use online_shop;
    > update customers set name = 'name C' where id = 2;
    > ```

  - **Bước 4**: Tại tab `user1`, các bạn sẽ kiểm tra lại dữ liệu của bảng `customers`
    > ```sql
    > select * from customers;
    > ```

  Trả lời câu hỏi: Bản ghi có id = 2 đã được cập nhật chưa, giải thích lý do.

  > mặc dù transaction chưa commit nhưng isolation level là read uncommitted nên vẫn đọc được

- _**Yêu cầu 3**_: Isolation level read committed

  - **Bước 1**: Tại tab `user1`, các bạn thực hiện truy vấn sau:
    > ```sql
    > use online_shop;
    > set transaction isolation level read committed;
    > start transaction;
    > insert into customers(name, email) values('name D', 'A@gmail.com');
    > select * from customers;
    > ```

  Trả lời câu hỏi: Câu lệnh insert bên trên đã thực hiện thành công chưa ?

  > Chưa có lệnh `commit` nên TRANSACTION chưa được thành công

  - **Bước 2**: Tại tab `user2`, các bạn thực hiện truy vấn sau:

    > ```sql
    > use online_shop;
    > select * from customers;
    > ```

  Trả lời câu hỏi: Ở tab `user2` có nhìn được dữ liệu vừa cập nhật ở tab `user1` không. Giải thích lý do.

  > Vì transaction của `user1` là read committed isolation level và chưa commit nên `user2` ko thể đọc được

  - **Bước 3**: Tại tab `user1`, các bạn chạy câu truy vấn sau:

    > ```sql
    > commit;
    > ```

  - **Bước 4**: Quay lại tab `user2` và hiển thị lại dữ liệu bản `customers`
    > ```sql
    > use online_shop;
    > select * from customers;
    > ```

  Trả lời câu hỏi: tab `user2` có nhìn được dữ liệu vừa cập nhật ở bước 1 không. Giải thích lý do.

  > Vì user1 vừa commit thành công transaction, nên lần truy xuất này user2 đã đọc được dữ liệu của user1 cập nhật

- _**Yêu cầu 4**_: Isolation level repeatable read

  - **Bước 1**: Tại tab user1, các bạn thực hiện truy vấn sau:
    > ```sql
    > use online_shop;
    > set transaction isolation level repeatable read;
    > start transaction;
    > update customers set name='name E' where id = 1;
    > select * from customers;
    > ```

  Trả lời câu hỏi: Câu lệnh insert bên trên đã thực hiện thành công chưa ?

  > Transaction chưa commit, đương nhiên là chưa thành công

  - **Bước 2**: Tại tab user2, các bạn thực hiện truy vấn sau:
    > ```sql
    > use online_shop;
    > update customers set name='name F' where id = 1;
    > ```

  Trả lời câu hỏi: Ở tab user2 có thực hiện cập nhật được cho bản ghi có id 1 không. Giải thích lý do.

  > Lệnh `update` id1 đang bị treo do `Transaction` của `user1` là `repeatable read` isolation level

  - **Bước 3**: Tại tab user1, các bạn chạy câu truy vấn sau:
    > ```sql
    > commit;
    > select * from customers;
    > ```

  Trả lời câu hỏi: Lúc này tab user1 có nhìn được dữ liệu vừa cập nhật ở bước 2 không. Giải thích lý do.

  > Không biết câu trả lời có đúng ý mentor không nhưng câu `update` của `user2` bị Lock wait timeout exceeded nên câu lệnh không thành công

- _**Yêu cầu 5**_: Isolation level Serializable – INSERT

  - **Bước 1**: Tại tab `user1`, các bạn sẽ chạy truy vấn sau:

    > ```sql
    > use online_shop;
    > set transaction isolation level serializable;
    > start transaction;
    > select * from customers;
    > ```

  - **Bước 2**: Tại tab `user2`, các bạn sẽ chạy truy vấn sau:

    > ```sql
    > use online_shop;
    > insert into customers(name, email) values('name A', 'A@gmail.com');
    > ```

  - Sau khi insert sau dữ liệu các bạn sẽ query thử dữ liệu hiện có trong bảng `customers`:
    > ```sql
    > select * from customers;
    > ```
  - **Bước 3**: Tại tab `user1`, các bạn sẽ chạy truy vấn dưới đây và đưa ra nhận xét về số lượng bản ghi tại bước 2 và bước 3, giải thích lý do.
    > ```sql
    > select * from customers;
    > ```
  - **Bước 4**: Tại tab `user1`, các bạn sẽ chạy truy vấn dưới đây và đưa ra nhận xét về số lượng bản ghi của bảng `customers` của `user1` và `user2`, giải thích lý do:
    > ```sql
    > commit;
    > select * from customers;
    > ```

  > `user1` đã tạo transaction repeatable read isolation level nên `user2` sẽ ko thể ghi đè lên bảng mà user1 thực hiện transaction

- _**Yêu cầu 6**_: Isolation level Serializable – UPDATE

  - **Bước 1**: Tại tab `user1`, các bạn sẽ chạy truy vấn sau:

    > ```sql
    > use online_shop;
    > set transaction isolation level serializable;
    > start transaction;
    > select * from customers;
    > ```

  - **Bước 2**: Tại tab `user2`, các bạn sẽ chạy truy vấn sau:

    > ```sql
    > update customers set name = 'name B' where id = 1;
    > ```

  Câu truy vấn trên có thực thi được không và giải thích lý do.

  > lúc này transaction của user1 đang lock table, nên query của user2 treo để đợi

  - **Bước 3**: Tại tab `user1`, các bạn thực hiện truy vấn sau:

    > ```sql
    > commit;
    > select * from customers;
    > ```

  Bản ghi có `id = 1` ở _bước 2_ đã được cập nhật dữ liệu chưa, giải thích kết quả.

  > lúc này transaction của user1 đã commit, và query của user đã hoàn tất sau đó, nên kết quả đã cập nhật những thay đổi từ user.
