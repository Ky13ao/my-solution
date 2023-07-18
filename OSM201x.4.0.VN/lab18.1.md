[Lab18.1](https://docs.google.com/document/d/1i8_brdHB7emBPFIItb_7iNnq2v6RBYTE8GmnqTzLUCI/edit)

# Tùy chỉnh Shell Prompt

Trong các biến môi trường của hệ thống dựa trên Linux thì sẽ là một tập hợp các giá trị động được đặt tên, được lưu trữ trong hệ thống được sử dụng bởi các ứng dụng được khởi chạy trong shell. Trong bài lab này chúng ra sẽ được thao tác với shell Prompt thông qua biến $PS1 và $prompt.

## Định nghĩa biến PS1:

PS (Prompt Statement) sử dụng để tùy chỉnh chuỗi nhắc của bạn trong cửa sổ đầu cuối để hiển thị thông tin bạn muốn. PS1 là biến chính điều khiển dấu nhắc dòng lệnh của bạn.

## Các biến của PS1:

Mặc định của biến PS1 sẽ có định dạng như sau:

`[04:21:12][root@minh ~] $echo $PS1`

`[\T][\u@\h \W]$`

> Trong đó:
>
> `\u`: tên tài khoản bạn đang sử dụng. \
> `\h`: tên máy chủ của bạn. \
> `\W`: thư mục cuối cùng trong thư mục bạn đang làm việc hiện tại. \
> `\T`: Giờ-phút-giây theo định dạng 12h.

Ngoài ra còn rất nhiều các biến khác như là:

| Biến | Mô tả                                                         |
| :--- | :------------------------------------------------------------ |
| `\a` | Một dãy ký tự ASCII (07)                                      |
| `\]` | Kết thúc của một chuỗi ký tự ko hiển thị (non-printing).      |
| `\h` | Hiển thị tên máy chủ của bạn từ đầu cho đến dấu “.” đầu tiên. |
| `\j` | Hiển thị ra số lượng công việc được quản lý bởi shell.        |
| `\n` | In ra thêm dòng mới.                                          |
| `\s` | Hiển thị ra tên của shel.                                     |
| `\d` | Hiển thị ngày tháng theo định dạng (thứ - ngày - tháng).      |

Còn rất nhiều biến nữa, bạn có tham khảo [tại đây](https://tldp.org/HOWTO/Bash-Prompt-HOWTO/bash-prompt-escape-sequences.html).

## 2 ví dụ cơ bản về PS1:

**VD1**: Hiển thị thêm giờ - phút - giây theo định dạng 12 giờ:

> `[root@minh ~ ] $ export PS1="[\T][\u@\h \W]\$ "` \
> `[03:57:12][root@minh ~ ]$`

**VD2**: Hiển thị số giây mà chỉ muốn hiển thị giờ - phút theo định dạng 24 giờ.

> `[03:59:23][root@minh ~ ] $ export PS1="[\A][\u@\h \W]\$ "` \
> `[15:29][root@minh ~ ]$`

Bài lab đã cung cấp cho bạn tổng quan về tùy chỉnh Shell Prompt sử dụng $PS1. Bạn hãy xem video bên dưới để có xem chi tiết kiến thức nâng cao và thực hành với PS1 và cũng như đối với $prompt.

## Bài tập:

> 1. Hiển thị giờ phút giây tại thời điểm nhập command theo định dạng 12 giờ (như VD1)
> 2. Hiển thị giờ, phút tại thời điểm nhập command (định dạng 24 giờ).
> 3. Hiển thị username, hostname (tên máy), và thư mục đang làm việc.
> 4. Chỉ hiển thị thư mục làm việc

## Bài giải

```sh
export PS1="[\T][\u@\h \W]\$ "
export PS1="[\A][\u@\h \W]\$ "
export PS1="[\u@\h \W]\$ "
export PS1="[\W]\$ "
```

[Tùy chỉnh Shell Prompt](https://funix.udemy.com/course/learn-linux-in-5-days/learn/lecture/1417762#overview)
