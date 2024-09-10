[Lab 12.2](https://docs.google.com/document/d/1NdUmyh2DVW1bUTAApWoDfUryiWBLqxw-/edit)

# Điều khiển Transaction

Để điều khiển các trạng thái trong một transaction, chúng ta sẽ hay gặp những lệnh sau:

- `start transaction`: Lệnh bắt đầu một transaction.
- `savepoint`: Lệnh này sẽ được sử dụng để lưu lại trạng thái dữ liệu hiện tại trong transaction.
- `rollback`: Lệnh này sẽ được sử dụng để quay lại trang thái đã lưu bởi savepoint. Thông thường lệnh này hay được sử dụng trong các trường hợp transaction bị lỗi dữ liệu và chúng ta sẽ quay lại trạng thái dữ liệu không bị lỗi đã lưu trước đó.
- `commit`: Lệnh này được sử dụng như cách thông báo một transaction đã hoàn tất.

**Bước 1**: Chạy các câu truy vấn:

> ```sql
> use online_shop;
> start transaction;
> insert into categories set name = 'name A';
> select * from categories;
> ```

Hãy chắc chắn rằng các bạn đã insert một category mới có tên là ‘name A’.

> OK

**Bước 2**: Chạy câu truy vấn:

> ```sql
> savepoint test1;
> ```

**Bước 3**: Chạy các câu truy vấn:

> ```sql
> update categories set name = 'name B' where id = 1;
> select * from categories;
> ```

Hãy chắc chắn rằng các bạn đã update thành công tên của category có id là 1

> OK

**Bước 4**: Chạy câu truy vấn sau:

> ```sql
> rollback to test1;
> select * from categories;
> ```

Hãy mô tả về dữ liệu sau khi truy vấn ở _bước 4_, giải thích kết quả.

> dữ liệu của hàng id=1 đã trả giá trị về trước khi query update được thực hiện
