# a = 1 # số nguyên
# b = 1.5 # số thực
# c = 'Hà Nội'
# d = True 
# # print(a, b, c, sep=" ") # mặc định nếu in các phần tử thì sep nó sẽ giúp tạo ra 1 khoảng trắng ở các phần tử

# print(a, b, c, sep="*", end=" ") # \n -> xuống dòng mới, end nó quyết định khi kết thúc câu lệnh print
# print(d)

# Dat_01 = 'Dat'
# print = 22
# print()


# Ép kiểu về số nguyên
# a = int(input('Nhập vào a: '))

# b = int(input('Nhập vào b: '))

# # print(a, b)

# # '1' + '2' => '12'

# # print(type(a))
# # print(type(b))

# tong = a + b
# hieu = a - b
# tich = a * b
# thuong = a / b
# chia_nguyen = a // b
# chia_du = a % b
# luy_thua = a ** b # 2 ^ 3 = 8

# print("tong: ", tong)
# print("hieu: ", hieu)
# print("tich: ", tich)
# print("thuong: ", thuong)
# print("chia du: ", chia_du)
# print("chia nguyen: ", chia_nguyen)
# print("luy thua: ", luy_thua)


# a = str(input())
# print(a)


# Kiểu rẽ nhánh trong python


# Xây dựng phần mềm kiểm tra độ tuổi nhập vào nếu tuối >= 18 thì được vào, còn nếu < 18 thì không được vào
# tuoi = int(input('Nhập vào tuổi của bạn: ')) # 18

# if tuoi >= 18: # 18 >= 18 ? -> True 
#                                 print('Được vào')
#                                 # print(f'Tuổi của bạn là: {tuoi}')
#                                 print('Tuổi của bạn là: {} '.format(tuoi))
# else:
#     print('Không được được vào')


# dạng if
# Khi so sánh thì kết quả của nó luôn trả về True hoặc False

# and: nó bắt buộc tất cả biểu thức phải đúng thì mới True
# or: chỉ cần một biểu thức thoả mãn đk đúng thì nó sẽ là True
# a = 4

# if a >= 9.0: # false
#     print('Học sinh giỏi')
# elif a < 9.0 and a >= 6.5:
#     print("Học sinh khá")
# elif a < 6.5 and a >= 5:
#     print('Học sinh trung bình')
# else:
#     print('Học sinh yếu')
    
    
# or: chỉ cần một biểu thức thoả mãn đk đúng thì nó sẽ là True

# Kiểm tra xem a có là số chẵn không, và nếu không là số chẵn thì nó có phải bằng 5 hay không?

# a = 21

# if a % 2 == 0 or a == 5 or a == 21:
#     print('a là số chẵn hoặc là bằng ', a)
# else:
#     print('Không hợp lệ')
    
    
# a = 20

# if a % 2 == 0 and (a >= 3 or b > 50):
#     print("ABCXY")


# not là phép phủ định lại kết quả VD: False -> True, True -> False
# a = 123

# if not a > 150:
#     print('Có lớn hơn')
# else:
#     print('Nhỏ hơn')

# dạng 3
# tuoi = 2

# if tuoi >= 18 and tuoi <= 27:
#     print("DI LINH ROI")


# Dạng 4 toán tử 3 ngôi

# tuoi = 22

# print(tuoi) if tuoi >= 22 else print('Tuổi của bạn nhỏ hơn 22')

"""
    Đây là chương trình tính tuổi, chỉ cần nhập vào năm sinh của bạn
    tôi sẽ giúp bạn tính toán ra số tuổi của bạn
"""

# nam_sinh = int(input('Nhập vào tuổi của bạn'))

# print(2025 - nam_sinh) if nam_sinh > 0 else print('Năm sinh không hợp lệ')


a, b = map(int, input().split())
print(a - b)
# 1020162078