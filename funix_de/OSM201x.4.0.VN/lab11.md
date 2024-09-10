## 1. Bộ nhớ đệm bên cạnh translation (TLB)

**TLB (Translation look aside buffer)** được định nghĩa như một bộ nhớ đệm có thể được sử dụng để giảm thời gian truy cập lại bảng trang. Ngoài ra nó còn được sử dụng để giảm thời gian truy cập lại bảng trang. Đây là bộ nhớ đệm gần CPU hơn và thời gian CPU truy cập vào TLB sẽ ít hơn so với thời gian cần để truy cập bộ nhớ chính. Nói cách khác, chúng ta có thể nói rằng TLB nhanh hơn và nhỏ hơn bộ nhớ chính nhưng rẻ hơn và lớn hơn thanh ghi (register).

TLB tuân theo khái niệm tham chiếu có nghĩa là nó chỉ chứa các mục nhập của nhiều trang được CPU truy cập thường xuyên.

Muốn tính được tỷ lệ truy cập TLB thì ta phải tính được tỷ lệ bỏ lỡ (miss).

Ta có công thức:
$$ Tỷ\ lệ\ truy\ cập\ TLB = 1 - Tỷ\ lệ\ bỏ\ lỡ \; ( unit: \% ) $$

**Thời gian truy cập TLB** sẽ nằm trong công thức tính toán của EMAT tương ứng.

Thông qua biến t đại diện đại lương, hoàn toàn tính toán ra những thông số và kết quả của đề bài tương ứng.

$EMAT = TLBHit + TLBMiss$

$TLBHit = h(t+m)$

- $h:Hit\ Ratio$
- $t:TLB\ Access$
- $m:Memory\ Access$

$TLBMiss(1-h)(t+m_{table}+m_{byte})$

- $1-h:Miss\ Ratio$
- $t:TLB\ access\ and\ miss$
- $m_{table}:Memory\ Access\ for\ table$
- $m_{byte}:Memory\ Access\ for\ byte\ (page)$

**Thời gian truy cập RAM** sẽ được tính theo công thức của EMAT là:

$EMAT = (LA \to PA) + Accessing\ the\ byte$ (Truy cập byte tương ứng)

Đại lượng $(LA \to PA)$ ta sẽ biểu diễn ra công thức tương ứng.
