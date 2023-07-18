[Lab16.3](https://docs.google.com/document/d/1Iw25QZiRjKsuP4LGSSM9dgBCtjyn6eSlJYeqTciVYpE/edit)

Trong bài lab trước chúng ta đã được tìm hiểu lý thuyết cơ bản với wildcard trong Linux, trong bài lab này chúng ta sẽ được thực hành sâu hơn với wildcard.

Bạn hãy xem video bên dưới để có xem chi tiết và thực hành làm việc với wildcard.

Bài tập:

> - Tạo folder mới, có tên “user-info”
> - Dùng vim hoặc nano, tạo các file có tên như trên hình “users-01.list”, “users-01.txt”, …
> - Liệt kê tên các file có đuôi là “\*.txt”
> - Liệt kê tên các file có dạng “users-0\*”
> - Liệt kê tên các file có dạng “users-0<number>\*”, trong đó, <number> là 1 số, số đó lớn hơn 4.

Bài giải:

```sh
mkdir lab16.3 && cd lab16.3
mkdir -p user-info
nano users-01.list users-02.list users-05.list users-06.list users-01.txt users-02.txt users-03.txt
ls *.txt
# output: users-01.txt  users-02.txt  users-03.txt
ls users-0*
# output: users-01.list  users-02.list  users-03.txt   users-06.list  users-01.txt   users-02.txt   users-05.list
ls users-0[5-9]*
# output: users-05.list users-06.list
```

Làm việc với Wildcard phần 2
