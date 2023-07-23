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

### shell prompt

- self help
  - `man bash`
  - change value of "PS1" environment variable

### shell alias

- key word: `alias`
- syntax:
  - new alias: `alias alias_name=’aliased_command –options’`
  - remove alias: `unalias alias_name`
  - set alias while starting up: write down the alias syntax to file `~/.bashrc`

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

### `<unistd.h>` fork() & exec()

### `<sys/wait.h>` wait() & waitpid()

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

### OS vs Kernel

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

### lời gọi hệ thống(system calls)

- là 1 phương thức tương tác với hệ điều hành thông qua các chương trình.
- là 1 phương pháp để chương trình máy tính yêu cầu 1 dịch vụ (service) từ kernel của hệ điều hành mà nó đang chạy.

- user mode vs. kernel mode

  - user mode:
    - a. DEFINITION:
      _restricted mode_ mà các chương trình ứng dụng đang thực thi và khởi động
    - b. MODES:
      _user mode_ được xem là _restricted mode_
    - c. ADDRESS SPACE:
      trong _user mode_, _1 process_ có không gian địa chỉ riêng của họ.
    - d. INTERRUPTIONS:
      trong _user mode_, nếu xảy ra _interrupt_, CHỈ CÓ 1 _process_ bị lỗi
    - e. DISADVANTAGES:
      trong _user mode_ có 1 số hạn chế khi truy cập các ứng dụng kernel. không thể truy cập trực tiếp
  - kernel mode:
    - a. DEFINITION:
      là _privileged mode_ mà máy tính sẽ truy cập tài nguyên phần cứng
    - b. MODES:
      _kernel mode_ là _system mode_, _privileged mode_
    - c. ADDRESS SPACE:
      trong _kernel mode_, _các processes_ nhận được 1 không gian địa chỉ.
    - d. INTERRUPTIONS:
      trong _kernel mode_, nếu xảy ra _interrupt_, toàn bộ hệ thống đều có thể bị lỗi
    - e. DISADVANTAGES:
      trong _kernel mode_ cả chương trình người dùng và chương trình kernel đều có thể được truy cập

- context switching vs. mode switching

  - context switching
    - là cơ chế lưu trữ và khôi phục lại trạng thái hoặc ngữ cảnh (context) của
      CPU trong khối điều khiển tiến trình (PCB - Process Control Block)
      để có thể tiếp tục thực thi tiến trình từ cùng một thời điểm sau đó.
  - mode switching
    - được sử dụng khi CPU thay đổi các mức đặc quyền (privelege levels).
    - kernel được hoạt động với _privilege_ cao hơn so với tác vụ của _standard user_
    - để truy cập các tác vụ của _user_ được kernel điều khiển, cần phải thực hiện _mode switching_
    - tiến trình đang được thực thi KHÔNG thay đổi trong quá trình _mode switching_
    - CPU sử dụng các chế độ để "bảo vệ" OS khỏi các chương trình độc hại hoặc hoạt động sai,
      cũng như kiểm soát các quyền truy cập đồng thời vào RAM, thiết vị I/O,...

- Nhân bản
  - fork() function
    - fork được sử dụng bởi một tiến trình để tạo ra một bản sao của chính nó
      nghĩa là không gian địa chỉ logic sẽ giống hệt nhau, ngoại trừ ID tiến trình
    - tiến trình có thể tạo ra nhiều trình con của nó.
      khi khởi động máy tính, hệ điều hành sẽ được nạp vào bộ nhớ chính
      và trở thành một tiến trình đặc quyền (privileged process)
      đây được gọi là cha của mọi tiến trình hay còn gọi là tiến trình gốc
      nếu người dùng nhập vào một lệnh terminal thì một tiến trình con mới sẽ được tạo ra từ tiến trình _user shell_
      có thể xem mối quan hệ giữa các tiến trình như một cấu trúc dữ liệu cây
    - nhược điểm
      - chi phí chuyển đổi ngữ cảnh (context switching)
      - lãng phí bộ nhớ do duy trì nhiều bản sao của một tiến trình (cùng 1 không gian địa chỉ)
  - exec() function
    - exec cũng là 1 cơ chế tạo tiến trình được hỗ trợ trên hầu hết các hệ điều hành
    - so sánh với fork:
      - fork():
        - tạo một tiến trình con và sao chép PCB của tiến trình cha
          cho tiến trình con vừa được tạo ra
        - tiến trình con sẽ thực thi tại lệnh nằm ngay sau lệnh fork
          vì tiến trình cha và tiến trình con có chung PCB ngoại trừ
          thông tin về định danh tiến trình
      - exec():
        - tạo một tiến trình con thông qua fork nhưng không sao chép PCB
          của tiến trình cha cho tiên trình con
        - nạp một chương trình mới và bắt đầu thực thi
          từ lệnh đầu tiên của chương trình mới này

## thread & multi-thread

### stack & heap

#### stack

- là cấu trúc dữ liệu tuyến tính
- không bao giờ bị phân mảnh
- stack chỉ truy cập các biến cục bộ
- không thay đổi kích thước
- bộ nhớ stack được phân bổ trong khối liền kề
- stack ko yêu cầu phân bổ lại
- phân bổ và hủy phân bổ Stack được thực hiện theo hướng dẫn của trình biên dịch

#### heap

- là cấu trúc dữ liệu phân nhánh
- có thể bị phân mảnh khi các khối bộ nhớ được cấp phát trước và sau đó được giải phóng
- heap cho phép bạn truy cập các biến toàn cầu
- có thể thay đổi kích thước
- bộ nhớ heap được phân bổ theo bất kỳ thứ tự ngẫu nhiên nào
- luôn yêu cầu phân bổ lại
- phân bổ và hủy phân bổ heap được thực hiện bởi lập trình viên

### single thread

- _process_ là những công việc mà hệ điều hành thực hiện 1 lần
- _thread_ là 1 đơn vị cơ bản trong CPU.
  1 thread sẽ chia sẻ với các luồng khác trong cùng process
  về thông tin data, các dữ liệu của mình
- 1 process có thể chưa nhiều luồng bên trong nó
  vd: khi chúng ta chạy ứng dụng,
  hệ điều hành tạo ra 1 tiến trình và bắt đầu chạy các luồng chính của tiến trình đó
- 1 thread có thể làm bất kỳ task gì 1 process có thể làm
  tuy nhiên, vì 1 tiến trình có thể chứa nhiều luồng, mỗi luồng có thể coi như là một tiến trình nhỏ
- ngoài ra, nhiều luồng nằm trong cùng một tiến trình dùng 1 không gian bộ nhớ giống nhau, trong khi tiến trình thì không

### multi thread

- _process_ có một vùng nhớ riêng, song các _process_ trong cùng 1 _process_ thì dùng chung địa chỉ nhớ
  và các _process_ cũng dùng chung bất cứ tài nguyên nào nằm trong tiến trình đấy.
  có nghĩa là rất dễ chia sẻ dữ liệu giữa các thread
  nhưng cũng rất dễ "nhảy" từ thread này sang thread khác
  dấn đến 1 kết quả không mong muốn
- ưu điểm:
  1. KHẢ NĂNG ĐÁP ỨNG:
     _multi thread_ có thể giúp ứng dụng tương tác có thể hoạt động tốt hơn
     vì ngay cả khi một phần chương trình bị block
     hoặc cần một thời gian dài để hoạt động,
     chương trình nhìn chung vẫn có thể chạy
  2. KHẢ NĂNG CHIA SẺ TÀI NGUYÊN
     các tiến trình có thể chia sẻ dữ liệu thông qua các kỹ thuật
     - _shared memory (vùng bộ nhớ chung)_
     - _message sharing (chia sẻ tin)_
  3. TIẾT KIỆM
     việc cung cấp tài nguyên và dữ liệu cho quá trình tạo _process_ rất tốn kém
     và vì threads tự động chia sẻ data cho _process_ mà nó thuộc về
     việc tạo các thread cho việc _context-switch_ sẽ giúp tiết kiệm chi phí rất nhiều
     không chỉ chi phí mà còn là thời gian
     vì việc tạo một process mới sẽ lâu hơn nhiều so với tạo một thread mới
  4. SCALABITY (MỞ RỘNG):
     lợi ích của multithreaded được thể hiện rõ trong
     ~ _kiến trúc đa xử lý (multiprocessor achitecture)_
     ~ multithread giúp các threads hoạt động song song trong các lõi xử lý khác nhau
     trong khi đối với tiến trình dạng _single-threaded_
     ~ một thread chỉ có thể chạy trên 1 bộ xử lý
     ~ không quan trọng việc có bao nhiêu thread trong hệ thống hiện tại

## quản lý I/O

- bất kỳ thiết bị nào cũng có 1 tập các thanh ghi để truy xuất bởi CPU
- các thanh ghi điều khiển được chia thành 3 loại
  - lệnh: CPU điều khiển thiết bị thực hiện công việc nào đó
  - truyền dữ liệu: truyền dữ liệu giữa CPU và thiết bị
  - trạng thái: Trạng thái của thiết bị
- bản thân thiết bị sẽ kết hợp các thành phần đặc thù khác bao gồm
  - vi điều khiển: giống như CPU, dùng để điều khiển thiết bị
  - bộ nhớ: lưu dữ liệu
  - các logic khác: thực hiện các chức năng khác, ví dụ:
    bộ chuyển đổi tín hiệu tương tự sang số (ADC),..
- các tiêu chuẩn kết nối:
  - PCI Bus
  - PCIe Bus
  - SCSI Bus
  - Peripheral bus
  - Bright bus
  - controllers
- Mỗi trình điều khiển có trách nhiệm truy cập, quản lý và điều khiển thiết bị
- các trình điều khiển thiết bị thường được các nhà sản xuất phần cứng hiện thực
  và cung cấp cho toàn bộ OS tương thích (Windows, Linux, Mac)...
- để hỗ trợ tính đa dạng của các thiết bị, OS thường gom nhóm các thiết bị thành các loại sau:
  - khối dữ liệu (block): ví dụ như ổ đĩa cứng
    - cho phép đọc/ ghi các khối dữ liệu
    - có thể truy cập 1 khối dữ liệu tùy ý
  - ký tự (character): ví dụ như bàn phím
    - nhận/ xuất 1 ký tự
    - dữ liệu được truyền theo từng ký tự
  - mạng (network): truyền một chuỗi dữ liệu vào/ ra
- OS duy trì sự hiện diện của mỗi thiết bị đang kết nối tới hệ thống thông qua việc đóng gói chúng thành 1 file.
- trong các hệ thống dựa trên UNIX, toàn bộ thiết bị xuất hiện như là các file tại thư mục `/dev`
- cách chính để PCI kết nối giữ CPU với thiết bị là làm cho CPU truy cập đến thiết bị giống như truy cập đến bộ nhớ
- việc truy xuất các thanh ghi giống như các lệnh nạp/ lưu thông qua các địa chỉ
- khi CPU ghi dữ liệu tới những địa chỉ này thì bộ điều khiển phải nhận ra được việc truy xuất thiết bị
  và cần được điều hướng đến thiết bị thích hợp
- một phần bộ nhớ vật lý trong hệ thống được dành riêng cho việc tương tác với thiết bị
  kỹ thuật này được gọi là ánh xạ bộ nhớ (Memory Mapped I/O)
- ngoài ra CPU có thể truy xuất đến các thiết bị thông qua các lệnh đặc biệt
  mỗi lệnh này phải chỉ rõ thiết bị thông qua các cổng I/O
  kỹ thuật này được gọi là truy xuất trực tiếp ( I/O port)
- liên lạc giữa thiết bị và CPU có thể thông qua 2 phương thức:
  - ngắt (interupt):
    thiết bị gửi 1 ngắt tới CPU để yêu cầu giao tiếp
    - ưu điểm:
      có thể thông báo trực tiếp đển CPU cần giao tiếp
    - nhược điểm:
      cần nhiều bước xử lý ngắt, trình xử lý ngắt (interupt handler)
      cần phải thiết lập và thiết lập lại mặt nạ ngắt (mask)
      phụ thuộc vào _interupt_ có được phép hay ko
      và cũng có thể do hệ quả của dữ liệu rác trên cache
      liên quan đến việc thực thi của trình xử lý ngắt
  - thăm dò (polling):
    CPU đọc các thanh ghi của trạng thái của thiết bị để quyết định giao tiếp
    - ưu điểm:
      OS có thể truy xuất vào thời điểm thích hợp
      có thể là khi dữ liệu rác trên cache ảnh hưởng không quá lớn
    - nhược điểm:
      gây ra sự trì hoãn mặt dù sự kiện đã hiện diện
      và CPU có thể quá tải vì liên tục phải thực hiện việc thăm dò
  - việc lựa chọn phương pháp ngắt hay thăm dò
    thì phụ thuộc vào loại thiết bị và mục tiêu tối đa hóa thông lượng và giảm độ trễ
    hay phụ thuộc vào độ phức tạp của trình xử lý ngắt và những đặc trưng của thiết bị
- chỉ với sự hỗ trợ cơ bản từ PCI và các bộ điều khiển PCI tương ứng trên các thiết bị
  hệ thống có thể truy cập hoặc yêu cầu mọi hoạt động từ một thiết bị sử dụng phương pháp gọi là lập trình I/O

- CPU có thể ra lệnh cho thiết bị thông qua việc ghi vào các thanh ghi lệnh (command)
  và di chuyển dữ liệu xung quanh bằng cách truy cập vào các thanh ghi truyền dữ liệu của thiết bị
  ví dụ, CPU sử dụng network interface card (thẻ giao diện mạng) để gửi gói TCP thông qua lập trình I/O
  - 1. CPU viết lệnh để yêu cầu gói tin
  - 2. CPU sao chép gói tin vào thanh ghi dữ liệu
  - 3. lặp lại cho đến khi gói tin được gửi
- đối với 1 gói tin 1500bytes và thanh ghi 8bytes
  nó sẽ cần 1 truy cập để ghi lệnh
  và 188 truy cập để truyền dữ liệu
  tổng cộng là 189 truy cập
