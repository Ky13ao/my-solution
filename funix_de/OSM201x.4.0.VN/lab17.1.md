[Lab 17.1](https://docs.google.com/document/d/1zZm1_fc62dcLwVeIlqEz9XUU08rBRz88fwC__9CdUNw/edit)

# Tìm kiếm trong tệp tin và sử dụng Pipes

Trong những bài lab trước, chúng ta đã được làm quen và làm việc với lệnh find trong Linux, nó rất hữu ích trong việc tìm kiếm file. Tiếp tục trong bài lab này, chúng ta sẽ được tìm hiểu về câu lệnh `grep` - giúp bạn tìm chuỗi trong file chỉ định.

## Tìm một chuỗi trong một file:

Đây là cách sử dụng cơ bản và hay dùng nhất, nếu đơn giản bạn muốn tìm một chuỗi nào đó trong chỉ một file duy nhất thì có thể dùng theo cú pháp sau:

$ `grep “chuoi” ten_file`

Kết quả sẽ in ra dòng nào có chứa chuỗi sẽ hiển thị cả dòng trong file đó ra và chuỗi đó sẽ được highlight.

## Tìm chuỗi trong nhiều file cùng lúc:

Để làm được việc này thì bạn cần chỉ định pattern chung của các file muốn thực hiện tìm kiếm:

$ `grep “chuoi” file_pattern`

## Các tùy chọn bổ sung với grep:

| Tùy chọn | Mô tả                                                                                     |
| :------: | :---------------------------------------------------------------------------------------- |
|   `-i`   | Tìm kiếm không phân biệt in hoa, in thường.                                               |
|   `-c`   | Đếm xem trong file chỉ định có bao nhiêu kết quả trả về.                                  |
|   `-n`   | Hiển thị số thứ tự của dòng chứa kết quả (dùng trong một file rất lớn).                   |
|   `-v`   | Tìm kiếm ngược, ví dụ bạn chỉ muốn tìm những dòng không chứa từ khóa đó thì hãy dùng `-v` |

## Sử dụng pipe:

Một trong những công cụ mạnh mẽ cho shell là dấu pipe ( | ). Dấu pipe lấy output từ câu lệnh này và dùng nó làm input cho câu lệnh kế tiếp. Trong một câu lệnh chúng ta có thể dùng bao nhiêu dấu pipes tùy thích, cho tới khi đạt được output bạn muốn xuất ra.

Một trong những công dụng chủ yếu là lọc. Chúng ta dùng dấu pipe để lọc nội dung của một file lớn, để tìm một chuỗi hoặc một từ cụ thể (kết hợp với công cụ grep và sort).

Công thức tổng quát: `cmd1 | cmd2`

Bài lab đã cung cấp cho bạn tổng quan khi làm việc với tìm kiếm trong tệp tin và sử dụng Pipes. Bạn hãy xem video bên dưới để có xem chi tiết chuyên sâu và thực hành tương ứng.

## Bài tập

> - Hiển thị tất cả ứng dụng đang được cài đặt trên máy (dùng lệnh `dpkg -l`)
> - Tìm kiếm xem trong các ứng dụng đã cài có vim hay không (dùng `dpkg` kết hợp pipe và `grep`)
> - Tìm kiếm các ứng dụng đã cài trên máy bắt đầu bằng chữ “a”

## Bài giải

```sh
dpkg -l
dpkg -l | grep vim
dpkg -l | grep '^ii\s*a'
```

[Tìm kiếm trong tệp tin và sử dụng Pipes](https://funix.udemy.com/course/learn-linux-in-5-days/learn/lecture/1417758#overview)
