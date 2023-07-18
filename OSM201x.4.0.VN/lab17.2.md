[Lab 17.2](https://docs.google.com/document/d/1EBRo2T5kgAarWhmGK-X4PEs6eZ6m2iIHD1NkUnhVW7U/edit)

# Truyền và sao chép tệp qua mạng

Trong bài lab này chúng ta sẽ được thao tác để truyền và sao chép tệp qua mạng thông qua câu lệnh scp hoặc sftp và những lệnh bổ sung thêm khác.

# Định nghĩa SCP:

- SCP (Secure Copy - Sao chép an toàn) là một ứng dụng sử dụng SSH để mã hóa toàn bộ quá trình chuyển tập tin.
- SCP là lệnh dùng để di chuyển file dữ liệu giữa các máy tính chạy hệ điều hành Linux từ xa.
- SCP dùng ssh để di chuyển dữ liệu, có chế độ bảo mật giống như SSH.

# Cài đặt SCP trên server Linux:

Với các bản hệ điều hành Linux mới đây thì công cụ scp đã được tích hợp sẵn khi cài đặt hệ điều hành. Nếu server của bạn chưa được tích hợp sẵn, hãy chạy lệnh sau để cài đặt:

`sudo apt-get install scp -y`

# Sử dụng SCP để truyền file:

#### Cú pháp cơ bản của SCP như sau:

`scp [option] <Source> <Destination>`

#### Trong đó:

- scp: là lệnh gọi công cụ scp.
- [option]: là các tùy chọn khi thực hiện trong quá trình truyền tải file.
- <Source\>: là đường dẫn đến file/folder nguồn thực hiện truyền tải.
- <Destination\>: là đường dẫn đích lưu trữ file/folder khi truyền tải.

Một số option thường sử dụng trong SCP như:

| Tùy chọn | Mô tả                                                                               |
| :------: | :---------------------------------------------------------------------------------- |
|    -r    | Sử dụng cho việc truyền các thư mục.                                                |
|    -P    | Sử dụng để khai báo cổng ssh máy chủ từ xa.                                         |
|    -C    | Sử dụng để nén dữ liệu trước khi gửi.                                               |
|    -c    | Sử dụng để chọn thuật toán mã hóa để truyền dữ liệu.                                |
|    -v    | Cho ra kết quả đầu ra với nhiều thông tin hơn về những gì chương trình sẽ thực thi. |

#### Ví dụ:

```sh
scp -v /var/log/syslog root@10.4.3.201:/root/
# Destination structure user@address:location
```

Bài lab đã cung cấp cho bạn tổng quan về kiến thức truyền tệp qua mạng sử dụng SCP. Bạn hãy xem video bên dưới để có xem chi tiết kiến thức và thực hành với việc truyền và sao chép tệp qua mạng cụ thể là với SFTP.

[Truyền và sao chép tệp qua mạng](https://funix.udemy.com/course/learn-linux-in-5-days/learn/lecture/1417760#overview)
