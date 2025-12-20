# ĐÁP ÁN ĐỀ KIỂM TRA PYTHON

---

## PHẦN 1: CÂU HỎI LÝ THUYẾT (20 điểm)

### Câu 1 (4 điểm)
**Đáp án:**
```python
a = 10 // 3  # Kết quả: 3 (chia lấy phần nguyên)
b = 10 % 3   # Kết quả: 1 (chia lấy phần dư)
c = 2 ** 3   # Kết quả: 8 (lũy thừa: 2^3 = 8)
d = 5.5 // 2 # Kết quả: 2.0 (chia lấy phần nguyên, kết quả là float)
```

**Giải thích:**
- `//`: Toán tử chia lấy phần nguyên
- `%`: Toán tử chia lấy phần dư
- `**`: Toán tử lũy thừa

---

### Câu 2 (4 điểm)
**Đáp án:**

**Sự khác biệt:**
- `break`: Thoát hoàn toàn khỏi vòng lặp, không thực hiện các lần lặp còn lại
- `continue`: Bỏ qua các câu lệnh còn lại trong lần lặp hiện tại, nhưng vẫn tiếp tục các lần lặp tiếp theo

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

### Câu 3 (4 điểm)
**Đáp án:**

- Hàm `input()` trong Python **mặc định trả về kiểu dữ liệu string (chuỗi)**

- Để nhập một số nguyên, ta cần **ép kiểu** bằng hàm `int()`:
```python
n = int(input("Nhập số: "))
```

**Ví dụ:**
```python
a = input("Nhập số: ")  # a có kiểu str
b = int(input("Nhập số: "))  # b có kiểu int
```

---

### Câu 4 (4 điểm)
**Đáp án:**

**Sự khác biệt chính:**

| Đặc điểm | List | Tuple |
|----------|------|-------|
| Cú pháp | `[1, 2, 3]` | `(1, 2, 3)` |
| Có thể thay đổi | Có (mutable) | Không (immutable) |
| Có thể thêm/xóa/sửa | Có | Không |
| Tốc độ | Chậm hơn | Nhanh hơn |
| Ứng dụng | Dữ liệu có thể thay đổi | Dữ liệu cố định, không đổi |

**Ví dụ:**
```python
# List - có thể thay đổi
a = [1, 2, 3]
a[0] = 10  # Được phép
a.append(4)  # Được phép

# Tuple - không thể thay đổi
b = (1, 2, 3)
b[0] = 10  # LỖI! Không được phép
```

---

### Câu 5 (4 điểm)
**Đáp án:**

**2 cách truy cập key trong Dictionary:**

**Cách 1: Dùng dấu ngoặc vuông `dict[key]`**
```python
info = {"name": "Thảo", "age": 20}
print(info["name"])  # Kết quả: Thảo
```
- **Nhược điểm:** Nếu key không tồn tại sẽ báo lỗi `KeyError`

**Cách 2: Dùng hàm `get(key)`**
```python
info = {"name": "Thảo", "age": 20}
print(info.get("name"))  # Kết quả: Thảo
print(info.get("address"))  # Kết quả: None (không báo lỗi)
```
- **Ưu điểm:** Nếu key không tồn tại, trả về `None` thay vì báo lỗi

**Kết luận:** Nên dùng `get()` để tránh lỗi khi key có thể không tồn tại.

---

## PHẦN 2: BÀI TẬP THỰC HÀNH (80 điểm)

### Câu 6 (15 điểm)
**Đáp án:**

```python
# Nhập 2 số từ bàn phím
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

# Tính các phép toán
tong = a + b
hieu = a - b
tich = a * b
thuong = round(a / b, 2)  # Làm tròn 2 chữ số thập phân
chia_du = a % b
luy_thua = a ** b

# In kết quả
print(f"Tổng: {tong}")
print(f"Hiệu: {hieu}")
print(f"Tích: {tich}")
print(f"Thương: {thuong}")
print(f"Chia dư: {chia_du}")
print(f"Lũy thừa: {luy_thua}")
```

**Hoặc cách khác:**
```python
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

print(f"Tổng: {a + b}")
print(f"Hiệu: {a - b}")
print(f"Tích: {a * b}")
print(f"Thương: {round(a / b, 2)}")
print(f"Chia dư: {a % b}")
print(f"Lũy thừa: {a ** b}")
```

---

### Câu 7 (15 điểm)
**Đáp án:**

```python
n = int(input("Nhập số nguyên n: "))

# Kiểm tra các điều kiện
if n % 2 == 0 and n > 10:
    print("Số chẵn lớn hơn 10")

if n % 2 != 0 and n < 5:
    print("Số lẻ nhỏ hơn 5")

if n % 3 == 0:
    print("Số chia hết cho 3")

# Kiểm tra nếu không thỏa mãn điều kiện nào
if not ((n % 2 == 0 and n > 10) or (n % 2 != 0 and n < 5) or (n % 3 == 0)):
    print("Không thỏa mãn điều kiện")
```

**Hoặc cách khác (dùng elif):**
```python
n = int(input("Nhập số nguyên n: "))
thoa_man = False

if n % 2 == 0 and n > 10:
    print("Số chẵn lớn hơn 10")
    thoa_man = True

if n % 2 != 0 and n < 5:
    print("Số lẻ nhỏ hơn 5")
    thoa_man = True

if n % 3 == 0:
    print("Số chia hết cho 3")
    thoa_man = True

if not thoa_man:
    print("Không thỏa mãn điều kiện")
```

---

### Câu 8 (15 điểm)
**Đáp án:**

```python
n = int(input("Nhập n: "))
tong = 0

# Dùng vòng lặp for
for i in range(1, n + 1):
    tong += i

print(f"Tổng từ 1 đến {n} là: {tong}")
```

**Hoặc dùng hàm sum():**
```python
n = int(input("Nhập n: "))
tong = sum(range(1, n + 1))
print(f"Tổng từ 1 đến {n} là: {tong}")
```

---

### Câu 9 (15 điểm)
**Đáp án:**

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. In ra các phần tử chẵn
print("Các phần tử chẵn:")
for x in a:
    if x % 2 == 0:
        print(x, end=" ")
print()  # Xuống dòng

# 2. Tính tổng các phần tử
tong = sum(a)
print(f"Tổng các phần tử: {tong}")

# 3. Tìm số lớn nhất và nhỏ nhất
so_lon_nhat = max(a)
so_nho_nhat = min(a)
print(f"Số lớn nhất: {so_lon_nhat}")
print(f"Số nhỏ nhất: {so_nho_nhat}")

# 4. Đếm số chia hết cho 3
dem = 0
for x in a:
    if x % 3 == 0:
        dem += 1
print(f"Số lượng phần tử chia hết cho 3: {dem}")
```

**Hoặc cách ngắn gọn hơn:**
```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. In ra các phần tử chẵn
print("Các phần tử chẵn:", [x for x in a if x % 2 == 0])

# 2. Tính tổng
print(f"Tổng: {sum(a)}")

# 3. Tìm max và min
print(f"Max: {max(a)}, Min: {min(a)}")

# 4. Đếm số chia hết cho 3
dem = len([x for x in a if x % 3 == 0])
print(f"Số chia hết cho 3: {dem}")
```

---

### Câu 10 (20 điểm)
**Đáp án:**

```python
# Tạo dictionary
hoc_sinh = {}

# Nhập thông tin
hoc_sinh["ten"] = input("Nhập tên: ")
hoc_sinh["tuoi"] = int(input("Nhập tuổi: "))
hoc_sinh["diem_toan"] = float(input("Nhập điểm toán: "))
hoc_sinh["diem_ly"] = float(input("Nhập điểm lý: "))
hoc_sinh["diem_hoa"] = float(input("Nhập điểm hóa: "))

# Tính điểm trung bình
diem_tb = (hoc_sinh["diem_toan"] + hoc_sinh["diem_ly"] + hoc_sinh["diem_hoa"]) / 3

# In thông tin
print("\nThông tin học sinh:")
print(f"Tên: {hoc_sinh['ten']}")
print(f"Tuổi: {hoc_sinh['tuoi']}")
print(f"Điểm trung bình: {round(diem_tb, 2)}")
```

**Hoặc cách khác:**
```python
# Nhập thông tin trực tiếp
ten = input("Nhập tên: ")
tuoi = int(input("Nhập tuổi: "))
diem_toan = float(input("Nhập điểm toán: "))
diem_ly = float(input("Nhập điểm lý: "))
diem_hoa = float(input("Nhập điểm hóa: "))

# Tạo dictionary
hoc_sinh = {
    "ten": ten,
    "tuoi": tuoi,
    "diem_toan": diem_toan,
    "diem_ly": diem_ly,
    "diem_hoa": diem_hoa
}

# Tính và in kết quả
diem_tb = round((diem_toan + diem_ly + diem_hoa) / 3, 2)

print("\nThông tin học sinh:")
print(f"Tên: {hoc_sinh['ten']}")
print(f"Tuổi: {hoc_sinh['tuoi']}")
print(f"Điểm trung bình: {diem_tb}")
```

---

## PHẦN 3: BÀI TẬP NÂNG CAO (10 điểm - Tùy chọn)

### Câu 11 (10 điểm)
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

# Chương trình chính
n = int(input("Nhập số cần kiểm tra: "))

if kiem_tra_so_nguyen_to(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")
```

**Hoặc cách tối ưu hơn (chỉ kiểm tra đến căn bậc 2):**
```python
from math import isqrt

def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    
    # Chỉ cần kiểm tra đến căn bậc 2 của n
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    
    return True

# Chương trình chính
n = int(input("Nhập số cần kiểm tra: "))

if kiem_tra_so_nguyen_to(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")
```

---

## THANG ĐIỂM CHI TIẾT

### Phần 1: Lý thuyết (20 điểm)
- Câu 1: 4 điểm (mỗi kết quả đúng 1 điểm)
- Câu 2: 4 điểm (giải thích 2 điểm, ví dụ 2 điểm)
- Câu 3: 4 điểm (kiểu dữ liệu 2 điểm, cách ép kiểu 2 điểm)
- Câu 4: 4 điểm (sự khác biệt 2 điểm, ví dụ 2 điểm)
- Câu 5: 4 điểm (2 cách 2 điểm, giải thích 2 điểm)

### Phần 2: Thực hành (80 điểm)
- Câu 6: 15 điểm (nhập đúng 2 điểm, tính đúng mỗi phép toán 2 điểm, in kết quả 1 điểm)
- Câu 7: 15 điểm (nhập đúng 2 điểm, mỗi điều kiện đúng 4 điểm, xử lý trường hợp khác 1 điểm)
- Câu 8: 15 điểm (nhập đúng 3 điểm, vòng lặp đúng 8 điểm, tính tổng đúng 2 điểm, in kết quả 2 điểm)
- Câu 9: 15 điểm (mỗi yêu cầu 3.75 điểm)
- Câu 10: 20 điểm (tạo dict 5 điểm, nhập đúng 5 điểm, tính điểm TB 5 điểm, in kết quả 5 điểm)

### Phần 3: Nâng cao (10 điểm - Tùy chọn)
- Câu 11: 10 điểm (định nghĩa hàm đúng 5 điểm, chương trình chính 3 điểm, logic đúng 2 điểm)

---

**TỔNG ĐIỂM: 100 điểm (hoặc 110 điểm nếu làm câu 11)**

