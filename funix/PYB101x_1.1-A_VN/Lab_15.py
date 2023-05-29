def lab15():
    # Lab15: https://courses.funix.edu.vn/courses/course-v1:FUNiX+PYB101x_1.1-A_VN+2021_T12/courseware/aa3cf4af7ef94ada992a9a3560c2c148/024eb5559aaf4282931cbb8d2bbd107a/?activate_block_id=block-v1%3AFUNiX%2BPYB101x_1.1-A_VN%2B2021_T12%2Btype%40sequential%2Bblock%40024eb5559aaf4282931cbb8d2bbd107a
    # Gọi lib cần thiết
    from urllib.request import urlopen
    import json

    # Kết nối đường link đề bài đã cho
    webUrl = urlopen("http://py4e-data.dr-chuck.net/comments_1430672.json")

    # Kiểm tra có kết nối thành công
    if webUrl.getcode() != 200:
        exit()

    # Nạp data comments lấy từ json webUrl vào biến comments
    comments = json.loads(webUrl.read())['comments']

    # Tính tổng các thuộc tính count của comment và in ra console
    print(sum([comment['count'] for comment in comments]))


if __name__ == "__main__":
    lab15()
