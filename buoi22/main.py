# Lập trình hướng đối tượng (OOP - Object Oriented Programming) là mô hình lập trình dựa trên khái niệm lớp 
# (class) và đối tượng (object), tập trung vào các đối tượng dữ liệu thay vì logic xử lý. 
# Nó giúp code dễ quản lý, tái sử dụng và bảo trì thông qua 4 tính chất cốt lõi: đóng gói, kế thừa, đa hình và trừu tượng

# 4 Nguyên tắc cốt lõi (4 pillars of OOP)
# Tính đóng gói (Encapsulation): Che giấu thông tin nội bộ của đối tượng, chỉ cho phép truy cập qua các phương thức công khai, giúp tăng bảo mật.
# Tính kế thừa (Inheritance): Cho phép một lớp con tái sử dụng các thuộc tính và phương thức của lớp cha, giúp giảm thiểu code lặp lại.
# Tính đa hình (Polymorphism): Các đối tượng khác nhau có thể thực hiện cùng một hành vi theo các cách khác nhau (ví dụ: cùng phương thức 'di chuyển' nhưng 'chim' thì bay, 'cá' thì bơi).
# Tính trừu tượng (Abstraction): Tập trung vào các đặc điểm chung, bỏ qua các chi tiết phức tạp không cần thiết, giúp mô hình hóa dễ dàng hơn. 


# for i in range(1, 11, 1):
#     print(i)

# class ten_class:
    # thuộc tính (đặc điểm cơ quản  bộ phân...)
    # hàm khởi tạo (nếu không có python nó sẽ tự định nghĩa 1 hàm tạo không có tham số)
    # phương thức (hoạt động)
    
# Đối tượng con người. 
# Thuộc tính: chân, tay,  mắt,  mũi,  tên,   số cmnd..
# Hàm khởi tạo: hàm giúp tạo ra đối tượng đó,  và dùng để set các giá  trị vào  thuộc   tính
# Phương thức: đi học,  đi làm, đứng lên, ngồi xuống, thanh toán...

# class Person:
#     #  Thuộc tính, có thể không có giá trị hoặc là gán giá trị mặc
#     species = "Canis familiaris" # Giá  trị mặc định, và nó sẽ thuộc về cả lớp, và đối tượng
#     # Hàm khởi tạo
#     # print("Ở  trên hàm init")
#     def __init__(self, name, age = 22):
#         print("Ở trong  hàm init")
#         # self này đại diện cho chính đối tượng Person
#         self.name =  name
#         self.age = age
#     # def Person(self, name, age,  cmnd, price):
#     #     self.name  =  name
#     #     self.age =  age
#     #     self.cmnd  = cmnd
#     #     self.price =  price
#     # print("Ở  dười hàm init")
#     # Phương thức nó là hàm (bên trong class người ta gọi là phương thức)
#     def info(self):
#         print(f"Hello: {self.name}, age: {self.age}, species: {self.species}")
        
#     def __str__(self):
#         return f"{self.name}; {self.age}"
        
# Cách dùng class để tạo  nên  đối  tượng
# manh = Person("Mạnh", 25)
# thao = Person("Thảo", 20)
# em_ham_xom = Person("Hàng  xóm")
# mong_co = Person("Mông cổ", 25,  123, 200)
# print(manh.name)
# print(manh.age)
# manh.info()
# thao.info()
# em_ham_xom.info()
# print(manh.species)
# print(Person.species)
# mong_co.info()
# class là gì?: nó là nguyên mẫu,  nó là đại diện cho lớp  chung
# đối tượng là gì?: nó là từng các thành phần (cá thể) được tạo nên từ lớp    
# Loài người -> nó là một lớp chung  có các thông tin đại diện cho toàn bộ đối  tượng người
# Đối tượng -> anh, em, tổng thống mỹ, cô hàng xóm
# Chốt lại
# Ta chỉ có thể gọi các  phương thức, và thuộc  tính bằng cách sử dụng đối tượng được tạo ra từ lơp


# manh = Person("Khánh", 25)

# print(manh)
# Nếu muốn khi in ra đối tượng  nó không còn là dạng ô nhớ ta dùng hàm def __str__(self)


# anitaion. @staticmethod,  @classmethod
# tên lớp bắt buộc chữ cái đầu phải viết hoa

# Static Method (@staticmethod):
# Định nghĩa: Sử dụng decorator @staticmethod. Không nhận tham số bắt buộc self (đối tượng) hay cls (lớp).
# Đặc điểm: Không thể thay đổi trạng thái của đối tượng hay lớp.
# Cách dùng: Sử dụng cho các hàm tiện ích (utility functions) liên quan đến lớp nhưng không cần dữ liệu cụ thể từ lớp hay đối tượng.

# Class Method (@classmethod):
# Định nghĩa: Sử dụng decorator @classmethod. Nhận tham số cls làm tham số đầu tiên, đại diện cho bản thân lớp đó.
# Đặc điểm: Có thể truy cập và sửa đổi trạng thái của lớp (biến lớp), nhưng không truy cập được biến của đối tượng.
# Cách dùng: Thường dùng để tạo các hàm khởi tạo thay thế hoặc các phương thức hoạt động trên dữ liệu của toàn bộ lớp.

# Đặc điểm	Instance Method	Class Method	Static Method
# Decorator	Không	@classmethod	@staticmethod
# Tham số ẩn	self (đối tượng)	cls (lớp)	Không có
# Truy cập Instance	Có	Không	Không
# Truy cập Class	Có	Có	Không
# Cách gọi	obj.method()	Class.method()	Class.method()



# class Calculator:
#     @staticmethod
#     def add(a, b):
#         return a + b
# tinh_tong = Calculator.add(1, 2)

# print(tinh_tong)

# import math

# print(math.sqrt(3))

# class Tinh_Toan:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     @staticmethod
#     def tong (a, b):
#         return a +  b
#     @staticmethod
#     def hieu(a, b):
#         return a - b
    

    
# tinh_toan = Tinh_Toan(1, 2)
# # sử dụng đối tượng
# print(tinh_toan.tong(5, 2))
# print(tinh_toan.hieu(7, 1))
# print(tinh_toan.tich())
# # sử dụng lớp
# print(Tinh_Toan.hieu(7, 1))
# print(Tinh_Toan.hieu(7, 10))


# class MyClass:
#     count = 0 # giá trị mặc định
#     # Hàm  khởi tạo
#     def __init__(self):
#         pass
#     @classmethod
#     def increment(cls):
#         cls.count += 1

# # Một lớp khi chưa được khai báo hàm khởi tạo __init__ thì mặc định python sẽ tạo cho nó 1 hàm khởi tạo rộng
# my_class = MyClass()
# my_class.increment()
# my_class.increment()
# print(f"Đối tượng: {my_class.count}")


# MyClass.increment()
# MyClass.increment()
# MyClass.increment()
# MyClass.increment()

# print(f"Lớp: {MyClass.count}")



# Xây dựng ứng dụng quản lý người dùng
# class User:
#     # Hàm khởi tạo
#     def __init__(self, name, age, address, point):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.point =  point
    
#     def __str__(self):
#         return f"name: {self.name}; age: {self.age}; address: {self.address}; point: {self.point}"


# # thêm sv
# datas = []
# for i in range(0, 2, 1):
#     name = input("Nhập vào tên: ")
#     age = int(input("Nhập vào tuổi: "))
#     address = input("Nhập vào address: ")
#     point = float(input("Nhập vào point: "))
#     sv =  User(name, age, address, point) # truyền vào hàm tạo để khởi tạo  đối tượng
#     datas.append(sv) # thêm vào mảng


# # sx theo  tuổi tăng  dần
# datas.sort(key=lambda u : u.age)
# for  user in datas:
#     print(user)
# # print(results)


# class Person:
#     # thuộc tính tĩnh
#     con_meo = "Múp" # dùng cho cả đối tượng và lớp
#     def __init__(self, name):
#         self.ho_va_ten = name # thuộc tính
#         pass
    
#     # thuộc về đối tượng
#     def sleep(self):
#         print("Người đang ngủ")
    
    
#     # thuộc về lớp
#     # @staticmethod
#     def eat():
#         print("Người đang ăn")
        
# person = Person("Mạnh") # đối tượng được tạo ra từ lớp


# thuộc về đối tượng
# print(person.ho_va_ten)
# person.sleep()
# person.eat()
# print(person.con_meo)

# thuộc về lớp
# Person.eat()
# print(Person.con_meo)
# Person.eat()
# lúc nào thì lớp truy cập được
# lúc nào dùng đối tượng truy cập
# đối tượng có thể truy cập vào thuộc tính + phương thức miễn là có dùng self và khác @staticmethod (phương thức tĩnh (thuộc về lớp))
# đối  với lớp,  không cần self 


# 4 Tính chất trong lập trình hướng đối tượng
# Lập trình hướng đối tượng (OOP – Object-Oriented Programming) là một phương pháp lập trình được sử dụng rộng rãi trong phát triển phần mềm hiện đại. 
# OOP tập trung vào việc tổ chức mã nguồn thành các đối tượng, mỗi đối tượng có thể chứa dữ liệu và các phương thức để thao tác với dữ liệu đó. 
# Một trong những yếu tố quan trọng giúp OOP trở thành một công cụ mạnh mẽ và dễ dàng quản lý trong việc phát triển phần mềm là bốn tính chất cơ bản của nó:
#     Encapsulation (Đóng gói), Abstraction (Trừu tượng hóa), Inheritance (Kế thừa) và Polymorphism (Đa hình).

# Tính đóng gói (Encapsulation)
# Encapsulation (hay còn gọi là đóng gói) là một trong những tính chất cơ bản của lập trình hướng đối tượng. Đóng gói liên quan đến việc nhóm dữ liệu 
# (các thuộc tính) và các phương thức (hành vi) có liên quan lại với nhau thành một đối tượng duy nhất. Đối tượng này có thể ẩn đi chi tiết triển khai bên 
# trong và chỉ cung cấp một giao diện công khai để người sử dụng tương tác với nó.

# Một trong những mục tiêu chính của đóng gói là bảo vệ dữ liệu khỏi sự thay đổi không mong muốn và không kiểm soát. Điều này được thực hiện thông qua cơ 
# chế quyền truy cập. Các trường dữ liệu của một lớp có thể được khai báo là private hoặc protected, nghĩa là chúng không thể bị truy cập trực tiếp từ bên
# ngoài lớp. Thay vào đó, các phương thức getter và setter sẽ được sử dụng để truy xuất và sửa đổi giá trị của các trường này.

# Trong python gồm có 3 loại phạm vi:
# public: công khai (đây là mặc định hiện tại)
# protected: _ (chỉ truy cập được trong phạm vi lớp và kế thừa nếu có) kế thừa
# private: __ (chỉ có thể truy cập trong lớp) riêng tư

# public: công khai (đây là mặc định hiện tại)
# class Animal:
#     def __init__(self, name, desc, age):
#         self.name = name
#         self.desc = desc
#         self.age =  age
#         pass
    
#     def __str__(self):
#         return f"name: {self.name}; desc: {self.desc}; {self.age}"
    
    
# # Vói public  thì mặc định  khi tạo 1 đối tương ta có thể truy cấp được  full giá trị  mà nó thuộc về
# dog = Animal("Chó nhà", "chó vịnh bắc bộ", 5)

# print(dog.name)
# print(dog.desc)
# print(dog.age)
# print(dog)


# private: phạm vi riêng tư
# class Animal:
#     # bên trong
#     def __init__(self, name, desc, age):
#         self.__name = name # private: chỉ có thể dùng được ở bên trong lớp
#         self.desc = desc
#         self.age =  age
#         pass
#     # def __sleep(self):
#     #     print("Còn mèo béo")
#     # getter
#     def get_name(self):
#         return self.__name
#     def __str__(self):
#         return f"name: {self.__name}; desc: {self.desc}; {self.age}"
    

# # Bên ngoài
# dog = Animal("Chó nhà", "chó vịnh bắc bộ", 5)
# dog.__sleep()
# print(f"dog: {dog}")
# print(dog.__name) # gọi thuộc tính trực  tiếp error
# print(dog.name)
# print(dog.desc)
# print(dog.age)
# print(dog)
# # print(Animal.name)
# print(dog.get_name()) # gọi phương  thức có chứa giá trị private



# protected: phạm vi kết thừa  (protected) _. chỉ sử dụng được ở bên trong lớp đó và các lớp kế thừa nó nếu có
# class Animal:
#     def __init__(self, name, desc, age):
#         self._name = name # phạm vi protected 
#         self.age = age
#         self.desc = desc
#         pass
#     def _sleep(self):
#         print("Ngủ")
    
    
# con_meo  = Animal("Mèo mướp", 'Việt Nam', 2)


# print(con_meo._name) # không nên làm vì vi phạm quy ước

# con_meo._sleep()


# Xử lý tiền của  ngân hàng

# hệ thông ngân hàng
# class Payment:
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price
#         pass
#     def tru_tien(self, so_tien):
#         self.__price -=  so_tien
#     def so_tien_con_lai(self):
#         return self.__price
#     def ban_tien(self, so_tien_ban):
#         self.__price  += so_tien_ban
    

# # bên  ngoài
# bo_thao = Payment("Bố thảo", 1000)
# # mua sắm
# # bo_thao.__price -= 500
# bo_thao.tru_tien(1000)
# # hack tên
# # bo_thao.price  += 100000
# # bo_thao.__price += 50000000
# bo_thao.ban_tien(5000)

# print(bo_thao.so_tien_con_lai())


# Tính chất kế thừa

# Tính chất đa hình

# Tính chất trừu tượng