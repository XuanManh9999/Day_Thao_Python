# Tính chất kế thừa
# Khi lớp con kế thừa lớp cha thì lớp con đó sẽ có đầy đủ các thuộc tính và phương thức của lớp cha
# từ khoá pass tức là kế thừa
# super() -> nó tương tự như tên của lớp cơ sở

# Lớp cơ sở
# class NguoiDung:
#     def __init__(self, name, age):
#         print("Vào lớp cơ sở")
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}, {self.age}"


# class SinhVien(NguoiDung):
#     def __init__(self, name, age, msv):
#         print("Vào lớp giảng viên")
#         # self.name = name
#         # self.age = age
#         # kế thừa thuộc tính từ lớp cơ sở
#         NguoiDung.__init__(self, name, age)
#         self.msv = msv

#     def get_all_data(self):
#         return f"name: {self.name}; age: {self.age};msv {self.msv}"
        

# class GiaoVien(NguoiDung):
#     def __init__(self, name, age, mgv):
#         # self.name = name
#         # self.age = age
#         # lưu ý khi dùng từ khoá supper thì ta bỏ self đi
#         super().__init__(name, age)
#         self.mgv = mgv
#     def get_all_data(self):
#         return f"name: {self.name}; age: {self.age};mgv: {self.mgv}" 
    

# nguoi_dung = NguoiDung("Lớp cơ sở", 100)
# print(nguoi_dung)
# sinh_vien = SinhVien("Nguyễn Xuân Mạnh", 20, 20210794)
# print(sinh_vien)
# print(sinh_vien.get_all_data())

# giao_vien = GiaoVien("Nguyễn Thị Chí Phèo", 40, 113)
# print(giao_vien)
# print(giao_vien.get_all_data())



# Tính chất đa hình
# nếu lớp con có các thuộc tính, phương thức trùng tên với lớp cha. Thì lúc này hàm con sẽ ưu tiên hàm bên trong nó định nghĩa và ghi đè hàm đã được định nghĩa ở hàm cha
# Các tính chất con ghi đề cha thì người ta gọi là overr. orverLoadding
# orverLoadding khi hai 2 trùng tên thì nó sẽ lấy hàm mới nhất
# class NguoiDung:
#     address = "Hà Nội"
#     def __init__(self, name, age):
#         print("Vào lớp cơ sở")
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}, {self.age}"


# class SinhVien(NguoiDung):
#     # overr thuộc tính tĩnh
#     address = "Hải Phòng"
#     def __init__(self, name, age, msv):
#         print("Vào lớp sinh viên")
#         # self.name = name
#         # self.age = age
#         # kế thừa thuộc tính từ lớp cơ sở
#         NguoiDung.__init__(self, name, age)
#         self.msv = msv

#     # overrding (ghi đè hàm)
#     # def __str__(self):
#     #     return f"{self.name}, {self.age}, {self.msv}"
#     def __str__(self):
#         return NguoiDung.__str__(self) +  f" {self.msv}"

#     def get_all_data(self):
#         return f"name: {self.name}; age: {self.age};msv {self.msv}"

#     # overloading
#     def tinh_tong(self, a, b):
#         return a + b

#     def tinh_tong (self, a, b, c):
#         return a + b + c    
        

# class GiaoVien(NguoiDung):
    
#     def __init__(self, name, age, mgv):
#         # self.name = name
#         # self.age = age
#         # lưu ý khi dùng từ khoá supper thì ta bỏ self đi
#         super().__init__(name, age)
#         self.mgv = mgv
#     def get_all_data(self):
#         return f"name: {self.name}; age: {self.age};mgv: {self.mgv}" 


# sinh_vien = SinhVien("Nguyễn Xuân Mạnh", 20, 20210794)
# print(f"Dia chi: {sinh_vien.address}")
# print(sinh_vien)

# # print(sinh_vien.tinh_tong(1, 2))
# print(sinh_vien.tinh_tong(1, 2, 3))



# Đa kế thừa
# Một lớp có thể kế thừa từ nhiều lớp khác nhau, gọi là đa kế thừa
# Khi 2 lớp cha có 1 hàm có tên chung thì lớp con kế thừa sẽ lấy hàm đầu tiên của thằng nó kế thừa
# class A:
#     def __init__(self, a):
#         self.a = a

#     def show_b(self):
#         return self.a

# class B:
#     def __init__(self, b):
#         self.b = b

#     def show_b(self):
#         return self.b

# class C (A, B):
#     def __init__(self, a, b, c):
#         A.__init__(self, a)
#         B.__init__(self, b)
#         self.c = c
    
#     def show_all(self):
#         return f"a: {self.a}; b: {self.b}; c: {self.c}"


# c = C(1, 2, 3)

# print(c.show_all())
# print(c.show_b())

# Đa hình
# class A:
#     def __init__(self, a):
#         self.a = a

#     def show_a(self):
#         return self.a

# class B(A):
#     def __init__(self, a, b):
#         self.b = b
#         A.__init__(self, a)

#     def show_b(self):
#         return self.b

# class C (B):
#     def __init__(self, a, b, c):
#         B.__init__(self, a, b)
#         self.c = c
    
#     def show_all(self):
#         return f"a: {self.a}; b: {self.b}; c: {self.c}"


# c =  C(1, 2, 3)

# print(c.show_a())
# print(c.show_b())
# print(c.show_all())


# Xây dựng một chương trình quản lý người dùng (Sinh Vien, Giang Vien)
# id, ten, tuoi, dia_chi, so_cmnd, msv, diem_toan, diem_ly, diem_hoa -> Sinh Vien
# id, ten, tuoi, dia_chi, so_cmnd, mgv, mon_day, tham_nien -> Giang Viên

class BaseUser:
    def __init__(self, id, ten, tuoi, dia_chi, so_cmnd):
        self.id = id
        self.ten = ten
        self.tuoi = tuoi
        self.dia_chi = dia_chi
        self.so_cmnd = so_cmnd

    def __str__(self):
        return f"id: {self.id}, ten: {self.ten}, tuoi: {self.tuoi}, dia_chi: {self.dia_chi}, so_cmnd: {self.so_cmnd}"

class SinhVien(BaseUser):
    def __init__(self, id, ten, tuoi, dia_chi, so_cmnd, msv, diem_toan, diem_ly, diem_hoa):
        self.msv = msv
        self.diem_toan = diem_toan
        self.diem_hoa = diem_hoa
        self.diem_ly = diem_ly
        BaseUser.__init__(self, id, ten, tuoi, dia_chi, so_cmnd)


class GiangVien(BaseUser):
    def __init__(self, id, ten, tuoi, dia_chi, so_cmnd, mgv, mon_day, tham_nien):
        self.mgv = mgv
        self.mon_day = mon_day
        self.tham_nien = tham_nien
        BaseUser.__init__(self, id, ten, tuoi, dia_chi, so_cmnd)


ds_sv = []
ds_gv = []
while True:
    print("------------------------------------------")
    print("1. Để thêm sinh viên")
    print("2. Để thêm giảng viên")
    print("3. Để in sinh viên")
    print("4. Để in giảng viên")
    print("5. Tìm bạn sv có tuổi lớn nhất")
    print("0. Để thoát")
    print("------------------------------------------")
    n = int(input("Nhập vào lựa chọn của bạn: "))

    if n == 1:
        sl_sv = int(input("Nhập vào số lượng sinh viên cần thêm: "))
        for i in range(0, sl_sv, 1):
            id = (input("Nhập vào id: "))
            ten = (input("Nhập vào ten: "))
            tuoi = int(input("Nhập vào tuoi: "))
            dia_chi = (input("Nhập vào dia_chi: "))
            so_cmnd = (input("Nhập vào so_cmnd: "))
            msv = (input("Nhập vào msv: "))
            diem_toan = float(input("Nhập vào diem_toan: "))
            diem_ly = float(input("Nhập vào diem_ly: "))
            diem_hoa = float(input("Nhập vào diem_hoa: "))
            sv =  SinhVien(id, ten, tuoi, dia_chi, so_cmnd, msv, diem_toan, diem_ly, diem_hoa)
            ds_sv.append(sv)
    if n == 2:
        sl_sv = int(input("Nhập vào số lượng giảng viên cần thêm: "))
        for i in range(0, sl_sv, 1):
            id = (input("Nhập vào id: "))
            ten = (input("Nhập vào ten: "))
            tuoi = int(input("Nhập vào tuoi: "))
            dia_chi = (input("Nhập vào dia_chi: "))
            so_cmnd = (input("Nhập vào so_cmnd: "))
            mgv = (input("Nhập vào mgv: "))
            mon_day = (input("Nhập vào mon_day: "))
            tham_nien = float(input("Nhập vào tham_nien: "))
            sv =  GiangVien(id, ten, tuoi, dia_chi, so_cmnd, mgv, mon_day, tham_nien)
            ds_gv.append(sv)

    if n == 3:
        print("Danh sách sinh viên: ")
        for sv in ds_sv:
            print(sv)
    if n == 4:
        print("Danh sách giảng viên: ")
        for gv in ds_gv:
            print(gv)
    if n == 5:
        # Tìm cái lớn -> cho cờ nhỏ
        # Tìm cái nhỏ -> cho cờ lớn
        tuoi_lon_nhat = -1
        for sv in ds_sv:
            if tuoi_lon_nhat < sv.tuoi:
                tuoi_lon_nhat = sv.tuoi
        print("SV có tuổi lớn nhất là bạn")
        for sv in ds_sv:
            if sv.tuoi == tuoi_lon_nhat:
                print(sv)



    if n == 0:
        break
    




