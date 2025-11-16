# for i in range(1, 10): # [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print(i)
# else:
#     print("Chạy xong")

# Tính giai thừa, tính tổng các số từ 1 - n
# Đếm số lượng phần tử trong mảng bằng cách // 10
# Tính tổng các chữ số của mảng % 10
# Lập ngược số phần tử
# Số nguyên tố là số là 2 ước là 1 và chính nó. 3 -> 1, 3; 5 -> 1, 5
# n = int(input())

# count = 0

# for i in range(1, n + 1, 1):
#     if n % i == 0: # 5 % 2 -> 1; 4 % 2 = 0; 10 % 5 = 0
#         count += 1

# if count == 2:
#     print("Đây là SNT")
# else:
#     print("Đây không phải SNT")


# a = input()
# b = int(input())
# # # '1' + '2' = '12'
# print(type(a))
# print(type(b))
# # print(a + b)


# Trong đó:
# +, def -> từ khoá của hàm
# +, say_hello ->  tên của hàm, tên đại diện cho hàm
# +, (name) -> name tham số của hàm, và đây là giá trị mà ta truyền vào
# +, return -> trả về kết quả cho hàm, khi gặp từ khoá return thì hàm sẽ dừng lại, các câu lệnh bên dưới sẽ không được thực thi
# +, cú pháp gọi hàm: ten_ham(doi_so1, doi_so_2)
# +, toán tử call: ()
# +, một hàm mà không có giá trị trả về thì nó sẽ là None

# def say_hello(name, address):
#     # code block
#     # print(f"Hello {name} ở {address}") # Cách 1
#     print(name, "ở", address, sep=" ", end="\n")


# name_doi_so = "Thảo"   
# address_doi_so = "Hà Nội"
# say_hello(name_doi_so, address_doi_so) # gọi hàm đó

# say_hello("Mạnh", address_doi_so) # gọi hàm đó

    
# def findMax(a, b, c):
#     print(f"a: {a}")
#     print(f"b: {b}")
#     print(f"c: {c}")
#     return max(a, b, c)
#     print("Xong rồi")



# response = findMax(1, 2, 3)

# print(f"Kết quả trả về: {response}")

# keywork arg
# cho phép em quy định giá trị truyền vào của đối so dành cho tham số nào


# def findMax(a, b, c):
#     print(f"a: {a}")
#     print(f"b: {b}")
#     print(f"c: {c}")
#     return max(a, b, c)
#     print("Xong rồi")



# response = findMax(b=1,a=2,c=3)

# print(f"Kết quả trả về: {response}")


# default arg
# Là giá trị mặc định cho tham số nếu không có đối số được truyền vào
# Nếu không truyền đối số tương ứng vào thì nó lấy giá trị mặc định, còn  truyền thì
# nó sẽ lấy giá trị từ đối số truyền vào


# def findMax(a, b, c=3):
#     print(f"a: {a}")
#     print(f"b: {b}")
#     print(f"c: {c}")
#     return max(a, b, c)
#     print("Xong rồi")



# response = findMax(1, 2, 11)

# print(f"Kết quả trả về: {response}")


# *arg 
# dùng khi em chưa biết trước số lượng đối số mà người dùng truyền vào
# khi dùng từ khoá này nó sẽ trả ra dữ liệu dạng tuppe
# sum là 1 hàm nằm buil in dùng để tính tổng 1 list, 1 tập hợp số
# def totals(*thaos):
#     print(f"thaos: {thaos}")
#     return sum(thaos)

# response = totals(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(f"response: {response}")
    
    
# **kwargs
# **kwargs -> nó sẽ trả về dữ liệu ở dạng từ điển {"key": "value"}
# bặt buộc phải dùng keyword arg 

# def dist_books(**kwargs):
#     print(f"kwargs: {kwargs}")

# dist_books(name="Thảo", address="Hà Nội", age=20)


# Định dạng dữ liệu:
# +, tuppe: (1, 2, 3, 4, 5, 6)
# +, dist: {"key": "value"}


# Nested function

def ham_cha(a, b, c):
    print(f"Hàm cha a: {a}")
    print(f"Hàm cha b: {b}")
    print(f"Hàm cha c: {c}")
    def ham_con(a, b, c, d):
        print(f"Hàm con a: {a}")
        print(f"Hàm con b: {b}")
        print(f"Hàm con c: {c}")
        print(f"Hàm con d: {d}")
    ham_con(1, 2, 3, 10)
        
ham_cha(1, 2, 3)