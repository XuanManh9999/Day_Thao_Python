# string
# Hàm replace là một hàm dùng để thay thế phần tử của chuỗi/xâu nhưng không làm thay đổi chuỗi ban đầu
# s = "Nguyễn Xuân Mạnh Mạnh"

# result = s.replace("Mạnh", "Thảo")
# print(result)
# print(s)


# Hàm split()
# s = 'Nguyễn Xuân Mạnh'
# # [Nguyễn, Xuân, Mạnh]
# print(s.split(" "))
# s = "Phạm-Phương-Thảo"
# print(s.split("-"))

# Hàm join() biến đổi một list thành một chuỗi dựa theo đối số truyền vào quy định
# a = ["Thảo", "Bạn Mông Cổ", "Bạn Ai Cập"]

# result = "*".join(a)
# print(result) # Thảo-Bạn Mông Cổ-Bạn Ai Cập

# D:\workspace\day_them\python-thao\buoi14
# python-thao\buoi14
# path = ["D:\workspace\day_them", "python-thao/buoi14"]
# result = '/'.join(path)

# Các hàm case conversion
# s = 'Nam Quốc Sơn Hà'

# print(s.upper()) # chuyển chuỗi qua in hoa
# print(s.lower()) # chuyển chuỗi thành in thường
# print(s.capitalize()) # chuỗi đổi chữ cái đầu tiên thành chữ in hoa
# print(s.swapcase()) # chuyển đổi các chữ in thành chữu thường, còn chữ thường thành chữ in của chuỗi an đầu hiện tại
# print(s.title()) # dùng để viết hoa chữ cái đầu của từng từ
# # Anh ấy đánh tôi gần chết. Có những lần tôi đi làm về


# Hàm kiểm tra xâu con
# Trong string/xâu để tìm kiếm các phần tử trong xâu thì có hàm find. Hàm này sẽ trả về chỉ mục xuất hiện phần tử đầu tiên của chuỗi cần tìm đó
# s = 'Bạn nam Mông Cổ Mông Cổ'

# print(s.find("Mông Cổ")) # 8
# print(s.find("Bạn Ấn Độ")) # -1 

# Dùng in để kiểm tra 1 xâu có còn tại trong xâu gốc không
# print("Mông Cổ" in s) # True
# print("Cổ nam" in s) # False Có từ Cổ nam xuất hiện liền ko
# print("Bạn nam" in s)

# String format
# Trong python có 3 dạng để nhúng biến vào trong xâu kí tự
# Dạng 1: f String

# a = "Mèo cam"
# b = f"Con {a} ngố"
# print(b)
# print(f"{a}:{b}") # "Mèo cam:Con Mèo cam ngố"


# Dạng 2: String formatting: %s -> chuỗi, %d số nguyên, %f số thực
# ten_meo = "Mèo Cam" # %s 
# tuoi_meo = 4 # %d
# can_nang_meo = 3.5 # %f

# s = "%s %d Tuổi %f Kg"  % (ten_meo, tuoi_meo, can_nang_meo)

# # Lưu ý:
# # Các dữ liệu truyền vào cần phần đúng kiểu dữ liệu
# # Số lượng các tham chiếu (%s, %d, %f) nó phải tương ứng các giá trị mà ta truyền vào

# print(s)

# Dạng 3: String.format()

# name = 'Sơn Tùng'
# age = '28'
# info = '09xx'
 
# # Các chỉ số truyền vào nó sẽ bắt đầu từ 0

# s = "Tên ca sĩ: {0}; Tuổi ca sĩ: {1}; Số Điện Thoại: {2}".format(name, age, info)

# print(s) # Tên ca sĩ: Sơn Tùng; Tuổi ca sĩ: 28; Số Điện Thoại: 09xx


# ======================================================== Ôn tập ==============================
# Biến và kiểu dữ liệu: int, float, bool (true, false), string (''), list, tuppe, set, dict
# Các phép toán, so sánh: +, -, *, /, //, %, **. >=, <=, ==, !=, >, <
# Phép toán tập hợp: and, or, not
# Thư viện toán học (math): pow(a, b), sqrt() căn bậc 2, isqrt() trả về phàn nguyên của căn bậc 2, floor() làm trong xuống, ceil() làm tròn lên, abs() trị tuyệt đối, round() làm trong dựa trên tỉ lệ, random() (0-1), max(), min, sum, sorted, count()..

# Nhập xuất:
# - Xuất: print(value, sep, end); sep: khoảng cách giữa các phần tử mặc định " ", end: quy định phần tử có xuống hàng mới hay không mặc định là \n
# - Nhập: hàm input() mặc định trả về chuỗi
# Kiểu dữ liệu rẽ nhánh
# Vòng lặp(for range, for in) break, continue
# Hàm
# List
# Tuppe
# Dict
# Set
# String
# a = 1
# b = 2
# print(a, b, sep="*", end="\n")
# print(b)

# Nhập
# s = input("Nhập vào con mèo nhà bạn: ")
# print(type(s))
# print(s)

# Rẽ nhánh
# a = 1
# b = 2

# if a > b: # False 1 > 2
#     print("A > B")
# else:
#     print("A < B")

# a = int(input("Nhập vào a: "))
# b = int(input("Nhập vào b: "))
# # and -> tất cả đúng mới đúng
# # or -> một trường hợp đúng là ok
# # not -> phủ định lại Đúng - Sai. Sai - Đúng
# if a  % b == 0 and a > 20:
#     print("A là người được chọn")
# elif a < b or b > 20:
#     print("B là người được chọn")
# else:
#     print("Còn mèo cam được chọn")


# Nếu người ta đã nghĩ mình: Điều mình nói đúng cũng thành xa
# Nếu người ta đã không cần nữa. 
# print(not(True))
# print(not(False))

# Vòng lặp(for range, for in) break, continue
# a = [1, 2, 3, 4, 5]
#    0, 1, 2, 3, 4
# print(a[0])
# for i in range(0, len(a), 1):
#     print(a[i])

# for x in a:
#     print(x)

# break: nghĩa là nếu vòng lặp gặp câu lệnh break thì nó sẽ thoát khỏi vòng lặp chứa câu lệnh break mà nó đang nằm trong đó
# for i in range(0, len(a), 1): # (0, 1, 2, 3, 4)
#     if a[i] == 3:
#         break
#     print(i) # 0, 1
    
# print("Các câu lệnh tiếp theo")

# continue: bỏ qua bước lặp hiện và các câu lệnh bên dưới của nó nếu có

# for i in range(0, len(a), 1): # (0, 1, 2, 3, 4)
#     if a[i] == 3:
#         continue
#     print(i)
    

# định nghĩa hàm
# Hàm có 2 loại:
# +, Trả về giá trị: dùng từ khoá return
# +, Không trả về giá trị thì là None

# def say_hello(name): # tham số
#     print(f"Hello wolrd: {name}")
#     return 22

# # Để kích hoạt hàm ta phải gọi nó
# # Cú pháp: ten_ham(_cac_doi_so_neu_co)

# say_hello("Mạnh") # đối số
# print("Kq trả về từ hàm: ", say_hello("Mạnh"))


