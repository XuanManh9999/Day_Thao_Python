# a = [3, 2, 1, 1]
# print(len(a))
# a.insert(2, 10)
# print(a)
# res =  a.pop(0)
# del a[0]
# a.clear()
# b = a
# b = a.copy()
# b[0] = 10
# print(a)
# print(b)
# print(a.count(1))
# a.sort()
# a.reverse()
# print(a.index(1)) # trả về vị trí chỉ mục đầu tiên mà nó tìm thấy
# print(a)
# print(max(a))
# print(min(a))
# for i in range(0, len(a), 1):
#     print(a[i])
# for i in a:
#     print(i)

# LIST SLICING [start : stop : step]
# Trả về một khoảng hoặc một đoạn nào đó trong list ban đầu, ngoài ra nó còn được dùng để copy list giống hàm copy

# a = [1, 2, 3, 4, 5]

# print(a[0 : 3 : 1])
# print(a[1 : 4 : 1])
# print(a[2 : 4 : 1])


# Tính chất
# Nếu không truyền stop thì mặc định nó sẽ lấy vị trí ở cuối list
# Nếu không truyền step thì mặc định là 1
# Nếu không truyền start vào thì mặc định nó sẽ là 0
# Ta có thể khoảng cả chỉ số âm và dương
# print(a[2:]) # 3, 4, 5
# print(a[0:])
# print(a[:3])


# LIST SLICING [start : stop : step] với chỉ số âm nó sẽ bắt đầu từ -1
# a = [1, 2, 3, 4, 5, 6]


# print(a[3:])
# print(a[-4 : ])
# print(a[0 : -1])

# Dùng LIST SLICING để lật ngược list
# ::-1 -> dùng để lật ngược 1 list
# a.reverse()
# print(a[::-1])


# Dùng LIST SLICING thay đổi giá trị nhiều phần tử trong một đoạn
# a[0] = 1000
# a[1] = 2000

# a[0:3] = [100, 200, 300] # [100, 200, 300, 4, 5, 6]

# a[2:-1] = [300, 400, 500]
# a[1:3] = [2000, 3000]
 
# print(a)


# Chèn và xoá với List slicing

# a = [1, 2, 3, 4, 5, 6]

# a[:0] = [100, 200, 300] # thêm vào đầu list

# a[len(a):] = [1000, 2000, 3000] # thêm vào cuối list
# print(a)


# a[2:3] = [1000, 2000, 3000]

# Xoá phần tử
# a[1:4] = [] # xoá phần tử trong khoảng 1 -> 3 [2, 3, 4]

# print(a)


# Dùng để copy phần tử list tương tự hàm copy

# b = a[:] # copy list hiện tại
# # [1, 2, 1, 2, 3, 4, 5, 6]
# b[2:4] = [1, 2, 3, 4]


# print(a)
# print(b)


# LIST Comprehension thường dùng để custom list ban đầu
# cú pháp: [Experession for var in interable if_clause]
# Trong đó:
# Experession là biểu thức, for (cú pháp lặp), var, thao (biến lưu dữ liệu), in cú pháp, interable (cấu trúc có thể lặp)

# a = [1, 2, 3, 4]
# s = 'hanquoc'
# b = [x for x in a] # copy list ban đầu
# b = [x * 2 for x in a]
# b = [x ** 2 for x in a]
# 1^2 = 1, 2 ^ 2 = 4, 3 ^ 2 = 9, 4 ^ 2 = 16
# kq = [x + "1" for x in s]# (hanquoc)
# print(kq)

# b = []
# for i in a:
#     if i % 2 == 0:
#         b.append(i)
# print(b) # 

# b = [x for x in a if x % 2 == 0]
# print(b)
# skip ở phần nested list


