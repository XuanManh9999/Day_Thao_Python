#  for, while
# break: THoát khỏi vòng lặp mà nó đang nằm trong đó
# continue: Bỏ qua các câu lệnh bên dưới, và tiếp tục các bước lặp tiếp theo nếu có

# for i in range(1, 11, 1):# (1-10)
#     # 5 % 2 = 1
#     # nhỏ hơn khi chia dư thì bằng chính số đó
#     if i % 2 == 0:
#         continue
#     print(i)



# def helloThao(name, address):
#     print("Đã gọi hàm hello thảo")
#     def tienCuaThao(so_tien):
#         print(f"{name} {address}; Số tiền của thảo là: {so_tien}")
#         def truongCuaThao(name):
#             print(name)
#             # return "Ở Hàn Quốc"
    
#         print(truongCuaThao("Thảo ĐZ"))
#         # print(truongCuaThao())
#     tienCuaThao("1000$")
        
# helloThao("Thảo", "Hải Dương")

# SNT thì không thể âm, và nó phải có đk là chỉ chia hết cho 1 và chính nó
# def kt_snt(n):
#     if n < 2:
#         return False
#     cnt = 1 # đếm số lần chia hết
#     for i in range(2, n + 1, 1):
#         if n % i == 0: # chia hết
#             cnt+= 1
#     if cnt == 2:
#         return True
#     else:
#         return False
# from math import *
# def kt_snt_tu(n):
#     if n < 2: return False
#     for i in range(2, isqrt(n) + 1, 1):
#         if n % i == 0:
#             return False
#     return True
    
# print(kt_snt(5))
# print(kt_snt_tu(6))
# 6 -> 1, 2, 3, 6
# 5 -> 1 -> 5

# Học về LIST
# CGV TELECOM -> 1000CV gửi về -> 200CV gọi phỏng vấn -> 10 -> INTERN (thực tập) -> 1 BẠN (DEVELOPER)
# BA -> phân tích nghiệp vụ (3tr VNĐ) -> chính thức 7tr (mới) -> 1 năm -> 15tr; 2-3,4 $
# TESTTER -> kiểm thử phần mềm (3tr VNĐ) chính thức 8tr (mới) -> 1 năm -> 15tr;
# 4-5 tỷ -> NHÀ Ở XÃ HỘI (8-15tr) 3 phòng 1 tỷ 8, 9 



# list (danh sách, dãy) []
# 1, 2, 3, 4, 5, 6
# a = 1
# b = 'a'
# c = True

# Thứ tự, chỉ mục của list thì nó sẽ bắt đầu từ 0
# Trong 1 list có thể chứa nhiều kiểu dữ liệu khác nhau
# 1, 2, 3, 4, 5, 6
# 0, 1, 2, 3, 4, 5 -> chỉ mục, chỉ số

# Cú pháp khởi tạo 1 list
# a = 1
# b = 2
# c = 3
# d = 4
# print(a, b, c, d)

# a = [1, 2, 3, 4, 5] # một list 
# print(a[0]) # -> 1
# print(a[1]) # -> 1
# print(a[2]) # -> 1
# print(a[3]) # -> 1
# print(a[4]) # -> 1
# print(a[5]) # -> khi vượt quá độ dài chỉ mục của nó thì sẽ báo lỗi

# List constructor dùng để biến đổi một tập hợp giá trị nào đó về 1 list
# name = 1
# print(list(name))


# len() -> in ra độ dài của các phần tử có bên trong list
# a = ['Thảo', 'Hải Dương', 'Hàn Quốc'] # thằng này có 3 pt 
# print(len(a))

# print(a[-1])
# print(a[-2])
# print(a[-3])


# print(a[2]) # Chắc chưa??
# print(a[-2])


# Duyệt list
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Duyệt thông qua chỉ số, chỉ mục
# for i in range(0, len(a), 1): # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#     print(a[i]) # a[0] -> in ra 1; a[1] -> in ra 2; a[2] -> in ra 3


# # a = "Thảo"
# a = True
# print(list(a))


# Buổi 6 ôn tâp về duyệt mảng
# -1, -2, -3, -4
# a = ["Cam", "Quýt", "Mít", 2025, 2000, 2003, 2005]
# 7 -> 0 -> 7
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])

# Cách in đầu tiên
# for i in range(0, len(a), 1):# 0;7;1 (0, 1, 2, 3, 4, 5, 6)
#     print(a[i]) # 
  
  
    
# Dùng for in để in ra các giá trị nằm bên trong mảng
# ý tưởng nó sẽ lấy từng phần tử trong list đó gán cho i    
# for thao in a: # ["Cam", "Quýt", "Mít", 2025, 2000, 2003, 2005]
#     print(thao)

# 
# for i in range(-1, len(a) * - 1 - 1, -1): # [-1, -6, -1]# -1, -2, -3, -4, -5, -6
#     print(a[i])

# Thay đổi giá trị của phần tử

# a = ["Cam", "Quýt", "Mít", 2025, 2000, 2003, 2005]
# a[0] = "Bưởi"
# a[-1] = 2055
# print(a)

# -- Thêm một phần tử vào list
# +, append(thêm phần tử vào cuối list), insert (thêm phân từ vào vị trí bất kì trong list))


# a = ["Cam", "Quýt", "Mít", 2025, 2000, 2003, 2005]

# a.append("2100")

# a.append("Lê") # thêm phần tử vào cuối list


# a.insert(3, "Ổi")
# a.insert(-1, 1900)
# a.insert(6, 2002)

# print(a)

# => xoá phần tử thông qua chỉ số

# Cách xoá phần tử trong list dùng hàm pop
# a = ["Cam", "Quýt", "Mít", 2025, 2000, 2003, 2005]
# res = a.pop() # xoá phần tử cuối cùng trong list và trả về chính phần tử đó
# a.pop(4)
# a.pop(4)
# # a.pop(0)
# # a.pop(-1)
# print(f"Ban vua xoa thanh cong phan tu: {res}")
# print(a)


# Xoá phần tử khỏi list mà không có kết quả trả về del
# a = ["Cam", "Quýt", "Mít", 2025, 2000, 2003, 2005]

# del a[0]
# del a[2]
# del a[3]
# print(a)


# xoá phần tử thông qua giá trị
# lưu ý hàm này nếu phần tử xoá mà không có trong list thì nó sẽ báo lỗi
# a = ["Cam", "Quýt", "Mít", 2025, 2000, 2003, 2005]

# a.remove("Cam")
# a.remove(2003)


# # khuyên dùng để tránh
# gia_tri_muon_xoa = input("Nhập vào: ")

# a.remove(gia_tri_muon_xoa)


# # if gia_tri_muon_xoa in a:
# #     a.remove(gia_tri_muon_xoa)
# # else:
# #     print("Không xoá")

# print(a)


# Hàm clear dùng để xoá tất cả các phần tử ở trong list


# a = ["Cam", "Quýt", "Mít", 2025, 2000, 2003, 2005]
# a.clear() # []

# a.append(1) # [1]
# a.insert(1, 20)# [1, 20]

# print(a)



# Sao chép list bản chất là nó sẽ nhân x lần số lượng phần tử ở trong list
# a = ["Cam", "Quýt", "Mít", 2025, 2000, 2003, 2005] 

# b = a * 2

# print(b)

# f = [0] * 1000000

# print(f)


# Tìm kiếm phần tử trong list
a = ["Cam", "Quýt", "Mít", 2025, 2000, 2003, 2005] 

# if "Cam" in a:
#     print("YES")
# else:
#     print("NO")

# Thuật toán tìm kiếm tuyến tính
# ý tưởng là ta sẽ duyệt list, mảng đó từ đầu đến cuối để tìm. Tại mỗi lần lặp ta dùng if để so khớp xem có trùng với phần tử trong mảng/list không.
# for i in range(0, len(a), 1):
#     print(f"i: {i}")
#     if a[i] == "Cam":
#         print("YES")
#         break


# append -> thêm phần tử vào cuối mảng
# insert -> dùng để thêm phần tử vào vị trí bất kì
# pop -> dùng để xoá phần tử cuối hoặc theo index
# del -> dùng để xoá phần tử nhưng ko trả về phần tử xoá như pop
# clear -> dùng để xoá toàn bộ phần tử trong list
# cách gán lại phần tử trong list. ten_list[0] = giá trị mới
# cách duyệt vòng lặp bằng for range và for in
# thuật toán tìm kiếm tuyến tính




