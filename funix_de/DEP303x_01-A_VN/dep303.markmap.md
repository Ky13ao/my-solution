# Big Data with Spark

## Lab list

- [Lab 1](#lab-1---setup-and-run-spark)
- [Lab 2](#lab2---using-rdd-exercise)
- [Lab 3](#lab3---read-write-operators-with-dataframe)
- [Lab 4](#lab-4---using-sparksql-table)
- [Lab 5](#lab-5---transformation-operators-with-dataframe)
- [Lab 6](#lab-6---aggregation--join-operators)
- [Lab 7](#lab-7---advanced-operators-with-dataframe)
- [Lab 8](#lab8---spark-streaming-exercises)
- [Lab 9](#lab9---kafka-source--join-operators-exercies)
- [Lab 10](#lab-10---windowing--aggregation-exercise)
- [Assessment 1](#assessment1---xây-dựng-hệ-thống-bigdata)
- [Lab 11](#lab11---creating-data-pipline-exercises)
- [Lab 12](#lab12---parallel-data-pipeline-exercises)
- [Lab 13](#lab13---branching-in-airflow-exercise)
- [Assessment 2](#assessment-2---thiết-lập-datapipeline-cho-dữ-liệu-lớn-từ-cloud)

## Big Data and Hadoop

### Big Data

#### Big Data concept

- Big Data là thuật ngữ
  dùng để chỉ 1 tập hợp dữ liệu rất lớn và phức tạp
  đến nỗi những công cụ, ứng dụng xử lý dữ liệu truyền thống
  không thể thu thập, quản lý và xử lý dữ liệu trong một khoản thời gian hợp lý
- Những tập hợp dữ liệu lớn này có thể bao gồm
  - các dữ liệu có cấu trúc **(structured data)**
  - các dữ liệu không cấu trúc **(unstructured data)** như video, file doc,...
  - các dữ liệu bán cấu trúc **(semi structured data)**
- Mỗi tập hợp có chút khác biệt
- Vòng đời của Big Data sẽ diễn ra như sau
  - **Business Case**
    Ở bước này, chúng ta sẽ quyết định các định dạng dữ liệu nào được thu thập trên các yêu cầu nghiệp vụ
  - **Data Collection**
    Lúc này dữ liệu sẽ được thu thập và lưu trữ phân tán thông qua HDFS
  - **Data Modelling**
    Để đảm bảo dữ liệu được lưu trữ đầy đủ, ta cần tạo ra các data model để lưu trữ và xác định mối quan hệ giữa các dữ liệu với nhau (Map Reduce và YARN)
  - **Data Processing**
    Sau khi được mô hình hóa, dữ liệu sẽ cần được xử lý để chỉ lấy các thông tin cần thiết (Spark, Pig, Hive, ...)
  - **Data Visualization**
    Dữ liệu cần được trực quan hóa thành các biểu đồ để người dùng có thể sử dụng dữ liệu cho các vấn đề nghiệp vụ
  - ![Big data life cycle](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L1_1..png?alt=media&token=b23caf48-e2b9-4e0e-a912-ca9ad5d1f4ff)
- Ngoài ra, Big Data cũng có các **đặc trưng (5V)** như sau:
  - **Volume (khối lượng)**
    Khối lượng của dữ liệu Big Data đang tăng lên mạnh mẽ từng ngày
  - **Velocity (tốc độ)**
    Với sự ra đời của các kỹ thuật, công cụ, ứng dụng lưu trữ
    nguồn dữ liệu lớn liên tục được bổ sung với tốc độ nhanh chóng
  - **Veriety (đa dạng)**
    Sự đa dạng của dữ liệu đến từ nhiều nguồn khác nhau
    như từ các thiết bị cảm biến, thiết bị di động, hay thông qua các trang mạng xã hội
  - **Veracity (tin cậy)**
    Bằng những phương tiện truyền thông xã hội bùng nổ như hiện nay
    và sự gia tăng mạnh mẽ về tương tác và chia sẻ của người dùng
    bức tranh toàn cảnh về độ chính xác cũng như tin cậy của thông tin
    ngày càng trở nên hỗn loạn và khó khăn
    Vấn đề phân tích và loại bỏ dữ liệu thiếu chính xác
    đang là một trong những vấn đề lớn của Big Data
  - **Value (giá trị)**
    Đây là đặc trưng **quan trọng nhất** bởi các thông tin đang tiềm ẩn
    trong bộ dữ liệu khổng lồ được trích xuất
    để phục vụ cho việc phân tích, dự báo
    Những thông tin này có thể được sử dụng trong rất nhiều lĩnh vực
    như kinh doanh, nghiên cứu khoa học, y học, vậy lý,...
    giúp giải quyết những vấn đề mà cuộc sống hiện đại đặt ra
- Videos:
  - [Big Data là gì?](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/24c4V/what-is-big-data)
  - [Tổng quan về Big Data](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/yqVpL/beyond-the-hype)
  - [Ảnh hưởng của Big Data](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/wLFkJ/impact-of-big-data)
  - [Nên sử dụng Big Data trong trường hợp nào?](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/570eD/big-data-use-cases)
- Ngoài ra, do dữ liệu của chúng ta sẽ được đến từ nhiều nguồn
  và đồng thời cũng sẽ ở nhiều dạng khác nhau
  Vậy nên chúng ta sẽ cần kết hợp các dữ liệu đó lại
  để đồng nhất với nhau và giúp dữ liệu giá trị hơn và liên kết hơn
  Công việc này sẽ bao gồm:
  - Làm giảm độ phức tạp của dữ liệu
  - Tăng mức độ phù hợp của dữ liệu
  - Chuyển đổi để các dữ liệu đồng nhất với nhau
  - Video: [Tích hợp dữ liệu ở các dạng khác nhau](https://www.coursera.org/learn/big-data-introduction/lecture/Ejk8J/the-key-integrating-diverse-data)

#### Ecosystems and tools for Big Data

- Chúng ta có hai cách để có thể xử lý các dữ liệu:
  - **Xử lý tuần tự (Linear processing):**
    - Các công việc xử lý dữ liệu sẽ được thực hiện tuần tự.
    - Các công việc trước cần phải hoàn thành thì mới có thể sang công việc tiếp theo
    - Nếu có lỗi xảy ra ở một bước đó thì các công việc sẽ phải
      dừng lại, hoặc chạy lại hết từ đầu sau khi xử lý các lỗi
  - **Xử lý song song (Parallel processing):**
    - Các công việc được xử lý song song, đọc lập với nhau
    - Nếu có 1 công việc bị lỗi thì cũng sẽ không ảnh hưởng
      đến các công việc còn lại và có thể dễ dàng thực hiện lại
  - ![linear & parallel processing](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L1_2..png?alt=media&token=0fdc5f0e-46e1-4adb-8637-717184fe9665)
- Có thể thấy rằng việc xử lý dữ liệu song song
  sẽ phù hợp hơn với Big Data nhờ vào một số ưu điểm sau:
  - Tiết kiệm thời gian xử lý dữ liệu
  - Tiết kiệm được các tài nguyên tính toán hơn cho các Node
  - Dễ dàng mở rộng hơn nếu dữ liệu nhiều hơn
- Với Big Data, để xử lý dữ liệu song song thì
  chúng ta sẽ chia hệ thống thành nhiều máy **(Cluster)** khác nhau
  mỗi máy có thể đảm nhiệm vai trò lưu trữ, tính toán hoặc cả hai
  Sau đó, chúng ta cần xử lý dữ liệu thì sẽ chạy song song với các Cluster khác nhau
  Kiến trúc này giúp cho dữ liệu có thể được xử lý song song và độc lập với nhau
- ![parallel processing clusters](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L1_3..png?alt=media&token=1fcea8af-5bd7-48c2-8db1-6b1da86e7fa6)
- Ngoài ra, kiến trúc này cũng giúp dễ dàng mở rộng theo chiều ngang
  tức là khi ta cần một tài nguyên lớn hơn để tính toán thì chỉ việc tạo thêm nhiều Cluster
  chứ không cần phải nâng cấp cấu hình cho các Cluster cũ
  Đồng thời cũng giúp tính bảo toàn tính toàn vẹn dữ liệu thông qua cơ chế **Fault tolerance**
  dữ liệu sẽ được tạo thành nhiều bản sao ở các Cluster khác nhau
  khi 1 Cluster gặp sự cố gây ra mất mát dữ liệu thì ta có thể dễ dàng backup lại
  Ta sẽ được tìm hiểu kỹ hơn ở bài về Hadoop HDFS
- [parallel processing clusters problem](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L1_4..png?alt=media&token=544bc364-9996-4696-ae90-fd241d154c2e)
- Video: [Xử lý dữ liệu song song và Scaling](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/ix1eD/parallel-processing-scaling-and-data-parallelism)

- Các công cụ trong hệ sinh thái Big Data sẽ được chia thành các công cụ như sau:
  - **Data Technologies**
    Sử dụng để xử lý, chia sẻ các dữ liệu ở định dạng khác nhau và giúp dữ liệu phân tán
  - **Analytics và Visualization**
    Giúp trực quan hóa và phân tích dữ liệu
  - **Business Intelligence**
    Giúp chuyển hóa các dữ liệu để dễ dàng truy cập, phục vụ cho các vấn đề nghiệp vụ
  - **Cloud Provider**
    Cung cấp các dịch vụ dưới dạng Cloud để dễ dàng mở rộng hơn
  - **NoSQL Database**
    Cơ sở dữ liệu NoSQL để lưu trữ dữ liệu
  - **Programming Tools**
    Các công cụ để xử lý các công việc đòi hỏi logic phức tạp trong vòng đời của Big Data
- Và đồng thời sẽ có những công cụ mã nguồn mở giúp chúng ta thao tác với Big Data dễ dàng hơn
- Video: [Hệ sinh thái và các công cụ về Big Data](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/WyhaU/big-data-tools-and-ecosystem)
- Video: [Các công cụ mã nguồn mở của Big Data](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/Fk5f4/open-source-and-big-data)

### Hadoop

#### Hadoop concepts

- Hadoop là một dạng Apache Framework
- Apache Hadoop là một mã nguồn mở cho phép sử dụng các distributed processing (ứng dụng phân tán) để quản lý và lưu trữ những tệp dữ liệu lớn
- Hadoop áp dụng mô hình MapReduce trong hoạt động xử lý Big Data
- Hadoop có những ưu điểm sau:
  - Cho phép ng dùng nhanh chóng viết và kiểm tra các hệ thống phân tán
    Đây là cách hiệu quả cho phép phân phối dữ liệu và công việc xuyên suốt các Cluster nhờ vào cơ chế xử lý song song của các lỗi CPU
  - Hệ thống Hadoop thiết kế sao cho các lỗi xảy ra trong hệ thống
    được xử lý tự động, không ảnh hưởng đến các ứng dụng phía trên
  - Có thể phát triển lên nhiều server với cấu trúc master-slave
    để đảm bảo thực các công việc linh hoạt và không bị ngắt quãng
    do chia nhỏ công việc cho các server slave được điều khiển bởi server master
  - Có thể tương thích trên mọi nền tảng như Window, Linux, MacOS do được tạo từ Java
- Tuy nhiên Hadoop vẫn có những khuyết điểm như:
  - thiết bị lưu trữ tốc độ chậm
  - máy tính thiếu tin cậy
  - lập trình song song phân tán không dễ dàng
- Video: [Giới thiệu về Hadoop](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/1sOjx/introduction-to-hadoop)
- Hadoop gồm 4 thành phần chính:
  - **Hadoop Common**
    Đây là các thư viện và tiện ích cần thiết của Java để các module khác sử dụng.
    Những thư viện này cung cấp hệ thống file và lớp OS trừu tượng,
    đồng thời chứa các mã lệnh Java để khởi động Hadoop.
  - **Hadoop YARN**
    Đây là framework để quản lý tiến trình và tài nguyên của các cluster.
  - **Hadoop Distributed File System (HDFS)**
    Đây là hệ thống file phân tán cung cấp truy cập thông lượng cao
    cho ứng dụng khai thác dữ liệu.
  - **Hadoop MapReduce**
    Đây là hệ thống dựa trên YARN dùng để xử lý song song các tập dữ liệu lớn.
- Hiện nay Hadoop đang ngày càng được mở rộng cũng như
  được nhiều framework khác hỗ trợ như Hive, Hbase, Pig.
  Tùy vào mục đích sử dụng mà ta sẽ áp dụng framework phù hợp
  để nâng cao hiệu quả xử lý dữ liệu của Hadoop.

- Video: [Hệ sinh thái Hadoop](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/g7y7n/hadoop-ecosystem)

#### HDFS

- Một trong những vấn đề lớn nhất của các hệ thống phân tích Big Data là quá tải
  Không phải hệ thống nào cũng đủ khỏe để có thể tiếp nhận một lượng thông tin khổng lồ như vậy
  Chính vì thế, nhiệm vụ của **Hadoop Distributed File System** là phân tán cung cấp truy cập thông lượng cao giúp cho ứng dụng chủ
  Cụ thể, khi HDFS nhận được một tệp tin, nó sẽ tự động chia file đó ra thành nhiều phần nhỏ
  Các mảnh nhỏ này được nhân lên nhiều lần và chia ra lưu trữ tại các máy chủ khác nhau
  để phân tán sức nặng mà dữ liệu tạo nên đồng thời cũng đảm bảo được tính toàn vẹn dữ liệu
- HDFS sử dụng các cấu trúc **master node** và **worker/slave node**
  Trong khi master node hay còn gọi là **Name Node** quản lý các file metadata
  thì **worker/slave node** chịu trách nhiệm lưu trữ dữ liệu
  Chính vì thế nên worker/slave node cũng được gọi là data node
  Một **Data node** sẽ chứa nhiều khối được phân nhỏ của tệp tin lớn ban đầu
  Dựa theo chỉ thị từ Master node, các Data node này sẽ trực tiếp điều hành hoạt động thêm, bớt những khối nhỏ của tệp tin
- ![HDFS architecture](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L2_1..png?alt=media&token=137107da-2f66-4c9d-9a2f-944266381b58)
- HDFS chỉ cung cấp 2 cơ chế truy cập dữ liệu là READ và WRITE
  - **READ**
    - Client sẽ gửi yêu cầu đến Name Node để biết được dữ liệu đang nằm ở Data Node nào.
      Sau đó sẽ trực tiếp đọc dữ liệu từ Data Node đó
  - **WRITE**
    - Name Node sẽ cần đảm bảo file đó chưa tồn tại,
      nếu đã tồn tại thì sẽ không báo lỗi.
    - Nếu như file chưa tồn tại vì client sẽ được cấp quyền để truy cập vào Data node để ghi dữ liệu
- Nguyên lý cốt lõi của HDFS như sau:
  - Chỉ ghi thêm (Append) giúp giảm chi phí điều khiển tương tranh
  - Phân tán dữ liệu
  - Nhân bản dữ liệu để bảo toàn tính toàn vẹn dữ liệu
  - Có cơ chế chịu lỗi:
    - Các Data Node có thể được backup nhờ sử dụng cơ chế nhân bản dữ liệu
    - Còn các Name Node cũng sẽ có Secondary Name Node để có thể thay thế nếu có lỗi
- Video: [HDFS](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/sfnQg/hdfs)

#### Map Reduce

- **Hadoop MapReduce** cho phép phân tán dữ liệu từ một máy chủ sang nhiều máy con
  Mỗi máy con này sẽ nhận một phần dữ liệu khác nhau và tiến hành xử lý cùng lúc
  Sau đó chúng sẽ báo lại kết quả lên máy chủ
  Máy chủ tổng hợp thông tin lại rồi trích xuất theo như yêu cầu của người dùng
- Các thực thi theo mô hình như vậy giúp tiết kiệm nhiều thời gian xử lý
  và cũng giảm gánh nặng lên hệ thống
- Chức năng của máy chủ là
  - quản lý tài nguyên
  - đưa ra thông báo
  - lịch trình hoạt động cho các Cluster
- Các cluster sẽ thực thi theo kế hoạch được định sẵn
  và gửi báo cáo dữ liệu lại cho máy chủ
  Tuy nhiên đây cũng là điểm yếu của hệ thống này
  Nếu máy chủ bị lỗi thì toàn bộ quá trình sẽ bị ngừng lại hoàn toàn
- Một chương trình Map Reduce có thể được lập trình với nhiều ngôn ngữ khác nhau
  ( Java, C+++, Python, R, Ruby)
  bạn sẽ cần phải cung cấp các hàm Map và Reduce để xác định các công việc phải làm
  hai hàm này được thực thi bởi các tiến trình Mapper và Reducer tương ứng.
- Trong chương trình MapReduce
  - dữ liệu được nhìn nhận như là các cặp khóa - giá trị (key-value)
  - các hàm Map và Reduce nhận đầu vào và trả về đầu ra các cặp (key-value)
- ![MapReduce flow](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L2_2..png?alt=media&token=bd81ffed-555e-4199-8dc7-db177d302175)
- Cơ chế hoạt động của MapReduce sẽ gồm các bước như sau
  - **Input** -> nạp dữ liệu cần xử lý
  - **Split** -> hệ thống sẽ chia dữ liệu thành các mảng cho từng máy
  - **Map** -> thực hiện song song hàm Map cho các mảnh dữ liệu đã chia trước đó
  - **Shuffle** -> sắp xếp và phân chia dữ liệu từ Map đưa vào các Reduce
  - **Reduce** -> thực hiện hàm Reduce cho các dữ liệu đã chia
  - **Output** -> gộp các dữ liệu đầu ra từ bước Reduce để trả về kết quả cuối cùng
- ![How MapReduce works](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L2_3.png?alt=media&token=91fe892c-b905-432e-b4e7-7b0ebdd38784)
- Video: [Map Reduce](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/nb5Lf/intro-to-mapreduce)

#### Others in Hadoop

##### YARN

- YARN : Yet Another Resource Negotiator
- YARN đóng vai trò cấp phát lượng tài nguyên phù hợp cho các ứng dụng khi có yêu cầu
- do Nodes có tài nguyên là
  bộ nhớ và CPU cores
  vậy nên các có cơ chế cấp phát hợp lý
- YARN cung cấp daemons và APIs cần thiết cho việc phát triển ứng dụng phân tán
  đồng thời xử lý và lập lịch sử dụng tài nguyên tính toán (CPU hay memory)
  cũng như giám sát quá trình thực thi các ứng dụng đó
- YARN tổng quát hơn MapReduce thể hệ đầu tiên
  (JobTracker/ TaskTracker)
- Video: [YARN](https://www.coursera.org/learn/big-data-introduction/lecture/Rn7sf/yarn-a-resource-manager-for-hadoop)

##### Hive

- Hive là một nền tảng được sử dụng để phát triển
  các tập lệnh gần giống SQL (HiveSQL)
  để thực hiện các hoạt động MapReduce
  từ đó giúp giảm thời gian phát triển mà vẫn có thể sử dụng được MapReduce
- Trình biên dịch Hive chạy trên các máy client
  giúp chuyển HiveQL script thành MapReduce jobs và đệ trình các công việc này lên cụm tính toán
- Video: [Hive](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/V8YLj/hive)

##### HBase

- HBase là một CSDL cột mở rộng phân tán, lưu trữ trên HDFS
- được xem như là hệ quản trị CSDL của Hadoop
- Dữ liệu được tổ chức về mặt logic là các bảng
  bao gồm rất nhiều dòng và cột
- Ưu điểm
  - Có tính khả mở cao, đáp ứng băng thông ghi dữ liệu tốc độ cao
  - Hỗ trợ hàng trăm ngàn thao tác INSERT mỗi giây (s)
- Nhược điểm

  - Do là NoSQL nên không có ngôn ngữ truy vấn mức cao như SQL và phải sử dụng API để scan/put/get dữ liệu theo khóa

- Video: [HBase](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/pI5Tx/hbase)

### Monitor and process Big Data

#### Big Data system management

##### Data Ingestion - bổ sung dữ liệu

- Quy trình bổ sung dữ liệu cho hệ thống nắm vai trò rất quan trọng
  và cũng tiêu tốn khá nhiều tài nguyên
- Các câu hỏi giúp xác định được quy trình bổ sung dữ liệu phù hợp:
  - Có bao nhiêu Data Source?
  - Độ lớn của dữ liệu?
  - Số Data Source có tăng lên nữa không?
  - Thời gian sẽ cần bổ sung thêm dữ liệu?
  - Bạn sẽ làm gì với các dữ liệu không tốt?
  - Bạn sẽ làm gì nếu lượng dữ liệu quá ít hoặc quá nhiều?
- Video: [Data Ingestion](https://www.coursera.org/learn/big-data-management/lecture/Lnlwf/data-ingestion)

##### Data storage - lưu trữ dữ liệu

- Tương tự với việc bổ sung dữ liệu thì lưu trữ dữ liệu cũng có vai trò quan trọng
- Sẽ có 2 vấn đề ở phần này
  - Cần phân bổ lưu trữ dữ liệu như thế nào
    Bao nhiêu dữ liệu cần lưu trữ và sẽ lưu trữ theo cách nào
    (truy cập trực tiếp hay truy cập qua Internet)
  - Yêu cầu về tốc độ đọc/ ghi dữ liệu như thế nào
- Sau khi có đáp án cho các câu hỏi trên
  thì ta có thể chọn được 1 cách lưu trữ dữ liệu để đáp ứng các yêu cầu đó
- Video: [Data Storage](https://www.coursera.org/learn/big-data-management/lecture/RplBY/data-storage)

##### Data quality - Chất lượng dữ liệu

- có 3 lý do chính mà bạn cần đảm bảo dữ liệu của bạn chất lượng
  - chúng ta sẽ trích xuất thông tin hữu ích từ dữ liệu
    vậy nên nếu ban đầu dữ liệu đã không chất lượng
    thì có thể làm ảnh hưởng đến các phân tích nghiệp vụ sau này
  - Dữ liệu liên quan đến các ngành như y tế, ngân hàng, ...
    nếu có sai sót thì có thể liên quan đến cả các vấn đề pháp lý
  - Nếu dữ liệu chúng ta cung cấp cho khách hàng
    hoặc các bên liên quan không tốt thì có thể làm giảm uy tín
- Video: [Data quality](https://www.coursera.org/learn/big-data-management/lecture/xdrBU/data-quality)

##### Data operations - Các thao tác làm việc với dữ liệu

- Để phù hợp với một yêu cầu nào đó,
  ta cần sử dụng các thao tác để làm việc với dữ liệu
- Các thao tác có thể được chia làm thành 2 loại
  - Thao tác trên 1 data item
  - Thao tác trên 1 tập hợp các dữ liệu
    Thao tác này còn có thể được chia nhỏ hơn thành các loại như sau:
    - Thao tác để chọn một phần dữ liệu (lấy subset)
    - Thao tác để kết hợp các tập hợp dữ liệu (merge)
    - Thao tác tính toán trên tập dữ liệu (đếm dữ liệu,..)
- Video: [Data operations](https://www.coursera.org/learn/big-data-management/lecture/3iZzB/data-operations)

##### Khả năng mở rộng và bảo mật dữ liệu

- Chúng ta có hai cách để mở rộng cho môi trường Big Data
  - **Mở rộng theo chiều dọc**
    - Nâng cấp cấu hình phần cứng cho các máy trên hệ thống
    - Cách này giúp các thao tác được thực hiện tốt hơn
      nhưng đồng thời cũng rất khó triển khai và maintain
  - **Mở rộng theo chiều ngang**
    - Bổ sung thêm các máy mới vào hệ thống
    - Cách này thường được dùng với các hệ thống xử lý phân tán
      tuy có thể hiệu suất sẽ kém hơn chút nhưng lại dễ dàng để triển khai và maintain
      -> Các môi trường Big Data thường sử dụng mở rộng theo chiều ngang
- Ngoài ra, bảo mật cũng là 1 công việc quan trọng
  Một số lưu ý về vấn đề bảo mật
  - Tăng số lượng máy trong hệ thống
    đồng nghĩa với việc quản lý bảo mật khó khăn hơn
  - Các dữ liệu được vận chuyển qua lại giữa các máy
    cũng cần phải đảm bảo tính bảo mật
  - Việc mã hóa và giải mã sẽ tốn nhiều tài nguyên
    nên ta cần phải sử dụng hợp lý
- Video: [Data Scalability & Security](https://www.coursera.org/learn/big-data-management/lecture/JEcdQ/data-scalability-and-security)

##### Tài liệu tham khảo

- Bạn có thể tham khảo thêm các tài liệu dưới đây về việc quản lý Big Data
- Tham khảo: [Energy Data Management Challenges at ConEd](https://www.coursera.org/learn/big-data-management/lecture/r7dn2/energy-data-management-challenges-at-coned)
- Tham khảo: [Gaming Industry Data Management: Q&A with Apmetrix CTO Mark Caldwell](https://www.coursera.org/learn/big-data-management/lecture/uDoPs/gaming-industry-data-management-q-a-with-apmetrix-cto-mark-caldwell)
- Tham khảo: [Flight Data Management at FlightStats: A Lecture by CTO Chad Berkley](https://www.coursera.org/learn/big-data-management/lecture/ITqCN/flight-data-management-at-flightstats-a-lecture-by-cto-chad-berkley)

#### Big Data processing

##### Big Data Pipeline

- Hầu hết các ứng dụng BigData được cấu tạo bởi nhiều thao tác kết hợp lại với nhau
  ta gọi đó là Pipeline
- MapReduce cũng có thể được gọi là 1 **Big Data Pipelines** do gồm các thao tác như Input, Split, Map, Shuffle, Reduce và Output
- Video: [Big Data Processing Pipelines](https://www.coursera.org/learn/big-data-integration-processing/lecture/c4Wyd/big-data-processing-pipelines)

##### Một số thao tác thường dùng trong Big Data Pipelines

- **Map**
  Áp dụng một thao tác nào đó trên toàn bộ phần tử của dữ liệu
- **Reduce**
  Kết hợp các dữ liệu theo các giá trị **key**, đầu vào của thao tác này thường là các dữ liệu có dạng **key-value**
- **Cross/Catesian**
  Áp dụng một thao tác nào đó trên từng cặp dữ liệu từ hai Sets
- **Match/Join**
  Đầu vào của thao tác này thường là các tập dữ liệu có dạng **key-value**
  sau đó áp dụng thao tác nào đó lên những cặp dữ liệu cùng giá trị **key** từ 2 tập đầu vào
- **Co-Group**
  Nhóm các phần tử với nhau
- **Filter**
  Lọc các phần tử thỏa mãn điều kiện
- Video: [Một số thao tác trong Big Data Processing Pipelines](https://www.coursera.org/learn/big-data-integration-processing/lecture/WZPCd/some-high-level-processing-operations-in-big-data-pipelines)

##### Aggregation trong Big Data Pipelines

- **GROUP BY** - chia nhóm các dữ liệu dựa trên một điều kiện nào đó
- Các thao tác tính toán như: **AVERAGE, MIN, MAX, STANDARD DEVIATION**
- Đồng thời, bạn cũng có thể kết hợp tuần tự các Aggregation với nhau cho các thao tác phức tạp hơn
- Video: [Các toán tử Aggregation trong Big Data Processing Pipelines](https://www.coursera.org/learn/big-data-integration-processing/lecture/VDBgw/aggregation-operations-in-big-data-pipelines)

##### Tổng quan Big Data processing

- 1 Hệ thống Big Data Processing sẽ có các tầng như sau:
  - **Data Management and Store**
    Tầng này sẽ chứa các thành phần giúp quản lý và lưu trữ các dữ liệu như HDFS
  - **Data Integration and Processing**
    Tầng này chứa các thành phần để dữ liệu được truy xuất, tích hợp và phân tích
    như YARN, Map Reduce,....
  - **Coordination and Workflow management**
    Tầng này chứa các thành phần để quản lý
    điều phối công việc cho các công cụ của 2 hai tầng còn lại
- Video: [Tổng quan về các hệ thống Big Data Processing](https://www.coursera.org/learn/big-data-integration-processing/lecture/Z1jrr/overview-of-big-data-processing-systems)

## Big Data with Spark

### Spark

- **Apache Spark**
  - là 1 framework mã nguồn mở
  - cho phép bạn xây dựng nhưng mô hình dự đoán nhanh chóng
    với khả năng thực hiện tính toán cùng lúc trên một nhóm các máy tính
    hay trên toàn bộ các tập dữ liệu
    mà không cần thiết phải trích xuất các mẫu tính toán thử nghiệm
  - tốc độ xử lý dữ liệu có được là do khả năng được thực hiện các tính toán
    trên nhiều máy tính khác nhau trên cùng 1 lúc tại bộ nhớ (in-memories)
    hay hoàn toàn trên RAM
- **Spark** được ưa chuộng hơn **Hadoop** trên một số ứng dụng nhờ tốc độ của mình
  (chính xác hơn là cấu trúc tính toán MapReduce trên Hadoop)
- Ưu điểm:
  thay vì lưu dữ liệu và các kết quả trung gian trong quá trình tính toán
  dưới dạng của các file hệ thống như Hadoop Map-Reduce nó lưu
  trong bộ nhớ của các Node
- Nhược điểm:
  không có hệ thống tập tin phân tán vì người ta thường chạy nó trên nền của Hadoop
- Spark cũng rất dễ dàng sử dụng từ Python, Java hoặc Scala
- Spark sẽ gồm các thành phần chính như sau

  - **Spark Core**
    - Được xem là nền tảng và điều kiện cho sự vận hành của các thành phần còn lại
    - Thành phần này đảm nhận vai trò thực hiện các công việc tính toán, xử lý trong bộ nhớ
      và tham chiếu các dữ liệu được lưu trữ bên ngoài
  - **Spark SQL**
    - Thành phần này giúp thực hiện các thao tác trên các Dataframe
      bằng các ngôn ngữ như Java, Scala hay Python thông qua sự hỗ trợ của ngôn ngữ SQL
    - Cung cấp SchemaRDD với mục đích hỗ trợ cho các kiểu **structured data** và **semi-structured data**.
  - **Spark Streaming**
    - Mục đích sử dụng cho thành phần này chính là coi stream là các mini batches
      và thực hiện các kỹ thuật RDD transformation với các dữ liệu này để phân tích stream
      Điều này giúp việc xử lý stream và phát triển lambda architecture
      trở nên dễ dàng bằng cách tận dụng lại các đoạn code được viết để xử lý batch
  - **MLlib**
    - Là một nền tảng học máy
    - Spark MLlib nhanh hơn gấp 9 lần so với phiên bản chạy trên Hadoop
      (theo so sánh từ benchmark) nhờ kiến trúc phân tán dựa trên bộ nhớ
  - **GraphX**
    - Đây là nền tảng xử lý các đồ thị dựa trên Spark
    - Nó cung cấp các API và được sử dụng để diễn tả tất cả các tính toán có trong đồ thị

- Video: [Khái niệm về Apache Spark](https://funix.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/3708614#questions)

- Tham khảo: [Spark 3 có gì mới?](https://funix.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/17919510#questions)

### Spark Architecture

- Kiến trúc của Spark bao gồm
  - **Driver (trình điều khiển)**
  - **Executor Processes (trình thực thi)**
- _Driver_ tạo ra **_Spark Job_** và **_Spark Context_**
  chia các Job thành các Task có thể chạy song song trong các trình thực thi trên Cluster
  mỗi ứng dụng sẽ có 1 _Spark Context_ điều phối Executor
- **Spark Job**
  là các công việc tính toán mà ứng dụng cần thực hiện
  và có thể được thực thi song song
- **Spark Task**
  thực hiện các Spark Job trên các phân vùng dữ liệu (Partitions) khác nhau
  và cũng có thể được thực thi song song
- ![Apache Spark Architecture](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L4_1.png?alt=media&token=9dce6761-35ca-447c-976f-25454eb47a36)
- **Stages**
  - là một tập hợp các Task được phân tách bằng một lần _Shuffles_ dữ liệu
    - việc Shuffles rất tốn kém
      vì chúng yêu cầu tuần tự hóa dữ liệu, đĩa và mạng I/O
    - Shuffles sẽ cần thiết
      nếu như các thao tác cần dữ liệu từ các phân vùng (Partitions) khác
      ví dụ: ![Shuffle example](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L4_2.png?alt=media&token=734cfe98-f5a4-421a-af8d-c1bd3519476f)
- Driver (chương trình điều khiển) có thể được chạy ở 2 chế độ sau
  - **Client Mode**
    Trình gửi ứng dụng (Application Submitter)
    chẳng hạn như thiết bị đầu cuối của máy người dùng khởi chạy trình điều khiển bên ngoài Cluster
  - **Cluster Mode**
    Chương trình điều khiển được gửi đến và chạy trên một Worker Node có sẵn bên trong Cluster
  - ![driver running modes](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L4_3.png?alt=media&token=613e7952-b1b7-4563-b287-e4f3913f3d7e)
- Video: [Kiến trúc của Apache Spark](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/7D9xA/apache-spark-architecture)
- Tham khảo: [Sự khác biệt giữa SparkSession và SparkContext](https://sparkbyexamples.com/spark/sparksession-vs-sparkcontext/)

#### Cách cài đặt và chạy chương trình Spark

- Cách 1: Cài đặt trực tiếp trên máy tính
  - Video: [Cài đặt môi trường để sử dụng Spark](https://funix.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/5586888#questions)
  - Tham khảo: [Cài đặt Pyspark qua Pip hoặc Conda](https://spark.apache.org/docs/3.1.1/api/python/getting_started/install.html)
- Cách 2: Sử dụng trên Google Colab
  - Google Colab là một dạng Jupyter Notebook tùy biến cho phép thực thi Python
    trên nền tảng đám mây, được cung cấp Google
  - Sử dụng Google Colab có những lợi ích ưu việt như:
    - sẵn sàng chạy Python ở bất kỳ thiết bị nào có kết nối internet mà ko cần cài đặt
    - chia sẻ và làm việc nhóm dễ dàng, sử dụng miễn phí GPU cho các dự án về AI
- Trong bài Lab này ta dùng Google collab
  - Tham khảo: [Hướng dẫn cài đặt và làm quen Google Colab cơ bản](https://trituenhantao.io/lap-trinh/lam-quen-voi-google-colab/)
  - Tham khảo: [Hướng dẫn sử dụng Google Colab chi tiết](https://thinhvu.com/2021/07/29/huong-dan-su-dung-google-colab-tutorial-101/)
  - Tham khảo: [Cài đặt và sử dụng PySpark trên Google Colab](https://www.analyticsvidhya.com/blog/2020/11/a-must-read-guide-on-how-to-work-with-pyspark-on-google-colab-for-data-scientists/)
- Sau khi đã cài đặt thành công Spark, ta sẽ có 2 cách để chạy được một Spark Job
  - **Spark Shell**
    - là một trình tương tác giúp ta viết và chạy trực tiếp các câu lệnh PySpark
    - là một công cụ khá hữu ích để làm quen với các Spark API cũng như thực hiện các thao tác phân tích dữ liệu
  - **spark-submit**
    - như tên gọi thì bạn sẽ submit một Spark Job và thực hiện Job đó
    - công việc của các Job này sẽ được khai báo bằng các đoạn code Python
- Hoặc nếu ta sử dụng một thư viện là pyspark
  ta có thể chạy 1 SparkJob bằng cách gọi `python <file-name>.py`
  - Video: [Thực hành: Cài đặt Dataset](https://funix.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/3702584#questions)
  - Video: [Thực hành: Chạy ứng dụng Spark đầu tiên](https://funix.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/3700612#questions)

### Lab 1 - Setup and run Spark

- [Lab1: Cài đặt và sử dụng Spark](https://colab.research.google.com/drive/1JKmBBvT7hv0civmZU__G923H5wKAiJN5?usp=sharing)
- [Hướng dẫn](https://docs.google.com/document/d/19aXDWH86NaVJ-sAWm9YERHN4KT2Pqe70g162_NITXwc/edit?usp=sharing)
- [Bài làm](https://colab.research.google.com/drive/1BRAIycbiRyKvSIf1eiiaM2GiJqxpjTlk?authuser=1#scrollTo=e_fAhSKr9uhE)

### Spark RDD

#### Resilient Distributed Datasets

- RDD là một cấu trúc cơ bản của Spark
- Là một tập hợp bất biến phân tán của một đối tượng
- Mỗi dataset trong RDD được chia ra thành nhiều phân vùng logical
  có thể được tính toán trên các node khác nhau của một cụm máy chủ (cluster)

- RDD có thể chưa bất kỳ kiểu dữ liệu nào của Python, Java hoặc đối tượng Scala
  bao gồm các kiểu dữ liệu do người dùng định nghĩa
- Thông thường RDD chỉ cho phép đọc, phân mục tập hợp của các bản ghi
- RDDs có thể được tạo ra qua điều khiển xác định trên dữ liệu trong bộ nhớ hoặc RDDs
- RDD là một tập hợp có khả năng chịu lỗi mỗi thành phần có thể được tính toán song song
- Chúng ta sẽ có các thao tác có thế được sử dụng trong RDD
  các thao tác này được chia thành 2 loại:
  - **Transformation**
    - Là các thao tác để biến đổi RDD hiện tại thành 1 RDD mới
      các thao tác này cũng có cơ chế **Lazy evaluation**
    - Khi bạn sử dụng các thao tác Transformation
      thì hệ thống sẽ không thực hiện tính toán ngay lập tức
      các thao tác này chỉ được thực thi khi có 1 _Action_ được gọi
  - **Action**
    - Là các thao tác trả về kết quả từ RDD ngay lập tức
- Quản lý các thao tác trong RDD:
  - Chúng ta sẽ sử dụng **DAG (Directed Acyclic Graph)** trong Spark
    Đây là cấu trúc điều phối các yêu cầu tính toán trong mạng các máy tính (cluster)
    giúp lập trình ứng dụng với Spark trở nên đơn giản hơn
  - Thay vì phải liên tục lưu và trải dữ liệu cho các thao tác Map-Reduce
    DAG cho phép các bước tính toán phức tập được thực hiện một cách tuần tự
    Cơ chế hoạt động của DAG sẽ như sau
  - Spark sẽ tạo 1 DAG mới khi tạo mới 1 RDD
  - Khi có 1 thao tác Transformation, DAG sẽ được cập nhật và lúc này DAG sẽ được trỏ tới RDD mới
  - Khi có 1 Action được gọi, Driver sẽ tiến hành các thao tác tính toán đã được lưu trong DAG và trả về kết quả
- Video: [Giới thiệu về RDD](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/Z6cIK/rdds-in-parallel-programming-and-spark)

#### Transformations and Actions trong RDD

##### Transformations

- `dictinct`
  loại bỏ trùng lắp trong RDD
- `filter`
  tương đương với việc sử dụng where trong SQL - các record trong RDD thỏa điều kiện
  có thể cung cấp một hàm phức tạp sử dụng để filter các record cần thiết
  như trong Python, ta có thể sử dụng hàm lambda để truyền vào filter
- `map`
  thực hiện một công việc nào đó trên toàn bộ RDD
  trong Python sử dụng lambda với từng phẩn tử để truyền vào map
- `flatMap`
  cung cấp 1 hàm đơn giản hơn hàm map
  yêu cầu output của map phải là 1 structure có thể lặp và mở rộng được
- `sortBy`
  mô tả một hàm để trích xuất dữ liệu từ các object của RDD và thực hiện sort được từ đó
- `randomSplit`
  nhận một mảng trọng số và tạo một random seed
  tách các RDD thành một mảng các RDD do số lượng chia theo trọng số
- `reduceByKey`
  gộp các giá trị theo các key giống nhau
- `groupByKey`
  nhóm các phần tử có key giống nhau
- `sortByKey`
  sắp xếp các dữ liệu của RDD dựa trên các key
- `keys()` hoặc `values()`
  tạo 1 RDD chỉ gồm các key hoặc value
- ví dụ và tài liệu tham khảo
  - Video: [Các hàm xử lý Key/Value trong RDD](https://funix.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/3710440#questions)
  - Tham khảo: [Thực hành: Average Friends by Age](https://funix.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/3710452#questions)
  - Video: [Lọc các dữ liệu trong RDD](https://funix.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/3719528#questions)
  - Tham khảo: [Thực hành: Minimum Temperature](https://funix.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/3719534#questions)
  - Video: [flatMap() trong RDD](https://funix.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/3723874#questions)

##### Actions

- `reduce`
  thực hiện hàm reduce trên RDD để thu về 1 giá trị duy nhất
- `count`
  đếm số dòng trong RDD
- `countByValue`
  đếm số giá trị của RDD chỉ sử dụng nếu map kết quả nhỏ
  vì tất cả dữ liệu sẽ được load lên memory của driver để tính toán
  chỉ nên sử dụng trong tình huống dòng nhỏ và số lượng item khác cũng nhỏ
- `max()` và `min()`
  lần lượt lấy giá trị lớn nhất và nhỏ nhất của dataset
- `collect`
  trả về giá trị của RDD
- tài liệu tham khảo:
  - Video: [Sử dụng Regex cho bài toán Word Count](https://funix.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/3723878#questions)
  - Video: [Sắp xếp lại các dữ liệu từ bài toán Word Count](https://funix.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/3723880#overview)
  - Tham khảo: [Các thao tác khác trong RDD.](https://spark.apache.org/docs/latest/api/python/reference/pyspark.html)

### Lab2 - Using RDD Exercise

- [Lab 2.1: Average Friends by Age](https://colab.research.google.com/drive/1pXHwWFOQmh_am6PX9UibL1wA9PlsrU-j?usp=sharing)
- [Lab 2.2: Minimum Temperature by Location](https://colab.research.google.com/drive/1JseilAKLLpzel8ix4yXJBsLKR-dYuIxa?usp=sharing)
- [Hướng dẫn cập nhật Spark](https://docs.google.com/document/d/19aXDWH86NaVJ-sAWm9YERHN4KT2Pqe70g162_NITXwc/edit?usp=sharing)

### SparkSQL, Data-frames, Datasets

#### Data-frames, Datasets

- Dataframe và Datasets là 2 khái niệm rất quan trọng trong SparkSQL
  Spark SQL là 1 trong những thành phần chính của Spark
- **DataFrame**
  - là 1 API bậc cao hơn RDD được Spark giới thiệu vào năm 2013 (từ Apache Spark 1.3)
  - tương tự RDD, dữ liệu trong DataFrame cũng được quản lý theo kiểu phân tán
    và không thể thay đổi (immutable distributed).
  - tuy nhiên dữ liệu trong DataFrame được sắp xếp theo các cột,
    tương tự như trong các CSDL
  - DataFrame được phát triển để giúp người dùng có thể dễ dàng thực hiện được
    các thao tác xử lý dữ liệu cũng như làm tăng đáng kể hiệu quả xử lý của hệ thống
  - Ta có thể đọc, ghi dữ liệu với Dataframe ở các dạng file như JSON, CSV hoặc Hive, ...
  - Trong việc xử lý dữ liệu chung ta cũng có thể sử dụng các câu lệnh SQL
    để truy vấn dữ liệu nhanh hơn cũng như dễ dàng hơn các truy vấn phức tạp
    ![dataframe spark sql](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L6_1.png?alt=media&token=eaf3ce5a-1dfc-4df7-adea-3b520783e633)
  - Hoặc sử dụng các hàm được xây dựng sẵn trong Dataframe API
    Tuy nhiên, ở bước cuối cùng thì các thuật toán này vẫn được chạy trên RDD
    mặc dù người dùng chỉ tương tác với DataFrame
    ![dataframeAPI spark sql](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L6_2.png?alt=media&token=85f40fda-d2ec-418e-9c23-8e9831f17f1e)
- **Datasets**
  - Lên đến Spark 2.0 thì Data Frame và Dataset được hợp nhất thành 1
    nên ở môn học này chúng ta sẽ thống nhất chỉ sử dụng Dataset
- Video: [Giới thiệu về SparkSQL](https://funix.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/5586908#overview)

#### Data Sources for Big Data

- Khi hoạt động, _Data Processing Engine_ như Spark sẽ cần đọc dữ liệu từ 1 Data Source nào đó
  và cũng sẽ cần lưu dữ liệu sau khi được xử lý vào một Data Sink nào đó
  Các nguồn dữ liệu này có thể được chia ra làm hai loại

  - **External**
    - là các nguồn dữ liệu nằm ngoài hệ thống BigData
    - ví dụ như một Database từ hệ thống khác, hoặc là các file dữ liệu từ hệ thống
    - chúng ta sẽ có 1 số loại Extenal Data Source như sau
      - JDBC Datasource: SQL Server, Oracle, PostgresSQL, ...
      - NoSQL Data System: MongoDB, Cassandra, ...
      - Cloud Data Warehouse
      - Stream Integrators: Kafka,...
    - Để tiếp cận ta thường có 2 cách:
      - Lấy dữ liệu từ Source và lưu lại ở hệ thống BigData, sau đó mới bắt đầu xử lý
        Cách này sẽ phù hợp với các trường hợp Batch processing
        do có thể đảm bảo về các yếu tố như hiệu suất, tính bảo mật, ...
      - Truy cập trực tiếp Datasource, sau đó lấy và xử lý dữ liệu
        Cách này phù hợp với các trường hợp Stream Processing
  - **Internal**
    - Ngược lại với External, đây là nguồn dữ liệu trực tiếp bên trong hệ thống BigData
      như **HDFS**, **AWS S3**, ...
      và để lấy dữ liệu thì bạn sẽ truy cập trực tiếp vào dữ liệu

- Video: [Nguồn dữ liệu cho Big Data](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20434107#overview)

#### Read & Write data

##### DataFrameReader API

- Để đọc dữ liệu từ các file, Spark cung cấp DataFrameReader API
- ![ví dụ](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L6_3.png?alt=media&token=81676d2c-178a-4561-8290-abd66b042a01)
- ta cần cung cấp một số thông tin cơ bản để thực hiện việc đọc dữ liệu như
  - **format** : loại file cần đọc
  - **path** : đường dẫn đến file cần đọc
  - **mode** : cơ chế đọc file
    do DataFrame làm việc với các dữ liệu có cấu trúc
    nên đôi khi trong lúc đọc file sẽ có một số phần tử bị lỗi
    (thiếu trường dữ liệu, sai kiểu dữ liệu,..)
    và các cơ chế đọc file sẽ có từng cách xử lý khác nhau
    có 3 MODE đọc file:
    - **Permissive** : tất cả các trường được đặt thành null
      và các bản ghi bị hỏng được đặt trong một cột được gọi là \_corrupt_record.
    - **DropMalformed** : xóa các hàng bị lỗi
    - **FailFast** : đưa ra lỗi cho hệ thống khi có hàng bị lỗi
  - **schema** : cấu trúc của dữ liệu ta muốn đọc
    hoặc có thể để hệ thống tự thiết lập nếu như dữ liệu có schema đơn giản
- video: [Spark DataFrameReader API](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20434109#overview)
- video: [Thực hành: Đọc dữ liệu từ file JSON, CSV,...](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20434113#overview)

##### Spark dataschema

- Chúng ta có thể cung cấp Schema để Spark có thể nắm được cấu trúc của dữ liệu
- Spark sẽ có các kiểu dữ liệu như sau: ![scala types](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L6_4.png?alt=media&token=20f63cfb-b18f-4442-a93f-dd0c4d403fd2)
- Chúng ta sẽ có 2 cách khai báo Schema:
  - Cách 1: Khai báo dưới dạng StructType
    ![structType declaration](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L6_5.png?alt=media&token=cd3da1ea-4a1b-4bb8-98c5-cef6e88874b0)
  - Cách 2: Khai báo dưới dạng DDL String
    ![schemaDDL declaration](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L6_6.png?alt=media&token=3c17ba54-bf79-4921-8680-1b619209cfc7)
- Video: [Tạo Spark DataFrame Schema](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20434117#overview)

##### DataFrameWriter API

- Tương tự với việc đọc dữ liệu thì Spark SQL cũng cung cấp cho chúng ta DataFrameWriter API
  để ghi dữ liệu ra các Sink, cách sử dụng DataFrameWriter như sau
  ![DataFrameWriter](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L6_8.png?alt=media&token=9b4dde07-7e38-49e1-84d9-a180fb54797c)
- Ta cũng sẽ cần khai báo 1 tham số để thiết lập cho việc ghi dữ liệu
- Video: [Spark DataFrameWriter API](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20434121#overview)
- Video: [Thực hành: Lưu dữ liệu ra file](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20434125#overview)

### Lab3 - Read write operators with Dataframe

- [Gdrive](https://colab.research.google.com/drive/1NMdi4R255huTfbr2g9p6fxTnQTRvPlRH?usp=sharing)

### SparkSQL and SparkSQL Table

#### SparkSQL manual

- Ngoại trừ sử dụng các hàm có sẵn để tương tác với dữ liệu
  thì Spark cũng cung cấp cơ chế sử dụng câu lệnh SQL để truy vấn dữ liệu
  Để sử dụng cơ chế này, bạn sẽ cần lưu trữ lại Dataframe đó dưới dạng 1 Hive Table trong Spark Session
  (khi session này kết thúc thì bảng đó cũng sẽ bị xóa)
  và sau đó có thể sử dụng các câu lệnh SQL để truy vấn
  ví dụ như sau:
  ```python
  surveyDF.createOrReplaceTempView("survey_tbl")
  countDF = spark.sql("select Country, count(1) as count from survey_tbl where Age<40 group by Country")
  ```
- Video: [Sử dụng SparkSQL](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20399111#overview)
- Để có thể thực hiện được các câu lệnh SQL, cơ chế này sẽ gồm 4 bước như sau và sẽ được thực hiện thông qua **Spark SQL Engine**:
  - **Analysis**:
    Spark sẽ đọc và tạo nên 1 Abstract Syntax Tree
    từ đó sẽ lấy được các thông tin như tên bảng, tên cột,...
  - **Logical Optimization**:
    Spark sẽ tối ưu hóa lại các truy vấn để tiết kiệm thời gian thực thi
  - **Physical Planning**:
    Spark sẽ lựa chọn ra phương án tối ưu phù hợp nhất để thực thi
  - **Code Generation**:
    Chuyển hóa truy vấn về các câu lệnh Java rồi thực hiện
- Video: [Spark SQL engine và Catalyst optimizer](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20399117#overview)
- Video: [Tối ưu hóa truy vấn trong SparkSQL](https://www.coursera.org/learn/introduction-to-big-data-with-spark-hadoop/lecture/DFpdP/catalyst-and-tungsten)

#### Spark Databases and Tables

- Trong spark cũng có _Database_ trong đó, vậy nên có thể tạo các Database
  và từ đó tạo các Table và View ở trong chính Spark.
  Một table ở trong Spark sẽ có 2 phần:
  - **Table Data**:
    được lưu trữ dưới dạng Data File ở trong hệ thống lưu trữ phân tán
  - **Table Metadata**:
    hay còn được gọi là catalog
    lưu các thông tin về bảng và dữ liệu của bảng đó như Schema: tên bảng, phân vùng,...
    Các dữ liệu này có thể được lưu theo Spark Session
    hoặc ở Hive
- _Spark table_ cũng được chia thành 2 loại:
  - **Managed Tables**:
    Dữ liệu ở Table sẽ được lưu ở 1 đường dẫn là **spark.sql.warehouse.dir**
    (do Cluster Admin quy định)
    Và khi ta xóa Table này đi thì Spark cũng sẽ xóa cả Metadata và dữ liệu của bảng
  - **Unmanaged Tables**:
    Khi tạo bảng này thì ta sẽ cần khai báo thêm cả về nơi mà Table Data sẽ được lưu trữ
    (có thể là một Data Store ở bên ngoài)
    lúc này Spark sẽ chỉ tạo Table Metadata để lưu trữ các thông tin về bảng.
    Khi ta xóa Table này thì Spark cũng chỉ xóa Metadata chứ không xóa dữ liệu
- Video: [Spark Databases và Tables](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20434129#overview)
- Để tạo một Managed Tables, ta có thể sử dụng câu lệnh như sau:
  ```python
  flightTimeParquetDF.write \
    .mode("overwrite")
    .saveAsTable("flight_data_tbl")
  ```
- Video: [Làm việc với SparkSQL Table](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20434133#overview)
- Video: [Ví dụ: Sử dụng Spark SQL](https://funix.udemy.com/course/taming-big-data-with-apache-spark-hands-on/learn/lecture/5586918#overview)

### Lab 4 - Using SparkSQL Table

- Lab 4.1 - [HelloSparkSQL](https://colab.research.google.com/drive/13_HlauTB5JYyXkIlBzloO_nl6HJQaLfF?usp=sharing)
- Lab 4.2 - [SparkSQLTableDemo](https://colab.research.google.com/drive/1pa4x9eoH4LVJ2rquNWeuT_gdrnWOFoUz?usp=sharing)

### Data transformation with Spark

#### Row and Column

- sau khi đã đọc được dữ liệu thì chúng ta sẽ cần thực hiện các phép chuyển đổi dữ liệu
- khi đọc dữ liệu, ta có thể lưu chúng dưới 2 dạng khác nhau
  - **dataframe**
  - **database table**
- 1 số thao tác phổ biến về việc xử lý dữ liệu trên Dataframe:
  - **hợp nhất các Dataframe( JOIN, UNION)**
  - **Tổng hợp lại dữ liệu từ nhiều Dataframe(joining, windowing, rollups)**
  - **Sử dụng các hàm và các Transformation có sẵn**
  - **Sử dụng các hàm tự định nghĩa**
- udemy: [Giới thiệu về Data Transformation](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20495288#overview)
- do dataframe sẽ lưu trữ các dữ liệu có cấu trúc theo các cột và hàng
  nên các thao tác cũng được chia ra để sử dụng cho các cột và hàng
  các thao tác với hàng sẽ biển đổi từng hàng trong Dataframe thành 1 hàng mới
  vd: ![dataframe rows](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L6_7.png?alt=media&token=a5b86e20-40f3-4a97-b980-80bfb40a741b)
- udemy: [Làm việc với dataframe rows](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20495330#overview)
- video tham khảo: [Dataframe Rows và Unit Testing](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20554784#overview)
- một ví dụ điển hình cho việc biến đổi các Row đó là để chuyển các dữ liệu
  không cấu trúc thành các dữ liệu có cấu trúc.
  giả sử ta muốn lấy các dữ liệu từ log file vô cùng lộn xộn chứ không được
  sắp xếp theo các cột và hàng.
  ví dụ ta có log file như sau:
  ```
  83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-search.png HTTP/1.1" 200 203023 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
  83.149.9.216 - - [17/May/2015:10:05:43 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-dashboard3.png HTTP/1.1" 200 171717 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
  83.149.9.216 - - [17/May/2015:10:05:47 +0000] "GET /presentations/logstash-monitorama-2013/plugin/highlight/highlight.js HTTP/1.1" 200 26185 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
  83.149.9.216 - - [17/May/2015:10:05:12 +0000] "GET /presentations/logstash-monitorama-2013/plugin/zoom-js/zoom.js HTTP/1.1" 200 7697 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
  83.149.9.216 - - [17/May/2015:10:05:07 +0000] "GET /presentations/logstash-monitorama-2013/plugin/notes/notes.js HTTP/1.1" 200 2892 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
  83.149.9.216 - - [17/May/2015:10:05:34 +0000] "GET /presentations/logstash-monitorama-2013/images/sad-medic.png HTTP/1.1" 200 430406 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
  ```
- nếu như bạn cần trích xuất các thông tin như thời gian, IP,...
  thì chúng ta sẽ cần phải sử dụng các Row Transformation
  để xử lý từng hàng dữ liệu.
  Spark cũng cung cấp cho chúng ta nhiều hàm hỗ trợ cho việc xử lý dữ liệu,
  ta có thể tham khảo các hàm đó và xem ví dụ ở các video sau
- udemy: [Dataframe Row và dữ liệu phi cấu trúc](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20585510#overview)
- [Spark Dataframe API](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/dataframe.html?highlight=dataframe)
- [Spark Function](https://spark.apache.org/docs/2.4.0/api/python/pyspark.sql.html)
- Tương tự với các hàng, Spark cũng cung cấp các hàm để chuyển đổi cho các cột
  Chúng ta sẽ có 2 thao tác chính như sau:
  - Tạo một con trỏ tới các cột trong Dataframe
  - Tạo các biểu thức để biến đổi các dữ liệu theo từng cột
- Với mỗi thao tác này thì chúng ta sẽ có 2 các làm là thông qua:
  - **Column String**
    - là cách chúng ta sử dụng một chuỗi để khai báo tên cột muốn lấy
      hoặc là khai báo biểu thức mà chúng ta muốn dùng cho cột đó
    - ví dụ: sử dụng _Column String_ để tạo con trỏ đến các cột:
      ```python
      airlinesDF.select("Origin", "Dest", "Distance").show(10)
      ```
    - ví dụ: sử dụng _Column String_ để khai báo các biểu thức biến đổi
      ```python
      airlinesDF.selectExpr("Origin", "Dest", "Distance", "to_date(concat(Year,Month,DayOfMonth),'yyyyMMdd') as FlightDate").show(10)
      ```
  - **Columns Object**
    - cũng giống như String nhưng thay vì dùng chuỗi thì bạn sẽ dùng các hàm
      hoặc các đoạn code Python để thực hiện việc tạo con trỏ hoặc khai báo
      biểu thức
    - ví dụ: sử dụng _Column Object_ để tạo con trỏ đến các cột:
      ```python
      from pyspark.sql.functions import *
      airlinesDF.select(column("Origin"), col("Dest"), "Distance").show(10)
      ```
    - ví dụ: sử dụng _Column Object_ để khai báo các biểu thức biến đổi
      ```python
      airlinesDF.select("Origin", "Dest", "Distance")
      to_date(concat("Year","Month","DayofMonth"),"yyyyMMdd").alias("FlightDate")
      ```
- udemy: [Làm việc với Dataframe Columns](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20601288#overview)

#### Data transformation by other ways

- Ngoài sử dụng các hàm có sẵn trong Spark
  chúng ta có thể tự định nghĩa để xử lý dữ liệu được gọi là UDF **(User Defined Function)**
  Cách này sẽ thuận tiện hơn nếu bạn muốn thực hiện các xử lý phức tạp.
  Để sử dụng được cơ chế này bạn sẽ cần 3 bước:
  - Khai báo hàm bạn sẽ sử dụng để xử lý dữ liệu
  - Đăng ký hàm đó thành 1 UDF
  - Sử dụng hàm
- UDF cũng sẽ hỗ trợ 2 cách thức là qua **String Expression** hoặc **Object Expression**
  với mỗi cách thức sử dụng này thì việc đăng ký và sử dụng UDF cũng sẽ khác nhau
- Để sử dụng _Object Expression_ ta có ví dụ như sau:
  ```python
  # Register UDF
  parse_gender_udf = udf(parse_gender, returnType=StringType())
  # Use UDF
  survey_df2 = survey_df.withColumn("Gender", parse_gender_udf("Gender"))
  ```
- Để sử dụng _String Expression_ ta cũng có ví dụ như sau:
  ```python
  # Register UDF
  spark.udf.register("parse_gender_udf", parse_gender, StringType())
  # Use UDF
  survey_df3 = survey_df.withColumn("Gender", expr("parse_gender_udf(Gender)"))
  ```
- Udemy: [Sử dụng UDF](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20655744#overview)
- chúng ta có một số tip và code để thực hiện 1 số thao tác với Dataframe nhanh hơn từ video sau: [Misc Transformation](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20702078#overview)
  - Cách tạo Dataframe nhanh nhất
  - Tạo trường id có thể tự động tăng
  - Sử dụng Case When Then Transformation
  - Chuyển đổi kiểu dữ liệu của một cột
  - Thêm/xóa các cột
  - Loại có các hàng trùng nhau
  - Sắp xếp lại Dataframe

### Lab 5 - Transformation operators with DataFrame

- [Lab 5.1: RowDemo](https://colab.research.google.com/drive/1d_48Rlj3SR0Fydgbm5N2nNFtcE3EWB_5?usp=sharing)
- [Lab 5.2: LogFileDemo](https://colab.research.google.com/drive/1jmNKDuwkFcytWcQRpEG6lg3C4940DLv1?usp=sharing)
- [Lab 5.3: ColumnDemo](https://colab.research.google.com/drive/1gkCWTykfuD0CCcXZGLlGExzZiCpipbCI?usp=sharing)
- [Lab 5.4: UDF Demo](https://colab.research.google.com/drive/1l_--yG5TIV-2cBfAkgdqdRx44IbEaykI?usp=sharing)

### Data Aggregation & Join on Spark

#### Data Aggregation

- Tập hợp dữ liệu
  - Ngoài các thao tác biến đổi dữ liệu thì chúng ta có các thao tác tổng hợp dữ liệu (Data Aggregation)
    sử dụng khi chúng ta muốn tính toán, tổng hợp dữ liệu từ nhiều Dataframe khác nhau
    Hoặc ta cũng có thể sử dụng các thao tác này để tổng hợp dữ liệu theo từng nhóm trên một DataFrame
  - Ví dụ:
    - Ta có bảng dữ liệu invoice_df như sau
    ```csv
    InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country
    536365,,WHITE HANGING HEART T-LIGHT HOLDER,6,01-12-2010 8.26,2.55,17850,United Kingdom
    536365,71053,WHITE METAL LANTERN,6,01-12-2010 8.26,3.39,17850,United Kingdom
    536365,84406B,CREAM CUPID HEARTS COAT HANGER,8,01-12-2010 8.26,2.75,17850,United Kingdom
    536365,84029G,KNITTED UNION FLAG HOT WATER BOTTLE,6,01-12-2010 8.26,3.39,17850,United Kingdom
    536365,84029E,RED WOOLLY HOTTIE WHITE HEART.,6,01-12-2010 8.26,3.39,17850,United Kingdom
    536365,22752,SET 7 BABUSHKA NESTING BOXES,2,01-12-2010 8.26,7.65,17850,United Kingdom
    536365,21730,GLASS STAR FROSTED T-LIGHT HOLDER,6,01-12-2010 8.26,4.25,17850,United Kingdom
    536366,22633,HAND WARMER UNION JACK,6,01-12-2010 8.28,1.85,17850,United Kingdom
    ```
    - Ta có thể thao tác `sum()`, `avg()`,... để thực hiện tính toán và tổng hợp dữ liệu
    ```python
    invoice_df.select(f.count("*").alias("Count *"),
        f.sum("Quantity").alias("TotalQuantity"),
        f.avg("UnitPrice").alias("AvgPrice"),
        f.countDistinct("InvoiceNo").alias("CountDistinct"))
    ```
    - Và được kết quả như sau
    ```
    +-------+-------------+-----------------+-------------+
    |Count *|TotalQuantity|         AvgPrice|CountDistinct|
    +-------+-------------+-----------------+-------------+
    | 541909|      5176450|4.611113626088512|        25900|
    +-------+-------------+-----------------+-------------+
    ```
    - Ta cũng có thể dùng **String Expression**
    ```python
    invoice_df.selectExpr(
      "count(1) as `Count 1`",
      "count(StockCode) as `count field`",
      "sum(Quantity) as TotalQuantity",
      "avg(UnitPrice) as AvgPrice"
    ).show()
    ```
    - Ngoài ra, các thao tác Aggregation cũng giúp chúng ta tính toán và gộp nhóm theo 1 số trường nhất định
      ví dụ, nếu muốn tính 2 cột là InvoiceValue và TotalQuantity theo từng bước ta dùng hàm `agg()` như sau
    ```python
    summary_df = invoice_df \
        .groupBy("Country", "InvoiceNo") \
        .agg(f.sum("Quantity").alias("TotalQuantity"),
             f.round(f.sum(f.expr("Quantity * UnitPrice")), 2).alias("InvoiceValue"),
             f.expr("round(sum(Quantity * UnitPrice),2) as InvoiceValueExpr"))
    ```
    - kết quả cho ví dụ trên:
    ```
    +--------------+----------+-------------+------------+
    |       Country|Invoice No|TotalQuantity|InvoiceValue|
    +--------------+----------+-------------+------------+
    |United Kingdom|    536446|          329|      440.89|
    |United Kingdom|    536508|          216|      155.52|
    |United Kingdom|    537018|           -3|         0.0|
    |United Kingdom|    537401|          -24|         0.0|
    ```
  - Tài liệu tham khảo: [Spark Dataframe APIs](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/frame.html)
  - Video udemy: [Aggregating Dataframes](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20715134#overview)
  - Video udemy: [Grouping Aggregations](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20717420#overview)
- **Cửa sổ trượt - Windowing aggregation**

  - Ví dụ ta muốn thêm 1 cột RunningTotal để tính tổng Invoice từ tuần đầu tiên đến tuần hiện tại:

    ```
    +-------+----------+-----------+-------------+------------+------------+
    |Country|WeekNumber|NumInvoices|TotalQuantity|InvoiceValue|RunningTotal|
    +-------+----------+-----------+-------------+------------+------------+
    |EIRE   |        48|          7|         2822|     3147.23|     3147.23|
    |EIRE   |        49|          5|         1280|      3284.1|     6431.33|
    |EIRE   |        50|          5|         1184|     2321.78|     8753.11|
    |EIRE   |        51|          5|           95|      276.84|     9029.95|
    +-------+----------+-----------+-------------+------------+------------+
    +-------+----------+-----------+-------------+------------+------------+
    |France |        48|          4|         1299|     2808.16|     2808.16|
    |France |        49|          9|         2303|     4527.01|     7335.17|
    |France |        50|          6|          529|      537.32|     7872.49|
    |France |        51|          5|          847|     1702.87|     9575.36|
    +-------+----------+-----------+-------------+------------+------------+
    ```

    - Lúc này chúng ta sẽ phải làm 3 bước:
      - **Bước 1**: Phân chia dữ liệu thành các vùng khác nhau.
      - **Bước 2**: Xác định trường để sắp xếp dữ liệu.
      - **Bước 3**: Xác định cách cửa sổ trượt hoạt động và các phép tính toán.
    - Với ví dụ này, ta sẽ có các điều kiện như sau:
      - Trường để phân chia dữ liệu: **Country**
      - Trường để sắp xếp dữ liệu: **WeekNumber**
      - Trường sẽ được dùng để trượt và tính tổng: **InvoiceValue**
    - Ta có thể sử dụng đoạn code sau để thực hiện thao tác:

      ```python
      running_total_window = Window.partitionBy("Country") \
        .orderBy("WeekNumber") \
        .rowsBetween(Window.unboundedPreceding, Window.currentRow)

      summary_df.withColumn("RunningTotal",
                          f.sum("InvoiceValue").over(running_total_window)) \
        .show()
      ```

  - Tài liệu tham khảo: [Spark Dataframe Window](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.Window.html)
  - Video Udemy: [Windowing Aggregations](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20718896#overview)

#### Data join

- **Join** là thao tác vô cùng quan trọng khi chúng ta muốn tổng hợp dữ liệu từ nhiều nguồn dataframe khác nhau
- Ví dụ muốn gộp 2 DataFrame chứa thông tin đặt hàng và thông tin sản phẩm với cấu trúc sau
  ![cấu trúc 2 dataframe](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L8_5.png?alt=media&token=4a328a5e-fcac-4e37-aeac-bd04b88e08c4)
- Spark hỗ trợ hầu hêt các loại JOIN trong database, ta có thể sử dụng như sau:
  ```python
  join_expr = order_df.prod_id == product_df.prod_id
  order_df.join(product_df, join_expr, "inner") \
          .select("order_id", "prod_id", "prod_name", "unit_price", "list_price", "qty")
          .show()
  ```
- Các mode Join trong spark:
  - **"inner"**: INNER JOIN
  - **"outer"**: FULL OUTER JOIN
  - **"left"**: LEFT OUTER JOIN
  - **"right"**: RIGHT OUTER JOIN
- Video udemy: [Dataframe Joins với tên cột không rõ ràng](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20930430#overview)
- Video udemy: [Outer Joins với Dataframe](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20949086#overview)
- Do Spark hỗ trợ xử lý dữ liệu phân tán vậy nên có thể dữ liệu trong Dataframe sẽ ở các phân vùng khác nhau.
  Từ đó dẫn đến một vấn đề khi JOIN đó là có thể bị thiếu dữ liệu,
  do dữ liệu tương ứng đang ở một phân vùng khác.
  ![ví dụ join thiếu dữ liệu do phân vùng](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L8_6.png?alt=media&token=2679fdb7-57ec-44a5-a18a-6ed4fbad1c5c)
  Lúc này Spark sẽ sử dụng một cơ chế gọi là Internal Joins and Shuffle,
  cơ chế này hoạt động khá giống với MapReduce.
  Ở Stage đầu tiên dữ liệu sẽ được tạo các id dựa trên điều kiện JOIN (join key)
  sau đó chuyển xuống các node để thực hiện việc JOIN dữ liệu.
  Điều đặc biệt là dữ liệu được gửi xuống các node sẽ được shuffle lại
  sao cho các id của cả hai bảng đều trùng nhau giúp tránh việc thiếu sót dữ liệu.
- Video udemy: [Spark Join và shuffle](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/20968646#overview)
- Cần phải lưu ý là việc sử dụng Internal Joins and Shuffle sẽ tốn rất nhiều tài nguyên
  do ta sẽ cần di chuyển dữ liệu sang các node, phân vùng khác nhau.
  Và cũng tùy thuộc vào số lượng các node xử lý mà ta đang thiết lập,
  nếu quá lớn thì có thể không cần thiết hoặc quá nhỏ dẫn đến dữ liệu xử lý chậm đi.
  Còn một phương án khác, đó là sử dụng Broadcast Join.
  Cơ chế này chỉ nên sử dụng nếu như 1 trong các dataframe của ta có khối lượng rất nhỏ
  so với dataframe còn lại, cơ chế này sẽ chuyển dữ liệu từ Dataframe
  nhỏ tới toàn bộ phân vùng chứa dữ liệu của Dataframe còn lại.
  Điều này đôi khi sẽ tiết kiệm tài nguyên hơn so với Shuffle.
- Mặc định Spark sẽ tự tính toán và lựa chọn xem nên dùng Broadcast hay Shuffle,
  nhưng chúng ta cũng có thể tự thiết lập để Spark sử dụng Boadcast như sau:

  ```python
  join_expr = order_df.prod_id == product_df.prod_id

  order_df.join(broadcast(product_df), join_expr, "inner") \
    .select("order_id", "prod_id", "prod_name", "unit_price", "list_price", "qty") \
    .show()
  ```

  ![mô phỏng broadcast df](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L8_7.png?alt=media&token=cf8ffd60-a643-4b28-a7bd-64b4774a0f75)

- Video udemy: [Tối ưu hóa thao tác Join](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/21019950#overview)
- Chúng ta cũng sẽ có phương án khác, đó là chia bucket cho Dataframe.
  Phương án này nên được sử dụng nếu dữ liệu chúng ta cần join nhiều lần,
  và chắc chắn sẽ cần phải thực hiện JOIN.
  Bản chất khi chia bucket thì chúng ta cũng đang thực hiện thao tác Shuffle
  nhưng thao tác này chỉ cần thực hiện một lần,
  các lần Join sau sẽ không cần phải Shuffle dữ liệu nữa mà sử dụng trực tiếp bucket luôn.
- Video udemy: [Bucket Joins](https://funix.udemy.com/course/apache-spark-programming-in-python-for-beginners/learn/lecture/21052336#overview)

### Lab 6 - Aggregation & Join operators

- [Lab 6.1: AggDemo](https://colab.research.google.com/drive/1wnbWQFHl4mrSCk8fjy9GFx30bRp2C-le?usp=sharing)
- [Lab 6.2: WindowingDemo](https://colab.research.google.com/drive/1q6iHk4ssismHi2Dq51kHdY_mSfV7wlga?usp=sharing)
- [Lab 6.3: Spark Join Demo](https://colab.research.google.com/drive/1ADa-IMk7zXK3btoBepUxPVfsoqvx_8pB?usp=sharing)

### Lab 7 - Advanced operators with DataFrame

- [Lab 7.1: Most Popular Superhero](https://colab.research.google.com/drive/1FmGCZwzQAghvwUeFlP4TdNKrQTUNChlF?usp=sharing)

### Spark Streaming

#### Data streaming concept

- Batch processing và Stream processing
  - Thực tế chúng ta phải xử lý lượng dữ liệu lớn và được nạp liên tục
  - Ví dụ,
    một sàn thương mại điện tử sẽ cần cập nhật liên tục các dữ liệu về mua bán,
    về lượt click xem sản phẩm của khách hàng,..
    Dữ liệu tăng lên thì nhu cầu phân tích tận dụng dữ liệu đó cũng tăng lên tương ứng.
    Việc xử lý lượng lớn dữ liệu thường được thực hiện bằng **Batch Processing**,
    dữ liệu chứa hàng triệu bản ghi mỗi ngày được lưu trữ dưới dạng các tệp tin hoặc bản ghi
    Các tệp tin này sẽ trải qua quá trình xử lý sau một thời gian nhất định
    để phân tích theo cách khác nhau mà công ty muốn thực hiện
    ![batch processing](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L10_2.jpeg?alt=media&token=6cc24f8e-5742-4a00-aa33-ac720af4c038)
  - Tuy nhiên, cách xử lý này sẽ có nhiều vấn đề liên quan đến việc chính xác của việc phân tích
    hoặc là không thể đưa ra các phân tích theo thời gian thực, và để xử lý các vấn đề trên
    thì chúng ta sẽ sử dụng **Stream Processing**
    Có thể hiểu đơn giản _Stream Processing_ là xử lý dữ liệu ngay khi nó xuất hiện trong hệ thống
    Mở rộng hơn nữa, _stream processing_ có khả năng làm việc với luồng dữ liệu vô hạn,
    quá trình tính toán xảy ra liên tục.
    ![stream processing](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L10_1.jpeg?alt=media&token=521b25d1-bed0-489e-8ede-4574a5fe4a6f)
  - Video udemy: [Giới thiệu về stream](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955586#overview)
- Spark streaming
  - Spark streaming dựa trên cơ chế micro-batches, tức là sẽ lấy dữ liệu dựa theo thời gian ngắn
    và xử lý bao gồm những tính chất sau:
    - Tự động lặp giữa các batches
    - Quản lý thời gian bắt đầu và kết thúc của từng batch
    - Quản lý trạng thái trung giang
    - Kết hợp kết quả phân tích từ các phân tích trước
    - Có cơ chế chịu lỗi và khởi động lại
  - Trước đây Spark cung cấp 1 dạng là **DStream** dựa trên _RDD_,
    nhưng hiện nay do DataFrame được sử dụng phổ biến hơn nên Spark đã đưa ra 1 dạng mới là
    **Structured Stream** với các ưu điểm sau:
    - Sử dụng Dataframe Base thay cho RDD
    - Sử dụng cơ chế tối ưu hóa của SQL Engine
    - Hỗ trợ Event Time Semantic
    - Có nhiều cải tiến hơn so với DStream
  - Video udemy: [DStream và Structured Streaming](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955588#overview)

#### Data Stream Processing with Spark

- 3 bước xử lý dữ liệu dạng Stream với ứng dụng Spark:
  - **Read**: Đọc dữ liệu từ luồng
  ```python
  lines_df = spark.readStream \
      .format("socket") \
      .option("host", "localhost") \
      .option("port", "9999") \
      .load()
  ```
  - **Transform**: Thực hiện các thao tác biến đổi dữ liệu
  ```python
  words_df = lines_df.select(expr("explode(split(value,' ')) as word"))
  counts_df = words_df.groupBy("word").count()
  ```
  - **Sink**: Lưu dữ liệu đã được xử lý ra một nền tảng khác.
  ```python
  word_count_query = counts_df.writeStream \
      .format("console") \
      .outputMode("complete") \
      .option("checkpointLocation", "chk-point-dir") \
      .start()
  ```
  - Video udemy: [Tạo ứng dụng xử lý Stream đầu tiên](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955590#overview)
- Cơ chế xử lý của Spark
  - các vòng xử lý stream sẽ tự động lặp lại mặc dù ta không viết một vòng lặp nào,
    đây là cơ chế xử lý của spark
  - Khi thực thi đoạn code thì Spark Driver sẽ thực hiện thao tác phân tích, tối ưu và biên dịch code
    và từ đó sẽ tạo ra 1 **Execution Plan** (bao gồm các Stages và Tasks).
  - Sau đó hệ thống sẽ có 1 **Background Thread** chạy các micro-batch
  - Sau khi thực hiện xong 1 _micro-batch_ thì Background Job sẽ chờ để nhận Input từ Stream
    để tạo micro-batch tiếp theo **ngay lập tức**
  - Vòng lặp này sẽ được điều khiển ở background và chạy mãi mãi.
    ![Execution plan](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L10_3.png?alt=media&token=a2f78f3f-cfb6-4e8a-8c75-d13ec553867b)
  - Ngoài ra, chúng ta cũng có thể thiết lập cách để tạo micro-batch tiếp theo
    Spark sẽ cung cấp chúng ta 4 cơ chế như sau:
    - **Unspecified**
      - Đây là cơ chế mặc định, một micro-batch mới sẽ được tạo ra ngay lập túc
        khi có dữ liệu mới từ source
    - **Time Interval**
      - Một micro-batch sẽ được tạo ra sau một khoảng thời gian nhất định
      - Nếu như micro-batch trước thực hiện quá thời gian thì micro-batch sau sẽ chờ và thực hiện ngay
        sau khi batch trước thực hiện xong, giúp cho dữ liệu được bảo toàn
    - **One time**
      - Cơ chế này giống như _Batch processing_, đoạn code chỉ chạy 1 lần duy nhất.
    - **Continuous**
      - Đây là cơ chế thử nghiệm, giúp cho thời gian giữ các batch sẽ được giảm xuống thấp nhất
  - Video udemy: [Stream processing model trong Spark](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955596#overview)

#### Read data from File Source

- Chúng ta có 4 loại source khi đọc các dữ liệu dạng luồng:
  - Socket source
  - Rate source
  - File source
  - Kafka source
- Trên thực tế, thường sẽ dùng File Source hoặc Kafka Source
  - File Source có thể là một hệ thống lưu trữ phân tán
    (các file được tạo ra liên tục từ các Data Ingestion Pipeline)
    khi đọc dữ liệu từ các File Source, ta có thể làm theo cơ chế sau:
    - Tạo các batch, mỗi batch sẽ đọc và xử lý dữ liệu từ một số lượng file nhất định.
    - Sau khi đọc xong sẽ loại các file đó ra, để batch tiếp theo không xử lý nhầm các file đó nữa
    - Lặp lại quy trình này sau một khoảng thời gian
  - Spark streaming đều hỗ trợ rất tốt các bước trong cơ chế này,
    đồng thời cũng có các phương pháp để đảm bảo cơ chế xử lý chính xác chứ không bị lỗi
- Video udemy: [Làm việc với File Source](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955598#overview)
- Video udemy: [Streaming Sources, Sinks và Output Mode](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955602#overview)
- Video udemy: [Khả năng chịu lỗi và khởi động lại](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955606#overview)

### Lab8 - Spark streaming exercises

- [Lab 8.1: FileStreamDemo](https://drive.google.com/file/d/1Z10FPlPMwyW8w6OkHC6BJVFWcsMUxGVV/view?usp=sharing)

### Reading Kafka Source & join operators with Stream

#### Kafka introduction and installing

- **Kafka** là hệ thống message pub/sub phân tán (distributed messaging system).
- Bên public dữ liệu được gọi là producer,
  bên subscribe nhận dữ liệu theo topic được gọi là consumer.
- Kafka có khả năng truyền một lượng lớn message theo thời gian thực,
  trong trường hợp bên nhận chưa nhận
  message vẫn được lưu trữ sao lưu trên một hàng đợi
  và cả trên ổ đĩa bảo đảm an toàn.
- Đồng thời nó cũng được replicate trong cluster giúp phòng tránh mất dữ liệu.
- Kafka là một hệ thống rất thích hợp cho
  việc xử lý dòng dữ liệu trong thời gian thực.
- Khi dữ liệu của một topic được thêm mới ngay lập tức
  được ghi vào hệ thống và truyền đến cho bên nhận.
- Ngoài ra Kafka còn là một hệ thống có đặc tính durability
  dữ liệu có thể được lưu trữ an toàn cho đến khi bên nhận sẵn sàng nhận nó.
- ![kafka instroduction](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L11_1.jpg?alt=media&token=d09ccdc7-b5e5-473d-9a36-3f977f6cbf4e)
- Video: [Giới thiệu và cài đặt Kafka](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955580#overview)

#### Read & Write data from Kafka

- Để đọc các dữ liệu từ Kafka,
  ta sẽ cần thêm một số tham số về Kafka như sau:

  ```python
  kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "invoices") \
    .option("startingOffsets", "earliest") \
    .load()
  ```

- Do dữ liệu trong kafka được xử lý theo dạng Key-Value nên khi đọc dữ liệu,
  ta sẽ cần chuyển giá trị Value thành các cột trong Dataframe tương ứng,
  ví dụ:
  `value_df = kafka_df.select(from_json(col("value").cast("string"), schema).alias("value"))`

- Chúng ta có thể đưa dữ liệu vào 2 loại Data Sink:

  - **File Sink**: lưu dữ liệu dưới dạng file
    ```python
    invoice_writer_query = flattened_df.writeStream \
      .format("json") \
      .queryName("Flattened Invoice Writer") \
      .outputMode("append") \
      .option("path","output") \
      .option("checkpointLocation","chk-point-dir") \
      .trigger(processingTime='1 minute')
      .start()
    ```
  - **Kafka Sink**:
    - do kafka hoạt động theo cơ chế Producer - Consumer
      nên bản thân Kafka cũng có thể được sử dụng như là 1 Data Sink.
    - tuy nhiên, ta sẽ cần phải chuyển đổi dữ liệu từ dạng Dataframe
      chứa nhiều cột thành Dataframe chỉ có 2 cột là Key-Value để
      Kafka có thể nhận được:
      ```python
      kafka_target_df = notification_df.selectExpr("InvoiceNumber as key",
              """to_json(named_struct(
                'CustomerCardNo',CustomerCardNo,
                'TotalAmount',TotalAmount,
                'EarnedLoyaltyPoints',TotalAmount*0.2)) as value""")
      ```
  - Udemy video: [Streaming từ Kafka Source](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955612#overview)
  - Udemy video: [Làm việc với Kafka](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955616#overview)

- Ta có thể kết hợp 2 loại datasink này cùng 1 lúc chứ không cần phải viết
  từng ứng dụng một, điều này giúp tiết kiệm các thao tác
  đọc và xử lý dữ liệu hơn, các thao tác này sẽ được xử lý song song với nhau
  và các **_checkpointLocation_** cũng phải được để khác nhau
  để tránh sự xung đột.

  - Udemy Video: [Multi-query Streams Application](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955620#overview)

- Trong kafka hỗ trợ 3 dạng dữ liệu Source là String/JSON, CSV và AVRO
  Tương ứng với từng loại source sẽ có các hàm phụ hợp để chuyển dữ liệu
  từ dạng Binary ra các Object tương ứng.
  Ví dụ với JSON sẽ có **to_json()** và **from_json()**
  - Udemy video: [Kafka Serialization và Deserialization cho Spark](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955622#overview)

#### Joining operations in working data from Kafka

- Spark Streaming hỗ trợ hai thao tác join:

  - Join một Streaming Dataframe với 1 Dataframe tĩnh.
  - Join một Streaming Dataframe với 1 Streaming Dataframe khác

- Cách join với một Dataframe tĩnh thường được sử dụng trong trường hợp
  ta cần lấy thêm các thông tin từ một nguồn dữ liệu tĩnh khác.
  Ví dụ như lấy các thông tin về người dùng khi có các lần login mới
  (dữ liệu Stream sẽ là các lần login).

  - Udemy video: [Kết hợp Stream với một nguồn dữ liệu tĩnh](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/22355480#overview)

- Khi join hai Streaming Dataframe với nhau, sẽ có một trường hợp là
  dữ liệu ở Dataframe 1 chưa xuất hiện ở Dataframe 2
  và sẽ khiến dữ liệu khi Join không còn được đầy đủ.
  Vì vậy Spark đã tạo ra một cơ chế gọi là State,
  lúc này tất cả dữ liệu sẽ được lưu lại ở một State,
  kể cả khi dữ liệu được Join thành công hay không thành công.
  Tuy nhiên cơ chế này lại dẫn đến một khả năng đó là chúng ta
  bị lặp lặp lại dữ liệu, nên ta cần phải để ý khi
  Join 2 Data Streaming với nhau để có thể bảo toàn được hiệu suất.

  - Udemy Video: [Kết hợp Stream với một nguồn Stream khác](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/22369992#overview)

- Để giải quyết vấn đề trùng lặp dữ liệu ở trên,
  ta có thể sử dụng Streaming Watermark.
  Tức là chúng ta sẽ đặt ra một khoảng thời gian mà
  các dữ liệu trong State Store được tồn tại,
  khi một dữ liệu mới được đưa vào thì Spark
  sẽ kiểm tra lại "hạn" của các dữ liệu cũ và xóa chúng đi nếu cần thiết.

  - Udemy Video: [Streaming Watermark](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/22370012#overview)

- Spark cũng hỗ trợ cơ chế Left Join và Right Join
  (Full Outer Join hiện đang không hỗ trợ),
  tuy nhiên ta sẽ cần chú ý một số điều như sau:
  - Khi sử dụng **Left Join** thì Streaming Dataframe sẽ phải nằm ở bên **trái**,
    ngược lại nếu ta sử dụng **Right Join** thì Streaming Dataframe
    cũng phải nằm ở bên **phải** và bắt buộc phải có Streaming Watermark.
  - Nếu như thực hiện Join giữa hai Streaming Dataframe
    thì phải có Time Range giữa hai Dataframe.
  - Udemy Video: [Streaming Outer Joins](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/22370012#overview)

### Lab9 - Kafka source & join operators exercies

- [Lab 9.1: MultiQueryDemo](https://drive.google.com/file/d/1sg2aVhCiV7PZ6-qKjS8eqDBvbo27EazC/view?usp=sharing)

### Streaming Windowing and Aggregation

#### Stateless and Stateful transformation

- Trong spark hỗ trợ 2 dạng Transformation là: Stateless và Stateful transformation
- State ở đây là 1 nơi lưu trữ các kết quả được xử lý ở batch trước
- Ví dụ:
  - Ta muốn tính tổng chi tiêu của một người vào từng ngày
    sau khi tính ra kết quả cho ngày thứ nhất và sẽ được lưu lại tại State store
  - Sau đó, vào ngày thứ 2 thì chỉ cần cộng các giao dịch trong ngày này với
    kết quả của ngày thứ 1.
- Tuy nhiên, cũng cần lưu ý rằng việc sử dụng Stateful Transformations
  cũng sẽ tốn rất nhiều bộ nhớ, vậy nên ta phải có phương án quản lý, thiết kế
  hợp lý sao cho hệ thống không bị quá tải vào một thời điểm nào đó.
- Udemy: [Stateless và Stateful transformations](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955632#overview)

#### Tumbling Window

- Spark streaming cũng hỗ trợ cơ chế Windowing cho việc tổng hợp, tính toán dữ liệu
  gọi là **Tumbling Window**.
- Cơ chế này sẽ tổng hợp dữ liệu theo các khoảng thời gian (gọi là các Window), và nếu như các dữ liệu có đến muộn thì Spark cũng sẽ cập nhật dữ liệu vào Window tương ứng.
- Ví dụ về kết quả của _Tumbling Window_ như sau:
  +-------------------+-------------------+--------+---------+
  | start| end|TotalBuy|TotalSell|
  +-------------------+-------------------+--------+---------+
  |2019-02-05 10:00:00|2019-02-05 10:15:00| 800| 0|
  |2019-02-05 10:15:00|2019-02-05 10:30:00| 800| 400|
  |2019-02-05 10:30:00|2019-02-05 10:45:00| 900| 0|
  |2019-02-05 10:45:00|2019-02-05 11:00:00| 0| 600|
  +-------------------+-------------------+--------+---------+
- Cơ chế này cũng có một hạn chế, đó là ta chỉ có thể kết hợp dữ liệu
  theo các khoảng thời gian, chứ không thể tổng hợp dât vào các Window cũ
  như sau:
  +---------+----------+--------+
  |RTotalBuy|RTotalSell|NetValue|
  +---------+----------+--------+
  | 800| 0| 800|
  | 1600| 400| 1200|
  | 2500| 400| 2100|
  | 2500| 1000| 1500|
  +---------+----------+--------+
- Udemy video: [Event time và Windowing](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955636#overview)
- Udemy video: [Tumbling Window aggregate](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955638#overview)

#### Watermarking windows

- Kể cả khi dữ liệu đến muộn thì Spark vẫn có thể xử lý do có cơ chế lưu trữ tại
  Stable store. Tuy nhiên, cơ chế này có thể gây ra hao tổn bộ nhớ vậy nên ta
  cũng phải cân nhắc lựa chọn các giải pháp để giải phóng cho Stable Store
  - **Watermark**:
    - Đây là cơ chế tự động dọn dẹp các dữ liệu được coi là "cũ" trong
      Stable store.
    - Tuy nhiên, ta cũng cần phải xem xét kỹ về khoảng thời gian mà dữ liệu
      có thể tồn tại trong Stable Store để tránh tình trạng bị xóa nhầm dữ liệu.
  - **Output mode**:
    - ta nên sử dụng Output mode hợp lý, ví dụ như ở mode "complete" thì
      State Store sẽ phải giữ lại tất cả các dữ liệu, vậy nên ta cần lựa chọn
      Output Mode thật kỹ theo yêu cầu nghiệp vụ.
- Udemy video: [Watermarking windows](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955642#overview)
- Udemy video: [Watermark và output modes](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955648#overview)
- **Tumbling Window** có 1 đặc điểm là các khoảng thời gian sẽ không được đè lên
  nhau. Tuy nhiên, có 1 số trường hợp mà ta cần xử lý các khoảng thời gian đè
  lên nhau, ví dụ như tổng hợp dữ liệu từ các cảm biến và đưa ra kết quả sau mỗi
  5 phút, lúc này ta sẽ cần sử dụng **Sliding Window** thay cho
  **Tumbling Window**. Ví dụ về kết quả như sau:
  ![Tumbling window vs Sliding window](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L14_3.png?alt=media&token=c41f9fbc-142f-4621-ba5c-4ec2911fcd4d)
- Udemy video: [Sliding Window](https://funix.udemy.com/course/spark-streaming-using-python/learn/lecture/21955650#overview)

### Lab 10 - windowing & aggregation exercise

- [Lab 10.1: Tumbling Window Demo](https://drive.google.com/file/d/1q8k6oDiHYR5y9iDtXaGDNAB353gXrqDO/view?usp=sharing)

### Monitoring and Control

#### Spark UI

- Spark cung cấp cho người phát triển Spark UI để nhìn được các thông tin liên
  quan đến chương trình đang chạy và cung cấp các Tab như sau:
  - **Jobs**: hiển thị trạng thái của các Spark Job trong ứng dụng Spark
  - **Stages**: hiển thị trạng thái của các Spark Stage trong ứng dụng Spark
  - **Storage**: hiển thị dung lượng của tất cả các RDD và DataFrame đang được lưu trữ
  - **Environment**: bao gồm mọi biến môi trường và thuộc tính hệ thống cho Spark hoặc JVM
  - **Executor**: hiển thị 1 bản tóm tắt cho thấy việc sử dụng bộ nhớ và đĩa cho bất kỳ Executors nào được sử dụng cho ứng dụng
  - **SQL** hiển thị và hiển thị số liệu cho mỗi truy vấn SQL
- ![Spark UI](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L13_1.png?alt=media&token=8102ca0c-64f1-4d59-b049-57bc949e2ed9)
- Udemy video: [Giới thiệu về Apache Spark User Interface](https://drive.google.com/file/d/12VQEEdapHh8XzQ9Zf8X8vejHBDGEgJee/view)
- Video: [Quản lý các tiến trình](https://drive.google.com/file/d/12UBCeStd_X0txk9nOzGWnfYmIiK_Dl5c/view)

#### Spark trouble shooting

- Khi phát triển ứng dụng Spark, ta có thể gặp các lỗi sau:
  - Lỗi từ User Code: Lỗi liên quan đến các vấn đề từ đoạn code mà ta đã viết
    có thể là lỗi thực thi, lỗi logic,...
  - Lỗi từ các Application Dependency: Lỗi do thiếu các thư viện hoặc
    các thư viện bị lỗi
  - Lỗi do Application Resource: Các lỗi liên quan đến vấn đề về bộ nhớ.
- Video: [Gỡ lỗi các vấn đề về Apache Spark](https://drive.google.com/file/d/12XMo7mPPwQxJWdJL65A7azewFQElNao5/view?t=3)
- Spark cũng hỗ trợ các thiết lập để có thể chỉnh sửa các tài nguyên liên quan đến bộ nhớ và tiến trình để phù hợp với các yêu cầu
- Video: [Tìm hiểu tài nguyên bộ nhớ](https://drive.google.com/file/d/12Ws4glVFxGnPBzyBreVEyspn8tcmk8WL/view?t=9)
- Video: [Tìm hiểu tài nguyên tiến trình](https://drive.google.com/file/d/12T_dP7ZXNleJviDTctY-TP10jK0JuvGH/view)

## Assessment1 - Xây dựng Hệ thống BigData

- Yêu cầu:
  - Import dữ liệu từ dạng file CSV sang MongoDB
  - Sử dụng Spark và đọc dữ liệu từ MongoDB
  - Chuẩn hóa dữ liệu
  - Tính số lần xuất hiện của ngôn ngữ lập trình
  - Tìm các domain được sử dụng nhiều nhất trong các câu hỏi
  - Tính tổng điểm của User theo từng ngày
  - Tính tổng số điểm mà User đạt được trong 1 khoảng thời gian
  - Tìm các câu hỏi có nhiều câu trả lời
  - (\*\*)Tìm các Active User
- Tài nguyên: [Dataset](https://drive.google.com/drive/folders/1uq4TNKlSE-a_UuVSUSidartcUtRGmS30?usp=sharing)
  - **Question.csv**
    - File csv chứa các thông tin liên quan đến câu hỏi của hệ thống, với cấu trúc như sau:
      - _Id_: Id của câu hỏi.
      - _OwnerUserId_: Id của người tạo câu hỏi đó.
        (Nếu giá trị là NA thì tức là không có giá trị này).
      - _CreationDate_: Ngày câu hỏi được tạo.
      - _ClosedDate_: Ngày câu hỏi kết thúc
        (Nếu giá trị là NA thì tức là không có giá trị này).
      - _Score_: Điểm số mà người tạo nhận được từ câu hỏi này.
      - _Title_: Tiêu đề của câu hỏi.
      - _Body_: Nội dung câu hỏi.
  - **Answer.csv**
    - File csv chứa các thông tin liên quan đến câu trả lời và có cấu trúc như sau:
      - _Id_: Id của câu trả lời.
      - _OwnerUserId_: Id của người tạo câu trả lời đó.
        (Nếu giá trị là NA thì tức là không có giá trị này)
      - _CreationDate_: Ngày câu trả lời được tạo.
      - _ParentId_: ID của câu hỏi mà có câu trả lời này.
      - _Score_: Điểm số mà người trả lời nhận được từ câu trả lời này.
      - _Body_: Nội dung câu trả lời.
- Một số tài liệu khác:
  - [Kết nối Pyspark với MongoDB](https://docs.mongodb.com/spark-connector/current/python-api/)
  - [Thao tác đọc/ghi dữ liệu với MongoDB trong PySpark](https://programmer.group/read-and-write-operations-on-mongodb-on-sparksql-python-version.html)
  - [PySpark Dataframe](https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.DataFrame.html)

## Apache Airflow

### Apache Airflow Introduction

#### Airflow Introduction

- Airflow giúp các ta quản lý, lên lịch và thực thi tự động các Data pipeline
  hiệu quả hơn, Data Pipeline của ta có thể bao gồm nhiều thao tác từ
  các hệ thống khác nhau và có thể có rất nhiều Data Pipeline khác nhau
  mà ta cần phải quản lý cùng lúc.
- Như vậy, nếu có một lỗi nào đó xảy ra
  (API không hoạt động, Database không khả dụng)
  cũng sẽ mất rất nhiều thời gian để xử lý.

- Udemy Video: [Tại sao cần phải sử dụng Airflow?](https://funix.udemy.com/course/the-ultimate-hands-on-course-to-master-apache-airflow/learn/lecture/15819404#overview)

- Airflow là một trong những công cụ workflow automation
  và scheduling systems phổ biến nhất.
- Hoặc có thể hiểu rằng Airflow giúp ta thực thi các Task theo đúng cách,
  đúng thời gian và đúng thứ tự.
- Một số ưu điểm của Airflow như sau:

  - **Dynamic**
    Airflow được dựa trên các code Python
    vậy nên trong Python có thể làm gì
    thì ta hoàn toàn có thể làm vậy trong Airflow
    các thao tác sẽ là không giới hạn.
  - **Scalability**:
    ta có thể chạy các Task song song với nhau,
    điều này tùy thuộc vào các tài nguyên tính toán mà ta đang có.
  - **UI**:
    Airflow hỗ trợ giao diện Flask app để quản lý các workflows,
    và giúp ta dễ dàng thay đổi, start và stop.
  - **Extensibility**:
    ta có thể tự tạo các Plugin để có thể
    tương tác với các thành phần khác.

- Trong Airflow có 5 thành phần chính:

  - **Web server**
    Một Flask Server để tạo UI tương tác.
  - **Scheduler**
    Chịu trách nhiệm cho việc lập lịch cho các Task hoặc workflows.
  - **Metastore**
    Một cơ sở dữ liệu (thường là PostgresDB, MySql hoặc SQLLite)
    sử dụng để lưu trữ các Metadata như trạng thái Task, Job, DAG, ...
  - **Executor**
    Mô tả xem các Task của ta sẽ được thực thi như thế nào.
  - **Worker**
    Nơi thực sự thực thi các Task và trả về kết quả.
  - ![core components in airflow](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L14_5.png?alt=media&token=3ead1b51-3026-4ba5-bc12-481ee32af619)

- Airflow quản lý tất cả các jobs bởi DAG
  (directed acyclic graphs/ đồ thị có hướng),
  cho phép quản lý các job dễ hiểu nhất cũng như
  hỗ trợ các workloads phức tạp nhất.
- Udemy Video: [Airflow là gì?](https://funix.udemy.com/course/the-ultimate-hands-on-course-to-master-apache-airflow/learn/lecture/15819406#overview)

- Chúng ta có hai mô hình để triển khai Airflow:

  - **One Node Architecture**:
    Tất cả các thành phần đều nằm chung trên một Node.
    ![One Node Architecture](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L14_5.png?alt=media&token=3ead1b51-3026-4ba5-bc12-481ee32af619)
  - **Multi Node Architecture**:
    Sẽ có những Node chứa các thành phần như Metastore, Webserver,...
    chịu trách nhiệm quản lý các công việc.
    Và sẽ có các Node khác gọi là Worker Node
    chịu trách nhiệm thực thi các công việc đó.
    ![Multi Node Architecture](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L14_6.png?alt=media&token=eb11c02a-08bf-456a-ae39-f9ad0bc6f0b0)

  - Cách thứ 2 sẽ có nhiều ưu điểm hơn do có thể xử lý nhiều Task song song với nhau, tuy nhiên sẽ đòi hòi kiến trúc và triển khai phức tạp hơn.

- Udemy Video: [Airflow hoạt động như thế nào?](https://funix.udemy.com/course/the-ultimate-hands-on-course-to-master-apache-airflow/learn/lecture/15819408#overview)

#### Airflow Installing

- Để cài đặt và bắt đầu sử dụng Airflow,
  ta có thể cài đặt thông qua máy ảo VM.
  Cách cài đặt này có thể sử dụng trên tất cả hệ điều hành như
  Window, Linux và MacOS.
  Hãy tham khảo các tài liệu dưới đây để biết cách cài đặt Airflow:

- Ta sẽ cần sử dụng file .ova của Funix để phù hợp cho các bài thực hành
  cho phần sau,
  ta có thể tải xuống ở [link sau](https://drive.google.com/file/d/1ep8YnyZW49034r-DK5swELkjEj6mZQLu/view?usp=sharing) và import vào Oracle VM VirtualBox.

- Udemy Video: [Cài đặt Airflow 2.0](https://funix.udemy.com/course/the-ultimate-hands-on-course-to-master-apache-airflow/learn/lecture/15819412#overview)

- Airflow cũng cung cấp các CLI để ta có thể tương tác một cách thuận tiện hơn, một số câu lệnh thường dùng như sau:

  - `airflow users creates` :
    Tạo mới một User trong Airflow.
  - `airflow db init` :
    Khởi tạo các thiết lập cho Database của Metastore
    để lưu trữ các thông tin của Airflow,
    ta chỉ cần chạy câu lệnh này vào lần đầu cài đặt.
  - `airflow webserver` :
    Khởi chạy Web Server ở port mặc định là 8080.
  - `airflow scheduler` :
    Khởi chạy Scheduler.
  - `airflow dags list` :
    Liệt kê các DAG hiện có.

- Udemy Video: [Giới thiệu về CLI trong Airlfow 2.0](https://funix.udemy.com/course/the-ultimate-hands-on-course-to-master-apache-airflow/learn/lecture/15819420#overview)

- Ngoài ra, Airflow cũng cung cấp một giao diện giúp ta
  có cái nhìn trực quan hơn về các thông số và dữ liệu.
  Ví dụ như hiển thị các DAG hiện có, trạng thái chạy của các Task, ...

- Video: [GIới thiệu về Airflow UI](https://funix.udemy.com/course/the-ultimate-hands-on-course-to-master-apache-airflow/learn/lecture/15819418#overview)

### Creating Datapipeline with Airflow

#### DAG, Operator, Provider

- Airflow quản lý Data Pipeline dựa trên một đồ thị có hướng hay DAG,
  mỗi một node trên đồ thị này sẽ là một Task cần hoàn thành và
  mỗi cạnh sẽ là sự phụ thuộc giữa các task với nhau.
  Các task sẽ được thực hiện lần lượt theo DAG đã được khai báo.
- Udemy Video: [DAG là gì?](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787768#overview)

- ![data pipeline](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L15_1.png?alt=media&token=2a5357d8-ccf2-4bbb-9957-e58b29941e22)

- Để tạo một DAG, ta có thể sử dụng đoạn code như sau:

  ```python
  default_args = {
      "start_date": datetime(2020, 1, 1)
  }

  with DAG("user_processing",
      default_args=default_args,
      schedule_interval="@daily",
    catchup=False) as dag:
  ```

- Ta sẽ cần khai báo một số thiết lập cho DAG, các thiết lập đó sẽ như sau:
  - `start_date` : Ngày bắt đầu thực hiện DAG.
  - `schedule_interval` : Tần xuất thực hiện DAG.
  - `catchup` : Có thực hiện cơ chế catchup không
    (ta sẽ được học về cơ chế này ở các bài sau).
  - Tên của DAG để phân biệt với các DAG khác.
- Udemy Video: [Cấu trúc của một DAG](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787782#overview)

- **Operator** được sử dụng để định nghĩa một Task trong DAG của ta,
  lưu ý là mỗi Operator chỉ nên định nghĩa một Task duy nhất.
- Có 3 loại Operator như sau:

  - **Action Operators**:
    Operators thực hiện các thao tác,
    hành động như xử lý dữ liệu, gọi API, ...
  - **Transfer Operators**:
    Operators thực hiện các thao tác dịch chuyển dữ liệu,
    ví dụ như đọc / ghi dữ liệu từ Database.
  - **Sensor**:
    Operators thực hiện các thao tác sau khi chờ một
    điều kiện nào đó xảy ra, ví dụ như khi download file
    hoặc khi Database được tạo.

- Udemy Video: [Operator là gì?](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787790#overview)

- Ngoài ra, Airflow có thể thao tác với rất nhiều công cụ khác nhau
  (Spark, AWS, ...) vậy nên Airflow cũng có những Provider,
  đây là những Python Package chứa đầy đủ mọi thứ mà ta cần
  để thao tác với một công cụ cụ thể như Operator, Hook, Database Connection, ...
  và ta sẽ cần cài đặt các Provider này thông qua pip.

- Udemy Video: [Provider](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787804#overview)

#### Initial a DAG

- Các bước tạo một DAG thực hiện quy trình ETL để trích xuất,
  xử lý và lưu trữ các dữ liệu về người dùng được lấy từ các API có sẵn.

- Ở bước đầu tiên,
  ta cần tạo các Table trong Database để có thể sẵn sàng lưu trữ dữ liệu.
  Ta sẽ cần làm theo các bước sau:

  - Tạo connection trong Airflow để kết nối với Database.
  - Sử dụng SQLiteOperator để thực hiện các câu lệnh SQL.
  - Lưu ý video hướng dẫn sẽ sử dụng SQLite để làm Database,
    tuy nhiên ta có thể sử dụng một loại Database khác như MongoDB, SQL Server
    bằng cách đổi các Provider và Operators.
    Tham khảo các Provider của Airflow tại [link sau](https://airflow.apache.org/docs/apache-airflow-providers/packages-ref.html).

  - Udemy Video: [Task: Tạo một Table](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787814#overview)
  - Udemy Video: [Tạo một Connection](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32340586#overview)
  - Udemy Video: [Kiểm tra dữ liệu](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787824#overview)

- Bước tiếp theo là kiểm tra xem API lấy dữ liệu hiện còn hoạt động không,
  ta sẽ cần Sensor để thực hiện Task này.
  Tức là hệ thống sẽ cần chờ đến lúc API hoạt động
  thì mới thực hiện các thao tác tiếp theo.
  Các bước cần phải làm là:

  - Tạo một HTTP Connection đến API trên Webserver.
  - Cài đặt Http Provider để có thể tương tác với các trang web.
  - Tạo một **HttpSensor** để kiểm tra API có hoạt động hay không.
  - Udemy Video: [Giới thiệu về Sensors](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787846#overview)
  - Udemy Video: [Task: Kiểu tra API có hoạt động được không?](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787830#overview)

- Sau khi đã kiểm tra API hoạt động,
  thì chúng ta sẽ đến các bước trích xuất và xử lý dữ liệu.
  Để trích xuất dữ liệu thì chúng ta sẽ cần dùng **SimpleHttpOperator**
  để tạo request lên API và lấy dữ liệu và sau đó sử dụng **PythonOperator**
  để áp dụng các đoạn code Python cho việc xử lý dữ liệu và lưu dưới dạng file csv.

  - Lưu ý: Để đưa dữ liệu từ Task trích xuất vào Task xử lý thì chúng ta sẽ sử dụng XCorn (ta sẽ được giới thiệu rõ hơn về cơ chế này trong các bài sau).
  - Video: [Task: Trích xuất dữ liệu](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787868#overview)
  - Video: [Task: Xử lý dữ liệu](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787876#overview)

- Sau khi lưu dữ liệu,
  bước cuối cùng đó là đưa dữ liệu đã xử lý vào Database.
  Để thực hiện thao tác này, ta cần dùng **BashOperator**
  để thực hiện các câu lệnh bash và đưa dữ liệu từ file .csv vào Database.
  Ngoài ra cũng có một cách khác là sử dụng **SQLiteOperator**
  và viết các truy vấn Insert.

  - Udemy Video: [Giới thiệu về Hook](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787890#overview)
  - Udemy Video: [Task: Lưu trữ dữ liệu](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787896#overview)

- Sau khi đã hoàn thành xong hết các Task
  thì ga sẽ cần sắp xếp lại các Task đó để thực hiện lần lượt theo đúng thứ tự,
  để làm điều này thì ta chỉ cần viết đoạn code sau ở cuối DAG:

  ```
  creating_table >> is_api_available >> extracting_user >> processing_user >> storing_user
  ```

  Đoạn code trên nghĩa là hệ thống sẽ thực lần lượt từ bước `creating_table` đến `storing_user` theo thứ tự bên trên.

  - Udemy Video: [Xử lý một số vấn đề về thứ tự](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787924#overview)
  - Video tham khảo: [Giải thích lại về Data Pipeline vừa tạo](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787940#overview)

- Có một điều cần phải chú ý đó là việc lập lịch cho các DAG.
  Khi tạo DAG thì ta luôn cần khai báo 2 tham số là
  `start_date` và `schedule_interval`.
  Hai tham số này sẽ cho ta biết được lần đầu thi DAG được thực thi
  và các lần thực thi tiếp theo vào các khoảng thời gian nào.

  - Udemy Video: [Lên lịch cho DAG](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787944#overview)

- Trong Airflow có một cơ chế mà ta cần phải chú ý là catchup,
  cơ chế này sẽ chạy những DAG vào các ngày mà chưa được trigger.
  Ví dụ ta có một DAG được bắt đầu từ ngày 01/01/2021 và được lặp lại hàng ngày,
  và vì một vấn đề nào đó mà ta phải dùng DAG này từ ngày 03/01/2021
  và chạy lại từ ngày 05/01/2021.
  Lúc này, ngay sau khi ta chạy lại DAG, thì Airflow sẽ thực hiện cả DAG
  của các ngày 03, 04/01/2021 do vào các ngày này DAG chưa được thực thi.
  Mặc định thì cơ chế này luôn được bật, ta có thể tắt đó bằng các thiết lặp ở
  DAG tham số catchup=False.

- Một lưu ý nữa là Airflow sử dụng UTC Timezone,
  vậy nên ta cũng phải chú ý khi tạo DAG.

- Udemy Video: [Backfilling and catchup](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/32787952#overview)

### Lab11 - Creating data pipline exercises

copy file user_process.py vào thư mục dags của AIRFLOW_HOME

### Paralel Datapipeline running

- Mặc định, các cài đặt của Airflow chỉ cho phép ta thực hiện các Task
  một cách tuần tự, ví dụ ta thiết kế các Task như sau:

  ```
  task_1 >> [task_2, task_3] >> task_4
  ```

  ![flow](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L16_4.png?alt=media&token=100f7cc8-557a-4dde-a8c7-b02d7e2b480c)

- Điều này nghĩa là ta muốn _task_2_ và _task_3_ được thực hiện song song,
  khi cả hai đã thực hiện xong thì sẽ sang _task_4_.
  Tuy nhiên với các cài đặt mặc định
  thì Airflow sẽ chỉ thực hiện tuần tự các task,
  nếu muốn chạy song song thì chúng ta sẽ cần thay đổi các cài đặt đó,
  ![flow](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L16_3.png?alt=media&token=7f535c1e-a642-4cf0-96a5-84ca728814ce)

- Để thay đổi cài đặt và thực hiện các task song song, ta sẽ cần làm các bước sau:

  - **Thay đổi Database Engine**:
    Mặc định thì Airflow sử dụng **SQLite** làm Database Engine,
    tuy nhiên **SQLite** không hỗ trợ đọc/ghi đồng thời,
    vậy nên ta sẽ cần chuyển sang một Database Engine khác
    hỗ trợ cơ chế này như **MySQL** hay **Postgresql** .
  - **Thay đổi Executor**:
    Mặc định thì Airflow sử dụng **SequentialExecutor**
    để thực hiện các Task tuần tự,
    ta sẽ cần đổi thành **LocalExcutor** để các Task có thể
    được thực hiện song song trên máy của ta.
  - Lưu ý, khi chuyển đổi **Database Engine**
    thì ta sẽ cần phải làm lại các bước như init db, tạo user, ...
    ![flow executors](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L16_2.png?alt=media&token=c02e32e2-e31c-4428-9ffa-a2beeff9732c)

- Nếu sử dụng **LocalExcutor** thì toàn bộ các task
  sẽ được chạy trên một máy của ta,
  tuy nhiên nếu ta có hàng nghìn Task cần chạy song song
  thì một máy chắc chắn sẽ không đáp ứng được.
  Vậy nên ta sẽ cần chuyển qua sử dụng **Celery Executor**,
  đây là Executor cho phép các Task được chạy trên các Worker khác nhau.
  Ví dụ ta có một hệ thống với cấu trúc như sau:

  - _Node 1_: Chứa các thành phần như Web Server, Scheduler.
  - _Node 2_: Chứa Metastore lưu trữ các thông tin.
  - _Node 3_: Đây là một ứng dụng khác hoạt động
    như một Queue để sắp xếp thứ tự các Task.
  - _Node 4, 5, 6_: Worker Node sử dụng để thực hiện các Task.

- Sau khi các Task được gửi đến Queue
  thì sẽ được gửi đến các _Worker Node_ để thực thi,
  cơ chế này sẽ giúp cho ta dễ dàng mở rộng theo quy mô hơn
  bằng cách thêm các _Worker Node_ cho hệ thống.
  Đồng thời, các _Worker Node_ cũng có tham số worker*concurrency
  để giới hạn số lượng Task tối đa mà \_Worker Node* có thể thực hiện cùng một lúc,
  ta cũng có thể mở rộng bằng việc tăng thêm số này lên.

- Airflow cũng cung cấp một số thông số mà ta có thể thiết lập
  để thiết kế hệ thống phù hợp với cơ sở hạ tầng hiện có và các yêu cầu
  cần thiết như sau:

  - `parallelism` : Số lượng Task tối đa có thể thực thi đồng thời
    trên toàn bộ hệ thống Airflow của ta.
  - `dag_concurrency` : Số lượng Task tối đa có thể thực thi đồng thời
    trên mỗi DAG. Tham số này cũng có thể được thiết lập trong từng DAG riêng biệt.
  - `max_active_runs_per_dag` : Số lượng DAG tối đa có thể chạy cùng một lúc.
    Tham số này cũng có thể được thiết lập trong từng DAG riêng biệt.
  - ta có thể tham khảo thêm các thông số khác tại [link sau](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html).

### Lab12 - Parallel Data pipeline exercises

- udemy video reference: [Mở rộng với Local Executor](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/11999776#overview)
- copy file parallel_tasks.py vào thư mục dags của AIRFLOW_HOME

### Advance definitions in Apache Airflow

#### SubDAGs and Tag Group

- Thực tế, DAG của bạn sẽ gồm rất nhiều Task có thể
  thực thi song song cùng nhau, làm cho DAG trở nên rất phức tạp vào khó quản lý.
  Ví dụ chúng ta có một DAG như sau:
  ![Graph view](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L17_2.png?alt=media&token=2384f3a6-ef76-4fc7-8c27-cb134a5afbf2)

- Để quản lý các Task này dễ dàng hơn thì bạn có thể sử dụng hai cơ chế
  là **SubDAGs** và **TaskGroups**.

- Udemy Video: [Adios repetitive patterns](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/11999870#overview)

- SubDAGs là cách mà bạn tạo ra một DAG con và kích hoạt nó từ một DAG cha, ví dụ:

  ```python
  def load_subdag(parent_dag_name, child_dag_name, args):
      dag_subdag = DAG(
          dag_id='{0}.{1}'.format(parent_dag_name, child_dag_name),
          default_args=args,
          schedule_interval="@daily",
      )
      with dag_subdag:
          for i in range(5):
              t = DummyOperator(
                  task_id='load_subdag_{0}'.format(i),
                  default_args=args,
                  dag=dag_subdag,
              )

      return dag_subdag
  ```

  Từ đoạn code trên, bạn đã tạo ra một DAG con để thực hiện các thao tác Load dữ liệu, để sử dụng trong DAG cha thì bạn có thể làm như sau:

  ```python
  load_tasks = SubDagOperator(
      task_id="load_tasks",
      subdag=load_subdag(
          parent_dag_name="example_subdag_operator",
          child_dag_name="load_tasks",
          args=default_args
      ),
      default_args=default_args,
      dag=dag,
  )
  ```

  Và khi đó DAG của bạn sẽ trở thành như thế này:
  ![DAG](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L17_1.png?alt=media&token=432b5384-a4f0-4a59-a9a0-c8391de5c9d2)

- Một số lưu ý khi sử dụng SubDAGs như sau:

  - Tên của các SubDAGs phải theo đúng định dạng `parent.child`,
    ví dụ: `example_subdag_operator.load_tasks`
  - Trạng thái của SubDAGs và các Task trong đó là độc lập với nhau.
  - SubDAG có thể được lên lịch giống với DAG cha.
  - Các Task trong SubDAG sẽ chỉ có thể được thực hiện tuần tự.
  - Video: [Giảm thiểu DAG với SubDAGs](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/11999876#overview)

- Có thể thấy việc sử dụng SubDAG sẽ làm tăng độ phức tạp của Data Pipeline
  của chúng ta lên rất nhiều do bạn phải tạo một DAG mới,
  chú ý về cách đặt tên, cách sử dụng,...
  Vì vậy nên ở Airflow 2.0 chúng ta có một cơ chế mới là TaskGroups.
  Cơ chế này sẽ giúp gộp nhóm các Task lại để dễ dàng trực quan hóa hơn
  khi nhìn ở WebServer nhưng bản chất vẫn chỉ nằm trên cùng 1 DAG,
  như vậy có thể giải quyết được các vấn đề kể trên. Ví dụ:

  ```python
  t0 = DummyOperator(task_id='start')

  # Start Task Group definition
  with TaskGroup(group_id='group1') as tg1:
      t1 = DummyOperator(task_id='task1')
      t2 = DummyOperator(task_id='task2')

      t1 >> t2
  # End Task Group definition

  t3 = DummyOperator(task_id='end')

  # Set Task Group's (tg1) dependencies
  t0 >> tg1 >> t3
  ```

- Và chúng ta có thể nhìn trên Webserver như sau:
  ![airflow webserver](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L17_3.gif?alt=media&token=36f4f5ef-3b2d-452b-9020-8567aa2f9871)

- Udemy Video: [Adios SubDAGs and TaskGroups!](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/33546490#overview)

#### XComs Usage

- **XComs** là một cơ chế giúp cho các Task có thể chia sẻ dữ liệu với nhau
  dựa theo cơ chế Push/Pull, tức là Task nào muốn truyền dữ liệu
  sẽ Push dữ liệu đó lên xComs và Task nhận dữ liệu sẽ Pull về,
  XComs sẽ giống như một nơi trung gian lưu trữ.
  XComs sẽ nhận dạng các dữ liệu theo key (thường sẽ là tên của biến đó)
  và đồng thời cũng sử dụng task_id và dag_id mà dữ liệu được Push lên.
  ![xComs overview](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FSumary_Image%2FDEP303_sum_L17_4.png?alt=media&token=17c6dabe-bfe0-4040-949d-692093b3681f)

- XComs có thể chứa bất kỳ giá trị nào (có thể tuần tự hóa),
  nhưng XComs chỉ được thiết kế cho một lượng nhỏ dữ liệu;
  không sử dụng cho các giá trị lớn, như Dataframe.
  Tùy thuộc vào Database Engine đang sử dụng mà XComs sẽ có dung lượng khác nhau,
  vậy nên bạn cần phải tính toán kỹ để lựa chọn Database Engine.

- Udemy Video: [Chia sẻ dữ liệu giữa các Task với XComs](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/12000706#overview)
- Udemy Video: [Thực hành: Sử dụng XComs](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/12000710#overview)

#### Task activating following condition

- Đôi khi, ta sẽ cần phải thực hiện các Task khác nhau
  trong các trường hợp khác nhau. Ví dụ như nếu file chưa tồn tại
  thì sẽ thực thi Task _download_file_, còn nếu file đã tồn tại thì
  sẽ thực hiện Task _process_file_. Để làm được thao tác này,
  ta sẽ cần sử dụng **BranchPythonOperator**,
  đây là một Operators tương tự với **PythonOperator**,
  sẽ nhận vào một Python Function và sau khi thực thi
  thì trả về _task_id_ của Task sẽ thực hiện tiếp theo. Ví dụ:

  ```python
  def branch_file_exist():
    if os.path.exists(path):
      return 'process_file'
    return 'download_file'

  branching = BranchPythonOperator(
    task_id='branching',
    python_callable=branch_file_exist,
    provide_context=True,
    dag=dag
  )
  ```

- Udemy Video: [Lựa chọn đường dẫn cụ thể cho DAG](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/12000686#overview)
- Udemy Video: [Thực hiện Task dựa trên một điều kiện](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/12000692#overview)

- Khi thực hiện các Task song song, mặc định sau khi các Task đều hoàn tất
  thì mới thực thi Task tiếp theo. Đây được gọi là Trigger Rule của Task,
  và ta có thể thay đổi Trigger Rule này để phù hợp viết yêu cầu thực tế hơn.
  Có các loại Trigger Rule như sau:

  - **all_success**: Các Task chia đều thực thi thành công.
  - **all_failed**: Các Task chia đều thực thi không thành công.
  - **all_done**: Các Task chia đều thực thi xong.
  - **one_failed**: Một trong các Task cha thực thi không thành công.
  - **one_success**: Một trong các Task cha thực thi thành công.
  - **none_failed**: Các Task cha không có cái nào bị failed.
  - **none_skipped**: Các Task cha không có cái nào bị skipped.

- Udemy Video: [Quy tắc kích hoạt và cách để kích hoạt một Task](https://funix.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/learn/lecture/13704146#overview)

### Lab13 - Branching in Airflow exercise

- copy file branching_weekday.py vào thư mục dags của AIRFLOW_HOME

## Assessment 2 - Thiết lập DataPipeline cho dữ liệu lớn từ Cloud

- Một Data Pipeline hoàn chỉnh để có thể làm các thao tác như:
  - Tải tập dữ liệu,
  - Import tập dữ liệu vào Database
  - Xử lý dữ liệu với Spark.
- Sản phẩm sẽ là một Data Pipeline có các bước như sau:
  ![project flow](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP303x%2FASM_Image%2FDEP303_ASM_2_1.png?alt=media&token=16304b2f-6bd3-4808-93df-458d5b73b914)
- Tài nguyên: [Dataset](https://drive.google.com/drive/folders/1uq4TNKlSE-a_UuVSUSidartcUtRGmS30?usp=sharing)
  - **Question.csv**
    - File csv chứa các thông tin liên quan đến câu hỏi của hệ thống, với cấu trúc như sau:
      - _Id_: Id của câu hỏi.
      - _OwnerUserId_: Id của người tạo câu hỏi đó.
        (Nếu giá trị là NA thì tức là không có giá trị này).
      - _CreationDate_: Ngày câu hỏi được tạo.
      - _ClosedDate_: Ngày câu hỏi kết thúc
        (Nếu giá trị là NA thì tức là không có giá trị này).
      - _Score_: Điểm số mà người tạo nhận được từ câu hỏi này.
      - _Title_: Tiêu đề của câu hỏi.
      - _Body_: Nội dung câu hỏi.
  - **Answer.csv**
    - File csv chứa các thông tin liên quan đến câu trả lời và có cấu trúc như sau:
      - _Id_: Id của câu trả lời.
      - _OwnerUserId_: Id của người tạo câu trả lời đó.
        (Nếu giá trị là NA thì tức là không có giá trị này)
      - _CreationDate_: Ngày câu trả lời được tạo.
      - _ParentId_: ID của câu hỏi mà có câu trả lời này.
      - _Score_: Điểm số mà người trả lời nhận được từ câu trả lời này.
      - _Body_: Nội dung câu trả lời.
- Một số tài liệu bạn có thể tham khảo để hoàn thành bài tập:
  - [DummyOperator](https://python.hotexamples.com/examples/airflow.operators/DummyOperator/-/python-dummyoperator-class-examples.htmlhttps://registry.astronomer.io/providers/apache-airflow/modules/dummyoperator)
  - [BranchPythonOperator](https://registry.astronomer.io/providers/apache-airflow/modules/branchpythonoperator)
  - [BashOperator](https://registry.astronomer.io/providers/apache-airflow/modules/bashoperator)
  - [PythonOperator](https://registry.astronomer.io/providers/apache-airflow/modules/pythonoperator)
  - [SparkSubmitOperator](https://registry.astronomer.io/providers/spark/modules/sparksubmitoperator)

## Review Lab

Các thứ cần ready trước khi vào buổi review

- Lab 1-Lab 7: Google Colab
- Lab 8-Lab 10: MongoDB, WSL: Spark, Kafka
- Lab 11-Lab 13: WSL: Venv, Airflow (scheduler+webserver, celery worker/flower)
