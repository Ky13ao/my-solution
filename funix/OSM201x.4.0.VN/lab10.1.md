# Lab 10.1: Tính toán thời gian trung bình để truy cập bộ nhớ

[Link](https://docs.google.com/document/d/13aIRZVoG1i-hL01LhrLAK537p-fC8ABq2tF6VXUcMQw/edit)
Trong bài lab này, chúng ta sẽ được thực hành với bài toán để tính toán thời gian trung bình để truy cập bộ nhớ.

## Tính toán thời gian truy cập bộ nhớ trung bình:

### 1. Nếu nó bị ‘tấn công’ thì CPU sẽ truy cập nội dung từ chính bộ nhớ đệm và nếu nó bị lỗi thì do đó bộ nhớ chính vẫn sẽ hoạt động.

Do đó, thời gian truy cập bộ nhớ trung bình trong trường hợp truy cập đồng thời sẽ là:

- Thời gian truy cập bộ nhớ trung bình = Tỷ lệ truy cập $\times$ Thời gian truy cập bộ nhớ đệm + ( 1- Tỷ lệ truy cập ) $\times$ Thời gian truy cập bộ nhớ chính.

### 2. Nếu giả sử vị trí của tham chiếu có trong đề bài, thì ta sẽ sử dụng công thức sau để xác định thời gian truy cập bộ nhớ trung bình:

- Thời gian truy cập bộ nhớ trung bình = Tỷ lệ truy cập $\times$ Thời gian truy cập bộ nhớ đệm + ( 1 - Tỷ lệ truy cập ) $\times$ Thời gian cần thiết để truy cập một khối bộ nhớ chính.
  Trong đó, thời gian cần thiết để truy cập khối bộ nhớ chính = kích thước khối $\times$ thời gian cần thiết để truy cập bộ nhớ chính.

### 3. Nếu giả sử thời gian truyền khối có trong đề bài, thì ta sẽ sử dụng công thức sau để xác định thời gian truy cập bộ nhớ trung bình:

- Thời gian truy cập bộ nhớ trung bình = Tỷ lệ truy cập $\times$ Thời gian truy cập bộ nhớ đệm + ( 1 - Tỷ lệ truy cập ) $\times$ (Thời gian truy cập bộ nhớ đệm + Thời gian cần thiết để truy cập một khối bộ nhớ chính).
  Trong đó, thời gian cần thiết để truy cập khối bộ nhớ chính = kích thước khối $\times$ thời gian cần thiết để truy cập bộ nhớ chính.

**Yêu cầu thực hành:**

> Trong một hệ thống phân cấp (2 cấp), cấp cao nhất có thời gian truy cập là 10ms, cấp dưới cùng có thời gian truy cập là 50ms, tỷ lệ truy cập ở cấp cao nhất là 90%.
> Nếu kích thước khối của bộ nhớ cache là 16 byte, thì thời gian truy cập bộ nhớ trung bình cần thiết là bao nhiêu?

**Hướng dẫn làm bài:**

> Đề bài đã cho thời gian truy cập bộ nhớ cache (mức cao nhất) = 10ms
> Vì hệ thống có 2 cấp, nên Thời gian truy cập bộ nhớ chính (mức dưới cùng) = thời gian truy cập cấp cao nhất + thời gian truy cập cấp dưới cùng = 50+10 = 60ms.
>
> => Sử dụng công thức số (2).

**Thời gian truy cập bộ nhớ trung bình** = 10 $\times$ 0.9 + ( 1 - 0.9 ) $\times$ (16 $\times$ 50 + 10) = 90ms.

**Bạn hãy ghi nhớ những công thức trên, nó sẽ được vận dụng trong bài quiz và assignment.**

$$ \overline{MemoryAccessTime} = TLBAccess+\frac{95}{100}\times L1_{HitTime}+\frac{5}{100}\times L1_{MissPenalty} $$
$$ TLBAccess = TLB_{HitTime}\times\frac{95}{100}+(TLB_{HitTime}+TLB_{MissPenalty})\times\frac{5}{100} $$
$$ L1_{MissPenalty}=\frac{80}{100}\times L2_{HitTime}+\frac{20}{100}\times L2_{MissPenalty} $$
$$ L2_{MissPenalty}=\frac{50}{100}\times L3_{HitTime}+\frac{50}{100}\times L3_{MissPenalty} $$

$$
L3_{MissPenalty}=Memory_{HitTime}
$$
