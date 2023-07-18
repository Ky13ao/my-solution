[Lab18.2](https://docs.google.com/document/d/1oTXvtDFyOvmrW-QRNNbkJcw3N2Bp0V0ff3utJOo10K8/edit)

# Làm việc với Shell Aliases

Khi bạn sử dụng Linux và dùng nhiều đến chế độ dòng lệnh, chắc chắn sẽ có những câu lệnh bạn sử dụng thường xuyên. Bạn sử dụng những câu lệnh ấy lặp đi lặp nhiều lần trong một ngày. Khi đó bạn sẽ cần đến alias để giảm bớt thời gian cho việc gõ đi gõ lại các câu lệnh đó. Trong bài lab này chúng ta sẽ thực hiện thao tác với alias tương ứng.

## Thiết lập và quản lý các alias:

Alias được chia thành 2 loại là permanent alias và temporarily alias. Temporarily alias sẽ mất đi mỗi khi phiên làm việc trên bash shell của bạn kết thúc. Còn permanent alias sẽ không bị mất đi trừ khi bạn xóa nó.

### Temporarily alias:

Để thêm mới 1 alias ta dùng lệnh: \

> `alias alias_name=’aliased_command –option’`

Để xóa 1 temporarily alias: \

> `unalias alias_name`

### Permanent alias:

Đối với các permanent alias, chúng sẽ được định nghĩa và lưu trong file `~/.bashrc` hoặc `~/.bash_profile`. Ngoài ra ta cũng có thể lưu riêng các alias ra 1 file khác ví dụ `~/.alias`. Khi đó cần thêm đoạn script sau vào file `~/.bashrc`.

Việc tạo 1 alias trong các file này cũng hoàn toàn tương tự như khi bạn tạo 1 temporarily alias. Với mỗi 1 alias mới sẽ được thêm vào bằng 1 dòng với cú pháp.

> `alias alias_name=’aliased_command –options’`

Sau khi thêm các alias và lưu file lại, để các alias mới có thể hoạt động ngay tại phiên làm việc hiện tại, bạn dùng lệnh:

> `source ~/.bashrc`

Hoặc

> `. ~/.bashrc`

Để xem danh sách các alias, ta dùng câu lệnh:

> `alias`

Màn hình terminal sẽ liệt kê tất cả các alias đang có bao gồm cả permanent và temporarily tương ứng. Bạn có thể thấy.

## Một số alias phổ biến:

### Quản lý các gói:

> `alias ai=’sudo apt-get install’` \
> `alias ar=’sudo apt-get remove’` \
> `alias au=’sudo apt-get update’` \
> `alias aug=’sudo apt-get upgrade’`

### File và thư mục:

> `alias ..=’cd ..’` \
> `alias ...=’cd ../..’` \
> `alias ....=’cd ../../..’` \
> `alias du = ‘du -h’`

Bài lab đã cung cấp cho bạn tổng quan về việc làm việc với alias. Bạn hãy xem video bên dưới để có xem chi tiết kiến thức và thực hành tương ứng.

## Bài tập

> - Tìm kiếm folder cài đặt python trên máy (dùng lệnh `which python` hoặc `which python3`), nếu chưa cài thì cài vào.
> - Thêm alias lệnh `“cd PYTHONPATH”` vào file path.
> - Dùng lệnh `source ./bash_profile` (tùy phiên bản mà có các lệnh để kích hoạt file bash khác nhau).
> - Gõ tên alias xem có thể chuyển đến thư mục chứa python hay không? (nếu di chuyển được thì hoàn thành bài tập)

## Bài giải

```sh
export PYTHONPATH=`which python3`
echo $PYTHONPATH
#Output: /usr/bin/python3
alias py3="cd $PYTHONPATH"
py3
#output: bash: cd: /usr/bin/python3: Not a directory
```

[Làm việc với Shell Aliases](https://funix.udemy.com/course/learn-linux-in-5-days/learn/lecture/1417764#overview)
