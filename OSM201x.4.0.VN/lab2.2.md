[Lab 2.2](https://docs.google.com/document/d/1fuRNQWW9Vs6iPAe4HXK7k_38fg-eGW-8AwqE9gCJE5w/edit)

# Làm việc với Shell

Trong bài lab này chúng ta sẽ được làm quen với khái niệm Shell trong Linux. Vậy Shell là gì? có tác dụng ra làm sao trong Linux?

### Khái niệm về Shell:

- Shell là chương trình người dùng đặc biệt, cung cấp giao diện cho người dùng sử dụng các dịch vụ hệ điều hành. Shell chấp nhận các lệnh có thể đọc được từ người dùng và chuyển đổi chúng thành thứ mà Kernel có thể hiểu được.
- Nó là một trình thông dịch ngôn ngữ lệnh thực thi các lệnh được đọc từ các thiết bị đầu cuối vào như keyboard hoặc từ file. Shell được bắt đầu khi người dùng đăng nhập hoặc khởi động Terminal.

### Phân loại:

Shell được chia làm 2 loại:

- Command Line Shell
- Graphical Shell (GUI).

#### 2.1. Command Line Shell:

- Shell có thể được truy cập bởi người dùng bằng cách sử dụng command line interface. Một chương trình đặc biệt có tên là Terminal trong Linux, được cung cấp để nhập vào các lệnh có thể đọc được của người dùng như ‘cat’, ‘ls’,... và sau đó nó được thực thi.

- Làm việc với command line shell sẽ có một chút khó khăn cho người mới bắt đầu bởi vì thật khó để nhớ hết các câu lệnh, nhưng khi đã quen thì nó thuận tiện và mạnh mẽ, nó cho phép người dùng lưu trữ các lệnh trong một file và thực thi chúng cùng nhau.

#### 2.2. Graphical Shells (GUI):

- Graphical Shells cung cấp phương tiện để thao tác với các chương trình dựa trên graphical user interface (GUI), bằng cách cho phép các hoạt động như: open, close, move,.. cũng như chuyển trọng tâm giữa các cửa sổ.
- Một số shell có sẵn trong các hệ thống Linux:
  - **BASH** - Được sử dụng rộng rãi nhất trong các hệ thống Linux.
  - **CSH** - Cú pháp và cách sử dụng của C shell rất giống với ngôn ngữ lập trình Shell.
  - **KSH** - Cơ sở cho các thông số kỹ thuật tiêu chuẩn của POSIX Shell.

> Đây là toàn bộ kiến thức khi làm việc về Shell trong Linux. Ngoài ra, học viên đọc có chỗ nào khó khăn nào thì hãy vào video bên dưới để có thể xem trực tiếp bài giảng tương ứng.

### Bài tập:

> Trình bày ra file word trả lời các câu hỏi sau:
>
> 1. Sự khác nhau giữa GUI và CLI là gì?
> 2. Trường hợp nào có thể dùng GUI?
> 3. Khi muốn điều khiển một instance EC2 trên AWS chạy hệ điều hành window, có thể sử dụng GUI không? Vì sao?
> 4. Khi muốn điều khiểu một instance EC2 trên AWS chạy hệ điều hành Linux, có thể sử dụng GUI không? Vì sao?

### Bài giải:

> 1. GUI (Graphic User Interface) giao diện trực quan người dùng, GUI được người dùng sử dụng để giao tiếp với máy tính bằng các đồ họa trực quan có thể thao tác bằng các hoạt động ấn kéo thả chuột thông qua các biểu tượng, hộp thoại, cửa sổ. Phương pháp để người dùng giao tiếp với máy tính phổ biến.\
>    CLI (Command Line Interface) giao diện dòng lệnh, khác với GUI, CLI chỉ có những dòng lệnh, những dòng lệnh này được hiểu như đoạn văn bản/ mã hoặc script, CLI tận dụng các hiệu năng của hệ thống để thực hiện tác vụ nhanh hơn thay vì dùng tài nguyên đó hiển thị giao diện đồ họa.
> 2. Hầu hết các ứng dụng được tạo ra hiện nay đều có GUI và để thân thiện với người dùng nhất, dễ sử dụng, dễ tùy chỉnh. Khi người dùng không quen với việc sử dụng dòng lệnh, cần sự linh hoạt, tương tác trực quan và dễ dàng thao tác với các ứng dụng phức tạp như duyệt web, chỉnh sửa hình ảnh/ video, chỉnh sửa định dạng văn bản
> 3. AWS EC2 có hỗ trợ GUI cho windows thông qua Remote Desktop Protocol cho phép kết nối GUI windows từ xa
> 4. AWS không hỗ trợ GUI cho linux, nhưng chúng ta có thể cài đặt các giao diện đồ họa như GNOME (vd ubuntu-desktop), KDE và sử dụng các công cụ remote như VNC (Virtual Network Computing) để kết nối GUI của instance

[Shell trong Linux](https://funix.udemy.com/course/learn-linux-in-5-days/learn/lecture/1417726#overview)
