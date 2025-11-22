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
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Duyệt thông qua chỉ số, chỉ mục
# for i in range(0, len(a), 1): # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
#     print(a[i]) # a[0] -> in ra 1; a[1] -> in ra 2; a[2] -> in ra 3

