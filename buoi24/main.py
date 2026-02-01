# Tính chất còn lại Trừu tượng
# Trừu tượng = Ẩn chi tiết thực thi, chỉ đưa ra "cái cần phải làm", không quan tâm "làm như thế nào"
# Lái xe ô tô: Đap ga -> xe chạy, đạp phanh -> xe dừng. Mình không cần biết động cơ nó hoạt động như nào

# Hiểu nó như là bản yêu cầu mà mình là khách hàng:
# Tôi cần 1 con xe máy có bàn đạp -> yêu cầu đạp là đi, ấn còi là kêu, đề phải nổ
# Trong oop python có thính trừu tượng: Phương thức trừu tượng (chưa có code), Phương thức thường

# # Cấu trúc:
# Class trừu tượng:
#     chứa: 
#         Thuộc tính
#         Phương thức trừu tượng
#         Phương thức bình thường (nếu cần)

# import abstractmethod
# from abc import abstractmethod

# class Car:
#     category = "Honda"
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def get_name(self):
#         return name

# class Payment(Car):
#     @abstractmethod
#     def pay(self, amount):
#         pass # khoong can logic thuc thi. Muốn là Payment thì phải có pay()


# # Các class con riển khai chi tiết
# class MomoPayment(Payment):
#     def __init__(self, name, price):
#         Payment.__init__(self, name, price)

    
#     def pay(self, amount):
#         print(f"Thanh toán: {amount} bằng momo")
#     def __str__(self):
#         return f"name: {self.name}; price: {self.price}"

# momo = MomoPayment("Ô tô Honda", 1000)

# print(momo)
    

# from abc import ABC, abstractmethod

# class Sep(ABC): # sếp khó tính
#     # Sếp yêu cầu
#     @abstractmethod
#     def kpi(self, amount):
#         pass
    
#     @abstractmethod
#     def phuong_an_kinh_doanh(self, desc):
#         pass
    
#     @abstractmethod
#     def tinh_lam_day_bao_lau(self, time):
#         pass

# class NhanVienCaBiet(Sep):
#     def nghi_mat(self):
#         print("Nghỉ ở Sầm Sơn")


# class NhanVienNgoan(Sep):
#     def kpi(self, amount):
#         print(f"Dạ sếp năm tới em tính KPI của em là {amount} tỏi")
#     def phuong_an_kinh_doanh(self):
#         print("Ngoài trừ, cướp, giết, hiếp thì gì em cũng làm")

#     def tinh_lam_day_bao_lau(self):
#         print("Tuỳ nếu đặt em ở lâu, hoặc có cty trả lương cao hơn thì nghỉ")

# nhan_vien_ca_biet = NhanVienNgoan()

# nhan_vien_ca_biet.kpi(1)
# nhan_vien_ca_biet.phuong_an_kinh_doanh()
# nhan_vien_ca_biet.tinh_lam_day_bao_lau()


# nhan_vien_ca_biet = NhanVienCaBiet()
# nhan_vien_ca_biet.nghi_mat()

# Trừu tượng = định nghĩa luật chơi, không chơi hộ người khác

# Những gì em muốn lớp con của nó phải làm thì ta hãy định nghĩa nó ở lớp cha

# print("Hello")


# Chốt về OOP gồm 4 tính chất: đóng gói, kế thừa, đa hình, trừu tượng:


# Nhập xuất file trong python
# File = nơi lưu dữ liệu trên ổ cứng -> noi luu du lieu tren o cung; co an com khong con cho;
# python hỗ trợ làm việc với file qua hàm open()
# cú pháp: open(file_path, mode, encoding)
# file_path: Đường dẫn file (vị trí lưu trữ của file ở trên ổ cứng) D:\workspace\day_them\python-thao\buoi24
# mode: chế độ độc/ghi khi mình tương tác với file
# encoding: Bẳng mã hiển thị (rất quan trong với tiếng việt)

# mode: 
# r -> đọc file
# w -> ghi file (xoá nội dung cũ)
# a -> ghi thêm
# x -> tạo file mới (nếu file đó tồn tại trước đó thì lỗi)
# rb -> đọc file nhị phận
# wb -> ghi file nhị phân

# 90% chỉ dùng: r, w, a

# with open("./data.text", "r", encoding="utf-8") as f:
#     content = f.read()
# # ../ -> nghĩa là nó nhảy ra ngoài thư mục hiện tại 1 cấp
# with open("../buoi23/tin-nhan.txt", "r", encoding="utf-8") as f:
#     content = f.read()
# print(content)

# with open("./bai-tho.text", "r", encoding="utf-8") as f:
    # content = f.read() # đọc toàn bộ rồi in toàn bộ nội dung của file bao gồm cả dầu xuống hàng các thứ
    # print(content)

    # đọc từng dòng và mỗi dòng nó in thêm 1 khoảng xuống hàng
    # for line in f:
    #     print(line)


    # Đọc từng dòng nhưng bỏ qua ký tự xuống hàng (\n)
    # count += 1
    # for line in f:
    #     print(line.strip())


    # Đọc thành list theo các dòng
    # lines = f.readlines() # ['Mặt trời xuống biển như hòn lửa\n', 'Sóng vô cài then đêm sập cửa\n', 'Đoàn thuyền đánh cá lại ra khởi\n', 'Câu hát răng buồng cùng gió khởi']

# print(f"lines: {lines}")



# Ghi file trong Python (w)
# Khi ghi bằng write này thì file cũ nó sẽ bị xoá đi và nó tự động tạo 1 file mới, nếu không có file nó  tự tạo
# with open("./container.txt", "w", encoding="utf-8") as f:
    # f.write("Xin chào Hà Nội\n")
    # f.write("Thủ đô của kẹt xe")
    # f.write(f"Mật khẩu xe máy: 4321")


# Ghi file nhưng gọi là ghi thêm vào (a)
# with open("./container.txt", "a", encoding="utf-8") as f:
#     f.write("\nmk fb: 123\n")
#     f.write("mk tiktok: 1234\n")

# Ghi nhiều dòng
# lines =  ["Ngày thứ 2 chúc bố ngủ ngon\n", "Ngày thứ 3 chúc mẹ ngủ ngon\n", "Ngày thứ 4 chúc hàng xóm ngủ ngon\n"]
# with open("./output.txt", "w", encoding="utf-8") as f:
#     f.writelines(lines)


# Vị dụ đọc file exce;
# with open("./users.csv", "r", encoding="utf-8") as f :
#     for line in f:
#         print(line)

# Path trong python