# ĐÁP ÁN ĐỀ KIỂM TRA FINAL PYTHON

---

## PHẦN I: LÝ THUYẾT TỔNG HỢP (30 điểm)

### Câu 1 (6 điểm): Phân tích Code

**Đáp án:**

**a) Kết quả:** `41`
- `x=5` (tham số đầu tiên)
- `*args` nhận `(1, 2, 3)` → `sum(args) = 6`
- `**kwargs` nhận `{"a": 10, "b": 20}` → `sum(kwargs.values()) = 30`
- Kết quả: `5 + 6 + 30 = 41`

**b) Kết quả:** `1 100`
- `b = a[:]` tạo một bản sao mới của list a (shallow copy)
- Thay đổi `b[0]` không ảnh hưởng đến `a[0]`
- `a[0]` vẫn là `1`, `b[0]` là `100`

**c) Kết quả:** `programming`
- `words = ["Python", "Programming"]`
- List comprehension lọc từ có độ dài > 5: `["Programming"]`
- Chuyển về lowercase và join: `"programming"`

**d) Kết quả:** `{'a': 1, 'c': 9}`
- Dictionary comprehension lọc các value lẻ (`v % 2 == 1`)
- `1 % 2 = 1` → giữ lại, bình phương = 1
- `2 % 2 = 0` → loại bỏ
- `3 % 2 = 1` → giữ lại, bình phương = 9
- Kết quả: `{"a": 1, "c": 9}`

**e) Kết quả:**
```
30
30
```
- `global x` trong `test()` cho phép truy cập biến global `x = 10`
- `nonlocal x` trong `inner()` tìm biến `x` ở hàm cha (`test()`)
- `inner()` gán `x = 30`, ảnh hưởng đến biến trong `test()`
- Cả 2 lần print đều in `30` vì cùng một biến

**f) Kết quả:** `[9, 5, 4, 3, 1, 1]`
- Hàm `sort()` với `key=lambda x: -x if x % 2 == 0 else x`
- Số chẵn: `key = -x` (âm) → sắp xếp đầu
- Số lẻ: `key = x` (dương) → sắp xếp sau
- Kết quả: chẵn giảm dần trước, lẻ tăng dần sau

---

### Câu 2 (6 điểm): So sánh và Giải thích

**Đáp án:**

#### 1. List, Tuple, Set, Dictionary (3 điểm)

| Tiêu chí | List | Tuple | Set | Dictionary |
|----------|------|-------|-----|------------|
| **Cú pháp** | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` | `{"a": 1}` |
| **Tính chất** | Mutable | Immutable | Mutable, Unique | Mutable |
| **Thứ tự** | Có thứ tự | Có thứ tự | Không thứ tự | Có thứ tự (Python 3.7+) |
| **Truy cập** | Index | Index | Không có index | Key |
| **Trùng lặp** | Cho phép | Cho phép | Không cho phép | Key unique |
| **Khi nào dùng** | Dữ liệu thay đổi | Dữ liệu cố định | Tập hợp không trùng | Key-value mapping |

**Ví dụ:**
```python
# List - có thể thay đổi
lst = [1, 2, 3]
lst.append(4)  # [1, 2, 3, 4]

# Tuple - không thể thay đổi
tup = (1, 2, 3)
# tup[0] = 10  # Lỗi!

# Set - không trùng lặp, không thứ tự
s = {1, 2, 2, 3}  # {1, 2, 3}

# Dictionary - key-value
d = {"a": 1, "b": 2}
```

#### 2. `sort()` vs `sorted()` (1.5 điểm)

**`sort()`:**
- Phương thức của list
- Thay đổi list gốc (in-place)
- Không trả về giá trị (`None`)
- Chỉ dùng với list

**`sorted()`:**
- Hàm built-in
- Không thay đổi list gốc
- Trả về list mới đã sắp xếp
- Dùng được với nhiều iterable (list, tuple, string, dict)

**Ví dụ:**
```python
lst = [3, 1, 2]
lst.sort()  # lst = [1, 2, 3], không trả về gì

lst = [3, 1, 2]
new_lst = sorted(lst)  # new_lst = [1, 2, 3], lst = [3, 1, 2]
```

#### 3. `global` vs `nonlocal` (1.5 điểm)

**`global`:**
- Sử dụng biến global (phạm vi file)
- Dùng khi muốn thay đổi biến global trong hàm
- Tìm biến ở phạm vi global

**`nonlocal`:**
- Sử dụng biến ở hàm cha (enclosing scope)
- Chỉ dùng trong hàm lồng nhau
- Tìm biến ở các hàm bao ngoài (không phải global)

**Ví dụ:**
```python
x = 10  # global

def outer():
    y = 20  # enclosing
    
    def inner():
        global x
        nonlocal y
        x = 100  # thay đổi global x
        y = 200  # thay đổi enclosing y
    
    inner()
    print(y)  # 200

outer()
print(x)  # 100
```

---

### Câu 3 (6 điểm): Hàm và Lambda

**Đáp án:**

#### 1. Hàm thông thường vs Lambda (2 điểm)

**Hàm thông thường (`def`):**
- Có tên hàm
- Có thể chứa nhiều câu lệnh
- Có thể có return hoặc không
- Có thể có docstring
- Phù hợp cho logic phức tạp

**Lambda function:**
- Hàm vô danh (không có tên)
- Chỉ chứa một biểu thức
- Tự động return
- Phù hợp cho hàm đơn giản, ngắn gọn

**Khi nào dùng Lambda:**
- Hàm ngắn gọn, chỉ một dòng
- Dùng làm tham số cho các hàm khác (map, filter, sort)
- Không cần tái sử dụng

**Ví dụ:**
```python
# Hàm thông thường
def square(n):
    return n ** 2

# Lambda tương đương
square = lambda n: n ** 2
```

#### 2. Map và Filter với Lambda (2 điểm)

**Ví dụ:**

```python
# Map - áp dụng hàm cho mỗi phần tử
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
# Kết quả: [1, 4, 9, 16, 25]

# Filter - lọc phần tử thỏa điều kiện
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Kết quả: [2, 4]
```

#### 3. Nested Function (2 điểm)

**Khái niệm:**
- Hàm được định nghĩa bên trong một hàm khác
- Có thể truy cập biến của hàm cha (closure)
- Giúp tổ chức code, tạo scope riêng

**Ví dụ:**
```python
def outer(x):
    def inner(y):
        return x + y  # Truy cập biến x của hàm cha
    return inner

add_5 = outer(5)
result = add_5(10)  # 15
```

---

### Câu 4 (6 điểm): Đệ quy và Thuật toán

**Đáp án:**

#### 1. Đệ quy (2 điểm)

**Khái niệm:**
- Hàm gọi lại chính nó
- Giải quyết bài toán lớn bằng cách chia thành các bài toán nhỏ tương tự
- Cần có điều kiện dừng để tránh lặp vô hạn

**Thành phần cần có:**
1. **Điều kiện dừng (base case):** Trường hợp đơn giản nhất, không cần gọi lại
2. **Công thức truy hồi (recursive case):** Cách chia bài toán thành bài toán nhỏ hơn

**Ví dụ:**
```python
def factorial(n):
    if n <= 1:  # Điều kiện dừng
        return 1
    return n * factorial(n - 1)  # Công thức truy hồi
```

#### 2. Binary Search (2 điểm)

**Ý tưởng:**
- Chia đôi mảng tìm kiếm mỗi lần
- So sánh phần tử ở giữa với giá trị cần tìm
- Loại bỏ một nửa mảng không chứa giá trị
- Lặp lại cho đến khi tìm thấy hoặc hết mảng

**Khi nào dùng:**
- Mảng đã được sắp xếp (tăng dần hoặc giảm dần)
- Cần tìm kiếm nhanh trong tập dữ liệu lớn
- Độ phức tạp O(log n)

#### 3. Linear Search vs Binary Search (2 điểm)

| Tiêu chí | Linear Search | Binary Search |
|----------|---------------|---------------|
| **Độ phức tạp** | O(n) | O(log n) |
| **Yêu cầu** | Không cần sắp xếp | Phải sắp xếp trước |
| **Cách làm** | Duyệt tuần tự | Chia đôi mảng |
| **Khi nào dùng** | Mảng nhỏ, chưa sắp xếp | Mảng lớn, đã sắp xếp |
| **Tốc độ** | Chậm hơn | Nhanh hơn |

---

### Câu 5 (6 điểm): String và Collections

**Đáp án:**

#### 1. 3 cách format string (2 điểm)

```python
name = "Thảo"
age = 20

# Cách 1: f-string (khuyên dùng)
s1 = f"Tên: {name}, Tuổi: {age}"

# Cách 2: % formatting
s2 = "Tên: %s, Tuổi: %d" % (name, age)

# Cách 3: .format()
s3 = "Tên: {}, Tuổi: {}".format(name, age)
# hoặc
s3 = "Tên: {0}, Tuổi: {1}".format(name, age)
```

#### 2. `append()`, `extend()`, `insert()` (2 điểm)

**`append(x)`:**
- Thêm phần tử `x` vào cuối list
- Nếu x là list, thêm cả list như một phần tử (nested)

**`extend(iterable)`:**
- Thêm từng phần tử của iterable vào cuối list
- Mở rộng list bằng cách thêm các phần tử

**`insert(index, x)`:**
- Chèn phần tử `x` vào vị trí `index`
- Các phần tử sau đó dịch sang phải

**Ví dụ:**
```python
lst = [1, 2, 3]
lst.append([4, 5])  # [1, 2, 3, [4, 5]]

lst = [1, 2, 3]
lst.extend([4, 5])  # [1, 2, 3, 4, 5]

lst = [1, 2, 3]
lst.insert(1, 10)  # [1, 10, 2, 3]
```

#### 3. `pop()` vs `get()` trong Dictionary (2 điểm)

**`dict.pop(key, default)`:**
- Xóa và trả về giá trị của key
- Nếu key không tồn tại → lỗi KeyError (hoặc trả về default nếu có)
- Thay đổi dictionary

**`dict.get(key, default)`:**
- Trả về giá trị của key
- Nếu key không tồn tại → trả về None (hoặc default nếu có)
- Không thay đổi dictionary

**Ví dụ:**
```python
d = {"a": 1, "b": 2}

value1 = d.pop("a")  # value1 = 1, d = {"b": 2}
value2 = d.get("c", 0)  # value2 = 0, d = {"b": 2}
```

---

## PHẦN II: BÀI TẬP THỰC HÀNH (70 điểm)

### Câu 6 (15 điểm): Xử lý Dữ liệu Phức tạp

**Đáp án:**

```python
# Khởi tạo danh sách sản phẩm
san_pham = []

# Nhập thông tin sản phẩm
n = int(input("Nhập số lượng sản phẩm: "))
for i in range(n):
    print(f"\nSản phẩm {i+1}:")
    sp = {
        "ten": input("Tên sản phẩm: "),
        "gia": float(input("Giá: ")),
        "loai": input("Loại: "),
        "so_luong": int(input("Số lượng: "))
    }
    san_pham.append(sp)

# Hoặc khởi tạo sẵn
# san_pham = [
#     {"ten": "Laptop", "gia": 15000000, "loai": "Điện tử", "so_luong": 5},
#     {"ten": "Bút", "gia": 5000, "loai": "Văn phòng phẩm", "so_luong": 100},
#     {"ten": "Sách", "gia": 50000, "loai": "Giáo dục", "so_luong": 8},
#     {"ten": "Máy tính", "gia": 20000000, "loai": "Điện tử", "so_luong": 3},
#     {"ten": "Vở", "gia": 10000, "loai": "Văn phòng phẩm", "so_luong": 50}
# ]

# 1. Tìm sản phẩm có giá cao nhất và thấp nhất
sp_dat_nhat = max(san_pham, key=lambda x: x["gia"])
sp_re_nhat = min(san_pham, key=lambda x: x["gia"])

print(f"\nSản phẩm đắt nhất: {sp_dat_nhat['ten']} - {sp_dat_nhat['gia']:,.0f}đ")
print(f"Sản phẩm rẻ nhất: {sp_re_nhat['ten']} - {sp_re_nhat['gia']:,.0f}đ")

# 2. Tính tổng giá trị
tong_gia_tri = sum(sp["gia"] * sp["so_luong"] for sp in san_pham)
print(f"\nTổng giá trị tất cả sản phẩm: {tong_gia_tri:,.0f}đ")

# 3. Lọc sản phẩm sắp hết (số lượng < 10)
sp_sap_het = [sp for sp in san_pham if sp["so_luong"] < 10]
print("\nSản phẩm sắp hết (< 10):")
for sp in sp_sap_het:
    print(f"- {sp['ten']}: {sp['so_luong']}")

# 4. Sắp xếp theo giá giảm dần, cùng giá thì theo tên
san_pham.sort(key=lambda x: (-x["gia"], x["ten"]))
print("\nDanh sách sắp xếp theo giá giảm dần:")
for sp in san_pham:
    print(f"- {sp['ten']}: {sp['gia']:,.0f}đ")

# 5. Tạo dictionary theo loại
sp_theo_loai = {}
for sp in san_pham:
    loai = sp["loai"]
    if loai not in sp_theo_loai:
        sp_theo_loai[loai] = []
    sp_theo_loai[loai].append(sp)

print("\nSản phẩm theo loại:")
for loai, danh_sach in sp_theo_loai.items():
    print(f"\n{loai}:")
    for sp in danh_sach:
        print(f"  - {sp['ten']}: {sp['gia']:,.0f}đ")
```

---

### Câu 7 (15 điểm): Xử lý Chuỗi và Text

**Đáp án:**

```python
# Nhập văn bản
print("Nhập văn bản (kết thúc bằng dòng trống):")
lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)

van_ban = " ".join(lines)

# 1. Đếm số từ và số câu
tu_list = van_ban.split()
so_tu = len(tu_list)

# Đếm số câu (kết thúc bằng . ! ?)
so_cau = 0
for char in van_ban:
    if char in '.!?':
        so_cau += 1

print(f"\nSố từ: {so_tu}")
print(f"Số câu: {so_cau}")

# 2. Đếm từ có độ dài > 5
tu_dai = [tu for tu in tu_list if len(tu) > 5]
print(f"\nTừ dài (>5 ký tự): {tu_dai}")

# 3. Đếm tần suất từ (không phân biệt hoa thường)
tan_suat = {}
for tu in tu_list:
    tu_lower = tu.lower()
    tan_suat[tu_lower] = tan_suat.get(tu_lower, 0) + 1

# Tìm từ xuất hiện nhiều nhất
tu_max = max(tan_suat.items(), key=lambda x: x[1])
print(f"\nTừ xuất hiện nhiều nhất: '{tu_max[0]}' ({tu_max[1]} lần)")

# 4. Danh sách từ duy nhất
tu_duy_nhat = list(set(tu.lower() for tu in tu_list))
print(f"\nDanh sách từ duy nhất: {tu_duy_nhat}")

# 5. Đảo ngược câu đầu tiên
if lines:
    cau_dau = lines[0]
    tu_cau_dau = cau_dau.split()
    cau_dao = " ".join(reversed(tu_cau_dau))
    print(f"\nCâu đầu đảo ngược: {cau_dao}")
```

---

### Câu 8 (15 điểm): Hàm Đệ quy

**Đáp án:**

```python
# 1. Tính giai thừa
def tinh_giai_thua(n):
    """
    Tính giai thừa của n sử dụng đệ quy
    Điều kiện dừng: n <= 1
    Công thức truy hồi: n * factorial(n-1)
    """
    if n <= 1:
        return 1
    return n * tinh_giai_thua(n - 1)


# 2. Tính tổng list
def tinh_tong_list(arr):
    """
    Tính tổng các phần tử trong list sử dụng đệ quy
    Điều kiện dừng: list rỗng
    Công thức truy hồi: phần tử đầu + tổng phần còn lại
    """
    if len(arr) == 0:
        return 0
    return arr[0] + tinh_tong_list(arr[1:])


# 3. Đảo ngược chuỗi
def dao_nguoc_chuoi(s):
    """
    Đảo ngược chuỗi sử dụng đệ quy
    Điều kiện dừng: chuỗi có <= 1 ký tự
    Công thức truy hồi: đảo phần còn lại + ký tự đầu
    """
    if len(s) <= 1:
        return s
    return dao_nguoc_chuoi(s[1:]) + s[0]


# Chương trình chính
if __name__ == '__main__':
    # Test giai thừa
    n = int(input("Nhập n: "))
    ket_qua = tinh_giai_thua(n)
    print(f"{n}! = {ket_qua}")
    
    # Test tổng list
    input_str = input("\nNhập list (cách nhau dấu cách): ")
    arr = [int(x) for x in input_str.split()]
    tong = tinh_tong_list(arr)
    print(f"Tổng: {tong}")
    
    # Test đảo ngược chuỗi
    s = input("\nNhập chuỗi: ")
    dao = dao_nguoc_chuoi(s)
    print(f"Chuỗi đảo ngược: {dao}")
```

---

### Câu 9 (15 điểm): Thuật toán Tìm kiếm và Sắp xếp

**Đáp án:**

```python
# Nhập list số nguyên
input_str = input("Nhập các số (cách nhau dấu cách): ")
arr = [int(x) for x in input_str.split()]

# Sắp xếp
arr_sorted = sorted(arr)
print(f"\nList sau khi sắp xếp: {arr_sorted}")


# Binary Search
def binary_search(arr, x):
    """
    Tìm x trong mảng đã sắp xếp sử dụng Binary Search
    Trả về index nếu tìm thấy, -1 nếu không tìm thấy
    """
    l, r = 0, len(arr) - 1
    so_lan_so_sanh = 0
    
    while l <= r:
        so_lan_so_sanh += 1
        m = (l + r) // 2
        
        if arr[m] == x:
            return m, so_lan_so_sanh
        elif arr[m] < x:
            l = m + 1
        else:
            r = m - 1
    
    return -1, so_lan_so_sanh


# Linear Search
def linear_search(arr, x):
    """
    Tìm x trong mảng sử dụng Linear Search
    Trả về index đầu tiên tìm thấy, -1 nếu không tìm thấy
    """
    so_lan_so_sanh = 0
    for i in range(len(arr)):
        so_lan_so_sanh += 1
        if arr[i] == x:
            return i, so_lan_so_sanh
    
    return -1, so_lan_so_sanh


# Chương trình chính
x = int(input("\nNhập số cần tìm: "))

# Binary Search
idx_binary, count_binary = binary_search(arr_sorted, x)
if idx_binary != -1:
    print(f"Binary Search: Tìm thấy tại vị trí {idx_binary} (số lần so sánh: {count_binary})")
else:
    print(f"Binary Search: Không tìm thấy (số lần so sánh: {count_binary})")

# Linear Search
idx_linear, count_linear = linear_search(arr_sorted, x)
if idx_linear != -1:
    print(f"Linear Search: Tìm thấy tại vị trí {idx_linear} (số lần so sánh: {count_linear})")
else:
    print(f"Linear Search: Không tìm thấy (số lần so sánh: {count_linear})")
```

---

### Câu 10 (10 điểm): Lambda và Higher-order Functions

**Đáp án:**

```python
from math import ceil

# List điểm số
diem = [8.5, 7.0, 9.5, 6.5, 8.0, 7.5, 9.0]
print(f"Điểm gốc: {diem}")

# 1. Làm tròn lên bằng map và lambda
diem_tron = list(map(lambda x: ceil(x), diem))
print(f"Điểm làm tròn: {diem_tron}")

# 2. Lọc điểm >= 8.0
diem_cao = list(filter(lambda x: x >= 8.0, diem))
print(f"Điểm >= 8.0: {diem_cao}")

# 3. Tính điểm trung bình của điểm >= 8.0
if len(diem_cao) > 0:
    diem_tb = sum(diem_cao) / len(diem_cao)
    print(f"Điểm trung bình (>=8.0): {diem_tb:.2f}")
else:
    print("Không có điểm >= 8.0")

# 4. Tìm điểm cao nhất và thấp nhất
diem_cao_nhat = max(diem, key=lambda x: x)
diem_thap_nhat = min(diem, key=lambda x: x)
print(f"Điểm cao nhất: {diem_cao_nhat}, Điểm thấp nhất: {diem_thap_nhat}")

# 5. List tên và lấy chữ cái đầu
ten = ["Nguyễn Văn A", "Trần Thị B", "Lê Văn C"]
chu_cai_dau = list(map(lambda x: x[0], ten))
print(f"\nChữ cái đầu: {chu_cai_dau}")
```

---

## PHẦN III: BÀI TẬP NÂNG CAO (20 điểm)

### Câu 11 (10 điểm): Quản lý Học sinh với Dictionary Nested

**Đáp án:**

```python
# Tạo dictionary lớp học
lop_hoc = {}

# Nhập thông tin lớp
lop_hoc["ten_lop"] = input("Nhập tên lớp: ")

# Nhập danh sách học sinh
danh_sach = []
n = int(input("Nhập số lượng học sinh: "))

for i in range(n):
    print(f"\nHọc sinh {i+1}:")
    hs = {
        "id": i + 1,
        "ho_ten": input("Họ tên: "),
        "diem_toan": float(input("Điểm Toán: ")),
        "diem_ly": float(input("Điểm Lý: ")),
        "diem_hoa": float(input("Điểm Hóa: "))
    }
    # Tính điểm trung bình
    hs["diem_tb"] = round((hs["diem_toan"] + hs["diem_ly"] + hs["diem_hoa"]) / 3, 2)
    
    # Xếp loại
    if hs["diem_tb"] >= 8.0:
        hs["xep_loai"] = "Giỏi"
    elif hs["diem_tb"] >= 6.5:
        hs["xep_loai"] = "Khá"
    elif hs["diem_tb"] >= 5.0:
        hs["xep_loai"] = "Trung bình"
    else:
        hs["xep_loai"] = "Yếu"
    
    danh_sach.append(hs)

lop_hoc["si_so"] = n
lop_hoc["danh_sach_hoc_sinh"] = danh_sach

# In thông tin lớp
print("\n=== THÔNG TIN LỚP HỌC ===")
print(f"Tên lớp: {lop_hoc['ten_lop']}")
print(f"Sĩ số: {lop_hoc['si_so']}")

# In bảng điểm
print("\n=== BẢNG ĐIỂM ===")
print("ID | Họ tên | Toán | Lý | Hóa | TB | Xếp loại")
for hs in danh_sach:
    print(f"{hs['id']} | {hs['ho_ten']} | {hs['diem_toan']} | {hs['diem_ly']} | {hs['diem_hoa']} | {hs['diem_tb']} | {hs['xep_loai']}")

# Tìm học sinh giỏi nhất
hs_gioi_nhat = max(danh_sach, key=lambda x: x["diem_tb"])
print(f"\nHọc sinh giỏi nhất: {hs_gioi_nhat['ho_ten']} ({hs_gioi_nhat['diem_tb']})")

# Sắp xếp theo điểm TB giảm dần
danh_sach.sort(key=lambda x: -x["diem_tb"])
print("\nDanh sách sắp xếp theo điểm TB giảm dần:")
for hs in danh_sach:
    print(f"- {hs['ho_ten']}: {hs['diem_tb']}")

# Thống kê
thong_ke = {
    "Giỏi": len([hs for hs in danh_sach if hs["xep_loai"] == "Giỏi"]),
    "Khá": len([hs for hs in danh_sach if hs["xep_loai"] == "Khá"]),
    "Trung bình": len([hs for hs in danh_sach if hs["xep_loai"] == "Trung bình"]),
    "Yếu": len([hs for hs in danh_sach if hs["xep_loai"] == "Yếu"])
}

print("\nThống kê:")
for loai, so_luong in thong_ke.items():
    print(f"- {loai}: {so_luong}")
```

---

### Câu 12 (10 điểm): Xử lý Tập hợp (Set Operations)

**Đáp án:**

```python
# Khởi tạo set học sinh đăng ký môn học
toan = {1, 2, 3, 4}
ly = {2, 3, 5, 6}
hoa = {3, 4, 6, 7}

print("Học sinh đăng ký Toán:", toan)
print("Học sinh đăng ký Lý:", ly)
print("Học sinh đăng ký Hóa:", hoa)

# Hoặc nhập từ bàn phím
# print("Nhập ID học sinh đăng ký Toán (cách nhau dấu cách):")
# toan = set(map(int, input().split()))
# print("Nhập ID học sinh đăng ký Lý (cách nhau dấu cách):")
# ly = set(map(int, input().split()))
# print("Nhập ID học sinh đăng ký Hóa (cách nhau dấu cách):")
# hoa = set(map(int, input().split()))

# 1. Học sinh đăng ký cả 3 môn (intersection)
ca_ba_mon = toan & ly & hoa
print(f"\nHọc sinh đăng ký cả 3 môn: {ca_ba_mon}")

# 2. Học sinh đăng ký ít nhất 1 môn (union)
it_nhat_mot_mon = toan | ly | hoa
print(f"Học sinh đăng ký ít nhất 1 môn: {it_nhat_mot_mon}")

# 3. Học sinh chỉ đăng ký Toán (difference)
chi_toan = toan - ly - hoa
print(f"Học sinh chỉ đăng ký Toán: {chi_toan}")

# 4. Học sinh (Toán hoặc Lý) và không Hóa
toan_hoac_ly = toan | ly
khong_hoa = toan_hoac_ly - hoa
print(f"Học sinh (Toán hoặc Lý) và không Hóa: {khong_hoa}")

# 5. Kiểm tra có học sinh không đăng ký môn nào
# Giả sử tổng số học sinh là 10
tong_hoc_sinh = {i for i in range(1, 11)}
hoc_sinh_co_dang_ky = toan | ly | hoa
hoc_sinh_khong_dang_ky = tong_hoc_sinh - hoc_sinh_co_dang_ky
co_hoc_sinh_khong_dang_ky = len(hoc_sinh_khong_dang_ky) > 0

print(f"\nCó học sinh không đăng ký môn nào: {co_hoc_sinh_khong_dang_ky}")
if hoc_sinh_khong_dang_ky:
    print(f"Học sinh không đăng ký: {hoc_sinh_khong_dang_ky}")
```

---

## THANG ĐIỂM CHI TIẾT

| Câu | Yêu cầu | Điểm |
|-----|---------|------|
| **1** | Mỗi phần (a-f) đúng | 1 điểm |
| **2.1** | So sánh List/Tuple/Set/Dict | 3 điểm |
| **2.2** | So sánh sort/sorted | 1.5 điểm |
| **2.3** | So sánh global/nonlocal | 1.5 điểm |
| **3.1** | Giải thích hàm vs lambda | 2 điểm |
| **3.2** | Ví dụ map/filter | 2 điểm |
| **3.3** | Nested function | 2 điểm |
| **4.1** | Đệ quy | 2 điểm |
| **4.2** | Binary Search | 2 điểm |
| **4.3** | So sánh thuật toán | 2 điểm |
| **5.1** | Format string | 2 điểm |
| **5.2** | List methods | 2 điểm |
| **5.3** | Dict methods | 2 điểm |
| **6** | Xử lý sản phẩm | 15 điểm |
| **7** | Xử lý văn bản | 15 điểm |
| **8** | Hàm đệ quy | 15 điểm |
| **9** | Tìm kiếm & sắp xếp | 15 điểm |
| **10** | Lambda & HOF | 10 điểm |
| **11** | Dictionary nested | 10 điểm |
| **12** | Set operations | 10 điểm |

---

**TỔNG ĐIỂM: 120 điểm**
