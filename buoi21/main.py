# a)
# a = 15 // 4
# b = 15 % 4
# print(a, b)

# b)
# x = 5
# y = 10
# result = x > 5 and y < 15
# print(result)

# # c)
# s = "Python"
# print(s[1:4])
# print(s[-3:])

# # d)
# lst = [1, 2, 3]
# lst.append([4, 5])
# print(lst)

# # e)
# d = {"a": 1, "b": 2}
# print(d.get("c", 0))



# Câu 2 (5 điểm)
# Hãy giải thích sự khác biệt giữa các cặp sau:

# List và Tuple: So sánh về tính chất, cách khai báo, và khi nào nên dùng mỗi loại.
# break và continue: Giải thích cách hoạt động và cho 2 ví dụ minh họa sự khác biệt.

# LIST
# Cú pháp: [1, 2, 3]
# Tính chất: Có thể thay đổi các phần tử
# Thao tác: thêm, sửa, xoá
# Tốc độ: chậm hơn
# Khi nào dùng: Dữ liệu cần thay đổi

# TUPLE

# Cú pháp: (1, 2, 3)
# Tính chất: không thể thay đổi được giá trị
# Thao tác: không thể thêm sửa xoá được
# Tốc độ: nhanh
# Khi nào dùng: Dữ liệu cố dịnh, không đổi


# def func1(a, b=10):
#     return a + b

# *args cho phép mình truyền vào số lượng tham số không xác định, các giá trị truyền vào sẽ là 1 tuppe
# def func2(*args):
#     print(f"args: {args}")
#     return sum(args)


# **kwargs cho phép hàm nhận số lượng tham số từ khoá không xác định, các giá trị truyền vào sẽ là ở định dạng dict
# def func3(**kwargs):
#     return kwargs


# print(func1(5))

# print(func2(5, 10, 15, 18, 11))

# {"name": "THảo", address: "Hải Dương"}
# print(func3(name="Thảo", address="Hải Dương"))


# Câu 4 (5 điểm)
# Trong Python có 3 cách format string. Hãy nêu tên và cho ví dụ minh họa cho mỗi cách:

# Ví dụ: Biến name = "Thảo", age = 20, cần in ra: "Tên: Thảo, Tuổi: 20"


# 1. F-string (đây là cách hiện tại nhất)
# name = 'Thảo'
# age = 20
# s = f'Tên: {name}, tuổi: {age}'

# print(s)

# 2. String formatting với %. Lưu ý: %s cho string, %d cho số nguyên, %f cho số thực

# name = 'Thảo'
# age = 20

# s = "Tên: %s, Tuổi: %d" % (name, age)
# print(s)

# 3. Phương thức .format()
# name = 'Thảo'
# age = 20

# s = "Tên: {}, Tuổi: {}".format(name, age)
# print(s)



# # Nhập 3 số nguyên
# a = int(input("Nhập a: "))
# b = int(input("Nhập b: "))
# c = int(input("Nhập c: "))

# # Tính tổng
# tong = a + b + c

# # Tính trung bình cộng
# trung_binh = round(tong / 3, 3)

# # Tìm số lớn nhất và nhỏ nhất
# so_lon_nhat = max(a, b, c)
# so_nho_nhat = min(a, b, c)

# # Kiểm tra số chia hết cho 3
# co_so_chia_het = "Có" if (a % 3 == 0 or b % 3 == 0 or c % 3 == 0) else "Không"

# # In kết quả
# print(f"Tổng: {tong}")
# print(f"Trung bình cộng: {trung_binh}")
# print(f"Số lớn nhất: {so_lon_nhat}")
# print(f"Số nhỏ nhất: {so_nho_nhat}")
# print(f"{co_so_chia_het} số chia hết cho 3")


# Câu 7 (15 điểm): Xử lý danh sách
# Cho một list số nguyên được nhập từ bàn phím (mỗi số cách nhau bởi dấu cách), ví dụ: "1 2 3 4 5 6 7 8 9 10"
# input_str = input("Nhap cac so nguyen moi so canh nhau boi 1 khoang trang")

# Chuyển chuỗi nhập vào thành list số nguyên
# numbers = [int(x) for x in input_str.split()]
# # print(numbers)

# # Tạo list mới chỉ chứa các số chẵn
# so_chan = [x for x in numbers if x % 2 == 0]
# # print(so_chan)
# # Tạo list mới chỉ chứa các số le
# so_le = [x for x in numbers if x % 2 == 1]

# # print(so_le)
# # Tính tổng các số chẵn và tổng các số lẻ

# tong_chan = sum(so_chan)

# tong_le = sum(so_le)

# # print(tong_chan)
# # print(tong_le)

# # Tìm số lớn nhất và số nhỏ nhất trong list gốc

# so_lon_nhat = max(numbers)
# so_nho_nhat = min(numbers)

# # print(so_lon_nhat)
# # print(so_nho_nhat)

# # Đếm số lượng phần tử chia hết cho 3

# dem_so_luong_chia_het_cho_3 = len([x for x in numbers if x % 3 == 0])

# print(dem_so_luong_chia_het_cho_3)


# Câu 8 (15 điểm): Quản lý sinh viên bằng Dictionary
# sinh_vien = {}
# #  input("Nhap ho ten: ")
# sinh_vien['ho_ten'] = input("Nhap ho ten: ")
# sinh_vien['tuoi'] = int( input("Nhap tuoi: "))
# sinh_vien['toan'] = float( input("Diem toan: "))
# sinh_vien['ly'] = float( input("Diem ly: "))
# sinh_vien['hoa'] = float( input("Diem Hoa: "))

# # tinh diem trung binh
# diem_tb = round((sinh_vien["toan"] + sinh_vien["ly"] + sinh_vien["hoa"]) / 3, 2)

# xep_loai = ""
# if diem_tb >= 8:
#     xep_loai = "Gioi"
# elif diem_tb >= 6.5 and diem_tb < 8.0:
#     xep_loai = "Kha"
# elif diem_tb >= 5.0 and diem_tb < 6.5:
#     xep_loai = "Trung Binh"
# else:
#     xep_loai = "Yeu"
    
# print("THONG TIN SINH VIEN")
# print(f"Ho ten: {sinh_vien["ho_ten"]}")
# print(f"Tuoi: {sinh_vien["tuoi"]}")
# print(f"Diem toan: {sinh_vien["toan"]}")
# print(f"Diem ly: {sinh_vien["ly"]}")
# print(f"Diem hoa: {sinh_vien["hoa"]}")
# print(f"Diem TB: {diem_tb}")
# print(f"Xep loai: {xep_loai}")


# Câu 9 (15 điểm): Xử lý chuỗi ký tự
# s = input("Nhap chuoi: ")
# # dem tu trong chuoi va phan cach nhau boi dau cach
# tu_list = s.split()
# so_tu = len(tu_list)

# Đếm số chữ cái in hoa
# dem_hoa = 0
# for char in s:
#     # kiem tra xem chu do co dang in hoa khong, neu co tra ve True
#     if char.isupper():
#         dem_hoa += 1

# # Đếm số chữ cái in thường
# dem_thuong = 0

# for char in s:
#     if char.islower():
#         dem_thuong += 1

# # dao nguoc chuoi
# dao_nguoc = s[::-1]
        
# Chuyển tất cả chữ cái đầu của mỗi từ thành chữ in hoa (title case)
#'meo to' => Meo To
# title_case = s.title()        


# kiem tra chuoi khong phan biet hoa thuong thi em nen dua toan bo chuoi do ve hoa hoac thuong

# 'Manh A57k21' -> 'manh' (thuong) -> manh -> False
# 'manh a57k21' -> 'manh'  (thuong) -> OK

# Kiểm tra xem chuỗi có chứa từ "Python" không (không phân biệt hoa thường)
# hello world Python Programming -> hello world python programming
# co_python = "Co" if "python" in s.lower() else "Khong"

# print(f"Số từ trong chuỗi: {so_tu}")
# print(f"Số chữ in hoa: {dem_hoa}")
# print(f"Số chữ in thuong: {dem_thuong}")
# print(f"Chuoi dao nguoc: {dao_nguoc}")
# print(f"Chuỗi title case:: {title_case}")
# print(f"Chuoi co chua python: {co_python}")

# Câu 10 (15 điểm): Hàm và vòng lặp
# Viết các hàm sau và chương trình chính để test:

# khai niem snt: snt la so chi chia het cho 1 va chinh no

def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    # Duyet tu 2 den n - 1
    # 1 loai tru roi, chinh no da loai tru roi
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def in_danh_sach_so_nguyen_to(start, end):
    so_nguyen_to = []
    
    for num in range(start, end + 1, 1):
        if kiem_tra_so_nguyen_to(num):
            so_nguyen_to.append(num)
    return so_nguyen_to
    

start = int(input("Nhap so bat dau: "))
end = int(input("Nhap so ket thuc: "))
print(f"Cac so nguyen to trong khoang tu 10 den 30: ")

ds_snt = in_danh_sach_so_nguyen_to(start, end)

for snt in ds_snt:
    print(snt)