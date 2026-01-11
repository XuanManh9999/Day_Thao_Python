# ten = "Nguyễn Xuân Mạnh"


# def print_name(ten_):
#     # ten = ten # local scope
#     global ten
#     print(ten)
    
    
# print_name("Thảo")

# def print_f ():
#     name = "ABC"
#     def print_m(name_):
#         nonlocal name
#         print(name)
#     print_m("kk")
    
# print_f()

# Mục tiêu của pham vi của biến, hàm.. là xác định phạm vi truy cập ở đâu (ta có thể dùng nó từ đâu)


# Sắp xếp trong python

# {}, [], (), ""
# Ai nhiều tiền nhất?
# a = [1000, 500, 3000]

# a.sort() # sắp xếp theo chiều tăng dần, hoặc thứ tự từ điển (default)

# print(a)

# Hàm sort
# sắp xếp theo chiều tăng dần, hoặc thứ tự từ điển (default)

# Cú pháp:
# list.sort(key=.., reverse=..)

# +, là hàm sử dụng làm tiêu chí sắp xếp (lambda, def)
# +, reverse là True nếu cần giảm dần mặc định là false

# Hàm sort nó không trả về giá trị list mới mà nó thay đổi list gốc (list ban đầu)


# Dùng hàm sort() để sắp xếp giảm dần
# a = [1, 2, 3, 4, 5]

# # a.sort(reverse = False) # [1, 2, 3, 4, 5]
# a.sort(reverse = True) # [5, 4, 3, 2, 1]
# print(a)



# Dùng đối số key để quy định cách sắp xếp
# def handle_sort(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# a = [1, 2, 31, 4, 5, 6, 7, 8]
# a.sort(key=handle_sort, reverse = True)

# print(a)


# 123 -> 6
# 12 -> 3
# def sumDigit(n):
#     res = 0
#     while n != 0:
#         res += n % 10 # 123 % 10 = 3; 12 % 10 = 2; 3 + 2 = 5; 1 % 10 = 1; 5 + 1 = 6
#         n //= 10# 123 // 10 = 12; 12 // 10 = 1; 1 // 10 = 0
#     return res

# print(sumDigit(123))


# if __name__ == '__main__':
#     a = [3, 24, 111, 30]
#     a.sort(key=sumDigit)
#     # [3, 3, 3, 6] -> sắp xếp [3:3, 6:24, 3:111, 3:30]
#     # [3, 111, 30, 24]
#     print(a)
    
# Sắp xếp các từ theo chiều dài
# a = ['Anh', "Mạnh", "Thảo", "Phượng", "Yến", "Hoài"]
# # a.sort()
# a.sort(key=len)# [3, 4, 4, 5, 3, 4]; [3, 3, 4, 4, 4, 5]
# print(a)


# Sắp xếp nested list
# def getItem(n):
#     # Phần từ thứ 2 ưu tiên nhất, nếu bằng nhau thì lựa phần từ 1
#     return n[1], n[0]


# a = [[3, 2], [4, 1], [5, 3], [3, 1], [4, 4]]

# # [2:[3, 2], 1: [4, 1], 3:[5: 3], 1:[3:1], 4:[4:4]]
# # [1:[3:1], 1: [4, 1] , 2:[3, 2], 3:[5: 3], 4:[4:4]]

# a.sort(key=getItem) # [[3, 1], [4, 1], [3, 2], [5, 3], [4, 4]]
# print(a)



# Hàm sort() và lambda
# Tham số key  của hàm sort có thể sử dụng hàm lambda để thay thế

# a = [[2, 1], [1, 2], [0, 5]]

# a.sort(key=lambda x : x[0])

# print(a)


# data = [
#     {
#         "id": 1,
#         "name": "Nguyễn Xuân Mạnh",
#         "price": 1000,
#         "type": "VIP"
#     },
#     {
#         "id": 2,
#         "name": "Nguyễn Hồng Tộp",
#         "price": 5000,
#         "type": "SUPPER VIP"
#     },
#     {
#         "id": 3,
#         "name": "Nguyễn Giàu Có",
#         "price": 500,
#         "type": "Dân thường"
#     },
#     {
#         "id": 4,
#         "name": "Nguyễn Chí phèo",
#         "price": 5000,
#         "type": "SUPPER VIP"
#     }
    
# ]

# Sắp xếp theo số tiền khách hàng có để phục vụ, nếu cùng số tiền thì sắp xếp theo ID lớn
# Lưu ý nếu muốn sắp xếp theo nhiều tiêu chí thì phải bao quanh ()
# data.sort(key = lambda x : (x.get("price"), x.get("id")), reverse=False)

# # print(data)
# for i in data:
#     print(i)


from operator import itemgetter
# Hàm itemgetter() lấy phần tử theo chỉ mục và attrgetter()

# friends = [("Mạnh", 60), ("Cọc", 40)]
friends = [["Mạnh", 60], ["Cọc", 40]]


# friends.sort(key=itemgetter(1))
# friends.sort(key=itemgetter(0, 1))
# ("Mạnh", 60) ; itemgetter(0) -> "MẠNH", itemgetter(1) -> 60
# print(friends)


# So sanh khác nhau giữa hàm sort() và hàm sorted buildin
# Hàm sorted nó không làm thay đổi list ban đầu, hàm sort kia thì có, và hàm sort hỗ trợ nhiều tính năng hơn.