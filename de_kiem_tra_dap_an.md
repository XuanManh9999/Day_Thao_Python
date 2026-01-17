# ĐÁP ÁN ĐỀ KIỂM TRA PYTHON CƠ BẢN

---

## PHẦN I: LÝ THUYẾT (25 điểm)

### Câu 1 (5 điểm)

**Đáp án:**

a) **Kết quả:** `3 3`
- `15 // 4 = 3` (chia lấy phần nguyên: 15 chia 4 = 3 dư 3)
- `15 % 4 = 3` (chia lấy phần dư: 15 chia 4 dư 3)

b) **Kết quả:** `False`
- `x > 5` → `5 > 5` → `False`
- `y < 15` → `10 < 15` → `True`
- `False and True` → `False` (toán tử `and` cần cả 2 đều `True` mới trả về `True`)

c) **Kết quả:**
```
yth
hon
```
- `s[1:4]` → Lấy từ vị trí 1 đến 3 (không lấy 4): `"yth"`
- `s[-3:]` → Lấy từ vị trí -3 đến cuối: `"hon"` (3 ký tự cuối)

d) **Kết quả:** `[1, 2, 3, [4, 5]]`
- `append()` thêm phần tử vào cuối list
- Ở đây thêm cả list `[4, 5]` như một phần tử (nested list)

e) **Kết quả:** `0`
- `dict.get(key, default)` trả về giá trị nếu key tồn tại, ngược lại trả về giá trị default
- Key `"c"` không tồn tại trong dict, nên trả về giá trị mặc định là `0`

---

### Câu 2 (5 điểm)

**Đáp án:**

#### 1. List vs Tuple

| Tiêu chí | List | Tuple |
|----------|------|-------|
| **Cú pháp** | `[1, 2, 3]` | `(1, 2, 3)` |
| **Tính chất** | Mutable (có thể thay đổi) | Immutable (không thể thay đổi) |
| **Thao tác** | Có thể thêm, xóa, sửa phần tử | Không thể thay đổi sau khi tạo |
| **Tốc độ** | Chậm hơn | Nhanh hơn |
| **Bộ nhớ** | Tốn nhiều bộ nhớ hơn | Tiết kiệm bộ nhớ hơn |
| **Khi nào dùng** | Dữ liệu cần thay đổi | Dữ liệu cố định, không đổi |

**Ví dụ:**
```python
# List - có thể thay đổi
lst = [1, 2, 3]
lst[0] = 10  # Được phép → [10, 2, 3]
lst.append(4)  # Được phép → [10, 2, 3, 4]

# Tuple - không thể thay đổi
tup = (1, 2, 3)
tup[0] = 10  # LỖI! TypeError
```

#### 2. break vs continue

**`break`:**
- Thoát hoàn toàn khỏi vòng lặp
- Các lần lặp còn lại sẽ không được thực hiện
- Chỉ thoát khỏi vòng lặp chứa nó

**`continue`:**
- Bỏ qua các câu lệnh còn lại trong lần lặp hiện tại
- Vẫn tiếp tục các lần lặp tiếp theo

**Ví dụ:**

```python
# Ví dụ với break
for i in range(1, 6):
    if i == 3:
        break
    print(i)
# Kết quả: 1, 2 (dừng khi i = 3)

# Ví dụ với continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Kết quả: 1, 2, 4, 5 (bỏ qua i = 3 nhưng tiếp tục)
```

---

### Câu 3 (5 điểm)

**Đáp án:**

#### 1. Tham số mặc định (`b=10`)

- `b=10` là **tham số mặc định** (default argument)
- Nếu không truyền giá trị cho `b` khi gọi hàm, `b` sẽ tự động nhận giá trị `10`
- Tham số mặc định phải đặt sau các tham số không có giá trị mặc định

**Ví dụ:**
```python
func1(5)      # a=5, b=10 → Kết quả: 15
func1(5, 20)  # a=5, b=20 → Kết quả: 25
func1(a=5)    # a=5, b=10 → Kết quả: 15
```

#### 2. Tham số `*args`

- `*args` cho phép hàm nhận **số lượng tham số không xác định** (variadic arguments)
- Các giá trị truyền vào sẽ được gói vào một **tuple**
- `args` chỉ là tên biến, có thể đặt tên khác như `*numbers`, `*values`

**Ví dụ:**
```python
func2(1, 2, 3)           # args = (1, 2, 3) → Kết quả: 6
func2(1, 2, 3, 4, 5)     # args = (1, 2, 3, 4, 5) → Kết quả: 15
func2(10)                # args = (10,) → Kết quả: 10
```

#### 3. Tham số `**kwargs`

- `**kwargs` cho phép hàm nhận **số lượng tham số từ khóa không xác định** (keyword arguments)
- Các giá trị truyền vào sẽ được gói vào một **dictionary**
- Khi gọi hàm, phải dùng cú pháp `key=value`
- `kwargs` chỉ là tên biến, có thể đặt tên khác

**Ví dụ:**
```python
func3(name="Thảo", age=20)
# kwargs = {"name": "Thảo", "age": 20}
# Kết quả: {"name": "Thảo", "age": 20}

func3(a=1, b=2, c=3)
# kwargs = {"a": 1, "b": 2, "c": 3}
# Kết quả: {"a": 1, "b": 2, "c": 3}
```

---

### Câu 4 (5 điểm)

**Đáp án:**

Có **3 cách format string** trong Python:

#### 1. F-string (f-string) - Cách hiện đại nhất (Python 3.6+)

```python
name = "Thảo"
age = 20
s = f"Tên: {name}, Tuổi: {age}"
print(s)  # Tên: Thảo, Tuổi: 20
```

**Ưu điểm:** Dễ đọc, nhanh nhất, có thể dùng biểu thức bên trong `{}`

#### 2. String formatting với `%` (printf-style)

```python
name = "Thảo"
age = 20
s = "Tên: %s, Tuổi: %d" % (name, age)
print(s)  # Tên: Thảo, Tuổi: 20
```

**Lưu ý:**
- `%s` cho string
- `%d` cho số nguyên
- `%f` cho số thực

#### 3. Phương thức `.format()`

```python
name = "Thảo"
age = 20
s = "Tên: {}, Tuổi: {}".format(name, age)
# hoặc
s = "Tên: {0}, Tuổi: {1}".format(name, age)
# hoặc với tên biến
s = "Tên: {n}, Tuổi: {a}".format(n=name, a=age)
print(s)  # Tên: Thảo, Tuổi: 20
```

---

### Câu 5 (5 điểm)

**Đáp án:**

#### 1. Truy cập giá trị: `dict[key]` vs `dict.get(key)`

**`dict[key]`:**
- ✅ Ưu điểm: Cú pháp ngắn gọn
- ❌ Nhược điểm: Nếu key không tồn tại → **Lỗi KeyError**
- 📌 Khi dùng: Khi chắc chắn key tồn tại

**`dict.get(key, default)`:**
- ✅ Ưu điểm: An toàn, không gây lỗi nếu key không tồn tại, trả về `None` hoặc giá trị mặc định
- ❌ Nhược điểm: Cú pháp dài hơn một chút
- 📌 Khi dùng: Khi không chắc chắn key có tồn tại

**Ví dụ:**
```python
d = {"a": 1, "b": 2}

# Cách 1 - có thể lỗi
print(d["c"])  # KeyError!

# Cách 2 - an toàn
print(d.get("c"))      # None
print(d.get("c", 0))   # 0 (giá trị mặc định)
```

#### 2. Xóa phần tử: `dict.pop(key)` vs `del dict[key]`

**`dict.pop(key)`:**
- ✅ Ưu điểm: Trả về giá trị của phần tử vừa xóa, có thể dùng giá trị này
- ❌ Nhược điểm: Nếu key không tồn tại → **Lỗi KeyError**
- 📌 Khi dùng: Khi cần lấy giá trị của phần tử vừa xóa

**`del dict[key]`:**
- ✅ Ưu điểm: Cú pháp ngắn gọn
- ❌ Nhược điểm: Không trả về giá trị, nếu key không tồn tại → **Lỗi KeyError**
- 📌 Khi dùng: Khi chỉ muốn xóa, không cần giá trị

**Ví dụ:**
```python
d = {"a": 1, "b": 2, "c": 3}

# Cách 1 - có giá trị trả về
value = d.pop("b")  # value = 2, d = {"a": 1, "c": 3}

# Cách 2 - không có giá trị trả về
del d["c"]  # d = {"a": 1}

# An toàn hơn
if "x" in d:
    del d["x"]
# hoặc
if d.get("x") is not None:
    d.pop("x")
```

---

## PHẦN II: BÀI TẬP THỰC HÀNH (75 điểm)

### Câu 6 (15 điểm): Bài toán số học

**Đáp án:**

```python
# Nhập 3 số nguyên
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

# Tính tổng
tong = a + b + c

# Tính trung bình cộng
trung_binh = round(tong / 3, 2)

# Tìm số lớn nhất và nhỏ nhất
so_lon_nhat = max(a, b, c)
so_nho_nhat = min(a, b, c)

# Kiểm tra số chia hết cho 3
co_so_chia_het = "Có" if (a % 3 == 0 or b % 3 == 0 or c % 3 == 0) else "Không"

# In kết quả
print(f"Tổng: {tong}")
print(f"Trung bình cộng: {trung_binh}")
print(f"Số lớn nhất: {so_lon_nhat}")
print(f"Số nhỏ nhất: {so_nho_nhat}")
print(f"{co_so_chia_het} số chia hết cho 3")
```

**Hoặc cách chi tiết hơn:**

```python
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

tong = a + b + c
trung_binh = tong / 3
trung_binh = round(trung_binh, 2)

# Tìm max, min
if a >= b and a >= c:
    so_lon_nhat = a
elif b >= a and b >= c:
    so_lon_nhat = b
else:
    so_lon_nhat = c

if a <= b and a <= c:
    so_nho_nhat = a
elif b <= a and b <= c:
    so_nho_nhat = b
else:
    so_nho_nhat = c

# Kiểm tra chia hết cho 3
co_chia_het = False
if a % 3 == 0 or b % 3 == 0 or c % 3 == 0:
    co_chia_het = True

print(f"Tổng: {tong}")
print(f"Trung bình cộng: {trung_binh}")
print(f"Số lớn nhất: {so_lon_nhat}")
print(f"Số nhỏ nhất: {so_nho_nhat}")
if co_chia_het:
    print("Có số chia hết cho 3")
else:
    print("Không có số chia hết cho 3")
```

---

### Câu 7 (15 điểm): Xử lý danh sách

**Đáp án:**

```python
# Nhập chuỗi số
input_str = input("Nhập các số (cách nhau bởi dấu cách): ")

# Chuyển thành list số nguyên
numbers = [int(x) for x in input_str.split()]

# Tạo list số chẵn và số lẻ
so_chan = [x for x in numbers if x % 2 == 0]
so_le = [x for x in numbers if x % 2 != 0]

# Tính tổng
tong_chan = sum(so_chan)
tong_le = sum(so_le)

# Tìm max, min
so_lon_nhat = max(numbers)
so_nho_nhat = min(numbers)

# Đếm số chia hết cho 3
dem_chia_het_3 = len([x for x in numbers if x % 3 == 0])

# In kết quả
print(f"List số chẵn: {so_chan}")
print(f"List số lẻ: {so_le}")
print(f"Tổng số chẵn: {tong_chan}")
print(f"Tổng số lẻ: {tong_le}")
print(f"Số lớn nhất: {so_lon_nhat}")
print(f"Số nhỏ nhất: {so_nho_nhat}")
print(f"Số lượng chia hết cho 3: {dem_chia_het_3}")
```

**Hoặc không dùng list comprehension:**

```python
input_str = input("Nhập các số (cách nhau bởi dấu cách): ")

# Tách chuỗi thành list string, rồi ép kiểu
str_list = input_str.split()
numbers = []
for s in str_list:
    numbers.append(int(s))

# Tạo list số chẵn và lẻ
so_chan = []
so_le = []
for x in numbers:
    if x % 2 == 0:
        so_chan.append(x)
    else:
        so_le.append(x)

# Tính tổng
tong_chan = 0
for x in so_chan:
    tong_chan += x

tong_le = 0
for x in so_le:
    tong_le += x

# Tìm max, min
so_lon_nhat = numbers[0]
so_nho_nhat = numbers[0]
for x in numbers:
    if x > so_lon_nhat:
        so_lon_nhat = x
    if x < so_nho_nhat:
        so_nho_nhat = x

# Đếm số chia hết cho 3
dem_chia_het_3 = 0
for x in numbers:
    if x % 3 == 0:
        dem_chia_het_3 += 1

print(f"List số chẵn: {so_chan}")
print(f"List số lẻ: {so_le}")
print(f"Tổng số chẵn: {tong_chan}")
print(f"Tổng số lẻ: {tong_le}")
print(f"Số lớn nhất: {so_lon_nhat}")
print(f"Số nhỏ nhất: {so_nho_nhat}")
print(f"Số lượng chia hết cho 3: {dem_chia_het_3}")
```

---

### Câu 8 (15 điểm): Quản lý sinh viên bằng Dictionary

**Đáp án:**

```python
# Tạo dictionary
sinh_vien = {}

# Nhập thông tin
sinh_vien["ho_ten"] = input("Nhập họ tên: ")
sinh_vien["tuoi"] = int(input("Nhập tuổi: "))
sinh_vien["toan"] = float(input("Nhập điểm Toán: "))
sinh_vien["ly"] = float(input("Nhập điểm Lý: "))
sinh_vien["hoa"] = float(input("Nhập điểm Hóa: "))

# Tính điểm trung bình
diem_tb = (sinh_vien["toan"] + sinh_vien["ly"] + sinh_vien["hoa"]) / 3
diem_tb = round(diem_tb, 2)

# Xếp loại
if diem_tb >= 8.0:
    xep_loai = "Giỏi"
elif diem_tb >= 6.5:
    xep_loai = "Khá"
elif diem_tb >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

# In kết quả
print("\n=== THÔNG TIN SINH VIÊN ===")
print(f"Họ tên: {sinh_vien['ho_ten']}")
print(f"Tuổi: {sinh_vien['tuoi']}")
print(f"Điểm Toán: {sinh_vien['toan']}")
print(f"Điểm Lý: {sinh_vien['ly']}")
print(f"Điểm Hóa: {sinh_vien['hoa']}")
print(f"Điểm trung bình: {diem_tb}")
print(f"Xếp loại: {xep_loai}")
```

**Hoặc cách khác:**

```python
# Nhập trực tiếp vào biến
ho_ten = input("Nhập họ tên: ")
tuoi = int(input("Nhập tuổi: "))
toan = float(input("Nhập điểm Toán: "))
ly = float(input("Nhập điểm Lý: "))
hoa = float(input("Nhập điểm Hóa: "))

# Tạo dictionary
sinh_vien = {
    "ho_ten": ho_ten,
    "tuoi": tuoi,
    "toan": toan,
    "ly": ly,
    "hoa": hoa
}

# Tính và xếp loại
diem_tb = round((toan + ly + hoa) / 3, 2)

if diem_tb >= 8.0:
    xep_loai = "Giỏi"
elif diem_tb >= 6.5:
    xep_loai = "Khá"
elif diem_tb >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"

# In kết quả
print("\n=== THÔNG TIN SINH VIÊN ===")
for key, value in sinh_vien.items():
    print(f"{key.capitalize()}: {value}")
print(f"Điểm trung bình: {diem_tb}")
print(f"Xếp loại: {xep_loai}")
```

---

### Câu 9 (15 điểm): Xử lý chuỗi ký tự

**Đáp án:**

```python
# Nhập chuỗi
s = input("Nhập chuỗi: ")

# 1. Đếm số từ
tu_list = s.split()
so_tu = len(tu_list)

# 2. Đếm số chữ in hoa
dem_hoa = 0
for char in s:
    if char.isupper():
        dem_hoa += 1

# 3. Đếm số chữ in thường
dem_thuong = 0
for char in s:
    if char.islower():
        dem_thuong += 1

# 4. Đảo ngược chuỗi
dao_nguoc = s[::-1]

# 5. Chuyển title case
title_case = s.title()

# 6. Kiểm tra chứa "Python" (không phân biệt hoa thường)
co_python = "Có" if "python" in s.lower() else "Không"

# In kết quả
print(f"Số từ trong chuỗi: {so_tu}")
print(f"Số chữ in hoa: {dem_hoa}")
print(f"Số chữ in thường: {dem_thuong}")
print(f"Chuỗi đảo ngược: {dao_nguoc}")
print(f"Chuỗi title case: {title_case}")
print(f"Chuỗi có chứa \"Python\": {co_python}")
```

**Hoặc cách khác:**

```python
s = input("Nhập chuỗi: ")

# Đếm từ
so_tu = len(s.split())

# Đếm chữ hoa/thường
dem_hoa = sum(1 for c in s if c.isupper())
dem_thuong = sum(1 for c in s if c.islower())

# Đảo ngược
dao_nguoc = ''.join(reversed(s))  # Hoặc s[::-1]

# Title case
title_case = s.title()

# Kiểm tra Python
co_python = "Có" if "python" in s.lower() else "Không"

print(f"Số từ trong chuỗi: {so_tu}")
print(f"Số chữ in hoa: {dem_hoa}")
print(f"Số chữ in thường: {dem_thuong}")
print(f"Chuỗi đảo ngược: {dao_nguoc}")
print(f"Chuỗi title case: {title_case}")
print(f"Chuỗi có chứa \"Python\": {co_python}")
```

---

### Câu 10 (15 điểm): Hàm và vòng lặp

**Đáp án:**

```python
def kiem_tra_so_nguyen_to(n):
    """
    Kiểm tra xem n có phải là số nguyên tố không
    Số nguyên tố là số chỉ chia hết cho 1 và chính nó
    """
    # Số nhỏ hơn 2 không phải số nguyên tố
    if n < 2:
        return False
    
    # Kiểm tra từ 2 đến n-1
    for i in range(2, n):
        if n % i == 0:  # Nếu chia hết cho số nào đó
            return False
    
    return True


def in_danh_sach_so_nguyen_to(start, end):
    """
    In ra tất cả các số nguyên tố trong khoảng [start, end]
    """
    so_nguyen_to = []
    
    for num in range(start, end + 1):
        if kiem_tra_so_nguyen_to(num):
            so_nguyen_to.append(num)
    
    if len(so_nguyen_to) == 0:
        print("Không có số nguyên tố nào trong khoảng này")
    else:
        print(f"Các số nguyên tố từ {start} đến {end}:")
        for prime in so_nguyen_to:
            print(prime)


# Chương trình chính
start = int(input("Nhập số bắt đầu: "))
end = int(input("Nhập số kết thúc: "))

# Kiểm tra khoảng hợp lệ
if start > end:
    print("Số bắt đầu phải nhỏ hơn hoặc bằng số kết thúc!")
else:
    in_danh_sach_so_nguyen_to(start, end)
```

**Hoặc tối ưu hơn (chỉ kiểm tra đến căn bậc 2):**

```python
from math import isqrt

def kiem_tra_so_nguyen_to(n):
    """Kiểm tra số nguyên tố - tối ưu"""
    if n < 2:
        return False
    
    # Chỉ cần kiểm tra đến căn bậc 2 của n
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    
    return True


def in_danh_sach_so_nguyen_to(start, end):
    """In danh sách số nguyên tố"""
    so_nguyen_to = []
    
    for num in range(start, end + 1):
        if kiem_tra_so_nguyen_to(num):
            so_nguyen_to.append(num)
    
    if so_nguyen_to:
        print(f"Các số nguyên tố từ {start} đến {end}:")
        for prime in so_nguyen_to:
            print(prime)
    else:
        print("Không có số nguyên tố nào trong khoảng này")


# Chương trình chính
start = int(input("Nhập số bắt đầu: "))
end = int(input("Nhập số kết thúc: "))

if start <= end:
    in_danh_sach_so_nguyen_to(start, end)
else:
    print("Khoảng không hợp lệ!")
```

---

## PHẦN III: BÀI TẬP NÂNG CAO (10 điểm)

### Câu 11 (10 điểm): Tần suất xuất hiện

**Đáp án:**

```python
# Nhập văn bản (nhiều dòng)
print("Nhập văn bản (kết thúc bằng dòng trống):")
lines = []
while True:
    line = input()
    if line.strip() == "":  # Dòng trống
        break
    lines.append(line)

# Nối tất cả các dòng thành một chuỗi
van_ban = " ".join(lines)

# Tách thành các từ và chuyển về chữ thường
tu_list = van_ban.lower().split()

# Đếm tần suất bằng Dictionary
tan_suat = {}
for tu in tu_list:
    if tu in tan_suat:
        tan_suat[tu] += 1
    else:
        tan_suat[tu] = 1

# Tìm từ xuất hiện nhiều nhất
max_tan_suat = 0
tu_xuat_hien_nhieu_nhat = None

for tu, so_lan in tan_suat.items():
    if so_lan > max_tan_suat:
        max_tan_suat = so_lan
        tu_xuat_hien_nhieu_nhat = tu
    elif so_lan == max_tan_suat:
        # Nếu cùng tần suất, chọn từ có thứ tự từ điển nhỏ nhất
        if tu < tu_xuat_hien_nhieu_nhat:
            tu_xuat_hien_nhieu_nhat = tu

# In kết quả
print(f"\nTừ xuất hiện nhiều nhất: {tu_xuat_hien_nhieu_nhat}")
print(f"Số lần xuất hiện: {max_tan_suat}")
```

**Hoặc cách ngắn gọn hơn:**

```python
# Nhập văn bản
print("Nhập văn bản (kết thúc bằng dòng trống):")
lines = []
while True:
    line = input()
    if not line.strip():
        break
    lines.append(line)

# Tách từ và đếm
tu_list = " ".join(lines).lower().split()

# Đếm tần suất
tan_suat = {}
for tu in tu_list:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1

# Tìm max (có xử lý trường hợp cùng tần suất)
max_count = max(tan_suat.values())
tu_max = min([tu for tu, count in tan_suat.items() if count == max_count])

print(f"\nTừ xuất hiện nhiều nhất: {tu_max}")
print(f"Số lần xuất hiện: {max_count}")
```

**Giải thích:**
1. Nhập văn bản nhiều dòng cho đến khi gặp dòng trống
2. Nối các dòng và chuyển về chữ thường
3. Tách thành list các từ
4. Dùng Dictionary để đếm tần suất
5. Tìm từ có tần suất cao nhất
6. Nếu nhiều từ cùng tần suất, chọn từ có thứ tự từ điển nhỏ nhất (dùng `min()`)

---

## THANG ĐIỂM CHI TIẾT

| Câu | Yêu cầu | Điểm |
|-----|---------|------|
| **1** | Mỗi phần (a-e) đúng | 1 điểm |
| **2** | So sánh List/Tuple | 2.5 điểm |
| | So sánh break/continue | 2.5 điểm |
| **3** | Giải thích default arg | 1.5 điểm |
| | Giải thích *args | 1.5 điểm |
| | Giải thích **kwargs | 2 điểm |
| **4** | 3 cách format string | Mỗi cách 1.67 điểm |
| **5** | So sánh truy cập dict | 2.5 điểm |
| | So sánh xóa dict | 2.5 điểm |
| **6** | Nhập đúng | 2 điểm |
| | Tính toán đúng | 10 điểm |
| | In kết quả đúng | 3 điểm |
| **7** | Chuyển đổi chuỗi | 2 điểm |
| | Tạo list chẵn/lẻ | 3 điểm |
| | Tính tổng | 3 điểm |
| | Tìm max/min | 3 điểm |
| | Đếm chia hết | 2 điểm |
| | In kết quả | 2 điểm |
| **8** | Nhập thông tin | 3 điểm |
| | Lưu vào dict | 2 điểm |
| | Tính điểm TB | 3 điểm |
| | Xếp loại | 4 điểm |
| | In kết quả | 3 điểm |
| **9** | Đếm từ | 2 điểm |
| | Đếm chữ hoa/thường | 4 điểm |
| | Đảo ngược | 2 điểm |
| | Title case | 2 điểm |
| | Kiểm tra Python | 2 điểm |
| | In kết quả | 3 điểm |
| **10** | Hàm kiểm tra SNT | 6 điểm |
| | Hàm in danh sách | 5 điểm |
| | Chương trình chính | 2 điểm |
| | Xử lý lỗi | 2 điểm |
| **11** | Nhập văn bản | 2 điểm |
| | Đếm tần suất | 4 điểm |
| | Tìm từ max | 3 điểm |
| | Xử lý cùng tần suất | 1 điểm |

---

**TỔNG ĐIỂM: 100 điểm (hoặc 110 điểm nếu làm câu 11)**
