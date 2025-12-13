# a = {
#     'name': "Mạnh",
#     'age': 25,
#     'address': 'Hà Nội'
# }
# a['gender'] = 'Nam'
# print(a['name'])
# print(a['age'])
# print(a.get('address'))
# print(a.get('gender'))
# Trường hợp cần dùng tới kết quả trả về
# result = a.pop('address')
# print(f"Bạn vừa xoá: {result}")

# Trường hợp không muốn kq trả về

# del a['address']
# Xoá phần tử cuối cùng
# a.popitem()

# print(a)

# print('Chuyển tiền thành công')


# a = {
#     'name': "Mạnh",
#     'age': 25,
#     'address': 'Hà Nội'
# }

# keys(), values(), items()
# Lấy tất cả keys của a
# print(a.keys())
# print(a.values())
# print(a.items())


# for key in a:
#     print(a[key])
#     print(a.get(key))
#     print(key)
# print(a.keys())
# for key in a.keys():# dict(['name', 'age', 'address'])
#     print(key)

# for value in a.values():
#     print(value)


# for (key, value) in a.items():
#     print(key, value)


# print('A', 'C', sep="+", end=" ")
# print('B', 'E', sep="+", end=" ")
# # A C
# # B E

# Ứng dụng của DIST vào các bài toán: tần suất, đếm, đánh dấu
# Dạng đếm số lần xuất hiện của các phần tử
# 1 -> 2 lần; số 2 -> 1, số 3 -> 2, số 4 -> 1
# for i in a:
#     print(f"i={i}; {a.count(i)}")
# a = [1, 1, 2, 3, 3, 4, 3]
# d = {} # {1: 2}
# for x in a:
#     # Nếu mà có rồi thì tăng số lượng phần tử đó lên
#     if x in d: # key dict([1])
#         d[x] += 1 # gán lại giá trị. d[1] = d[1] + 1; 1 + 1 = 2
#     else:
#         # Tạo ra key mới với key là giá trị phần tử trong list
#         d[x] = 1 # {1: 1}
        
# # print(f"d: {d}")

# for (key, value) in d.items():
#     print(f"phần từ: {key} xuất hiện: {value}")

# dạng tìm từ, số, xuất hiện nhiều nhất trong câu, nếu có nhiều từ cùng tần số xuất hiện thì in ra từ có thứ tự từ điển nhỏ nhất

# s = "xau xau xau xau xau ban ban ban ban ban hoi hoi"
# d = dict({})
# Bảng mã ASCII:
# số bắt đầu từ 0-9 có thứ tự (48, 57)
# chữ bắt IN đầu từ 0-9 có thứ tự (65, 90) -> chữ in A->Z
# chữ thường bắt đầu từ (97, 122) -> a - z
# "THẢO", "PHƯỢNG", "MẠNH", -> thứ tự từ điển 

# print(s.split(" ")) 
# for x in s.split(' '):
#     if x in d:
#         d[x] += 1
#     else:
#         d[x] = 1

# b = list(d.items()) # ép kiểu về list
# b.sort(key = lambda x : (-x[1], x[0]))

# print(b[0][0], b[0][1])

# print(b)
# print(d)

# list comprehension
# a = [1, 2, 3, 4, 5]
# so_chan = [x for x in a if x % 2 == 0] # [2, 4]
# print(so_chan)

# dict comprehension

# a = [1, 2, 3, 4]
# d = {}
# Khi chưa biết dict comprehension ta làm như này
# for x in a:
#     d[x] = x ** 2
# print(d)

# khi biết dict comprehension ta sẽ làm

# cú pháp: {key: value for in interable} # interable (tập hợp có thể lặp)
# d1 = {x : x ** 2 for x in a}
# print(d1)

# s = 'abc'
# d  = {x * 3 :  x * 3 for x in s}

# print(d)






        
    
        
