# print(range(0, 2, 1)) # (0, 1) => TUPPE
#lict [value, value] =>  dict({key: value}) => tuppe()

# Tuppe -> nó là một tập hợp có thứ tự trong python
# Tính chất tuppe
# +, sau khi khởi tạo ta không thể: thêm, sửa, xoá các giá trị bên trong tuppe
# +, để truy cập được các phần tử bên trong tuppe ta dùng chỉ số
# +, tuppe có thể chưa rất nhiều kiểu dữ liệu: int, float, list, dict
# +, các phần tử trong tuppe là có thứ tự 
# +, tuppe sẽ được ứng dụng khi ta muốn các phần tử có thứ tự và không thể thay đổi được sau khi được định nghĩa
# Tạo tuppe
# a = (1, 2, 3) # => 1 tuppe
# b = ("Thảo", "Mạnh", "Phượng")

# print(a)
# print(b)

# Tạo tuppe thông qua hàm khởi tạo constructor
# s = "28tech"
# b = tuple(s)
# c = tuple([1, 2, 3, 4])
# print(b)
# print(c)

# xem kiểu dữ liệu tuppe ta dùng type
# a = (1, 2, 3)

# print(type(a)) # <class 'tuple'>

# NESTED TUPPE()
# t = ("28tech", (1, 2, 3), "manh", [1, 2, 3])

# print(t)
# print(type(t))


# Tuppe unpacking
# Khi unpacking thì số lượng biến ở bên phải dấu bằng, phải bằng với số lượng phần tử trong tuppe
# t = ("thao", "han quoc", 1000000, "hai duong")
# # x,y,z,k = t
# # Trong trường hợp unpacking không đủ số lượng phần tử thì có thể sử dụng toán tử * để biểu hiện lấy tất cả phần tử nằm ở phía sau nó. Và nó sẽ trả list

# x,y,*z= t

# print(x) # thao
# print(y) # han quoc
# print(z) # [1000000, 'hai duong']

# Truy cập các phần tử trong tuppe (nó giống list). Để truy cập các phần tử trong tuppe ta dùng chỉ mục/chỉ số. Chỉ số/chỉ mục nó bắt đầu từ 0
# t = (1, 2, 3, 4, 5)
# print(t[1]) 
# print(t[2]) 
# print(t[-1]) # 3


# Duyệt tuppe
# t = (1, 2, 3, 4)

# print(len(t))

# Dùng for range
# for i in range(0, len(t), 1): # (0, 1, 2, 3)
#     # print(i)
#     print(t[i])

# Dùng hàm foreach
# for i in t: # (1, 2, 3, 4)
#     print(i)


# Kiểm tra phần tử xuất hiện trong tuppe bằng hàm in

# a = ("28tech", "Hà Nội", "Hải Phòng")
# # print("28tech" in a)
# if "28tech" in a:
#     print("YES")
# else:
#     print("NO")



# Thay đổi giá trị của các "Phần tử trong tuppe"

# t = ([1, 2, 3], "mạnh")

# t[0] = [1, 2, 3, 4]# Sai

# t[0][0] = 50# t[0] = [1, 2, 3][0] = 50

# print(t)


# Ta có thể kết hợp 2 tuppe, và nhân bản số lượng phần tử bên trong tuppe
# a = (1, 2, 3)
# b = (3, 4, 5)
# c = a + b
# print(c) # (1, 2, 3, 3, 4, 5)


# Nhân bản số lượng phần tử
# a = (1, 2, 3)
# b = a * 2
# print(b)

# Sắp xếp tuppe
# Cách 1: Dùng hàm build-in; max, min, sorted, sum...
# t = (5, 10, 15, 25, 20)
# print(sum(t)) # tính tổng các phần tử
# print(max(t)) # tìm số lớn nhất trong tuppe
# print(min(t)) # tìm số nhỏ nhất trogn tuppe
# print(sorted(t)) # Sắp xếp các phần tử trong tuppe() tăng dần


# Cách 2: chuyển đổi nó qua list
# l = list(t)

# l.sort()
# l.reverse()
# b = tuple(l) # ép list trở lại về tuppe
# print(b)

# Hàm count(), và hàm index() trong tuppe
# t = (1, 2, 3, 1, 1)
# count() dùng để đếm tấn xuất phần tử đó xuất hiện 
# print(t.count(1)) # #

# index() dùng để tìm kiếm phần tử và trả về chỉ mục/chỉ số của phần tử đầu tiên tìm thấy

# try:
#     print(t.index(19)) # không có sẽ báo lỗi
# except ValueError:
#     print("Lỗi rồi")

# print("ABC")


# python -> Kỹ thuật lập trình
# CSDL -> dùng để lưu dữ liệu
# Thư viện
# Lập trình web/app...