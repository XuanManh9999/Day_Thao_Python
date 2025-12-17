# a = set({"thảo"})
# b = set({"mạnh", "thảo"})
# # kiểm tra b có phải là cha của a hay không?
# print(b.issuperset(a))
# Hợp  | # hợp 2 set vào với nhau vấn đảm bảo tính chất là không có phần tử trùng nhau 
# Giao & # lấy phần tử chung thuộc cả hai tập hợp
# Defi ^ # Lấy các phần tử không thuộc vào tập hợp còn lại
# c = a | b
# c = a & b
# c = a ^ b
# print(c)
# Học về chuỗi string <class 'str'>
# Chuỗi trong python nó tập hợp các kí tự được đặt trong dấu nháy '' hoặc "" 
# s = "Nguyễn Xuân Mạnh"
# s = 'Nguyễn Xuân Mạnh'
# s = input("Nhập vào tên của Mạnh: ")
# print(type(s))
# print(s)

# Tạo chuỗi
# '' -> xâu rỗng, chuỗi rỗng
# s = 'Thảo'
# Trong python ta có thể chuyển đổi hầu hết các kiểu dữ liệu (int, float, list, tuppe..) qua hàm khởi tạo str
# s = str(123)
# m = str(["Mèo", "Cáo", "Thỏ", "Nai"])
# k = str("KK")
# print(s)
# print(m)
# print(k)

# Giải thích """ content  """
# s = 'Nguyễn Văn A
#     # error
# '

# s = """
#     Nam quốc sơn hà nam đế cư
#     Tiện nhiên định phận tại thiên thư
# """
# print(s)
# Cách truy cập các phần tử ở trong một chuỗi ta sẽ dùng thông qua chỉ mục/chỉ số
# s = "Thảo Nguyên Xanh Mướt"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4]) # dấu cách cũng là một từ ở trong str 

# 3. Truy cập kí tự thông qua chỉ số và duyệt xâu String slicing
# Một chuỗi sau khi khởi tạo thì không thể gán lại
# s = "Mông Cổ"
# s[0:4] = "Bụng"

# print(s)

# # print(s[-2], s[-1], sep="")
# print(s[-2:]) # cổ
# print(s[0 : 4])
# print(s[0:4:2])


# Duyệt xâu
s = "Cá vàng bởi trong bể nước"
# Hàm len trả về số lượng các phần tử có trong str
# print(len(s))

# Duyệt bằng hàm for range
# for i in range(0, len(s), 1):
#     print(s[i])

# Duyệt bằng for in
# count = 0
# for x in s:
#     if count == 2:
#         break
#     print(x)
#     count += 1


# String thì là immutable (ta có thể truy cập các phần tử của nó thông qua chỉ số/chỉ mục) nhưng không thể gán lại nó
# s = 'ABC'


# Nối chuỗi, nhân bản chuỗi. Thì Trong Python để nối chuỗi ta dùng +, còn để nhân bản chuỗi thì ta dùng dấu *

# s = 'ABCDEF'
# m = 'kk'

# print(s + m) # ABCDEFkk

# Nhân bản chuỗi
# s = 'ABC'
# c = s * 2

# print(c) # ABCABC


# Học về các hàm trong python
# Hàm replace(cũ, mới): được sử dụng để thay thế 1 xâu cũ bằng 1 xâu mới
# Chú ý: hàm replace sẽ trả về phần tử thay đổi, và không làm thay đổi chuỗi ban đầu
# s = 'Mông cổ cò' # chuỗi ban đầu
# result =  s.replace("cổ cò", "cổ vịt")
# print(s)
# print(result)


# Hàm split() và join()
# hàm split(): Tách các tử trong xâu, mặc định nếu hàm này không có tham số sẽ cắt theo dấu cách. Và tạo thành 1 list
# s = "Nguyễn Xuân Mạnh"

# print(s.split(" ")) # mặc định nó tách chuỗi thành 1 list. Trường hợp này không truyền vào đối số nên nó mặc định tách theo dấu cách ["Nguyễn", "Xuân", "Mạnh"]


# s = "Con mèo*béo"
# print(s.split("*")) # ['Con mèo', 'béo']
# print(s.split(" ")) # ['Con', 'mèo*béo']


# Hàm join: kết hợp các từ rời rạc thành 1 xâu được phân cách bởi kí tự cho trước
# s = ['Mèo', 'To', 'Nhỏ', 'Vừa']
# m = '+-*Hà Nội'.join(s) # biến đổi các phần tử trong tập thành 1 chuỗi khoảng khách giữa các phần tử theo sự duy định khi join
# print(m)