# Lab3.1 https://docs.google.com/document/d/16i_3sxyB9_uhKvX6FxTO6dB7k18ndE6J0Hpuqoto7O0/edit

# Di chuyển về thư mục Desktop
# find: ‘desktop’: No such file or directory so I navigate to ubuntu
cd /home/ubuntu
# Tạo mới 2 folder tên là lab31a, và lab31b
mkdir lab31a && mkdir lab31b
# Di chuyển vào thư mục lab31a, tạo mới 1 file bằng vim, tên “text.txt” rồi nhập nội dung bất kỳ, nhiều hơn 5 dòng
cd lab31a && touch text.txt
vi text.txt 
#input text -> press [Esc] -> save :w, save and exit :x, ignore saving :qa!
# Copy file vừa tạo vào folder lab31b
cp text.txt ../lab31b
# Copy folder lab31b thành lab31c.
cd .. && cp ./lab31b ./lab31c -r
# Xem 4 dòng đầu của file vừa tạo.
head -n 4 ./lab31a/text.txt
# Xem 5 dòng cuối của file vừa tạo.
tail -n 5 ./lab31a/text.txt
# Xóa folder lab31c
rm -r ./lab31c
# Nén 2 folder lab31a và lab31b bằng lệnh tar
tar -cf lab31.tar lab31a lab31b
tar -tvf lab31.tar