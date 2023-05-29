def lab14():
    # Lab14: https://courses.funix.edu.vn/courses/course-v1:FUNiX+PYB101x_1.1-A_VN+2021_T12/courseware/aa3cf4af7ef94ada992a9a3560c2c148/94abc5f0189c4992abfef2f3a2b0f943/?activate_block_id=block-v1%3AFUNiX%2BPYB101x_1.1-A_VN%2B2021_T12%2Btype%40sequential%2Bblock%4094abc5f0189c4992abfef2f3a2b0f943
    # Gọi lib cần thiết
    from urllib.request import urlopen
    import xml.etree.ElementTree as ET

    # Kết nối đường link đề bài đã cho
    webUrl = urlopen("http://py4e-data.dr-chuck.net/comments_1430671.xml")

    # Kiểm tra có kết nối thành công
    if webUrl.getcode() != 200:
        exit()

    # Tạo cây XML từ data lấy từ webUrl
    root = ET.fromstring(webUrl.read())

    # Tìm tất cả comment là con của nhánh comments
    comments = root.findall("./comments/comment")

    # Lập dict chứa các user và comment count của từng user sau đó in ra tổng
    print(sum({comment.find('name').text: int(comment.find(
        'count').text) for comment in comments}.values()))


if __name__ == "__main__":
    lab14()
