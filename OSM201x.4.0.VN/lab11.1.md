# Lab 11.1: Tính toán thời gian phân bổ TLB

[Link](https://docs.google.com/document/d/1SR_UstR57MiSFmEoeIAqmllwi4iPGkpF2y2maho9MVM/edit)

Trong bài này chúng ta sẽ vận dụng nội dung của những bài học vừa rồi để có thể tính thời gian phân bổ và thời gian trung bình tương ứng.

**Bài 1:** Xem xét phân trang phần cứng cùng với TLB. Giả sử rằng toàn bộ bảng trang (page table) và tất cả các trang đều nằm trong bộ nhớ vật lý. Nó mất 10 mili giây để tìm kiếm TLB và mất 80 mili giây để truy cập bộ nhớ vật lý.
Nếu tỉ lệ truy cập TLB là 0.6, thì thời gian truy cập bộ nhớ hiệu quả (tính bằng mili giây) là bằng bao nhiêu ?

**Gợi ý bài làm:**

**Từ dữ liệu đề bài, ta có sẽ có công thức tính toán _Thời gian truy cập bộ nhớ hiệu quả_ là:**

$$EAT=h_{access}(T+M)+h_{miss}(T+2M)$$

Trong đó:

> - $h_{access}$ : Tỷ lệ truy cập TLB
> - $T$: thời gian truy cập vào TLB
> - $M$: thời gian truy cập bộ nhớ chính.
> - $h_{miss}$ : Tỷ lệ bỏ lỡ TLB

**Bài giải**

> $EAT=0.6(10+80)+0.4(10+80\times 2)=54+68=122$

**Bài 2:** Hãy xem xét một hệ thống phân trang sử dụng bảng trang 1 cấp cấp nằm trong bộ nhớ chính và một TLB để dịch địa chỉ. Mỗi lần truy cập bộ nhớ chính mất 100ms và tra cứu TLB mất 20ms. Mỗi lần chuyển trang đến/từ đĩa mất 5000ms.
Giả sử tỷ lệ truy cập TLB là 95%, tỷ lệ lỗi trang là 10%. Giả sử rằng đối với 20% tổng số lỗi trang, một trang bảng phải được ghi lại vào đĩa trước khi trang được yêu cầu được đọc từ đĩa. Thời gian truy cập TLB không đáng kể.
Tính thời gian truy cập bộ nhớ trung bình (tính bằng ms).

**Gợi ý bài làm:**

**_Thời gian truy cập bộ nhớ trung bình_** =

$h\times (T + M) + (1-h) \{(1-p)\times 2M + p[(1-d)[D+M) + d(2D + M)] + T\}$

**Trong đó:**

> - $M$ là thời gian truy cập bộ nhớ chính.
> - $T$ là thời gian tra cứu TLB.
> - $D$ là thời gian khi mỗi lần chuyển trang đến/từ đĩa.
> - $h$ là tỷ lệ truy cập TLB
> - $p$ là tỷ lệ lỗi trang
> - $(1-p)$ là tỷ lệ truy cập trang bình thường.
> - $d$ là tổng số lỗi trang.
> - $(1-d)$ là tổng số trang bình thường.

**Bài giải**

Áp dụng vào công thức, ta có:

> $ EMAT=95\%(20 + 100) + 5\%\{(1-10\%)\times 2\times 100 + 10\%[(1 - 20\%)(5000 + 100) + 20\%(2\times 5000 + 100)] + 100\}\\
> =95\%\times 120 + 5\%[90\%\times 200 + 10\%(80\%\times 5100 + 20\%\times 10100) + 100]\\
> =114 + 5\%[180 + 10\%(4080 + 2020) + 100]\\
> =114 + 5\%[180 + 610 + 100]\\
> =114 + 5\%\times 890 \\
> =114 + 44.5\\
> =158.5 $

Các bài lab bạn sẽ thực hành và lưu lại công thức. Sẽ được vận dụng và làm trực tiếp trong những bài quiz hoặc những bài assignment.
