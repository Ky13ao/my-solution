[Lab 16.2](https://docs.google.com/document/d/1kjuMvxS8IQBLT8wXaND9u-_B0UVSej1Z_0YgqtKiLgw/edit)

Như chúng ta đã quen với Linux thì hệ thống command cung cấp một tập các ký tự đặc biệt để định nghĩa filenames group. Những ký tự đặc biệt này được gọi là wildcards. Sử dụng chúng có thể select những filename dựa trên một tập các pattern. Bảng sau sẽ định nghĩa cơ bản các wildcard trong Linux.

|   Wildcard    | Ý nghĩa                             |
| :-----------: | :---------------------------------- |
|      \*       | match bất kỳ ký tự nào.             |
|       ?       | match 1 ký tự bất kỳ.               |
| [characters]  | match ký tự nào có trong set        |
| [!characters] | không match ký tự nào có trong set. |
| [[:class:]\]  | match ký tự định nghĩa bởi class    |

Bảng dưới đây định nghĩa các class thường được dùng trong wildcard cuối cùng:

| Pattern | Ý nghĩa                    |
| :-----: | :------------------------- |
| :alnum: | Ký tự chữ và chữ số        |
| :alpha: | Ký tự chữ cái              |
| :digit: | Ký tự chữ số               |
| :lower: | Bất kỳ chữ cái thường nào. |
| :upper: | Bất kỳ chữ cái hoa nào.    |

Bài lab đã cung cấp cho bạn tổng quan các class tương ứng trong wildcard . Bạn hãy xem video bên dưới để có xem chi tiết và lý thuyết cơ bản khi làm việc với wildcard.

Bài tập

> - Tạo các file sau trong 1 folder bất kỳ, rồi di chuyển terminal vào folder đó. các fie có tên lần lượt là: ​​createbackup.sh list.sh lspace.sh speaker.sh listopen.sh lost.sh rename-files.sh topprocs.sh
> - Hiển thị các file bắt đầu bằng chữ “l”
> - Hiển thị các file có format “l?st.sh”
> - Hiển thị các file có format “l[abdcio]st.sh”

Bài giải

```sh
mkdir lab16.2 && cd lab16.2
touch ​createbackup.sh list.sh lspace.sh speaker.sh listopen.sh lost.sh rename-files.sh topprocs.sh
ls l*
# Output: list.sh listopen.sh lost.sh lspace.sh
ls l?st.sh
# Output: list.sh lost.sh
ls l[abdcio]st.sh
# Output: list.sh lost.sh
```

[Làm việc với Wildcard phần 1](https://funix.udemy.com/course/learn-linux-in-5-days/learn/lecture/3088866#overview)
