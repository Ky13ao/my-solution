def lab13():
    # Lab13: https://courses.funix.edu.vn/courses/course-v1:FUNiX+PYB101x_1.1-A_VN+2021_T12/courseware/aa3cf4af7ef94ada992a9a3560c2c148/4cd54c57d1104eefae6741eea401c04a/?activate_block_id=block-v1%3AFUNiX%2BPYB101x_1.1-A_VN%2B2021_T12%2Btype%40sequential%2Bblock%404cd54c57d1104eefae6741eea401c04a
    # Gọi lib cần thiết
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    # Kết nối đường link đề bài đã cho
    webUrl = urlopen("http://py4e-data.dr-chuck.net/comments_1430669.html")

    # Kiểm tra có kết nối thành công
    if webUrl.getcode() != 200:
        exit()
    # Đưa data lấy từ webUrl vào BS4
    data = webUrl.read()
    soup = BeautifulSoup(data, "html.parser")

    # Tìm tất cả comment bên trong bản với tên tag là 'span'
    comments = soup.table.find_all("span", class_="comments")

    # Tính tổng giá trị trong các span và in ra
    print(sum([int(_.string) for _ in comments]))


if __name__ == "__main__":
    lab13()
