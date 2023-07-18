[Lab16.1](https://docs.google.com/document/d/1Q64GYQJCWCaIhKeKrVQQ4LoZ4EtIthCXvw8vP-FDjuk/edit)

Bài tập

> - Di chuyển vào thư mục desktop
> - Tạo folder mới có tên “lab16.1”
> - Di chuyển vào folder “lab16.1”, dùng vim hoặc nano tạo 3 file lần lượt là: file1.txt, file2.txt, file3.txt.
> - Di chuyển thư mục làm việc về desktop.
> - Di chuyển thư mục lab16.1 vào bên trong thư mục “new2” (với thư mục new2 chưa tồn tại, lệnh di chuyển cần tạo mới thư mục new2 rồi di chuyển thư mục lab16.1 vào trong).
> - Xóa thư mục new2

Bài giải

```sh
cd desktop
mkdir lab16.1
cd lab16.1
nano file1.txt
nano file2.txt
nano file3.txt
cd ..
mkdir -p new2 && mv lab16.1 new2/
rm -r new2
```

[Thao tác tệp tin trong Linux (Delete, Copy, Move and Rename)]
(https://funix.udemy.com/course/learn-linux-in-5-days/learn/lecture/1417752#overview)
