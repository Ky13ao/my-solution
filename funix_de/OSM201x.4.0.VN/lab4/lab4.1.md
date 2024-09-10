# Lab 4.1: Tính thời gian trung bình của thuật toán lập lịch

[Link](https://docs.google.com/document/d/1hv8cotfYtDJ36zFqc4fLnKPHH4IczHyWCFvZdlti0ZA/edit)

Trong bài lab sẽ cung cấp cho bạn ví dụ về tính toán thời gian trung bình của thuật toán lập lịch như trong bài giảng đã mô tả.

Bài toán đưa ra cho hệ thống có 5 tiến trình. Thông tin sẽ như sau:

| id  | Arrival Time | Execution Time |
| :-- | -----------: | -------------: |
| T1  |            0 |             12 |
| T2  |            2 |              7 |
| T3  |            5 |              8 |
| T4  |            9 |              3 |
| T5  |           12 |              6 |

Tính toán thông lượng (throughput), thời gian quay vòng trung bình (average turnaround time) và thời gian chờ trung bình (average waiting time) của cả 5 tiến trình bằng cách sử dụng các thuật toán sau:

- FCFS
- Non-preemptive SJF
- Preemption-based SJF

**_Gợi ý:_**

> Tại thời điểm 0s, tiến trình T1 bước vào, đợi 0s, hoàn thành ở giây thứ 12 => thời gian đợi là 0, thời gian quay vòng là 12-0=12.
> Tại thời điểm 2s, tiến trình T2 bước vào, tuy nhiên, lúc này T1 đang chạy nên phải đợi 15s để T1 hoàn thành, đến giây thứ 12, T1 chạy xong, T2 bắt đầu chạy, hoàn thành ở giây thứ 19 => thời gian quay vòng là 19-2 = 17, thời gian đợi là 12-2=10.
> Tại thời điểm 5s, tiến trình T3 bước vào, tuy nhiên phải đợi T2 kết thúc thì mới chạy được, mà T2 kết thúc ở giây thứ 19 => thời gian đợi là 19-5=14s. Sau giây thứ 19, T3 chạy hết 8s, nên kết thúc ở giây thứ 27 => thời gian quay vòng là 27-5=22s.
> Tương tự với T4 và T5
>
> - Throughput = 5 / (12 + 7 + 8 + 3 + 6) = 0.14 (task/s)
> - Average waiting time = (0 + 10 + 14 + 18 + 18) / 5 = 12s
> - Average turnaround time = (12 + 17 + 22 + 21 + 24) / 5 = 19.2s
>
> - Throughput = 5 / (12 + 7 + 8 + 3 + 6) = 0.14 (task/s)
> - Average waiting time = (0 + 19 + 23 + 3 + 3) / 5 = 9.6s
> - Average turnaround time = (12 + 26 + 31 + 6 + 9) / 5 = 16.8s
>
> - Throughput = 5 / (12 + 7 + 8 + 3 + 6) = 0.14 (task/s)
> - Average waiting time = (24 + 0 + 13 + 0 + 0) / 5 = 7.4s
> - Average turnaround time = (36 + 7 + 21 + 3 + 6) / 5 = 14.6s

## **_Bài giải_**

#### First-Come, First-Served (FCFS):

Áp dụng thuật toán FCFS, tiến trình sẽ được thực thi theo thứ tự đến trước thực thi trước. Dưới đây là bảng biểu diễn quá trình thực thi của từng tiến trình:

| id  | Arrival Time | Execution Time | Completion Time | Turnaround Time | Waiting Time |
| :-- | -----------: | -------------: | --------------: | --------------: | -----------: |
| T1  |            0 |             12 |              12 |              12 |            0 |
| T2  |            2 |              7 |              19 |              17 |           10 |
| T3  |            5 |              8 |              27 |              22 |           14 |
| T4  |            9 |              3 |              30 |              21 |           18 |
| T5  |           12 |              6 |              36 |              24 |           18 |

- Thông lượng (Throughput) = Số lượng tiến trình /Tổng thời gian thực thi = 5 / 36 ≈ 0.14 (task/s)
- Thời gian quay vòng trung bình (Average Turnaround Time) = (12 + 17 + 22 + 21 + 24) / 5 = 19.2s
- Thời gian chờ trung bình (Average Waiting Time) = (0 + 10 + 14 + 18 + 18) / 5 = 12s

#### Non-preemptive SJF:

Áp dụng thuật toán Non-preemptive SJF, tiến trình có thời gian thực thi ngắn nhất sẽ được thực thi trước.
Tiến trình được thực hiện theo thứ tự sau:

| id  | Arrival Time | Execution Time | Completion Time | Turnaround Time | Waiting Time |
| :-- | -----------: | -------------: | --------------: | --------------: | -----------: |
| T1  |            0 |             12 |              12 |              12 |            0 |
| T4  |            9 |              3 |              15 |               6 |            3 |
| T5  |           12 |              6 |              21 |               9 |            3 |
| T2  |            2 |              7 |              28 |              26 |           19 |
| T3  |            5 |              8 |              36 |              31 |           23 |

GANTT CHART:

> ```r
> |           T1          | T4  |     T5    |      T2     |      T3       |
> |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
> 0                      12    15          21            28              36
> ```

Tính toán thông lượng (throughput), thời gian quay vòng trung bình (average turnaround time) và thời gian chờ trung bình (average waiting time) của các tiến trình:

Thông lượng (Throughput): Số tiến trình hoàn thành trong một đơn vị thời gian / Tổng thời gian thực thi của tất cả các tiến trình
Throughput = 5 / 36 = 0.1389 (approx.)

Thời gian quay vòng trung bình (Average Turnaround Time): Tổng thời gian quay vòng của tất cả các tiến trình / Số tiến trình
Average Turnaround Time = (12 + 6 + 9 + 26 + 31) / 5 = 16.8

Thời gian chờ trung bình (Average Waiting Time): Tổng thời gian chờ của tất cả các tiến trình / Số tiến trình
Average Waiting Time = (0 + 3 + 3 + 19 + 23) / 5 = 9.6

#### Preemption-based SJF:

Áp dụng thuật toán Preemption-based SJF, tiến trình có thời gian thực thi ngắn nhất sẽ được thực thi trước, và nếu có tiến trình mới có thời gian thực thi ngắn hơn xuất hiện, tiến trình đang chạy sẽ bị gián đoạn và tiến trình mới sẽ được thực thi. Dưới đây là bảng biểu diễn quá trình thực thi của từng tiến trình:

| id  | Arrival Time | Execution Time | Completion Time | Turnaround Time | Waiting Time |
| :-- | -----------: | -------------: | --------------: | --------------: | -----------: |
| T1  |            0 |             12 |              36 |              36 |           24 |
| T2  |            2 |              7 |               9 |               7 |            0 |
| T3  |            5 |              8 |              26 |              21 |           13 |
| T4  |            9 |              3 |              12 |               3 |            0 |
| T5  |           12 |              6 |              18 |               6 |            0 |

GANTT CHART:

```
|T1 |      T2     | T4  |     T5    |       T3      |         T1        |
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
0   2             9    12          18              26                  36
```

1. Bắt đầu ở thời điểm 0s, T1 được thực thi
2. Thời điểm 2s, T2 được thực thi ưu tiên (do tiến trình ngắn hơn tiến trình T1 ) trong vòng 7s, hoàn thành ở giây thứ 9 => thời gian đợi là 0, thời gian quay vòng là 9-2=7
3. Thời điểm 5s, T3 được gọi nhưng thời gian thực thi lớn hơn thời gian của T2, nên đợi đến giây thứ 9
4. Thời điểm 9s, T4 được gọi sau khi T2 hoàn thành, thời gian thực thi T4 < T3 nên T4 được thực thi trong 3 giây, hoàn thành ở giây 12, thời gian quay quay vòng là 12-9=3, thời gian đợi là 9-9=0
5. Thời điểm 12s, T5 được gọi sau khi T4 hoàn thành, thời gian thực T4 < T3 nên T5 được thực thi trong 6 giây, hoàn thành ở giấy thứ 18, thời gian quay vòng là 18-12=6, thời gian đợi là 12-12=0
6. Thời điểm 18s, T3 được thực thi do T1 vẫn lớn hơn T3, hoàn thành ở giây thứ 24, thời gian quay vòng 24-5=19, thời gian đợi 18-5=13
7. Thời điểm 24s, T1 được tiếp tục thực thi 10 giây còn lại, hoàn thành ở giây thứ 34, thời gian quay vòng là 34-0=34, thời gian chờ là 24-2=22

- Thông lượng (Throughput) = Số lượng tiến trình /Tổng thời gian thực thi = 5 / 36 ≈ 0.14 (task/s)
- Thời gian quay vòng trung bình (Average Turnaround Time) = (36 + 7 + 21 + 3 + 6) / 5 = 14.6s
- Thời gian chờ trung bình (Average Waiting Time) = (24 + 0 + 13 + 0 + 0) / 5 = 7.4s
