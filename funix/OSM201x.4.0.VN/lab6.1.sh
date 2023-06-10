# Lab6.1 https://docs.google.com/document/d/1EebF32RoNXuG-XbxAw_XF2ZiHwH_y_L4JzGyoNwdGiE/edit

# Bài tập
# Di chuyển thư mục làm việc đến folder /etc
cd /etc
# Tìm file có tên “paswd”
find . -name "paswd"
# Tìm các file, thư mục có cụm “wd”
find . -name "*wd*"
# Tìm file có phần mở rộng là “passwd”
find . -name "*.passwd"
# Tìm file có phân quyền 777
find . -perm 777
# Tìm file sửa đổi trong 30 ngày qua
find . -mtime -30
# Tìm các file đã truy cập trong 15 phút trước
find . -atime -15
# Tìm file có kích thước nhỏ hơn 50MB
find . -size -50M
