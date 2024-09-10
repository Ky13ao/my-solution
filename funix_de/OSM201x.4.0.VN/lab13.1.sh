# https://docs.google.com/document/d/13JioVqPMpUWK_iYP-03Cx7Te3xFgBcGlZirU4TxLOO0/edit
# Tạo 1 crobjob chạy mỗi 30 giây với chức năng in ra số lượng các tiến trình đang chạy trong hệ thống. Học viên có thể xem cách ghi log cho cronjob tại: https://stackoverflow.com/a/4811775
ps -e >> pse.log 2>&1