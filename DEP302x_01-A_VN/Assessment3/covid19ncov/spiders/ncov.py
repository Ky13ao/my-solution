from scrapy import Spider, Request
import re


class NcovSpider(Spider):
    name = "ncov"
    allowed_domains = ["web.archive.org"]
    start_urls = [
        "https://web.archive.org/web/20210907023426/https://ncov.moh.gov.vn/vi/web/guest/dong-thoi-gian"
    ]

    def parse(self, response):
        # lấy các cập nhật ncov bằng cách tìm xpath các thẻ div có class = 'timeline'
        timelines = response.xpath("//div[@class='timeline']")
        for timeline in timelines:
            # thẻ div 1 trực tiếp của timeline là 1 dấu chấm nên chúng ta chỉ lấy các con của thẻ div 2
            # lấy nội dung giờ và ngày ở h3 trong thẻ div thứ 1 của thẻ nói trên
            timeline_timedate = timeline.xpath("./div[2]/div[1]/h3/text()").get()
            # lấy các nội dung cập nhật từ các thẻ p trong thẻ div thứ 2
            timeline_content = [
                _p.xpath(".//text()").get()
                for _p in timeline.xpath("./div[2]/div[2]/p")
            ]
            content_extraction = extraction(timeline_content)
            if content_extraction is None:
                continue
            yield {"time": timeline_timedate, **content_extraction}

        # vì đây là đường link tĩnh nên chúng ta lấy nội dung thuộc tính href của a nút "Trang tiếp theo", nếu không thì kết thúc parse
        next_page_url = response.xpath(
            "//ul[@class='lfr-pagination-buttons pager'][1]/li[2]/a/@href"
        ).get()
        if next_page_url is not None:
            yield Request(url=next_page_url, callback=self.parse)


def extraction(lstring):
    """
    Function trả về các dữ liệu được trích xuất từ nội dung của ncov
    """
    # Kiểm các thành phần nội dung là những chuỗi tìm được từ xpath get và độ dài chuỗi > 0
    new_lstring = [s.strip() for s in lstring if s is not None and len(s.strip()) > 0]
    if len(new_lstring) == 0:
        return None
    new_case = extract_number_from_subject(new_lstring[0])
    if new_case is None:
        return None
    result = {"new_case": new_case}
    city_case = extract_city_from_content("\n".join(new_lstring[1:]))
    # cập nhật danh sách thành phố nếu tìm được danh sách
    if len(city_case) > 0:
        result["city_case"] = city_case
    return result


def extract_number_from_subject(string):
    """
    Function trả về con số trong tiêu đề trước chữ CA MẮC MỚI
    (\d{1,3}.)* để xác định các chữ số hàng nghìn hàng triệu được ngăn cách bởi dấu chấm nếu có
    \d{1,3} để xác định các chữ số hàng đơn vị theo sau
    (?= CA M\w+) để xác định sau hàng đơn vị có đơn vị "CA MẮC"
    """
    pattern = r"(?:\d{1,3}.)*\d{1,3}(?= CA M\w+)"
    # Tìm 1 kết quả duy nhất cho pattern
    numbers_of_case_result = re.search(pattern, string)
    if numbers_of_case_result is not None:
        return int(re.search(pattern, string).group().replace(".", ""))


def extract_city_from_content(string):
    """
    Function trả về danh sách thành phố kèm với số ca mắc tìm được
      trong nội dung bài viết theo định dạng <tên thành phố> (<số ca mắc>)
    (?P<city_name>(?:[A-ZĐ]\S+ )+) pattern để tìm tên thành phố (các từ viết liền có chữ cái đầu tiên viết hoa)
    (?:\()(?P<city_case>(?:\d{1,3}.)*\d{1,3}(?=\))) pattern để tìm số ca mắc bắt đầu với dấu '(' và đứng trước = dấu ')'
        cách xác định số giống cách xác định số ở function extract_number_from_subject
    """
    city_name_pattern = r"(?P<city_name>(?:[A-ZĐ]\S+ )+)"
    city_case_pattern = r"(?:\()(?P<city_case>(?:\d{1,3}.)*\d{1,3}(?=\)))"
    # tìm tất cả các kết quả match với 2 pattern, được trả về là những tuple (<tên thành phố>, <số ca mắc>)
    # do 1 số group chỉ mục đích match mà không lấy với pattern (?:...) nên ta chỉ thu được tuple 2 phần tử như trên
    all_city_result = re.findall(city_name_pattern + city_case_pattern, string)
    return [
        {"city": city[0].rstrip(), "case": int(city[1].replace(".", ""))}
        for city in all_city_result
    ]
