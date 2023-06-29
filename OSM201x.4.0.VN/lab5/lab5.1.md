# Lab 5.1: Tương tác về quyền với thư mục và tệp tin trong Linux phần 1

Trong những bài học trước, chúng ta đã được thực hành và làm việc với thư mục và tệp tin trong Linux. Bài học cũng phần nào nhắc đến việc phân quyền trong tập tin. Vậy vì sao cần phải phân quyền? Thực sự có những nhóm phân quyền nào? Trong bài lab này, chúng ta sẽ đi tìm hiểu những vấn đề đấy.

## 1. Tại sao cần có phân quyền?

Ngày nay, hầu hết các hệ điều hành phổ biến đều hỗ trợ nhiều người dùng sử dụng đồng thời. Mục đích của hệ điều hành sinh ra sẽ giúp có càng nhiều người sử dụng càng tốt. (người dùng A sẽ vào với quyền A, người dùng B sẽ vào với quyền B,..). Do vậy có thể một người nào đó không cần hệ điều hành phải hỗ trợ nhiều người sử dụng nhưng những người khác lại cần đến. Tính năng phân quyền được tạo ra là để hỗ trợ cho việc sử dụng đồng thời của hệ điều hành.

## 2. Các nhóm phân quyền:

Trong Linux có 3 nhóm phân quyền chính, không bao nhau:

- Owner: chỉ cấp quyền cho chủ sở hữu của file.
- Group: chỉ cấp quyền cho nhóm sở hữu của file.
- Other: cấp quyền cho những người dùng và nhóm không thuộc 2 nhóm trên.
  Tuy nhiên, trong bài học còn nhắc tới một người dùng đặc biệt, đó là root. Người dùng này có mọi quyền hạn trên mọi file trong hệ thống, không bị ràng buộc bởi bất cứ sự phân quyền nào.
  Do vậy với bất cứ một tác vụ gì phải dùng tới quyền hạn của người dùng root thì ta nên chắc chắn sẽ không gây hại cho hệ thống thì mới nên sử dụng, hoặc tìm một phương án thay thế mà không cần tới quyền hạn nguy hiểm này.

## 3. Các loại phân quyền:

Với một tệp tin, có 3 loại phân quyền cơ bản ở trong bảng bên dưới:

| Tên quyền | Ký hiệu | Dạng số | Mô tả               |
| --------- | ------- | ------- | ------------------- |
| Read      | r       | 4       | Quyền đọc file      |
| Write     | w       | 2       | Quyền ghi file      |
| Execute   | e       | 1       | Quyền thực thi file |

### Ngoài ra, có một vài phân quyền đặc biệt như sau:

| Tên quyền      | Ký hiệu | Dạng số | Mô tả                                                                                         |
| -------------- | ------- | ------- | --------------------------------------------------------------------------------------------- |
| Setuid/ Setgid | s       | 1       | Nếu file được thực thi, người thực thi sẽ là chủ sở hữu.                                      |
| Sticky bit     | t       | 1       | Chỉ chủ sở hữu mới được xóa hoặc thay đổi tên file kể cả khi Other có toàn quyền với file đó. |

## 4. Cách xem phân quyền của một file:

Tất cả phần trên chỉ là lý thuyết, giờ đây sẽ là ví dụ thực tế giúp cho bạn hiểu rõ các quyền thực sự của tập tin. Để xem được phân quyền của một file thì câu lệnh bạn sử dụng sẽ là ls -l .
Kết quả của câu lệnh trên ví dụ sẽ có dạng như sau:
**-rwxr-x-r-x**

Ký tự - đầu tiên là một cờ (flag) đặc biệt để chỉ loại file.

- 3 ký tự rwx đầu tiên là quyền hạn của Owner, ở đây Owner sẽ có mọi quyền với file.
- 3 ký tự r-x ở giữa là quyền hạn của Group, ở đây Group sẽ có quyền đọc và quyền dùng lệnh cd.
- 3 ký tự r-x cuối cùng là quyền hạn của Other, tương tự như Group ở trên sẽ có quyền đọc và dùng lệnh cd.

Bạn hãy thực hành với câu lệnh ls -l để hiển thị ra thông tin chi tiết của tệp tin, để có thể phân tích chi tiết các quyền hạn của các tệp tin trong Linux của bạn.

Hiện tại, bạn đã tìm hiểu cơ bản về quyền với thư mục và tệp tin trong Linux. Ngoài ra, học viên hãy tham khảo video bài giảng bên dưới để có thể hiểu rõ về kiến thức cũng như chi tiết phần thực hành tương ứng.

[Tương tác về quyền với thư mục và tệp tin trong Linux phần 1](https://funix.udemy.com/course/learn-linux-in-5-days/learn/lecture/1417738#overview)
