# ĐỀ KIỂM TRA FINAL PYTHON - TỔNG HỢP TOÀN BỘ KIẾN THỨC

**Thời gian làm bài:** 90 phút  
**Tổng điểm:** 120 điểm  
**Hình thức:** Làm bài trên máy tính hoặc viết code Python

---

## HƯỚNG DẪN CHUNG

1. Đọc kỹ đề trước khi làm bài
2. Phân bổ thời gian hợp lý: Lý thuyết (20 phút) - Thực hành (60 phút) - Nâng cao (10 phút)
3. Làm bài theo thứ tự, có thể bỏ qua câu khó để làm câu khác
4. Chương trình phải chạy được, có nhập xuất đầy đủ
5. Code phải rõ ràng, có comment khi cần thiết
6. Điểm chi tiết cho từng phần được ghi trong từng câu

---

## PHẦN I: LÝ THUYẾT TỔNG HỢP (30 điểm)

### Câu 1 (6 điểm): Phân tích Code

Cho các đoạn code sau, hãy xác định kết quả và giải thích:

```python
# a)
def func(x=10, *args, **kwargs):
    return x + sum(args) + sum(kwargs.values())

result = func(5, 1, 2, 3, a=10, b=20)
print(result)

# b)
a = [1, 2, 3, 4, 5]
b = a[:]
b[0] = 100
print(a[0], b[0])

# c)
s = "Python Programming"
words = s.split()
result = "-".join([w.lower() for w in words if len(w) > 5])
print(result)

# d)
data = {"a": 1, "b": 2, "c": 3}
new_data = {k: v**2 for k, v in data.items() if v % 2 == 1}
print(new_data)

# e)
x = 10
def test():
    global x
    x = 20
    def inner():
        nonlocal x
        x = 30
    inner()
    print(x)
test()
print(x)

# f)
lst = [3, 1, 4, 1, 5, 9]
lst.sort(key=lambda x: -x if x % 2 == 0 else x)
print(lst)
```

**Yêu cầu:** Viết kết quả và giải thích ngắn gọn cho mỗi phần (a-f).

---

### Câu 2 (6 điểm): So sánh và Giải thích

Hãy so sánh và giải thích sự khác biệt giữa các cặp sau:

1. **List, Tuple, Set, Dictionary:** Nêu đặc điểm, cách khai báo, và trường hợp sử dụng của mỗi loại. (3 điểm)

2. **`sort()` và `sorted()`:** Giải thích sự khác biệt về cách sử dụng và kết quả trả về. (1.5 điểm)

3. **`global` và `nonlocal`:** Giải thích mục đích và cách sử dụng của mỗi từ khóa. (1.5 điểm)

---

### Câu 3 (6 điểm): Hàm và Lambda

1. Giải thích sự khác biệt giữa hàm thông thường và lambda function. Khi nào nên dùng lambda? (2 điểm)

2. Cho ví dụ sử dụng `map()` và `filter()` với lambda để xử lý list. (2 điểm)

3. Giải thích khái niệm nested function (hàm lồng nhau) và cho ví dụ minh họa. (2 điểm)

---

### Câu 4 (6 điểm): Đệ quy và Thuật toán

1. Giải thích khái niệm đệ quy (recursion). Một hàm đệ quy cần có những thành phần gì? (2 điểm)

2. Nêu ý tưởng của thuật toán Binary Search. Khi nào có thể sử dụng Binary Search? (2 điểm)

3. So sánh Linear Search và Binary Search về độ phức tạp và trường hợp sử dụng. (2 điểm)

---

### Câu 5 (6 điểm): String và Collections

1. Nêu 3 cách format string trong Python và cho ví dụ minh họa. (2 điểm)

2. Giải thích sự khác biệt giữa `list.append()`, `list.extend()`, và `list.insert()`. (2 điểm)

3. Trong Dictionary, giải thích sự khác biệt giữa `dict.pop(key)` và `dict.get(key)`. (2 điểm)

---

## PHẦN II: BÀI TẬP THỰC HÀNH (70 điểm)

### Câu 6 (15 điểm): Xử lý Dữ liệu Phức tạp

Viết chương trình quản lý danh sách sản phẩm với các yêu cầu sau:

**Yêu cầu:**
1. Tạo một list chứa ít nhất 5 dictionary, mỗi dictionary có các key: `"ten"`, `"gia"`, `"loai"`, `"so_luong"`
2. Nhập thông tin sản phẩm từ bàn phím (hoặc khởi tạo sẵn trong code)
3. Thực hiện các thao tác:
   - Tìm sản phẩm có giá cao nhất và thấp nhất
   - Tính tổng giá trị tất cả sản phẩm (giá × số lượng)
   - Lọc và in ra các sản phẩm có số lượng < 10
   - Sắp xếp danh sách theo giá giảm dần (nếu cùng giá thì sắp xếp theo tên)
4. Tạo một dictionary mới với key là `"loai"` và value là list các sản phẩm thuộc loại đó

**Ví dụ:**
```
Danh sách sản phẩm:
- Sản phẩm đắt nhất: {'ten': 'Laptop', 'gia': 15000000, ...}
- Sản phẩm rẻ nhất: {'ten': 'Bút', 'gia': 5000, ...}
- Tổng giá trị: 25000000
- Sản phẩm sắp hết: [{'ten': 'Sách', 'so_luong': 5}, ...]
```

---

### Câu 7 (15 điểm): Xử lý Chuỗi và Text

Viết chương trình phân tích văn bản với các yêu cầu:

**Yêu cầu:**
1. Nhập một đoạn văn bản từ bàn phím (có thể nhiều dòng, kết thúc bằng dòng trống)
2. Thực hiện:
   - Đếm tổng số từ, số câu (kết thúc bằng dấu `.`, `!`, `?`)
   - Đếm số từ có độ dài > 5 ký tự
   - Tìm từ xuất hiện nhiều nhất (không phân biệt hoa thường)
   - Loại bỏ các từ trùng lặp và in ra danh sách từ duy nhất
   - Đảo ngược thứ tự các từ trong câu đầu tiên
3. Sử dụng dictionary để đếm tần suất từ

**Ví dụ:**
```
Nhập văn bản: Python là ngôn ngữ lập trình. Python rất dễ học. Học Python thật vui.

Số từ: 11
Số câu: 3
Từ dài (>5): ['ngôn ngữ', 'lập trình']
Từ xuất hiện nhiều nhất: python (3 lần)
Danh sách từ duy nhất: ['python', 'là', 'ngôn', 'ngữ', ...]
Câu đầu đảo ngược: lập trình ngôn ngữ là Python
```

---

### Câu 8 (15 điểm): Hàm Đệ quy

Viết các hàm đệ quy để giải quyết các bài toán sau:

1. **Hàm `tinh_giai_thua(n)`:**
   - Tính giai thừa của số n (n! = n × (n-1) × ... × 1)
   - Điều kiện dừng: n = 0 hoặc n = 1

2. **Hàm `tinh_tong_list(arr)`:**
   - Tính tổng tất cả phần tử trong list sử dụng đệ quy
   - Điều kiện dừng: list rỗng

3. **Hàm `dao_nguoc_chuoi(s)`:**
   - Đảo ngược chuỗi sử dụng đệ quy
   - Điều kiện dừng: chuỗi có ≤ 1 ký tự

4. **Chương trình chính:**
   - Nhập giá trị n, list số, và chuỗi
   - Gọi các hàm trên và in kết quả

**Ví dụ:**
```
Nhập n: 5
5! = 120

Nhập list (cách nhau dấu cách): 1 2 3 4 5
Tổng: 15

Nhập chuỗi: Python
Chuỗi đảo ngược: nohtyP
```

---

### Câu 9 (15 điểm): Thuật toán Tìm kiếm và Sắp xếp

Viết chương trình thực hiện:

1. **Tạo list số nguyên:**
   - Nhập n số nguyên từ bàn phím (mỗi số cách nhau dấu cách)
   - Sắp xếp list theo thứ tự tăng dần

2. **Triển khai Binary Search:**
   - Viết hàm `binary_search(arr, x)` tìm số x trong list đã sắp xếp
   - Trả về vị trí (index) nếu tìm thấy, -1 nếu không tìm thấy

3. **Triển khai Linear Search:**
   - Viết hàm `linear_search(arr, x)` tìm số x trong list
   - Trả về vị trí đầu tiên tìm thấy, -1 nếu không tìm thấy

4. **So sánh hiệu quả:**
   - Nhập số cần tìm
   - Sử dụng cả 2 phương pháp và đếm số lần so sánh của mỗi phương pháp

**Ví dụ:**
```
Nhập các số: 5 2 8 1 9 3
List sau khi sắp xếp: [1, 2, 3, 5, 8, 9]

Nhập số cần tìm: 5
Binary Search: Tìm thấy tại vị trí 3 (số lần so sánh: 2)
Linear Search: Tìm thấy tại vị trí 3 (số lần so sánh: 4)
```

---

### Câu 10 (10 điểm): Lambda và Higher-order Functions

Sử dụng lambda, map, filter để xử lý dữ liệu:

1. **Cho list điểm số:** `[8.5, 7.0, 9.5, 6.5, 8.0, 7.5, 9.0]`

2. **Yêu cầu:**
   - Sử dụng `map()` và lambda để tính điểm sau khi làm tròn (làm tròn lên)
   - Sử dụng `filter()` và lambda để lọc các điểm >= 8.0
   - Tính điểm trung bình của các điểm >= 8.0
   - Tìm điểm cao nhất và thấp nhất sử dụng `max()` và `min()` với lambda

3. **Cho list tên:** `["Nguyễn Văn A", "Trần Thị B", "Lê Văn C"]`
   - Sử dụng `map()` và lambda để tạo list chứa chữ cái đầu của mỗi tên

**Ví dụ:**
```
Điểm gốc: [8.5, 7.0, 9.5, 6.5, 8.0, 7.5, 9.0]
Điểm làm tròn: [9, 7, 10, 7, 8, 8, 9]
Điểm >= 8.0: [8.5, 9.5, 8.0, 9.0]
Điểm trung bình (>=8.0): 8.75
Điểm cao nhất: 9.5, Điểm thấp nhất: 6.5

Chữ cái đầu: ['N', 'T', 'L']
```

---

## PHẦN III: BÀI TẬP NÂNG CAO (20 điểm)

### Câu 11 (10 điểm): Quản lý Học sinh với Dictionary Nested

Viết chương trình quản lý lớp học với cấu trúc dữ liệu phức tạp:

**Yêu cầu:**
1. Tạo dictionary `lop_hoc` chứa thông tin lớp:
   - Key: `"ten_lop"`, `"si_so"`, `"danh_sach_hoc_sinh"`
   - `"danh_sach_hoc_sinh"` là một list các dictionary, mỗi dictionary chứa:
     - `"id"`, `"ho_ten"`, `"diem_toan"`, `"diem_ly"`, `"diem_hoa"`

2. Nhập thông tin lớp và ít nhất 3 học sinh

3. Thực hiện các thao tác:
   - Tính điểm trung bình cho mỗi học sinh
   - Tìm học sinh có điểm trung bình cao nhất
   - Sắp xếp danh sách học sinh theo điểm trung bình giảm dần
   - Tạo dictionary thống kê: số học sinh Giỏi (>=8), Khá (>=6.5), Trung bình (>=5), Yếu (<5)
   - In ra bảng điểm chi tiết

**Ví dụ:**
```
=== THÔNG TIN LỚP HỌC ===
Tên lớp: 12A1
Sĩ số: 3

=== BẢNG ĐIỂM ===
ID | Họ tên | Toán | Lý | Hóa | TB | Xếp loại
1  | Nguyễn Văn A | 8.5 | 9.0 | 8.0 | 8.5 | Giỏi
2  | Trần Thị B | 7.0 | 6.5 | 7.5 | 7.0 | Khá
3  | Lê Văn C | 5.5 | 6.0 | 5.0 | 5.5 | Trung bình

Học sinh giỏi nhất: Nguyễn Văn A (8.5)

Thống kê:
- Giỏi: 1
- Khá: 1
- Trung bình: 1
- Yếu: 0
```

---

### Câu 12 (10 điểm): Xử lý Tập hợp (Set Operations)

Viết chương trình quản lý danh sách học sinh đăng ký môn học:

**Yêu cầu:**
1. Có 3 môn học: "Toán", "Lý", "Hóa"
2. Mỗi môn có một set chứa ID của học sinh đăng ký
3. Thực hiện các phép toán tập hợp:
   - Tìm học sinh đăng ký tất cả 3 môn (intersection)
   - Tìm học sinh đăng ký ít nhất 1 môn (union)
   - Tìm học sinh chỉ đăng ký Toán (difference)
   - Tìm học sinh đăng ký Toán hoặc Lý nhưng không đăng ký Hóa
   - Kiểm tra xem có học sinh nào không đăng ký môn nào không
4. In ra kết quả các phép toán

**Ví dụ:**
```
Học sinh đăng ký Toán: {1, 2, 3, 4}
Học sinh đăng ký Lý: {2, 3, 5, 6}
Học sinh đăng ký Hóa: {3, 4, 6, 7}

Học sinh đăng ký cả 3 môn: {3}
Học sinh đăng ký ít nhất 1 môn: {1, 2, 3, 4, 5, 6, 7}
Học sinh chỉ đăng ký Toán: {1}
Học sinh (Toán hoặc Lý) và không Hóa: {1, 2, 5}
Có học sinh không đăng ký môn nào: False
```

---

## THANG ĐIỂM

| Phần | Câu | Điểm |
|------|-----|------|
| **I. Lý thuyết** | 1-5 | 30 điểm |
| **II. Thực hành** | 6-10 | 70 điểm |
| **III. Nâng cao** | 11-12 | 20 điểm |
| **TỔNG CỘNG** | | **120 điểm** |

---

## LƯU Ý ĐÁNH GIÁ

- **Logic và thuật toán:** 40%
- **Cú pháp và chạy được:** 30%
- **Code sạch, dễ đọc, có comment:** 20%
- **Xử lý lỗi và edge cases:** 10%

---

**CHÚC CÁC EM LÀM BÀI TỐT!**

*Đây là bài kiểm tra tổng hợp cuối khóa, hãy vận dụng toàn bộ kiến thức đã học!*
