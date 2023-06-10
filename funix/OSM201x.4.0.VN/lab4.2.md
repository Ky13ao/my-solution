Lab 4.2: Bài toán sử dụng thuật toán lập lịch FCFS

[Link](https://docs.google.com/document/d/1V4INvIvoTZ6EAg84xXYmWjO8y6Eh8WSb37cHmQp15Z8/edit)
Trong bài lab này, chúng ta sẽ vận dụng kiến thức của lập lịch FCFS để giải quyết bài toán và hiển thị được kết quả tương ứng.

Viết chương trình mô phỏng thuật toán lập lịch FCFS.
Đầu vào của bài toán là phải nhập từ bàn phím, bao gồm số lượng của tiến trình, số thứ tự của từng quy trình và thời gian sử dụng CPU của từng quy trình.
Đầu ra thì có định dạng như sau:

| PName | Arrival Time | Burtime | Start | TAT | Finish |
| ----- | ------------ | ------- | ----- | --- | ------ |
| 0     | 0            | 24      | 0     | 24  | 24     |
| 1     | 1            | 3       | 24    | 26  | 27     |
| ..    | …            | …       | …     | …   | …      |
| n     | n            | n       | n     | n   | n      |

Average waiting time: 16.00
Average turnaround time: 26.00

Kết quả đầu ra 1 tương ứng:

```shell
Enter the number of processes: 3
Enter the Process Name, Arrival Time & Burst Time of Process 0: 0 0 24
Enter the Process Name, Arrival Time & Burst Time of Process 1: 1 1 3
Enter the Process Name, Arrival Time & Burst Time of Process 2: 2 2 3

PName   Arrtime Burtime Start   TAT   Finish
0       0       24      0       24    24
1       1       3       24      26    27
2       2       3       27      28    30
```

Kết quả đầu ra 2 tương ứng:

```shell
Enter the number of processes: 5
Enter the Process Name, Arrival Time & Burst Time of Process 0: 0 0 12
Enter the Process Name, Arrival Time & Burst Time of Process 1: 1 2 7
Enter the Process Name, Arrival Time & Burst Time of Process 2: 2 5 8
Enter the Process Name, Arrival Time & Burst Time of Process 3: 3 9 3
Enter the Process Name, Arrival Time & Burst Time of Process 4: 4 12 6

PName   Arrtime Burtime Start  TAT   Finish
    0         0      12     0   12       12
    1         2       7    12   17       19
    2         5       8    19   22       27
    3         9       3    27   21       30
    4        12       6    30   24       36
```

Học viên có thể sử dụng ngôn ngữ python để làm bài tập này.
Đầu tiên dùng 1 vòng for để cho phép người dùng nhập vào các tham số: process name, arrival time, burst time
Vì là thuật toán FCFS, nên tuần tự các process sẽ diễn ra theo arrival time (nghĩa là trong trường hợp người dùng nhập process 1 có arrival time=3 và process 2 có arrival time=1 thì process 2 sẽ chạy trước), cho nên cần sắp xếp lại các process theo arrival time.
Dùng vòng for để tính thời gian hoàn thành của từng tiến trình.
Dùng vòng for khác để tính TAT.
Hiển thị kết quả ra màn hình
Học viên có thể tham khảo lời giải để hoàn thành bài tập: https://drive.google.com/file/d/1cpc2N3tIhQq5Z44wMaJ7mMrW9FrtRk68/view?usp=share_link
