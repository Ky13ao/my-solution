[Lab 2.1](https://docs.google.com/document/d/1i2prQ4cQIngr8A1Gk5FvCmf3g1Z7ViAdedKDDRJJFo0/edit)

# Làm việc với cấu trúc thư mục của Linux

Trong những bài lab trước, chúng ta đã được thực hành với việc cài đặt Linux trên máy ảo tương ứng, cũng như được làm việc với chương trình C thông qua GCC trên đó. Ở bài lab này, chúng ta sẽ tìm hiểu về cấu trúc thư mục của Linux.

Một hệ thống khi xây dựng luôn được có ‘gốc rễ’ và các nhánh tương ứng. Linux cũng không nằm ngoài phạm vi đó. Như hình bên dưới bạn có thể thấy là đã tồn tại thư mục gốc (Root Directory) và đi kèm với nó là rất nhiều nhánh con (`/bin/`, `/boot/`,...). Giờ chúng ta sẽ đi tìm hiểu chi tiết cùng từng thành phần tương ứng.

#### / - Root

Thư mục root là nơi bắt đầu của tất cả các file và thư mục. Chỉ có root user mới có quyền ghi trong thư mục này.
Lưu ý: /root là thư mục home của root user chứ không phải là /

##### /bin/ - Chương trình người dùng

Thư mục này chứa các chương trình thực thi. Các chương trình chung của Linux được sử dụng bởi tất cả người dùng được lưu ở đây.
VD: ls, ps, ping,...

##### /boot/ - Các file khởi động

Tất cả các file yêu cầu khi khởi động như initrd, ,grub,..

##### /dev/ - Các file thiết bị

Các phân vùng ổ cứng, thiết bị ngoại vi như USB, ổ đĩa cắm ngoài hay bất cứ thiết bị nào gắn kèm vào hệ thống đều được lưu ở đây.

##### /etc/ - Các file cấu hình

Thư mục này chứa các file cấu hình của các chương trình, đồng thời nó còn chứa các shell script dùng để khởi động hoặc tắt các chương trình khác.
VD: /etc/resolv.conf, /etc/logrotate.conf

##### /home/ - Thư mục người dùng

Thư mục này chứa tất cả các file cá nhân của từng người dùng.
VD: /home/john, /home/minh,...

##### /lib/ - Thư viện hệ thống

Chứa các thư viện hỗ trợ cho các file thực thi trong /bin và /sbin.
Các thư viện này thường có tên bắt đầu bằng ld* hoặc lib*.so.\*.

##### /media/ - Các thiết bị gắn (có thể gỡ bỏ)

Thư mục tạm này chứa các thiết bị như CdRom( /media/cdrom) hay các phân vùng đĩa cứng (/media/Data).

##### /mnt/ - Thư mục để mount

Đây là thư mục tạm để mount các file hệ thống.
VD: # mount /dev/sda2/mnt

##### /opt/ - các ứng dụng tùy chọn thêm

Chứa các ứng dụng thêm vào của các hãng khác nhau. Các ứng dụng bổ sung (thêm) nên được cài trong thư mục con của thư mục /opt/

##### /sbin/ - Chương trình hệ thống

Cũng giống như /bin, /sbin cũng chứa các chương trình thực thi, nhưng chúng là những chương trình của admin, dành cho việc bảo trì hệ thống.

##### /srv/ - Dữ liệu của các dịch vụ khác

Chứa dữ liệu liên quan đến các dịch vụ máy chủ như /srv/svs, chứa các dữ liệu liên quan đến CVS.

##### /tmp/ - Các file tạm

Thư mục này chứa các các file tạm thời được tạo bởi hệ thống và các người dùng. Các file lưu trong thư mục này sẽ bị xóa khi hệ thống khởi động lại.

##### /usr/ - Chương trình của người dùng

Chứa các thư viện, file thực thi, tài liệu hướng dẫn và mã nguồn chạy ở level 2 của hệ thống. Trong đó:

- /usr/bin: chứa các file thực thi của người dùng như: at, awk, cc,.. Nếu bạn không tìm thấy chúng trong /bin hãy tìm trong /usr/bin.
- /usr/sbin: chứa các file thực thi của hệ thống dưới quyền của admin như: atd, cron, sshd,...
- /usr/lib: chứa các thư viện cho các chương trình trong /usr/bin và /usr/sbin
- /usr/local: chứa các chương trình của người dùng được cài đặt từ mã nguồn.

##### /proc/ - Thông tin về các tiến trình

Thông tin về các tiến trình đang chạy sẽ được lưu trong /proc dưới dạng một hệ thống file thư mục mô phỏng.
Ngoài ra đây cũng là nơi lưu thông tin về các tài nguyên đang sử dụng của hệ thống như: /proc/version, /proc/uptime,..

> Đây là toàn bộ kiến thức khi làm việc về cấu trúc thư mục trong Linux. Ngoài ra, học viên đọc có chỗ nào khó khăn nào thì hãy vào video bên dưới để có thể xem trực tiếp bài giảng tương ứng.

## Bài tập:

1. In cấu trúc cây thư mục trong linux: dùng lệnh `tree` https://www.geeksforgeeks.org/tree-command-unixlinux/
2. In cấu trúc cây thư mục của folder `etc` (lệnh `tree` và tham số `-d`)

## Bài giải:

```sh
tree
tree -d
```

[Cấu trúc thư mục trong Linux](https://funix.udemy.com/course/learn-linux-in-5-days/learn/lecture/1417724#overview)
