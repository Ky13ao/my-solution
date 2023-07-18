# Operating System

## bash/ shell

### basic command

#### print

- `echo`: print a line of text
- `printf`: format and print file
- `yes`: print a string until interrupt

#### word count

- `wc`
  `-l` count lines
  `-c` count characters
  `-w` count words
  add `|` before to count current print command result

#### read

- read from output and assign to a variable:
  some_var=`ps aux | wc -l` , no space after `=`

#### file

- các thao tác cơ bản về file

  - `mv` move file
  - `cp` copy file
  - `dd` convert & copy file
  - `install` copy files & set attributes
    ex. install /path/to/file1 /target/directory
  - `rm` remove files/directory

- so sánh từng dòng nội dung trong 2 file

  - `diff`
    - usage: `diff file1 file2`
  - `sdiff`
  - `vimdiff`

- thay đổi nâng cao về file
  - `shred` remove files more securely
  - `touch` change file's timestamp
  - `chmod` change access permission
    `chown` change file's owner
    `chgrp` change group owner ship

#### file space usage

- `df` report
- `du` estimate
- `stat` status
- `truncate` shrink/extend the size of file

### user context

- `id` user identity
- `logname` current login name
- `whoami` effective username
- `groups` group names a user is in
- `users` current all login users
- `who` who is current login

### switch user

#### `su`

- usage:
  `su -l username`
  `su username`
  su with no username force user log in to root user
  example:
  `su -root` or `su-`
  `su root` or `su`

- help:
  `su -h`

#### `sudo`

- usage:
  `sudo -u username command`

- grant sudo user:
  `visudo` or edit file at `/etc/sudoers`

- help:
  `sudo -h`

#### `su-`

- usage:
  `su-` or `su -l` or `su --login`

- affect to:
  home, shell, user, logname, path, env of user

- note:
  `su-` used password from user, `sudo` used password from root

### working context

- `pwd` current working directory
- `printenv` all or some environment variables
- `tty` a file name of terminal on standard output

### system context

- `date` print/ set date & time
- `arch` machine hardware name
- `nproc` number of available processes
- `uname` system information
- `hostname` print/ set system name
- `hostid` numeric host identifier
- `uptime` print system update & load

### process control

#### `kill`

#### delaying

- `sleep`

#### process stats

- `ps`

### job scheduler

#### `crontab`

- option:
  `-l` list
  `-e` edit
  `-u "user"` user's jobs

- job setting:
  ` * * * * * /bin/execute/this/script.sh`

  - minute, hour, and day can be set with wildcards such as `*` or `,`
    minute (0-59)
    hour (0-23)
    day of month(1-31)
    month(1-12)
    day of week (0-6 - Sunday to Saturday)
    example: ` 0 1 * * 5  script.sh` job se chay 1:00 thu sau hang tuan

  - special keywork:
    `@reboot`: run once reboot
    `@yearly`: run once a year
    `@annually`: similiar @yearly
    `@monthly`: run once a month
    `@weekly`: run once a week
    `@daily`: run once a day
    `@midnight`: similiar @daily
    `@hourly`: run once an hour
    example: `@daily script.sh`

### shell history

- key shortcut: Ctrl + R

- 4 ways redo command just done:
  up arrow
  command `!!`
  command `!-1`
  combined keys Ctrl + P

- index history: `history | more`
  redo:
  `!index` eg: `!2001`

- history expansion:
  `!!` redo command just done
  `!10` redo 10th command from `history`
  `!-2` redo 2nd previous command
  `!string` redo the string command that has been done
  `!?string` redo the command contains "string" that has been done
  `^str1^str2^` replace "str1" by "str2" in last command then redo
  `!string:n` obtain nth argument in last command starts with "string"

### shell alias

### shell prompt

## c++

### `man` cli

- manual user guides

### file & folder

- `create()`

  - tạo file chưa tồn tại trong folder
  - cấu trúc:
    `int create( *filename, mode_t mode)`
    - _filename_: tên file
    - _mode_: cho biết quyền của tệp mới

- `open()`

  - lấy thông tin bộ mô tả của tệp tin
  - cấu trúc:
    `file = open(*filename, mode, permission)`
    - _filename_ : đường dẫn và tên tệp tin cần mở
    - _mode_ : phương thức để mở tệp tin (O_CREATE | O_RDWR)
    - _permission_ : được sử dụng để xác định quyền truy cập của tệp. ex: 0777

- `read()`

  - được sử dụng để _đọc_ nội dung từ tệp
  - cú pháp:
    `length = read(file_descriptor, buffer, max_len)`
    - _file_descriptor_ : là bộ mô tả của tệp tin (vd: file, 0)
    - _buffer_ : là tên bộ đệm nơi dữ liệu sẽ được lưu trữ
    - _max_len_ : là số chỉ định dữ liệu tối đa có thể đọc được
  - nếu đọc thành công function sẽ trả về số byte thực tế

- `write()`
  - được sử dụng để _ghi_ nội dung từ tệp
  - cú pháp:
    `length = write(file_descriptor, buffer, len)`
    - _file_descriptor_ : là bộ mô tả của tệp tin (vd: file, 0)
    - _buffer_ : là tên bộ đệm nơi dữ liệu sẽ được lưu trữ. vd: `"Hello World"`
    - _len_ : là số chỉ định dữ liệu tối đa có thể đọc được
  - nếu đọc thành công function sẽ trả về số byte thực tế

### `<pthread.h>`

- thư viện xử lý luồng tiến trình
- khai báo biến: `pthread_t threadVar;`
- usage:
  `pthread_create(&threadVar, NULL, &function, NULL)`
  `pthread_join(threadVar, NULL)`

### `<semaphore.h>`

- thư viện xử lý đồng bộ theo cấu trúc semaphore
- khai báo biến: `sem_t semVar;`
- usage:
  `sem_init(&semVar, giá trị chia sẻ = 0, giá trị khởi tạo = 1);`
  (sem_unit)[https://man7.org/linux/man-pages/man3/sem_init.3.html]
  `sem_wait(&semVar); // wait for resource access`
  `sem_post(&semVar); // post to mark process as done`
  `sem_destroy(&semVar); // gỡ biến khỏi bộ nhớ`

## thuật toán lập lịch

## đồng bộ hóa

### tạo bộ nhớ chung

- tạo ra vùng bộ nhớ chung để giao tiếp
- ưu điểm
  - giao tiếp giữa các tiến trình nhanh hơn
  - giao tiếp đồng thời 1 vùng dữ liệu
  - tăng tốc khả năng tính toán
  - chia bài toán lớn thành nhiều bài toán nhỏ
  - module hóa hệ thống dùng chung bộ nhớ
- cơ chế đồng bộ hóa
  - phải đảm bảo duy trì tính nhất quán của dữ liệu
  - đảm bảo chỉ 1 quy trình có thể thay đổi dữ liệu tại 1 thời điểm
  - các cơ chế đồng bộ hóa điển hình là: mutex, semaphore,...
  - phải đáp ứng 3 yêu cầu:
    - mutual exclusion / loại trừ lẫn nhau
    - progress / tiến trình
    - bounded waiting / giới hạn chờ đợi

### các cơ chế đồng bộ hóa

#### TSL

#### mutex lock

- là 1 cơ chế phần mềm ( software machinism)
- được triển khai trong chế độ người dùng (user mode)
- không cần sự hỗ trợ từ hệ điều hành
- là giải pháp cho busy waiting, giữ CPU luôn bận rộn
- sử dụng 2 tiến trình trở lên

- Busy waiting
  - critical section
    - phần tử đầu chưa sử dụng ( Lock = 0)
      phần tử đầu đã sử dụng ( Lock = 1)
    - dùng để cản trở các tiến trình bước vào. đây là quy tắc Progress
    - pseudo code: _Lock Variable_ | _Process Synchronize_ | _Gate Vidyalay_
  - nhược điểm
    - làm tiêu tốn thời gian của CPU
    - vấn đề đảo ngược ưu tiên ( preverse inversion):
      xảy ra khi áp dụng thuật toán lập lịch ưu tiên
    - nguyên nhân
      - hầu hết các giải pháp Busy-waiting loại trừ lẫn nhau.
        Tuy nhiên Busy-waiting ko phải là cách phân bổ tài nguyên tối ưu
        vì nó khiến CPU luôn phải bận rộn để kiểm tra tình trạng của critical section
      - vấn đề đảo ngược ưu tiên, luôn có khả năng khóa quay bất cứ lúc nào
        khi có 1 tiến trình có mức ưu tiên cao hơn

#### semaphore

- bản chất của semaphore là 1 cấu trúc dữ liệu
- được dùng để đồng bộ tài nguyên và đồng bộ hoạt động
- gồm 2 thành phần chính:
  - _count variable_
    giá trị cực đại của biến count thể hiện số lượng thread tối đa
    được sử dụng trong critical resource tại cùng một thời điểm
  - _wait list_
- counting semaphore là 1 semaphore với max(count) > 1
- binary semaphore là 1 semaphore mà các _count variables_ chỉ có 0 và 1
- binary semaphore có 1 số điểm tương đồng với mutex lock
  _thuờng được dùng để làm giải pháp cho các vấn đề của critical section với nhiều process_

#### wait and signal

- `wait()`

  - chặn tiến trình gọi cho đến khi 1 trong các tiến trình con của nó kết thúc hoặc nhận được tín hiệu.
  - sau khi tiến trình con kết thúc. tiến trình sẽ đợi lệnh gọi từ hệ thống.
  - tiến trình con có thể chấm dứt theo các cách sau:
    - `exit()`
    - trả 1 `int` từ `main`
    - nhận được tín hiệu ( từ hệ thống hoặc quy trình khác) có hành động mặc định là chấm dứt

- `signal()`

  - cài đặt 1 trình xử lý tín hiệu mới cho tín hiệu có ký hiệu số
  - trình xử lý tín hiệu được đặt là _sighandler_ có thể là
    - chức năng do người dùng chỉ định
    - _SIG_IGN_
    - _SIG_DFL_

- đáp ứng 3 yêu cầu quan trọng

  - _mutual exclusion_
    khi _process_ đang thực thi trong _critical section_,
    thì ko _process_ nào được thực thi vào _critical section_
  - _progress_
    nếu ko có _process_ nào trong _critical section_ và các _process_ khác đang chờ bên ngoài
    thì chỉ những _process_ không thực thi trong phần còn lại của chúng
    mới có thể tham gia vào việc quyết định cái nào sẽ đi vào _critical section_ tiếp theo
    và việc lựa chọn có thể không được hoãn vô thời hạn.
  - _bounded waiting_
    phải tồn tại 1 giới hạn về số lần mà các _process_ khác được vào _critical section_ của chúng
    sau khi một _process_ được đưa ra yêu cầu để vào _critical section_ của nó
    trước khi yêu cầu đó được chấp nhận

- các tính năng khác
  - giải pháp _multiple process_
  - thực hiện trong chế độ kernel
  - ổ cứng độc lập

### deadlock

- mọi tiến trình đều cần 1 số tài nguyên để hoàn thành tiến trình thực thi
  tuy nhiên tài nguyên được cấp theo 1 thứ tự tuần tự.
  - tiến trình yêu cầu 1 số tài nguyên
  - os cung cấp tài nguyên nó có sắn, nếu ko tiến trình phải chờ
  - tiền trình sử dụng nó và giải phóng sau khi dùng
- là 1 tình huống trong đó mỗi tiến trình máy tính chờ đợi một tài nguyên đang được gán cho 1 số tiến trình khác
- deadlock vs. starvation
  - Deadlock
    a. là tình huống ko có Process nào bị chặn và ko có Process nào tiếp diễn.
    b. là sự chờ đợi vô thời hạn
    c. mỗi lần deadlock luôn là 1 lần starvation
    d. resource được yêu cầu bị chặn bởi Process khác
    e. deadlock xảy ra khi mutual exclution, hold và wait, no preemption và circular wait
  - Starvation
    a. là tình huống Process có độ ưu tiên thấp bị chặn và Process có mức độ ưu tiên cao vẫn tiếp tục.
    b. là sự chờ đợi lâu dài nhưng ko phải vô thời hạn
    c. mọi starvation không phải là deadlock
    d. resource được yêu cầu liên tục được sử dụng bởi các process ưu tiên cao hơn
    e. nó xảy ra do mức độ ưu tiên và quản lý tài nguyên không được kiểm soát
- 4 điều kiện cần thiết để xảy ra deadlock
  1. Mutual Exclustion
     1 tai nguyen chi co the duoc chia se theo cac Mutual Exclusion. nếu 2 tiến trình ko thể sử dụng cùng một tài nguyên cùng 1 lúc
  2. Hold and Wait
     1 tiến trình đợi 1 số tài nguyên trong khi giữ tài nguyên khác cùng 1 lúc
  3. No preemption
     process đã từng được lên lịch sẽ được thực hiện cho đến khi hoàn thành.
     không có process nào khác có thể được lên lịch bởi người lập lịch trong thời gian đó
  4. Circular Wait
     tất cả tiến trình phải chờ tài nguyên theo cách tuần hoàn
     để process cuối cùng đang đợi tài nguyên mà đang được process đầu tiên nắm giữ
- 4 phương pháp kiểm soát deadlock:
  1. Deadlock prevention:
     có thể được ngăn chặn bằng cách loại bỏ bất kỳ điều kiện nào trong 4 điều kiện cần thiết
     đó là loại trừ lẫn nhau, hold & wait, ko có quyền ưu tiên, vòng chờ tuần hoàn
  2. Deadlock Avoidance:
     yêu cầu đối với bất kỳ tài nguyên nào sẽ được cấp nếu trạng thái kết quả của hệ thống không ra bế tắc trong hệ thống.
     trạng thái của hệ thống sẽ liên tục được kiểm tra trạng thái an toàn và ko an toàn.
  3. Deadlock Ignorance:
     kỹ thuật được sử dụng rộng rãi nhất để bỏ qua deadlock
     nó cũng được dùng cho tất cả mục đích sử dụng của end-user
     nếu có deadlock trong hệ thống, thì OS sẽ khởi động lại hệ thống để hoạt động tốt hơn
     phương pháp giải quyết các vấn đề khác nhau tùy theo mọi người.
  4. Deadlock Detection và Recovery:
     hệ điều hành không áp dụng bất kỳ cơ chế nào để tránh hoặc ngăn chặn các bế tắc
     do đó, hệ thống cho rằng bế tắc chắc chắn xảy ra
     để thoát khỏi deadlock, OS sẽ kiểm tra định kỳ hệ thống xem có bầt kỳ bế tắc nào ko
     trong trường hợp, nó tìm thấy bất kỳ bế tắc nào thì hệ điều hành sẽ khôi phục hệ thống
     bằng 1 số kỹ thuật khôi phục.
- thuật toán banker
  - được sử dụng trong trường hợp tài nguyên có nhiều phiên bản khác nhau
    cho phép quản lý các tài nguyên không được rơi vào tình trạng deadlock, hết hoặc không an toàn.
  - thuật toán này được các ngân hàng sử dụng để phân bổ và xử lý các tài khoản vay trong hệ thống của mình
  - thuật toán sẽ tạo ra 1 chuỗi an toàn bằng cách sử dụng một số dữ liệu có sẵn
    như các tài nguyên tối đa được yêu cầu và tổng số tài nguyên có sẵn trong hệ điều hành.

### file & folder system

#### hệ thống tệp tin

- quyết định cách lưu trữ và sắp xếp nội dung của phương tiện lưu trữ (bộ nhớ phụ)
- các hệ tệp tin như là:
  - btrfs
  - xfs
  - zfs
- các hệ thống tệp tin khác nhau
  - khía cạnh triển khai
  - trường hợp sử dụng
- rất cần thiết để cho OS hoạt động một cách hiệu quả
- có thể là bộ nhớ thứ cấp của
  - máy tính
  - bộ nhớ flash
- nội dung có thể là các tệp hoặc thư mục
- hầu hếu thời gian, một thiết bị lưu trữ có 1 số phân vùng
  mỗi phân vùng này được định dạng bằng một hệ thống tệp tin trống cho thiết bị đó
  phân vùng giúp phân tách dữ liệu trên bộ lưu trữ thành các phân đoạn tương đối nhỏ hơn và đơn giản hơn
  những khối này là các tập tin và thư mục
- cung cấp khả năng lưu trữ dữ liệu liên quan đến tệp, chẳng hạn như tên, phần mở rộng, quyền,...
- những thuộc tính của tệp tin:
  1. tên của tệp tin
  2. kiểu của tệp tin
  3. vị trí của tệp tin
  4. kích thước của tệp tin
  5. bảo vệ thông tin của tệp tin
  6. thời gian và ngày

#### số khối

- khái niệm
  - _ổ đĩa cứng (hard disk)_ là thiết bị lưu trữ thứ cấp mà chúng ta có thể sử dụng để lưu trữ dữ liệu
  - _số khối vật lý_ là số khối của những số khối có trong hard disk
  - _số khối logic_ là số khối của tệp tin tương ứng

### phân bổ tệp

#### phân bổ tệp liền kề

##### lợi ích

1. đơn giản thực hiện
2. thời gian để đọc một tệp là rất ngắn
3. truy cập ngẫu nhiên (random access) rất dễ dàng

##### nhược điểm

1. vấn đề khai báo kích thước
2. vần đề phân mảnh bên ngoài
3. phân mảnh nội bộ

#### phân bổ danh sách liên kết

- là 1 dạng phân bổ không liên tục
- các khối tệp tin không cần được đặt trong các khối đĩa liền kề
- mỗi khối tệp tin sẽ có địa chỉ của khổi tệp tin tiếp theo ở đầu

##### ưu điểm

- linh hoạt hơn về kích thước tệp tin
- có thể được tăng lên dễ dàng vì hệ thống không phải tìm kiếm một đoạn bộ nhớ liền kề
- phương pháp này không bị phân mảnh bên ngoài
- sử dụng tốt hơn về mặt sử dụng bộ nhớ

##### nhược điểm

- phân bổ liên kết chậm hơn do:
  các khối tệp tin được phân phối ngẫu nhiên trên đĩa
- cần có một số lượng lớn tìm kiếm để truy cập từng khối riêng lẻ
- truy cập ngẫu nhiên (random access) rất mất nhiều thời giangian
- _nhược điểm chính_:
  - không cung cấp quyền truy cập ngẫu nhiên vào một khối cụ thể
  - để truy cập 1 khối chúng ta cần phải truy tập tất cả các khối trước đó

#### phân bổ FAT

- được sinh ra để khắc phục nhược điểm chính của phân bổ danh sách liên kết

##### ưu điểm

- sử dụng toàn bộ khối đĩa cho dữ liệu
- một khối đĩa hỏng không làm mất đi tất cả các khối liên tiếp
- truy cập ngẫu nhiên được cung cấp mặc dù không quá nhanh
- chỉ cần duyệt FAT trong mỗi thao tác tệp tin

##### nhược điểm

- mỗi khối đĩa cần một mục nhập FAT (FAT entry)
- kích thước FAT có thể rất lớn tùy theo số lượng mục nhập FAT
- số mục nhập FAT có thể giảm bằng cách tăng kích thước khối nhưng nó cũng sẽ tăng phân mảnh nội bộ

## kernel

- OS vs Kernel
  - OS:
    - là 1 trong những thành phần quan trọng nhất giúp quản lý tài nguyên phần mềm và phần cứng máy tính.
    - là chương trình đầu tiên bắt đầu khi máy tính khởi động.
    - giống như 1 phần mềm hệ thống (system software).
    - mục đích chính của hệ điều hành là cung cấp bảo mật.
    - nó cung cấp một giao diện giữa phần cứng và người dùng.
    - đối với máy tính, không có hệ điều hành sẽ ko chạy được
  - Kernel
    - là thành phần cốt lõi của hệ điều hành giúp dịch các câu truy vấn của người dùng thành ngôn ngữ máy
    - là chương trình đầu tiên khởi động khi hệ điều hành chạy
    - là phần mềm hệ thống, là một thành phần quan trọng của hệ điều hành
    - mục đích chính của kernel là quản lý bộ nhớ, đĩa và tác vụ
    - nó cung cấp một giao diện giữa ứng dụng và phần cứng
    - không có kernel, hệ diều hành không chạy được
