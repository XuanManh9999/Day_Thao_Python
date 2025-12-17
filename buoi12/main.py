# Học về set trong python
# [1, 2, 3] => 1, 2, 3. 2, 3, 1, 3, 2, 1
# Set trong python là tập hợp các phần tử duy nhất không có thứ tự. Và thường được sử dụng để tính toán những phép toán liên quan đến tập hợp

# Các tính chất của SET
# +, Các phần tử trong set sẽ không có thứ tự nhất định
# +, Các phần tử trong set là độc nhất, không có 2 phần tử nào trùng nhau
# +, Set không thể truy cập được thông qua chỉ số (nó không phụ thuộc vào index)
# +, Set có thể thay đổi giá trị

# Cách tạo set {}
# s = {"Hà Nội", "Hải Phòng", "Hải Dương", "Hải Dương", 1, 1, 1, 2, 2, 3, 3, 3, 3, 33, 33}

# print(s)


# Set không lưu được những phần tử có thể thay đổi được giá trị VD: list 
# unhashable type: 'list'
# s = {[1, 2], "python", "28tech"}

# print(s)


# Set constructor
# Mình có thể khởi tạo được set bằng hàm tạo (constructor) từ các object khác như list, str, range...

# a = [1, 2, 1, 3, 4, 5, 6, 7]
# b = set(a) # c huyển đổi list thành set

# a = list(b) # chuyển đổi lại set thành list

# print(a) # [1, 2, 3, 4, 5, 6, 7]

# print(a)

# Các hàm của set
# Thêm phần tử vào set
# s = {} # mặc định nó sẽ hiểu là dict
# s = set() # dùng để chỉ định tạo set
# s.add("Mạnh")
# s.add("Thảo")
# s.add("Thảo")
# s.add("Phượng")

# print(s)


# Để có thể thêm nhiều phần tử set vào cùng một lúc ta sẽ sử dụng hàm update
# s = set()

# s.update([4, 1, 1, 2, 3, 4, 5])

# print(s)


# Xoá phần tử khỏi set
# Hàm pop: nó sẽ xoá một phần tử ngẫu nhiên ở set
# Hàm clear: xoá toàn bộ phần tử ở trong set
# Hàm remote: sử dụng để xoá một phần tử ở trong set, nhưng nếu phần tử đó không có thì nó sẽ báo lỗi KeyError
# Hàm discard: sử dụng để xoá một phàn tử ở trong set nếu có

# s = set()
# s.update([11, 11, 2, 2, 33, 33, 44, 44])
# s.pop()
# s.clear()

# s.remove(55)

# s.discard(55) # không có thì thôi

# print(s)


# hàm len trong set
# Được sử dụng để thống kê số lượng phần tử ở trong set
# s = set()

# s.update([1, 2, 3, 4, 4, 5])

# print(len(s))


# Duyệt qua set
# dùng foreach để duyệt qua set
# for x in s: # {1, 2, 3, 4, 5}
#     print(x)


# Các phép toán tập hợp trong set
# Union: Phép hợp bản chất là hợp 2 set vào với nhau. Kết quả thu về 1 set mới chưa các phần tử không trùng lặp ở cả 2 set
# s = {"Mạnh", "Thảo", "Phượng", "Khánh", } # set A
# b = {"Phương", "Quyền", "Mạnh", "Khánh"} # set B
# c = b.union(s)
# c = b | s
# print(c)

# intersection: Phép giao lấy ra các phần tử thuộc cả 2 tập hợp, sử dụng & hoặc hàm intersection để tìm giao của 2 tập hợp

# Lấy ra những phần tử đều có ở 2 tập hợp set
# s = {"28tech", "5am", "123tech"}
# m = {"28tech", "5am", "Học mãi"}
# # u = s.intersection(m) # phép giao
# u = m & s # phép giao

# print(u)

# Phép Diffrence: hàm symmetric_difference:  lấy ra các phần tử thuộc 1 trong 2 tập hợp nhưng bỏ đi phần tử thuộc cả 2 tập hợp
# s = {"28tech", "mạnh", "ptit"}
# m = {"codezen", "mạnh", "hust"}
# # c = s.symmetric_difference(m) # Cách 1
# c = s ^ m # cách 2
# print(c) # 

# Mục tiêu là tôi muốn kq xem trong 2 set có thằng nào trùng nhau không -> Nếu không là OK (TRUE), Có thì False
# Hàm isdisjoint(): Xác định xem 2 tập hợp (set) có phần tử nào chung không? Trả về True, False
# Trả về False nếu 2 set có phần tử trùng nhau
# Trả về True nếu 2 set không có phần tử nào giống nhau
# s = {"Thảo", "Khánh"}
# m = {"Thảo", "Đức"}
# k = {"Ptit", "Hust", "Uet"}

# print(s.isdisjoint(m)) # False 
# print(s.isdisjoint(k)) # True



# Hàm issubset(): Kiểm tra xem tập hợp này có phải là con của tập hợp khác hay không? (True, False)
# maytinh = {"Mạnh", "Chiến", "Dương", "Khải"}
# m = {"Trung", "Chung", "Phước"}
# dienthoai = {"Mạnh", "Khải"}
# Kiểm là điện thoại có là tập con của máy tính không?
# print(sub.issubset(s))
# print(dienthoai.issubset(maytinh)) # True
# print(m.issubset(dienthoai)) # False



# Hàm issuperset(): Kiểm tra xem tập này có phải là cha của tập khác hay không
# Một tập ở để được gọi là cha của tập hợp khác khi và chỉ khi là. Tập cha đó chưa "Toàn bộ" các phần tử nằm trong tập hợp con
# s = {"28tech", "codezen", "python"}
# t = {"28tech",  "python"}
# u = {"BKA", "UET", "28tech"}

# print(s.issuperset(t)) # True
# print(u.issuperset(t)) # False