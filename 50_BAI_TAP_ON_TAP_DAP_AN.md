# ĐÁP ÁN 50 BÀI TẬP ÔN TẬP PYTHON

---

## PHẦN I: CƠ BẢN - BIẾN, TOÁN TỬ, RẼ NHÁNH (Bài 1-10)

### Bài 1 (2 điểm): Tính toán cơ bản

```python
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

tong = a + b
hieu = a - b
tich = a * b
thuong = round(a / b, 2) if b != 0 else "Không chia được"
chia_du = a % b if b != 0 else "Không chia được"
luy_thua = a ** b

print(f"Tổng: {tong}")
print(f"Hiệu: {hieu}")
print(f"Tích: {tich}")
print(f"Thương: {thuong}")
print(f"Chia dư: {chia_du}")
print(f"Lũy thừa: {luy_thua}")
```

---

### Bài 2 (2 điểm): Kiểm tra số chẵn lẻ

```python
n = int(input("Nhập số nguyên n: "))

if n < 0:
    print("Số âm")
elif n % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")
```

---

### Bài 3 (2 điểm): So sánh 3 số

```python
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

so_lon_nhat = max(a, b, c)
so_nho_nhat = min(a, b, c)

print(f"Số lớn nhất: {so_lon_nhat}")
print(f"Số nhỏ nhất: {so_nho_nhat}")
```

---

### Bài 4 (3 điểm): Xếp loại điểm

```python
diem = float(input("Nhập điểm (0-10): "))

if diem < 0 or diem > 10:
    print("Điểm không hợp lệ!")
elif diem >= 8.0:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")
```

---

### Bài 5 (3 điểm): Giải phương trình bậc nhất

```python
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print(f"Nghiệm: x = {x}")
```

---

### Bài 6 (3 điểm): Kiểm tra năm nhuận

```python
nam = int(input("Nhập năm: "))

if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(f"{nam} là năm nhuận")
else:
    print(f"{nam} không phải năm nhuận")
```

---

### Bài 7 (3 điểm): Tính tiền điện

```python
so_dien = int(input("Nhập số điện (kWh): "))

if so_dien <= 0:
    tien = 0
elif so_dien <= 50:
    tien = so_dien * 1500
elif so_dien <= 100:
    tien = 50 * 1500 + (so_dien - 50) * 2000
elif so_dien <= 200:
    tien = 50 * 1500 + 50 * 2000 + (so_dien - 100) * 2500
else:
    tien = 50 * 1500 + 50 * 2000 + 100 * 2500 + (so_dien - 200) * 3000

print(f"Tổng tiền điện: {tien:,}đ")
```

---

### Bài 8 (3 điểm): Máy tính đơn giản

```python
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
phep_toan = input("Nhập phép toán (+, -, *, /, %, **): ")

if phep_toan == "+":
    ket_qua = a + b
elif phep_toan == "-":
    ket_qua = a - b
elif phep_toan == "*":
    ket_qua = a * b
elif phep_toan == "/":
    ket_qua = a / b if b != 0 else "Không chia được"
elif phep_toan == "%":
    ket_qua = a % b if b != 0 else "Không chia được"
elif phep_toan == "**":
    ket_qua = a ** b
else:
    ket_qua = "Phép toán không hợp lệ"

print(f"Kết quả: {ket_qua}")
```

---

### Bài 9 (2 điểm): Toán tử 3 ngôi

```python
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

so_lon_hon = a if a > b else b
print(f"Số lớn hơn: {so_lon_hon}")
```

---

### Bài 10 (3 điểm): Kiểm tra tam giác

```python
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra có phải tam giác
if a + b > c and a + c > b and b + c > a:
    print("Đây là tam giác")
    
    # Kiểm tra loại tam giác
    if a == b == c:
        print("Tam giác đều")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")
```

---

## PHẦN II: VÒNG LẶP (Bài 11-20)

### Bài 11 (2 điểm): In số từ 1 đến n

```python
n = int(input("Nhập n: "))

for i in range(1, n + 1):
    print(i, end=" ")
print()
```

---

### Bài 12 (3 điểm): Tính tổng và giai thừa

```python
n = int(input("Nhập n: "))

# Tính tổng
tong = 0
for i in range(1, n + 1):
    tong += i

# Tính giai thừa
giai_thua = 1
for i in range(1, n + 1):
    giai_thua *= i

print(f"Tổng từ 1 đến {n}: {tong}")
print(f"Giai thừa của {n}: {giai_thua}")
```

---

### Bài 13 (3 điểm): Bảng cửu chương

```python
for i in range(2, 10):
    print(f"\nBảng cửu chương {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
```

---

### Bài 14 (3 điểm): Tìm ước số

```python
n = int(input("Nhập số nguyên dương n: "))

print(f"Ước số của {n}:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()
```

---

### Bài 15 (3 điểm): Kiểm tra số nguyên tố

```python
n = int(input("Nhập số nguyên n: "))

if n < 2:
    print(f"{n} không phải số nguyên tố")
else:
    la_nguyen_to = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            la_nguyen_to = False
            break
    
    if la_nguyen_to:
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải số nguyên tố")
```

---

### Bài 16 (3 điểm): Tính tổng số chẵn và lẻ

```python
n = int(input("Nhập n: "))

tong_chan = 0
tong_le = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        tong_chan += i
    else:
        tong_le += i

print(f"Tổng số chẵn từ 1 đến {n}: {tong_chan}")
print(f"Tổng số lẻ từ 1 đến {n}: {tong_le}")
```

---

### Bài 17 (4 điểm): Vẽ hình

```python
n = int(input("Nhập n: "))

for i in range(n):
    for j in range(n):
        print("*", end="")
    print()
```

---

### Bài 18 (3 điểm): Fibonacci

```python
n = int(input("Nhập n: "))

if n <= 0:
    print("Số không hợp lệ")
elif n == 1:
    print("0")
elif n == 2:
    print("0 1")
else:
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    
    for num in fib:
        print(num, end=" ")
    print()
```

---

### Bài 19 (4 điểm): Tìm số hoàn hảo

```python
n = int(input("Nhập n: "))

print(f"Các số hoàn hảo < {n}:")
for num in range(2, n):
    tong_uoc = 0
    for i in range(1, num):
        if num % i == 0:
            tong_uoc += i
    
    if tong_uoc == num:
        print(num, end=" ")
print()
```

---

### Bài 20 (3 điểm): Đếm chữ số

```python
n = int(input("Nhập số nguyên n: "))
n = abs(n)  # Xử lý số âm

# Đếm số lượng chữ số
so_chu_so = 0
tong_chu_so = 0
tich_chu_so = 1
temp = n

if n == 0:
    so_chu_so = 1
    tich_chu_so = 0
else:
    while temp > 0:
        chu_so = temp % 10
        so_chu_so += 1
        tong_chu_so += chu_so
        tich_chu_so *= chu_so
        temp //= 10

print(f"Số lượng chữ số: {so_chu_so}")
print(f"Tổng các chữ số: {tong_chu_so}")
print(f"Tích các chữ số: {tich_chu_so}")
```

---

## PHẦN III: LIST (Bài 21-30)

### Bài 21 (3 điểm): Thao tác List cơ bản

```python
lst = [1, 2, 3, 4, 5]

# Thêm 6 vào cuối
lst.append(6)
print("Sau khi thêm 6:", lst)

# Chèn 0 vào đầu
lst.insert(0, 0)
print("Sau khi chèn 0:", lst)

# Xóa phần tử cuối và in ra
phan_tu_cuoi = lst.pop()
print(f"Phần tử cuối: {phan_tu_cuoi}")
print("Sau khi pop:", lst)

# Đảo ngược
lst.reverse()
print("Sau khi đảo ngược:", lst)
```

---

### Bài 22 (4 điểm): Xử lý List số

```python
input_str = input("Nhập các số (cách nhau dấu cách): ")
numbers = [int(x) for x in input_str.split()]

# Tìm max, min
so_lon_nhat = max(numbers)
so_nho_nhat = min(numbers)

# Tính tổng, trung bình
tong = sum(numbers)
trung_binh = tong / len(numbers) if len(numbers) > 0 else 0

# Đếm số chẵn, lẻ
so_chan = len([x for x in numbers if x % 2 == 0])
so_le = len([x for x in numbers if x % 2 != 0])

# Tạo list chẵn và lẻ
list_chan = [x for x in numbers if x % 2 == 0]
list_le = [x for x in numbers if x % 2 != 0]

print(f"Số lớn nhất: {so_lon_nhat}")
print(f"Số nhỏ nhất: {so_nho_nhat}")
print(f"Tổng: {tong}")
print(f"Trung bình: {trung_binh:.2f}")
print(f"Số lượng số chẵn: {so_chan}")
print(f"Số lượng số lẻ: {so_le}")
print(f"List số chẵn: {list_chan}")
print(f"List số lẻ: {list_le}")
```

---

### Bài 23 (4 điểm): List Comprehension

```python
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Bình phương
binh_phuong = [x ** 2 for x in original]
print("Bình phương:", binh_phuong)

# Chỉ số chẵn
so_chan = [x for x in original if x % 2 == 0]
print("Số chẵn:", so_chan)

# Số nguyên tố
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

so_nguyen_to = [x for x in original if la_nguyen_to(x)]
print("Số nguyên tố:", so_nguyen_to)
```

---

### Bài 24 (4 điểm): Sắp xếp List

```python
input_str = input("Nhập các số (cách nhau dấu cách): ")
numbers = [int(x) for x in input_str.split()]

# Tăng dần
tang_dan = sorted(numbers)
print("Tăng dần:", tang_dan)

# Giảm dần
giam_dan = sorted(numbers, reverse=True)
print("Giảm dần:", giam_dan)

# Theo giá trị tuyệt đối
theo_abs = sorted(numbers, key=abs)
print("Theo giá trị tuyệt đối:", theo_abs)
```

---

### Bài 25 (5 điểm): Tìm kiếm và đếm

```python
lst = [1, 2, 3, 2, 4, 2, 5, 2]

# Vị trí xuất hiện đầu tiên
vi_tri_dau = lst.index(2) if 2 in lst else -1
print(f"Vị trí xuất hiện đầu tiên của 2: {vi_tri_dau}")

# Đếm số lần xuất hiện
so_lan = lst.count(2)
print(f"Số lần xuất hiện của 2: {so_lan}")

# Tất cả vị trí
tat_ca_vi_tri = []
for i in range(len(lst)):
    if lst[i] == 2:
        tat_ca_vi_tri.append(i)
print(f"Tất cả vị trí: {tat_ca_vi_tri}")
```

---

### Bài 26 (4 điểm): List Slice

```python
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3 phần tử đầu
ba_dau = lst[:3]
print("3 phần tử đầu:", ba_dau)

# 3 phần tử cuối
ba_cuoi = lst[-3:]
print("3 phần tử cuối:", ba_cuoi)

# Vị trí chẵn
vi_tri_chan = lst[::2]
print("Vị trí chẵn:", vi_tri_chan)

# Lật ngược
lat_nguoc = lst[::-1]
print("Lật ngược:", lat_nguoc)
```

---

### Bài 27 (5 điểm): Xóa phần tử trùng

```python
input_str = input("Nhập list (cách nhau dấu cách): ")
lst = input_str.split()

# Cách 1: Dùng list
moi = []
for item in lst:
    if item not in moi:
        moi.append(item)

print("List không trùng (giữ thứ tự):", moi)

# Cách 2: Nếu không cần giữ thứ tự
moi2 = list(set(lst))
print("List không trùng (không giữ thứ tự):", moi2)
```

---

### Bài 28 (4 điểm): Tìm phần tử lớn thứ 2

```python
input_str = input("Nhập các số (cách nhau dấu cách): ")
numbers = [int(x) for x in input_str.split()]

# Loại bỏ trùng lặp và sắp xếp
unique_numbers = sorted(set(numbers), reverse=True)

if len(unique_numbers) >= 2:
    print(f"Số lớn thứ 2: {unique_numbers[1]}")
else:
    print("Không có số lớn thứ 2")
```

---

### Bài 29 (5 điểm): Nested List

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Tổng đường chéo chính
tong_cheo = 0
for i in range(len(matrix)):
    tong_cheo += matrix[i][i]

print(f"Tổng đường chéo chính: {tong_cheo}")

# Hoặc
tong_cheo = sum(matrix[i][i] for i in range(len(matrix)))
print(f"Tổng đường chéo chính: {tong_cheo}")
```

---

### Bài 30 (5 điểm): Merge và Sort

```python
list1 = [1, 3, 5]
list2 = [2, 4, 6]

# Merge hai list đã sắp xếp
result = []
i, j = 0, 0

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1

# Thêm phần còn lại
result.extend(list1[i:])
result.extend(list2[j:])

print("List sau khi merge:", result)
```

---

## PHẦN IV: DICTIONARY (Bài 31-35)

### Bài 31 (4 điểm): Dictionary cơ bản

```python
hoc_sinh = {}

hoc_sinh["id"] = input("Nhập ID: ")
hoc_sinh["ten"] = input("Nhập tên: ")
hoc_sinh["tuoi"] = int(input("Nhập tuổi: "))
hoc_sinh["diem"] = float(input("Nhập điểm: "))

print("\nThông tin học sinh:")
for key, value in hoc_sinh.items():
    print(f"{key}: {value}")
```

---

### Bài 32 (5 điểm): Dictionary với nhiều học sinh

```python
danh_sach_hs = []

# Nhập 3 học sinh
for i in range(3):
    print(f"\nHọc sinh {i+1}:")
    hs = {
        "id": input("ID: "),
        "ten": input("Tên: "),
        "diem": float(input("Điểm: "))
    }
    danh_sach_hs.append(hs)

# Tìm học sinh điểm cao nhất
hs_gioi_nhat = max(danh_sach_hs, key=lambda x: x["diem"])
print(f"\nHọc sinh điểm cao nhất: {hs_gioi_nhat['ten']} - {hs_gioi_nhat['diem']}")

# Điểm trung bình
diem_tb = sum(hs["diem"] for hs in danh_sach_hs) / len(danh_sach_hs)
print(f"Điểm trung bình lớp: {diem_tb:.2f}")

# Xếp loại
for hs in danh_sach_hs:
    diem = hs["diem"]
    if diem >= 8:
        hs["xep_loai"] = "Giỏi"
    elif diem >= 6.5:
        hs["xep_loai"] = "Khá"
    elif diem >= 5:
        hs["xep_loai"] = "Trung bình"
    else:
        hs["xep_loai"] = "Yếu"
    
    print(f"{hs['ten']}: {hs['xep_loai']}")
```

---

### Bài 33 (5 điểm): Đếm tần suất

```python
s = input("Nhập chuỗi: ")

# Đếm tần suất
tan_suat = {}
for char in s:
    if char in tan_suat:
        tan_suat[char] += 1
    else:
        tan_suat[char] = 1

# Tìm ký tự xuất hiện nhiều nhất
ky_tu_max = max(tan_suat.items(), key=lambda x: x[1])

print(f"\nKý tự xuất hiện nhiều nhất: '{ky_tu_max[0]}' ({ky_tu_max[1]} lần)")
print("\nTần suất tất cả ký tự:")
for char, count in tan_suat.items():
    print(f"'{char}': {count}")
```

---

### Bài 34 (5 điểm): Dictionary Comprehension

```python
lst = [1, 2, 3, 4, 5]

# Key: value bình phương
dict1 = {x: x**2 for x in lst}
print("Dictionary bình phương:", dict1)

# Chỉ số chẵn với bình phương
dict2 = {x: x**2 for x in lst if x % 2 == 0}
print("Dictionary số chẵn:", dict2)
```

---

### Bài 35 (6 điểm): Quản lý sản phẩm

```python
san_pham = {}

while True:
    print("\n=== QUẢN LÝ SẢN PHẨM ===")
    print("1. Thêm sản phẩm")
    print("2. Tìm sản phẩm")
    print("3. Tính tổng giá trị")
    print("4. Sắp xếp theo giá")
    print("5. Thoát")
    
    choice = input("Chọn chức năng: ")
    
    if choice == "1":
        ten = input("Tên sản phẩm: ")
        gia = float(input("Giá: "))
        so_luong = int(input("Số lượng: "))
        san_pham[ten] = {"gia": gia, "so_luong": so_luong}
        print("Đã thêm sản phẩm!")
    
    elif choice == "2":
        ten = input("Nhập tên sản phẩm cần tìm: ")
        if ten in san_pham:
            print(f"Thông tin: {san_pham[ten]}")
        else:
            print("Không tìm thấy!")
    
    elif choice == "3":
        tong_gia_tri = sum(sp["gia"] * sp["so_luong"] for sp in san_pham.values())
        print(f"Tổng giá trị kho: {tong_gia_tri:,.0f}đ")
    
    elif choice == "4":
        sp_sorted = sorted(san_pham.items(), key=lambda x: x[1]["gia"], reverse=True)
        print("Danh sách sắp xếp theo giá:")
        for ten, info in sp_sorted:
            print(f"{ten}: {info['gia']:,.0f}đ")
    
    elif choice == "5":
        break
```

---

## PHẦN V: STRING (Bài 36-40)

### Bài 36 (3 điểm): Xử lý chuỗi cơ bản

```python
s = input("Nhập chuỗi: ")

# Đếm số từ
so_tu = len(s.split())
print(f"Số từ: {so_tu}")

# Đếm chữ hoa, thường
chữ_hoa = sum(1 for char in s if char.isupper())
chu_thuong = sum(1 for char in s if char.islower())
print(f"Chữ hoa: {chữ_hoa}, Chữ thường: {chu_thuong}")

# Đảo ngược
dao_nguoc = s[::-1]
print(f"Đảo ngược: {dao_nguoc}")
```

---

### Bài 37 (4 điểm): Format String

```python
ten = input("Nhập tên: ")
tuoi = int(input("Nhập tuổi: "))
dia_chi = input("Nhập địa chỉ: ")

# F-string
s1 = f"Tên: {ten}, Tuổi: {tuoi}, Địa chỉ: {dia_chi}"
print("F-string:", s1)

# % formatting
s2 = "Tên: %s, Tuổi: %d, Địa chỉ: %s" % (ten, tuoi, dia_chi)
print("% formatting:", s2)

# .format()
s3 = "Tên: {}, Tuổi: {}, Địa chỉ: {}".format(ten, tuoi, dia_chi)
print(".format():", s3)
```

---

### Bài 38 (5 điểm): Xử lý chuỗi nâng cao

```python
s = input("Nhập chuỗi: ")

# Loại bỏ khoảng trắng thừa
loai_bo = " ".join(s.split())
print(f"Loại bỏ khoảng thừa: '{loai_bo}'")

# Title case
title = s.title()
print(f"Title case: {title}")

# Đếm số câu
so_cau = sum(1 for char in s if char in '.!?')
print(f"Số câu: {so_cau}")

# Thay thế
thay_the = s.replace("Python", "Java")
print(f"Thay thế: {thay_the}")
```

---

### Bài 39 (5 điểm): Palindrome

```python
s = input("Nhập chuỗi: ")

# Loại bỏ khoảng trắng và chuyển về chữ thường
s_clean = s.replace(" ", "").lower()

# Kiểm tra palindrome
la_palindrome = s_clean == s_clean[::-1]

if la_palindrome:
    print(f"'{s}' là palindrome")
else:
    print(f"'{s}' không phải palindrome")
```

---

### Bài 40 (6 điểm): Đếm từ trong văn bản

```python
van_ban = input("Nhập văn bản: ")

# Tách thành từ
tu_list = van_ban.lower().split()

# Đếm tần suất
tan_suat = {}
for tu in tu_list:
    tan_suat[tu] = tan_suat.get(tu, 0) + 1

print("\nTần suất từ:")
for tu, count in tan_suat.items():
    print(f"'{tu}': {count}")

# Từ dài nhất, ngắn nhất
tu_dai_nhat = max(tu_list, key=len)
tu_ngan_nhat = min(tu_list, key=len)

print(f"\nTừ dài nhất: '{tu_dai_nhat}' ({len(tu_dai_nhat)} ký tự)")
print(f"Từ ngắn nhất: '{tu_ngan_nhat}' ({len(tu_ngan_nhat)} ký tự)")
```

---

## PHẦN VI: HÀM (Bài 41-45)

### Bài 41 (4 điểm): Hàm cơ bản

```python
def tinh_chu_vi_hinh_chu_nhat(a, b):
    return 2 * (a + b)

def tinh_dien_tich_hinh_chu_nhat(a, b):
    return a * b

# Test
a = float(input("Nhập chiều dài: "))
b = float(input("Nhập chiều rộng: "))

chu_vi = tinh_chu_vi_hinh_chu_nhat(a, b)
dien_tich = tinh_dien_tich_hinh_chu_nhat(a, b)

print(f"Chu vi: {chu_vi}")
print(f"Diện tích: {dien_tich}")
```

---

### Bài 42 (5 điểm): Hàm với *args và **kwargs

```python
def tinh_tong(*args):
    return sum(args)

def hien_thi_thong_tin(**kwargs):
    print("Thông tin:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

# Test
tong = tinh_tong(1, 2, 3, 4, 5)
print(f"Tổng: {tong}")

hien_thi_thong_tin(ten="Nguyễn Văn A", tuoi=20, dia_chi="Hà Nội")
```

---

### Bài 43 (6 điểm): Hàm kiểm tra số nguyên tố (nâng cao)

```python
def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def in_so_nguyen_to_tu_m_den_n(m, n):
    so_nguyen_to = []
    for num in range(m, n + 1):
        if kiem_tra_so_nguyen_to(num):
            so_nguyen_to.append(num)
    return so_nguyen_to

# Test
m = int(input("Nhập m: "))
n = int(input("Nhập n: "))

ds_nguyen_to = in_so_nguyen_to_tu_m_den_n(m, n)
print(f"Số nguyên tố từ {m} đến {n}: {ds_nguyen_to}")
```

---

### Bài 44 (5 điểm): Hàm đệ quy - Giai thừa

```python
# Đệ quy
def giai_thua_de_quy(n):
    if n <= 1:
        return 1
    return n * giai_thua_de_quy(n - 1)

# Không đệ quy
def giai_thua_khong_de_quy(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua

# Test
n = int(input("Nhập n: "))
print(f"Giai thừa (đệ quy): {giai_thua_de_quy(n)}")
print(f"Giai thừa (không đệ quy): {giai_thua_khong_de_quy(n)}")
```

---

### Bài 45 (6 điểm): Hàm đệ quy - Fibonacci

```python
# Đệ quy (chậm)
def fib_de_quy(n):
    if n <= 1:
        return n
    return fib_de_quy(n - 1) + fib_de_quy(n - 2)

# Không đệ quy (nhanh)
def fib_khong_de_quy(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Test
n = int(input("Nhập n: "))
print(f"Fibonacci thứ {n} (đệ quy): {fib_de_quy(n)}")
print(f"Fibonacci thứ {n} (không đệ quy): {fib_khong_de_quy(n)}")
```

---

## PHẦN VII: NÂNG CAO (Bài 46-50)

### Bài 46 (7 điểm): Lambda và Map/Filter

```python
from math import ceil

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Bình phương
binh_phuong = list(map(lambda x: x ** 2, lst))
print("Bình phương:", binh_phuong)

# Lọc số chẵn
so_chan = list(filter(lambda x: x % 2 == 0, lst))
print("Số chẵn:", so_chan)

# Kiểm tra số nguyên tố
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

so_nguyen_to = list(map(lambda x: la_nguyen_to(x), lst))
print("Kiểm tra nguyên tố (True/False):", so_nguyen_to)
```

---

### Bài 47 (8 điểm): Binary Search

```python
def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    
    while l <= r:
        m = (l + r) // 2
        
        if arr[m] == x:
            return m
        elif arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    
    return -1

# Test
arr = [1, 3, 5, 7, 9, 11, 13, 15]
x = int(input("Nhập số cần tìm: "))

vi_tri = binary_search(arr, x)
if vi_tri != -1:
    print(f"Tìm thấy tại vị trí: {vi_tri}")
else:
    print("Không tìm thấy")
```

---

### Bài 48 (8 điểm): Set Operations

```python
lop_a = {1, 2, 3, 4, 5}
lop_b = {4, 5, 6, 7, 8}

print("Lớp A:", lop_a)
print("Lớp B:", lop_b)

# Chỉ học lớp A
chi_lop_a = lop_a - lop_b
print(f"\nChỉ học lớp A: {chi_lop_a}")

# Chỉ học lớp B
chi_lop_b = lop_b - lop_a
print(f"Chỉ học lớp B: {chi_lop_b}")

# Học cả 2 lớp
ca_hai_lop = lop_a & lop_b
print(f"Học cả 2 lớp: {ca_hai_lop}")

# Tổng số học sinh
tong_hoc_sinh = lop_a | lop_b
print(f"Tổng số học sinh: {tong_hoc_sinh}")
```

---

### Bài 49 (8 điểm): Scope - Global và Nonlocal

```python
count = 0  # Global

def tang_count():
    global count
    count += 1
    print(f"Count trong hàm: {count}")
    
    def ham_con():
        nonlocal count  # Không thể dùng nonlocal với global
        # Trong trường hợp này, ta vẫn dùng global
        # hoặc tạo biến local khác
    
    ham_con()

print(f"Count ban đầu: {count}")
tang_count()
print(f"Count sau khi gọi hàm: {count}")

# Ví dụ với nonlocal
def ham_cha():
    x = 10  # Enclosing scope
    
    def ham_con():
        nonlocal x
        x = 20
        print(f"x trong ham_con: {x}")
    
    print(f"x trong ham_cha (trước): {x}")
    ham_con()
    print(f"x trong ham_cha (sau): {x}")

ham_cha()
```

---

### Bài 50 (10 điểm): Dự án nhỏ - Quản lý Thư viện

```python
thu_vien = []

def them_sach():
    sach = {
        "id": input("ID sách: "),
        "ten": input("Tên sách: "),
        "tac_gia": input("Tác giả: "),
        "nam_xb": input("Năm xuất bản: "),
        "trang_thai": "chưa mượn"
    }
    thu_vien.append(sach)
    print("Đã thêm sách!")

def tim_sach():
    ten = input("Nhập tên sách: ")
    ket_qua = [s for s in thu_vien if ten.lower() in s["ten"].lower()]
    
    if ket_qua:
        for sach in ket_qua:
            print(f"ID: {sach['id']}, Tên: {sach['ten']}, Trạng thái: {sach['trang_thai']}")
    else:
        print("Không tìm thấy!")

def muon_sach():
    id_sach = input("Nhập ID sách cần mượn: ")
    for sach in thu_vien:
        if sach["id"] == id_sach:
            if sach["trang_thai"] == "chưa mượn":
                sach["trang_thai"] = "đã mượn"
                print("Đã mượn sách!")
            else:
                print("Sách đã được mượn!")
            return
    print("Không tìm thấy sách!")

def tra_sach():
    id_sach = input("Nhập ID sách cần trả: ")
    for sach in thu_vien:
        if sach["id"] == id_sach:
            if sach["trang_thai"] == "đã mượn":
                sach["trang_thai"] = "chưa mượn"
                print("Đã trả sách!")
            else:
                print("Sách chưa được mượn!")
            return
    print("Không tìm thấy sách!")

def danh_sach_dang_muon():
    sach_muon = [s for s in thu_vien if s["trang_thai"] == "đã mượn"]
    if sach_muon:
        print("\nDanh sách sách đang mượn:")
        for sach in sach_muon:
            print(f"- {sach['ten']} (ID: {sach['id']})")
    else:
        print("Không có sách nào đang mượn")

def thong_ke():
    tong_so = len(thu_vien)
    so_da_muon = len([s for s in thu_vien if s["trang_thai"] == "đã mượn"])
    so_con_lai = tong_so - so_da_muon
    
    print(f"\n=== THỐNG KÊ ===")
    print(f"Tổng số sách: {tong_so}")
    print(f"Số sách đã mượn: {so_da_muon}")
    print(f"Số sách còn lại: {so_con_lai}")

# Chương trình chính
while True:
    print("\n=== QUẢN LÝ THƯ VIỆN ===")
    print("1. Thêm sách mới")
    print("2. Tìm sách theo tên")
    print("3. Mượn sách")
    print("4. Trả sách")
    print("5. Danh sách sách đang mượn")
    print("6. Thống kê")
    print("7. Thoát")
    
    choice = input("Chọn chức năng: ")
    
    if choice == "1":
        them_sach()
    elif choice == "2":
        tim_sach()
    elif choice == "3":
        muon_sach()
    elif choice == "4":
        tra_sach()
    elif choice == "5":
        danh_sach_dang_muon()
    elif choice == "6":
        thong_ke()
    elif choice == "7":
        print("Cảm ơn đã sử dụng!")
        break
    else:
        print("Lựa chọn không hợp lệ!")
```

---

## TỔNG KẾT

Đã hoàn thành 50 bài tập với đáp án chi tiết!

**Mẹo làm bài:**
1. Đọc kỹ yêu cầu
2. Phân tích bài toán
3. Viết code từng bước
4. Test với nhiều trường hợp
5. Refactor code cho đẹp

**Chúc các em học tốt!**
