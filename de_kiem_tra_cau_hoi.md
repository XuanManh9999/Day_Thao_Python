# ĐỀ KIỂM TRA PYTHON CƠ BẢN

**Thời gian làm bài:** 60 phút  
**Tổng điểm:** 100 điểm  
**Hình thức:** Làm bài trên máy tính hoặc viết code Python

---

## HƯỚNG DẪN CHUNG

1. Đọc kỹ đề trước khi làm bài
2. Làm bài theo thứ tự, nhưng có thể bỏ qua câu khó để làm câu khác
3. Chương trình phải chạy được, có nhập xuất đầy đủ
4. Code phải rõ ràng, dễ đọc, có comment khi cần thiết
5. Điểm chi tiết cho từng phần được ghi trong từng câu

---

## PHẦN I: LÝ THUYẾT (25 điểm)

### Câu 1 (5 điểm)

Cho các đoạn code sau, hãy xác định kết quả và giải thích:

```python
# a)
a = 15 // 4
b = 15 % 4
print(a, b)

# b)
x = 5
y = 10
result = x > 5 and y < 15
print(result)

# c)
s = "Python"
print(s[1:4])
print(s[-3:])

# d)
lst = [1, 2, 3]
lst.append([4, 5])
print(lst)

# e)
d = {"a": 1, "b": 2}
print(d.get("c", 0))
```

**Yêu cầu:** Viết kết quả của mỗi đoạn code (a, b, c, d, e).

---

### Câu 2 (5 điểm)

Hãy giải thích sự khác biệt giữa các cặp sau:

1. **List và Tuple:** So sánh về tính chất, cách khai báo, và khi nào nên dùng mỗi loại.
2. **break và continue:** Giải thích cách hoạt động và cho 2 ví dụ minh họa sự khác biệt.

---

### Câu 3 (5 điểm)

Cho đoạn code sau:

```python
def func1(a, b=10):
    return a + b

def func2(*args):
    return sum(args)

def func3(**kwargs):
    return kwargs
```

Hãy giải thích:
1. Tham số `b=10` trong `func1` là gì? Cho ví dụ cách gọi hàm.
2. Tham số `*args` trong `func2` là gì? Cho ví dụ.
3. Tham số `**kwargs` trong `func3` là gì? Cho ví dụ.

---

### Câu 4 (5 điểm)

Trong Python có 3 cách format string. Hãy nêu tên và cho ví dụ minh họa cho mỗi cách:

**Ví dụ:** Biến `name = "Thảo"`, `age = 20`, cần in ra: `"Tên: Thảo, Tuổi: 20"`

---

### Câu 5 (5 điểm)

Hãy so sánh các phương thức sau của Dictionary:

1. Truy cập giá trị bằng `dict[key]` và `dict.get(key)`
2. Xóa phần tử bằng `dict.pop(key)` và `del dict[key]`

Nêu ưu nhược điểm và khi nào nên dùng phương thức nào.

---

## PHẦN II: BÀI TẬP THỰC HÀNH (75 điểm)

### Câu 6 (15 điểm): Bài toán số học

Viết chương trình Python thực hiện các yêu cầu sau:

**Yêu cầu:**
1. Nhập vào 3 số nguyên `a`, `b`, `c` từ bàn phím
2. Tính và in ra:
   - Tổng 3 số
   - Trung bình cộng (làm tròn 2 chữ số thập phân)
   - Số lớn nhất và số nhỏ nhất
   - Kiểm tra xem có số nào chia hết cho 3 không (in ra "Có" hoặc "Không")

**Ví dụ:**
```
Nhập a: 15
Nhập b: 7
Nhập c: 9
Tổng: 31
Trung bình cộng: 10.33
Số lớn nhất: 15
Số nhỏ nhất: 7
Có số chia hết cho 3
```

---

### Câu 7 (15 điểm): Xử lý danh sách

Cho một list số nguyên được nhập từ bàn phím (mỗi số cách nhau bởi dấu cách), ví dụ: `"1 2 3 4 5 6 7 8 9 10"`

**Yêu cầu:**
1. Chuyển chuỗi nhập vào thành list số nguyên
2. Tạo list mới chỉ chứa các số chẵn
3. Tạo list mới chỉ chứa các số lẻ
4. Tính tổng các số chẵn và tổng các số lẻ
5. Tìm số lớn nhất và số nhỏ nhất trong list gốc
6. Đếm số lượng phần tử chia hết cho 3

**Ví dụ:**
```
Nhập các số (cách nhau bởi dấu cách): 1 2 3 4 5 6 7 8 9 10
List số chẵn: [2, 4, 6, 8, 10]
List số lẻ: [1, 3, 5, 7, 9]
Tổng số chẵn: 30
Tổng số lẻ: 25
Số lớn nhất: 10
Số nhỏ nhất: 1
Số lượng chia hết cho 3: 3
```

---

### Câu 8 (15 điểm): Quản lý sinh viên bằng Dictionary

Viết chương trình quản lý thông tin sinh viên sử dụng Dictionary:

**Yêu cầu:**
1. Nhập thông tin sinh viên gồm:
   - Họ tên (string)
   - Tuổi (int)
   - Điểm Toán, Lý, Hóa (float)
2. Lưu thông tin vào dictionary với các key: `"ho_ten"`, `"tuoi"`, `"toan"`, `"ly"`, `"hoa"`
3. Tính điểm trung bình 3 môn (làm tròn 2 chữ số)
4. Xếp loại học lực:
   - Giỏi: >= 8.0
   - Khá: >= 6.5 và < 8.0
   - Trung bình: >= 5.0 và < 6.5
   - Yếu: < 5.0
5. In ra thông tin đầy đủ của sinh viên

**Ví dụ:**
```
Nhập họ tên: Nguyễn Văn A
Nhập tuổi: 20
Nhập điểm Toán: 8.5
Nhập điểm Lý: 7.5
Nhập điểm Hóa: 9.0

=== THÔNG TIN SINH VIÊN ===
Họ tên: Nguyễn Văn A
Tuổi: 20
Điểm Toán: 8.5
Điểm Lý: 7.5
Điểm Hóa: 9.0
Điểm trung bình: 8.33
Xếp loại: Giỏi
```

---

### Câu 9 (15 điểm): Xử lý chuỗi ký tự

Viết chương trình xử lý chuỗi với các yêu cầu sau:

**Yêu cầu:**
1. Nhập vào một chuỗi từ bàn phím
2. Đếm số từ trong chuỗi (từ được phân cách bởi dấu cách)
3. Đếm số chữ cái in hoa
4. Đếm số chữ cái in thường
5. Đảo ngược chuỗi
6. Chuyển tất cả chữ cái đầu của mỗi từ thành chữ in hoa (title case)
7. Kiểm tra xem chuỗi có chứa từ "Python" không (không phân biệt hoa thường)

**Ví dụ:**
```
Nhập chuỗi: hello world Python Programming
Số từ trong chuỗi: 4
Số chữ in hoa: 2
Số chữ in thường: 22
Chuỗi đảo ngược: gnimmargorP nohtyP dlrow olleh
Chuỗi title case: Hello World Python Programming
Chuỗi có chứa "Python": Có
```

---

### Câu 10 (15 điểm): Hàm và vòng lặp

Viết các hàm sau và chương trình chính để test:

**Yêu cầu:**

1. **Hàm `kiem_tra_so_nguyen_to(n)`:**
   - Nhận vào một số nguyên `n`
   - Trả về `True` nếu `n` là số nguyên tố, ngược lại trả về `False`
   - Số nguyên tố là số chỉ chia hết cho 1 và chính nó

2. **Hàm `in_danh_sach_so_nguyen_to(start, end)`:**
   - Nhận vào 2 số nguyên `start` và `end`
   - In ra tất cả các số nguyên tố trong khoảng từ `start` đến `end` (bao gồm cả 2 đầu)
   - Sử dụng hàm `kiem_tra_so_nguyen_to()` đã viết ở trên

3. **Chương trình chính:**
   - Nhập vào 2 số `start` và `end`
   - Gọi hàm `in_danh_sach_so_nguyen_to()` để in ra kết quả

**Ví dụ:**
```
Nhập số bắt đầu: 10
Nhập số kết thúc: 30
Các số nguyên tố từ 10 đến 30:
11
13
17
19
23
29
```

**Lưu ý:** 
- Số nguyên tố nhỏ nhất là 2
- Số âm không phải số nguyên tố
- Nếu không có số nguyên tố nào trong khoảng, in ra "Không có số nguyên tố nào trong khoảng này"

---

## PHẦN III: BÀI TẬP NÂNG CAO (Tùy chọn - 10 điểm)

### Câu 11 (10 điểm): Tần suất xuất hiện

Viết chương trình đếm tần suất xuất hiện của các từ trong một đoạn văn bản:

**Yêu cầu:**
1. Nhập vào một đoạn văn bản (nhiều dòng, kết thúc bằng dòng trống hoặc dòng rỗng)
2. Tách văn bản thành các từ (phân cách bởi dấu cách)
3. Đếm tần suất xuất hiện của mỗi từ (không phân biệt hoa thường)
4. In ra từ xuất hiện nhiều nhất và số lần xuất hiện
5. Nếu có nhiều từ cùng tần suất cao nhất, in ra từ có thứ tự từ điển nhỏ nhất

**Ví dụ:**
```
Nhập văn bản (kết thúc bằng dòng trống):
Python là ngôn ngữ lập trình
Python rất dễ học
Python được sử dụng rộng rãi

Từ xuất hiện nhiều nhất: python
Số lần xuất hiện: 3
```

**Gợi ý:** 
- Sử dụng Dictionary để lưu tần suất
- Sử dụng hàm `split()` để tách từ
- Sử dụng hàm `lower()` để không phân biệt hoa thường
- Sắp xếp để tìm từ có thứ tự từ điển nhỏ nhất khi cùng tần suất

---

## THANG ĐIỂM

| Phần | Câu | Điểm |
|------|-----|------|
| **I. Lý thuyết** | 1-5 | 25 điểm |
| **II. Thực hành** | 6-10 | 75 điểm |
| **III. Nâng cao** | 11 | 10 điểm (tùy chọn) |
| **TỔNG CỘNG** | | **100 điểm** (hoặc 110 nếu làm câu 11) |

---

## LƯU Ý

- Làm đúng yêu cầu: **70%**
- Code chạy được, có xử lý lỗi cơ bản: **20%**
- Code sạch, dễ đọc, có comment: **10%**

---

**CHÚC CÁC EM LÀM BÀI TỐT!**

*Thời gian còn lại sẽ được thông báo định kỳ*
