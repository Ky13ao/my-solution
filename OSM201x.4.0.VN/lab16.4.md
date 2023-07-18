[Lab16.4](https://docs.google.com/document/d/1CB50JYysHSgxzfPC0wtehX2Z-u8_Wxa06b063kRJYCY/edit)

# So sánh tệp tin

Trong bài lab này, chúng ta sẽ được làm quen với việc so sánh tệp tin tương ứng trong Linux. Thông qua những câu lệnh `diff`, `sdiff` hay là `vimdiff`.

### So sánh tập tin với lệnh `diff`:

Lệnh `diff` dùng để so sánh tập tin và thư mục:

**Cú pháp tương ứng:**

`diff [tùy chọn] <filename 1> <filename 2>`

Ví dụ khi sử dụng lệnh `diff` để so sánh file:

Để xem các tùy chọn của lệnh `diff` ta dùng lệnh: `man diff`

**Một vài tùy chọn được dùng thường xuyên gồm:**

| Tùy chọn | Sử dụng                                                      |
| :------: | :----------------------------------------------------------- |
|   `-c`   | Cung cấp 3 dòng trước và sau của sự khác nhau về nội dung.   |
|   `-r`   | Sử dụng để so sánh đệ quy các thư mục con, thư mục hiện tại. |
|   `-i`   | Bỏ qua trường hợp chữ cái.                                   |
|   `-w`   | Bỏ qua sự khác biệt về tab (khoảng trắng).                   |
|   `-q`   | Báo những tệp khác nhau mà không cần liệt kê sự khác biệt.   |

### So sánh tệp tin với `sdiff`:

`sdiff` sẽ thực hiện so sánh song song sự khác biệt giữa FILE1 và FILE2 và hợp nhất chúng theo tùy chọn (xem tùy chọn).
Nếu một trong các FILE được chỉ định dưới dạng dấu gạch ngang (“-”), `sdiff` sẽ đọc từ đầu vào chuẩn.

**Cú pháp tương ứng:**

`sdiff [OPTION]... FILE1 FILE2`

**Một vài tùy chọn được dùng thường xuyên bao gồm:**

| Tùy chọn                    | Sử dụng                                                    |
| --------------------------- | ---------------------------------------------------------- |
| `-o` FILE, `-output` = FILE | Hợp nhất các tệp một cách tương tác và gửi đầu ra tới FILE |
| `-i`                        | Xử lý chữ hoa và chữ thường như thể chúng giống nhau.      |
| `-E`                        | Bỏ qua các thay đổi do mở rộng tab.                        |
| `-NS`                       | Bỏ qua những thay đổi về lượng khoảng trắng.               |
| `-W`                        | Bỏ qua tất cả các khoảng trắng.                            |

Bài lab đã cung cấp cho bạn tổng quan khi thực hành thông qua câu lệnh `diff` và `sdiff`. Còn kiến thức liên quan tới `vimdiff` tương ứng. Bạn hãy xem video bên dưới để có xem chi tiết và thực hành với việc so sánh tệp tin.

### Bài tập:

> - Học viên truy cập vào link, tải folder này về: https://drive.google.com/drive/folders/1BpuklzrrxmmdzwhQPJacyl6S2avXzWcY?usp=sharing, bên trong folder có 2 file.
> - Dùng lệnh `diff` để so sánh sự khác nhau giữa 2 file
> - Dùng lệnh `sdiff` để so sánh 2 file.
> - Dùng lệnh `sdiff` so sánh 2 file không phân biệt hoa thường.

### Bài giải:

```sh
diff a.txt b.txt
#---Output---#
# 3d2
# < Telangana
sdiff a.txt b.txt
#---Output---#
# Gujarat                                                         Gujarat
# Andhra Pradesh                                                  Andhra Pradesh
# Telangana                                                     <
# Bihar                                                           Bihar
# Uttar pradesh                                                   Uttar pradesh
sdiff a.txt b.txt -i
#---Output---#
# Gujarat                                                         Gujarat
# Andhra Pradesh                                                  Andhra Pradesh
# Telangana                                                     <
# Bihar                                                           Bihar
# Uttar pradesh                                                   Uttar prades
```

[So sánh tệp tin](https://funix.udemy.com/course/learn-linux-in-5-days/learn/lecture/1417756#overview)
