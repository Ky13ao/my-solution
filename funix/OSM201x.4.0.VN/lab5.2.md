# Lab 5.2: Tương tác về quyền với thư mục và tệp tin trong Linux phần 2

[Link](https://docs.google.com/document/d/1QDkPbTeFaEyRjtM2s3Mbu4c4Sd1dNGzXcbmUQCeiWfA/edit)
Trong bài lab này, chúng ta sẽ được tìm hiểu và thực hành tiếp về việc tương tác với quyền trong thư mục và tệp tin của Linux.

## 1. Quyền hạn mặc định:

Do Linux được tạo ra nhằm mục đích cho nhiều người sử dụng nên cũng sẽ có các thiết lập mặc định dành cho người dùng bình thường, những người mà không quan tâm hoặc ít quan tâm đến vấn đề cài đặt hoặc cấu hình. Không nằm ngoài quy luật này, với các file được tạo ra bởi người dùng thì luôn có những giá trị mặc định được thiết lập sẵn. Chi tiết ở bảng dưới đây:

| **Kiểu** | **Owner**                  | **Group**             | **Other**             |
| -------- | -------------------------- | --------------------- | --------------------- |
| Tệp tin  | rw- (đọc và ghi)           | r– (chỉ đọc)          | r– (chỉ đọc)          |
| Thư mục  | rwx (đọc, ghi và truy cập) | r-x (đọc và truy cập) | r-x (đọc và truy cập) |

Như vậy, khi tạo một file mới, quyền cao nhất luôn luôn thuộc về người tạo nó, bao gồm đọc, sửa, xóa,.., nhóm và người dùng khác chỉ có quyền xem. Với thư mục, mặc dù vẫn dùng chung các kí hiệu r,w,x như file thông thường nhưng quyền hạn thì có một chút khác biệt, cụ thể là:

- r (read): quyền xem danh sách file và thư mục con (dùng lệnh ls).
- w (write): quyền tạo file và thư mục con (dùng lệnh touch và mkdir).
- x (execute): quyền chuyển vào thư mục (dùng lệnh cd).

## 2. Phân quyền nâng cao sử dụng chmod:

- Nếu nói tới phân quyền trong Linux, không thể không nhắc tới chmod. Đây là câu lệnh cơ bản nhất dùng để phân quyền file, chức năng chính của nó thì như tên gọi - chmod (change file mode bits). Hai cú pháp cơ bản của chmod là:

```shell
chmod MODE[,MODE] … FILE … # Dùng symbolic
chmod OCTAL-MODE FILE … # Dùng octal number
```

- Cách thứ nhất, dùng để phân quyền một cách rõ ràng cho từng nhóm phân quyền (owner, group, other hoặc all), còn cách thứ hai sẽ giúp người sử dụng thao tác nhanh hơn nếu đã làm quen với lệnh. Về cách thứ nhất, format chung của mode sẽ như sau.

```shell
chmod [group_permission] [operator] [permission].
```

### Bảng Group Permission

| **Group Permission** | **Symbolic** | **Description**            |
| -------------------- | ------------ | -------------------------- |
| Owner                | u            | Chủ sở hữu                 |
| Group                | g            | Nhóm sở hữu                |
| Other                | o            | Người dùng và nhóm khác    |
| All                  | a            | Toàn bộ người dùng và nhóm |

### Bảng Operator

| **Operator** | **Symbolic** | **Description**       |
| ------------ | ------------ | --------------------- |
| Add          | -            | Loại bỏ quyền         |
| Remove       | \*           | Cấp thêm quyền        |
| Assign       | =            | Chỉ định quyền cụ thể |

### Bảng Permission:

| **Permission** | **Symbolic** | **Description**                                                  |
| -------------- | ------------ | ---------------------------------------------------------------- |
| Read           | r            | Quyền đọc                                                        |
| Write          | w            | Quyền ghi                                                        |
| Execute        | x            | Quyền thực thi                                                   |
| Setuid/Setgid  | s            | Người thực thi là người sở hữu thay vì người sử dụng lệnh        |
|                | s            | Tượng tự với Setuid/Setgid nhưng file không thể thực thi         |
| Sticky         | t            | Chủ sở hữu (hoặc root) mới được phép xóa hoặc thay đổi tên file. |

- Cách thứ hai sẽ khó sử dụng hơn cách thứ nhất do dùng chữ số nhưng nếu quen rồi thì khi thao tác sẽ nhanh hơn rất nhiều.
  Cụ thể phân quyền bằng cách này sẽ sử dụng một dãy tối đa 4 chữ số để phân quyền. Chữ số nào bị thiếu thì mặc định sẽ coi như bằng 0.
  VD: 7 tương đương với 0007.
  Các giá trị cho phép sẽ là một số octal (hệ 8) trong khoảng từ 0 đến 7777. Bảng sau sẽ trình bày cụ thể các giá trị:

| **Giá trị** | **Hàng thứ nhất**        | **Hàng thứ 2,3,4**               |
| ----------- | ------------------------ | -------------------------------- |
| 0           |                          | Không có quyền (---)             |
| 1           | Sticky                   | Quyền thực thi (--x)             |
| 2           | Setgid                   | Quyền ghi (-w-)                  |
| 3           | Sticky và Setgid         | Quyền ghi và thực thi (-wx)      |
| 4           | Setuid                   | Quyền đọc (r–)                   |
| 5           | Sticky và Setuid         | Quyền đọc và thực thi (r-x)      |
| 6           | Setgid và Setuid         | Quyền đọc và ghi (rw-)           |
| 7           | Sticky. Setgid và Setuid | Quyền đọc, ghi và thực thi (rwx) |

Thông thường với một file văn bản, hình ảnh,... thì ta nên sử dụng mode rw-r–r– hay 644, bất cứ ai cũng có thể đọc nhưng chỉ chủ sở hữu mới có quyền ghi. Với thư mục hoặc file cần thực thi thì ta có thể cấp quyền thực thi, nhưng phải chú ý công năng của file và hạn chế cấp quyền cho Other hoặc thậm chí cả Group nếu không cần thiết.

## 3. Phân quyền sử dụng chown và chgrp:

- Lệnh chmod chỉ có khả năng thay đổi quyền truy xuất tới file (đọc, ghi, thực thi,..). Còn nếu ta muốn thay đổi chủ sở hữu hoặc nhóm sở hữu thì phải dùng đến 2 lệnh là chown và chgrp.
- chown là lệnh dùng để thay đổi chủ sở hữu (có thể thay đổi nhóm sở hữu) còn chgrp thì chỉ cho phép thay đổi nhóm sở hữu của file.
  VD: chown john:admin abc thì sẽ chuyển quyền sở hữu của file abc sang cho người dùng john và nhóm admin.
- Đặc biệt ta có thể thêm tùy chọn -R để chuyển quyền cho toàn bộ cây thư mục (file và thư mục con), tùy chọn này sẽ hữu ích khi ta muốn thay đổi chủ sở hữu hoặc nhóm trên tất cả file trong thư mục nào đó mà không muốn lặp đi lặp lại một thao tác.

Hiện tại, bạn đã tìm hiểu cơ bản về quyền với thư mục và tệp tin trong Linux. Ngoài ra, học viên hãy tham khảo video bài giảng bên dưới để có thể hiểu rõ về kiến thức cũng như chi tiết phần thực hành tương ứng.

> **Bài tập**
>
> - Tạo 1 file tên “a.txt”, điền nội dung bất kỳ.
> - Xem phân quyền của file vừa tạo bằng lệnh ls.
> - Set quyền chỉ đọc cho file với group hiện tại.
> - Kiểm tra set quyền thành công hay chưa (bằng lệnh ls)
> - Thay đổi nội dung của file rồi lưu lại.
> - Dùng tài khoản sudo để thay đổi nội dung file, có thay đổi được không?
> - Kiểm tra lại quyền của file có bị ảnh hưởng sau khi sudo thay đổi file hay không.

**Bài giải**

```shell
#Tao file "a.txt"
touch a.txt && vi a.txt
# Xem phan quyen file vua tao
ls -l a.txt
# -rw-rw-r-- 1 ubuntu ubuntu 49 Jun 10 02:56 a.txt
# Set quyen chi doc file voi group hien tai, & kiem tra
chmod g=r a.txt && ls -l a.txt
# -rw-r--r-- 1 ubuntu ubuntu 0 Jun 10 03:25 a.txt
# Thay doi noi dung file
vi a.txt #E45: 'readonly' option is set (add ! to override)
sudo vi a.txt
# khong thay doi quyen, do dùng user ubuntu
```

[Tương tác về quyền với thư mục và tệp tin trong Linux phần 2](https://funix.udemy.com/course/learn-linux-in-5-days/learn/lecture/1417740#overview)
