# Amazon Web Service

## Labs & assignments

- [Lab 1](#lab-1) - done 1 demonstrate
- [Lab 2](#lab-2) - done
- [Lab 3](#lab-3) - done both 1 demonstrate, 1 lab
- [Lab 4](#lab-4) - done 2 labs
- [Lab 5](#lab-5) - done 2 activities
- [Lab 6](#lab-6) - done
- [Lab 7](#lab-7) - done 2 demonstrate
- [Lab 8](#lab-8) - done
- [Assignment 1](#assessment-1-auto-scaling-application-on-ec2-for-webserver)
- [Lab 9](#lab-9) - done
- [Lab 10](#lab-10-redshift-cluster) - done
- [Assignment 2](#assessment-2-build-up-database-for-google-play-store)
- [Assignment 3](#assessment-3-integrate-media-store-on-aws-redshift)

## Welcome to AWS

### Overall about Cloud and AWS

#### Cloud overall

1. Bài giảng đầu tiên sẽ giới thiệu về điện toán đám mây,
   là sự phân phối theo yêu cầu về tài nguyên của máy tính,
   cơ sở dữ liệu, lưu trữ, các ứng dụng và các tài nguyên khác
   thông qua Internet với hình thức chỉ thanh toán chi phí
   cho những gì ta sử dụng (pay-as-you-go pricing).

   - Điện toán đám mây cho phép ta ngừng suy nghĩ về hệ thống
     của mình như một hardware, và thay vào đó, hãy nghĩ hạ tầng
     như một software, **Infrastructure as a Service**.
   - Có ba mô hình dịch vụ đám mây chính **SaaS**, **IaaS**, **Paas**.
     Mỗi mô hình đại diện cho một phần khác nhau của nền tảng điện toán đám mây
     và cung cấp cho ta một mức độ kiểm soát khác nhau đối với tài nguyên của ta.
   - Và cũng có ba _mô hình triển khai điện toán đám mây_ chính là **Cloud**,
     **Hydrid** và **On-premises**, đại diện cho các môi trường đám mây
     mà các ứng dụng của ta có thể được triển khai.
   - Các điểm tương đồng giữa _AWS và mô hình truyền thống_ như
     **AWS Security Group**, **AWS IAM**, **Network ACLs** thì tương đồng với
     **Firewalls**, **Administrator** và **Access Control Lists**.
   - Video: [Giới thiệu về Cloud Computing](https://awsacademy.instructure.com/courses/77750/modules/items/7000768)

2. Trong bài giảng tiếp theo, chúng ta sẽ tìm hiểu
   về các Ưu điểm của điện toán đám mây.

   - **Chi phí vốn thương mại cho chi phí biến đổi**:
     Chi phí vốn hay chi phí tài sản cố định (capex)
     là khoản tiền mà một công ty sử dụng để mua, nâng cấp và duy trì
     các tài sản vật chất như tài sản, văn phòng hoặc thiết bị.
     Ta có nhớ ví dụ về trung tâm dữ liệu trong mô hình truyền thống
     nơi ta cần xếp và xếp chồng phần cứng, sau đó quản lý tất cả không?
     Ta phải trả tiền cho mọi thứ trong trung tâm dữ liệu
     cho dù ta có sử dụng nó hay không.
   - **Hưởng lợi từ quy mô kinh tế lớn**:
     Bằng cách sử dụng điện toán đám mây, ta có thể đạt được mức chi phí biến đổi
     thấp hơn mức ta có thể tự kiếm được. Vì lượng khách hàng trên dịch vụ đám mây
     lên đến hàng trăm nghìn, các nhà cung cấp như AWS có thể đạt được quy mô
     kinh tế lớn hơn, điều này dẫn đến giá thành (pay-as-you-go) sẽ thấp hơn.
   - **Không phải dự đoán công suất của hạ tầng**:
     Không cần phỏng đoán về nhu cầu cơ sở hạ tầng của ta.
     Khi ta đưa ra quyết định về dung lượng trước khi triển khai ứng dụng,
     ta thường có các nguồn tài nguyên không sử dụng đắt đỏ
     hoặc lại phải đối mặt với vấn đề tài nguyên hạn chế.
     Với điện toán đám mây, những vấn đề này sẽ biến mất.
     Ta có thể truy cập nhiều hay ít tùy theo nhu cầu và tăng giảm quy mô
     theo yêu cầu chỉ với một vài phút thông báo.
   - **Tăng tốc độ và tính nhanh gọn**:
     Trong môi trường điện toán đám mây, các tài nguyên được tạo mới
     chỉ cách một cú nhấp chuột, có nghĩa là ta giảm thời gian cung cấp
     các tài nguyên đó cho các nhà phát triển của mình
     từ vài tuần xuống chỉ vài phút.
     Kết quả là sự nhanh nhạy của tổ chức tăng lên đáng kể
     vì chi phí và thời gian để thử nghiệm và phát triển thấp hơn đáng kể.
   - **Không phải chi tiền vào việc vận hành và duy trì các trung tâm dữ liệu**:
     Tập trung vào các dự án tạo sự khác biệt cho doanh nghiệp của ta
     thay vì tập trung vào cơ sở hạ tầng. Điện toán đám mây cho phép ta
     tập trung vào khách hàng của chính mình thay vì các máy chủ xếp chồng,
     xếp chồng và cấp nguồn nặng nề.
   - **Truy cập toàn cầu trong vài phút**:
     Ta có thể triển khai ứng dụng của mình trong nhiều AWS Regions
     trên khắp thế giới chỉ với một vài cú nhấp chuột.
     Do đó, ta có thể cung cấp độ trễ thấp hơn và trải nghiệm tốt hơn
     cho khách hàng của mình một cách đơn giản và với chi phí tối thiểu
   - Video: [Ưu điểm của Cloud](https://awsacademy.instructure.com/courses/77750/modules/items/7000770)

3. Sau bài giảng này, chúng ta sẽ hiểu được:

   - Một **Web Service** là bất kỳ thành phần của phần mềm nào giúp nó
     khả dụng trên Internet hoặc trên các mạng riêng (mạng nội bộ).
     Web Service sử dụng định dạng chuẩn hóa chẳng hạn như XML hoặc JSON
     cho yêu cầu và phản hồi của API. Nó không bị ràng buộc với bất kỳ
     một hệ điều hành hoặc ngôn ngữ lập trình nào.
     Nó tự mô tả thông qua tệp định nghĩa giao diện và nó có thể khám phá được.
   - **Amazon Web Services (AWS)** là một nền tảng đám mây an toàn
     cung cấp một loạt các sản phẩm dựa trên đám mây toàn cầu.
     Bởi vì các sản phẩm này được phân phối qua Internet,
     ta có quyền truy cập theo yêu cầu vào máy tính, lưu trữ, mạng, cơ sở dữ liệu
     và các tài nguyên khác mà ta có thể cần cho các dự án của mình
     và các công cụ để quản lý chúng.
     Ta có thể cung cấp và khởi chạy tài nguyên AWS ngay lập tức.
     Các tài nguyên đã sẵn sàng để ta sử dụng trong vài phút.
   - Ta có thể tự hỏi **làm thế nào để truy cập** vào một loạt các dịch vụ
     được cung cấp bởi AWS.
     Có ba cách để tạo và quản lý tài nguyên trên Đám mây AWS:
     - **AWS Management Console**:
       Bảng điều khiển cung cấp giao diện đồ họa phong phú cho phần lớn
       các tính năng do AWS cung cấp.
       (Lưu ý: Đôi khi, các tính năng mới có thể không có tất cả các khả năng
       của chúng trong bảng điều khiển khi tính năng này khởi chạy lần đầu.)
     - **AWS Command Line Interface (AWS CLI)**:
       AWS CLI cung cấp một bộ tiện ích có thể được khởi chạy từ tập lệnh
       trong Linux, macOS hoặc Microsoft Windows.
     - **Software Development Kits (SDK)**:
       AWS cung cấp các gói cho phép truy cập AWS
       bằng nhiều ngôn ngữ lập trình phổ biến.
       Điều này giúp ta dễ dàng sử dụng AWS trong các ứng dụng hiện có của mình
       và nó cũng cho phép ta tạo các ứng dụng triển khai
       và giám sát các hệ thống phức tạp hoàn toàn thông qua mã.
   - Tất cả ba tùy chọn đều được xây dựng trên một REST API,
     đóng vai trò là nền tảng của AWS. Nếu muốn tìm hiểu thêm về nội dung này,
     ta có thể tham khảo trong mục Tài liệu tham khảo.
   - Video: [Giới thiệu về AWS](https://awsacademy.instructure.com/courses/77750/modules/items/7000772)

4. Video cuối của bài học giúp ta biết về:

   - **AWS CAF (AWS Cloud Adoption Framework)**, cung cấp hướng dẫn
     và các phương pháp hay nhất để giúp các tổ chức xác định
     những lỗ hổng trong kỹ năng và quy trình.
     Nó cũng giúp các tổ chức xây dựng một cách tiếp cận toàn diện
     đối với điện toán đám mây trên toàn bộ tổ chức và trong suốt vòng đời
     của CNTT để đẩy nhanh việc áp dụng điện toán đám mây thành công.
   - AWS CAF tổ chức hướng dẫn thành 6 lĩnh vực trọng tâm, được gọi là quan điểm.
     Các quan điểm bao gồm **con người**, **quy trình** và **công nghệ**.
     Mỗi quan điểm bao gồm một tập hợp các khả năng,
     bao gồm các trách nhiệm riêng biệt được sở hữu
     hoặc quản lý bởi các bên liên quan có chức năng.
   - Video: [Dịch chuyển dịch vụ lên AWS](https://awsacademy.instructure.com/courses/77750/modules/items/7000775)

#### AWS structure overall

1.  Trong bài học này, video đầu tiên sẽ giúp ta có được cái nhìn tổng quan
    về high-level Global Infrastructure của AWS.

    - Chúng ta sẽ đi qua các định nghĩa cơ bản nhất của AWS như:

      - **Region** là một vị trí địa lý thực tế,
        mỗi region cung cấp đầy đủ dự phòng và kết nối mạng,
        một region thường bao gồm nhiều Availability Zone (AZ).
      - **Availability Zone** cung cấp
        khả năng vận hành các ứng dụng và cơ sở dữ liệu có tính khả dụng cao,
        khả năng chịu lỗi và khả năng mở rộng cao hơn so với khả năng có thể có
        với một trung tâm dữ liệu riêng lẻ.
        Mỗi AZ có thể _bao gồm nhiều Data Center_ (thường là 3) và ở quy mô đầy đủ,
        chúng có thể bao gồm hàng trăm nghìn máy chủ.
        Chúng là các phân vùng hoàn toàn biệt lập của cơ sở hạ tầng
        toàn cầu của AWS.
        Các AZ có cơ sở hạ tầng điện riêng và chúng cách nhau nhiều km
        về mặt vật lý từ các AZ khác.
      - Nền tảng cho cơ sở hạ tầng AWS là các trung tâm dữ liệu **Data Center**.
        Khách hàng không cần chỉ định một trung tâm dữ liệu
        khi triển khai các tài nguyên. Thay vào đó, AZ là cấp đặc điểm kỹ thuật
        chi tiết nhất mà khách hàng có thể chỉ định.
        Tuy nhiên, trung tâm dữ liệu là nơi chứa dữ liệu thực tế.
        Amazon vận hành các trung tâm dữ liệu hiện đại, có tính khả dụng cao.
      - **AWS Points of Presence** có mặt tại hầu hết các thành phố lớn
        (tổng cộng 69 thành phố) trên 30 quốc gia trên thế giới.
        Bằng cách liên tục đo lường kết nối internet, hiệu suất và tính toán
        để tìm ra cách tốt nhất để định tuyến các yêu cầu,
        Points of Presence mang đến trải nghiệm người dùng
        gần như thời gian thực tốt hơn.
        Chúng được nhiều dịch vụ AWS sử dụng, bao gồm các dịch vụ
        Amazon CloudFront, Amazon Route 53, AWS Shield
        và AWS Web Application Firewall (AWS WAF).

    - Cơ sở hạ tầng toàn cầu AWS có một số đặc điểm như sau:

      - Đầu tiên là đặc tính đàn hồi và khả năng mở rộng.
        Điều này có nghĩa là các nguồn lực có thể tự động điều chỉnh
        để tăng hoặc giảm các yêu cầu về dung lượng.
        Nó cũng có thể nhanh chóng điều chỉnh để thích ứng với sự phát triển.
      - Thứ hai, cơ sở hạ tầng này mặc định có khả năng chịu lỗi,
        có nghĩa là nó có dự phòng thành phần tích hợp cho phép
        nó tiếp tục hoạt động mặc dù một thành phần bị lỗi.
      - Cuối cùng, cơ sở hạ tầng toàn cầu AWS yêu cầu ở mức tối thiểu
        hoặc không có sự can thiệp của con người, trong khi
        cung cấp tính khả dụng cao với thời gian ngừng hoạt động thấp nhất.

    - Video: [Kiến trúc tổng quan về AWS](https://awsacademy.instructure.com/courses/77750/modules/items/7000812)

2.  Như ở video trên đã đề cập, cơ sở hạ tầng toàn cầu của AWS
    có thể được chia thành ba yếu tố:
    Regions, Availability Zone, and Points of Presence.
    Cơ sở hạ tầng này cung cấp nền tảng cho một loạt các Service,
    trong đó bao gồm **3 Service cơ bản** như Networking, Storage, Compute
    và các dịch vụ này được phân phối dưới dạng tiện ích theo yêu cầu,
    khả dụng trong vài giây.

    - AWS cung cấp một loạt các dịch vụ.
      Có 23 danh mục sản phẩm hoặc có thể gọi là **Service Categories**
      và mỗi danh mục bao gồm một hoặc nhiều Service.
      Khóa học này sẽ không cố gắng giới thiệu cho ta từng Service.
      Thay vào đó, khóa học sẽ đặt trọng tâm vào các dịch vụ
      được sử dụng rộng rãi nhất và giới thiệu tốt nhất về AWS.
      Chúng ta có thể tìm hiểu thêm về các sản phẩm khác của AWS
      trong mục Tài liệu tham khảo.
      - **AWS Storage Service Category**
        bao gồm các dịch vụ được liệt kê ở đây và nhiều dịch vụ khác:
        Amazon S3, Amazon EBS, Amazon EFS, Amazon S3 Glacier.
      - **AWS Compute Service Category**
        bao gồm các dịch vụ được liệt kê ở đây và nhiều dịch vụ khác:
        Amazon EC2, Amazon EC2 Auto Scaling, Amazon ECS, Amazon ECR,
        AWS Elastic Beanstalk, AWS Lambda, Amazon EKS, AWS Fargate.
      - **AWS Database Service Category**
        bao gồm các dịch vụ được liệt kê ở đây và nhiều dịch vụ khác:
        Amazon RDS, Amazon Aurora, Amazon Redshift, Amazon DynamoDB.
      - **AWS Networking Service Category**
        bao gồm các dịch vụ được liệt kê ở đây và nhiều dịch vụ khác:
        Amazon VPC, ELB, Amazon CloudFront, AWS Transit Gateway,
        Amazon Route 53, AWS Direct Connect, AWS VPN.
      - **AWS Security, Identity và Compliance Service Category**
        bao gồm các dịch vụ được liệt kê ở đây và nhiều dịch vụ khác:
        AWS IAM, AWS Organizations, Amazon Cognito, AWS Artifact,
        AWS KMS, AWS Shield.
      - **AWS Cost Management Service Category**
        bao gồm các dịch vụ được liệt kê ở đây và nhiều dịch vụ khác:
        AWS Cost and Usage Report, AWS Budgets, AWS Cost Explorer.
      - **AWS Management và Governance Service Category**
        bao gồm các dịch vụ được liệt kê ở đây và nhiều dịch vụ khác:
        AWS Management Console, AWS Config, Amazon CloudWatch, AWS Auto Scaling,
        AWS CLI, AWS Trusted Advisor, AWS Well-Architected Tool, AWS CloudTrail.
    - Video: [Các dịch vụ và phân loại dịch vụ AWS](https://awsacademy.instructure.com/courses/77750/modules/items/7000814)

#### Creating account on AWS

- Tài khoản chính (root account) là một tài khoản có quyền cao nhất
  khi mà ta sử dụng các dịch vụ trên AWS. Root account có thể cấp phát quyền
  cho các tài khoản khác, khởi tạo không giới hạn các dạng tài nguyên
  có trên hệ thống AWS.
  Vậy làm thế nào để chúng ta có thể có được một tài khoản như thế.?
  Chúng ta có thể làm theo một số bước sau:

- Ta có thể truy cập vào trang chủ của AWS tại [link sau](https://aws.amazon.com/)
  và chọn " Create an AWS Account" để bắt đầu tạo tài khoản
  và nhập các thông tin dưới đây:

  - Email ta sẽ sử dụng cho Root Account, một số thông tin cá nhân cơ bản.
  - Điền đầy đủ thông tin thanh toán cho tài khoản của ta
    (địa chỉ hoá đơn, thông tin của visa/ credit card của ta)
  - Xác thực số điện thoại của ta hợp lệ bằng một cuộc gọi từ AWS,
    nhập số PIN được đề cập trong cuộc điện thoại đó.
  - Xác nhận lại tất cả các thông tin phía bên trên của ta
    và việc tạo tài khoản trên web AWS.

- Sau đó, ta đã tạo được 1 tài khoản trên AWS và có thể tham gia
  vào Free Tier trong vòng một năm kể từ lúc lập tài khoản đó.

- Tài liệu tham khảo: [Create and activate new AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/).
  (xem bản dịch hỗ trợ [tại đây](https://drive.google.com/file/d/17IKC4_j_4rx75xbEArhm3gEjz5I4oWch/view))

- Lưu ý:

  - Ta cần phải có **visa/credit card** để có thể tạo được tài khoản,
    AWS sẽ không trừ tiền trong tài khoản của ta cho tới khi
    ta sử dụng vượt quá dung lượng tài nguyên miễn phí hàng tháng
    mà AWS đã quy định trong mỗi account.
  - Tài khoản AWS này sẽ được sử dụng để làm một số bài Lab và Assignment
    trong môn học này.
  - **Để không gặp vấn đề về việc thanh toán,
    thẻ của ta chỉ nên duy trì 2$ trong tài khoản
    bởi nếu trong quá trình sử dụng service hệ thống có tính phí
    thì ta sẽ không bị trừ đi quá nhiều tiền.**

#### References

- Các tài liệu dưới đây giúp ta xem và hiểu rõ hơn khi gặp
  các vấn đề cụ thể liên quan đến Cloud Computing và AWS:

  - [Khái niệm tổng quan về Cloud](https://drive.google.com/file/d/1aTMzOjZURYfTXsFscnbUUSyPxFoeIgb2/view)
  - [Tools to Build on AWS](https://aws.amazon.com/tools/)
  - [Kiến trúc tổng quan về AWS](https://drive.google.com/file/d/1gGFdBTetPWaBP_ay_lTXAN-1RRsMFDJq/view)
  - [AWS Global infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
  - [AWS Cloud Product](https://aws.amazon.com/products/)

### Cloud economics and payment

#### Overall

- **Mô hình giá cả AWS**:
  Có ba đối tượng cơ bản khi tính chi phí với AWS:
  _Compute_, _Storage_, and _Outbound Data Transfer_.
  Những đặc điểm này hơi khác nhau, tùy thuộc vào sản phẩm AWS
  và mô hình giá cả mà ta chọn.
- **Phương thức thanh toán cho AWS**,
  AWS cung cấp một loạt các dịch vụ điện toán đám mây.
  Đối với mỗi dịch vụ, ta phải trả cho chính xác số lượng tài nguyên
  mà ta thực sự cần. Mô hình định giá kiểu tiện ích này bao gồm:
  - Thanh toán cho những gì ta sử dụng
  - Trả ít hơn khi ta đặt trước
  - Trả ít hơn khi ta sử dụng nhiều hơn
  - Trả ít hơn khi AWS phát triển
- **AWS Free Tier**: Để giúp khách hàng AWS mới bắt đầu sử dụng đám mây,
  AWS cung cấp cấp sử dụng miễn phí (AWS Free Tier)
  cho khách hàng mới trong tối đa 1 năm.
  AWS Free Tier áp dụng cho một số dịch vụ và tùy chọn nhất định.
  Nếu ta là khách hàng AWS mới, ta có thể chạy miễn phí các service
  của Amazon Elastic Compute Cloud (Amazon EC2) T2 trong một năm,
  đồng thời sử dụng AWS Free Tier cho Amazon S3,
  Amazon Elastic Block Store (Amazon EBS), Elastic Load Balancing ,
  AWS data transfer và các dịch vụ AWS khác.
  Ta có thể tìm hiểu thêm về nội dung này ở mục Tài liệu tham khảo.
- **Các Service miễn phí**:
  - Amazon Virtual Private Cloud (Amazon VPC)
  - AWS Identity and Access Management (IAM)
  - Consolidated Billing
  - AWS Elastic Beanstalk
  - AWS CloudFormation
  - Automatic Scaling
  - AWS OpsWorks.
- Video: [Các nguyên tắc cơ bản về định giá](https://awsacademy.instructure.com/courses/77750/modules/items/7000787)

#### Better option between On-premises and Cloud

- **Định nghĩa TCO**:
  Tổng chi phí sở hữu (Total Cost of Ownership - TCO)
  là một ước tính tài chính nhằm giúp người mua và chủ sở hữu
  xác định chi phí trực tiếp và gián tiếp của một sản phẩm hoặc hệ thống.
  TCO bao gồm chi phí của một dịch vụ, cộng với tất cả các chi phí liên quan
  đến việc sở hữu dịch vụ.
- **Các cân nhắc của TCO**,
  một số chi phí liên quan đến quản lý trung tâm dữ liệu bao gồm:
  - Chi phí máy chủ cho cả phần cứng và phần mềm,
    và chi phí cơ sở vật chất để chứa thiết bị
  - Chi phí lưu trữ cho phần cứng, quản trị và cơ sở vật chất
  - Chi phí mạng cho phần cứng, quản trị và cơ sở vật chất
  - Và chi phí lao động CNTT được yêu cầu để quản lý toàn bộ giải pháp
- AWS cung cấp **AWS Pricing Calculator**
  để giúp ta ước tính hóa đơn AWS hàng tháng,
  ta có thể tìm hiểu về công cụ này ở mục Tài liệu tham khảo.
  Trong đó, AWS Pricing Calculator giúp ta:
  - Ước tính chi phí hàng tháng của các dịch vụ AWS
  - Xác định các cơ hội để giảm chi phí
  - Lập mô hình các giải pháp của ta trước khi xây dựng chúng
  - Khám phá các điểm giá và tính toán đằng sau ước tính của ta
  - Tìm các loại phiên bản có sẵn và các điều khoản hợp đồng
    đáp ứng nhu cầu của ta
- Video: [Tổng chi phí sở hữu](https://awsacademy.instructure.com/courses/77750/modules/items/7000788)

#### Case study

- Các nội dung của bài giảng sẽ được trình bày thông qua Case Study
  cho ta hiểu rõ hơn về TCO.
- Video: [Ví dụ](https://awsacademy.instructure.com/courses/77750/modules/items/7000790)

#### AWS Organizations

- **AWS Organizations**
  là một dịch vụ quản lý tài khoản miễn phí cho phép ta hợp nhất nhiều tài khoản
  AWS thành một Organization riêng mà ta tạo và quản lý tập trung.
  AWS Organizations bao gồm các khả năng quản lý tài khoản và thanh toán tổng hợp
  giúp ta đáp ứng tốt hơn các nhu cầu về ngân sách,
  bảo mật và tuân thủ của doanh nghiệp mình.
- Các **lợi ích chính** của AWS Organizations là:
  - Chính sách truy cập được quản lý tập trung trên nhiều tài khoản AWS
  - Quyền truy cập có kiểm soát vào các dịch vụ AWS
  - Tạo và quản lý tài khoản AWS tự động
  - Thanh toán tổng hợp trên nhiều tài khoản AWS
- Sơ đồ **cấu trúc của AWS Organizations** cho thấy một tổ chức cơ bản,
  hoặc tổ chức gốc, bao gồm bảy tài khoản
  được tổ chức thành bốn đơn vị tổ chức (hoặc OU).
  Đơn vị tổ chức là một vùng chứa cho các tài khoản trong thư mục gốc.
  Một đơn vị tổ chức cũng có thể chứa các đơn vị tổ chức khác.
- Khi ta attach một policy vào một trong các nút trong hệ thống phân cấp,
  chính sách đó sẽ áp dụng xuống và ảnh hưởng đến tất cả các nhánh và lá.
  Tổ chức mẫu này có một số chính sách được đính kèm với một số đơn vị tổ chức
  hoặc được gắn trực tiếp vào tài khoản.
- Các **chức năng và lợi ích chính của AWS Organizations** cho phép ta:
  - Tạo chính sách kiểm soát dịch vụ (SCP) kiểm soát tập trung các dịch vụ
    AWS trên nhiều tài khoản AWS
  - Tạo các nhóm tài khoản và sau đó đính kèm các chính sách vào một nhóm
    để đảm bảo rằng các chính sách đúng được áp dụng trên các tài khoản
  - Đơn giản hóa việc quản lý tài khoản bằng cách sử dụng các API
    để tự động hóa việc tạo và quản lý các tài khoản AWS mới
  - Đơn giản hóa quy trình thanh toán bằng cách thiết lập
    một phương thức thanh toán duy nhất cho tất cả các tài khoản AWS
    trong tổ chức của ta. Với thanh toán tổng hợp, ta có thể xem tổng hợp
    các khoản phí phát sinh bởi tất cả các tài khoản của mình và ta
    không liên quan đến lợi ích của việc đặt giá từ việc sử dụng tổng hợp
- **Bảo mật với AWS Organizations**
  không thay thế việc liên kết các policies của AWS IAM với user,
  group và role trong tài khoản AWS.
- Với **IAM policies**, ta có thể cho phép hoặc từ chối quyền truy cập
  vào các dịch vụ AWS (chẳng hạn như Amazon S3), các tài nguyên AWS riêng lẻ
  (chẳng hạn như một nhóm S3 cụ thể) hoặc các hành động API riêng lẻ
  (chẳng hạn như s3: CreateBucket).
  IAM policies chỉ có thể được áp dụng cho user, group và role IAM
  và policies này không bao giờ có thể hạn chế root user của tài khoản AWS.
- Ngược lại, với _Organizations_,
  ta sử dụng các chính sách kiểm soát dịch vụ (SCPs)
  để cho phép hoặc từ chối quyền truy cập vào các dịch vụ AWS cụ thể
  cho các tài khoản AWS cá nhân hoặc cho các nhóm tài khoản trong đơn vị tổ chức.
  Các hành động được chỉ định từ SCP được đính kèm ảnh hưởng đến tất cả IAM user,
  group và role của một tài khoản, bao gồm cả root user của tài khoản AWS.
- Có những **hạn chế** về tên mà ta có thể tạo trong AWS Organizations,
  bao gồm tên tài khoản, đơn vị tổ chức, đơn vị tổ chức và chính sách.
  Tên phải bao gồm các ký tự Unicode và độ dài không vượt quá 250 ký tự.
  AWS Organizations có một số giá trị tối đa và tối thiểu cho các thực thể.
- Video: [AWS Organizations](https://awsacademy.instructure.com/courses/77750/modules/items/7000792)

#### AWS Billing and Cost Management

- Quản lý chi phí và lập hóa đơn AWS **(AWS Billing and Cost Management)**
  là dịch vụ mà ta sử dụng để thanh toán hóa đơn AWS, theo dõi việc sử dụng
  và lập ngân sách chi phí của mình.
  Quản lý Thanh toán và Chi phí cho phép ta dự đoán và có được ý tưởng tốt hơn
  về chi phí và mức sử dụng của ta có thể ra sao trong tương lai
  để ta có thể lập kế hoạch trước.
- Trang tổng quan thanh toán AWS **(AWS Billing Dashboard)**
  cho phép ta xem trạng thái chi tiêu AWS hàng tháng của mình,
  xác định các dịch vụ chiếm phần lớn tổng chi tiêu của ta và hiểu ở cấp độ
  cao chi phí đang có xu hướng như thế nào.
- Từ trang tổng quan thanh toán, ta có thể truy cập một số công cụ quản lý
  chi phí khác mà ta có thể sử dụng để ước tính
  và lập kế hoạch chi phí AWS của mình.
  Các công cụ đó bao gồm _AWS Bills_, _AWS Cost Explorer_, _AWS Budgets_,
  and _AWS Cost and Usage Reports_.
- Với **Cost Explorer**, ta có thể hình dung, hiểu và quản lý chi phí
  và việc sử dụng AWS của mình theo thời gian.
  Trình khám phá Chi phí (Cost Explorer) bao gồm một báo cáo mặc định hiển thị
  chi phí và việc sử dụng cho các dịch vụ AWS chịu chi phí hàng đầu của chúng ta.
  Báo cáo chi phí hoạt động hàng tháng cung cấp cho ta cái nhìn tổng quan
  về tất cả các chi phí của ta trong 3 tháng qua.
  Báo cáo này cũng cung cấp các con số dự báo cho tháng tới,
  với khoảng tin cậy tương ứng.
- Video: [Quản lý chi phí và lập hóa đơn AWS](https://awsacademy.instructure.com/courses/77750/modules/items/7000794)

#### Technical support models

- **Hỗ trợ AWS** được phát triển để cung cấp hỗ trợ đầy đủ và các nguồn lực
  phù hợp để hỗ trợ thành công của ta.
  Họ muốn hỗ trợ tất cả các khách hàng của mình,
  bao gồm cả những khách hàng có thể đang thử nghiệm AWS,
  những khách hàng đang tìm cách sử dụng AWS trong sản xuất
  và cả những khách hàng sử dụng AWS như một tài nguyên
  quan trọng trong kinh doanh.
  Bộ phận hỗ trợ AWS có thể thay đổi loại hỗ trợ được cung cấp,
  tùy thuộc vào nhu cầu và mục tiêu của khách hàng
  - Nếu ta muốn có hướng dẫn chủ động,
    AWS Support có **Technical Account Managers (TAMs)**
    được chỉ định làm đầu mối liên hệ chính của người dùng đó.
  - Nếu ta muốn đảm bảo rằng ta tuân theo các phương pháp hay nhất
    để tăng hiệu suất và khả năng chịu lỗi trong môi trường AWS,
    AWS Support có AWS Trusted Advisor
  - Để được hỗ trợ về tài khoản, Support Concierge
    là chuyên gia thanh toán và tài khoản, người sẽ cung cấp phân tích
    nhanh chóng và hiệu quả về các vấn đề thanh toán và tài khoản.
    Nhân viên hướng dẫn giải quyết tất cả các câu hỏi liên quan
    đến thanh toán phi kỹ thuật và cấp tài khoản
- AWS muốn ta tự tin có thể lập kế hoạch, triển khai và tối ưu hóa.
  Chúng tôi đã phát triển các **kế hoạch hỗ trợ** cụ thể,
  bao gồm các kế hoạch hỗ trợ Basic, Developer, Business, and Enterprise.
- Ngoài việc hiểu các chi phí liên quan đến các kế hoạch hỗ trợ khác nhau,
  điều quan trọng là ta phải hiểu các cấp độ dịch vụ liên quan đến mỗi kế hoạch.
  Ngoài kế hoạch hỗ trợ ta chọn, **mức độ nghiêm trọng** của trường hợp
  sẽ dẫn đến **loại phản hồi** mà ta nhận được.
  Có năm mức độ nghiêm trọng khác nhau: Critical, Urgent, High, Normal, Low.
- Ta có thể xem thêm về các so sánh giữa các kế hoạch hỗ trợ
  trong mục Tài liệu tham khảo.
- Video: [Mô hình hỗ trợ kỹ thuật](https://awsacademy.instructure.com/courses/77750/modules/items/7000799)

#### References

- [Cloud Economics & Billing](https://drive.google.com/file/d/1N6l3gu-tol02kUwF5qlvwf6dO-XpdwH8/view)
- [AWS Free Tier](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)
- [AWS Pricing Calculator](https://calculator.aws/#/)
- [Reading an estimate](https://docs.aws.amazon.com/pricing-calculator/latest/userguide/reading-estimate.html)
- [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/)

### Lab 1

- Lab 1: [Console Demonstration - Billing Dashboard](https://awsacademy.instructure.com/courses/77750/modules/items/7000796)

### AWS Identity and Access Management

#### Mô hình trách nhiệm chung (AWS Shared Responsibility Model)

- **Bảo mật và tuân thủ** là trách nhiệm chung giữa AWS và khách hàng.
  **Mô hình trách nhiệm chung** này được thiết kế để giúp giảm bớt gánh nặng
  hoạt động của khách hàng. Đồng thời, để cung cấp tính linh hoạt và sự kiểm soát
  của khách hàng cho phép triển khai các giải pháp của khách hàng trên AWS,
  khách hàng vẫn phải chịu trách nhiệm về một số khía cạnh của bảo mật tổng thể.
  Sự khác biệt về người chịu trách nhiệm cho những gì thường được gọi là bảo mật
  **"của"** đám mây so với bảo mật **"trong"** đám mây.
- **AWS vận hành, quản lý và kiểm soát** các thành phần từ lớp ảo hóa phần mềm
  cho đến bảo mật vật lý của các cơ sở nơi dịch vụ AWS hoạt động.
  AWS chịu trách nhiệm bảo vệ cơ sở hạ tầng chạy tất cả các dịch vụ được cung cấp
  trong AWS. Cơ sở hạ tầng này bao gồm phần cứng, phần mềm, mạng và cơ sở chạy
  các dịch vụ AWS.
- **Khách hàng chịu trách nhiệm** về việc mã hóa dữ liệu ở chế độ nghỉ và dữ liệu
  đang chuyển đi. Khách hàng cũng nên đảm bảo rằng mạng được định cấu hình
  để bảo mật và thông tin đăng nhập và thông tin đăng nhập bảo mật được quản lý
  một cách an toàn. Ngoài ra, khách hàng chịu trách nhiệm về cấu hình của các
  nhóm bảo mật và cấu hình của hệ điều hành chạy trên các phiên bản máy tính mà
  họ khởi chạy (bao gồm các bản cập nhật và bản vá bảo mật).
- Video: [AWS Shared Responsibility Model](https://awsacademy.instructure.com/courses/77750/modules/items/7000825)

#### AWS IAM (Identity and Access Management):

- **AWS IAM** cho phép ta kiểm soát quyền truy cập vào các dịch vụ máy tính,
  lưu trữ, cơ sở dữ liệu và ứng dụng trong Đám mây AWS.
  IAM có thể được sử dụng để xử lý xác thực và chỉ định và thực thi
  các chính sách ủy quyền để ta có thể chỉ định người dùng nào
  có thể truy cập dịch vụ nào.
- Để hiểu cách sử dụng IAM để bảo mật tài khoản AWS của ta,
  điều quan trọng là phải hiểu vai trò và chức năng của từng thành phần
  trong số bốn thành phần IAM: **IAM User, IAM Group, IAM Policy, IAM Role**.
- **Xác thực** là một khái niệm bảo mật máy tính cơ bản:
  người dùng hoặc hệ thống trước tiên phải chứng minh danh tính của họ.
  Hãy nghĩ đến cách ta xác thực bản thân khi đến sân bay và ta muốn thông qua
  an ninh sân bay để có thể bắt chuyến bay của mình. Trong tình huống này,
  ta phải xuất trình một số mẫu giấy tờ tùy thân cho nhân viên an ninh
  để chứng minh ta là ai trước khi ta có thể vào khu vực hạn chế.
  Một điều kiện tương tự áp dụng cho việc giành quyền truy cập vào các tài nguyên
  AWS trên đám mây.
- Khi ta xác thực với IAM user, ta chọn loại quyền truy cập mà người dùng
  được phép sử dụng để truy cập tài nguyên AWS. ta có thể chỉ định hai loại quyền
  truy cập khác nhau cho người dùng:
  **Programmatic Access** and **AWS Management Console Access**.
  Để tăng cường bảo mật, **AWS khuyến khích bật MFA (Multi-factor Authetication)**.
  Với MFA, người dùng và hệ thống phải cung cấp mã thông báo MFA,
  ngoài thông tin đăng nhập thông thường, trước khi họ có thể truy cập các
  dịch vụ và tài nguyên AWS.
- Video: [AWS IAM](https://awsacademy.instructure.com/courses/77750/modules/items/7000827)

#### Giao diện AWS console & IAM example.

- Video: [Ví dụ IAM](https://awsacademy.instructure.com/courses/77750/modules/items/7000829)

### AWS Securing Objects

#### Secure a New AWS Account

- Best practice về root user là **không** sử dụng tài khoản root AWS
  ngoại trừ thực sự cần thiết. Thay vào đó, AWS khuyên ta nên sử dụng IAM
  để tạo thêm người dùng và chỉ định quyền cho những người dùng này,
  tuân theo nguyên tắc ít đặc quyền nhất, ta có thể tìm hiểu thêm thông tin
  để xử lý với tài khoản root ở mục _Tài liệu tham khảo_.
- Cụ thể, các cách bảo mật tài khoản AWS mới:
  - Ngừng sử dụng tài khoản root, ta có thể tham khảo ở _Tài liệu tham khảo_:
    Creating your first IAM Admin User and Group
  - Bật MFA, ta có thể tham khảo ở _Tài liệu tham khảo_:
    Configuring MFA-protected API Access
  - Tạo AWS CloudTrail, ta có thể tham khảo ở _Tài liệu tham khảo_:
    CloudTrail Supported Services and Integrations và Creating a Trail
  - Bật Billing reports: ta có thể tham khảo ở _Tài liệu tham khảo_:
    Creating Cost and Usage Reports
- Video: [Bảo mật tài khoản AWS mới](https://awsacademy.instructure.com/courses/77750/modules/items/7000831)

#### Securing multiple Accounts

- **AWS Organizations** là một tính năng bảo mật hữu ích, ta có thể nhóm
  các tài khoản thành các **Đơn vị tổ chức (Organizational Units - OUs)**
  và đính kèm các chính sách truy cập khác nhau cho từng OU.
  Ví dụ: nếu ta có các tài khoản chỉ được phép truy cập các dịch vụ AWS đáp ứng
  các yêu cầu quy định nhất định,
  ta có thể đặt các tài khoản đó vào một đơn vị tổ chức.
  Sau đó, ta có thể xác định một chính sách chặn truy cập của OU vào các dịch vụ
  không đáp ứng các yêu cầu quy định đó và sau đó đính kèm chính sách đó vào OU.
- Một tính năng bảo mật khác là **AWS Organizations tích hợp và hỗ trợ IAM**.
  AWS Organizations mở rộng quyền kiểm soát đó đến cấp tài khoản bằng cách
  cho phép ta kiểm soát những gì người dùng và vai trò trong một tài khoản
  hoặc một nhóm tài khoản có thể thực hiện. Các quyền kết quả là giao điểm hợp lý
  giữa những gì được cho phép bởi cài đặt chính sách AWS Organizations và những
  quyền nào được IAM cấp rõ ràng trong tài khoản cho người dùng hoặc vai trò đó.
  Người dùng chỉ có thể truy cập những gì được cho phép bởi các chính sách
  của AWS Organizations và chính sách IAM.
- AWS Organizations cung cấp các **chính sách kiểm soát dịch vụ**
  **(Service Control Policies - SCP)** cho phép ta chỉ định quyền tối đa
  mà các tài khoản thành viên trong tổ chức có thể có.
  Trong SCP, ta có thể hạn chế dịch vụ AWS, tài nguyên và hành động cá nhân nào
  mà người dùng và vai trò trong mỗi tài khoản thành viên có thể truy cập.
  Các bài viết tham khảo: Enabling all Features, Enabling and Disabling a Policy
  Type on a Root và Policies and Permissions in IAM trong mục _Tài liệu đọc_.
- **Dịch vụ quản lý khóa AWS (Key Management Service - KMS)** là một dịch vụ
  cho phép ta tạo và quản lý khóa mã hóa, đồng thời kiểm soát việc sử dụng mã hóa
  trên nhiều loại dịch vụ AWS và ứng dụng của ta. AWS KMS là một dịch vụ an toàn
  và linh hoạt sử dụng các mô-đun bảo mật phần cứng (HSM) đã được xác thực theo
  Tiêu chuẩn xử lý thông tin liên bang (FIPS) 140-2 để bảo vệ khóa của chúng ta.
  AWS KMS cũng tích hợp với AWS CloudTrail để cung cấp cho ta nhật ký về tất cả
  việc sử dụng chính để giúp đáp ứng các nhu cầu về quy định và tuân thủ.
  Tham khảo bài viết AWS Key Management Service Features trong mục _Tài liệu đọc_.
- **Amazon Cognito** cung cấp các giải pháp để kiểm soát quyền truy cập
  vào tài nguyên AWS từ ứng dụng. Ta có thể xác định vai trò và ánh xạ
  người dùng đến các vai trò khác nhau để ứng dụng của ta
  chỉ có thể truy cập các tài nguyên được cấp phép cho từng người dùng.
- **AWS Shield** là một dịch vụ bảo vệ khách hàng khỏi những vụ tấn công
  Từ chối dịch vụ phân tán **(Distributed Denial of Service - DDoS)**
  được quản lý nhằm bảo vệ các ứng dụng chạy trên AWS. Nó cung cấp khả năng
  phát hiện luôn bật và giảm thiểu nội tuyến tự động giúp giảm thiểu thời gian
  ngừng hoạt động và độ trễ của ứng dụng, vì vậy không cần phải tham gia
  Hỗ trợ AWS để được hưởng lợi từ bảo vệ DDoS.
  Chúng ta có thể xem thêm bài viết:
  AWS WAF Developer Guide trong mục _Tài liệu tham khảo_.
- Video: [Bảo mật nhiều tài khoản](https://awsacademy.instructure.com/courses/77750/modules/items/7000833)

#### Securing data

- **Mã hóa dữ liệu (Encryption of Data)** là một công cụ cần thiết để sử dụng
  khi mục tiêu của ta là bảo vệ dữ liệu kỹ thuật số.
  Mã hóa dữ liệu lấy dữ liệu dễ đọc và mã hóa dữ liệu đó để bất kỳ ai
  không có quyền truy cập vào khóa bí mật có thể được sử dụng để giải mã nó
  đều không thể đọc được. Do đó, ngay cả khi kẻ tấn công giành được
  quyền truy cập vào dữ liệu của ta, chúng không thể hiểu được.
- **Dữ liệu ở trạng thái nghỉ (Data at Rest)** đề cập đến dữ liệu được lưu trữ
  vật lý trên đĩa hoặc trên băng. Ta có thể tạo hệ thống tệp được mã hóa trên AWS
  để tất cả dữ liệu và siêu dữ liệu của ta được mã hóa hoàn toàn bằng cách
  sử dụng thuật toán mã hóa Advanced Encryption Standard (AES)-256 tiêu chuẩn mở.
  Khi ta sử dụng AWS KMS, mã hóa và giải mã được xử lý tự động và minh bạch,
  do đó ta không cần phải sửa đổi các ứng dụng của mình. Nếu tổ chức của ta
  tuân theo các chính sách quy định hoặc công ty yêu cầu mã hóa dữ liệu
  và siêu dữ liệu ở chế độ nghỉ, AWS khuyên nên bật mã hóa trên tất cả
  các dịch vụ lưu trữ dữ liệu. Ta có thể mã hóa dữ liệu được lưu trữ trong bất kỳ
  dịch vụ nào được AWS KMS hỗ trợ.
  Xem thêm tài liệu How AWS Services use AWS KMS trong mục Tài liệu tham khảo.
- **Mã hóa dữ liệu đang chuyển tiếp (Data in Transit)** đề cập đến dữ liệu
  đang di chuyển trên mạng. Việc mã hóa dữ liệu trong quá trình truyền
  được thực hiện bằng cách sử dụng **Bảo mật lớp truyền tải (TLS) 1.2**
  với mật mã AES-256 tiêu chuẩn mở.
  TLS trước đây được gọi là Lớp cổng bảo mật (SSL).
  Xem thêm bài Encryption of EFS Data in Transit trong mục Tài liệu tham khảo.
- Theo mặc định, tất cả các Amazon S3 buckets là private và chỉ có thể
  được truy cập bởi những người dùng được cấp quyền truy cập rõ ràng.
  Điều cần thiết là quản lý và kiểm soát quyền truy cập vào dữ liệu Amazon S3.
  AWS cung cấp nhiều công cụ và tùy chọn để kiểm soát quyền truy cập vào nhóm
  hoặc đối tượng S3, bao gồm: Amazon S3 Block Public Access, IAM Policies,
  Bucket Policies, Access Control Lists (ACLs), AWS Trusted Advisor.
- Video: [Bảo mật dữ liệu](https://awsacademy.instructure.com/courses/77750/modules/items/7000835)

#### Working to Ensure Compliance

- **AWS Compliance Programs**: AWS hợp tác với các tổ chức chứng nhận
  bên ngoài và các đánh giá viên độc lập để cung cấp cho khách hàng thông tin
  về các chính sách, quy trình và kiểm soát do AWS thiết lập và vận hành.
  Danh sách đầy đủ các AWS Compliance Programs hiện có sẵn
  trong tài liệu tham khảo.
  Ngoài ra, để biết chi tiết về các dịch vụ AWS nào thuộc phạm vi
  của các chương trình đảm bảo AWS,
  hãy tham khảo thêm tài liệu AWS Services in Scope by Compliance Program
  trong mục Tài liệu tham khảo
- **AWS Config** là một dịch vụ cho phép ta đánh giá, kiểm tra và đánh giá
  các cấu hình của tài nguyên AWS của ta.
  AWS Config liên tục theo dõi và ghi lại các cấu hình tài nguyên AWS của ta
  và nó cho phép ta tự động đánh giá các cấu hình đã ghi
  so với các cấu hình mong muốn.
  Với Cấu hình AWS, hãy xem xét các thay đổi về cấu hình và mối quan hệ
  giữa các tài nguyên AWS, xem lại lịch sử cấu hình tài nguyên chi tiết
  và xác định sự tuân thủ tổng thể của ta đối với các cấu hình được chỉ định
  trong nguyên tắc nội bộ của ta.
  Điều này cho phép ta đơn giản hóa việc kiểm tra tuân thủ, phân tích bảo mật,
  quản lý thay đổi và khắc phục sự cố hoạt động.
- **AWS Artifact** cung cấp tải xuống theo yêu cầu các tài liệu tuân thủ
  và bảo mật AWS, chẳng hạn như chứng nhận AWS ISO,
  báo cáo Ngành thẻ thanh toán (PCI) và Kiểm soát tổ chức dịch vụ (SOC).
  Ta có thể gửi các tài liệu về bảo mật và tuân thủ
  (còn được gọi là tạo tác theo dõi) cho kiểm toán viên hoặc cơ quan quản lý
  của mình để chứng minh tính bảo mật và tuân thủ của cơ sở hạ tầng
  và dịch vụ AWS mà ta sử dụng. Ta cũng có thể sử dụng các tài liệu này
  làm hướng dẫn để đánh giá kiến trúc đám mây của riêng mình và đánh giá hiệu quả
  của các kiểm soát nội bộ của công ty ta. AWS Artifact chỉ
  cung cấp tài liệu về AWS. Khách hàng của AWS chịu trách nhiệm phát triển
  hoặc lấy các tài liệu chứng minh tính bảo mật và tuân thủ của công ty họ.
  Ngoài ra, ta có thể xem thêm tài liệu Managing agreements in AWS Artifact
  trong mục Tài liệu tham khảo.
- Video: [Working to Ensure Compliance](https://awsacademy.instructure.com/courses/77750/modules/items/7000838)

#### Document references

- Tài liệu dưới đây giúp ta hiểu hơn về AWS IAM:
  - [Tổng quan về IAM](https://drive.google.com/file/d/1NjLyaKrEOf9aMY_wTMYnurpVAR5OxsN0/view)
- Các tài liệu dưới đây giúp ta hiểu rõ hơn về cách bảo vệ các Object:
  - [Tasks that require root user credentials](https://docs.aws.amazon.com/general/latest/gr/root-vs-iam.html#aws_tasks-that-require-root)
  - [Creating your first IAM admin user and group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
  - [Configuring MFA-protected API access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html)
  - [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
  - [Creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html)
  - [Creating Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/cur-create.html)
  - [Enabling all features in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html)
  - [Enabling and Disabling a Policy Type on a Root](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html#enable_policies_on_root)
  - [Policies and permissions in IAM](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html#enable_policies_on_root)
  - [AWS Key Management Service features](https://aws.amazon.com/kms/features/)
  - [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)
  - [How AWS Services use AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/service-integration.html)
  - [Encryption of EFS Data in Transit](https://docs.aws.amazon.com/whitepapers/latest/efs-encrypted-file-systems/encryption-of-data-in-transit.html)
  - [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/)
  - [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/)
  - [Managing agreements in AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/managing-agreements.html)

### Lab 2

- Lab 2: [Lab - 1 Introduction to AWS IAM](https://awsacademy.instructure.com/courses/77750/assignments/785902?module_item_id=7000843)
  [Vietsub](https://docs.google.com/document/d/18LSCLTAoPDXvtw4rvJqFCgJt-tWamolR/view)

### AWS VPC

#### Basic concepts

- **Mạng máy tính (Network)**
  là hai hoặc nhiều máy khách được kết nối với nhau để chia sẻ tài nguyên.
  Một mạng có thể được phân vùng một cách hợp lý thành các subnet.
  Kết nối mạng yêu cầu một thiết bị mạng (chẳng hạn như Router hoặc Switch)
  để kết nối tất cả các máy khách với nhau và cho phép giao tiếp giữa chúng.
- Mỗi máy khách trong mạng có một địa chỉ Internet Protocol (IP) duy nhất
  để xác định nó. Địa chỉ IP là một nhãn số ở định dạng thập phân.
  Máy móc chuyển đổi số thập phân đó sang định dạng nhị phân.
- Địa chỉ IP 32 bit được gọi là địa chỉ IPv4.
  Địa chỉ IPv6, 128 bit. Địa chỉ IPv6 có thể chứa nhiều thiết bị người dùng hơn.
- Một phương pháp phổ biến để mô tả mạng là
  **Classless Inter-Domain Routing (CIDR)**.
  Địa chỉ CIDR được biểu thị như sau:
  - Địa chỉ IP (là địa chỉ đầu tiên của mạng).
  - Tiếp theo, một ký tự gạch chéo (/).
  - Cuối cùng, một số cho ta biết có bao nhiêu bit của tiền tố định tuyến
    phải được cố định hoặc cấp phát cho mã định danh mạng.
- Các bit không cố định được phép thay đổi.
  CIDR là một cách để thể hiện một nhóm địa chỉ IP liên tiếp với nhau.
- **Mô hình OSI** là một mô hình khái niệm được sử dụng để giải thích
  cách dữ liệu truyền qua mạng. Nó bao gồm bảy lớp và hiển thị các giao thức
  và địa chỉ chung được sử dụng để gửi dữ liệu ở mỗi lớp.
- Video: [Cơ bản về Networking](https://awsacademy.instructure.com/courses/313/modules/items/48831)

#### Amazon Virtual Private Cloud (Amazon VPC)

- **Amazon Virtual Private Cloud (Amazon VPC)**
  là một dịch vụ cho phép ta cung cấp một phần riêng biệt một cách hợp lý
  của Đám mây AWS (được gọi là đám mây riêng ảo hoặc VPC),
  nơi ta có thể khởi chạy các tài nguyên AWS của mình.
  Amazon VPC cung cấp cho ta quyền kiểm soát các tài nguyên mạng ảo của mình,
  bao gồm việc lựa chọn dải địa chỉ IP của riêng ta, tạo subnet cũng như cấu hình
  route tables và network gateway. Ta có thể sử dụng cả IPv4 và IPv6 trong VPC
  của mình để truy cập an toàn vào các tài nguyên và ứng dụng.
  Ta có thể sử dụng nhiều lớp bảo mật, bao gồm các **Security Group**
  và danh sách kiểm soát truy cập mạng **(network ACL)**,
  để giúp kiểm soát quyền truy cập vào
  các **Amazon Elastic Compute Cloud (Amazon EC2)** instance trong mỗi subnet.
- Amazon VPC cho phép ta cung cấp các đám mây riêng ảo (VPC).
  VPC là một mạng ảo được cách ly hợp lý với các mạng ảo khác trong Đám mây AWS.
  VPC dành riêng cho tài khoản của ta. VPC thuộc về một AWS Region duy nhất
  và có thể mở rộng nhiều Availability Zones. Sau khi tạo VPC, ta có thể chia nó
  thành một hoặc nhiều Subnet. **Subnet là một dải địa chỉ IP trong VPC**.
  Subnet thuộc về một Availability Zone duy nhất. Ta có thể tạo các subnets trong
  các Availability Zone khác nhau để có tính khả dụng cao.
  Subnet thường được phân loại là public hoặc private.
  Public subnet có quyền truy cập trực tiếp vào Internet,
  nhưng private subnet thì không.
- **Địa chỉ IP** cho phép các tài nguyên trong VPC của ta giao tiếp với nhau
  và với các tài nguyên qua Internet. Khi ta tạo VPC, ta chỉ định
  một khối **IPv4 CIDR (một loạt các địa chỉ private IPv4)** cho nó.
  Sau khi tạo VPC, ta không thể thay đổi dải địa chỉ,
  vì vậy điều quan trọng là ta phải chọn nó cẩn thận.
  Khối IPv4 CIDR có thể lớn bằng / 16 (là 216 hoặc 65.536 địa chỉ)
  hoặc nhỏ bằng / 28 (là 24 hoặc 16 địa chỉ).
  Ta có thể tùy chọn liên kết IPv6 CIDR block với VPC và subnet của mình,
  đồng thời gán địa chỉ IPv6 từ block đó cho các tài nguyên trong VPC.
  Để hiểu chi tiết hơn ta có thể tham khảo thêm bài
  _IP Addressing in your VPC_ trong mục Tài liệu tham khảo.
- Khi ta tạo một Subnet, nó yêu cầu khối CIDR của riêng nó.
  Đối với mỗi khối CIDR mà ta chỉ định, AWS bảo lưu năm địa chỉ IP trong khối đó
  và các địa chỉ này không có sẵn để sử dụng. AWS bảo lưu các địa chỉ IP này cho:
  - Địa chỉ mạng
  - Router cục bộ VPC (truyền thông nội bộ)
  - Phân giải hệ thống tên miền (DNS)
  - Sử dụng trong tương lai
  - Địa chỉ broadcast
- Khi ta tạo VPC, mọi instance trong VPC đó sẽ
  tự động nhận được một địa chỉ IP riêng.
  Ta cũng có thể yêu cầu chỉ định **địa chỉ Public IP** khi tạo instance
  bằng cách sửa đổi các thuộc tính địa chỉ public IP tự động gán của subnet.
  **Elastic IP Address** là địa chỉ IPv4 tĩnh và public được thiết kế
  cho điện toán đám mây động. Ta có thể liên kết Elastic IP address với bất kỳ
  instance hoặc giao diện mạng nào cho bất kỳ VPC nào trong tài khoản của ta.
  Chi tiết hơn về EIP ta có thể xem thêm bài _Elastic IP Addresses _
  trong mục Tài liệu tham khảo.
- **Elastic Network Interface** một giao diện mạng ảo mà ta có thể gắn
  hoặc tách khỏi một instance trong VPC. Các thuộc tính của giao diện mạng
  tuân theo nó khi nó được gắn lại với một instance khác.
  Khi ta di chuyển giao diện mạng từ instance này sang instance khác,
  lưu lượng mạng được chuyển hướng đến instance mới.
  Chi tiết hơn ta có thể xem thêm bài _Elastic Network Interface_
  trong mục Tài liệu tham khảo.
- **Bảng định tuyến** chứa một tập hợp các quy tắc (được gọi là các tuyến)
  hướng lưu lượng mạng từ subnet của ta.
  Mỗi tuyến chỉ định một số phận và một mục tiêu.
  Định vị khối CIDR đích ở nơi ta muốn lưu lượng truy cập
  từ subnet của mình đi tới. Định hướng mục tiêu mà lưu lượng đích được gửi qua.
  Theo mặc định, mọi bảng lộ trình mà ta tạo đều chứa một lộ trình cục bộ
  để liên lạc trong VPC. Ta có thể tùy chỉnh bảng tuyến đường
  bằng cách thêm tuyến đường. Ta không thể xóa mục nhập tuyến đường cục bộ
  được sử dụng cho liên lạc nội bộ. Mỗi subnet trong VPC của ta phải được
  liên kết với một bảng lộ trình. Bảng tuyến đường chính là bảng tuyến đường
  được tự động gán cho VPC của ta. Nó kiểm soát việc định tuyến cho tất cả
  các subnet không được liên kết rõ ràng với bất kỳ bảng định tuyến nào khác.
  Một subnet chỉ có thể được liên kết với một bảng lộ trình tại một thời điểm,
  nhưng ta có thể liên kết nhiều subnet với cùng một bảng lộ trình.
  Chi tiết hơn ta có thể tham khảo thêm bài _Route table and routes_
  trong mục Tài liệu tham khảo.
- Video: [AWS VPC](https://awsacademy.instructure.com/courses/313/modules/items/48832)

#### NAT Instances

- Ta có thể dùng **NAT Instance** trong public subnet trong VPC của mình
  thay vì NAT Gateways. Bảng lộ trình chính được liên kết với private subnet
  và gửi lưu lượng từ các instance trong private subnet đến NAT Instance
  trong Subnet công cộng. Sau đó, NAT Instance sẽ gửi lưu lượng
  đến internet gateway cho VPC. Lưu lượng truy cập được quy cho địa chỉ
  Elastic IP Address của NAT Instance.
  NAT Instance chỉ định số cổng cao cho phản hồi; nếu một phản hồi quay trở lại,
  NAT instance sẽ gửi nó đến một instance trong private subnet
  dựa trên số cổng cho phản hồi.

- Lưu lượng truy cập Internet từ các instance trong private subnet
  được chuyển đến NAT instance, sau đó giao tiếp với internet.
  Do đó, NAT instance phải có quyền truy cập internet.
  Nó phải nằm trong một subnet công cộng (một subnet có bảng định tuyến
  với đường dẫn đến Internet gateway và nó phải có địa chỉ public IP
  hoặc địa chỉ Elastic IP address.
  Chi tiết hơn ta có thể tham khảo thêm bài _NAT Instances_
  trong mục Tài liệu tham khảo.

- Video: [NAT Instances](https://funix.udemy.com/course/awsnetworking/learn/lecture/16371290#overview)

#### NAT Gateways

- **NAT Gateways (NAT)** tạo ra các instance trong private subnet
  để kết nối với internet hoặc các dịch vụ AWS khác,
  nhưng ngăn không cho internet kết nối với các instance đó.

- Để tạo NAT gateway, ta phải chỉ định public subnet mà NAT gateway
  sẽ nằm trong đó. Ta cũng phải chỉ định một địa chỉ Elastic IP address
  để liên kết với NAT gateway khi ta tạo nó.
  Sau khi ta tạo NAT gateway, ta phải cập nhật bảng định tuyến
  được liên kết với một hoặc nhiều private subnet của ta
  để hướng lưu lượng truy cập liên kết internet đến NAT gateway.
  Do đó, các instance trong private subnet của ta có thể giao tiếp với internet.
  Để hiểu chi tiết hơn ta có thể tham khảo thêm các bài viết
  _NAT Gateways_ và _Compare NAT gateways and NAT instances_
  trong mục Tài liệu tham khảo.

Video: [NAT Gateways](https://funix.udemy.com/course/awsnetworking/learn/lecture/16371296#overview)

#### VPC Networking

- **Internet Gateway** là một thành phần VPC có thể mở rộng, dự phòng
  và có tính khả dụng cao cho phép giao tiếp giữa các instance
  trong VPC và internet. Internet gateway phục vụ hai mục đích:
  cung cấp mục tiêu trong bảng định tuyến VPC
  cho lưu lượng truy cập internet có thể định tuyến
  và thực hiện dịch địa chỉ mạng cho các trường hợp
  được chỉ định địa chỉ public IPv4.
  Để đặt subnet ở chế độ public, ta gắn internet gateway vào VPC của mình
  và thêm tuyến đường vào bảng định tuyến để gửi lưu lượng truy cập không cục bộ qua internet gateway tới internet(0.0.0.0/0).
  Để hiểu chi tiết hơn ta có thể tham khảo thêm bài _Internet gateway_
  trong mục Tài liệu tham khảo.
- **VPC Sharing** cho phép khách hàng chia sẻ subnet với các tài khoản AWS khác
  trong cùng một tổ chức trong AWS organization.
  VPC sharing cho phép nhiều tài khoản AWS tạo tài nguyên ứng dụng của họ
  — chẳng hạn như Amazon EC2 instance,
  cơ sở dữ liệu Amazon Relational Database Service (Amazon RDS),
  cụm Amazon Redshift và các chức năng AWS Lambda
  — thành các VPC được quản lý tập trung, được chia sẻ.
  Trong mô hình này, tài khoản sở hữu VPC (chủ sở hữu)
  chia sẻ một hoặc nhiều subnet với các tài khoản khác (người tham gia)
  thuộc cùng một tổ chức trong AWS organization.
  Sau khi một subnet được chia sẻ, những người tham gia có thể
  xem, tạo, sửa đổi và xóa các tài nguyên ứng dụng của họ
  trong các subnet được chia sẻ với họ.
  Người tham gia không thể xem, sửa đổi hoặc xóa các tài nguyên
  thuộc về những người tham gia khác hoặc chủ sở hữu VPC.
- **VPC Peering** là kết nối mạng giữa hai VPC
  cho phép ta định tuyến lưu lượng truy cập giữa chúng một cách riêng tư.
  Các instance trong một trong hai VPC có thể giao tiếp với nhau
  như thể chúng nằm trong cùng một mạng.
  Bạn có thể tạo VPC peering giữa các VPC của riêng ta,
  với VPC trong tài khoản AWS khác hoặc với VPC trong AWS Region khác.
  Chi tiết hơn ta có thể xem thêm về _VPC peering_ trong mục Tài liệu tham khảo.
- Theo mặc định, các instances mà ta khởi chạy vào VPC
  không thể giao tiếp với mạng từ xa.
  Để kết nối VPC với mạng từ xa của ta
  (nghĩa là tạo mạng riêng ảo hoặc kết nối VPN).
  Chi tiết hơn ta có thể xem thêm bài _AWS Site-to-Site VPN_
  trong mục Tài liệu tham khảo.
- Một trong những thách thức của kết nối mạng là hiệu suất mạng.
  Hiệu suất có thể bị ảnh hưởng tiêu cực nếu trung tâm dữ liệu của ta
  nằm ở xa AWS Region của ta. Đối với những trường hợp như vậy,
  AWS cung cấp **AWS Direct Connect** hoặc DX.
  AWS Direct Connect cho phép ta thiết lập kết nối private network,
  chuyên dụng giữa mạng của ta và một trong các vị trí DX.
  Kết nối riêng tư này có thể giảm chi phí mạng của ta, tăng lưu lượng băng thông
  và cung cấp trải nghiệm mạng nhất quán hơn so với kết nối dựa trên internet.
  DX sử dụng mạng cục bộ ảo 802.1q chuẩn hoạt động (VLAN).
  Chi tiết hơn ta có thể xem thêm bài _AWS Direct Connect Product Page_
  trong mục Tài liệu tham khảo.
- **VPC Endpoint** là một thiết bị ảo cho phép ta kết nối riêng VPC của mình
  với các dịch vụ AWS được hỗ trợ
  và dịch vụ VPC Endpoint được cung cấp bởi **AWS PrivateLink**.
  Kết nối với các dịch vụ này không yêu cầu cổng internet, thiết bị NAT,
  kết nối VPN hoặc kết nối **AWS Direct Connect**.
  Các instance trong VPC của ta không yêu cầu địa chỉ IP công cộng
  để giao tiếp với các tài nguyên trong dịch vụ.
  Lưu lượng truy cập giữa VPC của ta và dịch vụ khác không rời khỏi mạng Amazon.
  Có 2 loại VPC endpoint: **Interface VPC Endpoint** và **Gateway Endpoints**.
  Để hiểu chi tiết hơn ta có thể xem thêm bài viết **Interface Endpoints**
  và **VPC endpoints** trong mục Tài liệu tham khảo.
- Với **AWS Transit Gateway**, ta chỉ cần tạo và quản lý một kết nối duy nhất
  từ cổng trung tâm vào từng VPC, trung tâm dữ liệu on-premises hoặc văn phòng
  từ xa trên toàn mạng của ta.
  Cổng chuyển tuyến hoạt động như một trung tâm kiểm soát cách lưu lượng được
  định tuyến giữa tất cả các mạng được kết nối, hoạt động giống như nan hoa.
  Mô hình hub-and-spoke này giúp đơn giản hóa đáng kể việc quản lý
  và giảm chi phí vận hành vì mỗi mạng chỉ cần kết nối với cổng chuyển tuyến
  chứ không cần kết nối với mọi mạng khác.
  Mọi VPC mới đều được kết nối với cổng chuyển tuyến
  và sau đó sẽ tự động khả dụng cho mọi mạng khác được kết nối
  với cổng chuyển tuyến. Khả năng kết nối dễ dàng này giúp mở rộng mạng của ta
  dễ dàng hơn khi ta phát triển.
- Video: [VPC Networking](https://awsacademy.instructure.com/courses/313/modules/items/48833)

#### VPC Security

- Một **Security Group** hoạt động như một bức tường lửa ảo
  cho ví dụ của ta và nó kiểm soát lưu lượng truy cập vào và ra.
  Các Security Group hoạt động ở cấp Instance , không phải cấp subnet.
  Do đó, mỗi Instance trong Subnet trong VPC của ta có thể được gán
  cho một security group khác nhau. Ở cấp độ cơ bản nhất,
  Security Group là một cách để ta lọc lưu lượng truy cập
  vào các Instance của mình.
- **Network ACL** là lớp bảo mật tùy chọn cho Amazon VPC của ta.
  Nó hoạt động như một bức tường lửa để kiểm soát lưu lượng truy cập
  vào và ra khỏi một hoặc nhiều Subnet. Để thêm một lớp bảo mật khác vào VPC,
  ta có thể thiết lập Network ACL với các quy tắc tương tự như các
  Security Group của ta.
- Dưới đây là tóm tắt về **sự khác biệt giữa các Security Group và Network ACL**:
  - Security Group hoạt động ở cấp Instance,
    nhưng Network ACL hoạt động ở cấp subnet.
  - Security Group chỉ hỗ trợ allow rule,
    nhưng Network ACL hỗ trợ cả allow và deny rule.
  - Security Group là stateful, nhưng Network ACL là stateless.
  - Đối với Security Group, tất cả các rule được đánh giá
    trước khi đưa ra quyết định cho phép lưu lượng truy cập.
    Đối với Network ACL, các rule được đánh giá theo thứ tự số
    trước khi đưa ra quyết định cho phép lưu lượng.
- Video: [VPC Security](https://awsacademy.instructure.com/courses/313/modules/items/48834)

#### Document references

##### Bastion Host/Jump Box:

- Là máy chủ có mục đích cung cấp quyền truy cập vào mạng internal
  từ mạng external, chẳng hạn như Internet. Do có khả năng bị tấn công,
  bastion host/jump box phải giảm thiểu cơ hội xâm nhập.
- Ví dụ: ta có thể sử dụng bastion host/jump box để giảm thiểu rủi ro cho phép
  kết nối SSH từ mạng external với các Linux Instance được khởi chạy trong
  private subnet của Amazon Virtual Private Cloud (VPC) của ta.
- ![Diagram showing how bastion host users connect to the bastion host to connect to the Linux instances](https://dmhnzl5mp9mj6.cloudfront.net/security_awsblog/images/NM_diagram_061316_a.png)

##### Tài liệu đọc: Các tài liệu dưới đây giúp ta xem và hiểu rõ hơn:

- [AWS VPC (trang 1 đến trang 35)](https://drive.google.com/file/d/1DrY93AaOYVMcNB498ZA5hcHpwI8g5Wge/view)
- [IP Addressing in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html)
- [Elastic IP Addresses](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html)
- [Elastic network interface](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ElasticNetworkInterfaces.html)
- [Route table and routes](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
- [Internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
- [NAT Instances](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_NAT_Instance.html)
- [NAT Gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
- [Compare NAT gateways and NAT instances](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html)
- [VPC peering](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-peering.html)
- [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpc/latest/userguide/vpn-connections.html)
- [AWS Direct Connect product page](https://aws.amazon.com/directconnect/)
- [Interface endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-services-overview.html)
- [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html)

### Lab 3

- Lab 3.1: [Console Demonstration - VPC Wizard](https://awsacademy.instructure.com/courses/77750/modules/items/7000855)
- Lab 3.2: [Lab2 AWS](https://awsacademy.instructure.com/courses/77750/modules/items/7000869)

### AWS CDN

#### Route 53

- Amazon Route 53 là dịch vụ web Hệ thống tên miền (Domain Name System - DNS)
  đám mây có khả năng mở rộng cao.
  Nó được thiết kế để cung cấp cho các nhà phát triển và doanh nghiệp
  một giải pháp đáng tin cậy và tiết kiệm chi phí để định tuyến người dùng đến
  các ứng dụng Internet bằng cách dịch tên (như www.example.com) thành địa chỉ
  IP số (như 192.0.2.1) mà các máy tính sử dụng để kết nối với nhau.
  **Amazon Route 53** kết nối hiệu quả các yêu cầu của người dùng với
  cơ sở hạ tầng chạy trong AWS chẳng hạn như **Amazon EC2 instance**,
  bộ cân bằng tải **Elastic Load Balancing** hoặc **Amazon S3 bucket** và
  cũng có thể được sử dụng để định tuyến người dùng đến cơ sở hạ tầng
  nằm ngoài AWS. Bạn có thể sử dụng Amazon Route 53 để định cấu hình kiểm tra
  tình trạng DNS để ta có thể định tuyến lưu lượng truy cập đến các điểm cuối
  lành mạnh hoặc theo dõi độc lập tình trạng ứng dụng của ta
  và các điểm cuối của nó.

- Amazon Route 53 hỗ trợ một số loại chính sách định tuyến,
  giúp xác định cách Amazon Route 53 phản hồi các truy vấn:
  - Simple Routing (Round Robin)
  - Weighted Round Robin Routing
  - Latency Routing (LBR)
  - Geolocation Routing
  - Geoproximity Routing
  - Failover Routing (DNS Failover)
  - Multivalue Answer Routing
- **Amazon Route 53** cho phép ta cải thiện tính khả dụng
  của các ứng dụng chạy trên AWS của mình bằng cách:
  - Cấu hình sao lưu và chuyển đổi dự phòng cho các ứng dụng của riêng ta.
  - Kích hoạt các kiến trúc Multi-Region trên AWS.
  - Tạo kiểm tra tình trạng để theo dõi tình trạng và hiệu suất của
    các ứng dụng web, máy chủ web và các tài nguyên khác của ta.
    Mỗi lần kiểm tra tình trạng mà ta tạo có thể theo dõi một trong
    những điều sau — tình trạng của tài nguyên cụ thể,
    chẳng hạn như máy chủ web; trạng thái của các lần kiểm tra sức khỏe khác;
    và trạng thái của cảnh báo Amazon CloudWatch.
- Video: [Route 53](https://awsacademy.instructure.com/courses/77750/modules/items/7000861)

#### Amazon CloudFront

- Như đã giải thích trước đó khi ta tìm hiểu về AWS Direct Connect,
  một trong những thách thức của giao tiếp mạng là hiệu suất mạng.
  Khi ta duyệt một trang web hoặc phát trực tuyến video,
  yêu cầu của ta được chuyển qua nhiều mạng khác nhau để đến máy chủ nguồn.
  Máy chủ gốc (hoặc nguồn gốc) lưu trữ các Instance gốc,
  cuối cùng của các đối tượng (trang web, hình ảnh và tệp phương tiện).
  Số lượng các bước nhảy mạng và khoảng cách mà yêu cầu phải di chuyển
  ảnh hưởng đáng kể đến hiệu suất và **khả năng đáp ứng** của trang web.
  Hơn nữa, độ trễ của mạng là khác nhau ở các vị trí địa lý khác nhau.
  Vì những lý do này, mạng phân phối nội dung có thể là giải pháp.
- **Mạng phân phối nội dung (Content Delivery Network - CDN)**
  là một hệ thống máy chủ lưu trữ bộ nhớ đệm được phân phối trên toàn cầu.
  CDN lưu trữ bản sao của các tệp thường được yêu cầu được lưu trữ
  trên máy chủ gốc ứng dụng. CDN cung cấp một bản sao cục bộ của nội dung
  được yêu cầu từ một cạnh trong bộ nhớ cache hoặc Point of Presence
  để cung cấp khả năng phân phối nhanh nhất cho người yêu cầu.
- Amazon CloudFront là một dịch vụ CDN nhanh chóng cung cấp một cách an toàn
  dữ liệu, video, ứng dụng và giao diện lập trình ứng dụng
  (Application Programming Interface - API) cho khách hàng trên toàn cầu
  với độ trễ thấp và tốc độ truyền cao, đồng thời cung cấp một môi trường
  thân thiện với nhà phát triển.
  **Amazon CloudFront** cung cấp tệp cho người dùng qua mạng toàn cầu
  gồm các vị trí biên và bộ nhớ đệm cạnh Khu vực.
  Amazon CloudFront khác với các giải pháp phân phối nội dung truyền thống
  vì nó cho phép ta nhanh chóng nhận được lợi ích của việc phân phối nội dung
  hiệu suất cao mà không cần thỏa thuận hợp đồng, giá cao hoặc phí tối thiểu.
  Giống như các dịch vụ AWS khác, Amazon CloudFront
  là một dịch vụ tự phục vụ với giá tùy chọn.
- Amazon CloudFront cung cấp nội dung _thông qua mạng lưới các trung tâm dữ liệu_
  trên toàn thế giới được gọi là các vị trí biên.
  Khi người dùng yêu cầu nội dung mà ta phân phối bằng CloudFront,
  người dùng sẽ được chuyển đến vị trí biên cung cấp độ trễ thấp nhất
  (hoặc độ trễ thời gian) để nội dung được phân phối với hiệu suất
  tốt nhất có thể. Các vị trí biên CloudFront được thiết kế để phân phát
  nội dung phổ biến một cách nhanh chóng cho người xem của ta.
  Để tìm hiểu chi tiết hơn ta có thể xem thêm bài viết
  _How CloudFront Delivers Content_ trong mục Tài liệu tham khảo.
- Video: [CloudFront](https://awsacademy.instructure.com/courses/77750/modules/items/7000863)
- Video: [Ví dụ tạo một CloudFront Formation](https://funix.udemy.com/course/awsnetworking/learn/lecture/16435272#overview)

#### Document references

- [Content Delivery (từ trang 36 đến hết)](https://docs.google.com/document/d/1jeT4HWnhUic86ZJq2aBTt41_X-hSIokv1b1UeJZjBVc/view)
- [How CloudFront delivers content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html#HowCloudFrontWorksContentDelivery)

### AWS EC2

#### Computer Services

- **Amazon Web Services (AWS)** cung cấp nhiều **dịch vụ máy tính**.
  Đây là bản tóm tắt ngắn gọn về những gì mà mỗi dịch vụ máy tính cung cấp:
  Amazon EC2, Amazon ECR, Amazon ECS, Amazon EKS, VMware Cloud on AWS,
  AWS Elastic Beanstalk, AWS Lambda, Amazon Lightsail, AWS Batch, AWS Fargate,
  AWS Outposts, AWS Serverless Application Repository.

- Ta có thể coi mỗi dịch vụ tính toán AWS thuộc một trong **bốn danh mục lớn**:

  - Virtual machines (VMs) cung cấp cơ sở hạ tầng như một dịch vụ (IaaS)
  - serverless
  - container-based
  - nền tảng như một dịch vụ (PaaS).

- Amazon EC2 cung cấp các **VMs** và ta có thể coi nó là cơ sở hạ tầng
  như một dịch vụ (IaaS). Dịch vụ IaaS cung cấp sự linh hoạt
  và để lại nhiều trách nhiệm quản lý máy chủ cho ta.

- AWS Lambda là một nền tảng máy tính không quản trị,
  ta có thể coi nó là **Serverless**.
  AWS Lambda cho phép ta chạy code mà không cần cung cấp hay quản lý máy chủ.

- **Container-Based**

  - bao gồm
    - Amazon Elastic Container Service
    - Amazon Elastic Kubernetes Service
    - AWS Fargate và Amazon Elastic Container Registry
  - cho phép ta chạy nhiều khối lượng công việc
    trên một hệ điều hành (OS) duy nhất.

- Cuối cùng, AWS Elastic Beanstalk cung cấp nền tảng như một dịch vụ (PaaS),
  tạo điều kiện triển khai nhanh chóng các ứng dụng mà ta tạo bằng cách cung cấp
  tất cả các dịch vụ ứng dụng mà ta cần. AWS quản lý hệ điều hành,
  máy chủ ứng dụng và các thành phần cơ sở hạ tầng khác để ta có thể
  tập trung vào việc phát triển mã ứng dụng của mình.

- Video: [Tổng quan về Compute](https://awsacademy.instructure.com/courses/77750/modules/items/7000876)

#### EC2

- Các bước để **khởi tạo một EC2 trên EC2 console**,
  các thành phần cần để tạo nên một EC2
  như AMI, Instance Type, Network Setting, Key Pair,...
- **Amazon Elastic Compute Cloud (Amazon EC2)**
  cung cấp các máy ảo nơi ta có thể lưu trữ các loại ứng dụng tương tự mà ta
  có thể chạy trên một máy chủ On-Premises truyền thống.
  Nó cung cấp khả năng tính toán an toàn,
  có thể thay đổi kích thước trên đám mây.
  Các EC2 instance có thể hỗ trợ nhiều khối lượng công việc khác nhau
- Amazon EC2 cung cấp các máy ảo trên đám mây và cung cấp cho ta toàn quyền
  kiểm soát quản trị đối với hệ điều hành Windows hoặc Linux
  chạy trên Instance đó. Hầu hết các hệ điều hành máy chủ được hỗ trợ,
  bao gồm: Windows 2008, 2012, 2016 và 2019,
  Red Hat, SuSE, Ubuntu và Amazon Linux
- Với Amazon EC2, ta có thể khởi chạy bất kỳ instance nào
  ở bất kỳ kích thước nào vào bất kỳ Availability Zone nào
  ở bất kỳ đâu trên thế giới chỉ trong vài phút.
  Các Instance khởi chạy từ Amazon Machine Images (AMI),
  đây là những mẫu máy ảo hiệu quả.
  Chi tiết hơn ta có thể xem thêm tại mục Tài liệu tham khảo.
- Ta có thể kiểm soát lưu lượng truy cập đến
  và đi từ các instance bằng cách sử dụng các Security Groups.
- Video: [AWS EC2 Phần 1](https://awsacademy.instructure.com/courses/77750/modules/items/7000878)
- Video: [AWS EC2 Phần 2](https://awsacademy.instructure.com/courses/77750/modules/items/7000880)
- Video: [AWS EC2 Phần 3](https://awsacademy.instructure.com/courses/77750/modules/items/7000882)

#### Document references

- [Tổng quan về EC2 (từ trang 1 đến trang 61)](https://drive.google.com/file/d/1q3t5yqq81FhF4rw8nS23XzFgWqgrT4zA/view)

### Lab 4

- Lab 4.1:
- Lab 4.2: [Lab 3 AWS Academy](https://awsacademy.instructure.com/courses/77750/modules/items/7000885)
  [Vietsub](https://docs.google.com/document/d/189z1KplQpBL1Uyben7xiPwfeM9EFLSOI/view)

### Serverless

#### Serverless Application Model

- Mô hình Serverless Application (SAM)
  một Framework để phát triển và triển khai các ứng dụng Serverless.
- **AWS Serverless Application Model (SAM)**
  là một open-source framework để xây dựng các ứng dụng serverless.
  Nó cung cấp cú pháp viết tắt để diễn đạt các hàm, API, cơ sở dữ liệu
  và ánh xạ nguồn sự kiện. Chỉ với một vài dòng trên mỗi tài nguyên,
  bạn có thể xác định ứng dụng bạn muốn và lập mô hình ứng dụng đó bằng YAML.
  Trong quá trình triển khai, SAM chuyển đổi và mở rộng cú pháp SAM
  thành cú pháp AWS CloudFormation,
  cho phép bạn xây dựng các ứng dụng serverless nhanh hơn.
- Để bắt đầu xây dựng các ứng dụng dựa trên SAM, hãy sử dụng **AWS SAM CLI**.
  SAM CLI cung cấp môi trường thực thi giống như Lambda cho phép bạn xây dựng,
  kiểm tra và gỡ lỗi cục bộ các ứng dụng được xác định bởi mẫu SAM
  hoặc thông qua Bộ phát triển đám mây AWS (CDK).
  Bạn cũng có thể sử dụng SAM CLI để triển khai các ứng dụng của mình
  lên AWS hoặc tạo các pipeline tích hợp và triển khai (CI/CD) liên tục an toàn
  tuân theo các phương pháp hay nhất và tích hợp với hệ thống CI/CD
  của bên thứ ba của AWS.
- SAM và SAM CLI có nguồn mở theo giấy phép Apache 2.0.
  Bạn có thể đóng góp các tính năng và cải tiến mới cho SAM trên GitHub
  hoặc SAM CLI trên GitHub.
  Bạn có thể xem thêm AWS SAM và AWS SAM CLI ở mục Tài liệu tham khảo.
- Video: [Serverless Application Model](https://funix.udemy.com/course/aws-certified-developer-associate-dva-c01/learn/lecture/11851436#overview)

#### Elastice Container Services

- **Container** là một phương pháp ảo hóa hệ điều hành cho phép ta chạy
  một ứng dụng và các phần phụ thuộc của nó trong các quy trình
  bị cô lập về tài nguyên. Bằng cách sử dụng container, ta có thể dễ dàng
  đóng gói mã, cấu hình và phần phụ thuộc của ứng dụng thành các khối xây dựng
  dễ sử dụng mang lại tính nhất quán về môi trường, hiệu quả hoạt động,
  năng suất của nhà phát triển và kiểm soát Instance.

- **Container nhỏ hơn máy ảo** và không chứa toàn bộ hệ điều hành.
  Thay vào đó, các container chia sẻ một hệ điều hành được ảo hóa
  và chạy dưới dạng các quy trình cách ly tài nguyên,
  đảm bảo triển khai nhanh chóng, đáng tin cậy và nhất quán.
  container chứa mọi thứ mà phần mềm cần để chạy,
  chẳng hạn như thư viện, công cụ hệ thống, mã và thời gian chạy.

- **Docker** là một nền tảng phần mềm đóng gói phần mềm
  (chẳng hạn như ứng dụng) vào các container.
  Docker được cài đặt trên mỗi máy chủ sẽ lưu trữ các container
  và nó cung cấp các lệnh đơn giản mà ta có thể sử dụng để xây dựng,
  bắt đầu hoặc dừng các container.
  Bằng cách sử dụng Docker, ta có thể nhanh chóng triển khai
  và mở rộng ứng dụng vào bất kỳ môi trường nào.

- Nhiều người lần đầu tiên làm quen với khái niệm container
  nghĩ rằng container giống hệt như máy ảo.
  Tuy nhiên, sự khác biệt là ở các chi tiết.
  Một _điểm khác biệt_ đáng kể là các máy ảo chạy trực tiếp trên một supervisor,
  nhưng các container có thể chạy trên bất kỳ hệ điều hành Linux nào
  nếu chúng có hỗ trợ tính năng hạt nhân thích hợp và có mặt daemon Docker.
  Điều này làm cho các container rất dễ di chuyển.
  Máy tính xách tay, máy ảo của ta, instance EC2 và bare-metal của ta
  đều là các máy chủ tiềm năng mà ta có thể chạy một container.

- **Amazon Elastic Container Service (Amazon ECS)**
  là một dịch vụ quản lý container hiệu suất cao,
  có khả năng mở rộng cao, hỗ trợ các container Docker.

- **Kubernetes** là phần mềm nguồn mở để điều phối container.
  Kubernetes có thể hoạt động với nhiều công nghệ container hóa,
  bao gồm cả Docker.
  Bởi vì đây là dự án mã nguồn mở thông thường, một cộng đồng lớn
  các nhà phát triển và công ty xây dựng các tiện ích mở rộng,
  tích hợp và bổ sung để giữ cho phần mềm có liên quan và các tính năng mới
  và theo yêu cầu được bổ sung thường xuyên.

- Kubernetes cho phép ta **triển khai và quản lý các ứng dụng**
  được đóng gói trên quy mô lớn.
  Với Kubernetes, ta có thể chạy bất kỳ loại ứng dụng được chứa nào
  bằng cách sử dụng cùng một bộ công cụ trong cả trung tâm dữ liệu
  on-premises và đám mây.
  Kubernetes quản lý các cluster của _compute instance(được gọi là các nút)_.
  Nó chạy các container trên cluster, dựa trên nơi có sẵn tài nguyên tính toán
  và yêu cầu tài nguyên của mỗi container.
  Các container được chạy theo _các nhóm logic được gọi là pods_.
  Bạn có thể chạy và chia tỷ lệ một hoặc nhiều container với nhau
  dưới dạng một pods. Mỗi nhóm được cấp một địa chỉ IP
  và một tên Hệ thống tên miền (DNS) duy nhất mà Kubernetes sử dụng để kết nối
  các dịch vụ của ta với nhau và lưu lượng truy cập bên ngoài.

- Một ưu điểm chính của Kubernetes là ta có thể sử dụng nó để chạy các ứng dụng
  được chứa trong container của mình ở **bất cứ đâu** mà không cần thay đổi công cụ
  hoạt động của mình.
  Ví dụ: các ứng dụng có thể được chuyển từ các máy phát triển cục bộ tại chỗ
  sang triển khai sản xuất trên đám mây bằng cách sử dụng
  cùng một công cụ hoạt động.

- **Amazon Elastic Kubernetes Service (Amazon EKS)** là một dịch vụ Kubernetes
  được quản lý giúp ta dễ dàng chạy Kubernetes trên AWS mà không cần cài đặt,
  vận hành và bảo trì máy bay điều khiển Kubernetes của riêng ta.
  Nó được chứng nhận tuân thủ Kubernetes, vì vậy các ứng dụng hiện có chạy
  trên Kubernetes ngược dòng tương thích với Amazon EKS.

- **Amazon Elastic Container Registry (Amazon ECR)** là một cơ quan
  đăng ký container Docker được quản lý hoàn toàn giúp các nhà phát triển
  dễ dàng lưu trữ, quản lý và triển khai hình ảnh container Docker.
  Nó được tích hợp với Amazon ECS, vì vậy ta có thể lưu trữ, chạy và quản lý
  hình ảnh container cho các ứng dụng chạy trên Amazon ECS.
  Chỉ định kho lưu trữ Amazon ECR trong định nghĩa nhiệm vụ của ta
  và Amazon ECS sẽ truy xuất các hình ảnh thích hợp cho các ứng dụng của ta.

- Video: [Giới thiệu Elastic Container Services](https://awsacademy.instructure.com/courses/77750/modules/items/7000890)

#### Amazon Lambda

- AWS Lambda là một dịch vụ máy tính serverless, hướng sự kiện.
  **Lambda cho phép ta chạy code mà không cần cung cấp hoặc quản lý máy chủ**.
  Ta tạo hàm Lambda, là tài nguyên AWS có chứa code mà ta tải lên.
  Sau đó, ta đặt hàm Lambda để được kích hoạt, trên một sự kiện đã lên lịch
  để phản hồi một sự kiện. Code của ta chỉ chạy khi được kích hoạt.
  Ta chỉ trả tiền cho thời gian tính toán mà ta sử dụng ta **không bị tính phí**
  khi code của ta không chạy.

- Với Lambda, **không có ngôn ngữ, công cụ hoặc frameworks mới nào để học**.
  Lambda hỗ trợ nhiều ngôn ngữ lập trình, bao gồm Java, Go, PowerShell, Node.js,
  C\#, Python và Ruby. **Lambda hoàn toàn tự động hóa việc quản trị**.
  Nó quản lý tất cả cơ sở hạ tầng để chạy code của ta trên cơ sở hạ tầng
  có khả năng chịu lỗi cao, cho phép ta tập trung vào việc xây dựng các dịch vụ
  phụ trợ khác biệt. Lambda cung cấp **khả năng chịu lỗi tích hợp**.
  Nó duy trì khả năng tính toán trên nhiều Availability Zones ở mỗi Region
  để giúp bảo vệ code của ta khỏi các lỗi máy riêng lẻ
  hoặc lỗi trung tâm dữ liệu. Ta **sắp xếp nhiều chức năng Lambda**
  cho các tác vụ phức tạp hoặc lâu dài bằng cách xây dựng quy trình làm việc
  với AWS Step Functions. Với Lambda, ta **chỉ trả tiền cho các yêu cầu**
  được cung cấp và thời gian tính toán cần thiết để chạy code của ta.

- **Nguồn sự kiện** là một dịch vụ AWS hoặc ứng dụng do nhà phát triển tạo
  để tạo ra các sự kiện kích hoạt chức năng AWS Lambda chạy.
  Một số dịch vụ xuất bản các sự kiện lên Lambda bằng cách
  gọi trực tiếp hàm Lambda. Các dịch vụ này gọi các chức năng
  Lambda asynchronously, nhưng không giới hạn ở Amazon S3,
  Amazon Simple Notification Service (Amazon SNS) và Amazon CloudWatch Events.

- Video: [Giới thiệu AWS Lambda](https://awsacademy.instructure.com/courses/77750/modules/items/7000892)

- Video: [Giới thiệu AWS Elastic Beanstalk](https://awsacademy.instructure.com/courses/77750/modules/items/7000896)

#### Document references

- [Cơ bản về Serverless (từ trang 62 đến hết)](https://drive.google.com/file/d/1q3t5yqq81FhF4rw8nS23XzFgWqgrT4zA/view)
- [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-reference.html#serverless-sam-cli)

### Lab 5

- Lab 5.1: [Activity - AWS Lambda](https://awsacademy.instructure.com/courses/77750/modules/items/7000894)
  [Vietsub](https://docs.google.com/document/d/18ETNvSpR8zHCoxiWI6JYu_a5nm49_AmT/view)
- Lab 5.2: [Activity - AWS Elastic Beanstalk](https://awsacademy.instructure.com/courses/77750/modules/items/7000899)
  [Vietsub](https://docs.google.com/document/d/18Gu5dth5GXN1I_c6PyQFQuykZSs5EZ0r/view)

### AWS EBS

#### Elastic Block Store

- Cung cấp volume block storage liên tục để sử dụng với Amazon EC2 Instance.
  Lưu trữ liên tục là bất kỳ thiết bị lưu trữ dữ liệu nào lưu giữ dữ liệu
  sau khi nguồn điện cho thiết bị đó bị tắt.
  Nó cũng đôi khi được gọi là non-volatile storage.
  Mỗi Amazon EBS volume được sao chép tự động với Availability Zone
  để bảo vệ ta khỏi lỗi thành phần.
  Nó được thiết kế để có tính khả dụng và độ bền cao.
  Amazon EBS volume cung cấp hiệu suất nhất quán và độ trễ thấp cần thiết
  để chạy volume công việc của ta.
  Với Amazon EBS, ta có thể tăng hoặc giảm mức sử dụng của mình
  trong vòng vài phút, trong khi chỉ trả một mức giá thấp
  cho những gì ta cung cấp.

- Điều gì xảy ra nếu ta muốn thay đổi một ký tự trong tệp 1 GB?
  Với **Block Storage**, ta chỉ thay đổi block chứa ký tự.
  Với **Object Storage**, toàn bộ tệp phải được cập nhật.
  Một điểm khác biệt quan trọng giữa một số loại lưu trữ
  là chúng cung cấp lưu trữ cấp block-level hay lưu trữ cấp object-level.
  Sự khác biệt này có ảnh hưởng lớn đến thông lượng, độ trễ và chi phí
  của giải pháp lưu trữ của ta. Các giải pháp block storage thường nhanh hơn
  và sử dụng ít băng thông hơn, nhưng chúng có thể tốn nhiều tiền hơn
  so với lưu trữ cấp đối tượng.

- Amazon EBS cho phép ta tạo các storage block riêng lẻ và đính kèm chúng
  vào một Amazon EC2 Instance. **Amazon EBS cung cấp bộ nhớ cấp Block Storage**,
  nơi các volume của nó được tự động sao chép trong Availability Zone của nó.
  Amazon EBS được thiết kế để cung cấp khả năng lưu trữ cấp block storage,
  có thể tháo rời (giống như ổ cứng gắn ngoài)
  cho các Amazon EC2 Instance của ta.
  Bởi vì chúng được gắn trực tiếp vào các Instance,
  chúng có thể cung cấp độ trễ thấp giữa nơi dữ liệu được lưu trữ
  và nơi nó có thể được sử dụng trên Instance.
  Vì lý do này, chúng có thể được sử dụng để chạy cơ sở dữ liệu
  với Amazon EC2 Instance.
  Volume Amazon EBS được bao gồm như một phần
  của quá trình sao lưu các Instance của ta vào AMI.
  **AMI được lưu trữ trong Amazon S3 và có thể được sử dụng lại**
  để tạo các Amazon EC2 Instance mới sau này.
  Xem thêm tài liệu Amazon EBS volume types trong mục Tài liệu tham khảo.

- Để **cung cấp mức độ bền dữ liệu cao hơn nữa**, Amazon EBS cho phép
  ta tạo point-in-time snapshots các volume của mình
  và ta có thể tạo lại một volume mới từ snapshots bất kỳ lúc nào.
  Ta cũng có thể chia sẻ snapshots hoặc thậm chí sao chép snapshots
  sang các AWS Region khác nhau để bảo vệ khả năng
  phục hồi sau thảm họa (DR) tốt hơn.
  Ví dụ: ta có thể mã hóa và chia sẻ snapshots của mình
  từ Virginiain Mỹ đến Tokyo, Nhật Bản.
  Ta cũng có thể có Amazon EBS volume được mã hóa mà không phải trả thêm phí,
  vì vậy dữ liệu di chuyển giữa EC2 Instance và EBS volume
  bên trong trung tâm dữ liệu AWS được mã hóa khi truyền.
  Khi công ty của ta phát triển, lượng dữ liệu được lưu trữ
  trên các EBS volume của ta cũng có khả năng tăng lên.
  Ổ đĩa Amazon EBS có thể tăng dung lượng và thay đổi thành các loại khác nhau,
  vì vậy ta có thể thay đổi từ ổ đĩa cứng (HDD) sang ổ trạng thái rắn (SSD)
  hoặc tăng từ ổ 50 GB lên 16 TB.
  Ví dụ: ta có thể thực hiện thao tác thay đổi kích thước này một cách động
  mà không cần dừng các Instance.

- Khi bắt đầu ước tính chi phí cho Amazon EBS, ta phải cân nhắc những điều sau:

  - Volumes
    Volume storage cho tất cả các loại Amazon EBS volume
    được tính phí bằng số tiền ta cung cấp tính bằng GB mỗi tháng,
    cho đến khi ta giải phóng bộ nhớ.
  - IOPS
    I/O được bao gồm trong giá của General Purpose SSD volumes.
    Tuy nhiên, đối với ổ đĩa từ tính của Amazon EBS,
    I/O được tính phí theo số lượng yêu cầu mà ta thực hiện
    đối với volume của mình. Với khối lượng SSD IOPS được cung cấp,
    ta cũng bị tính phí bằng số tiền ta cung cấp trong IOPS
    (nhân với phần trăm số ngày mà ta cung cấp trong tháng).
  - Snapshot
    Amazon EBS cho phép ta sao lưu dữ liệu snapshot của ta vào Amazon S3
    để lưu trữ lâu dài. Nếu ta chọn Snapshot Amazon EBS,
    chi phí cộng thêm là cho mỗi GB-tháng dữ liệu được lưu trữ.
  - Truyền dữ liệu
    Khi ta sao chép Snapshot Amazon EBS, ta sẽ bị tính phí cho dữ liệu
    được truyền qua các Region. Sau khi Snapshot được sao chép,
    các khoản phí Snapshot Amazon EBS tiêu chuẩn
    sẽ áp dụng cho bộ nhớ trong Region đích.

- Video: [AWS EBS](https://awsacademy.instructure.com/courses/77750/modules/items/7000910)

- Thao tác với giao diện AWS Console sẽ giúp ta hiểu rõ hơn về EBS:
  Video: [Ví dụ EBS](https://awsacademy.instructure.com/courses/77750/modules/items/7000912)

#### Elastic File System

- EFS (Elastic File System) và triển khai lưu trữ cho các EC2 Instances có thể truy cập cùng một lúc.

- **Amazon EFS** cung cấp khả năng lưu trữ tệp đơn giản, có thể mở rộng,
  linh hoạt để sử dụng với các dịch vụ AWS và tài nguyên on-premises.
  Nó cung cấp một giao diện đơn giản cho phép ta tạo
  và cấu hình các hệ thống tệp một cách nhanh chóng và dễ dàng.
  EFS được thiết kế để các ứng dụng của ta có dung lượng lưu trữ
  cần thiết khi họ cần.

- Amazon EFS là một dịch vụ được quản lý hoàn toàn **giúp dễ dàng thiết lập**
  **và mở rộng quy mô lưu trữ** tệp trong Đám mây AWS.
  Ta có thể sử dụng Amazon EFS để xây dựng hệ thống tệp cho bigdata
  và analytics, quy trình xử lý phương tiện, quản lý nội dung, phục vụ web
  và thư mục gia đình. Ta có thể tạo hệ thống tệp có thể truy cập
  vào các Amazon EC2 Instance thông qua giao diện hệ thống tệp
  (sử dụng các API I/O). Các hệ thống tệp này hỗ trợ ngữ nghĩa
  truy cập hệ thống tệp đầy đủ, chẳng hạn như tính nhất quán mạnh mẽ
  và khóa tệp. Hệ thống tệp của Amazon EFS có thể tự động thay đổi tỷ lệ
  từ gigabyte đến petabyte dữ liệu mà không cần cung cấp bộ nhớ.
  Hàng nghìn Amazon EC2 Instance có thể truy cập hệ thống tệp Amazon EFS
  cùng một lúc và Amazon EFS được thiết kế để cung cấp hiệu suất nhất quán
  cho từng Amazon EC2 Instance. Amazon EFS cũng được thiết kế để có độ bền cao
  và tính khả dụng cao. Amazon EFS không yêu cầu phí tối thiểu
  hoặc chi phí thiết lập và ta chỉ phải trả cho bộ nhớ mà ta sử dụng.

- Amazon EFS cung cấp dịch vụ lưu trữ tệp trên đám mây.
  Với Amazon EFS, ta có thể **tạo hệ thống tệp**,
  **gắn kết hệ thống tệp** trên Amazon EC2 Instance,
  sau đó đọc và ghi dữ liệu từ và đi từ hệ thống tệp của ta.
  Ta có thể gắn hệ thống tệp Amazon EFS trong VPC của mình,
  thông qua phiên bản NFS (Network File System) 4.0 và 4.1 (NFSv4).
  Ta có thể truy cập đồng thời vào hệ thống tệp Amazon EFS của mình
  từ các Amazon EC2 Instance trong VPC của ta,
  vì vậy các ứng dụng có quy mô vượt quá một kết nối duy nhất
  có thể truy cập vào hệ thống tệp.
  Các Amazon EC2 Instance chạy trong nhiều Availability Zones
  trong cùng một AWS Region có thể truy cập vào hệ thống tệp,
  vì vậy nhiều người dùng có thể truy cập và chia sẻ nguồn dữ liệu chung.

- Trong Amazon EFS, **hệ thống tệp là tài nguyên chính**.
  Mỗi hệ thống tệp có các thuộc tính như: ID, Creation token, Creation time,
  File system size in bytes, Number of mount targets được tạo cho hệ thống tệp,
  File system state. Amazon EFS cũng hỗ trợ các tài nguyên khác
  để định cấu hình tài nguyên chính.
  Các tài nguyên này bao gồm gắn kết các mục tiêu và thẻ.

- **Mount Target**: Để truy cập hệ thống tệp của ta,
  ta phải tạo mục tiêu gắn kết trong VPC của mình.
  Mỗi mục tiêu gắn kết có các thuộc tính sau:

  - ID mục tiêu gắn kết.
  - ID mạng con cho mạng con nơi nó được tạo.
  - ID hệ thống tệp cho hệ thống tệp nơi nó được tạo.
  - Địa chỉ IP nơi hệ thống tệp có thể được gắn kết.
  - the mount target state.
    Xem thêm Amazon Elastic File System ở mục Tài liệu tham khảo.

- Video: [AWS EFS](https://awsacademy.instructure.com/courses/77750/modules/items/7000918)
- Video cuối của bài học sẽ giúp ta hiểu rõ hơn về EFS thông qua giao diện AWS Console:
  Video: [Ví dụ EFS](https://awsacademy.instructure.com/courses/77750/modules/items/7000919)

#### Document references

- [Blob storage và File System (từ trang 1 đến trang 10)](https://drive.google.com/file/d/12jfMZ7g8_moBh7KeBzz__Jjp758gb1L-/view)
- [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html)
- [Amazon Elastic File System](https://aws.amazon.com/efs/)

### Lab 6

- Lab 6: [Lab - 4 Working with EBS](https://awsacademy.instructure.com/courses/77750/modules/items/7000913)
  [Vietsub](https://docs.google.com/document/d/18RGpGa2mmzMXLPEgmRNTSIEeQlyqxPAc/view)

### S3 and Glacier

#### Amazon S3

- Các công ty cần có khả năng thu thập, lưu trữ và phân tích dữ liệu của họ
  trên quy mô lớn một cách đơn giản và an toàn.

- **Amazon S3 là object-level storage**,
  có nghĩa là nếu ta muốn thay đổi một phần của tệp,
  ta phải thực hiện thay đổi và sau đó tải lên lại toàn bộ tệp đã sửa đổi.
  Amazon S3 lưu trữ dữ liệu dưới dạng các object trong các tài nguyên
  **được gọi là bucket**.

- **Amazon S3** là giải pháp lưu trữ đám mây được quản lý được thiết kế
  để mở rộng quy mô liền mạch và cung cấp độ bền 119 giây.
  Ta có thể lưu trữ hầu như bao nhiêu đối tượng tùy thích trong một object
  và ta có thể ghi, đọc và xóa các đối tượng trong object của mình.
  Tên bucket là phổ biến và phải đồng nhất
  với tất cả các tên bucket hiện có trong Amazon S3.
  **Đối tượng có thể có kích thước lên đến 5 TB**.
  Theo mặc định, dữ liệu trong Amazon S3 được lưu trữ dự phòng
  trên nhiều cơ sở và nhiều thiết bị trong mỗi cơ sở.

- Dữ liệu ta lưu trữ trong Amazon S3
  **không được liên kết với bất kỳ máy chủ cụ thể nào**
  và ta **không cần tự quản lý** bất kỳ cơ sở hạ tầng nào.
  Ta có thể đưa bao nhiêu đối tượng vào Amazon S3 tùy thích.
  Amazon S3 chứa hàng nghìn tỷ đối tượng
  và thường xuyên đạt đỉnh hàng triệu yêu cầu mỗi giây.
  Theo mặc định, không có dữ liệu nào của ta được chia sẻ công khai.
  Ta cũng có thể mã hóa dữ liệu của mình khi chuyển tiếp
  và chọn bật mã hóa server-side trên các đối tượng của ta.

- Khi quan sát thấy truy cập không thường xuyên,
  ta có thể dễ dàng tạo chính sách độ tuổi vòng đời mới dựa trên kết quả.
  Phân tích lớp bộ nhớ cũng cung cấp hình ảnh trực quan hàng ngày
  về việc sử dụng bộ nhớ của ta trong Bảng điều khiển quản lý AWS.
  Ta có thể xuất chúng sang Amazon S3 Bucket để phân tích
  bằng cách sử dụng các công cụ thông minh kinh doanh (BI) mà ta chọn,
  chẳng hạn như **Amazon QuickSight**.

- Amazon S3 cung cấp một loạt các lớp lưu trữ cấp đối tượng
  được thiết kế cho các trường hợp sử dụng khác nhau.
  Xem thêm _Amazon S3 Storage Classes_ trong mục Tài liệu tham khảo.
  Các lớp này bao gồm:

  - Amazon S3 Standard
  - Amazon S3 Intelligent-Tiering
  - Amazon S3 Standard-Infrequent Access (Amazon S3 Standard-IA)
  - Amazon S3 One Zone-Infrequent Access (Amazon S3 One Zone-IA)
  - Amazon S3 Glacier
  - Amazon S3 Glacier DeepArchive

- Để sử dụng Amazon S3 một cách hiệu quả,
  ta phải hiểu một vài khái niệm đơn giản.
  Đầu tiên, Amazon S3 lưu trữ dữ liệu bên trong các bucket.
  **Bucket** về cơ bản là tiền tố cho một tập hợp các tệp
  và phải được đặt tên duy nhất trên tất cả Amazon S3 trên toàn cầu.
  Các bucket là các container hợp lý cho các đối tượng.
  Ta có thể có một hoặc nhiều buckets trong tài khoản của mình.
  Ta có thể kiểm soát quyền truy cập cho từng bucket
  — người có thể tạo, xóa và liệt kê các đối tượng trong bucket.
  Ta cũng có thể xem nhật ký truy cập bucket và các đối tượng của nó,
  đồng thời chọn khu vực địa lý nơi Amazon S3 lưu trữ bucket và nội dung của nó.
  Amazon S3 đề cập đến các tệp dưới dạng đối tượng.
  Ngay sau khi ta có một cái bucket,
  ta có thể lưu trữ hầu như bất kỳ số lượng đồ vật nào bên trong nó.
  Một đối tượng bao gồm dữ liệu và bất kỳ siêu dữ liệu nào mô tả tệp đó,
  bao gồm cả URL.
  Để lưu trữ một đối tượng trong Amazon S3,
  ta tải tệp ta muốn lưu trữ lên một bucket.

- Video: [AWS S3](https://awsacademy.instructure.com/courses/77750/modules/items/7000915)

- Video: [Ví dụ S3](https://awsacademy.instructure.com/courses/77750/modules/items/7000917)

#### Amazon S3 Glacier

- **Amazon S3 Glacier** là dịch vụ lưu trữ đám mây an toàn, bền bỉ
  và chi phí cực thấp để lưu trữ dữ liệu và sao lưu lâu dài.

- Khi ta sử dụng Amazon S3 Glacier để lưu trữ dữ liệu, ta có thể lưu trữ dữ liệu
  của mình với chi phí cực kỳ thấp (thậm chí so với Amazon S3),
  nhưng ta **không thể truy xuất dữ liệu của mình ngay lập tức khi ta muốn**.
  Dữ liệu được lưu trữ trong Amazon S3 Glacier có thể mất vài giờ để truy xuất,
  đó là lý do tại sao nó hoạt động tốt để lưu trữ.
  Có **ba thuật ngữ chính** của Amazon S3 Glacier mà ta nên quen thuộc:
  Archive, Vault, Vault access policy.
  Ta có **ba tùy chọn để truy xuất dữ liệu**, mỗi tùy chọn với thời gian
  và chi phí truy cập khác nhau: Expedited, Standard, Bulk.

- **Để lưu trữ và truy cập dữ liệu trong Amazon S3 Glacier**,
  ta có thể sử dụng bảng điều khiển quản lý AWS.
  Tuy nhiên, chỉ một số thao tác — chẳng hạn như tạo và xóa vault
  cũng như tạo và quản lý các chính sách lưu trữ — có sẵn trong bảng điều khiển.
  Đối với hầu hết các hoạt động và tương tác khác với Amazon S3 Glacier,
  ta phải sử dụng Amazon S3 Glacier REST APIs,
  AWS Java hoặc .NET SDK hoặc AWS CLI.
  Ta cũng có thể sử dụng các chính sách vòng đời
  để lưu trữ dữ liệu vào Amazon S3 Glacier.

- Ta nên tự động hóa vòng đời của dữ liệu có trong Amazon S3.
  Bằng cách sử dụng các **chính sách vòng đời**, ta có thể xoay vòng dữ liệu
  theo chu kỳ đều đặn giữa các loại lưu trữ Amazon S3 khác nhau.
  Tự động hóa này làm giảm chi phí tổng thể của ta,
  bởi vì ta trả ít hơn cho dữ liệu
  vì nó trở nên ít quan trọng hơn theo thời gian.
  Ngoài việc đặt quy tắc vòng đời cho mỗi đối tượng,
  ta cũng có thể đặt quy tắc vòng đời cho mỗi bucket.
  Ta có thể xem thêm về Object Lifecycle Management trong mục Tài liệu tham khảo.

- Hãy cẩn thận khi ta quyết định giải pháp lưu trữ nào
  phù hợp với nhu cầu của ta.
  Hai dịch vụ này phục vụ các nhu cầu lưu trữ rất khác nhau.
  **Amazon S3** được thiết kế để truy cập dữ liệu của ta thường xuyên
  với độ trễ thấp, nhưng **Amazon S3 Glacier** được thiết kế để lưu trữ lâu dài
  với chi phí thấp đối với dữ liệu được truy cập không thường xuyên.
  - Kích thước mặt hàng tối đa trong Amazon S3 là 5TB,
    nhưng Amazon S3 Glacier có thể lưu trữ
    các mặt hàng có dung lượng lên đến 40TB.
  - Vì Amazon S3 cho phép ta truy cập dữ liệu của mình nhanh hơn,
    chi phí lưu trữ trên mỗi gigabyte cao hơn so với Amazon S3 Glacier.
  - Mặc dù cả hai dịch vụ đều có phí theo yêu cầu,
    Amazon S3 tính phí cho các hoạt động PUT, COPY, POST, LIST, GET.
    Ngược lại, Amazon S3 Glacier tính phí TẢI LÊN và các thao tác truy xuất.
  - Vì Amazon S3 Glacier được thiết kế để truy cập dữ liệu ít thường xuyên hơn,
    nên chi phí cho mỗi yêu cầu truy xuất cao hơn so với Amazon S3
- Một sự khác biệt quan trọng khác giữa Amazon S3 và Amazon S3 Glacier
  là cách dữ liệu được mã hóa.
  Mã hoá server-side tập trung vào việc bảo vệ dữ liệu ở trạng thái nghỉ.
  Với cả hai giải pháp,
  ta có thể chuyển dữ liệu của mình qua HTTPS một cách an toàn.
  Mọi dữ liệu được lưu trữ trong Amazon S3 Glacier
  đều được mã hóa theo mặc định.
  Với Amazon S3, ứng dụng của ta phải bắt đầu mã hóa server-side.
  Ta có thể thực hiện mã hóa server-side trong Amazon S3 in theo một số cách:
  - Server-side encryption with Amazon S3-managed encryption keys(SSE-S3)
  - Server-side encryption with Customer-provided Encryption Keys (SSE-C)
  - Server-side encryption with AWS Key Management Service(AWS KMS)
- Video: [AWS S3 Glacier](https://awsacademy.instructure.com/courses/77750/modules/items/7000920)

#### Document references

- [S3 và S3 Glacier (từ trang 11 đến hết)](https://drive.google.com/file/d/12jfMZ7g8_moBh7KeBzz__Jjp758gb1L-/view)
- [Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Object lifecycle management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [AWS Storage page](https://aws.amazon.com/products/storage/)
- [Storage Overview](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/storage-services.html)
- [Recovering files from an Amazon EBS volume backup](https://aws.amazon.com/blogs/compute/recovering-files-from-an-amazon-ebs-volume-backup/)
- [Confused by AWS Storage Options? S3, EFS, EBS Explained](https://dzone.com/articles/confused-by-aws-storage-options-s3-ebs-amp-efs-explained)

### Lab 7

- Dùng sandbox
- Lab 7.1: [Console Demonstrations - S3 and EFS](https://awsacademy.instructure.com/courses/77750/modules/items/7000919)
- Lab 7.2: [Console Demonstrations - Glacier](https://awsacademy.instructure.com/courses/77750/modules/items/7000921)

### ELB, Auto Scaling and Monitoring

#### Elastic Load Balancing

- Các trang web hiện đại có lưu lượng truy cập cao phải phục vụ hàng trăm nghìn
  — nếu không phải hàng triệu — yêu cầu đồng thời từ người dùng hoặc khách hàng,
  sau đó trả lại văn bản, hình ảnh, video hoặc dữ liệu ứng dụng chính xác
  một cách nhanh chóng và đáng tin cậy.
  Các máy chủ bổ sung thường được yêu cầu để đáp ứng những khối lượng lớn này.

- Elastic Load Balancing là một dịch vụ AWS phân phối ứng dụng đến
  hoặc lưu lượng mạng trên nhiều Target (mục tiêu)
  — chẳng hạn như các Amazon Elastic Compute Cloud (Amazon EC2) Instance,
  Container, địa chỉ giao thức Internet (IP)
  và các Lambda function trong một Availability Zones duy nhất
  hoặc trên nhiều Availability Zones.
  Elastic Load Balancing cân bằng bộ cân bằng tải của ta khi lưu lượng truy cập
  vào ứng dụng của ta thay đổi theo thời gian.
  Nó có thể tự động mở rộng quy mô thành hầu hết các khối lượng công việc.

- ELB có ba loại:
  - **Application Load Balancer**:
    Tốc độ cân bằng tải ứng dụng ở cấp ứng dụng
    (Open Systems Interconnection, hoặc OSI, model layer 7).
    Nó định tuyến lưu lượng truy cập đến các
    Target Amazon Elastic Compute Cloud (Amazon EC2) Instance, Container,
    địa chỉ Giao thức Internet (IP) và các chức năng Lambda
    dựa trên nội dung của yêu cầu.
  - **Network Load Balancer**:
    Cân bằng tải mạng hoạt động ở cấp độ truyền tải mạng
    (lớp 4 của mô hình OSI), định tuyến kết nối đến các mục tiêu EC2 instance,
    microservices và container dựa trên dữ liệu giao thức IP.
    Nó hoạt động tốt để cân bằng tải cả lưu lượng
    Giao thức điều khiển truyền (TCP) và Giao thức dữ liệu người dùng (UDP).
  - **Classic Load Balancer**:
    cung cấp khả năng cân bằng tải cơ bản trên nhiều EC2 instance
    và nó hoạt động ở cả cấp ứng dụng và cấp truyền tải mạng.
    Cân bằng tải cổ điển hỗ trợ cân bằng tải
    các ứng dụng sử dụng HTTP, HTTPS, TCP và SSL.
- Xêm thêm về sự khác biệt của 3 loại ở _Elastic Load Balancing Features_
  trong mục Tài liệu tham khảo.
- Video: [Elastic Load Balancing](https://awsacademy.instructure.com/courses/77750/modules/items/7000949)
- Chúng ta sẽ đến với giao diện AWS console để đến với một tính năng
  của ELB đó là Health Checks, chúng ta sẽ tìm hiểu khái niệm
  và console cách kết hợp 2 chức năng này.
  Video: [Ví dụ Health Checks](https://funix.udemy.com/course/aws-ec2-masterclass/learn/lecture/9223090#overview)

#### EC2 Auto Scaling

- Scaling là **khả năng tăng hoặc giảm** khả năng tính toán của ứng dụng của ta.
  Để hiểu **tại sao việc mở rộng quy mô lại quan trọng**, hãy xem xét ví dụ này
  về một khối lượng công việc có các yêu cầu tài nguyên khác nhau.
  Trong ví dụ này, dung lượng tài nguyên nhiều nhất được yêu cầu vào thứ Tư
  và dung lượng tài nguyên ít nhất được yêu cầu vào Chủ Nhật.
  Một lựa chọn là phân bổ nhiều hơn đủ công suất để ta luôn
  có thể đáp ứng nhu cầu cao nhất của mình, trong trường hợp này là thứ Tư.
  Tuy nhiên, tình huống này có nghĩa là ta đang sử dụng các tài nguyên
  sẽ không được sử dụng hết hầu hết các ngày trong tuần. Với tùy chọn này,
  chi phí của ta không được tối ưu hóa.
  Một lựa chọn khác là phân bổ ít công suất hơn để giảm chi phí.
  Tình trạng này có nghĩa là ta đang thiếu năng lực vào một số ngày nhất định.
  Nếu ta không giải quyết được vấn đề dung lượng của mình,
  ứng dụng của ta có thể hoạt động kém hiệu quả
  hoặc thậm chí có khả năng không khả dụng cho người dùng.

- Trong đám mây, vì sức mạnh tính toán là một tài nguyên có lập trình,
  ta có thể thực hiện một cách tiếp cận linh hoạt để Scaling.
  **Auto Scaling** là một dịch vụ AWS giúp ta duy trì tính khả dụng của ứng dụng
  và cho phép ta tự động thêm hoặc xóa các EC2 Instance
  theo các điều kiện ta xác định.
  Ta có thể sử dụng các tính năng quản lý nhóm của EC2 Auto Scaling
  để duy trì tình trạng hoạt động và tính khả dụng của nhóm của mình.
  Auto Scaling cung cấp một số cách điều chỉnh tỷ lệ
  để đáp ứng tốt nhất nhu cầu của các ứng dụng của ta.
  Ta có thể thêm hoặc xóa các EC2 Instance theo cách thủ công,
  theo lịch trình, để đáp ứng nhu cầu thay đổi
  hoặc kết hợp với AWS Auto Scaling để mở rộng dự đoán.
  Chia tỷ lệ động và mở rộng dự đoán có thể được sử dụng cùng nhau
  để mở rộng quy mô nhanh hơn.
  Tìm hiểu thêm ở Auto Scaling Auto Scaling trong mục Tài liệu tham khảo.

- **Nhóm Auto Scaling** là một tập hợp các Auto Scaling Instance
  được coi là nhóm hợp lý cho mục đích quản lý và chia tỷ lệ tự động.
  Kích thước của một nhóm Auto Scaling tỷ lệ phụ thuộc vào
  số lượng Instance ta đặt làm dung lượng mong muốn.
  Ta có thể điều chỉnh kích thước của nó để đáp ứng nhu cầu,
  theo cách thủ công hoặc bằng cách sử dụng tính năng chia tỷ lệ tự động.

- **Để khởi chạy các EC2 Instance**,
  nhóm Auto Scaling tỷ lệ sử dụng cấu hình khởi chạy
  (xem thêm Tài liệu tham khảo Launch configurations),
  là một mẫu cấu hình Instance.
  Ta có thể nghĩ về cấu hình khởi chạy khi ta đang mở rộng quy mô.
  Khi ta tạo cấu hình khởi chạy, ta chỉ định thông tin cho các Instance.
  Thông tin ta chỉ định bao gồm ID AMI, loại instance, IAM, bộ nhớ bổ sung,
  một hoặc nhiều nhóm bảo mật và bất kỳ khối lượng
  Amazon Elastic Block Store (Amazon EBS) nào.

- Ta xác định số lượng Instance tối thiểu và tối đa cũng
  như dung lượng mong muốn của nhóm Auto Scaling của ta.
  Sau đó, ta khởi chạy nó vào một mạng con trong VPC
  (ta có thể coi đây là nơi ta đang mở rộng quy mô).
  Amazon EC2 Auto Scaling tích hợp với Elastic Load Balancing
  để cho phép ta đính kèm một hoặc nhiều bộ cân bằng tải
  vào nhóm Auto Scaling hiện có.
  Sau khi ta đính kèm bộ cân bằng tải, nó sẽ tự động đăng ký các Instance
  trong nhóm và phân phối lưu lượng đến trên các Instance.
  Cuối cùng, ta chỉ định khi nào ta muốn sự kiện Scaling xảy ra,
  xem thêm các tuỳ chọn Scaling ở mục Tài liệu tham khảo.
- Video: [Amazon EC2 Auto Scaling](https://awsacademy.instructure.com/courses/77750/modules/items/7000951)

#### Monitoring

- **CloudWatch** giúp ta giám sát các tài nguyên AWS và ứng dụng chạy trên AWS,
  thu thập và theo dõi với các metric được định nghĩa sẵn
  hoặc ta tự định nghĩa, gửi các cảnh báo khi có thông báo được định trước.

- **Amazon CloudWatch** là một dịch vụ theo dõi
  và khả năng quan sát được xây dựng cho các DevOps engineer, Developer,
  Site Reliability Engineers (SRE) và các nhà quản lý CNTT.
  CloudWatch giám sát tài nguyên AWS của ta (và các ứng dụng ta chạy trên AWS)
  trong thời gian thực. Ta có thể sử dụng CloudWatch để thu thập
  và theo dõi các chỉ số,
  là những biến số mà ta có thể đo lường cho các tài nguyên và ứng dụng của mình.

- Ta có thể tạo **cảnh báo CloudWatch** theo dõi một chỉ số CloudWatch duy nhất
  hoặc kết quả của một biểu thức toán học _dựa trên chỉ số CloudWatch_.
  Ta có thể tạo cảnh báo CloudWatch _dựa trên ngưỡng tĩnh_,
  phát hiện bất thường hoặc biểu thức toán học chỉ số.

- Khi ta tạo báo thức dựa trên ngưỡng tĩnh, ta chọn chỉ số CloudWatch
  cho báo thức cần xem và ngưỡng cho chỉ số đó.
  Cảnh báo chuyển sang trạng thái ALARM khi chỉ số vi phạm ngưỡng
  trong một số khoảng thời gian đánh giá cụ thể.

- Đối với cảnh báo dựa trên ngưỡng tĩnh, ta phải chỉ định:
  Namespace, Metric, Statistic, Period, Conditions,
  Additional Configuration Information, Actions.
  Ta có thể tìm hiểu thêm thông qua _Using CloudWatch Alarms_
  ở mục Tài liệu tham khảo.

- Video: [Amazon CloudWatch](https://awsacademy.instructure.com/courses/77750/modules/items/7000950)

#### Document references

- Các tài liệu đọc dưới đây giúp ta hiểu rõ hơn về ELB:

  - [Elastic Load Balancing (từ trang 1 đến trang 16)](https://drive.google.com/file/d/1-0L5QR8N363kanFJ0946VsPJvNSDl0vq/view)
  - [Elastic Load Balancing features](https://aws.amazon.com/elasticloadbalancing/features/?nc=sn&loc=2)

- Các tài liệu đọc dưới đây giúp ta hiểu rõ hơn về EC2 Auto Scaling:

  - [EC2 Auto Scaling (từ trang 17 đến hết)](https://drive.google.com/file/d/1-0L5QR8N363kanFJ0946VsPJvNSDl0vq/view)
  - [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/)
  - [Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html)
  - [Launch configurations](https://docs.aws.amazon.com/autoscaling/ec2/userguide/LaunchConfiguration.html)
  - [Manual scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-manual-scaling.html)
  - [Scheduled scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html)
  - [Dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html)
  - [Dynamic scaling policy types](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html#as-scaling-types)
  - [Predictive Scaling](https://aws.amazon.com/blogs/aws/new-predictive-scaling-for-ec2-powered-by-machine-learning/)
  - [Scaling the size of your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/scaling_plan.html)

- Các tài liệu đọc dưới đây giúp ta hiểu rõ hơn về Cloud Watch:
  - [Using CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

### Lab 8

- Lab 8: [Lab - 6 Scale & Load Balance your Architecture](https://awsacademy.instructure.com/courses/77750/assignments/785913?module_item_id=7000953)
  [Vietsub](https://docs.google.com/document/d/18Y0WIZxSxXCpzk-WTfSlKJQox8zICO70/view)

## Assignment 1: Auto scaling application on EC2 for webserver

- [Funix Course](https://courses.funix.edu.vn/courses/course-v1:FUNiX+DEP304x_01-A_VN+2021_T11/courseware/aa95505973274c5d93ab346593f50877/c5a04066d0cc41639b602703ec15fe55/?child=first)
- **Tổng quan dự án** ![Project diagram](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FDevOps%2FAssingment_Image%2FDOP301x_ASM2_T%E1%BB%95ng%20quan_H%C3%ACnh%201.png?alt=media&token=81830a67-579e-4946-9846-3c0faba493a0)
- Trong bài tập này, chúng ta sẽ xây dựng ứng dụng chịu tải
  khi tài nguyên đột ngột tăng cao. Hãy dùng Service Application Load Balancer
  để cân bằng tải với Auto Scaling Group trên 2 Availability Zones như sau:

  - Tạo Application Load Balancer
  - Tạo Auto Scaling Group
  - Tạo Launch Configuration
  - Đợi Instance running
  - Tăng tải hệ thống
  - Chờ trong 5 phút và xem các hoạt động Scaling có đang diễn ra hay không

- **Hướng đi**
  1. Tạo tài khoản AWS
  2. Tạo Application Load Balancer
     1. Tạo target group nhưng không thêm bất kỳ instance nào
  3. Tạo Auto Scaling group
     1. Cấu hình tối thiểu 2, tối đa 4, mong muốn 2
     2. Tạo launch configuration. Chắc chắn rằng bạn thêm userdata
        để tải xuống và cài đặt website
     3. Liên kết target group với Auto Scaling group
     4. Liên kết ELB health check
     5. Cấu hình Auto Scaling policy với Average CPU > 20%.
        Cấu hình thông báo email. Xác nhận email subscription
  4. Đợi cho instance chạy xong.
     Kiểm tra nếu bạn có thể truy cập vào Web Application sử dụng Load Balancer DNS
  5. Tăng độ tải trên web servers
     1. Tiến hành ssh đến bất kỳ EC2 nào (chắc chắn port 22 đã được mở)
     2. Cài đặt stress: sudo yum install stress -y
     3. Tăng tải: stress --cpu 2 --timeout 300
  6. Chờ 5 phút và xem hoạt động scale
- **Yêu cầu**:
  - Yêu cầu chức năng:
    - 0.5 Tạo IAM User và Group
    - 0.5 Tạo được VPC và Security Group
    - 0.5 Tạo được Target Group
    - 1.5 Tạo được Application Load Balancer
    - 1.0 Tạo được Launch Template
    - 1.5 Tạo được Auto Scaling Group
    - 1.0 Thực hiện việc tăng tải cho Server
  - Yêu cầu phi chức năng
    - 0.5 README.txt
  - Yêu cầu nâng cao
    - 2.0 Tạo Snapshot cho EC2

## AWS Database

### AWS Database

#### Amazon RDS

- Sự khác biệt giữa dịch vụ được quản lý và không được quản lý
  liên quan đến Amazon RDS.
  - Với dịch vụ không được quản lý, các thao tác như scale, FT, availability
    sẽ do ta thực hiện.
  - Với các dịch vụ được quản lý, các thao tác này
    thường là các Build-in Service, do người dùng cấu hình.
- **Amazon RDS (Relational Database Service)** là một dịch vụ được quản lý
  nhằm thiết lập và vận hành cơ sở dữ liệu quan hệ trên đám mây.
- Amazon RDS cho phép ta tập trung vào ứng dụng của mình,
  vì vậy ta có thể cung cấp cho các ứng dụng hiệu suất,
  tính khả dụng cao, bảo mật và khả năng tương thích mà chúng cần.

- Các **dịch vụ không được quản lý** thường được cung cấp theo các phần rời rạc
  do người dùng chỉ định. Giả sử ta khởi chạy máy chủ web
  trên Amazon Elastic Compute Cloud (Amazon EC2) Instance.
  Bởi vì Amazon EC2 là một giải pháp không được quản lý,
  máy chủ web đó sẽ không mở rộng quy mô để xử lý lưu lượng truy cập tăng
  hoặc thay thế các Instance không lành mạnh bằng các Instance lành mạnh
  trừ khi ta chỉ định rằng nó sử dụng giải pháp mở rộng, c
  hẳng hạn như AWS Automatic Scaling.
  Lợi ích của việc sử dụng dịch vụ không được quản lý
  là ta có quyền kiểm soát tốt hơn đối với cách giải pháp của ta xử lý
  các thay đổi về tải, lỗi và các tình huống mà tài nguyên không có sẵn.

- Các **dịch vụ được quản lý** yêu cầu người dùng cấu hình chúng. Ví dụ: ta tạo
  một nhóm Amazon Simple Storage Service (Amazon S3) và sau đó đặt quyền cho nó.
  Tuy nhiên, các dịch vụ được quản lý thường yêu cầu ít cấu hình hơn.
  Giả sử rằng ta có một trang web tĩnh mà ta lưu trữ trong một giải pháp lưu trữ
  dựa trên đám mây, chẳng hạn như Amazon S3.
  Trang web tĩnh không có máy chủ web, tuy nhiên, vì Amazon S3
  là một giải pháp được quản lý nên các tính năng như mở rộng quy mô,
  khả năng chịu lỗi và tính khả dụng sẽ được Amazon S3 xử lý tự động và nội bộ.

- Khi ta **chạy cơ sở dữ liệu quan hệ của riêng mình**,
  ta chịu trách nhiệm về một số tác vụ quản trị, chẳng hạn như bảo trì máy chủ,
  phần mềm, cài đặt và vá lỗi cũng như sao lưu cơ sở dữ liệu, cài đặt
  và vá lỗi hệ điều hành (OS). Tất cả các nhiệm vụ này lấy tài nguyên
  từ các mục khác trong danh sách việc cần làm của ta
  và yêu cầu chuyên môn trong một số lĩnh vực.

- Amazon RDS là một dịch vụ được quản lý nhằm thiết lập
  và vận hành cơ sở dữ liệu quan hệ trên đám mây.
  Để giải quyết những thách thức khi chạy cơ sở dữ liệu quan hệ độc lập,
  không được quản lý, AWS cung cấp dịch vụ thiết lập, vận hành và mở rộng quy mô
  cơ sở dữ liệu quan hệ mà không yêu cầu việc quản trị liên tục.
  Amazon RDS cung cấp dung lượng hiệu quả về chi phí và có thể thay đổi kích thước,
  đồng thời tự động hóa các tác vụ quản trị tốn nhiều thời gian.
  Amazon RDS cho phép ta tập trung vào ứng dụng của mình,
  vì vậy ta có thể cung cấp cho các ứng dụng hiệu suất, tính khả dụng cao, bảo mật
  và khả năng tương thích mà chúng cần.
  Với Amazon RDS, trọng tâm chính của ta là dữ liệu và tối ưu hóa ứng dụng của ta.

- **Khi cơ sở dữ liệu của ta ở on-premises**,
  người quản trị cơ sở dữ liệu chịu trách nhiệm về mọi thứ.
  Các nhiệm vụ quản trị cơ sở dữ liệu bao gồm tối ưu hóa các ứng dụng và truy vấn;
  thiết lập phần cứng; vá phần cứng; thiết lập mạng và nguồn;
  và quản lý hệ thống sưởi, thông gió và điều hòa không khí (HVAC).

  - Nếu ta chuyển sang cơ sở dữ liệu chạy trên
    Amazon Elastic Compute Cloud (Amazon EC2) Instance, ta không cần quản lý
    phần cứng bên dưới hoặc xử lý các hoạt động của trung tâm dữ liệu nữa.
    Tuy nhiên, ta vẫn phải chịu trách nhiệm vá hệ điều hành và xử lý
    tất cả các phần mềm và hoạt động sao lưu.
  - Nếu ta thiết lập cơ sở dữ liệu của mình trên Amazon RDS hoặc Amazon Aurora,
    ta sẽ giảm bớt trách nhiệm quản trị của mình.
  - Bằng cách chuyển sang đám mây, ta có thể tự động mở rộng cơ sở dữ liệu của mình,
    kích hoạt tính khả dụng cao, quản lý các bản sao lưu và thực hiện vá lỗi.
  - Do đó, ta có thể tập trung vào những gì thực sự quan trọng nhất -
    tối ưu hóa ứng dụng của ta.

- Với Amazon RDS, **ta quản lý việc tối ưu hóa ứng dụng của mình**.
  AWS quản lý cài đặt và vá hệ điều hành, cài đặt và vá phần mềm cơ sở dữ liệu,
  sao lưu tự động và tính sẵn sàng cao. AWS cũng mở rộng quy mô tài nguyên,
  quản lý nguồn và máy chủ, đồng thời thực hiện bảo trì.
  Việc giảm tải các hoạt động này cho dịch vụ Amazon RDS được quản lý
  giúp giảm khối lượng công việc hoạt động của ta và chi phí
  liên quan đến cơ sở dữ liệu quan hệ của ta.

- Video: [AWS RDS](https://awsacademy.instructure.com/courses/77750/modules/items/7000926)
- Video sau đây giúp bạn hiểu rõ hơn về AWS RDS thông qua AWS console.
  [Ví dụ RDS](https://awsacademy.instructure.com/courses/77750/modules/items/7000927)

#### Other databases

##### DynamoDB

- DynamoDB là một dịch vụ cơ sở dữ liệu NoSQL nhanh chóng và linh hoạt:

  - **Cơ sở dữ liệu quan hệ (RDB)**

    - Hoạt động với dữ liệu có cấu trúc được sắp xếp theo bảng, bản ghi và cột.
    - RDB thiết lập một mối quan hệ được xác định rõ ràng
      giữa các bảng cơ sở dữ liệu.
    - RDB sử dụng ngôn ngữ truy vấn có cấu trúc (SQL),
      là một ứng dụng người dùng tiêu chuẩn cung cấp giao diện lập trình
      theo chương trình để tương tác với cơ sở dữ liệu.
    - Cơ sở dữ liệu quan hệ có thể gặp khó khăn khi mở rộng quy mô theo chiều ngang
      hoặc làm việc với dữ liệu có cấu trúc bán nguyệt
      và cũng có thể yêu cầu nhiều phép nối cho dữ liệu chuẩn hóa.

  - **Cơ sở dữ liệu không quan hệ**
    - Là bất kỳ cơ sở dữ liệu nào không tuân theo mô hình quan hệ
      được cung cấp bởi các hệ quản trị cơ sở dữ liệu quan hệ truyền thống (RDBMS).
    - Cơ sở dữ liệu không quan hệ đã trở nên phổ biến vì chúng được thiết kế
      để khắc phục những hạn chế của cơ sở dữ liệu quan hệ
      để xử lý các nhu cầu của dữ liệu có cấu trúc biến đổi.
    - Cơ sở dữ liệu không quan hệ mở rộng theo chiều ngang
      và chúng có thể hoạt động với dữ liệu không có cấu trúc và bán cấu trúc.

- DynamoDB là **một dịch vụ cơ sở dữ liệu NoSQL** nhanh chóng
  và linh hoạt cho tất cả các ứng dụng cần độ trễ thấp,
  tính theo mili giây trên bất kỳ quy mô nào.
  Amazon quản lý tất cả cơ sở hạ tầng dữ liệu cơ bản cho dịch vụ này
  và lưu trữ dự phòng dữ liệu trên nhiều cơ sở trong Khu vực Hoa Kỳ bản địa
  như một phần của kiến trúc chịu lỗi.
- Với DynamoDB, ta có thể tạo bảng và mục. Ta có thể thêm các mục vào một bảng.
  Hệ thống tự động phân vùng dữ liệu của ta và có bảng lưu trữ
  để đáp ứng các yêu cầu về khối lượng công việc.
  Không có giới hạn thực tế về số lượng mục mà ta có thể lưu trữ trong một bảng.
  Ví dụ: một số khách hàng có bảng sản xuất chứa hàng tỷ mặt hàng.
  Một trong những lợi ích của cơ sở dữ liệu NoSQL là các mục trong cùng một bảng
  có thể có các thuộc tính khác nhau. Điều này mang lại cho ta sự linh hoạt
  để thêm các thuộc tính khi ứng dụng của ta phát triển.
  Ta có thể lưu trữ các mục định dạng mới hơn song song với các mục
  định dạng cũ hơn trong cùng một bảng mà không cần thực hiện di chuyển giản đồ.

- Các **thành phần DynamoDB cốt lõi** là bảng, mục và thuộc tính.

  - Bảng là một tập hợp dữ liệu
  - Mục là một nhóm các thuộc tính có thể nhận dạng duy nhất
    giữa tất cả các mục khác
  - Thuộc tính là một phần tử dữ liệu cơ bản,
    không cần phải chia nhỏ thêm

- DynamoDB hỗ trợ **hai loại khóa chính khác nhau**.

  - **Partition Key** là một khóa chính đơn giản,
    bao gồm một thuộc tính gọi là **sort key**.
  - Partition key và sort key còn được gọi là khóa chính tổng hợp,
    bao gồm hai thuộc tính.
  - Xem thêm Table item attributes trong mục Tài liệu tham khảo.

- Video: [AWS DynamoDB](https://awsacademy.instructure.com/courses/77750/modules/items/7000929)

- Triển khai AWS DynamoDB thông qua AWS console giúp ta hiểu rõ hơn
  [Ví dụ DynamoDB](https://awsacademy.instructure.com/courses/77750/modules/items/7000930)

##### Amazon Redshift

- **Amazon Redshift** là một kho dữ liệu nhanh chóng, được quản lý đầy đủ,
  giúp phân tích tất cả dữ liệu của ta một cách đơn giản và tiết kiệm chi phí
  bằng cách sử dụng SQL tiêu chuẩn và các công cụ Business Intelligent (BI)
  hiện có của ta.

- Analytics rất quan trọng đối với các doanh nghiệp ngày nay,
  nhưng việc xây dựng một kho dữ liệu rất phức tạp và tốn kém.
  Kho dữ liệu mất nhiều tháng và nguồn tài chính đáng kể để thiết lập.
  Amazon Redshift là một kho dữ liệu được quản lý đầy đủ và nhanh chóng và mạnh mẽ,
  đơn giản và tiết kiệm chi phí để thiết lập, sử dụng và mở rộng quy mô.
  Nó cho phép ta chạy các truy vấn phân tích phức tạp dựa trên petabyte dữ liệu
  có cấu trúc bằng cách sử dụng tối ưu hóa truy vấn phức tạp,
  lưu trữ dạng cột trên các đĩa cục bộ hiệu suất cao
  và xử lý dữ liệu song song hàng loạt.
  Hầu hết các kết quả sẽ trở lại sau vài giây.

- **Leader Node** quản lý các giao tiếp với các chương trình khách
  và tất cả các giao tiếp với các **Compute Node**.
  Nó phân tích cú pháp và phát triển các kế hoạch
  để thực hiện các hoạt động cơ sở dữ liệu - cụ thể là một loạt các bước cần thiết
  để thu được kết quả cho các truy vấn phức tạp.
  Leader node biên dịch mã cho các phần tử riêng lẻ của kế hoạch
  và gán mã cho các Compute Node riêng lẻ.
  Các compute nodes chạy mã đã biên dịch và gửi các kết quả trung gian trở lại
  leader node để tổng hợp cuối cùng.

- Thật dễ dàng để **tự động hóa** hầu hết các tác vụ quản trị phổ biến để quản lý,
  giám sát và mở rộng Amazon Redshift cluster của ta - cho phép ta tập trung
  vào dữ liệu và doanh nghiệp của mình. **Scaling** là nội tại của Amazon Redshift.
  Cluster của ta có thể được mở rộng lên và xuống khi nhu cầu của ta thay đổi
  bằng một vài cú nhấp chuột trong bảng điều khiển.
  Bảo mật là ưu tiên cao nhất đối với AWS.
  Với Amazon Redshift, bảo mật là nội dung và nó được thiết kế để cung cấp mã hóa
  mạnh mẽ cho dữ liệu của ta cả khi ở trạng thái nghỉ và khi đang chuyển.

- Cuối cùng, Amazon Redshift **tương thích với các công cụ** mà ta đã biết
  và sử dụng. Amazon Redshift hỗ trợ SQL tiêu chuẩn. Nó cũng cung cấp các
  trình kết nối JDBC và ODBC hiệu suất cao, cho phép ta sử dụng
  các ứng dụng SQL client và các công cụ BI mà ta chọn.

- Video: [AWS Redshift](https://awsacademy.instructure.com/courses/77750/modules/items/7000931)

##### Amazon Aurora

- Amazon Aurora là cơ sở dữ liệu quan hệ **tương thích với MySQL và PostgreSQL**,
  được xây dựng cho cloud, kết hợp hiệu suất và tính khả dụng
  của cơ sở dữ liệu thương mại cao cấp với sự đơn giản và hiệu quả về chi phí
  của cơ sở dữ liệu nguồn mở. Sử dụng Amazon Aurora có thể giảm chi phí
  cơ sở dữ liệu của ta trong khi cải thiện độ tin cậy
  và tính khả dụng của cơ sở dữ liệu.
  Là một dịch vụ được quản lý hoàn toàn, Aurora được thiết kế để tự động hóa
  các nhiệm vụ tốn thời gian như cung cấp, vá lỗi, sao lưu, phục hồi,
  phát hiện lỗi và sửa chữa.

- Amazon Aurora có tính sẵn sàng (HA)
  và nó cung cấp một hệ thống con **lưu trữ phân tán, nhanh chóng**.
  Amazon Aurora rất dễ thiết lập và sử dụng các truy vấn SQL.
  Nó được thiết kế để có **khả năng tương thích** với cơ sở dữ liệu
  MySQL và PostgreSQL mà ta có thể sử dụng hầu hết các công cụ cơ sở dữ liệu
  hiện có của mình mà không cần thay đổi hoặc ít.
  Các dịch vụ và tính năng mà ta sử dụng.
  Đây là một dịch vụ được quản lý tích hợp với các tính năng
  như AWS Database Migration Service (AWS DMS) và AWS Schema Conversion Tool.
  Các tính năng này được thiết kế để giúp ta
  di chuyển tập dữ liệu của mình vào Amazon Aurora.

- Amazon Aurora được thiết kế để **có tính khả dụng cao**: nó lưu trữ nhiều bản sao
  dữ liệu của ta trên nhiều Availability Zones với các bản sao lưu liên tục
  vào Amazon S3. Amazon Aurora có thể sử dụng tối đa 15 bản sao đã đọc có thể
  được sử dụng để giảm khả năng mất dữ liệu của ta.
  Ngoài ra, Amazon Aurora được thiết kế để khôi phục sự cố tức thì
  nếu cơ sở dữ liệu chính của ta trở nên không khỏe mạnh.

- Sau sự cố cơ sở dữ liệu, Amazon Aurora
  **không cần phải phục hồi từ điểm kiểm tra cơ sở dữ liệu cuối cùng**.
  Thay vào đó, nó thực hiện điều này trên mọi thao tác đọc.
  Điều này giúp giảm thời gian khởi động lại sau sự cố cơ sở dữ liệu
  xuống dưới 60 giây trong hầu hết các trường hợp.
  Điều này làm giảm nhu cầu ta phải điều chỉnh quyền truy cập
  cho đến khi bộ nhớ cache được lưu trữ lại để tránh hiện tượng duyệt web.

Video: [AWS Aurora](https://awsacademy.instructure.com/courses/77750/modules/items/7000932)

#### Document references

- Các tài liệu đọc về Relational Database Service RDS:
  - [Relational Database Service RDS (từ trang 1 đến trang 18)](https://drive.google.com/file/d/1lZIdChC761ItaqOfSToKS98UZXGswMqU/view)
  - [AWS Database page](https://aws.amazon.com/products/databases/)
  - [Amazon RDS page](https://aws.amazon.com/rds/)
  - [Overview of Amazon database services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/database.html)
  - [Getting started with AWS databases](https://aws.amazon.com/products/databases/learn/)
- Các tài liệu đọc về DynamoDB, Redshift và Aurora
  - [DynamoDB, Redshift và Aurora (từ trang 19 đến hết)](https://drive.google.com/file/d/1lZIdChC761ItaqOfSToKS98UZXGswMqU/view)
  - [Table Item Attributes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.TablesItemsAttributes)
  - [Amazon Aurora](https://aws.amazon.com/rds/aurora/?aurora-whats-new.sort-by=item.additionalFields.postDateTime&aurora-whats-new.sort-order=desc)
  - [Overview of Amazon Database Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/database.html)
  - [Getting started with AWS Databases](https://aws.amazon.com/products/databases/learn/)

### Amazon RDS

#### Amazon RDS Configuration

- AWS cung cấp cho ta hai cách để thay đổi các thiết lập cho RDS:
  1. Parameter Groups:
     - Sử dụng để thay đổi các thiết lập của RDS, ví dụ như:
       - `autocommit`: Thiết lập chế độ autocommnit cho RDS.
       - `time_zone`: Thiết lập múi giờ cho RDS.
       - `force_ssl`: Bắt buộc tất cả các kết nối đến RDS của ta sử dụng SSL.
       - `default_storage_engine`: Thay đổi Storage Engine mặc định của RDS.
       - `max_connections`: Số kết nối tối đa đến RDS của ta.
     - Các trường trong Parameter group được chia thành 2 loại là:
       Static và Dynamic. Khi ta thay đổi giá trị của
       các trường Dynamic thì sẽ được áp dụng ngay lập tức,
       còn nếu ta thay đổi giá trị các trường Static thì sẽ cần khởi động thủ công
       lại RDS để áp dụng các thay đổi.
     - Để thay đổi Parameter Group cho một RDS Instance,
       ta sẽ cần tạo mới một Parameter Group chứ không thể thay đổi
       trong default Parameter Group của AWS.
     - Video: [RDS parameter groups](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21273966#overview)
  2. Options Groups:
     - Khác với Parameter Groups, Options Groups giúp ta thay đổi
       các thiết lập riêng biệt cho từng loại Database Engines, ví dụ:
       - `SQLSERVER_BACKUP_RESTORE` trong SQL Server
       - `NATIVE_NETWORK_ENCRYPTION` trong Oracle
       - `MARIADB_AUDIT_PLUGIN` trong MariaDB và MySQL
       - `MEMCACHED` để kích hoạt Memcached support trong MySQL
     - Để thay đổi Option Group cho một RDS Instance,
       ta sẽ cần tạo mới một Parameter Group chứ không thể thay đổi
       trong default Option Group của AWS.
     - Video: [RDS option groups](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21273970#overview)
- Video: [RDS - Hands on](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21273972#overview)

#### RDS Security

##### RDS Security - Network

- Ta có thể khởi tạo RDS bên trong một VPC để có để hạn chế sự truy cập Internet,
  thông thường RDS sẽ được triển khai ở trong một private subnet như sau:
  ![RDS with private subnet](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L12_1.png?alt=media&token=3617de80-344e-42cf-8660-590e28645c18)
- Đây là mô hình Shared Responsibility khi sử dụng RDS:

  - **Khách hàng**
    - Kiểm tra và thiết lập về ports / IP / security group inbound rules.
    - Tạo và quản lý quyền truy cập của các User.
    - Tạo Database public access hoặc private.
    - Đảm bảo Parameter Groups hoặc Database được thiết lập
      để chỉ cho phép các kết nối sử dụng SSL.
  - **AWS**
    - Không cho phép truy cập qua SSH.
    - Tự động cập nhật các bản vá lỗi cho Database và hệ điều hành.

- Lưu ý:
  - Ta sẽ không thể thay đổi VPC sau khi đã tạo một Database.
  - RDS security hoạt động khá tương đồng với EC2,
    kiểm soát xem IP nào sẽ được giao tiếp với RDS.
- Video: [RDS security - Network](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21276582#overview)

##### RDS Security - IAM

- Ta cũng sẽ cần sử dụng IAM để kiểm soát được những User nào có thể truy cập
  và thực hiện các thao tác với RDS.
  Ta cũng có thể sử dụng IAM database authentication cho **MySQL và PostgreSQL**,
  từ đó cũng cấp cho ta các lợi ích sau:
  - Network traffic được mã hóa sử dụng **Secure Socket Layer (SSL)**
    hoặc **Transport Layer Security (TLS)**.
  - Ta có thể sử dụng IAM để quản lý quyền truy cập vào tài nguyên
    cơ sở dữ liệu của mình, thay vì quản lý quyền truy cập riêng lẻ
    trên từng Database Instance.
  - Đối với các ứng dụng chạy trên Amazon EC2,
    ta có thể sử dụng thông tin đăng nhập cho EC2 Instance
    để truy cập cơ sở dữ liệu thay vì sử dụng mật khẩu, giúp bảo mật cao hơn.
- Video: [RDS security - IAM](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21276980#overview)

##### Rotating RDS DB credentials

- Để đảm bảo yếu tố bảo mật cho những tài nguyên cần thiết cần thiết
  để truy cập các ứng dụng, dịch vụ và tài nguyên trên AWS thì ta có thể sử dụng
  dịch vụ **AWS Secrets Manager** - đây là dịch vụ giúp ta dễ dàng thay đổi
  các key, token một cách tự động cũng như quản lý, truy xuất các thông tin
  để đăng nhập và Database, API keys. Người dùng và các ứng dụng có thể truy xuất
  vào các tài nguyên này bằng cách gửi Request tới **Secrets Manager APIs**.
- AWS Secrets Manager hỗ trợ để tích hợp với RDS sử dụng **MySQL, PostgreSQL**
  và **Aurora**.
- Video: [Rotating RDS DB credentials](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21277050#overview)

##### RDS encryption in transit and at rest

- RDS cũng hỗ trợ cơ chế để mã hóa dữ liệu khi chuyển tiếp
  hoặc khi đang trong trang thái nghỉ,
  điều này giúp tăng tính bảo mật của dữ liệu hơn.
- Khi chuyển tiếp (Transit) dữ liệu thì ta sẽ cần sử dụng kết nối SSL/TLS
  và phía Client cũng sẽ cần trust AWS Root CA (Certified Authority).
- Khi dữ liệu đang trong trạng thái nghỉ (Rest) thì các dữ liệu trong RDS
  vẫn sẽ được mã hóa theo thuật toán AES-256 và sẽ mã hóa ở cả master
  và read replicas. Lưu ý là sự mã hóa này cần phải được khai báo khi mà tạo RDS.
- Video: [RDS encryption in transit and at rest](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21277076#overview)

#### RDS Backups

##### RDS Backups

- RDS hỗ trợ cơ chế backups tự động để, các bản backup này mặc định sẽ được lưu trữ
  trong **7 ngày** (ta có thể chỉnh sửa tham số này theo khoảng từ **0 - 35 ngày**,
  nếu là 0 ngày tức là sẽ không Backup nữa).
  Trong lần backup đầu tiên, toàn bộ dữ liệu sẽ được backup,
  nhưng ở các lần tiếp theo thì RDS sẽ chỉ backup các dữ liệu đã được thay đổi
  (Incremental Data). Bản Backup sẽ được lưu trữ ở một S3 Bucket của RDS
  (Bucket này sẽ được quản lý ở RDS nên ta sẽ không thấy ở S3 console).
- Ngoài ra, ta nên sử dụng cơ chế Multi-AZ để tránh các vấn đề về hiệu suất
  khi quá trình Backup được thực thi và sử dụng dịch vụ AWS Backup
  để quản lý các thao tác này.
- Vậy Backups và Snapshots sẽ khác gì nhau?
  - **Backup**
    - Hoàn toàn tự động.
    - Hỗ trợ Incremental Backup.
    - Bản backup sẽ được lưu trữ tối đa là 35 ngày.
    - Phù hợp để tránh các lỗi không mong muốn xảy ra trong quá trình hoạt động.
    - Hỗ trợ tạo Snapshot trước và sau quá trình cập nhật Database.
  - **Snapshot**
    - Cần các thao tác thủ công.
    - Hỗ trợ Full Backup.
    - Có thể được lưu trữ không giới hạn thời gian.
    - Phù hợp để lưu trữ cho các sự kiện như cập nhật Database,...
    - Hỗ trợ Lambda để chuyển dữ liệu về S3.
- Video: [RDS backups](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21284532#overview)

##### Copying and sharing RDS snapshots

- Ta có thể sao chép các **Automated Backups** hoặc **Manual Snapshots**,
  tuy nhiên khi đó các backup này đều sẽ được coi là một Manual Snapshots.
  Ta có thể sao chép sao chép snapshots trong một region hoặc giữa các region,
  tài khoản với nhau, tuy nhiên nếu bạn sao chép giữa các region
  và các tài khoản thì **sẽ bị tính phí di chuyển dữ liệu (transfer data)**.
- ![Transfer data](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L12_2.png?alt=media&token=7a6746f6-a3dd-410d-b431-7da4fe3c6437)
- Video: [Copying and sharing RDS snapshots](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21285288#overview)

##### How to encrypt an unencrypted RDS database

- Ta có thể mã hóa hoặc giải mã một RDS Database,
  tuy nhiên sẽ có một số lưu ý như sau:
  - Ta không thể mã hóa một RDS Database chưa được mã hóa có sẵn.
  - Ta không thể tạo một bản sao (được mã hóa) từ một RDS Database chưa mã hóa.
  - Để mã hóa một RDS Database, ta sẽ cần sao chép Database đó
    với thiết lập "**encryption**" đã được bật.
- Video: [How to encrypt an unencrypted RDS database](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21285294#overview)

##### DB restore options in RDS

- Một số lưu ý khi ta khôi phục dữ liệu từ một Snapshot như sau:
  - Ta cần tạo một RDS Instance mới để chứa dữ liệu được khôi phục.
  - Ta không thể khôi phục dữ liệu từ một encrypted snapshot
    hoặc snapshot được chia sẻ với ta.
    Để làm được thao tác này thì ta cần sao chép lại snapshot đó trước
    rồi mới khôi phục.
  - Ta không thể khôi phục snapshot từ một region khác (phải sao chép về trước).
  - Ta không thể khôi phục không thuộc VPC hiện tại.
- ![Restore snapshot](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L12_3.png?alt=media&token=a2459ef4-69bd-4fe3-9ac0-0aacdf18fa14)
- Video: [DB restore options in RDS](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21285296#overview)
- Video: [RDS backup and restore - Hands on](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21285610#overview)
- Video tham khảo: [Exporting RDS DB snapshot to S3](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21285298#overview)

#### RDS Monitoring

##### RDS Monitoring

- Để kiểm tra và giám sát tình trạng của một RDS Database,
  ta có thể sử dụng các số liệu sau:
  - Các số liệu phổ biến như **CPU, RAM, Network traffic, DB connections**,...
  - Các log của từng loại Database Engine
  - Các công cụ giám sát thủ công như **RDS console, AWS Trusted Advisor,**  
    **CloudWatch**
  - Các công cụ giám sát tự động như **RDS event notifications, Database logs,**
    **CloudWatch, Enhanced Monitoring**,...
- Video: [RDS monitoring](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21437832#overview)

##### RDS automatical tools

- **RDS Notifications/Event subscriptions** là một dịch vụ trong AWS giúp ta có thể
  gửi một thông báo (notification) khi một RDS Event xảy ra,
  hoặc là khi một số liệu nào đó trong CloudWatch vượt quá ngưỡng.
  Các notification này có thể ở dưới dạng Email, SMS hoặc là một HTTP Endpoint.
- **RDS Recommendations** sẽ giúp đề xuất các phương án thực thi, vấn đề gặp phải trong RDS Database của ta.
- **RDS Logs** là công cụ giúp ta tải xuống hoặc Stream các file log từ RDS, hoặc có thể xuất các file log thành CloudWatch Log.
- Video: [RDS event subscriptions, recommendations and logs](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21437842#overview)

##### RDS Enhanced Monitoring

- RDS Enhanced Monitoring giúp ta thực hiện các thao tác phân tích số liệu
  về hệ điều hành, hỗ trợ theo dõi các số liệu của từng tiến trình
  và luồng đang sử dụng CPU, từ đó giúp cho ta tìm hiểu các lỗi liên quan
  đến hiệu xuất. Để sử dụng chức năng này, ta sẽ cần cài đặt trên Database Server.
- Video: [RDS Enhanced Monitoring](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21437852#overview)

### Lab 9

- Lab 9: [Lab - 5 Build a Database Server](https://awsacademy.instructure.com/courses/77750/assignments/785911?module_item_id=7000928)
  [Vietsub](https://docs.google.com/document/d/18Y1Kkm6Y7A5nTov-Wiqn65m707CS0qap/view)

### RDS Multi-AZ deployments and read replicas

#### RDS Multi-AZ deployments and read replica

##### Concepts

- Multi-AZ deployments là cơ chế giúp đảm báo tính khả dụng, độ bền của dữ liệu
  và khả năng chịu lỗi của hệ thống. Dữ liệu từ Primary RDS (RDS chính)
  sẽ được đồng bộ sang một Secondary RDS (RDS phụ) nằm ở 1 Availability Zone khác.
  Nếu Primary RDS gặp lỗi hoặc bị tắt đột ngột thì Secondary RDS sẽ được sử dụng
  thay thế với độ trễ thấp nhất (thường là từ 60 đến 120 giây).
  Một số lưu ý như sau:

  - Ta có thể có nhiều Secondary RDS.
  - Backup sẽ được thực hiện trên Secondary RDS
    để đảm bảo hiệu năng cho Primary RDS.
  - AWS sử dụng DNS để kết nối đến đến RDS,
    vậy nên ta sẽ **không cần thay đổi** các connection string.

- ![Multi-AZ deployments](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L13_1.png?alt=media&token=7f927417-965c-451f-836a-c34501ce887e)

- **Read Replicas** là cơ chế giúp đảm bảo hiệu suất và độ bền cho RDS.
  Ta sẽ nhân bản RDS Database thành các bản sao và bản sao này chỉ được sử dụng
  cho mục đích đọc dữ liệu.
  Cơ chế này giúp ta giải quyết các bài toán có lượng lớn các thao tác đọc dữ liệu.
  Một số lưu ý như sau:

  - Ta _có thể có đến 5 Read Replicas_.
  - Việc nhân bản sẽ là bất đồng bộ,
    vì vậy sẽ có một độ trễ nhất định để dữ liệu từ Primary đến các Red Replica.
  - Ứng dụng của ta cần phải cập nhật connection string
    để trỏ tới Read Replica phù hợp.
  - Để sử dụng cơ chế này, ta sẽ cần phải bật cơ chế Backup tự động.
  - Các Read Replicas có thể ở Availability Zone khác nhau,
    tuy nhiên ta **sẽ bị tính phí** khi sử dụng cơ chế này.

- ![Read replicas](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L13_2.png?alt=media&token=86566abc-d005-4c2b-8817-a1c046faa07e)

- Video: [RDS Multi-AZ deployments and read replicas](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21419674#overview)

- Video tham khảo: [Read replica use cases](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21420228#overview)

- Video tham khảo: [Enabling writes on a read replica](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21420866#overview)

##### Promotes a read replica to a standalone DB instance

- Ta cũng có thể "thăng cấp" cho một Read Replica để trở thành
  một RDS Instance hoạt động độc lập,
  thường sẽ được sử dụng trong những trường hợp sau:
  - Sử dụng để phục hồi dữ liệu khi Primary RDS bị lỗi.
  - Tránh các vấn đề liên quan đến hiệu suất của thao tác DDL
    (ví dụ như tạo Index cho Database).
  - GIúp phân mảnh một Database lớn thành nhiều Database nhỏ.
- ![Promoting a read replica](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L13_3.png?alt=media&token=aa53d587-0699-43b2-978b-0d65f9860168)

- Video: [Promoting a read replica to a standalone DB instance](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21420862#overview)

- Video: [RDS Multi-AZ failover and replica promotion - Demo](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21443800#overview)

##### Second-tier Read Replica

- Ta cũng có thể tạo ra một Read Replica từ một Read Replica khác,
  gọi là **Second-tier Read Replica**, tuy nhiên cần lưu ý rằng dữ liệu
  ở Second-tier Read Replica sẽ có độ trễ cao hơn
  vì cần phải đi ra Read Replica ban đầu,
  nhưng bù lại hiệu suất sẽ được đảm bảo hơn.

- ![Second-tier Read Replica](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L13_4.png?alt=media&token=14b013a1-cbca-4d71-974e-468423042d30)

- Video: [RDS read replica capabilities](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21420870#overview)

- Video: [RDS Second-tier replicas and replica promotion - Demo](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21440518#overview)

#### Read Replica Machenisms

##### Cross-region read replicas in RDS

- Ta có thể tạo các Read Replicas ở các Region khác nhau
  để đảm bảo khả năng phục hồi khi gặp lỗi, hoặc giúp làm giảm độ trễ
  khi đọc dữ liệu từ RDS cho những người dùng ở nhiều khu vực khác nhau.
  Tuy nhiên cách này sẽ gây ra một số hạn chế sau:
  - Độ trễ khi đồng bộ dữ liệu sẽ cao hơn
  - Tối đa chỉ có 5 Read Replicas
  - Không hỗ trợ với SQL Server
- Video: [Cross-region read replicas in RDS](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21420876#overview)

- Video tham khảo: [RDS replicas with an external database](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21420884#overview)

##### RDS disaster recovery strategies

- **Khả năng khắc phục sau sự cố (Disaster Recovery)** rất quan trọng
  khi bạn sử dụng RDS để đảm bảo hoạt động nghiệp vụ liên tục
  kể cả khi gặp sự cố/sự kiện không mong muốn.
  Dưới đây là bảng so sánh một số phương pháp:
  - **RTO (Recovery time objective)**:
    Ta mất bao lâu để hồi phục sau sự cố, thường được tính bằng giờ.
  - **RPO (Recovery point objective)**:
    Lượng dữ liệu bị mất do sự cố là bao nhiêu?
    Thường đươc tính theo đơn vị thời gian (giờ).
- ![Disaster Recovery](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L13_5.png?alt=media&token=88dfdd40-4167-4de8-9c8f-df3e7e9ec62c)

- Video: [RDS disaster recovery strategies](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21422450#overview)

##### Troubleshooting replica issues in RDS

- **Replica Lag** là độ trễ khi đồng bộ dữ liệu từ Primary RDS sang Replica RDS,
  đây là một số liệu mà bạn cần chú ý để RDS có thể hoạt động tốt,
  một số lý do làm tăng Replica Lag là:
  - Thực hiện truy vấn phức tạp và tốn thời gian thực thi để đồng bộ dữ liệu.
  - instance class size hoặc storage không đủ.
  - Các truy vấn thực thi song song ở Primary RDS.
- Video: [Troubleshooting replica issues in RDS](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21422456#overview)
- Video tham khảo: [Performance hit on new read replicas](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21422464#overview)

##### Scaling and sharding in RDS

- RDS có hai cơ chế để hỗ trợ cho việc mở rộng:

  - **Vertical Scaling (Scaling up)**:
    Tăng cấu hình cho RDS.
    ![VScaling](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L13_7.png?alt=media&token=797f3e42-1517-4171-95a0-b2b4455f3b58)
  - **Horizontal Scaling (Scaling out)**:
    Bổ sung thêm các Read Replicas để tăng hiệu suất cho hệ thồng,
    phù hợp với các bài toán có khối lượng sử dụng lớn.
    ![HScaling](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L13_6.png?alt=media&token=4536231c-645c-40cb-be8f-79105082cade)

- **Sharding** là cơ chế giúp phân tán dữ liệu thành các Database nhỏ hơn,
  sau đó sử dụng Mapping/routing để đưa truy vấn đến đúng với Database đúng.
  Từ đó giúp tăng khả năng chịu lỗi của Database do nếu một Database con bị lỗi
  thì cũng không ảnh hưởng đến các Database còn lại.
  ![Sharding](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L13_8.png?alt=media&token=fc23d794-4c0b-4577-89a4-8812b9bf77ac)
- Video: [Scaling and sharding in RDS](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21422468#overview)

### Amazon Redshift

#### Redshift overview

- **Amazon Redshift** là một kho dữ liệu nhanh chóng, được quản lý đầy đủ,
  giúp phân tích tất cả dữ liệu của ta một cách đơn giản và tiết kiệm chi phí
  bằng cách sử dụng SQL tiêu chuẩn và các công cụ thông minh kinh doanh (BI)
  hiện có của ta.

- Analytics rất quan trọng đối với các doanh nghiệp ngày nay,
  nhưng việc xây dựng một kho dữ liệu rất phức tạp và tốn kém.
  Kho dữ liệu mất nhiều tháng và nguồn tài chính đáng kể để thiết lập.
  Amazon Redshift là một kho dữ liệu được quản lý đầy đủ và nhanh chóng và mạnh mẽ,
  đơn giản và tiết kiệm chi phí để thiết lập, sử dụng và mở rộng quy mô.
  Nó cho phép ta chạy các truy vấn phân tích phức tạp dựa trên petabyte dữ liệu
  có cấu trúc bằng cách sử dụng tối ưu hóa truy vấn phức tạp, lưu trữ dạng cột
  trên các đĩa cục bộ hiệu suất cao và xử lý dữ liệu song song hàng loạt.
  Hầu hết các kết quả sẽ trở lại sau vài giây.

- Cuối cùng, Amazon Redshift **tương thích với các công cụ** mà ta đã biết
  và sử dụng. Amazon Redshift hỗ trợ SQL tiêu chuẩn.
  Nó cũng cung cấp các trình kết nối JDBC và ODBC hiệu suất cao,
  cho phép ta sử dụng các ứng dụng SQL client và các công cụ BI mà ta chọn.

- Video: [Redshift overview](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21322334#overview)

- Video: [Creating a Redshift cluster - Hands on](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21525774#overview)

#### Redshift architecture

- **Leader Node** quản lý các giao tiếp với các chương trình khách
  và tất cả các giao tiếp với các **Compute Nodes**.
  Nó phân tích cú pháp và phát triển các kế hoạch để thực hiện
  các hoạt động cơ sở dữ liệu - cụ thể là một loạt các bước cần thiết
  để thu được kết quả cho các truy vấn phức tạp.
  Leader node biên dịch mã cho các phần tử riêng lẻ của kế hoạch
  và gán mã cho các compute nodes riêng lẻ.
  Các compute nodes chạy mã đã biên dịch và gửi các kết quả trung gian
  trở lại leader node để tổng hợp cuối cùng.

  ![](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L13_9.png?alt=media&token=f70c20d7-e4f3-4c68-903a-c3fbe2377cba)

- Thật dễ dàng để **tự động hóa** hầu hết các tác vụ quản trị phổ biến để quản lý,
  giám sát và mở rộng Amazon Redshift cluster của ta

  - cho phép ta tập trung vào dữ liệu và doanh nghiệp của mình.
    Scaling là nội tại của Amazon Redshift. Cluster của ta có thể được mở rộng lên
    và xuống khi nhu cầu của ta thay đổi bằng một vài cú nhấp chuột
    trong bảng điều khiển. _Bảo mật là ưu tiên cao nhất đối với AWS._
    Với Amazon Redshift, bảo mật là nội dung và nó được thiết kế
    để cung cấp mã hóa mạnh mẽ cho dữ liệu của ta cả khi ở trạng thái nghỉ
    và khi đang chuyển.

- Video: [Redshift architecture](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21325086#overview)

#### Loading data to Redshift

- Có 3 cách được sử dụng để Load dữ liệu vào Redshift:
  - **Load dữ liệu từ các hệ thống OLTP**:
    dữ liệu từ các hệ thống OLTP được Load vào S3,
    sau đó dữ liệu ở S3 sẽ được Load vào Redshift.
    Dữ liệu từ Kinesis Firehose cũng có thể được Load theo cách này.
  - Copy dữ liệu từ S3.
  - Sử dụng Glue để tạo các ETL (Extract - Transform - Load).
- ![Loading data to Redshift](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L14_1.png?alt=media&token=6ebb238e-672e-440a-ba67-cbbf0a471d1a)

- Video: [Loading data into Redshift](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21325094#overview)

- Video: [Loading data from S3 into Redshift - Hands on](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21525784#overview)

- Video: [More ways to load data into Redshift](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21325100#overview)

#### Redshift Spectrum

- **Redshift Spectrum** là một tính năng của Amazon Redshift,
  cho phép ta chạy các truy vấn đối với hàng exabyte dữ liệu không có cấu trúc
  trên Amazon S3 mà không yêu cầu Load hoặc ETL.
  Khi ta thực thi một truy vấn, truy vấn đó chuyển tới Amazon Redshift SQL endpoint
  để tạo và tối ưu một Query Plan.
  Amazon Redshift xác định đâu là dữ liệu cục bộ và trên Amazon S3 có những gì,
  tạo một Query Plan để giảm thiểu lượng dữ liệu trên Amazon S3 cần được đọc,
  yêu cầu các Redshift Spectrum Worker (Node) ngoài phạm vi của một nhóm tài nguyên
  chia sẻ đọc và xử lý dữ liệu từ Amazon S3.
- **Chú ý**: Redshift cluster và S3 bucket phải nằm trong cùng một Region
  và khi bắt đầu thực thi truy vấn thì ta vẫn cần một **Redshift Cluster**.
  ![Redshift clusters](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L14_2.png?alt=media&token=c553e887-8774-4bbc-b193-ba7cced9698e)

- Video: [Redshift Spectrum](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21325106#overview)

- Video: [Querying S3 data with Redshift Spectrum - Hands on](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21525800#overview)

#### Redshift Federated Query

- **Redshift Federated Query** là tính năng trong RDS sử dụng để truy vấn
  và phân tích dữ liệu từ các loại Database, Data Warehouse và Data Lake khác nhau.
  Hiện nay tính năng này đã hỗ trợ trên Redshift, PostgreSQL on RDS,
  Aurora PostgreSQL và S3.

  ![Redshift Federated Query](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L14_3.png?alt=media&token=ccc902f4-83ef-4544-bddc-c89bada1c198)

- Video: [Redshift federated query](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21325108#overview)
- Video tham khảo: [Star schema in data warehouses](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21326272#overview)

### Scaling, Monitoring and Security in Redshift

#### Redshift fundamentals

- Khi sử dụng **Redshift**, ta sẽ cần lưu ý những vẫn đề sau:

  - Redshift không hỗ trợ cơ chế index.
    Thay vào đó thì Redshift hỗ trợ **sort key**,
    tức là dữ liệu sẽ được lưu trữ xuống ổ cứng
    theo thứ được sắp xếp của các sort key.
  - Các ràng buộc về **Primary Key, Unique keys và Foreign key** không được thực thi
    (chỉ mang tính chất thông tin). Trình tối ưu hóa truy vấn sử dụng các ràng buộc
    này để tạo các Query Plan hiệu quả hơn.
  - Ta có thể thực thi các mối quan hệ PK/FK thông qua ứng dụng của mình.

- Để thiết kế một Table phù hợp trong Redshift, ta sẽ cần **lưu ý** các điểm sau:

  - **Data distribution**: Dữ liệu được phân bố ở các Node như thế nào.
  - **Sort strategies**: Dữ liệu sẽ được sắp xếp ở các bảng như thế nào.
  - **Compression**: Tối ưu hóa bộ nhớ và giảm thiểu các thao tác I/O

- Video: [Redshift fundamentals](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21326278#overview)

#### Redshift Workload Management (WLM)

- **Redshift Workload Management (WLM)** là tính năng trong Redshift giúp ta
  sắp xếp, ưu tiên các khối lượng công việc trong Redshift,
  từ đó giúp tránh các trường hợp các truy vấn phức tạp,
  cần nhiều thời gian thực thi ảnh hưởng đến các truy vấn ngắn.
  WLM được chia ra làm 2 chế độ là Automatic WLM và Manual WLM,
  một số lưu ý khi thiết lập WLM như sau:

  - WLM cũng sử dụng **Parameter Groups** để thiết lập.
  - Các **trường** trong WLM cũng được chia ra làm 2 loại là **Dynamic và Static**.
  - Để chuyển chế độ của WLM thì ta sẽ cần khởi động lại cluster.

- Video: [Redshift Workload Management (WLM)](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21326760#overview)

#### Redshift Concurrent Scaling

- **Concurrency Scaling** là một tính năng trong RDS giúp tự động mở rộng
  "sức chứa" (capacity) của cluster để có thể đáp ứng việc có nhiều người dùng
  hoặc nhiều truy vấn đồng thời (có thể mở rộng không giới hạn số lượng truy vấn).
  Ta vẫn có thể thực hiện các thao tác đọc/ghi dữ liệu
  ngay cả khi Concurrency Scaling được thực thi.

- Video: [Redshift concurrency scaling](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21326764#overview)

#### Redshift scaling

- Redshift hỗ trợ các cơ chế mở rộng như sau:
  - **Elastic Resize**: Thêm hoặc bớt các Node từ một Cluster có sẵn,
    và sẽ cần một khoảng thời gian để thực hiện thao tác này (từ 4 đến 8 phút).
    Đây là một thao tác thủ công và Cluster sẽ không khả dụng
    khi quá trình này diễn ra.
    ![Elastic Resize](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L15_1.png?alt=media&token=2b8885c6-d00d-424b-8e5b-75735c58472c)
  - **Classic resize**: Thay đổi Node Type, số lượng Node.
    Sau đó sẽ sao chép dữ liệu từ Cluster cũ sang Cluster mới,
    trong khi quá trình này diễn ra thì Source Cluster
    chỉ có thể được đọc dữ liệu (Read-only).
    ![Classic resize](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L15_2.png?alt=media&token=268a3939-2239-4dbb-96b5-09e4765ab5f6)
  - **Snapshot, restore, and classic resize**:
    Sao chép cluster và resize cluster vừa được sao chép,
    sau đó mới chuyển dữ liệu từ Source Cluster sang Cluster mới.
    Cách này khác với Classic resize là Source Cluster
    vẫn sẽ khả dụng khi quá trình diễn ra.
    ![Snapshot, restore, and classic resize](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L15_3.png?alt=media&token=f84f7078-9e8d-497b-abd3-ae5a874031c3)
- Video: [Redshift scaling](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21329864#overview)

#### Redshift backup

- Redshift duy trì ít nhất ba bản sao dữ liệu của ta:
  Bản chính, Replica ở trên Compute Nodes và bản Backup ở S3 (Snapshot).
  Một số lưu ý về Snapshot trong Redshift:
  - Là cơ chế point-in-time backups của Cluster, được lưu ở S3.
  - Snapshot sẽ chỉ lưu các thay đổi ở trên Cluster.
  - Bạn có thể khôi phục Snapshot thành một Cluster mới.
  - Gồm 2 loại:
    - **Automated**:
      sẽ tự động xóa đi khi đạt điều kiện (sau 8 giờ, mỗi 5GB dữ liệu,...)
    - **Manual** - Snapshot sẽ tồn tại đến khi ta xóa nó đi.
- Video: [Redshift backup, restore and cross-region snapshot](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21331668#overview)

#### Redshift multi-AZ deployment alternative

- Một điểm bạn cần lưu ý là Redshift không hỗ trợ cơ chế Multi-AZ,
  tuy nhiên bạn có thể sử dụng một số cách sau để thay thế:
  - Tạo các Redshift clusters ở nhiều Availability Zone
    bằng cách tải dữ liệu ở nhiều Availability Zone khác nhau.
  - Khôi phục Cluster Snapshot ở một Availability Zone khác.
  - Sử dụng Spectrum để đọc dữ liệu S3 từ các Cluster
    ở các Availability Zone khác nhau.
- ![No Multi-AZ](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L15_4.png?alt=media&token=6bf7cca0-b571-4812-b07f-cead1b8c6ebe)
- Video: [Redshift Multi-AZ deployment alternative](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21331674#overview)

#### Redshift available and durability

- Một số trường hợp có thể ảnh hưởng đến Redshift như sau:
  - **Drive failure**:
    Redshift cluster vẫn còn hoạt động nhưng hiệu suất truy vấn bị giảm mạnh.
    Để giải quyết vấn đề này thì ta có thể restore lại từ Snapshot trên S3.
  - **Node failure**:
    Redshift hỗ trợ tự động phát hiện và thay thế các Node bị lỗi,
    Cluster sẽ không khả thi đến khi Node được thay thế.
  - **AZ outage**:
    Đây là trường khi Availability Zone gặp sự cố dễ đến Cluster không khả thi,
    ta có thể khôi phục Cluster từ Snapshot và đặt vào một Availability Zone khác.
- Video: [Redshift availability and durability](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21331686#overview)

#### Redshift security

- Quyền truy cập vào các tài nguyên Redshift được kiểm soát ở 4 cấp độ:

  - **Cluster management**: sử dụng IAM policies.
  - **Cluster connectivity**: sử dụng cluster security groups/VPC.
  - **Database access**:
    sử dụng các người dùng/group và các quyền truy cập trong Database.
  - **IAM Authentication**

- Video: [Redshift security](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21331694#overview)

- Video: [Enhanced VPC routing in Redshift](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21332256#overview)

#### Redshift mornitoring

- Để giám sát một Redshift, bạn có thể sử dụng một số cách sau:
  - Sử dụng **CloudWatch** để giám sát việc sử dụng CPU, độ trễ và thông lượng,...
  - Sử dụng **Amazon Redshift console** để giám sát hiệu suất của Cluster,
    lịch sử truy vấn, hiệu suất DB, concurrency scaling,...
  - Sử dụng **Redshift Advisor** để đưa ra các đề xuất để tối ưu hóa chi phí
    và điều chỉnh hiệu suất phù hợp.
- Video: [Redshift monitoring](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21331698#overview)

### Lab 10 Redshift Cluster

- [Description](https://courses.funix.edu.vn/courses/course-v1:FUNiX+DEP304x_01-A_VN+2021_T11/courseware/3a8c750402a24420904c42983322073a/445aa26c514d47dd8af76324f6eff64b/?child=first)
- Các bước thực hiện:

  1. Tạo Redshift Cluster:

     - Ta cần vào Redshift Dashboard, sau đó nhấn "**Create Cluster**".
       Lưu ý: để tránh ta bị tính phí khi sử dụng Redshift,
       ta cần chọn "Free Trial" và sử dụng các tham số đã được thiết lập trước đó.
       ![create cluster](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FLab_Image%2FDEP304_Lab_10_1.png?alt=media&token=1b694c3d-616a-4f1e-b33e-a1d45a40d92e)

  2. Thiết lập "Publicly accessible" cho Cluster:

     - Để có thể kết nối với Redshift Cluster,
       ta sẽ cần thay đổi thiết lập "Publicly accessible" của Redshift.
       Chọn "Action" => "Modify publicly accessible setting"
       ![Edit public accessible](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FLab_Image%2FDEP304_Lab_10_2.png?alt=media&token=1dfe2627-5794-4db5-b922-9e7aac154ce9)

  3. Kết nối với Redshift thông qua Jetbrain DataGrip:

     - Ta sẽ cần sử dụng một công cụ là DataGrip để kết nối
       và thực hiện các truy vấn vào Redshift,
       về cách cài đặt và kết nối ta có thể tham khảo các tài liệu sau:

       - [Cài đặt DataGrip](https://www.jetbrains.com/help/datagrip/installation-guide.html)
       - [Sử dụng Educational Licenses cho các ứng dụng của Jetbrain](https://www.jetbrains.com/community/education/#students)
       - [Tạo Database Connection trong DataGrip](https://www.jetbrains.com/help/datagrip/connecting-to-a-database.html)
       - [Kết nối với Redshift.](https://www.jetbrains.com/help/datagrip/amazon-redshift.html)

  4. Sau đó, ta có thể thử viết truy vấn đề lấy dữ liệu từ bảng "public.category",
     nếu được kết quả sau thì ta đã thành công:
     ![result](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FLab_Image%2FDEP304_Lab_10_3.png?alt=media&token=a1a521f4-77e9-4d71-9f6b-e4032cbf71fb)

### Amazon DocumentDB

#### Amazon DocumentDB Introduction

##### Amazon DocumentDB Overview

- Amazon DocumentDB là một Fully-managed Database Service trong AWS.
  **Amazon DocumentDB** là một Document-base cho các MongoDB workloads.
  **Tương tự với MongoDB** thì dữ liệu ở trong DocumentDB
  cũng được lưu ở dạng JSON Document trong các Collection.
- Một số ưu điểm của DocumentDB như sau:
  - Hỗ trợ lập chỉ mục linh hoạt, truy vấn đặc biệt mạnh mẽ và phân tích
  - Lưu trữ và tính toán có thể mở rộng quy mô độc lập.
  - Hỗ trợ 15 read replicas (Multi-AZ) với độ trễ thấp.
  - Hỗ trợ Auto scaling cho việc lưu trữ từ 10 GB đến 64 TB.
  - Bộ nhớ có khả năng chịu lỗi và tự phục hồi.
  - Automatic, continuous, incremental backups và PITR.
- Video: [DocumentDB overview](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21302388#overview)
-
- Video: [What and why about document databases](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21302884#overview)

##### Amazon DocumentDB Architecture

- Kiến trúc của DocumentDB khá giống với Aurora và là một dạng thiết kế phân tán.
  DocumentDB sẽ được tạo ra thành **6 bản sao ở 3 Availability Zone**, trong đó:

  - 4 bản sao cần thiết cho thao tác ghi,
    dữ liệu được coi là bền khi ít nhất 4/6 bản sao đảm nhận thao tác ghi.
  - 3 bản sao cần thiết cho thao tác đọc dữ liệu.

- Ngoài ra, có một số lưu ý như sau:

  - Các Compute Nodes trên bản sao sẽ không cần đảm nhận các thao tác ghi dữ liệu,
    từ đó giúp tăng hiệu suất cho các thao tác đọc dữ liệu.
  - Có thể tạo đến 15 Read Replicas.
  - Dữ liệu sẽ được lưu trữ liên tục trên S3 theo thời gian thực.

- ![DocumentDB Architecture](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L16_1.png?alt=media&token=93a6b593-4d5e-4e98-816d-ac521582de13)

- DocumentDB cũng có một số tính chất sau về việc tạo các bản sao dữ liệu:

  - Có thể tạo đến 15 Read Replicas.
  - Quá trình sao chép là bất đồng bộ.
  - Các bản sao chia sẻ cùng một cơ sở hạ tầng.
  - Vẫn sẽ có Replication Lag.
  - Hiệu suất sẽ bị ảnh hưởng một chút trong quá trình sao chép.

- Cơ chế hồi phục sau sự cố cũng **gần giống với Aurora**, một bản sao (replica)
  sẽ được tự động chuyển thành Primary ngay trong quá trình hồi phục
  (DocumentDB sẽ chuyển các kết nối đến Primary sang Replica phù hợp nhất),
  quá trình này sẽ mất tầm 30 giây downtime.
  Hoặc ta có thể tạo một Instance mới (quá trình này sẽ mất tầm 8-10 phút).

- Video: [DocumentDB architecture](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21305224#overview)

#### Amazon DocumentDB Machenism

##### DocumentDB backup and restore

- Cơ chế Backup and Restore trong DocumentDB giống với RDS,
  các bản backup này mặc định sẽ được lưu trữ trong 7 ngày
  (ta có thể chỉnh sửa tham số này theo khoảng từ 0 - 35 ngày,
  nếu là 0 ngày tức là sẽ không backup nữa).
  Trong **lần backup đầu tiên**, toàn bộ dữ liệu sẽ được backup,
  nhưng ở **các lần tiếp theo** thì DocumentDB sẽ chỉ backup các dữ liệu
  đã được thay đổi (Incremental Data), bản Backup sẽ được lưu trữ ở một S3 Bucket.
  Quá trinh backup sẽ không ảnh hưởng đến hiệu suất của Performance.

- Một số lưu ý như sau:

  - Ta chỉ có thể khôi phục thành một Cluster mới.
  - Có thể khôi phục từ Snapshot không được mã hóa thành một Cluster được mã hóa
    (nhưng ngược lại thì không được).
  - Để khôi phục từ Snapshot được mã hóa thì ta sẽ cần truy cập với KMS key.
  - Ta chỉ có thể chia sẻ các Manual Snapshot (có thể sao chép tự động).
  - Ta có thể chia sẻ Snapshot cho những Account khác nhau,
    **nhưng phải ở cùng một Region**.

- Video: [DocumentDB backup and restore](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21303346#overview)

##### DocumentDB scaling

- DocumentDB cũng hỗ trợ 2 cơ chế mở rộng là:

  - **Vertical scaling (scale up / down)**:
    nâng cấp Instance.
  - **Horizontal scaling (scale out / in)**:
    Thêm các Instance, và có thể thêm lên tới 15 Read Replicas.

- Tuy nhiên, cơ chế Sharding trong MongoDB hiện tại chưa được DocumentDB hỗ trợ.
  Các bản sao có thể được mở rộng độc lập với các bản sao khác,
  thường để phục vụ cho các công việc liên quan đến phân tích.
  Ngoài ra, còn **có cơ chế mở rộng dung lượng tự động** từ 10GB đến 64TB
  (không cần thao tác thủ công).
- Video: [DocumentDB scaling](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21303350#overview)

##### DocumentDB security

- Về cơ chế bảo mật, ta vẫn có thể sử dụng IAM để quản lý các quyền truy cập,
  ngoài ra còn hỗ trợ một số cơ chế sau:

  - **MongoDB SCRAM (Salted Challenge Response Authentication Mechanism)**
    cho việc xác thực vào Database.
  - **RBAC (role-based access control)** để tạo các Role trong Database.
  - **Encryption at rest/transit**.

- DocumentDB clusters **chỉ sử dụng được trong một Private Subnet**,
  còn Clients (MongoDB shell) **có thể chạy trên một EC2 với Public Subnet**.

- Video: [DocumentDB security](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21303372#overview)

##### DocumentDB monitoring

- Ta có thể thực hiện các thao tác giám sát qua một số cách sau:
  - Thông qua API log từ CloudTrail.
  - Thông qua các chỉ số từ CloudWatch.
    CloudWatch cũng hỗ trợ hai loại log là **Profiler logs** và **Audit logs**.
- **DocumentDB Profiler (profiler logs)** sẽ ghi lại chi tiết các hoạt động
  được thực hiện trên Cluster của bạn, từ đó giúp xác định các hoạt động chậm
  và cải thiện hiệu suất truy vấn.

- **DocumentDB audit logs** sẽ ghi lại các câu lệnh DDL,
  xác thực, ủy quyền và các sự kiện quản lý người dùng.

- Video: [DocumentDB monitoring](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21303376#overview)

##### DocumentDB pricing

- Một số câu lệnh bạn có thể sử dụng để quản lý hiệu suất trong DocumentDB là:
  ```js
  db.runCommand({explain: {<query document>}})
  db.adminCommand({killOp: 1, op: <opid of the query>});
  ```
  Video: [DocumentDB performance management](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21304390#overview)

Video tham khảo: [DocumentDB pricing](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21303374#overview)

Video: [Creating a DocumentDB cluster - Hands on](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21557286#overview)

## Assignment 2: Build up database for Google Play Store

- [FUNiX Course](https://courses.funix.edu.vn/courses/course-v1:FUNiX+DEP304x_01-A_VN+2021_T11/courseware/3a8c750402a24420904c42983322073a/fcaa452069b14f5d8fb4e892542003c4/?child=first)

### Project overview

- Google Play Store là một chợ ứng dụng của hệ điều hành Android
  cho phép người dùng tìm kiếm và tải các ứng dụng, trò chơi
  về thiết bị di động của mình, dưới sự quản lý của Google.
  Ở bài Assignment này, ta sẽ thực hành để xây dựng một cơ sở dữ liệu
  để lưu trữ các thông tin ứng dụng trên Google Play Store sử dụng Amazon RDS.

  - Tạo được VPC cho hệ thống.
  - Tạo được Security Group và Subnet Group.
  - Tạo và thiết lập được RDS phù hợp với yêu cầu hệ thống.
  - Import được dữ liệu lên RDS.
  - Tạo được Snapshot cho RDS và có thể khôi phục dữ liệu từ Snapshot đó.
  - (Nâng cao) So sánh hiệu năng giữa Amazon RDS và On Premise Database.

### Solution

- Để hoàn thành bài Assignment này, ta sẽ cần tạo tài khoản trên AWS
  và đăng ký để sử dụng Free Tier của AWS.
  Sau đó ta cũng cần tài xuống các Datasets ở phần "Tài nguyên"
  để có thể hoàn thành bài tập.
- Đồng thời, ta cũng sẽ cần cài đặt phần mềm Jetbrain DataGrip để thực hiện các truy vấn và thao tác import dữ liệu.

### Resources

- Ta sẽ cần tải Dataset tại [Link sau](https://drive.google.com/drive/folders/1mzGazJVwJRXFJkTtz6p-bA27eWg2ecJO?usp=sharing) để có thể hoàn thành bài tập này.
  Dataset sẽ gồm 2 file như sau:

  - app.csv: File csv chứa thông tin về các ứng dụng trên Google Play Store.
  - review.csv: FIle csv chứa các đánh giá về ứng dụng trên Googgle Play Store.

- Một số tài liệu khác:
  - [Cài đặt DataGrip](https://www.jetbrains.com/help/datagrip/installation-guide.html)
  - [Sử dụng Educational Licenses cho các ứng dụng của Jetbrain](https://www.jetbrains.com/community/education/#students)
  - [Tạo Database Connection trong DataGrip](https://www.jetbrains.com/help/datagrip/connecting-to-a-database.html)
  - [Import file csv trong DataGrip](https://www.jetbrains.com/datagrip/features/importexport.html)

## AWS Data Pipeline

### AWS Database Migration Service

#### Database migration overview

- Data Migration (Di chuyển dữ liệu)
  là quá trình di chuyển dữ liệu giữa các hệ thống lưu trữ dữ liệu,
  các định dạng dữ liệu hay giữa các hệ thống máy tính.
  Một dự án Data Migration thường được triển khai trong các trường hợp sau:

  - Thay thế hoặc nâng cấp máy chủ hay các thiết bị lưu trữ dữ liệu
  - Tích hợp các website
  - Bảo trì máy chủ
  - Di dời trung tâm dữ liệu hoặc thay đổi loại cơ sở dữ liệu
  - Nhân bản cơ sở dữ liệu sang các region khác

- Data Migration có thể gây ảnh hưởng tới các hoạt động nghiệp vụ
  khi nó kéo dài các khoảng thời gian chết, các vấn đề về hệ thống
  và khả năng tương thích hệ thống. Vì vậy khi thực hiện dự án data migration,
  chúng ta cần phải tìm giải pháp để tối thiểu hóa các ảnh hưởng tiêu cực
  lên hệ thống.

- Có 3 dạng Migration như sau:

  - **Homogeneous DB Migration**:
    Source và Target có cùng Database Engine.
  - **Heterogeneous DB Migration**:
    Source và Target sử dụng hai Database Engine khác nhau.
    Lúc này ta sẽ cần thêm một bước biến đổi Schema để đồng nhất với nhau.
  - **DW Migration**:
    Di chuyển dữ liệu vào một Data Warehouse.

- ![Migration flow](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L17_1.png?alt=media&token=84979b4b-7490-448a-8f58-0416781c0e52)

- Video: [Database migration overview](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21352262#overview)

- Video: [DMS sources and targets](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21367468#overview)

#### DMS architecture and overview

- **AWS Database Migration Service (AWS DMS)**
  giúp bạn thực hiện các quá trình Data Migration một cách nhanh chóng và bảo mật.
  Cơ sở dữ liệu nguồn vẫn duy trì toàn bộ hoạt động trong quá trình di chuyển,
  giúp giảm thiểu thời gian ngừng hoạt động của các ứng dụng phụ thuộc
  vào cơ sở dữ liệu đó.
  AWS DMS hỗ trợ cả Homogeneous DB Migration và Heterogeneous DB Migration.

- ![DMS architecture](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L17_2.png?alt=media&token=a82e48c8-4933-4ff2-b092-0eb544d3939d)

- Video: [DMS architecture and overview](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21367470#overview)

- Video: [Migration with DMS in action - Hands on](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21563104#overview)

#### Schema Conversion Tool overview

- **AWS Schema Conversion Tool (SCT)**
  là dịch vụ giúp chuyển đổi Schema của Database, Data Warehouse
  từ Source sang Target
  (bao gồm các procedures/views/secondary indexes/khóa phụ và các ràng buộc),
  chủ yếu được sử dụng cho _Heterogeneous DB Migration_ hoặc _DW Migration_.

- Bao gồm 2 loại chuyển đổi:

  - **Application conversion**:
    Có thể chuyển đổi các câu lệnh SQL được nhúng trong mã nguồn của ứng dụng.
  - **Script conversion**:
    Di chuyển các ETL scripts (Oracle/Microsoft/Teradata scripts )
    sang Aurora/Redshift scripts.

- SCT cũng cung cấp các báo cáo đánh giá,:

  - Báo cáo chi tiết hiển thị đối tượng nào có thể được chuyển đổi tự động
    và đối tượng nào cần can thiệp thủ công (với mã màu).
  - Có thể được sử dụng để tạo một bussiness case khi chuyển đổi.
  - Xác định các vấn đề/hạn chế/hành động để chuyển đổi Schema.
    - Objects that can be converted automatically
    - Objects that can be converted with simple actions
    - Objects that can be converted with medium-complexity actions
    - Objects that require complex actions for conversion

- Đối với các đối tượng không thể được tạo theo cách thủ công,
  SCT cung cấp hướng dẫn để giúp bạn tạo Schema tương đương theo cách thủ công.

- Video: [SCT overview](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21367472#overview)

#### DMS tasks and task assessment reports

- **DMS tasks (replication tasks)** giúp bạn thiết lập các tùy chọn
  khi di chuyển dữ liệu như:

  - _Table mapping_ (quy tắc khi di chuyển).
  - _Filters_ (lựa chọn các dữ liệu để di chuyển).
  - _Migration type_ (full load, CDC hoặc cả hai).

- Ngoài ra, DMS Tasks cũng giúp xác thực dữ liệu
  hoặc các thao tác giám sát (task status, task's control table).

- Video: [DMS tasks and task assessment reports](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21367476#overview)

#### DMS migration types

- DMS có 3 dạng migration như sau:

  - **Full Load**:
    Di chuyển các dữ liệu có sẵn và chỉ di chuyển 1 lần từ Source sang Target.
  - **CDC Only**:
    Di chuyển các dữ liệu đang "thay đổi" từ Source sang Target
    và không di chuyển các dữ liệu có sẵn.
  - **Full Load + CDC**:
    Kết hợp cả Full Load và CDC Only.

- Video: [DMS migration types](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21367478#overview)
- Video tham khảo: [Workload Qualification Framework (WQF)](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21367474#overview)
- Video tham khảo: [DMS - Good things to know](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21367482#overview)

### Database Migration operators

#### A number of parts in DMS

##### Migrating large tables and LOBs

- Khi thực hiện thao tác di chuyển dữ liệu lớn,
  ta nên chia nhỏ ra thành các nhiều task để thực hiện.
  Khi này ta sẽ cần chia nhỏ các dữ liệu,
  ví dụ nếu ta có khóa chính số nguyên từ 1 đến 8.000.000
  thì ta cần tạo 8 task bằng cách sử dụng row filtering
  để di chuyển 1.000.000 bản ghi mỗi tác vụ.

- Trong DMS có một số khái niệm như sau:

  - **LOB** = **Large Binary Object**.
    DMS sẽ di chuyển dữ liệu LOB theo hai bước:
    - tạo một hàng mới trong bảng Target
      và điền tất cả dữ liệu ngoại trừ dữ liệu LOB,
    - sau đó cập nhật hàng với dữ liệu LOB.
  - **CLOB** = **Character Large Object**.

- ![Migrating large tables and LOBs with DMS](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L18_1.png?alt=media&token=a72890a2-f036-42e2-875a-36bdc138e048)

- DMS có một số tùy chọn khi di chuyển dữ liệu LOB như sau:

  - "Don't include LOB columns": dữ liệu LOB bị bỏ qua.
  - "Full LOB mode":
    di chuyển tất cả dữ liệu LOB,
    từng phần một (ta cung cấp kích thước phân đoạn LOB).
  - "Limited LOB mode": cắt ngắn từng LOB thành kích thước LOB tối đa (nhanh hơn).

- Video: [Migrating large tables and LOBs with DMS](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21367484#overview)

##### DW migration with SCT

- SCT Extractors là một migration agent được cài đặt cục bộ,
  hoặc là cài đặt trên EC2 giúp trích suất dữ liệu từ một Source song song với nhau
  và các dữ liệu này sẽ được tối ưu hóa cho Redshift
  là được lưu trữ ở các file cục bộ, sau đó các file sẽ được chuyển lên S3,
  cuối cùng thì bạn sẽ dùng câu lệnh COPY để import dữ liệu từ S3 vào Redshift.

- Biểu đồ sau mô tả quá trình DW migration với SCT:
  ![DW migration with SCT](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L18_2.png?alt=media&token=2d9710dd-694b-49b2-aed2-5d387bc9cfc3)

- Video: [DW migration with SCT](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21367486#overview)

##### Migration playbooks

- Migration playbooks là tập hợp bao gồm các hướng dẫn sử dụng DMS
  được cung cấp bởi AWS, cung cấp các phương pháp hay nhất
  và bản thiết kế cho các quá trình Heterogeneous Migrations khác nhau.

- ![Migration playbooks](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L18_3.png?alt=media&token=a80a1de7-a64a-4f42-90e1-37b834319f53)

- Video: [Migration playbooks](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21563556#overview)

#### DMS Machenism

##### DMS monitoring

- Ta có thể giám sát thông tin các task thông qua các cách sau:

  - Kiểm tra trạng thái của task
  - Sử dụng task’s control table
  - Sử dụng Cloud Watch

- **DMS Task Logs** sẽ lưu lại một số vấn đề/cảnh báo/thông báo lỗi DMS,
  ví dụ như data truncation issues hoặc row rejections
  do khóa ngoại vi phạm chỉ được ghi vào nhật kí DMS Task Logs.

- Video: [DMS monitoring](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21604086#overview)

##### DMS statistics and control tables

- **Table statistics**:
  Hiển thị trạng thái của từng bảng (thống kê hiệu suất)
  đang trong quá trình miragte.

- **Control tables**:
  Hỗ trợ khắc phục các sự cố trong quá trình di chuyển dữ liệu.
  Cung cấp số liệu thống kê hữu ích để giúp bạn lập kế hoạch
  và quản lý các migration Task.

- Video: [DMS statistics and control tables](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21604142#overview)

##### DMS security

- Ta có thể sử dụng IAM để quản lý các quyền và khả năng truy cập
  vào các tài nguyên của DMS.

- DMS cũng hỗ trợ mã hóa các endpoints sử dụng SSL certificates:

  - Có thể gán chứng chỉ cho một End point (thông qua bảng điều khiển DMS hoặc API).
  - Mỗi End point có thể cần cấu hình SSL khác nhau tùy thuộc vào Database Engine.

- Ngoài ra, DMS cũng có cơ chế Encryption at rest cho việc lưu trữ sử dụng KMS.
  DMS có một số cách thiết lập liên quan đến mặt Networking như sau:

  - **Single VPC**: Tất cả các thành phần nều nằm trong một VPC.
    ![single vpc](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L18_4.png?alt=media&token=0d90fc3f-f67f-4ccc-a434-085ab110d59e)
  - **Two VPCs**: Source và Target sẽ nằm ở hai VPC khác nhau,
    và sử dụng VPC Peering để kết nối giữa hai VPC.
    Một lưu ý là bạn sẽ được hiệu suất tốt hơn nếu để
    DMS replication instance trong cùng AZ với Target.
    ![two vpcs](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L18_5.png?alt=media&token=d005f0c8-365b-49f7-a2d8-6830316e8f92)
  - **On-premises to VPC**: Sử dụng DX hoặc VPN để kết nối giữa
    On-premises Database và Target Database.
    ![on-premises to vpc](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L18_6.png?alt=media&token=da1adaf7-5564-47e4-8131-4c30cef3fdb7)
  - **RDS outside VPC to VPC**: Sử dụng ClassicLink với máy chủ proxy để kết nối.
    ![RDS outside VPC to VPC](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L18_7.png?alt=media&token=d44a5f42-7b3f-40a3-ab99-77f576654eef)

- Video: [DMS security - IAM, encryption and networking](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21604148#overview)

##### DMS general best practices

- Một số kiến trúc mà bạn có thể sử dụng để giảm thiếu downtime
  khi thực hiện các thao tác di chuyển dữ liệu như sau:

  - Fallback
    ![fallback](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L18_8.png?alt=media&token=647280ac-1e88-4cf6-b68c-51a743671a9c)
  - Roll forward/Fall forward
    ![roll forward/fall forward](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L18_9.png?alt=media&token=192584c4-5c93-4f62-8879-4adad39df45e)
  - Dynamic connection
    ![dynamic connection](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L18_10.png?alt=media&token=af149d74-42a2-41aa-a993-ff89ac6c3bb4)
  - Dual write
    ![dual write](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L18_11.png?alt=media&token=b10d98dd-a75b-4686-b7c2-1b33c661b104)

- Video: [DMS general best practices](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21604164#overview)

- Video: [DMS migration architectures to minimize downtime](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21604166#overview)

- Video tham khảo: [DMS pricing](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21604156#overview)

#### Frequently DMS Process

- Để thực hiện các thao tác di chuyển các Database lớn,
  ta sẽ cần lưu ý một số điều như sau:

  - Sử dụng di chuyển nhiều bước (multiphase).
  - Sao chép các bảng tĩnh trước (trước khi di chuyển các bảng đang hoạt động).
  - Dọn dẹp dữ liệu cũ không cần thiết để giảm kích thước Database.
  - Ngoài ra, sử dụng Snowball Edge để di chuyển dữ liệu sang S3
    và sau đó di chuyển bằng DMS.
  - Video: [Migrating large databases](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21605014#overview)

- Ở hai video dưới đây sẽ hướng dẫn ta quy trình để thực hiện di chuyển dữ liệu
  từ một số Source và Target phổ biến như RDS, DocumentDB, Aurora,...

  - Video: [Migrating to RDS databases](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21605534#overview)
  - Video: [Migrating to DocumentDB](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21609646#overview)

- Video tham khảo: [Streaming use cases for DMS](https://funix.udemy.com/course/aws-certified-database-specialty-dbs/learn/lecture/21609652#overview)

### Amazon Glue

#### What is Glue?

- AWS Glue là dịch vụ tích hợp dữ liệu Severless, giúp người dùng dễ dàng tìm kiếm,
  chuẩn bị và tổng hợp dữ liệu cho hoạt động phân tích, máy học
  và phát triển ứng dụng. AWS Glue cung cấp tất cả các chức năng cần thiết
  cho quá trình tích hợp dữ liệu (ETL) để ta có thể bắt đầu phân tích
  và đưa dữ liệu vào sử dụng chỉ trong ít phút thay vì vài tháng như trước.

- Glue crawler giúp quét các dữ liệu từ S3 và sau đó tạo các Schema tương ứng.
  Các công việc này có thể thực hiện định kỳ, từ đó giúp tạo Glue Data Catalog
  và giúp các dịch vụ khác như Glue, Athena có thể xem được dữ liệu ở S3
  dưới dạng một Database với cấu trúc rõ ràng.

- Video: [What is Glue? + Partitioning your Data Lake](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/14077116#overview)

#### Glue ETL

- Glue ETL là một trình tạo code tự động, giúp tạo hoặc chỉnh sửa mã ETL
  bằng Python hoặc Scala. Có thể cung cấp các tập lệnh Spark hoặc PySpark
  của riêng ta, Target có thể là S3, JDBC (RDS, Redshift),
  hoặc trong Glue Data Catalog. Glue ETL cho phép ta phát triển ETL script
  và tạo ETL Job để chạy ETL đó thông qua Notebook.

- **DynamicFrame** là một tập hợp các DynamicRecords:
  ![Dyanmic Frame](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L19_1.png?alt=media&token=59b3f016-32e7-4d57-87e3-d4fd47cb570d)

  - DynamicRecords tự mô tả và có một Schema.
  - Rất giống với Spark DataFrame, nhưng với nhiều thứ liên quan đến ETL hơn.
  - Là Scala và Python APIs.

- Video: [Glue, Hive, and ETL](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/14077122#overview)

- Video: [Glue ETL: Developer Endpoints, Running ETL Jobs with Bookmarks](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/17411932#overview)

#### Glue Costs and Anti-Patterns

- Khi sử dụng AWS Glue, ta sẽ cần thanh toán theo số phút cho các công việc
  thu thập thông tin và ETL. Development endpoints để phát triển mã ETL
  được tính phí theo phút.

- AWS Glue hỗ trợ các Engine sau:

  - Glue ETL dựa trên Spark.
  - Nếu ta muốn sử dụng các động cơ khác (Hive, Pig,...)
    thì **Data Pipeline EMR** sẽ phù hợp hơn.
  - Glue ETL hỗ trợ serverless streaming ETL,
    sử dụng Apache Spark Structured Streaming.

- Video: [Glue Costs and Anti-Patterns](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/14077128#overview)

#### AWS Glue Studio

- AWS Glue Studio là một giao diện giúp trực quan hóa ETL Workflow
  cũng như giúp ta chỉnh sửa các ETL Job trực quan hơn:
  - Tạo DAG cho quy trình công việc phức tạp
  - Các Source bao gồm S3, Kinesis, Kafka, JDBC
  - Target là S3 hoặc Glue Data Catalog
- Video: [AWS Glue Studio](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/25339532#overview)

#### AWS Glue DataBrew

- AWS Glue DataBrew là một công cụ chuẩn bị dữ liệu trực quan,
  cung cấp giao diện trực quan để làm các công việc tiền xử lý dữ liệu từ S3,
  data warehouse hoặc Database và đưa dữ liệu về S3.

- Video: [AWS Glue DataBrew](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/25339538#overview)

#### AWS Lake Formation

- AWS Lake Formation là một dịch vụ giúp ta dễ dàng thiết lập một hồ dữ liệu
  bảo mật chỉ trong vài ngày. Hồ dữ liệu là một kho lưu trữ trung tâm,
  được chọn lọc và bảo mật để chứa toàn bộ dữ liệu của ta,
  ở cả định dạng gốc lẫn chuẩn bị cho tác vụ phân tích.
  ![AWS Lake formation](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L19_3.png?alt=media&token=8d9b2c1d-a8f3-406e-a202-d2ed02f3c0a3)

- Video: [AWS Lake Formation](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/25339550#overview)

- Video tham khảo: [AWS Glue Elastic Views](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/25339546#overview)

### Elastic MapReduce (EMR)

#### Elastic MapReduce (EMR) Architecture and Usage

- Amazon EMR (Elastic MapReduce) là một nền tảng xử lý, phân tích và ứng dụng
  nhanh chóng công nghệ máy học (ML) vào dữ liệu lớn bằng cách
  sử dụng các khung mã nguồn mở. Gần tương đồng với việc ta sử dụng Hadoop
  trên một EC2 Instance, bao gồm Spark, HBase, Presto, Flink, Hive,...
  và EMR Notebooks.

- Một ERM Cluster sẽ bao gồm các thành phần sau:

  - **Master node**: Chịu trách nhiệm quản lý CLuster, theo dõi trạng thái của task, tình trạng của Cluster.
  - **Core node**: Lưu trữ dữ liệu HDFS và chạy các task.
  - **Task node**: Chỉ thực hiện các task chứ không lưu trữ dữ liệu.

- ![ERM Cluster](https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FData%20Engineer%2FDEP304x%2FSumary_Image%2FDEP304_sum_L19_4.png?alt=media&token=0ba562a2-84e5-4973-b0a0-61853cf22704)

- Video: [Elastic MapReduce (EMR) Architecture and Usage](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/14077134#overview)

- Video: [EMR, AWS integration, and Storage](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/14085792#overview)

#### EMR Promises; Intro to Hadoop

- **EMR promises** giúp cung cấp các Node mới nếu có một Node nào đó gặp lỗi
  một cách nhanh chóng, từ đó tăng khả năng xử lý,
  nhưng không tăng dung lượng HDFS.
  Ngoài ra, EMR Promises cũng có thể thay đổi kích thước các Core Node
  của một Cluster đang chạy, giúp tăng cả khả năng xử lý và HDFS.

- Ngoài ra ERM cũng cho phép ta sử dụng các Framework
  như Hadoop và Spark để thực thi các tác vụ trên đó.

- Video: [EMR Promises; Intro to Hadoop](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/14085810#overview)

- Video : [Spark Integration with Kinesis and Redshift](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/14098944#overview)

#### Zeppelin and EMR Notebooks

- Apache Zeppelin khá tương đồng với một Jupyter Notebook,
  cho phép ta tương tác chạy các tập lệnh/mã dựa trên dữ liệu của ta
  và có thể xen kẽ với các ghi chú được định dạng độc đáo.
  Apache Zeppelin hỗ trợ Spark, Python, JDBC, HBase, Elasticsearch,...

- EMR Notebook cũng tương tự như Zeppelin và tích hợp thêm AWS,
  các Notebook này sẽ được lưu trữ ở trên S3 và sẽ chỉ được truy cập vào
  thông qua AWS Console.

- Video: [Zeppelin and EMR Notebooks](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/14105904#overview)

#### S3DistCP and Other Services

- **S3DistCP** là một công cụ giúp sao chép số lượng lớn dữ liệu,
  sử dụng MapReduce để sao chép theo cách phân tán:

  - Từ S3 sang HDFS
  - Từ HDFS sang S3

- Công cụ này thích hợp cho việc sao chép song song số lượng lớn
  các đối tượng trên các region khác nhau, hoặc trên các account khác nhau.

Video: [S3DistCP and Other Services](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/14105928#overview)

#### EMR Security and Instance Types

- Để đảm bảo tính bảo mật cho ERM, ta có thể sử dungh một số phương pháp sau:
  - IAM policies
  - Kerberos
  - SSH
  - IAM roles
  - Block public access
    Video: [EMR Security and Instance Types](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/14105932#overview)

#### Exercises

- Ở hai video sau,
  ta sẽ được hướng dẫn thực hành một số thao tác khi sử dụng ERM.

  - Video: [[Exercise] Elastic MapReduce, Part 1](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/13894191#overview)

  - Video: [[Exercise] Elastic MapReduce, Part 2](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/13894213#overview)

### Document references

- Ta có thể tham khảo thêm các video dưới đây để biết được thêm các cách sử dụng Database trong ERM.

  - Video tham khảo: [Hive on EMR ](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/14098948#overview)
  - Video tham khảo: [Pig on EMR](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/14098956#overview)
  - Video tham khảo: [HBase on EMR](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/14098958#overview)
  - Video tham khảo: [Presto on EMR](https://funix.udemy.com/course/aws-data-analytics/learn/lecture/14098966#overview)

## Assignment 3: Integrate media store on AWS Redshift

### Project name

### Project overview

- Netflix là dịch vụ xem video trực tuyến của rất nổi tiếng hiện nay,
  ở bài Assignment này bạn sẽ được thực hành xây dựng một On-premises Data
  Warehouse dùng để chứa thông tin về các bộ phim đang được chiếu trên Netflix.
  Sau đó, bạn sẽ thực hiện thao tác để di chuyển On-premises Data Warehouse đó
  sang Cloud Data Warehouse (Amazon Redshift).

  - Import Dataset vào SQL Server.
  - Tạo SSIS để làm ETL tải dữ liệu từ Dataset vào Data Warehouse.
  - Chuyển ETL vừa tạo từ SSIS sang dạng T-SQL ETL.
  - Tạo một Redshift Cluster để làm Cloud Data Warehouse.
  - Sử dụng công cụ Amazon SCT để chuyển đổi Schema giữa SQL Server và Redshift.
  - Di chuyển dữ liệu của On-premises Data Warehouse sang Cloud Data Warehouse.
  - Kiểm tra ETL có hoạt động đúng trên Redshift không.
  - (Nâng cao) so sánh hiệu năng giữa On-premises Data Warehouse
    và Cloud Data Warehouse.

### Resources

- Ta cần tải Dataset ở [link sau](https://drive.google.com/drive/folders/1qvFgXWDQE9iZW7bctwA3HJys6O89_qTR?usp=sharing), Dataset này sẽ gồm 2 file như sau:

  - **netflix_titles.csv**: Chứ thông tin về các bộ phim hiện có trên Netflix.
  - **extra_data.csv**: Một số dữ liệu mẫu,
    giúp ta thực hiện yêu cầu số 7 trong đề bài.

- File Dataset sẽ gồm các trường dữ liệu như sau:

  - **show_id** - INT: Id của bộ phim
  - **type** - VARCHAR(255): Thể loại của bộ phim đó
  - **title** - NVARCHAR(255): Tên phim
  - **director** - NVARCHAR(255): Đạo diễn
  - **cast** - NVARCHAR(2000): Danh sách các diễn viên
  - **country** - VARCHAR(255): Nơi sản xuất
  - **date_added** - VARCHAR(255): Thời gian được thêm vào trên Netflix.
  - **release_year** - VARCHAR(255): Năm công chiếu
  - **rating** - VARCHAR(255): Rating của khán giả
  - **duration** - VARCHAR(255): Thời lượng
  - **listed_in** - NVARCHAR(255): Danh mục
  - **description** - NVARCHAR(1000): Mô tả về phim

- Một số tài liệu khác:

  - [Cài đặt DataGrip](https://www.jetbrains.com/help/datagrip/installation-guide.html)
  - [Sử dụng Educational Licenses cho các ứng dụng của Jetbrain](https://www.jetbrains.com/community/education/#students)
  - [Tạo Database Connection trong DataGrip](https://www.jetbrains.com/help/datagrip/connecting-to-a-database.html)
  - [Kết nối với Redshift](https://www.jetbrains.com/help/datagrip/amazon-redshift.html)
  - [Import dữ liệu từ file CSV vào SQL Server](https://qawithexperts.com/article/sql/import-csv-into-sql-server-with-query-or-without-query-using/265)
  - [Load Employee Dim using Stored Proc](https://www.youtube.com/watch?v=teAIA_Ko9AE&t=588s)
  - [Load Fact table using Stored Proc](https://www.youtube.com/watch?v=JA-lwCjmWhI)
  - [Hướng dẫn sử dụng SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.html)
  - [Import csv vào redshift](https://hevodata.com/learn/load-csv-to-redshift-3-easy-methods/)

### Expections

- [Course](https://courses.funix.edu.vn/courses/course-v1:FUNiX+DEP304x_01-A_VN+2021_T11/courseware/59e917fb412843f393d35345325ff1ea/272002c20cb849e8a551b6766bc0a24a/?child=first)

## References
