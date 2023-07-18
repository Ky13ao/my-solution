# Bài tập:
# Xem tất cả tiến trình đang chạy.
ps aux
# Lọc các tiến trình đang chạy theo người dùng
ps -e -u root
# Lọc các tiến trình theo tên bất kỳ.
ps -C bash
# Lọc các tiến trình với tên bất kỳ (nhưng thử tên không tồn tại).
ps -C any
# Sắp xếp các tiến trình theo cách sử dụng
ps -e --sort=comm
# Chỉ hiển thị các cột pid và đổi tên tiêu đề thành Process,
ps -e -o pid=Process
