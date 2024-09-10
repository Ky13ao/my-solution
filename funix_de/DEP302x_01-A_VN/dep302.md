# DEP302x_01-A_VN

Data Engineering

## Lab list

- [Lab 1](#lab1---structure-designing)
- [Lab 2](#lab2---etl-initiation-with-ssis)
- [Lab 3](#lab3---transformation-trong-etl)
- [Lab 4](#lab4---fact-table-design)
- [Lab 5](#lab5---initiating-scd-slowly-changing-dimension-with-ssis)
- [Lab 6](#lab6---initiating-etl-for-dimension-table-and-fact-table)
- [Assessment 1](#assignment1--dw-contruction)
- [Lab 7](#lab-7)
- [Lab 8](#lab8---aggregation-operators-exercise)
- [Assessment 2](#assignment-2--build-mongodb-database)
- [Lab 9](#lab9---working-with-data-in-python)
- [Lab 10](#lab10---regex)
- [Lab 11](#lab11---collect-data-from-static-web)
- [Lab 12](#lab12---splash-with-scrapy)
- [Assessment 3](#assignment3---building-covid19-data-collection-system)

## Data Engineering introduction

### What is DE

#### Data ecosystem concepts

- Hệ sinh thái dữ liệu bao gồm một mạng lưới các thành phần được kết nối với nhau và liên tục phát triển bao gồm:

  - **Dữ liệu**: có sẵn ở nhiều định dạng, cấu trúc và nguồn khác nhau
  - **Môi trường Dữ liệu Doanh nghiệp**: trong đó dữ liệu thô được tổ chức, sắp xếp, làm sạch và tối ưu hóa để người dùng cuối sử dụng
  - **Người dùng cuối**: các bên liên quan doanh nghiệp, nhà phân tính và lập trình viên, những người sử dụng dữ liệu cho các mục đích khác nhau

#### Roles in DE industry

- Có rất nhiều vai trò trong hệ sinh thái dữ liệu với từng nhiệm vụ khác nhau
  - **Data Engineer**
    - _Công việc_
      - xây dựng, bảo trì các kiến trúc dữ liệu
      - chuyển hóa dữ liệu để phù hợp cho việc phân tích nghiệp vụ
    - _Các kỹ năng cần có_
      - Kiến thức tốt về lập trình
      - Có kiến thức vững chắc về kiến thức công nghệ
      - biết rõ về các CSDL quan hệ, phi quan hệ
  - **Data Analyst**
    - _Công việc_
      - Dựa vào các dữ liệu đã được xử lý để thu thập thông tin chi tiết.
      - Xác định các mối tương quan, tìm các pattern và áp dụng các phương pháp thống kê để phân tích và khai thác dữ liệu.
      - Trực quan hóa dữ liệu.
    - _Các kỹ năng_
      - kỹ năng lập trình.
      - có kiến thức tốt về việc sử dụng bảng tính, viết truy vấn, sử dụng công cụ xác xuất để tạo dashboard và các biểu đồ.
      - có khả năng truyền đạt tốt.
  - **Data Scientist**
    - _Công việc_
      - Xây dựng các mô hình chuẩn đoán dựa vào các dữ liệu có sẵn bằng Machine Learning hoặc Deep Learning
    - _Các kỹ năng_
      - Kiến thức về Toán và Xác Xuất
      - Kiến thức về lập trình, sử dụng database và xây dựng các mô hình dữ liệu
      - Các kiến thức nghiệp vụ
  - **Business Analyst và BI Analyst**
    - _Công việc_
      - Làm việc với DA và DS để có cái nhìn tổng quan về mặt nghiệp vụ.
        Từ đó xác định được các công việc cần phải triển khai tiếp theo để phát triển doanh nghiệp
    - _Kỹ năng cần thiết_ là các kiến thức về nghiệp vụ

#### DE Definitions

##### Nhiệm vụ của các _DE_ [refer](#roles-in-de-industry)

##### Công việc chính:

- **Thu thập dữ liệu**
  - Lấy dữ liệu từ nhiều người khác nhau
  - Đồng thời thiết kế các kiến trúc để lưu trữ dữ liệu
- **Xử lý dữ liệu**
  - Làm sạch, chuẩn hóa và chuẩn bị dữ liệu để có thể sử dụng được
    Bao gồm các bước như Trích xuất - Chuyển hóa - Tải dữ liệu (ETL)
- **Lưu trữ dữ liệu**
  - Bạn cần lưu trữ lại các dữ liệu đã được xử lý
    Hệ thống lưu trữ cần đảm bảo về tính mở rộng cũng như bảo mật
- **Xử lý dữ liệu để người dùng có thể sử dụng**
  - Bạn cần thiết kế các API
  - Các dịch vụ hoặc các Dashboard để người dùng
    có thể dễ dàng truy cập vào các dữ liệu cần thiết

##### Kỹ năng cần thiết

- Data Engineer cần có sự kết hợp các Kỹ năng chuyên môn, Kỹ năng nghiệp vụ, và các kỹ năng mềm
  - **Kỹ năng chuyên môn**
    - làm việc các hệ điều hành và các cơ sở hạ tầng khác nhau như máy ảo, mạng và dịch vụ ứng dụng
    - làm việc với Database và Data Warehouse, Data Pipeline
    - công cụ ETL, BigData và Query Languages, thao tác và xử lý dữ liệu
  - **Kỹ năng nghiệp vụ**
    - khả năng chuyển đổi các yêu cầu nghiệp vụ thành các đặc điểm kỹ thuật
    - hiểu biết về vòng đời phát triển phần mềm và các lĩnh vực
      chất lượng dữ liệu, quyền riêng tư, bảo mật và quản trị
  - **Kỹ năng mềm**
    - kỹ năng giao tiếp giữa các cá nhân
    - khả năng làm việc hợp tác, làm việc nhóm, giao tiếp hiệu quả

#### DE Ecosystem

- Hệ sinh thái của kỹ thuật dữ liệu bao gồm

  - Cơ sở hạ tầng, công cụ, khuôn khổ
  - Quy trình để trích xuất dữ liệu
    lưu trữ và quản lý quy trình dữ liệu và Data Warehouse
  - Quản lý quy trình công việc
  - Phát triển ứng dụng và quản lý các công cụ BI báo cáo

- Các dữ liệu có thể được chia thành 3 loại như sau:

  - **Dữ liệu có cấu trúc (SQL)**: Dữ liệu có định dạng có thể lưu xuống cơ sở dữ liệu
  - **Dữ liệu bán cấu trúc**: Dữ liệu có 1 phần là cấu trúc, 1 phần là tự do
  - **Dữ liệu phi cấu trúc**: Dữ liệu không thể đưa về dạng bảng để lưu trong cơ sở dữ liệu.

- Dữ liệu có nhiều định tệp khác nhau

  - chẳng hạn như:
    - Tệp văn bản được phân tách
    - Bảng tính
    - XML, PDF, JSON
  - mỗi định dạng có ưu nhược điểm riêng
  - dữ liệu cũng được trích xuất từ nhiều nguồn dữ liệu, từ cơ sở dữ liệu quan hệ và phi quan hệ
    đến API, dịch vụ web, luồng dữ liệu, nền tảng xã hội và thiết bị cảm biến

- trong việc phát triển các kho dữ liệu, thường có 2 loại chính:

  - OLTP - Online transactional processing
    - **OLTP** được thiết kế để lưu trữ một khối lượng dữ liệu **hoạt động hàng ngày** như
      - giao dịch ngân hàng trực tuyến
      - giao dịch ATM
      - đặt vé máy bay
    - mục đích của OLTP chính là bảo đảm tính chính xác và tính toàn vẹn của các giao dịch, hoạt động
  - OLAP - Online analytical processing
    - **OLAP** được tối ưu hoá để tiến hành **phân tích dữ liệu** phức tạp
    - **OLAP** cho phép chúng ta tìm ra xu hướng, điểm mấu chốt thường phục vụ cho các mục đích phân tích

- các chuyên gia dữ liệu cần các ngôn ngữ có thể giúp họ trích xuất, chuẩn bị và phân tích dữ liệu. Ví dụ:
  - **Ngôn ngữ truy vấn** được thiết kế để truy cập và thao tác dữ liệu trong một cơ sở dữ liệu, ví dụ: SQL, ...
  - **Ngôn ngữ lập trình** được thiết kế để phát triển các ứng dụng và kiểm soát hành vi ứng dụng như Python, Java, ...
  - **Unix/ Linux shell** được thiết kế cho các tác vụ lặp đi lặp lại gây tốn nhiều thời gian.

### DE Ecosystem Definitions

#### Data Repositories overview

- **Data Repositories**

  - là 1 thuật ngữ chung đề cập đến dữ liệu và đã được thu thập, tổ chức và trích xuất
    để nó có thể được sử dụng cho báo cáo, phân tích và cũng cố cho mục đích lưu trữ
  - Có một số Data Repositories như sau
    - **Database**: Có thể là cơ sở dữ liệu quan hệ hoặc phi quan hệ, có 2 loại chính:
      - RDBMS - Relational Database Management System
        - Trong RDBMS, dữ liệu được biểu diễn bởi các hàng
        - Nó chứa các bảng và mỗi bảng có Primary Key riêng, bởi vì các bảng này được tổ chức chặt chẽ
          nên việc truy cập dữ liệu trở nên dễ dàng hơn trong RDBMS thông qua ngôn ngữ SQL
      - NoSQL - một dạng cơ sở dữ liệu sử dụng cho các dữ liệu phi cấu trúc
        - dữ liệu có thể được biểu diễn ở dạng Document, Key-Value, Graph hoặc là Column
        - NoSQL mang đến một số ưu điểm về tốc độ truy vấn cũng như tốc độ thực hiện các thao tác CRUD dữ liệu
          đồng thời cũng có thể được mở rộng và chạy trên nhiều cụm máy khác nhau
    - **Data Warehouse**: Tổng hợp và chuyển đôi các dữ liệu từ nhiều nguồn khác nhau
    - **Data Lake**: Tương tự như data warehouse, nhưng dữ liệu sẽ không được xử lý và đưa thẳng vào luôn
    - **Data Mart**: Là 1 dạng nhỏ của Data Warehouse, các dữ liệu chỉ tập trung vào 1 lĩnh vực duy nhất.
    - **Big Data Stores**: Cung cấp cơ sở hạ tầng lưu trữ và tính toán phân tán để mở rộng quy mô và xử lý các tập dữ liệu lớn

- **ETL (Extract-Transform-Load)**
  - là một quy trình tự động chuyển đổi dữ liệu thô thành dữ liệu có thể phân tích bằng cách:
    - **Extract**
      Trích xuất dữ liệu từ các nguồn dữ liệu
    - **Transform**
      Chuyển đổi dữ liệu thô bằng cách làm sạch, chuẩn hóa và xác thực dữ liệu đó
    - **Load**
      Tải dữ liệu đó vào hệ thống đích
  - ELT - một khái niệm khác với ETL
    - dữ liệu sau khi được trích xuất sẽ lưu xuống Data Lake/ Data Warehouse
    - sau đó các phép Transform mới được thực hiện ở nơi lưu trữ dữ liệu
    - quy trình này mang đến một số ưu điểm như sau
      - giảm thời gian giữa bước Trích xuất (Extract) - Phân phối (Delivery) dữ liệu
      - có thể sử dụng dữ liệu thô ngay khi chúng sẵn sàng
      - mang đến sự linh hoạt trong việc phân tích/ xử lý dữ liệu do dữ liệu chưa được biến đổi gì hết
      - ta chỉ cần thực hiện transform các dữ liệu cần thiết cho 1 nhu cầu phân tích cụ thể nào đó

#### Data Integration platform

- Nền tảng tích hợp dữ liệu
  - kết hợp các nguồn dữ liệu khác nhau, về mặt vật lý hoặc logic
    để cung cấp một cái nhìn thống nhất về dữ liệu cho các mục đích phân tích
  - bao gồm các công việc như sau:
    - Truy cập, truy vấn và trích xuất dữ liệu
    - Chuyển đổi và hợp nhất dữ liệu vừa được trích xuất
    - Quản lý về chất lượng của dữ liệu
    - Cung cấp dữ liệu thông qua cách tích hợp cho mục đích phân tích

### Quy trình DE

#### Kiến trúc của một nền tảng dữ liệu

- Kiến trúc của nền tảng dữ liệu

  - Có thể được xem như một tập hợp các tầng hoặc các thành phần chức năng
  - Mỗi tầng thực hiện một tập hợp các nhiệm vụ cụ thể
    - **Tầng thu thập dữ liệu**: bao gồm Data Warehouse
      chịu trách nhiệm đưa dữ liệu từ nguồn dữ liệu vào nền tảng dữ liệu.
    - **Tầng tích hợp và lưu trữ dữ liệu**: bao gồm ETL tools
      chịu trách nhiệm lưu trữ dữ liệu và hợp nhất dữ liệu đã trích xuất.
    - **Tầng xử lý dữ liệu**: bao gồm MongoDB
      chịu trách nhiệm xác thực, chuyển đổi và áp dụng các quy tắc nghiệp vụ cho dữ liệu
    - **Tầng phân tích và giao diện người dùng**: bao gồm MongoDB
      chịu trách nhiệm cung cấp dữ liệu đã xử lý cho người tiêu dùng dữ liệu
    - **Tầng Data Pipeline (đường ống dữ liệu)**:
      chịu trách nhiệm triển khai và duy trì quy trình
  - (Video)[https://www.coursera.org/learn/introduction-to-data-engineering/lecture/cf092/architecting-the-data-platform]

- **Data Store** hay **Data Repositories**
  - là một thuật ngữ chung đề cập đến dữ liệu đã thu thập, sắp xếp và tách biệt
    để nó có thể sử dụng cho báo cáo, phân tích và cũng cho mục đích lưu trữ
  - việc lựa chọn hoặc thiết kế 1 Data Store ảnh hưởng bởi
    - loại dữ liệu và khối lượng dữ liệu cần được lưu trữ
    - mục đích sử dụng dữ liệu
  - các nhu cầu về quyền riêng tư, bảo mật và quản trị của tổ chức của bạn
    cũng ảnh hưởng đến sự lựa chọn nào
  - Video:
    - [Các yếu tố để lựa chọn và thiết kế Datastore](https://www.coursera.org/learn/introduction-to-data-engineering/lecture/b4RA9/factors-for-selecting-and-designing-data-stores)
    - [Bảo mật](https://www.coursera.org/learn/introduction-to-data-engineering/lecture/weR2q/security)

#### Thu thập và làm gọn dữ liệu

- Các cách riêng biệt để thu thập dữ liệu từ các Data Source khác nhau

  - SQL Query
    - truy vấn và lấy dữ liệu từ Database
    - đồng thời SQL cũng hỗ trợ các thao tác như `Group`, `Count`,...
    - với các Database thuộc dạng NoSQL thì cũng sẽ có các công cụ truy vấn như GraphQL,...
  - API
    - thường được sử dụng để thu thập dữ liệu từ các data source
    - khi được thực thi từ các ứng dụng cần dữ liệu, API sẽ truy cập vào Database
      truy vấn và trả về dữ liệu cần thiết
  - Web Scraping
    - là phương pháp thu thập, trích xuất dữ liệu dạng text, ảnh, video,...
      từ các trang web
  - Data Stream
    - là phương pháp để tổng hợp các dữ liệu liên tục
    - phù hợp để thu thập các dữ liệu từ IoT, cảm biến, hoặc các ứng dụng thời gian thực
  - Data Exchanges:
    - cho phép trao đổi dữ liệu giữa bên cung cấp và bên cần sử dụng dữ liệu
  - video [cách để thu thập và nhập dữ liệu](https://www.coursera.org/learn/introduction-to-data-engineering/lecture/745p6/how-to-gather-and-import-data)

- Làm gọn dữ liệu

  - liên quan đến các hoạt động biến đổi và làm sạch được thực hiện trên dữ liệu
  - chuyển đổi dữ liệu thô bao gồm các nhiệm vụ bạn thực hiện như sau
    - kết hợp các dữ liệu bằng cách `JOIN` và `UNIONS`
    - chuẩn hóa dữ liệu, tức là làm sạch database của dữ liệu thừa
    - kết hợp dữ liệu từ nhiều bảng thành một bảng duy nhất để có thể truy vấn nhanh hơn
  - video [Làm gọn dữ liệu](https://www.coursera.org/learn/introduction-to-data-engineering/lecture/WLz3F/data-wrangling)
  - video [các công cụ cho việc làm gọn dữ liệu](https://www.coursera.org/learn/introduction-to-data-engineering/lecture/ngaMF/tools-for-data-wrangling)
  - sau khi đã nhập dữ liệu thành công thì dữ liệu đó đã có thể được phân tích
  - chúng ta cũng có 1 số thao tác phân tích dữ liệu cơ bản như sau:
    - **Counting** đếm số lượng Row, Record trong tập dữ liệu
    - **Aggregation** Tổng hợp dữ liệu từ nhiều khía cạnh khác nhau để có 1 cái nhìn tổng quát hơn
    - **Extreme Value Identification** xác định các cực trị trong dữ liệu, ví dụ như MIN, MAX,...
    - **Slicing Data** tìm các dữ liệu dựa trên một tập các điều kiện
    - **Sorting Data** sắp xếp lại dữ liệu dựa trên các điều kiện
    - **Filtering Patterns** lọc các dữ liệu cần thiết
  - video [truy vấn và phân tích dữ liệu](https://www.coursera.org/learn/introduction-to-data-engineering/lecture/WpGrK/querying-and-analyzing-data)

- vòng đời kỹ thuật dữ liệu
  - cần phải theo dõi liên tục hiệu suất và tính khả dụng về:
    - Data Pipelines
    - hiệu suất của data pipelines có thể bị ảnh hưởng nếu
      - khối lượng công việc tăng lên đáng kể
      - có lỗi ứng dụng hoặc các Task đã lên lịch không hoạt động như mong đợi
    - các nền tảng
    - Databases
    - ứng dụng, công cụ, truy vấn và lập lịch
      - một số cung cụ trong Data Pipelines gặp sự cố tương thích
    - cơ sở dữ liệu dễ bị ngừng hoạt động, sử dụng quá mức dung lượng
    - ứng dụng chạy chậm
    - các truy vấn bị xung đột khi thực thi đồng thời
  - chúng ta cần một hệ thống giám sât hiệu suất
    hệ thống giám sát và cảnh báo sẽ
    - thu thập dữ liệu định lượng
    - trong thời gian thực
    - để cung cấp khả năng hiển thị về hiệu suất
      - Data Pipelines, nền tảng, Databases
      - ứng dụng, công cụ, truy vấn, lập lịch,...
    - và cũng cần có lịch trình bảo trì
      - dựa trên thời gian và điều kiện tạo ra dữ liệu
      - giúp xác định các hệ thống và quy trình chịu trách nhiệm về lỗi và tính khả dụng thấp
  - video [hiệu suất](https://www.coursera.org/learn/introduction-to-data-engineering/lecture/5PkCj/performance-tuning-and-troubleshooting)

### Cơ hội nghề nghiệp trong DE

- DE được báo cáo là một trong mười ngành hàng đầu có tốc độ phát triển vượt bậc ở Hoa Kỳ hiện nay
- Nó cũng được báo cáo là 1 trong những ngành công nghệ phát triển nhanh nhất với mức tăng trưởng hàng năm khoảng 50%
- Hiện tại, nhu cầu vễ các Data Engineer có tay nghề cao hơn nhiều so với nguồn cung, có nghĩa là các công ty sẵn sàng trả một khoản phí cao để thuê các Kỹ sư dữ liệu có tay nghề cao
- Data Engineer có thể đảm nhiều rất nhiều vai trò quan trọng, các vai trò này sẽ phụ thuộc vào công ty mà bạn đang làm việc
- Tuy nhiên thông thường sẽ được chia thành các mảng như sau:
  - Data Architecture
  - Database Design and Architecture
  - Data Platforms
  - Data Pipelines and ETL
  - Data Warehouses
  - Big Data
- Từ đó cũng sẽ có những vai trò trong DE như sau:
  - Data Architect
  - Database Architect
  - ETL Engineer
  - Data Warehouse Engineer
  - Big Data Engineer
- Video [Cơ hội nghề nghiệp trong ngành DE](https://www.coursera.org/learn/introduction-to-data-engineering/lecture/thWrv/career-opportunities-in-data-engineering)
- Video [Con đường học tập về ngành DE](https://www.coursera.org/learn/introduction-to-data-engineering/lecture/Cs66I/data-engineering-learning-path)
- Video [Góc nhìn: Nhà tuyển dụng tìm kiếm gì ở 1 Data Engineer](https://www.coursera.org/learn/introduction-to-data-engineering/lecture/S0xc4/viewpoints-what-do-employers-look-for-in-a-data-engineer)
- Video [Góc nhìn: Nhiều con đường dẫn đến DE](https://www.coursera.org/learn/introduction-to-data-engineering/lecture/5J5rb/viewpoints-the-many-paths-to-data-engineering)
- Video [Góc nhìn: Lời khuyên cho các kỹ sư dữ liệu](https://www.coursera.org/learn/introduction-to-data-engineering/lecture/W23Fb/viewpoints-advice-to-aspiring-data-engineers)

## Data Warehousing - Storing data

### Khái niệm về DW

#### Tính chất và lợi ích của DW

- là 1 kỹ thuật thu thập và quản lý dữ liệu từ nhiều nguồn khác nhau để cung cấp những thông tin kinh doanh có ý nghĩa
- các tính chất của Data Warehouse
  - **Được tích hợp (Integrated)**
    - Dữ liệu trong DW sẽ được lấy từ nhiều nguồn dữ liệu **(Data Source)** khách nhau để có được đầy đủ thông tin
  - **Hướng chủ đề (Subject oriented)**
    - Tổ chức dữ liệu theo chủ đề để thuận tiện cho việc phân tích
    - Ví dụ:
      - với chủ đề nhân sự thì có thể bao gồm
        - các độ đo về doanh thu của từng người, số ngày nghỉ trong tháng, số dự án tham gia trong tháng,...
        - theo các chiều phân tích: thời gian, chi nhánh, sản phẩm,...
    - chỉ lưu trữ các dữ liệu cần thiết cho công việc phân tích
      không cần những dữ liệu thừa khác
  - **Có gán nhãn thời gian (Time variant)**:
    - các dữ liệu sẽ được gán 1 nhãn thời gian tương ứng
      có thể lưu lại được các dữ liệu lịch sử **(historical data)**.
    - dữ liệu lịch sử có tầm quan trọng đặc biệt trong phân tích dữ liệu
    - cùng một độ đo sẽ có nhiều giá trị khác nhau trong lịch sử
    - có thể dùng để so sánh với nhau để biết được sự thay đổi là tốt hay xấu
  - **Bất biến (Non volatile)**
    - khác với Database thì Data Warehouse chỉ có hai thao tác chính là đọc và ghi dữ liệu
    - dữ liệu sẽ ko thể bị thay đổi, cập nhật do như vậy sẽ không phản ánh đúng với thực tế
  - ![data warehouse](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L1_1.JPG.png?alt=media&token=5a38d1cc-1238-4c5e-89bf-f37529109401)
  - video [khái niệm DW](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728264#overview)
- các lợi ích khi sử dụng Data Warehouse
  - Hỗ trợ đưa ra quyết định theo hướng dữ liệu
  - **One Stop Shopping**
    - tất cả dữ liệu (từ nhiều nguồn khác nhau) được tập trung về 1 chỗ.
    - giúp cho ta chỉ cần tập trung vào việc phân tích dữ liệu
      mà không cần phải lo việc thu thập dữ liệu nữa
  - video [tại sao lại cần DW](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728274#overview)

#### So sánh DW và **Data Lake**

- Cơ sở
  - DW thường được xây dựng trên một RDB hoặc hệ CSDL đa chiều **(Multidimensional Database)**
  - Data Lake thường được xây dựng trên 1 môi trường Big Data
- Công dụng
  - DW biến đổi và phân loại dữ liệu từ các nguồn khác nhau của doanh nghiệp.
    Dữ liệu này sẽ sẵn sàng để phục vụ cho các mục đích khác đặc biệt là báo cáo và phân tích
  - Data Lake lưu trữ dữ liệu chưa qua phân tích và giữ trong trạng thái thô.
    Những dữ liệu này cần được xử lý thêm khi có nhu cầu sử dụng
- Đặc tính
  - DW gồm các dữ liệu có cấu trúc cụ thể
  - Data Lake có thể chứa tất cả các loại dữ liệu.
- [So sánh Data Warehouse với Data Lake](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L1_2.JPG.png?alt=media&token=09f0f441-8d9f-4b6f-b0ea-063fe4181b7c)
- Video [So sánh Data Warehouse với Data Lake](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728282#overview)

#### So sánh Data Warehouse với Data Visualization

- Data Visualization hay bị nhầm lẫn với Data Warehouse về khái niệm
- Một số điểm khác biệt của Data Visualization như sau:
  - là 1 cơ sở dữ liệu quan hệ Readonly (các dữ liệu chỉ đọc)
  - trong quá trình phân tích, thống kê thì sẽ truy cập trực tiếp vào Database
    thay vì phải sao chép dữ liệu về 1 chỗ khác
- Chúng ta có thể thấy được Data Visualization nên được sử dụng trong các trường hợp sau:
  - Không yêu cầu các phép biến đổi dữ liệu quá nặng
  - số lượng nguồn dữ liệu ít
  - thời gian thực hiện truy vấn không quá quan trọng
- Video [So sánh](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728284#overview)

#### Quy trình DW đầu cuối

- Dữ liệu từ nhiều nguồn (datasource) qua quá trình ETL sẽ được đưa vào DW
- Đôi khi, các dữ liệu sẽ được tiếp tục chuyển đến cho các môi trường nhỏ hơn như Data Mart
- [quy trình DW](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L1_3.png?alt=media&token=1b3ca1cf-2ee6-4791-87d6-9ecacd75a545)
- video [Quy trình Data Warehouse đầu cuối](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728292#overview)

#### Lựa chọn giữa Cloud và On-Premises Setting

- Ưu điểm khi dùng Cloud
  - Giảm tải bảo trì và cập nhật hệ thống định kỳ
  - Chi phí đầu tư nền tảng có thể thấp hơn
  - Dễ dàng khắc phục các tai nạn hệ thống
  - Có thể kết hợp với Data Lake và Big Data
- Nhược điểm Cloud so với OnPremises
  - Bảo mật thấp hơn
  - Khó để chuyển dữ liệu từ OnPremises Data Warehouse sang Cloud
  - Khó để chuyển dữ liệu giữa data center và cloud
- [các kiến trúc tương ứng](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L12_1.png?alt=media&token=a6090acc-112a-4943-9ea8-0c80df4effa8)
- video [Lựa chọn giữa cloud và onpremises](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729392#overview)
- video [các kiến trúc tương ứng](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729396#overview)

### Các kiến trúc DW

#### Centralized DW

- 1 môi trường chỉ gồm 1 DW duy nhất, tất cả các dữ liệu đều được lưu ở đây
- Kiến trúc này mang đến 1 số ưu điểm sau
  - One Stop Shopping (một điểm dừng): tất cả dữ liệu (từ nhiều nguồn khác nhau)
    được tập trung về một chỗ giúp việc phân tích dễ dàng hơn
  - Dễ dàng vẽ các sơ đồ thiết kế
- Tuy có một số vấn đề về mặt công nghệ, quy trình hoạt động nhưng đến nay đã được giải quyết
- Video: [Centralized Data Warehouse](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728412#overview)

#### So sánh DW vs Data Mart

- dữ liệu không cần dừng lại ở Data Warehouse mà có thể chuyển xuống các môi trường nhỏ hơn như DataMart
- **Data Mart** là một tập hợp nhỏ của DW, thường chỉ tập trung vào 1 lĩnh vực duy nhất, vd DataMart về sale, về khách hàng,...
- vì vậy, data mart sẽ nhỏ và linh hoạt hơn
  khi phân tích về một lĩnh vực nhỏ thì sẽ chỉ cần dùng dữ liệu từ Data Mart tương ứng chứ không cần tìm trong Data Warehouse
- có 2 loại data mart
  - Dependent Data Mart
    - dữ liệu được lấy từ Data Warehouse
    - Các dữ liệu sẽ đồng nhất với nhau
  - Indepent Data Mart
    - dữ liệu được lấy trực tiếp từ các data source
    - các dữ liệu không nhất thiết phải đồng nhất với nhau
- như vậy, DW khá giống với Independent Data Mart, ta có sự khác biệt như sau
  - DW: dữ liệu được lấy từ rất nhiều nguồn
  - Independent Data Mart: dữ liệu được lấy từ 1 số nguồn

#### Lựa chọn cấu trúc phù hợp nhất

- Khác với centralized, kiến trúc Component-Based sẽ gồm nhiều thành phần (DW, Data Mart hoặc Data Lake) liên kết với nhau
- Để lựa chọn cấu trúc phù hợp nhất, đầu tiên ta cần chọn giữa Centralized và Component-Based
- Centralized
  - Ưu điểm
    - Là phương án mặc định
    - One Stop shopping
    - công nghệ hiện đại
  - Nhược điểm
    - Các tổ chức cần liên kết chặt chẽ với nhau
    - khả năng quản lý dữ liệu phải tốt
    - có thể xảy ra ripple effect
      khi một dữ liệu thay đổi có thể ảnh hưởng đến toàn bộ dữ liệu
- Component-Based
  - Ưu điểm
    - Hỗ trợ Mix-and-Match
    - Có thể liên kết với thành phần với nhau
    - Dễ xử lý các vấn đề liên quan đến lưu trữ dữ liệu
  - Nhược điểm
    - Các dữ liệu thường ko nhất quán với nhau
    - Khó để tích hợp chéo

#### Database đa chiều trong DW

- Ngoại trừ RDBMS, ta còn có thể sử dụng CSDL đa chiều MDBMS, MDBMS thường sẽ phù hợp với các Data Warehouse có quy mô nhỏ
- Ưu điểm
  - Thời gian truy xuất dữ liệu nhanh
  - Dung lương lưu trữ ko quá lớn
- Nhược điểm
  - Cấu trúc ít linh hoạt hơn RDBMS
  - Có nhiều sự biến thể hơn RDBMS
- Video: [Database đa chiều trong DW](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728568#overview)

#### ODS trong DW

- Ngoài DW, ta còn có thể sử dụng oDS(Operational Data Store)
- ODS giống như DW nhưng khi dữ liệu được cập nhật sẽ ghi đè lên dữ liệu
  dẫn đến ODS sẽ không có các dữ liệu lịch sử (Historical Data)
- video [ODS trong DW](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728580#overview)

#### Staging Layer trong DW

- **Staging Layer (tầng trung gian)**
  - là khu vực thực h iện việc xử lý thông tin cũng như lưu trữ trước khi đưa vào DW
- **User Access Layer(tầng người cùng truy cập)**
  - là khu vực mà user có thể truy cập được vào dữ liệu
- [Staging layer & User access layer](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L6_1.png?alt=media&token=ea681db1-b950-4f8e-8510-6d3788ceb9e1)
- Staging Layer được chia làm 2 loại
  - Non Persistent(không liên tục)
    - Sau khi đưa dữ liệu vào DW thì sẽ xóa dữ liệu của ở Staging Layer đi
    - Ưu điểm
      - Lưu trữ ít hơn
      - Dữ liệu đc chuyển hẳn sang User Layer
    - Nhược điểm
      - Khi user layer gặp lỗi và cần dừng lại thì sẽ phải lấy lại các dữ liệu từ Data Source
      - Việc đảm bảo chất lượng dữ liệu cũng cần đến Data Store
  - Persistent (liên tục)
    - Sau khi đưa dữ liệu vào DW thì vẫn giữ dữ liệu cũ ở Staging Layer
    - Ưu điểm
      - Khi User layer gặp lỗi và cần dựng lại thì có thể lấy trực tiếp từ Staging Layer
      - Để đảm bảo chất lượng dữ liệu thì cần so sánh giữa User Layer và Staging Layer
    - Nhược điểm
      - Phải truy cập nhiều hơn
      - Có rủi ro bị truy cập trái phép
  - video [staging layer trong DW](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728588#overview)
  - video [các loại staging layer](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728608#overview)

### Lab1 - Structure designing

- Đề bài [shortcut](https://courses.funix.edu.vn/courses/course-v1:FUNiX+DEP302x_01-A_VN+2021_T8/courseware/3a8c750402a24420904c42983322073a/fdd45c0e3ad0432488b2fb9d09d8e66f/?activate_block_id=block-v1%3AFUNiX%2BDEP302x_01-A_VN%2B2021_T8%2Btype%40sequential%2Bblock%40fdd45c0e3ad0432488b2fb9d09d8e66f)

- Bài giải: xem file "lab1.dio"

### Load data to DW

#### ETL & ELT comparison

- ETL viết tắt cho:

  - Trích xuất (Extract):
    Lấy dữ liệu từ các Data Source theo từng lô
    bao gồm tất cả dữ liệu thô (chưa qua xử lý) và chuyển đến Staging Layer.
  - Chuyển đổi (Transform):
    Biến đổi để dữ liệu từ nhiều nguồn đồng nhất với nhau.
    Quá trình này có thể rất phức tạp.
  - Tải (Load):
    Chuyển các dữ liệu đã được biến đổi vào User Access Layer.

- RDBMS (Relational Database Management System)
  là hệ quản trị cơ sở dữ liệu quan hệ. RDBMS sử dụng các bảng để lưu trữ dữ liệu.
  Một bảng là một tập hợp các dữ liệu có liên quan và chứa các hàng và các cột để lưu dữ liệu.

- MDBMS (Multidimensional Database Management System)
  là hệ quản trị cơ sở dữ liệu đa chiều.
  Các dữ liệu sẽ được cấu trúc theo nhiều chiều, mỗi chiều mô tả một đặc trưng nào đó của dữ liệu.
  MDBMS còn có một tên gọi khác là Cube.

- ETL

  - Dữ liệu được lưu trữ và xử lý ở Staging Layer sau đó mới chuyển vào Data Warehouse.
    [figure](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L7_2.png.png?alt=media&token=4a46476a-5e23-410a-9522-c7da56cd479e)
  - Phù hợp với các môi trường dùng RDBMS hoặc MDBMS.

- ELT

  - Dữ liệu thô được đưa vào Data Warehouse. Khi phân tích thì mới bắt đầu biến đổi.
    [figure](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L7_1.png.png?alt=media&token=1c10d640-bde0-4fb7-ad34-05441d47f6cf)
  - Phù hợp với các môi trường dùng Big Data.

- video [So sánh giữa ETL và ELT](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728682#overview)

#### Initial Load ETL và Incremental ETL

- BI (Business Intelligence)

  - là một quy trình có khả năng tích hợp công nghệ
  - giúp các doanh nghiệp kiểm soát khối lượng dữ liệu khổng lồ đến từ
    nhiều nguồn khác nhau và khai thác nguồn dữ liệu đó một cách hiệu quả.
  - Đồng thời hệ thống tạo ra những tri thức (knowledge) mới giúp cho các nhà quản lý
    có thể đưa ra các quyết định hiệu quả hơn trong hoạt động kinh doanh của mình.

- Initial Load ETL (ETL tải ban đầu)

  - là một biến thể của ETL, gồm một số đặc điểm sau:
    - Chỉ xảy ra một lần trước khi Data Warehouse được đưa vào vận hành.
    - Đưa tất cả các dữ liệu cần thiết cho việc phân tích và BI vào Data Warehouse.
    - Có thể thực hiện lại nếu Data Warehouse gặp lỗi và cần khởi động lại.
  - Video: [Initial Load ETL](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728684#overview)

- Incremental ETL (ETL gia tăng)
  - cũng là một biến thể của ETL
  - mục đích là giữ cho các dữ liệu luôn mới nhất
  - bằng cách thêm các dữ liệu mới hoặc cập nhật các dữ liệu cũ.
  - Ngoài ra, Incremental ETL cũng xử lý việc xóa dữ liệu.
    Lúc này thì dữ liệu sẽ không bị xóa hẳn khỏi Data Warehouse
    mà chỉ đánh dấu là không còn active nữa.
  - _Bốn thao tác trong Incremental ETL_:
    - **Append**: Chèn thêm dữ liệu vào Data Warehouse.
    - **In-place Update**: Thay đổi một số dữ liệu có sẵn.
    - **Complete replacement**: Thay đổi toàn bộ dữ liệu có sẵn.
    - **Rolling append**: Thường được sử dụng trong việc quản lý dữ liệu theo thời gian. Khi chèn thêm một dữ liệu mới thì sẽ xóa dữ liệu cũ tương ứng đi.
  - Video: [Incremental ETL](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728686#overview)

#### Tầm quan trọng của việc Transform dữ liệu

- Bước Transform giúp các dữ liệu đồng nhất với nhau và phù hợp về mặt nghiệp vụ.
- Do Data Warehouse lấy dữ liệu từ rất nhiều nguồn khác nhau nên bước Transform này rất quan trọng.

- Các mô hình Transform:
  - Đồng nhất về giá trị.
  - Đồng nhất về loại và kích thước của dữ liệu.
  - Loại bỏ các dữ liệu trùng nhau.
  - Video: [Tầm quan trọng của việc Transform dữ liệu](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728696#overview)
  - Loại bỏ các cột không cần thiết.
  - Loại bỏ các hàng không cần thiết.
  - Sửa các lỗi được phát hiện.
  - Video: [Các mô hình Transform khác với ETL](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728698#overview)

#### Mix-and-Match Incremental ETL

- Thực tế, Data Warehouse sẽ không lấy dữ liệu từ tất cả các Data Source cùng một thời gian
- có Data Source sẽ lấy dữ liệu hàng tháng, hoặc hàng giờ,…
- Và mỗi Data Source cũng sẽ sử dụng một mô hình chuyển đổi khác nhau.
- vì vậy, Mix-and-Match (pha trộn và kết hợp) là phương pháp kết hợp nhiều mô hình chuyển đổi với nhau.
- Video: [Mix-and-Match Incremental ETL](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728702#overview)

### Lab2 - ETL initiation with SSIS

- Đề bài [shortcut](https://courses.funix.edu.vn/courses/course-v1:FUNiX+DEP302x_01-A_VN+2021_T8/courseware/3a8c750402a24420904c42983322073a/98656d6d42a6422a90de08708d73ad62/?activate_block_id=block-v1%3AFUNiX%2BDEP302x_01-A_VN%2B2021_T8%2Btype%40sequential%2Bblock%4098656d6d42a6422a90de08708d73ad62)

- Bài giải: Xem SSISProject1 solution

### DW contruction

#### Xác định mục đích sử dụng

- Để bắt đầu xây dựng 1 DW, chúng ta cần dựa vào mục đích sử dụng, từ đó chọn ra được model sử dụng
- BI category drives data model
  - Basic reporting - Dimensional
  - Online analytical processing (OLAP) - Dimensional
  - Predictive analytics - Data mining/specialized
  - Exploratory analytics - Data mining/specialized
- Video: [Xác định xem Data Warehouse được sử dụng cho mục đích gì](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728858#overview)
- Video: [Các nguyên tắc cơ bản của Dimensionality (kích thước)](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728864#overview)

#### Facts, Fact Tables, Dimensions va Dimension Tables

##### Facts

- Thường là phép đo (measure), số liệu (metrics) hoặc sự kiện (fact) của quy trình kinh doanh (business process).
  _Ví dụ_: điểm số, thù lao, ... => Fact Table là một bảng chứa các Fact.
- Fact có thể được chia ra làm 3 loại:
  - **Additive**:
    là những Fact có thể được tổng hợp thông qua tất cả các Dimension trong Fact Table.
  - **Semi-Additive**:
    là những Fact có thể được tóm tắt cho một số Dimension trong Fact Table chứ không phải là những bảng khác.
  - **Non-Additive**:
    là những Fact không được tóm tắt cho bất kỳ Dimension hiện tại nào trong Fact Table.

##### Dimensions

- Cung cấp các thông tin, ngữ cảnh cho Fact.
  _Ví dụ_: tên môn học, tên công ty, ... => Dimension Table là một bảng chứa các Dimension.

##### Video:

- [Facts, Fact Tables, Dimensions, và Dimension Tables](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728874#overview)
- [Phân loại Fact](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728882#overview)

#### Star Schema và Snowflake Schema

##### Star Schema

- Định nghĩa
  - Gồm 1 Fact Table nằm ở trung tâm và được bao quanh bởi những Dimension Table
  - Dữ liệu không được chuẩn hoá.
- Ví dụ
  - ![star schema image](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L8_1.png?alt=media&token=6414cbca-f966-4b1f-afad-950bfdca692b)
- Ưu điểm
  - Fact Table, Dimension Table được mô tả rõ ràng, dễ hiểu.
  - Khoá của Fact Table được tạo bởi khoá của các Dimension Table.
    Nghĩa là khoá chính của các Dimension Table chính là khoá của Fact Table.
- Nhược điểm
  - Dữ liệu không được chuẩn hóa.

##### Snowflake Schema

- Định nghĩa
  - Là dạng mở rộng của Star Schema bằng cách chuẩn hóa các Dimension Table.
  - Dữ liệu được chuẩn hoá.
- Ví dụ
  - ![snow schema image](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L8_3.png?alt=media&token=f4d147ac-5fbf-45ca-a9ec-416b6c4832e8)
- Ưu điểm
  - Số chiều được phân cấp thể hiện dạng chuẩn của Dimension Table.
  - Các Dimension Table sử dụng ít bộ nhớ hơn.
- Nhược điểm - Cần thực hiện các bước JOIN bảng để lấy dữ liệu.

##### Video

- [Star Schema và Snowflake Schema](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728890#overview)

#### Database Keys trong Data Warehousing

- Khóa chính (Primary Key) trong Datawarehouse được chia thành 2 loại:
  - Surrogate Key:
    - Là khóa chính dimension table thường có giá trị là kiểu số.
    - Thường được hệ thống DW sinh ra (duy nhất) bằng các luồng ETL.
    - Tuy nhiên đây là khóa không có ý nghĩa trong ngữ cảnh nghiệp vụ.
  - Natural Key:
    - Là loại khoá sử dụng chính một hoặc kết hợp nhiều thuộc tính
      có sẵn của đối tượng lưu trữ trong CSDL để làm khoá
      ⇒ có ý nghĩa trong ngữ cảnh nghiệp vụ.
- Video: [Database Keys trong Data Warehousing](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17728892#overview)

### Lab3 - Transformation trong ETL

- đề bài lab3 [shortcut](https://courses.funix.edu.vn/courses/course-v1:FUNiX+DEP302x_01-A_VN+2021_T8/courseware/3a8c750402a24420904c42983322073a/22b0c6a2a9d74be2a2b5479f70683a46/?child=first)

- Bài giải: Xem SSISProject1 solution

### Fact Tables and Dimension Tables designing

- Cách thiết kế Dimension, Fact Tables cho Star Schemas và Snowflake Schemas, với dimension table:
  - Star Schemas: Chỉ có 1 bảng duy nhất chứa toàn bộ thông tin.
  - Snowflake Schemas: Chia ra các bảng con và kết nối với nhau bằng Primary Key and Foreign key.
- video [Thiết kế Dimension Tables cho Star Schemas và Snowflake Schemas](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729122#overview)
- video [So sánh về cấu trúc của Fact Tables trong Star Schemas và Snowflake Schemas](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729276#overview)

- Fact Table được chia thành 4 loại chính:

  - Video [4 Fact Table loại chính](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729218#overview)
  - Transaction
    - Dữ liệu chủ yếu là các Additive Facts được lưu lại từ các giao dịch.
    - có thể được coi là loại được sử dụng nhiều nhất.
    - Được sử dụng để lưu lại thông tin cụ thể của mỗi giao dịch ( mỗi record sẽ là một giao dịch).
    - các Transaction này phải có đầy đủ thông tin về thời gian xảy ra để có thể dễ dàng phân tích hơn.
    - Bảng cũng chứa nhiều khóa ngoại vì có mối quan hệ với Dimension Table.
    - Video: [Nhiệm vụ của Transaction Fact Tables](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729222#overview)
    - Video: [Rules Governing Facts và Transaction Fact Tables](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729234#overview)
  - Periodic Snapshot
    - Bảng này lưu trữ Snapshot quy trình kinh doanh trong một khoảng thời gian cụ thể.
    - Trong bảng dữ liệu này có thể không ở cấp độ quy trình kinh doanh
    - Nó tóm tất hoạt động trong một khoảng thời gianm có thể là tháng, năm hoặc tuần.
    - ví dụ [Tracking student meal card payments](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L9_1.png?alt=media&token=5eb892b3-9fae-4517-bf45-191bda2afaab)
    - video [Vai trò của Periodic Snapshot Fact Tables](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729242#overview)
    - video [Periodic Snapshots và Semi-Additive Facts](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729250#overview)
  - Accumulating Snapshot
    - Đại diện cho toàn bộ vòng đời của quy trình kinh doanh từ đầu đến cuối quy trình.
      ( tức là "Xử lý đơn hàng bán hàng", "Xử lý yêu cầu")
    - Mỗi bản ghi trong loại bảng này đại diện cho một thực thể
      của quy trình kinh doanh tương ứng
      sau đó bản ghi này sẽ được cập nhật mỗi lần theo trạng thái hiện tại của thực thể
    - ví dụ:
      Chúng ta đang xử lý một đơn đặt hàng.
      Mỗi khi trạng thái của đơn hàng đó (Đã đặt, đã chuẩn bị hàng, đang vận chuyển, đã vận chuyển, ...) được cập nhật
      thì dữ liệu tương ứng ở Fact table cũng sẽ được cập nhật.
    - Video: [Vai trò của Accumulating Snapshot Fact Tables](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729254#overview)
    - Video: [Ví dụ về Accumulating Snapshot Fact Table](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729264#overview)
  - Factless
    - Dữ liệu không bao gồm một Fact nào hết.
    - Do có một số sự kiện không có số liệu thước đo
      Nên Fact Table sẽ chỉ gồm các PK và FK
    - Các bảng này được sử dụng để nắm bắt các hành động của quy trình kinh doanh
    - Ví dụ [Fact leave](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L9_2.png?alt=media&token=c3945030-aafe-41af-9eed-a066c736588e)

- Khóa chính và Khóa ngoại cho Fact Table
  - **Primary Key** trong Fact Table sẽ là tổng hợp của tất cả các Foreign Key
    liên kết với các Dimension Table có liên quan (kể cả khi bảng đã có Nature Key).
  - **Foreign Key** trong Fact Table sẽ liên kết với các Dimension Table có liên quan.
  - Video: [Khóa chính và Khóa Ngoại cho Fact Table](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729238#overview)

### Lab4 - Fact Table design

- Đề bài : [shortcut](https://courses.funix.edu.vn/courses/course-v1:FUNiX+DEP302x_01-A_VN+2021_T8/courseware/3a8c750402a24420904c42983322073a/ef648f3b92ff41868339cf62884ce0ff/?child=last)

- Bài giải : xem lab4.dio

### DW version control

1. Slowly Changing Dimensions (SCDs) và lịch sử của Data Warehouse

- DW sẽ lưu lại các dữ liệu trong quá khứ (Time variant)
  Nên chúng ta cần dùng SCD để quản lý lịch sử của dữ liệu trong DW

- Từ đó chia ra làm 3 loại SCD:

  - Loại 1:
    - Kỹ thuật
      - In-place update
      - Đơn giản là thay đổi giá trị cũ thành mới
    - Tính chất
      - Đây là loại đơn giản nhất nhưng sẽ không giữ được các dữ liệu cũ
  - Loại 2:
    - Kỹ thuật
      - Khi có thay đổi thì sẽ chèn thêm 1 hàng nữa chứa các giá trị update mới
        => Giữ cả 2 version cũ và mới
    - Tính chất
      - Phức tạp về mặt kỹ thuật nhưng sẽ giữ lại được các dữ liệu cũ
  - Loại 3:
    - Kỹ thuật
      - Khi thay đổi dữ liệu thì sẽ có 2 cột: 1 cột chứa giá trị cũ, 1 cột chứa giá trị mới
    - Tính chất
      - Ưu điểm: Không tăng kích thước của bảng và có thể giữ lại được các dữ liệu cũ
      - Khuyết điểm: Sẽ không giữ được các dữ liệu cũ nếu bị thay đổi nhiều lần

- Video: [Slowly Changing Dimensions (SCDs) và lịch sử của Data Warehouse](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729308#overview)
- Video: [Thiết kế SCD loại 1](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729310#overview)
- Video: [Thiết kế SCD loại 2](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729312#overview)
- Video: [Thiết kế SCD loại 3](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729318#overview)

2. Duy trì thứ tự dữ liệu chính xác với SCD loại 2

- Nếu như sử dụng SCD loại 2 thì chúng ta sẽ không biết được đâu là giữ liệu mới nhất. Có một số giải pháp như sau:
  - **Current_Flag**: Thêm 1 cột current_flag đánh dấu xem đó có phải là giá trị mới nhất không.
  - **Eff_date** and **Exp_date**: Thêm 2 cột để thể hiện ngày dữ liệu được thêm và ngày dữ liệu bị thay đổi.

### Lab5 - Initiating SCD (Slowly Changing Dimension) with SSIS

- đề bài: [link](https://courses.funix.edu.vn/courses/course-v1:FUNiX+DEP302x_01-A_VN+2021_T8/courseware/3a8c750402a24420904c42983322073a/f9e3691e24a04132be23c67b8fbb1430/?child=last)

- bài giải: xem SSISProject1

### ETL designing

#### Thiết kế ETL từ kiến trúc ETL

- Có 1 số lưu ý trong thiết kế ETL:
  - Giới hạn lượng dữ liệu sẽ xử lý:
    Chúng ta sẽ không xử lý hết tất cả các dữ liệu
    từ nguồn dữ liệu mà nên giới hạn lại những dữ liệu cần thiết
  - Xử lý dữ liệu cho các Dimension table trước Fact table:
    Thông thường, các dữ liệu ở Fact Table sẽ liên quan mật thiết
    đến dữ liệu trong Dimension Table
  - Hãy xử lý song song:
    Thay vì xử lý tuần tự thì hãy xử lý song song để tiết kiệm thời gian
- Video: [Thiết kế ETL từ kiến trúc ETL](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729338#overview)

#### Thiết kế ETL cho Dimension Table

- Quy trình thiết kế ETL cho Dimension Table:

1. Chuẩn bị dữ liệu (data preparation)

- Chúng ta nên xử lý toàn bộ các dữ liệu từ nguồn dữ liệu
  mà hãy giới hạn lại thông tin kỹ thuật **Change Data Capture**
  - Sử dụng nhãn thời gian
    Mỗi dữ liệu sẽ có một nhãn thời gian
    ta sẽ so sánh và xem dữ liệu nào đã có từ lần ETL trước và loại dữ liệu đó
  - So sánh với log từ database
  - Phương án cuối cùng là load toàn bộ dữ liệu
    và so sánh với Data Warehouse để xem dữ liệu nào đã có

2. Chuyển hóa dữ liệu

3. Đưa dữ liệu vào Dimension Table

- Nếu đó là một loại dữ liệu mới hoàn toàn thì chúng ta chỉ cần thêm dữ liệu đó và Dimension Table
- Nếu đó là cập nhật thì chúng ta sử dụng SCD để lưu lại dữ liệu lịch sử

- Video: [Thiết kế ETL cho Dimension Table](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729344#overview)
- Video: [SCD Loại 1 cho Dimension Table](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729350#overview)
- Video: [SCD Loại 2 cho Dimension Table](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729352#overview)

#### Thiết kế ETL cho Fact Table

- Khi đưa 1 dữ liệu mới vào Fact Table, bạn sẽ dựa vào các dữ liệu trong Dimension Table
  để biết được đâu là **Surrogate Key** của dữ liệu mới nhất
  Tương tự, nếu là các dữ liệu lịch sử được cập nhật
  thì chúng ta cũng dựa vào Dimension Table để chọn Surrogate Key phù hợp
- Video: [Thiết kế ETL cho Fact Table](https://funix.udemy.com/course/data-warehouse-fundamentals-for-beginners/learn/lecture/17729364#overview)

### Lab6 - Initiating ETL for Dimension Table and Fact Table

- đề bài : [link](https://courses.funix.edu.vn/courses/course-v1:FUNiX+DEP302x_01-A_VN+2021_T8/courseware/3a8c750402a24420904c42983322073a/4085b37f5309497daf5c083baa540d61/?child=first)

### Assignment1: DW contruction

#### Tên dự án: Xây dựng Data Warehouse

#### Tổng quan dự án

- Ở bài Assignment này, bạn sẽ được xây dựng một Data Warehouse từ một tập dữ liệu có sẵn. Data Warehouse sẽ cần đảm bảo các yêu cầu sau:

1. Thiết kế được ERD cho Data Warehouse dựa trên bộ dữ liệu cho trước.
2. Xác định được tối thiểu 3 business queries (truy vấn nghiệp vụ) để thực hiện phân tích dữ liệu.
3. Xây dựng được quy trình ETL trong SSIS.
4. Mô tả được quy trình ETL để đưa dữ liệu vào Data Warehouse.
5. Đưa được dữ liệu vào Database.
6. Viết các câu lệnh SQL để xây dựng Database.
7. Viết các câu lệnh SQL để lấy dữ liệu cho các business queries đã xác định.

- data resource: (https://drive.google.com/file/d/1YAlWdqPd5T48XzLGVbpuYZ0oirKwoQXm/view)

#### Một số tài liệu khác:

- Tài liệu đọc: [cơ chế Change Data Capture với SSIS](https://www.mssqltips.com/sqlservertip/5815/sql-server-integration-services-ssis-cdc-tasks-for-incremental-data-loading/)
- Video: [Cơ chế Change Data Capture với SSIS](https://www.youtube.com/watch?v=QVF1JGFFt8w)
- [Thiết kế ETL chạy song song](http://www.techbrothersit.com/2014/03/what-is-parallel-execution-in-ssis-how.html#:~:text=DBA%20INTERVIEW%20QUESTIONS-,What%20Is%20Parallel%20Execution%20In%20SSIS%2C%20How%20Many%20Tasks%20A,Tasks%20will%20run%20in%20Parallel.)
- [Sử dụng Sequence Container](https://www.youtube.com/watch?v=1ibHZ7VmhvY)
- [Xây dựng ETL cho Dimension Table](https://mindmajix.com/ssis/dimension-table-loading)
- [Lookup Transformation](https://www.learnmsbitutorials.net/ssis-lookup-transformation-example.php)

## MongoDB

### MongoDB & basic operations

#### Definition

- MongoDB là một hệ cơ sở dữ liệu mã nguồn mở thuộc dạng NoSQL
- Cấu trúc MongoDB khác với RDBMS:
  - MongoDB chứa các **Collection** (có thể coi là một Table trong RDBMS)
  - Các Collection này sẽ gồm nhiều **Document** (mỗi Document sẽ giống như một record trong RDBMS)
  - Các Document sẽ có cấu trúc dạng **BSON** (khá giống JSON) và mỗi document ko bắt buộc phải có một cấu trúc giống nhau như trong RDMBS
  - Điều này giúp cho tốc độ truy vấn, xử lý dữ liệu trong MongoDB cũng nhanh hơn so với RDBMS.
  - ![Ví dụ](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L13_1.png?alt=media&token=d519ff32-af72-485a-9c04-332010ee9589)
- Một số ưu điểm của MongoDB
  - Cấu trúc của một đối tượng rõ ràng
  - Không có các join phức tạp
  - Khả năng mở rộng cực lớn:
    - Việc mở rộng dữ liệu mà không phải lo đến các vấn đề như khóa ngoại, khóa chính, kiểm tra ràng buộc
    - MongoDB cho phép thực hiện replication và sharding nên việc mở rộng cũng thuận lợi hơn.
  - Ít schema hơn
- Video:
  - [Giới thiệu về MongoDB](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739108#overview).
  - [Các đặc điểm chính của MongoDB](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739116#overview)
  - [Hệ sinh thái MongoDB](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739118#overview)
  - [Tìm hiểu về Database, Collection, Document](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739172#overview)

Cài đặt MongoDB

- Bạn có thể lên [trang chủ](https://docs.mongodb.com/manual/installation/) của MongoDB để cài đặt hoặc tham khảo các tài liệu sau:
- [Tham khảo: Cài đặt MongoDB](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/27711524#overview)
- [Tham khảo: Cài đặt MongoDB Shell](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/27711526#overview)

#### Create new Database and Collection

- Basic commands:
  - `show dbs` - Hiển thị các Database đang có
  - `use <database name>` - chuyển sang database tương ứng có tên là 'database name'
  - `db` - hiển thị tên database hiện tại
- MongoDB sẽ tự động tạo Database, Collection khi bạn thêm một dữ liệu vào đó
  vậy nên để tạo mới một Database thì bạn cần sử dụng những câu lệnh sau đây:
  ```mongodb
  use <new database name>
  db.<new collection name>.insertOne({})
  ```
- Video: [Tạo Databse và Collection](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739180#overview)

#### CRUD operations in MongoDB

##### CREATE

- `insertOne(data)`
  - thêm 1 document vào collection
  - https://docs.mongodb.com/manual/reference/method/db.collection.insertOne/
- `insertMany(data)`
  - thêm nhiều document vào collection
  - https://docs.mongodb.com/manual/reference/method/db.collection.insertMany/

##### READ

- `find(query, projection)`
  - trả về document thoả mãn với _query_
  - _projection_ là một tham số không bắt buộc
  - https://docs.mongodb.com/manual/reference/method/db.collection.find/#definition
- `findOne(query, projection)`
  - giống như hàm `find()` nhưng chỉ trả về document đầu tiên thỏa mãn _query_

##### UPDATE

- `updateOne(query, update)`
  - cập nhật dữ liệu của Document đầu tiên thoả mãn với _query_
  - dữ liệu đó sẽ được cập nhật thành _update_
  - nếu bạn muốn thay đổi giá trị của các field trong document hoặc thêm 1 field mới thì bạn sử dụng `$set`
    - vd:
      ```
      db.restaurant.updateOne(
          { "name" : "Central Perk Cafe" },
          { $set: { "violations" : 3 } }
        );
      ```
  - nếu bạn muốn xóa field trong document thì sử dụng `$unset`
    - vd:
      ```
      db.restaurant.updateOne(
        { "name" : "Central Perk Cafe" },
        { $unset: { "address" : '' } }
      );
      ```
  - https://docs.mongodb.com/manual/reference/method/db.collection.updateOne/
- `updateMany(query, update)`
  - tương tự như hàm updateOne, nhưng updateMany sẽ cập nhật toàn bộ các document thõa màn với query
  - https://docs.mongodb.com/manual/reference/method/db.collection.updateMany/
- `replaceOne(query, update)`
  - tương tự hàm updateOne nhưng bạn chỉ có thể thay thế toàn bộ document chứ không cập nhật các field được
  - https://docs.mongodb.com/manual/reference/method/db.collection.replaceOne/

##### DELETE

- `deleteOne(query)`
  - xóa document đầu tiên thỏa mãn với query
  - https://docs.mongodb.com/manual/reference/method/db.collection.deleteOne/
- `deleteMany(query)`
  - xóa tất cả document thỏa mãn với query
  - https://docs.mongodb.com/manual/reference/method/db.collection.deleteMany/

##### video

- [CRUD trong MongoDB](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739200#overview)
- [Tạo - Đọc - Sửa - Xóa Document](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739206#overview)
- [Hàm insertMany()](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739208#overview)
- [update() vs updateMany()](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739218#overview)
- [Understanding Projection](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739228#overview)

#### Embedded Documents & array in MongoDB

- Trong MongoDB các document sẽ có cấu trúc giống như JSON
- Chúng ta có thể sử dụng cơ chế **JSON nested objects**
  để lưu 1 Document bên trong một Document khác hoặc là lưu lại một trường có giá trị là mảng
- Ví dụ:
  [vi du](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L13_2.png?alt=media&token=07fbc34b-a7e0-4769-a834-0598625c7999)
- Với ví dụ trên, để truy cập vào trường _lastname_ của _author_, ta có thể sử dụng cú pháp như sau: `author.lastname`
- video:
  - [Lý thuyết về Embedded Documents & Mảng](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739232?start=0#overview)
  - [Làm việc với Embedded Documents](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739234#overview)
  - [Làm việc với mảng](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739236#overview)
  - [Truy cập vào trường của Embedded Documents](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11739240#overview)

#### Deeply understanding about CRUD operations

##### Inorder inserting data

- Khi sử dụng hàm **insertMany()** ta cần truyền vào danh sách các document muốn chèn
- Theo mặc định thì các document sẽ được chèn vào collection theo thứ tự trong mảng
- Và khi có một document nào bị lỗi (ví dụ như \_id bị trùng) thì toàn bộ quá trình chèn dữ liệu sẽ dừng lại
- Vd: ta đang chèn 3 document [Doc1, Doc2, Doc3].
  Trong quá trình chèn Doc2 xảy ra lỗi
  => lúc này chỉ có Doc1 được chèn vào, còn Doc3 sẽ ko được chèn
  do thao tác đã dừng ở Doc2
  Tuy nhiên bạn có thể thay đổi cơ chế này bằng cách sử dụng chèn không thứ tự
  Bạn chỉ cần thêm một tham số `{ordered: false}`, lúc này thì khi có lỗi xảy ra
  các Document khác có thể được chèn vào
- Video: [Chèn dữ liệu không theo thứ tự](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850590#overview)

##### Operators in querying data

- [Basic comparison query operators](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850712#overview)
  - [`$eq` ](https://docs.mongodb.com/manual/reference/operator/query/eq/#mongodb-query-op.-eq)
  - [`$ne`](https://docs.mongodb.com/manual/reference/operator/query/ne/#mongodb-query-op.-ne)
  - [`$gt`](https://docs.mongodb.com/manual/reference/operator/query/gt/#mongodb-query-op.-gt)
  - [`$gte`](https://docs.mongodb.com/manual/reference/operator/query/gte/#mongodb-query-op.-gte)
  - [`$lt`](https://docs.mongodb.com/manual/reference/operator/query/lt/#mongodb-query-op.-lt)
  - [`$lte`](https://docs.mongodb.com/manual/reference/operator/query/lte/#mongodb-query-op.-lte)
- [IN and NIN comparison operators](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850720#overview)
  - [`$in`](https://docs.mongodb.com/manual/reference/operator/query/in/#mongodb-query-op.-in) - Matches any of the values specified in an array.
  - [`$nin`](https://docs.mongodb.com/manual/reference/operator/query/nin/#mongodb-query-op.-nin) - Matches none of the values specified in an array.
- [Logical query operators](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850722#overview)
  - [`$or`](https://docs.mongodb.com/manual/reference/operator/query/or/#mongodb-query-op.-or)
  - [`$nor`](https://docs.mongodb.com/manual/reference/operator/query/nor/#mongodb-query-op.-nor)
  - [`$and`](https://docs.mongodb.com/manual/reference/operator/query/and/#mongodb-query-op.-and) - [udemy](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850724#overview)
  - [`$not`](https://docs.mongodb.com/manual/reference/operator/query/not/#mongodb-query-op.-not) - [udemy](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850728#overview)
- Element query operators
  - [`$exist`](https://docs.mongodb.com/manual/reference/operator/query/exists/) - [udemy](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850730?start=180#overview)
  - [`$type`](https://docs.mongodb.com/manual/reference/operator/query/type/) - [udemy](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850732#overview)
- [Regex](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850734#overview)
  - [`$regex`](https://www.mongodb.com/docs/manual/reference/operator/query/regex/)
- [Aggregation Expression](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850736#overview)
  - [`$expr`](https://www.mongodb.com/docs/manual/reference/operator/query/expr/)
- Array query operators
  - [`$size`](https://docs.mongodb.com/manual/reference/operator/query/size/#mongodb-query-op.-size) - [udemy](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850746#overview)
  - [`$all`](https://docs.mongodb.com/manual/reference/operator/query/all) - [udemy](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850752#overview)
  - [`$elemMatch`](https://docs.mongodb.com/manual/reference/operator/query/elemMatch) - [udemy](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850760#overview)
- [Projection operators](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850794#overview)
  - [`$`](https://www.mongodb.com/docs/manual/reference/operator/projection/positional)
  - [`$elemMatch`](https://www.mongodb.com/docs/manual/reference/operator/projection/elemMatch)
  - [`$slice`](https://www.mongodb.com/docs/manual/reference/operator/projection/slice) - [udemy](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850800#overview)

##### Understanding about Cursor

- Khi thực hiện truy vấn dữ liệu thì ta sẽ được trả về hàng nghìn, thậm chí hàng triệu document
  Tuy nhiên, nếu như trả về sll dữ liệu cùng 1 lúc sẽ gây tốn bộ nhớ cũng như tài nguyên hệ thống.
  Một biện pháp tốt hơn là chia nhỏ dữ liệu thành từng batch và trả về lần lượt
  Từ đó, ta có khái niệm **Cursor**
- Cursor là một con trỏ, sẽ được trỏ đến từng batch dữ liệu mà ta muốn lấy.
  Từ đó giúp hệ thống vẫn hoạt động tốt kể cả khi phải xử lý một lượng lớn dữ liệu
  Cursor cũng hỗ trợ rất nhiều hàm trong việc xử lý dữ liệu
- Video: [Khái niệm về Cursor](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850774#overview)
- Video: [Sử dụng Cursor](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850778#overview)
- Video: [Sắp xếp lại kết quả trong Cursor](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850782#overview)
- Video: [Bỏ qua và giới hạn kết quả trong Cursor](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850784#overview)
- Tài liệu đọc: [Các hàm trong Cursor](https://docs.mongodb.com/manual/reference/method/js-cursor/)

##### Operators in updating data

- Field update operators
  - [`$set`](https://www.mongodb.com/docs/manual/reference/operator/update/set) - [udemy](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850846#overview)
  - [`$unset`](https://www.mongodb.com/docs/manual/reference/operator/update/unset) - [udemy](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850854#overview)
  - [`$rename`](https://www.mongodb.com/docs/manual/reference/operator/update/rename) - [udemy](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850856#overview)
- [Field match update operators](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850852#overview)
  - [`$inc`](https://www.mongodb.com/docs/manual/reference/operator/update/inc)
  - [`$min`](https://www.mongodb.com/docs/manual/reference/operator/update/min)
  - [`$max`](https://www.mongodb.com/docs/manual/reference/operator/update/max)
  - [`$mul`](https://www.mongodb.com/docs/manual/reference/operator/update/mul)
- Array update operators
  - [`$`](https://www.mongodb.com/docs/manual/reference/operator/update/positional)
  - [`$[]`](https://www.mongodb.com/docs/manual/reference/operator/update/positional-all)
  - [`$[<identifier>]`](https://www.mongodb.com/docs/manual/reference/operator/update/positional-filtered)
  - [`$push`](https://www.mongodb.com/docs/manual/reference/operator/update/push)
  - [`$pop`](https://www.mongodb.com/docs/manual/reference/operator/update/pop)
  - [`$addToSet`](https://www.mongodb.com/docs/manual/reference/operator/update/addToSet)
- Ngoài ra, đôi lúc bạn sẽ cập nhật các dữ liệu không tồn tại và muốn chèn thêm dữ liệu đó vào
  Lúc này bạn có thể sử dụng upsert()
  Video [`upsert()`](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850860#overview)

### Lab 7

- [datasource](https://drive.google.com/file/d/1MA2vmRWbj_xIoAn0KtqF_o1ZnygAg1I6/view?usp=sharing)
- import data by mongoimport
  ```shell
  mongoimport /uri:mongodb://localhost:27017/ /file:people.json /type:json /db:lab7 /collection:people /legacy /jsonArray
  ```

### Aggregation understanding

#### Aggregation definition

- Aggregation giúp xử lý truy vấn nâng cao của MongoDB,
  cho phép thực hiện tính toán, xử lý và kết hợp
  từ nhiều document để cho ra thông tin cần thiết
- Aggregation sẽ thực hiện xử lý dựa theo các **Aggregation Pipeline**
- Mỗi bước thực hiện 1 tính toán duy nhất trong các dữ liệu đầu vào
  và tạo dữ liệu đầu ra, sau đó dữ liệu đầu ra này
  sẽ lại thành dữ liệu đầu vào cho bước tiếp theo hoặc được trả về
- ![Aggregation flow](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L15_1.png?alt=media&token=e93500e9-b958-4a0b-8551-bd749fcdd140)
- Video: [Aggregation là gì?](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11859810#overview)
- Video: [Bắt đầu sử dụng Aggregation](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11859818#overview)
- Video: [Sử dụng Aggregation](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11859820#overview)

#### `$group` operator

- Toán tử `$group` giúp các nhóm document theo các điều kiện cho trước
- Đồng thời, ta cũng có thể thực hiện các phép tính toán thông qua [accumulator operators](https://docs.mongodb.com/manual/reference/operator/aggregation/group/#std-label-accumulators-group)
- Vi du:
  ```js
  db.persons
  	.aggregate([
  		{
  			$match: {
  				gender: "female"
  			}
  		},
  		{
  			$group: {
  				_id: {
  					state: "$location.state"
  				},
  				totalPersons: {
  					$sum: 1
  				}
  			}
  		}
  	])
  	.pretty();
  ```
- Video: [Giới thiệu về $group](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11859824#overview)
- Video: [Tìm hiểu về $group](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11859826#overview)
- Video: [Thêm phần tử vào mảng](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11859866#overview)
- Tài liệu đọc: [$group](https://docs.mongodb.com/manual/reference/operator/aggregation/group/#definition)

#### `project` operator

- Toán tử `$project` giúp chúng ta thực hiện thao tác Projection,
  tức là chỉ định các trường sẽ được trả về
- Ví dụ:
  ```js
  db.persons
  	.aggregate([
  		{
  			$project: {
  				_id: 0,
  				gender: 1
  			}
  		}
  	])
  	.pretty();
  ```
- Video: [Sử dụng $project](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11859846#overview)
- Video: [$group vs $project](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11859864#overview)
- Video: [Projection với mảng](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11859874#overview)
- Tài liệu đọc: [$project](https://docs.mongodb.com/manual/reference/operator/aggregation/project/#definition)

#### `$convert` operator

- Toán tử `$convert` được sử dụng để chuyển đổi kiểu dữ liệu của 1 trường
- Chúng ta có thể sử dụng toán tử khác để làm việc này,
  ví dụ như: `$toDate`, `$toInt`, `$toBool`,...

```js
db.persons
	.aggregate([
		{
			$project: {
				_id: 0,
				name: 1,
				email: 1,
				birthdate: {
					$convert: {
						input: "$dob.date",
						to: "date"
					}
				}
			}
		}
	])
	.pretty();
```

- Video: [Các phép chuyển đổi](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11859854#overview)
- Video: [Các toán tử chuyển đổi có sẵn](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11859858#overview)
- Tài liệu đọc: [$convert](https://docs.mongodb.com/manual/reference/operator/aggregation/convert/#example)

#### `$unwind` operator

- `$unwind` được dùng để phân tách giá trị của một mảng trong các document đầu vào
- Nếu như mảng có N phần tử thì trong output sẽ có N document
- ví dụ
  ```js
  db.friends
  	.aggregate([
  		{
  			$unwind: "$hobbies"
  		}
  	])
  	.pretty();
  ```
- Video: [Toán tử $unwind](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11859870#overview)
- Tài liệu đọc: [$unwind](https://docs.mongodb.com/manual/reference/operator/aggregation/unwind/#example)

#### `$bucket` operator

- Toán tử `$bucket` được sử dụng để phân loại các Document đến thành các nhóm
  dựa trên 1 biểu thức và ranh giới được chỉ định
- ví dụ:
  ```js
  db.persons
  	.aggregate([
  		{
  			$bucket: {
  				groupBy: "$dob.age",
  				boundaries: [18, 30, 40, 50, 60, 120],
  				output: {
  					numPersons: {
  						$sum: 1
  					},
  					averageAge: {
  						$avg: "$dob.age"
  					}
  				}
  			}
  		}
  	])
  	.pretty();
  ```
- ngoài ra cũng có toán tử `$bucketAuto` cũng tương tự như $bucket
  nhưng các ranh giới sẽ được tự động tính toán dựa trên số nhóm muốn chia
- Ví dụ

  ```js
  db.persons
  	.aggregate([
  		{
  			$bucketAuto: {
  				groupBy: "$dob.age",
  				buckets: 5,
  				output: {
  					numPersons: {
  						$sum: 1
  					},
  					averageAge: {
  						$avg: "$dob.age"
  					}
  				}
  			}
  		}
  	])
  	.pretty();
  ```

- Video: [Toán tử $bucket](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11859882#overview)
- Tài liệu đọc: [$bucket](https://docs.mongodb.com/manual/reference/operator/aggregation/bucket)
- Tài liệu đọc: [$bucketAuto](https://docs.mongodb.com/manual/reference/operator/aggregation/bucketAuto/)
- Vẫn còn rất nhiều toán tử khác chưa được giới thiệu, bạn có thể tham khảo ở các link sau:

- [Tài liệu đọc 1](https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/)
- [Tài liệu đọc 2](https://docs.mongodb.com/manual/reference/operator/aggregation/)

### Lab8 - Aggregation operators exercise

- [datasource](https://drive.google.com/file/d/1MA2vmRWbj_xIoAn0KtqF_o1ZnygAg1I6/view?usp=sharing)
- import data by mongoimport
  ```shell
  mongoimport /uri:mongodb://localhost:27017/ /file:people.json /type:json /db:lab8 /collection:people /legacy /jsonArray
  ```

### Others in MongoDB

#### Index

- Index hay chỉ mục trong MongoDB là một cấu trúc dữ liệu
  dùng để định vị và truy cập nhanh nhất vào các Document.
- Có thể Index như là mục lục vậy.
  Thông thường khi tìm kiếm một Document thì hệ thống sẽ phải quét toàn bộ collection và lọc ra các document phù hợp.
  Nếu như bạn đang có hàng triệu Document thì thời gian thực hiện sẽ rất lâu
  Index sẽ giúp giải quyết vấn đề này
  giống như việc xem mục lục sách
  hệ thống chỉ cần duyệt qua Index là sẽ lọc được các Document cần tìm
- Dù index đóng vai trò quan trọng trong việc tối ưu truy vấn
  và tăng tốc độ tìm kiếm trong Database nhưng nhược điểm của nó là tốn thêm bộ nhớ để lưu trữ
  Do vậy, việc Index cho các cột phải được tính toán, tránh lạm dụng
  Đồng thời các thao tác như thêm, sửa, xóa cũng sẽ chậm hơn do mỗi lần thực hiện thao tác sẽ phải đánh lại Index
- Video: [Index là gì](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850914#overview)
- Video: [Index đơn](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850922#overview)
- Tài liệu đọc: [Cơ chế hoạt động của Index](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11859188#overview)
- Video: [Những hạn chế của Index](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850928#overview)
- Video: [Index hỗn hợp](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850936#overview)
- Ngoài ra, khi sử dụng Index trên một trường có thứ tự, các thao tác sắp xếp kết quả cũng sẽ thực thi nhanh hơn.
- Video: [Sử dụng Index cho việc sắp xếp](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850942#overview)
- Index cũng cho phép bạn thiết lập một số lựa chọn để việc sử dụng Index hiệu quả hơn, ví dụ:
  - Tham số `Unique`:
    - Tạo một **Unique Index** để Collection sẽ không chấp nhật việc chèn hoặc cập nhất các Document trong đó giá trị khóa Index khớp với giá trị hiện có trong Index
    - [Video tham khảo](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850952#overview)
  - Tham số `PartialFilterExpression`:
    - Tạo **Partial Indexes** chỉ tham chiếu tới các một số Document thỏa mãn điều kiện
    - [Video tham khảo](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850956#overview)
    - [Video tham khảo](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850962#overview)
    - [Tài liệu đọc tham khảo](https://docs.mongodb.com/manual/core/index-partial/)
  - Tham số `ExpireAfterSeconds` chỉ định khoảng thời gian mà MongoDB sẽ giữ cho Document tồn tại
    - [Video tham khảo](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850970#overview)

#### Multikey Indexes & Text Indexes

- **Multikey Indexes** là một dạng Index đặc biệt sử dụng cho các trường dạng mảng
  **Multikey Indexes** sẽ tạo các khóa cho từng phần tử trong mảng
  từ đó giúp cho việc truy vấn phần tử mảng nhanh hơn

  - Video: [Sử dụng Multikey Indexes](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850984#overview)
  - Tài liệu đọc: [Multikey Indexes](https://docs.mongodb.com/manual/core/index-multikey/)

- **Text Indexes** được sử dụng cho các trường dạng chuỗi
  Nếu bạn chỉ tạo index đơn thuần cho các trường dạng chuỗi
  lúc này, Index chỉ phát huy tác dụng khi bạn tìm theo một chuỗi đầy đủ nhưng sẽ ko tốt nếu bạn muốn tìm chuỗi theo từ khóa
  Lúc này thì bạn nên sử dụng Text Indexes
  MongoDB sẽ tự động cắt chuỗi thành từng từ khóa nhỏ
  đồng thời cũng lọc đi các từ khóa vô nghĩa **(a, an, of, the, ...)** và tạo Index cho từng từ khóa
  Lúc này khi tìm chuỗi theo từ khóa sẽ nhanh hơn
  - Lưu ý là mỗi Collection chỉ có thể có một Text Indexes duy nhất
    Do Text Indexes sẽ tốn rất nhiều bộ nhớ nên nếu có quá nhiều thì sẽ ảnh hưởng lớn đến hệ thống
  - Video: [Khái niệm về Text Indexes](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850986#overview)
  - Video: [Sắp xếp sử dụng Text Indexes](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850988#overview)
  - Video: [Kết hợp nhiều trường vào một Text Indexes](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850994#overview)
  - Video: [Loại các từ trong Text Indexes](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850998#overview)
  - Tài liệu đọc: [Text Indexes](https://docs.mongodb.com/manual/core/index-text/)

#### Transactions

- Transaction là 1 tập hợp các thao tác mà ở đó
  hoặc là các thao tác đó được thực hiện thành công
  hoặc là không một thao tác nào được thực hiện thành công cả
  Giúp cho dữ liệu được đảm bảo tính toàn vẹn
  do trong quá trình chèn hoặc sửa dữ liệu có thể xảy ra lỗi, khiến cho dữ liệu bị sai so với ban đầu
  - Video: [Transaction là gì](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11861268#overview)
  - Video: [Trường hợp cần dùng Transaction](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11861270#overview)
  - Video: [Cơ chế hoạt động của Transaction](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11861272#overview)
  - Tài liệu đọc: [Transactions](https://docs.mongodb.com/manual/core/transactions/)

### Performance and Security

#### Security in MongoDB

- Bạn có thể thấy, khi truy cập vào MongoDB thì bạn sẽ có toàn quyền thực hiện các thao tác với dữ liệu trong Database
  Đây là một cơ chế nguy hiểm, làm giảm sự bảo mật của Database
  Vậy nên chúng ta cần tăng cường cơ chế bảo mật hơn
  bằng cách tạo các người dùng và chia quyền cho từng người dùng
  Từ đó sẽ giới hạn được các thao tác mà từng người dùng có thể thực hiện
- Video: [Cơ chế bảo mật trong MongoDB](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11861174#overview)
- Video: [Ví dụ về Role](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11861176#overview)
- Video: [Tạo một User mới](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11861178#overview)
- Video: [Các Role có sẵn trong MongoDB](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11861182#overview)
- Video: [Gán một Role vào một User](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11861188#overview)
- Video: [Chỉnh sửa các Role](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11861194#overview)

#### Performance enhancing in MongoDB

- Hiệu suất xử lý dữ liệu cũng là một trong những thước đo vô cùng quan trọng trong mỗi cơ sở dữ liệu.
  Để tăng cường thêm hiệu suất cho hệ thống, chúng ta có thể sử dụng một số biện pháp như sau:
  - **Capped Collection**
    - Là các Circular Collection có kích cỡ cố định mà theo sau thứ tự chèn để làm tăng cao hiệu suất của các hoạt động `create`, `read` và `delete`.
    - Với Circular, nó nghĩa là khi kích cỡ cố định được cấp phát hết cho Collection
      thì nó sẽ bắt đầu xóa Document **cũ nhất** trong Collection đó mà không cần cung cấp bất kỳ lệnh tường minh nào
    - Capped Collection giới hạn các hoạt động cập nhật tới Document nếu các cập nhật đó làm tăng kích cỡ của Document
    - Khi Capped Collection lưu giữ các Document theo trật tự của Disk Storage
    - nó đảm bảo rằng kích cỡ tài liệu không tăng hơn kích cỡ được cấp phát trên Disk
      Capped Collection là tốt nhất để lưu giữ thông tin log, cache data, ...
    - Video: [Capped Collection](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11861236#overview)
  - **Replica Sets**
    - Trong MongoDB là một nhóm các instance của MongoDB duy trì cùng một bộ dữ liệu
    - Các replica set cung cấp tính dự phòng và tính sẵn sàng cao và là cơ sở để triển khai nhập xuất dữ liệu khi cần thiết
    - Video: [Replica Sets](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11861238#overview)
  - **Sharding**
    - Là một tiến trình lưu giữ các bản ghi dữ liệu qua nhiều thiết bị
      và nó là một phương pháp của MongoDB để đáp ứng yêu cầu về sự gia tăng dữ liệu
    - Khi kích cỡ của dữ liệu tăng lên, một thiết bị đơn không thể đủ để lưu trữ dữ liệu
    - Sharding giải quyết vấn đề này với việc mở rộng phạm vi theo bề ngang **(horizontal scaling)**.
    - Với Sharding, bạn bổ sung thêm nhiều thiết bị để hỗ trợ cho việc gia tăng dữ liệu và các yêu cầu của các hoạt động đọc và ghi
    - Video: [Sharding](https://funix.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11861240#overview)

### Assignment 2: Build MongoDB database

#### Project statement

- phân tích và thiết kế cơ sở dữ liệu sử dụng MongoDB phục vụ cho một nhu cầu cụ thể.
  - Phân tích được tập dữ liệu.
  - Thiết kế được lược đồ của Database dựa trên các phân tích.
  - Hiểu được sự khác nhau khi thiết kế Database giữa SQL Server và MongoDB.
  - Viết được các câu lệnh để tạo Database theo như lược đồ đã thiết kế.
  - Liệt kê được các Business Query (truy vấn nghiệp vụ) và viết các câu lệnh để thực hiện các truy vấn đó.
  - Viết các câu lệnh để thực hiện các thao tác CRUD.

#### Resource

- [link](https://drive.google.com/file/d/1OqXKZC6ygasKbyj1eDVfzOsNa_hIY5sN/view?usp=sharing)

#### Documentation

- [Xây dựng ERD cho MongoDB](https://dataedo.com/tutorials/how-to-create-er-diagram-for-mongodb)
- [Sự khác biệt về việc thiết kế Database giữa SQL Server và MongoDB](https://www.mongodb.com/developer/article/mongodb-schema-design-best-practices/)

## Web scrapping with Python

### Work with data and Pandas

#### Work with text file

- Trong phần đầu của bài học, chúng ta sẽ cùng tìm hiểu về các hoạt động của file trong Python.
  Cụ thể hơn là về cách mở file, đọc file, ghi file, đóng file cũng như các phương thức làm việc với tập tin mà bạn nên biết.

- Video: [Mở file trong Python (Link Backup)](https://drive.google.com/file/d/1GdSGb9207jyho33W9tiQFFiI5G4TuzXD/view)
- Video: [Ghi file trong Python (Link Backup)](https://drive.google.com/file/d/1chNEwOEUk2puy7oLEC1xwkIDhNNd5QQn/view)
- Các bạn có thể tìm hiểu kỹ hơn về các thao tác cơ bản với file ở tài liệu đọc dưới đây:
- Tài liệu đọc: [Đọc/ghi file trong Python](https://drive.google.com/file/d/17IbjlB_f1xVAqBd8lLS6BIVGnmmPRTJp/view)
- Ngoài ra, bạn có thể tham khảo các tài liệu sau để biết cách đọc dữ liệu từ file ảnh hoặc file audio:
- Tham khảo: [Đọc file Audio với Python](https://analyticsindiamag.com/step-by-step-guide-to-audio-visualization-in-python/)
- Tham khảo: [Đọc file Ảnh với OpenVC và Python.](https://docs.opencv.org/4.5.2/db/deb/tutorial_display_image.html)

#### Pandas with Python

- Pandas là một thư viện Python cung cấp
  các cấu trúc dữ liệu nhanh, mạnh mẽ, linh hoạt và mang hàm ý.
- Tên thư viện được bắt nguồn từ panel data (bảng dữ liệu).
- Pandas được thiết kế để làm việc dễ dàng và trực quan
  với dữ liệu có cấu trúc (dạng bảng, đa chiều, có tiềm năng không đồng nhất)
  và dữ liệu chuỗi thời gian.

- Mục tiêu của pandas là trở thành khối căn bản (building block)
  cấp cao cơ bản cho công việc thực tế,
  phân tích dữ liệu thế giới thực trong Python,
  và rộng hơn là trở thành công cụ thao tác / phân tích
  mã nguồn mở mạnh mẽ và linh hoạt nhất có sẵn
  trong bất kỳ loại ngôn ngữ lập trình nào.

- Video: [Load dữ liệu dataframe với Pandas (Link Backup)](https://www.coursera.org/learn/python-for-applied-data-science-ai/lecture/QN5Cl/loading-data-with-pandas)
- Video: [Làm việc với Pandas (Link Backup)](https://drive.google.com/file/d/1GOu06lUUQ6JDI8t2MOaee5lHE2PBRT2H/view)
- Các bạn có thể tìm hiểu kỹ hơn về các thao tác cơ bản với dataframe trên Pandas ở tài liệu đọc dưới đây:

- Tài liệu đọc: [Pandas - Deep AI KhanhBlog](https://phamdinhkhanh.github.io/deepai-book/ch_appendix/appendix_pandas.html#)
- Đối với các học viên có nền tảng tiếng Anh tốt
  và muốn tìm hiểu sâu hơn về Pandas,
  các bạn có thể tham thảo thêm phần tài liệu về Pandas ở official website:
  - Tài liệu đọc tham khảo: [Getting Started with Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)
  - Note: Trong tài liệu đọc thêm, có một số phần nâng cao và khó hiểu,
    chúng ta không cần phải tìm hiểu hết mọi thứ ngay trong quá trình đọc tài liệu tham khảo.
    Sau này, trong quá trình sử dụng thư viện Pandas ở các bài lab/assignment
    chúng ta có thể quay lại sử dụng nguồn tài liệu này để tra cứu thêm và tìm hiểu sâu hơn về Pandas.

### Lab9 - Working with data in Python

- Đọc và ghi là các tác vụ căn bản nhất với dữ liệu,
  hãy thực hành với các hàm tích hợp sẵn trong Python:

  - [9.1 Reading Files with Open](https://colab.research.google.com/drive/1aqWXKNTI3A6KA3-fPZoTYuG621Y42Hp6?usp=sharing)
  - [9.2 Writing Files with Open](https://colab.research.google.com/drive/1JjDb3t83TcpFLfQaJNS0U3HHP1kdNcxk?usp=sharing)

- Hãy làm quen với Pandas bằng cách hoàn thành lab sau:

  - [9.3 Getting started with Pandas in Python](https://colab.research.google.com/drive/1z5ZbJ5PKYzzBmqmXrabq7x2azWaMzygC?usp=sharing)

### Work with web data in Python

#### Utilize Regex to extract data

- Regex là các mẫu (pattern) thay vì các chuỗi cụ thể được sử dụng tìm/thay thế (Find/Replace).
- Là một công cụ cực mạnh cho xử lí chuỗi trong Python…
- Ví dụ: Khi kiểm tra tính hợp lệ của email hoặc số điện thoại thì điều bạn nghĩ tới đầu tiên chính là regex.
- Regex là viết tắt của Regular Expression, tên thuần Việt là biểu thức chính quy.

- Video: [Tìm hiểu về toán tử Regex](https://www.coursera.org/learn/python-network-data/lecture/bMyWb/11-1-regular-expressions)
- Video: [Trích xuất dữ liệu](https://www.coursera.org/learn/python-network-data/lecture/5LN6R/11-2-extracting-data)
- Tài liệu đọc: [Regex Cheat Sheet](https://www.dataquest.io/blog/regex-cheatsheet/)

#### Process JSON data type

- JSON là viết tắt của JavaScript Object Notation.
- là một kiểu định dạng dữ liệu tuân theo một quy luật nhất định
  mà hầu hết các ngôn ngữ lập trình hiện nay đều có thể đọc được.
  JSON là một tiêu chuẩn mở để trao đổi dữ liệu trên web.

- Định dạng JSON sử dụng các cặp key – value để dữ liệu sử dụng.
  Nó hỗ trợ các cấu trúc dữ liệu như đối tượng và mảng, ví dụ: ![vi_du](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L18_1.png?alt=media&token=6d58726d-5188-454e-bec9-092f30f32047)

Video: [Giới thiệu về JSON](https://www.coursera.org/learn/python-network-data/lecture/BZD1x/13-5-javascript-object-notation-json)
Video: [Xử lý dữ liệu dạng JSON](https://www.coursera.org/learn/python-network-data/lecture/G1up7/worked-example-json-chapter-13)

### Lab10 - RegEx

- Statement [funix course](https://courses.funix.edu.vn/courses/course-v1:FUNiX+DEP302x_01-A_VN+2021_T8/courseware/99ba64326f6b486d8b8aa72579680701/f55b9d31e754433ba2eb246ae9848cd7/?child=first)
- Datasource [link](https://drive.google.com/file/d/1A1wB2fxR7vPmSm67URgKhgJqSdxGIpaI/view?usp=sharing)

### Basic scrapy

#### Web scraping & Scrapy

- Một số trang web có thể chứa một lượng rất lớn dữ liệu vô giá,
  như giá cổ phiếu, chi tiết sản phẩm, số liệu thống kê thể thao, thông tin liên hệ của công ty,...
- Web scraping đề cập đến việc trích xuất dữ liệu từ một trang web.
  Thông tin này được thu thập và sau đó xuất thành định dạng hữu ích hơn cho người dùng ( có thể là bảng tính hoặc API).

- Scrapy là một thư việc Python được tạo ra để quét và xây dựng các trình thu nhập dữ liệu web.
  Nó nhanh chóng, đơn giản và có thể điều hướng qua nhiều trang web mà không mất nhiều công sức

- Scrapy sẽ gồm các thành phần như sau:
  - **Scrapy Engine**: có trách nhiệm kiểm soát luồng dữ liệu
    giữa tất cả các thành phần hệ thống và kích hoạt các sự kiện
    khi 1 số hành động xảy ra.
  - **Scheduler**: giống như 1 hàng đợi (queue), scheduler sắp xếp thứ tự các URL cần download
  - **Spiders**: Spiders là class được viết bởi người dùng
    Chúng có trách nhiệm bóc tách dữ liệu cần thiết vào tạo các url mới để nạp lại cho Scheduler qua engine
  - **Pipeline**: Những dữ liệu Spiders bóc tách được sẽ được đưa đến đây
    Item pipeline có nhiệm vụ xử lý chúng và lưu vào cơ sở dữ liệu
  - **Middlewares**: Là các thành phần nằm giữa Engine với các thành phần khác
    Chúng đều có mục đích là giúp người dùng có thể tùy biến, mở rộng khả năng xử lý cho các thành phần
    Ví dụ: sau khi download url xong, bạn muốn tracking, gửi thông tin ngay lúc đó
    thì bạn có thể viết phần mở rộng và sửa lại cấu hình để sau khi Downloader tải xong trang thì sẽ thực hiện việc tracking.
  - ![scapy engine](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L17_1.png?alt=media&token=503e8a9c-478c-4828-94ba-f9180322a596)
  - để cài đặt Scrapy, các bạn có thể cài thông qua pip như sau:
    `pip install scrapy`
  - Nếu bạn sử dụng Windows hoặc MacOS thì bạn có thể cài đặt Scrapy trên Anaconda, bạn có thể xem video hướng dẫn [tại đây](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/11497662#overview)

#### Utilize Scrapy

- Scrapy sẽ cung cấp cho bạn một số câu lệnh cơ bản như sau khi các bạn thao tác trên Terminal

  - `bench`
    - cú pháp: `scrapy bench`
    - chạy một benchmark test để kiểm tra về hiệu suất của scrapy trên máy của bạn
  - `fetch`
    - cú pháp: `scrapy fetch <url>`
    - Tải xuống trang web ở địa chỉ <url> đầu vào bằng trình tải xuống của Scrapy và ghi nội dung vào đầu ra chuẩn
  - `genspider`
    - cú pháp: `scrapy genspider [-t template] <name> <domain>`
    - tạo một spider mới.
      tham số <name> được đặt làm tên của spider,
      <domain> được sử dụng để tạo các thuộc tính _allow_domains_ và _start_urls_ của spider
  - `startproject`
    - cú pháp: `scrapy startproject <project_name> [project_dir]`
    - tạo một dự án Scrapy mới có tên là project_name, trong thư mục project_dir
      nếu project_dir ko được chỉ định
      thì project_dir sẽ giống như project_name
  - `shell`
    - cú pháp: `scrapy shell`
    - bắt đầu tương tác cho URL (nếu được cung cấp)
  - video:
    - [bench & fetch](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249086#overview)
    - [genspider & startproject](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249090#overview)
    - [shell](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249092#overview)

- `Scrapy shell` là 1 shell tương tác
  nơi bạn có thể thử và gỡ lỗi _scraping code_ của mình nhanh chóng
  mà không cần phải chạy trình thu thập dữ liệu
- `Scrapy shell` cũng được sử dụng để kiểm tra mã trích xuất dữ liệu
  nhưng bạn thực sự có thể sử dụng nó để kiểm tra bất kỳ loại mã nào vì nó cũng là một trình shell python bình thường
- Tài liệu đọc: [Scrapy shell](https://docs.scrapy.org/en/latest/topics/shell.html#topics-shell)
- Video: [Scrapy commands](https://docs.scrapy.org/en/latest/topics/commands.html)
- Sau khi tải được toàn bộ trang web,
  công việc tiếp theo sẽ trích xuất các thông tin lấy được từ trang web đó
  Với _Scrapy_ bạn có thể sử dụng xPath Selector hoặc CSS Selector để truy vấn các phần tử, từ đó trích xuất các thông tin cần thiết
- 1 lưu ý là Scrapy sẽ không chạy được Javascript khi load trang web
  vậy nên ta cần "Disable Javascript" trên Chrome để có thể tìm được selector chính xác nhất cho các phần tử muốn lấy.
- Video: [Sử dụng Scrapy phần 4](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249096#overview)
- Video: [Sử dụng Scrapy phần 5](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249098#overview)

#### Understanding xPath & CSS Selector

- Video: [XPath & CSS Selectors](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/11497700#overview)

- **XPath** là một trong 3 thành phần trong ngôn ngữ XSL – Extensible Style Language.
  Đó là ngôn ngữ hỗ trợ tìm kiếm thông tin trong tài liệu XML
  sử dụng biểu thức XPath để định hướng tìm kiếm dữ liệu trên XML
  thay vì phải thực hiện tìm kiếm đệ quy để duyệt cây XML.
- **Xpath** được sử dụng để tìm vị trí bất kỳ phần tử trên Web sử dụng cấu trúc HTML – DOM.
  XPath chứa đường dẫn của phần tử nằm trên trang Web.

- Video: [XPath cơ bản](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/11497706#overview)
- Video: [Bản chất của XPath](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249192#overview)
- Tài liệu tham khảo: [XPath cheatsheet](https://devhints.io/xpath)

- **XPath** cũng có cơ chế Preceding và Following cho phép lọc các đối tượng UI từ một đối tượng xác định trước đó.
  Các cách tìm kiếm và định vị các phần tử UI trong Selenium với XPath ở trên
  sẽ giúp việc tìm kiếm được chính xác và hiệu quả hơn,
  lựa chọn cách tìm kiếm phù hợp với từng tình huống.

Video: [Preceding](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249176#overview)
Video: [Following](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249188#overview)

- **CSS Selector** cũng tương tự như xPath, tuy nhiên lại dễ viết và gọn hơn xPath. Đổi lại thì CSS sẽ khó thực thi được các truy vấn phức tạp như với xPath

Video: [CSS Selectors cơ bản](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/11497702#overview)

Video: [Bản chất của CSS Selectors](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/11497704#overview)

Tài liệu tham khảo: [CSS Selector Cheatsheet](https://gist.github.com/magicznyleszek/809a69dd05e1d5f12d01)

#### Build a complete Spider

- Việc tiếp theo chúng ta cần làm là trích xuất tên nước,
  link để đi đến trang chứa các số liệu của nước đó.
  Công việc này có thể được hoàn thành bằng cách sử dụng xPath.
- Video: [Worldometers (Phần 1)](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/11497720#overview)
- Ta mới chỉ có thể lấy được tên các nước và link để lấy thông tin.
  Ta sẽ cần tạo một request mới đến các link đó để có thể lấy được dữ liệu thông qua hàm `response.follow`
- Video: [Worldometers (Phần 2)](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/11497722#overview)
- Tuy nhiên, khi tạo một request mới như vậy thì chúng ta chưa xử lý,
  trích xuất được các dữ liệu từ request mới, vậy nên ta cần xây dựng 1 call_back tương tự với hàm `parse`
  để có thể trích xuất các dữ liệu trả về từ request mới.
  Đồng thời, bạn cũng có thể sử dụng meta để truyền dữ liệu qua lại giữa 2 call_back.
- Video: [Worldomaters (Phần 3)](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/11497724#overview)
- Video: [Worldomaters (Phần 4)](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/11497726#overview)
- Sau khi đã trích xuất được các thông tin cần thiết,
  ta cần lưu dữ liệu đó lại vào một file (`.csv` , `.json` hoặc `.xml`).
  Để làm được điều này, bạn chỉ cần thêm tham số `-o <tên file>` vào câu lệnh để chạy spider.
- Ví dụ: `scrapy crawl countries -o export.csv`
- Video: [Lưu dữ liệu xuống Dataset](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/11497756#overview)

#### Debug Spider

- **Debug** là quá trình tìm kiếm ra lỗi hay nguyên nhân gây ra lỗi (_bug_ ở đâu) để có hướng sửa lỗi (_fix bug_).
- Việc kiểm soát lỗi của rất nhiều các dòng code là việc không hề đơn giản với những người lập trình viên chưa có nhiều kinh nghiệm.
- Đôi lúc, khi chúng ta xây dựng Spider sẽ có thể gặp các lỗi, vì vậy chúng ta nên sử dụng một số phương pháp để debug xem Spider đang gặp vấn đề ở đoạn lệnh nào và sửa lại.
- Video: [Debug là gì?](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/21485656#overview)
- Chúng ta có 4 phương pháp Debug chính với Spider:
  - **Parse Command**
    Cách cơ bản nhất để kiểm tra đầu ra của Spider là sử dụng _Parse Command_.
    Nó cho phép kiểm tra hành vi của các phần khác nhau của Spider ở cấp hàm (method level).
    Nó có ưu điểm là linh hoạt và dễ sử dụng, nhưng không cho phép gỡ lỗi mã bên trong một method.
  - **Scrapy Shell**
    Mặc dù _Parse Command_ rất hữu ích để kiểm tra hành vi của một Spider,
    nhưng việc kiểm tra những gì xảy ra bên trong một call*back sẽ giúp ích rất ít
    cho việc hiển thị phản hồi đã nhận và kết quả đầu ra.
    \_Scrapy Shell* sẽ giúp gỡ lỗi trong những tình huống như vậy.
  - **Open in browser**
    Đôi khi bạn chỉ muốn xem một _response_ trông như thế nào trong trình duyệt,
    bạn có thể sử dụng hàm _open_in_browser_ cho điều đó.
  - **Logging**
    _Logging_ là một tùy chọn hữu ích khác để nhận thông tin về lần chạy _Spider_ của bạn.
    Mặc dù không thuận tiện nhưng nó có lợi thế là
    các log sẽ có sẵn trong tất cả các lần chạy trong tương lai nếu chúng cần thiết.
- Video: [Debug phần 1](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16388478#overview)
- Video: [Debug phần 2](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16388482#overview)
- Tài liệu tham khảo: [Debug Spider trong Scrapy](https://docs.scrapy.org/en/latest/topics/debug.html)

### Lab11 - Collect data from static web

- Target web: [Worldometers](https://www.worldometers.info/world-population/population-by-country/)
- Statement: [funix course](https://courses.funix.edu.vn/courses/course-v1:FUNiX+DEP302x_01-A_VN+2021_T8/courseware/99ba64326f6b486d8b8aa72579680701/724f5c63a3a5415aaaaa858768fab84d/?child=first)
- Chuẩn bị:

  - Cài scrapy: `pip install scrapy`
  - Cài ipython: `pip install ipython`

- Các bước để hoàn thành bài Lab:

  - 1-Tạo một Project mới thông qua lệnh `startproject`
    `scrapy startproject worldometers`
    `cd worldometers`
    `scrapy genspider countries https://www.worldometers.info/world-population/population-by-country/`
  - 2-Lên trang web Worldometers và tìm các selector phù hợp để truy vấn phần tử.
  - 3-Xây dựng Spider để có thể lấy được danh sách các nước ở trang chủ.
    Sau đó sẽ chuyển request sang từng link để có thể lấy dữ liệu về dân số cụ thể của một nước.
  - 4-Lưu dữ liệu đã thu thập dưới dạng file `.csv`
    `scrapy crawl countries -o countries.csv`

### Collection from dynamic web with Splash

#### Splash introduction

- Splash cung cấp một công cụ để hiển thị mã javaScript cho khung trình thu thập thông tin Scrapy.
  Nó có các chức năng sau:

  - Trả về HTML của một trang web.
  - Xử lý đồng thời nhiều trang.
  - Tắt việc tải hình ảnh của trang web, tăng tốc độ xử lý.
  - Thực thi các đoạn code JS do người dùng định nghĩa.
  - Được viết ở dạng Lua Script.
  - Như vậy Splash sẽ có thể giải quyết được các vấn đề
    khi chúng ta cần tương tác với trang web mới có thể lấy được dữ liệu.

- Video: [Splash giải quyết vấn đề gì?](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249404#overview)

- Cách cài đặt Splash đa nền tảng là sử dụng Docker
- nếu bạn có thể chạy Docker trên Windows,
  bạn có thể kéo Splash Image và sử dụng nó.
- Để cài đặt Splash, bạn có thể tham khảo các tài liệu dưới đây:

- Video: [Cài đặt Splash trên Window và MacOS](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/19190770#overview)

- Sau khi cài đặt và chạy được Splash, bạn có thể vào _localhost:8050_ để kiểm tra xem Splash đã được cài đặt thành công chưa.
- [localhost:8050](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP302x%2FSummary_Image%2FDEP302_sum_L19_1.png?alt=media&token=813931ba-6990-49b6-8fdb-a2bbc478b5f8)
- Sau đó, bạn có thể sử dụng Splash để thu thập dữ liệu
  thông qua việc tương tác với các trang web.
  Một số thao tác cơ bản như là tương tác với form, button,
  cũng như thay đổi Header của request.
  Kết quả trả về từ Splash ngoài HTML của trang web thì có thể là ảnh chụp màn hình của trang web.

- Video: [Splash cơ bản](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249426#overview)
- Video: [Thao tác với các phần tử](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249436#overview)
- Video: [Thay đổi Request Header](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249446#overview)

#### Combine Splash with Scrapy

- Scrapy có thể sử dụng kèm với headless browser như Splash
  để chờ trang web render ra nội dung và cookie,
  rồi gửi lại HTML đã generated về crawler
  để bóc tách như bình thường, việc này làm tốn thêm một ít thời gian chờ
  nhưng bạn sẽ có thể tương tác được với trang web.
- Chúng ta cũng có thư viện `scrapy-splash`
  để hỗ trợ việc tương tác giữa Splash và Scrapy.
  Bạn có thể tải thư viện này thông qua pip hoặc Anaconda.

- Video: [Cơ chế ẩn danh trong Splash](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249468#overview)
- Video: [Splash với Scrapy](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249486#overview)
- Video: [Trích xuất dữ liệu](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16249496#overview)

### Lab12 - Splash with Scrapy

- Data resource: [web.archive.org](https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/)
  Hãy viết chương trình để thu thập dữ liệu về các đồng BTC.

- Chuẩn bị cho project

  - Tạo docker: Truy cập https://labs.play-with-docker.com/ để chạy docker online
  - Cài splash trên docker: `sudo docker pull scrapinghub/splash`
  - Chạy splash trên docker với port 8050: `sudo docker run -it -p 8050:8050 --rm scrapinghub/splash`
  - Mở port 8050 từ địa chỉ được cấp bởi docker ( dùng địa chỉ này cho config 'SPLASH_URL' trong file `settings.py`)
  - Cài scrapy-splash ở máy local: `pip install scrapy-splash`
  - Cấu hình file `settings.py` trong scrapy project theo [link](https://github.com/scrapy-plugins/scrapy-splash#configuration)

- Các bước để hoàn thành bài Lab như sau:

1. Tạo Project mới với câu lệnh startproject
   `scrapy startproject livecoin`
   `scrapy genspider coin web.archive.org`
2. Tìm selector tương ứng với button để chuyển Tab.
   Sau đó viết Splash Script để có thể tương tác với trang Web
   và lấy được dữ liệu từ tab BTC.

3. Tìm selector để có thể truy vấn được các trường "Pair" và "Volume (24h)"

4. Viết Spider kết hợp với Scrapy để thu thập dữ liệu,

5. Lưu các dữ liệu đó xuống file `.json`
   `scrapy crawl coin -o coin.json`

### Collection data from API

- Có một số trường hợp khi ta muốn lấy dữ liệu từ các trang web động
  không cần thiết phải sử dụng đến Splash mà có thể tìm API mà trang web đó sử dụng để lấy API.
  Ta sẽ thu thập các dữ liệu trực tiếp từ API đó
  việc này sẽ giúp các thao tác thu thập dữ liệu đơn giản hơn rất nhiều.
  Tuy nhiên, đổi lại ta cũng sẽ mất thời gian để đi tìm các API của trang web đó và đôi khi API có thể bị chặn.

- Thông thường các API sẽ trả về dữ liệu dưới dạng JSON.
  Vậy nên thay vì dùng XPath hoặc CSS Selector thì ta sẽ phải lấy dữ liệu từ JSON.

Video: [Scraping APIs Phần 1](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/19293104#overview)
Video: [Scraping APIs Phần 2](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/19295014#overview)
Video: [Scraping APIs Phần 3](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/19295712#overview)
Video: [Scraping APIs Phần 4](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/19296442#overview)
Video: [Scraping APIs Phần 5](https://funix.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/19296452#overview)

### Assignment3 - Building Covid19 data collection system

- **Tên dự án**: Xây dựng hệ thống thu thập dữ liệu Covid 19

- **Tổng quan dự án**

  - Ở bài ASM này, ta cần xây dựng hệ thống thu thập dữ liệu số ca nhiễm Covid 19 ở VIệt Nam qua từng ngày khác nhau.
    - Xây dựng được Spider để tải và bóc tách các dữ liệu cần thiết.
    - Sử dụng Spider để xử lý việc chuyển trang web để lấy được các dữ liệu từ ngày cũ hơn.
    - Lấy được dữ liệu về ngày tháng và số ca nhiễm mới vào ngày đó.
    - Lưu các dữ liệu thu thập được dưới dạng `.json`

- **Chi tiết dự án**

  - Làm thế nào để hoàn thành bài tập?

    - Để hoàn thành bài ASM, bạn cần cài đặt Scrapy ở máy. Cũng như nắm được các kiến thức về Scrapy, xPath hoặc CSS Selector để có thể truy vấn và xử lý dữ liệu.

- **Tài nguyên tham khảo**

  - Trang Web bạn sẽ thu thập dữ liệu có [địa chỉ như sau](https://web.archive.org/web/20210907023426/https://ncov.moh.gov.vn/vi/web/guest/dong-thoi-gian).
  - Trang Web này chứa các thông tin dạng Text về các ca mắc mới theo từng mốc thời gian.
    Bạn sẽ cần trích xuất dữ liệu ở các thông tin này.
  - _Lưu ý_: Do hiện trang web đã thay đổi giao diện, nên bạn sẽ sử dụng link từ web.archive.org để thực hành.

- Ngoài ra, bạn có thể tham khảo một số tài liệu sau:

  - [Sử dụng Regex với Python](https://www.tutorialspoint.com/python/python_reg_expressions.htm)

- Bạn có thể sử dụng file [no_accent_vietnamese](https://drive.google.com/file/d/1IioZsz8BTm9BN37CVL57l4--H3aKZreU/view?usp=sharing) để loại bỏ các dấu tiếng Việt có trong chuỗi.

- **Lưu ý về nộp bài**

  - Sản phẩm cần nộp của bạn sẽ gồm các tài nguyên sau:
    - Source Code sử dụng Scrapy để thu thập dữ liệu.
    - File `.json` chứa dữ liệu đã thu thập được.

- **Chuẩn bị**
  - Tạo project scrapy
    `scrapy startproject covid19ncov`
  - Đổi tên thư mục chứa project
    `move /y covid19ncov Assessment3`
  - Chuyển thư mục làm việc
    `cd Assessment3`
  - Tạo spider cho thu thập dữ liệu
    `scrapy genspider ncov`
