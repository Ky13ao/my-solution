[Lab 1.2](https://docs.google.com/document/d/1XEsPPbwvsZNJVrJRJtOqh7LIaxxPlttetCjlAnjV180/edit)

# Cài đặt GCC để thao tác C trên Linux

## Tìm hiểu về ngôn ngữ C:

C là một ngôn ngữ lập trình phổ biến nhất thế giới, là ngôn ngữ đơn giản và linh hoạt khi sử dụng. Nó là một ngôn ngữ lập trình có cấu trúc độc lập và được sử dụng rộng rãi để viết các ứng dụng, hệ điều hành như Windows và nhiều chương trình phức tạp khác như Oracle database, Git, Python Interpreter,...

sudo

Ngoài ra, rất nhiều lập trình viên khi học lập trình C đều ví C là “ngôn ngữ mẹ”. Bởi C là cơ sở, nền tảng cho các ngôn ngữ khác và nếu bạn học tốt C thì các ngôn ngữ khác như C++, C#, Java,.. thì có thể dễ dàng chinh phục.

## Ngôn ngữ C hoạt động như thế nào:

C là ngôn ngữ biên dịch và trình biên dịch là một công cụ đặc biệt để biên dịch lập trình và chuyển đổi thành các tệp đối tượng mà máy có thể đọc được. Sau khi được biên dịch, các tệp đối tượng sẽ được trình liên kết hợp lại và tạo ra tệp thực thi duy nhất để chạy lập trình. Sơ đồ dưới đây sẽ giúp bạn hiểu rõ:

| (1)         | (2)           | (3)          |
| ----------- | ------------- | ------------ |
| Writing a   | Compiling a   | Linking      |
| source-code | source-code   | object-files |
| ----------- | ------------- | ------------ |
| filename.c  | filename.obj  | filename.exe |
|             | or filename.o |              |

Ngày nay, có rất nhiều trình biên dịch khác nhau có sẵn bạn có thể dễ dàng sử dụng. Các trình biên dịch này không có nhiều sự khác nhau và có thể đáp ứng hầu hết các nhu cầu, tính năng cần thiết để lập trình C.

## Cài đặt GNU C để biên dịch C trên Linux.

Đối với một người Linux mới và bạn đã từng viết các chương trình C trên hệ điều hành Windows. Bạn sẽ tự hỏi là không biết làm thế nào để bạn có thể biên dịch một chương trình C trên các hệ điều hành Linux bằng cách sử dụng ứng dụng bash Terminal?

Câu trả lời đó là bạn sẽ phải biên dịch chương trình C trên bất kỳ bản phối Linux nào như Ubuntu, Red Hat, Fedora, Debian và bản phân phối Linux khác mà bạn cần phải cài đặt (Ở đây dùng Ubuntu):

- Bộ sưu tập trình biên dịch GNU C.
- Công cụ phát triển.
- IDE hoặc trình soạn thảo văn bản để viết chương trình.

GCC (GNU Compiler Collection) là một tập hợp các trình biên dịch cho các ngôn ngữ lập trình khác nhau như C, C++, … GCC hiện tại có thể cài trực tiếp trên hệ điều hành Linux hoặc thông qua môi trường Linux trên Windows 10.

**Bước 1**: Cài đặt trình biên dịch C và các công cụ liên quan:\
Gõ lệnh apt-get sau đây để cài đặt GNU C trình biên dịch:

> ```sh
> $ sudo apt-get update
> $ sudo apt-get install gcc
> ```

**Bước 2**: Xác minh cài đặt:\
Gõ lệnh sau đây để hiển thị số phiên bản và vị trí của trình biên dịch trên Linux

> ```sh
> $ gcc -v
> ```

Biên dịch và chạy chương trình C trên Linux:\
Bạn có thể tạo một tệp có tên là demo.c bằng cách sử dụng trình soạn thảo văn bản như: text editor, vi, emacs,.. (Cái này không yêu cầu bạn sẽ hiểu các trình soạn thảo ngay bây giờ).

Nếu bạn chưa có tệp tin thì có thể tải [tại đây](https://drive.google.com/file/d/1mCVZ5AnVWlKR0a-EVHG6wUpqWtCC7veL/view?usp=sharing).

Nội dung bên trong của tệp tin sẽ là:

> ```cpp
> #include <stdio.h>
> int main(){
>   printf("Hello world");
>   return 0;
> }
> ```

_(Bạn cũng chưa cần thiết phải hiểu rõ hết câu lệnh, dần dần sẽ được tìm hiểu)._

Để thực thi chương trình demo.c ta sẽ tiến hành biên dịch demo.c thành một tập tin có định dạng .obj. Ta sẽ có câu lệnh sau để tiến hành biên dịch test.c thành test.o
(.o có nghĩa .obj).

> ```sh
> $ gcc -c demo.c -o demo.o
> ```

Sau khi biên dịch xong, dùng lệnh ls để kiểm tra những tập tin đang tồn tại trong thư mục hiện tại.

> ```sh
> $ ls
> ```

Kết quả sẽ có một tập tin demo.o đã được tạo ra như hình trên.
Tiếp theo chuyển demo.o thành file thực thi (file này tương tự file .exe của môi trường Windows) bằng câu lệnh sau:

> ```sh
> $ gcc -o program demo.o
> ```

Với program là tên file thực thi chạy chương trình bạn định nghĩa.

Sau khi thao tác xong, dùng lệnh ls để kiểm tra danh sách tập tin hiện có trong thư mục hiện hành.

Cuối cùng, để thực thi chương trình program dùng câu lệnh sau

> ```sh
> $ ./program
> ```

Bạn thấy màn hình hiển thị ra chữ “Hello World” , không có báo đỏ gì là đã biên dịch thành công.

(Lưu ý: Đối với ngôn ngữ C++ cũng thao tác tương tự, chỉ khác ở cấu trúc câu lệnh. Ở bài học thì sẽ thao tác với ngôn ngữ C).

**_Lưu ý_**: Khi cài đặt và thao tác tương ứng, nếu bạn gặp bất kỳ khó khăn nào thì hãy vào video bên dưới để có xem trực tiếp thực hành tương ứng.

[Cài đặt GCC để thao tác C/C++ trên Linux](https://www.youtube.com/watch?v=Wq-2BjWRIkw&t)
