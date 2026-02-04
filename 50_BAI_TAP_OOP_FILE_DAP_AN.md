# ĐÁP ÁN 50 BÀI TẬP ÔN TẬP PYTHON - OOP VÀ ĐỌC GHI FILE

---

## PHẦN I: OOP CƠ BẢN - CLASS VÀ OBJECT (Bài 1-10)

### Bài 1 (2 điểm): Tạo Class cơ bản

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

# Tạo đối tượng
name = input("Nhập tên: ")
age = int(input("Nhập tuổi: "))
grade = input("Nhập lớp: ")

student = Student(name, age, grade)
print(f"Thông tin: {student.name}, {student.age} tuổi, lớp {student.grade}")
```

---

### Bài 2 (2 điểm): Phương thức trong Class

```python
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        print(f"Tên: {self.name}, Tuổi: {self.age}, Lớp: {self.grade}")

# Sử dụng
student = Student("Nguyễn Văn A", 20, "12A1")
student.display_info()
```

---

### Bài 3 (3 điểm): Hàm __str__

```python
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self):
        return f"Sách: {self.title} - Tác giả: {self.author} - Giá: {self.price}đ"

# Sử dụng
book = Book("Python cơ bản", "Nguyễn Văn A", 150000)
print(book)
```

---

### Bài 4 (3 điểm): Thuộc tính mặc định

```python
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Tôi là {self.name}, {self.age} tuổi")

# Sử dụng
p1 = Person("Anh A")
p1.introduce()  # Tôi là Anh A, 18 tuổi

p2 = Person("Anh B", 25)
p2.introduce()  # Tôi là Anh B, 25 tuổi
```

---

### Bài 5 (3 điểm): Class với nhiều phương thức

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def display(self):
        print(f"Chiều rộng: {self.width}, Chiều dài: {self.height}")
        print(f"Diện tích: {self.area()}")
        print(f"Chu vi: {self.perimeter()}")

# Sử dụng
rect = Rectangle(5, 10)
rect.display()
```

---

### Bài 6 (3 điểm): Quản lý danh sách đối tượng

```python
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"ID: {self.id}, Tên: {self.name}, Giá: {self.price}đ"

# Nhập danh sách
n = int(input("Nhập số lượng sản phẩm: "))
products = []

for i in range(n):
    print(f"\nSản phẩm {i+1}:")
    id = input("ID: ")
    name = input("Tên: ")
    price = float(input("Giá: "))
    products.append(Product(id, name, price))

# In danh sách
print("\nDanh sách sản phẩm:")
for p in products:
    print(p)
```

---

### Bài 7 (4 điểm): Tìm kiếm trong danh sách đối tượng

```python
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"ID: {self.id}, Tên: {self.name}, Giá: {self.price}đ"

# Nhập danh sách (giống bài 6)
products = []
n = int(input("Nhập số lượng sản phẩm: "))
for i in range(n):
    id = input("ID: ")
    name = input("Tên: ")
    price = float(input("Giá: "))
    products.append(Product(id, name, price))

# Tìm theo tên
search_name = input("\nNhập tên sản phẩm cần tìm: ")
found = [p for p in products if search_name.lower() in p.name.lower()]
if found:
    print("Kết quả tìm kiếm:")
    for p in found:
        print(p)
else:
    print("Không tìm thấy!")

# Tìm giá cao nhất
if products:
    max_price_product = max(products, key=lambda x: x.price)
    print(f"\nSản phẩm giá cao nhất: {max_price_product}")
```

---

### Bài 8 (4 điểm): Sắp xếp danh sách đối tượng

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    
    def __str__(self):
        return f"Tên: {self.name}, Tuổi: {self.age}, Điểm: {self.score}"

# Nhập danh sách
n = int(input("Nhập số học sinh: "))
students = []

for i in range(n):
    print(f"\nHọc sinh {i+1}:")
    name = input("Tên: ")
    age = int(input("Tuổi: "))
    score = float(input("Điểm: "))
    students.append(Student(name, age, score))

# Sắp xếp theo điểm giảm dần
students.sort(key=lambda x: x.score, reverse=True)

# In kết quả
print("\nDanh sách học sinh (sắp xếp theo điểm):")
for s in students:
    print(s)
```

---

### Bài 9 (3 điểm): Thuộc tính Class (Class Variable)

```python
class Counter:
    count = 0  # Thuộc tính class
    
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

# Tạo các đối tượng
c1 = Counter()
c2 = Counter()
c3 = Counter()

print(f"Số lượng đối tượng đã tạo: {Counter.get_count()}")
```

---

### Bài 10 (4 điểm): Tính toán với đối tượng

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Đã nạp {amount}đ. Số dư hiện tại: {self.balance}đ")
        else:
            print("Số tiền không hợp lệ!")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Đã rút {amount}đ. Số dư hiện tại: {self.balance}đ")
            else:
                print("Số dư không đủ!")
        else:
            print("Số tiền không hợp lệ!")
    
    def display(self):
        print(f"Chủ tài khoản: {self.owner}")
        print(f"Số dư: {self.balance}đ")

# Sử dụng
account = BankAccount("Nguyễn Văn A", 1000000)
account.display()
account.deposit(500000)
account.withdraw(200000)
account.display()
```

---

## PHẦN II: STATIC METHOD VÀ CLASS METHOD (Bài 11-15)

### Bài 11 (3 điểm): Static Method cơ bản

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def power(a, b):
        return a ** b

# Gọi không cần tạo đối tượng
print(MathUtils.add(5, 3))  # 8
print(MathUtils.multiply(4, 7))  # 28
print(MathUtils.power(2, 8))  # 256
```

---

### Bài 12 (4 điểm): Static Method với xử lý chuỗi

```python
class StringHelper:
    @staticmethod
    def reverse_string(s):
        return s[::-1]
    
    @staticmethod
    def count_words(s):
        return len(s.split())
    
    @staticmethod
    def is_palindrome(s):
        s_clean = s.replace(" ", "").lower()
        return s_clean == s_clean[::-1]

# Sử dụng
text = "Hello World"
print(StringHelper.reverse_string(text))  # dlroW olleH
print(StringHelper.count_words(text))  # 2
print(StringHelper.is_palindrome("madam"))  # True
```

---

### Bài 13 (4 điểm): Class Method

```python
class Person:
    total_people = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def create_person(cls, name, age):
        cls.total_people += 1
        return cls(name, age)
    
    @classmethod
    def get_total(cls):
        return cls.total_people

# Sử dụng
p1 = Person.create_person("Anh A", 20)
p2 = Person.create_person("Anh B", 25)
p3 = Person.create_person("Anh C", 30)

print(f"Tổng số người đã tạo: {Person.get_total()}")  # 3
```

---

### Bài 14 (5 điểm): So sánh Static và Class Method

```python
class Calculator:
    version = "1.0"
    
    def __init__(self, version):
        self.version = version
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def create_calculator(cls, version):
        return cls(version)

# Static method: không cần đối tượng, không truy cập class/instance
result = Calculator.add(5, 3)
print(result)  # 8

# Class method: tạo đối tượng, có thể truy cập class variable
calc = Calculator.create_calculator("2.0")
print(calc.version)  # 2.0
```

---

### Bài 15 (4 điểm): Ứng dụng thực tế

```python
class DateUtils:
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    @staticmethod
    def days_in_month(month, year):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and DateUtils.is_leap_year(year):
            return 29
        return days[month - 1]
    
    @classmethod
    def from_string(cls, date_str):
        # Format: "dd/mm/yyyy"
        parts = date_str.split("/")
        return {
            "day": int(parts[0]),
            "month": int(parts[1]),
            "year": int(parts[2])
        }

# Sử dụng
print(DateUtils.is_leap_year(2024))  # True
print(DateUtils.days_in_month(2, 2024))  # 29
date = DateUtils.from_string("15/03/2024")
print(date)  # {'day': 15, 'month': 3, 'year': 2024}
```

---

## PHẦN III: ENCAPSULATION - ĐÓNG GÓI (Bài 16-23)

### Bài 16 (3 điểm): Public thuộc tính

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Public
        self.model = model  # Public
        self.year = year  # Public

# Truy cập trực tiếp
car = Car("Toyota", "Camry", 2023)
print(car.brand)  # Toyota
print(car.model)  # Camry
print(car.year)  # 2023
```

---

### Bài 17 (4 điểm): Private thuộc tính

```python
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # Private
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Số dư không thể âm!")

# Sử dụng
account = BankAccount(1000)
print(account.get_balance())  # 1000
account.set_balance(2000)
print(account.get_balance())  # 2000
# print(account.__balance)  # Lỗi! Không thể truy cập trực tiếp
```

---

### Bài 18 (4 điểm): Protected thuộc tính

```python
class Animal:
    def __init__(self, name, age):
        self._name = name  # Protected
        self._age = age  # Protected
    
    def display(self):
        print(f"Tên: {self._name}, Tuổi: {self._age}")

# Sử dụng (có thể truy cập nhưng không nên)
dog = Animal("Chó", 3)
dog.display()  # Tên: Chó, Tuổi: 3
# print(dog._name)  # Có thể nhưng không nên (vi phạm quy ước)
```

---

### Bài 19 (5 điểm): Getter và Setter hoàn chỉnh

```python
class Student:
    def __init__(self, name, age, score):
        self.__name = name
        self.set_age(age)
        self.set_score(score)
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_score(self):
        return self.__score
    
    def set_age(self, age):
        if 6 <= age <= 100:
            self.__age = age
        else:
            print("Tuổi phải từ 6 đến 100!")
            self.__age = 18  # Giá trị mặc định
    
    def set_score(self, score):
        if 0 <= score <= 10:
            self.__score = score
        else:
            print("Điểm phải từ 0 đến 10!")
            self.__score = 0  # Giá trị mặc định

# Sử dụng
student = Student("Anh A", 20, 8.5)
print(f"Tên: {student.get_name()}, Tuổi: {student.get_age()}, Điểm: {student.get_score()}")
student.set_age(25)
student.set_score(9.5)
```

---

### Bài 20 (5 điểm): Bảo vệ dữ liệu

```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.set_price(price)
        self.set_quantity(quantity)
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Giá không thể âm!")
            self.__price = 0
    
    def get_quantity(self):
        return self.__quantity
    
    def set_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity
        else:
            print("Số lượng không thể âm!")
            self.__quantity = 0
    
    def get_total(self):
        return self.__price * self.__quantity

# Sử dụng
product = Product("Laptop", 15000000, 5)
print(f"Tổng giá trị: {product.get_total()}đ")  # 75000000đ
product.set_price(-1000)  # Giá không thể âm!
```

---

### Bài 21 (4 điểm): Encapsulation với tính toán

```python
class Circle:
    def __init__(self, radius):
        self.set_radius(radius)
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        if radius >= 0:
            self.__radius = radius
        else:
            print("Bán kính không thể âm!")
            self.__radius = 0
    
    def area(self):
        return 3.14159 * self.__radius ** 2
    
    def circumference(self):
        return 2 * 3.14159 * self.__radius

# Sử dụng
circle = Circle(5)
print(f"Diện tích: {circle.area():.2f}")
print(f"Chu vi: {circle.circumference():.2f}")
```

---

### Bài 22 (5 điểm): Quản lý tài khoản ngân hàng

```python
class Account:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin
    
    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("PIN sai!")
            return False
        if amount > self.__balance:
            print("Số dư không đủ!")
            return False
        self.__balance -= amount
        print(f"Đã rút {amount}đ. Số dư còn lại: {self.__balance}đ")
        return True
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Đã nạp {amount}đ. Số dư: {self.__balance}đ")
        else:
            print("Số tiền không hợp lệ!")
    
    def check_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            print("PIN sai!")
            return None

# Sử dụng
account = Account(1000000, "1234")
account.deposit(500000)
account.withdraw(200000, "1234")
balance = account.check_balance("1234")
print(f"Số dư: {balance}đ")
```

---

### Bài 23 (6 điểm): Hệ thống đăng nhập

```python
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    def login(self, username, password):
        if username == self.__username and password == self.__password:
            print("Đăng nhập thành công!")
            return True
        else:
            print("Tên đăng nhập hoặc mật khẩu sai!")
            return False
    
    def change_password(self, old_pass, new_pass):
        if old_pass == self.__password:
            if len(new_pass) >= 6:
                self.__password = new_pass
                print("Đổi mật khẩu thành công!")
                return True
            else:
                print("Mật khẩu mới phải có ít nhất 6 ký tự!")
                return False
        else:
            print("Mật khẩu cũ không đúng!")
            return False

# Sử dụng
user = User("admin", "password123")
user.login("admin", "password123")  # Đăng nhập thành công!
user.change_password("password123", "newpass456")
user.login("admin", "newpass456")  # Đăng nhập thành công!
```

---

## PHẦN IV: INHERITANCE - KẾ THỪA (Bài 24-33)

### Bài 24 (3 điểm): Kế thừa cơ bản

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        Animal.__init__(self, name, age)
        self.breed = breed
    
    def display(self):
        print(f"Tên: {self.name}, Tuổi: {self.age}, Giống: {self.breed}")

# Sử dụng
dog = Dog("Lucky", 3, "Golden Retriever")
dog.display()
```

---

### Bài 25 (4 điểm): Kế thừa với super()

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def display(self):
        print(f"Tên: {self.name}, Tuổi: {self.age}, Mã SV: {self.student_id}")

# Sử dụng
student = Student("Nguyễn Văn A", 20, "SV001")
student.display()
```

---

### Bài 26 (4 điểm): Ghi đè phương thức

```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

# Sử dụng
rect = Rectangle(5, 10)
print(f"Diện tích hình chữ nhật: {rect.area()}")

circle = Circle(5)
print(f"Diện tích hình tròn: {circle.area():.2f}")
```

---

### Bài 27 (5 điểm): Kế thừa nhiều cấp

```python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

class ElectricCar(Car):
    def __init__(self, brand, year, doors, battery_capacity):
        super().__init__(brand, year, doors)
        self.battery_capacity = battery_capacity
    
    def display(self):
        print(f"Hãng: {self.brand}, Năm: {self.year}, Số cửa: {self.doors}, Pin: {self.battery_capacity}kWh")

# Sử dụng
ev = ElectricCar("Tesla", 2023, 4, 75)
ev.display()
```

---

### Bài 28 (5 điểm): Quản lý nhân viên

```python
class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return f"ID: {self.id}, Tên: {self.name}, Lương: {self.salary}đ"

class Manager(Employee):
    def __init__(self, id, name, salary, department):
        super().__init__(id, name, salary)
        self.department = department
    
    def __str__(self):
        return f"{super().__str__()}, Phòng ban: {self.department}"

class Developer(Employee):
    def __init__(self, id, name, salary, programming_language):
        super().__init__(id, name, salary)
        self.programming_language = programming_language
    
    def __str__(self):
        return f"{super().__str__()}, Ngôn ngữ: {self.programming_language}"

# Quản lý danh sách
employees = []
employees.append(Manager("M001", "Nguyễn Văn A", 20000000, "IT"))
employees.append(Developer("D001", "Trần Thị B", 15000000, "Python"))

for emp in employees:
    print(emp)
```

---

### Bài 29 (6 điểm): Đa kế thừa

```python
class Flyable:
    def fly(self):
        print("Đang bay...")

class Swimmable:
    def swim(self):
        print("Đang bơi...")

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Tên: {self.name}")

# Sử dụng
duck = Duck("Vịt trời")
duck.display()
duck.fly()  # Từ Flyable
duck.swim()  # Từ Swimmable

# Giải thích: Python sử dụng MRO (Method Resolution Order) để tìm phương thức
# Khi gọi duck.fly(), Python tìm trong Duck trước, sau đó Flyable, rồi Swimmable
```

---

### Bài 30 (5 điểm): Override __str__

```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Person: {self.name}"

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    
    def __str__(self):
        return f"Student: {self.name} - ID: {self.student_id}"

# Sử dụng
person = Person("Anh A")
print(person)  # Person: Anh A

student = Student("Anh B", "SV001")
print(student)  # Student: Anh B - ID: SV001
```

---

### Bài 31 (6 điểm): Hệ thống quản lý thư viện

```python
class Item:
    def __init__(self, id, title):
        self.id = id
        self.title = title

class Book(Item):
    def __init__(self, id, title, author, pages):
        super().__init__(id, title)
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"ID: {self.id}, Sách: {self.title}, Tác giả: {self.author}, Số trang: {self.pages}"

class Magazine(Item):
    def __init__(self, id, title, issue_number):
        super().__init__(id, title)
        self.issue_number = issue_number
    
    def __str__(self):
        return f"ID: {self.id}, Tạp chí: {self.title}, Số: {self.issue_number}"

# Quản lý
library = []

while True:
    print("\n1. Thêm sách")
    print("2. Thêm tạp chí")
    print("3. Tìm theo tên")
    print("4. Hiển thị tất cả")
    print("0. Thoát")
    
    choice = input("Chọn: ")
    
    if choice == "1":
        id = input("ID: ")
        title = input("Tên sách: ")
        author = input("Tác giả: ")
        pages = int(input("Số trang: "))
        library.append(Book(id, title, author, pages))
    
    elif choice == "2":
        id = input("ID: ")
        title = input("Tên tạp chí: ")
        issue = input("Số: ")
        library.append(Magazine(id, title, issue))
    
    elif choice == "3":
        search = input("Nhập tên cần tìm: ")
        found = [item for item in library if search.lower() in item.title.lower()]
        for item in found:
            print(item)
    
    elif choice == "4":
        for item in library:
            print(item)
    
    elif choice == "0":
        break
```

---

### Bài 32 (5 điểm): Tính đa hình với kế thừa

```python
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Gâu gâu!")

class Cat(Animal):
    def make_sound(self):
        print("Meo meo!")

class Bird(Animal):
    def make_sound(self):
        print("Chíp chíp!")

# Sử dụng đa hình
animals = [Dog(), Cat(), Bird()]

for animal in animals:
    animal.make_sound()
# Output:
# Gâu gâu!
# Meo meo!
# Chíp chíp!
```

---

### Bài 33 (6 điểm): Hệ thống thanh toán

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(Payment):
    def pay(self, amount):
        print(f"Thanh toán {amount}đ bằng tiền mặt")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Thanh toán {amount}đ bằng thẻ")

class MomoPayment(Payment):
    def pay(self, amount):
        print(f"Thanh toán {amount}đ bằng Momo")

# Sử dụng
payments = [CashPayment(), CardPayment(), MomoPayment()]
amount = 100000

for payment in payments:
    payment.pay(amount)
```

---

## PHẦN V: POLYMORPHISM - ĐA HÌNH (Bài 34-38)

### Bài 34 (4 điểm): Đa hình với phương thức

```python
class Shape:
    def calculate_area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14159 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height

# Tính tổng diện tích
shapes = [
    Rectangle(5, 10),
    Circle(5),
    Triangle(4, 6)
]

total_area = sum(shape.calculate_area() for shape in shapes)
print(f"Tổng diện tích: {total_area:.2f}")
```

---

### Bài 35 (5 điểm): Đa hình với toán tử

```python
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)
    
    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)
    
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

# Sử dụng
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

print(f1 + f2)  # 5/6
print(f1 - f2)  # 1/6
print(f1 * f2)  # 1/6
```

---

### Bài 36 (5 điểm): Đa hình trong thực tế

```python
class MediaPlayer:
    def play(self):
        pass

class AudioPlayer(MediaPlayer):
    def play(self):
        print("Đang phát audio...")

class VideoPlayer(MediaPlayer):
    def play(self):
        print("Đang phát video...")

# Sử dụng
players = [AudioPlayer(), VideoPlayer()]

for player in players:
    player.play()
```

---

### Bài 37 (6 điểm): Hệ thống vận chuyển

```python
class Transport:
    def deliver(self, distance):
        pass

class Truck(Transport):
    def __init__(self, speed=60):
        self.speed = speed
    
    def deliver(self, distance):
        time = distance / self.speed
        print(f"Xe tải vận chuyển {distance}km trong {time:.2f} giờ")

class Ship(Transport):
    def __init__(self, speed=30):
        self.speed = speed
    
    def deliver(self, distance):
        time = distance / self.speed
        print(f"Tàu vận chuyển {distance}km trong {time:.2f} giờ")

class Plane(Transport):
    def __init__(self, speed=800):
        self.speed = speed
    
    def deliver(self, distance):
        time = distance / self.speed
        print(f"Máy bay vận chuyển {distance}km trong {time:.2f} giờ")

# Sử dụng
transports = [Truck(), Ship(), Plane()]
distance = 1200

for transport in transports:
    transport.deliver(distance)
```

---

### Bài 38 (5 điểm): Đa hình với list

```python
class Employee:
    def calculate_salary(self):
        return 0

class FullTimeEmployee(Employee):
    def __init__(self, base_salary):
        self.base_salary = base_salary
    
    def calculate_salary(self):
        return self.base_salary

class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate, hours):
        self.hourly_rate = hourly_rate
        self.hours = hours
    
    def calculate_salary(self):
        return self.hourly_rate * self.hours

# Tính tổng lương
employees = [
    FullTimeEmployee(10000000),
    PartTimeEmployee(50000, 80),
    FullTimeEmployee(12000000),
    PartTimeEmployee(60000, 60)
]

total_salary = sum(emp.calculate_salary() for emp in employees)
print(f"Tổng lương: {total_salary:,}đ")
```

---

## PHẦN VI: ABSTRACTION - TRỪU TƯỢNG (Bài 39-43)

### Bài 39 (5 điểm): Abstract Class cơ bản

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

# Sử dụng
rect = Rectangle(5, 10)
print(f"Diện tích: {rect.area()}")

circle = Circle(5)
print(f"Diện tích: {circle.area():.2f}")
```

---

### Bài 40 (6 điểm): Abstract Class với nhiều phương thức

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    def sleep(self):
        print("Đang ngủ")

class Dog(Animal):
    def make_sound(self):
        print("Gâu gâu!")
    
    def move(self):
        print("Chạy bằng 4 chân")

class Cat(Animal):
    def make_sound(self):
        print("Meo meo!")
    
    def move(self):
        print("Đi nhẹ nhàng")

# Sử dụng
dog = Dog()
dog.make_sound()
dog.move()
dog.sleep()
```

---

### Bài 41 (6 điểm): Hệ thống Database

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def query(self, sql):
        pass
    
    @abstractmethod
    def close(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Kết nối MySQL...")
    
    def query(self, sql):
        print(f"Thực thi MySQL: {sql}")
    
    def close(self):
        print("Đóng kết nối MySQL")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Kết nối PostgreSQL...")
    
    def query(self, sql):
        print(f"Thực thi PostgreSQL: {sql}")
    
    def close(self):
        print("Đóng kết nối PostgreSQL")

# Sử dụng
db = MySQLDatabase()
db.connect()
db.query("SELECT * FROM users")
db.close()
```

---

### Bài 42 (7 điểm): Hệ thống Plugin

```python
from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def execute(self):
        pass

class TextPlugin(Plugin):
    def execute(self):
        print("Xử lý văn bản...")

class ImagePlugin(Plugin):
    def execute(self):
        print("Xử lý hình ảnh...")

class VideoPlugin(Plugin):
    def execute(self):
        print("Xử lý video...")

# Quản lý plugin
plugins = [TextPlugin(), ImagePlugin(), VideoPlugin()]

for plugin in plugins:
    plugin.execute()
```

---

### Bài 43 (6 điểm): Template Method Pattern

```python
from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate_header(self):
        pass
    
    @abstractmethod
    def generate_body(self):
        pass
    
    @abstractmethod
    def generate_footer(self):
        pass
    
    def generate(self):
        self.generate_header()
        self.generate_body()
        self.generate_footer()

class PDFReport(Report):
    def generate_header(self):
        print("=== PDF Header ===")
    
    def generate_body(self):
        print("PDF Body Content")
    
    def generate_footer(self):
        print("=== PDF Footer ===")

class HTMLReport(Report):
    def generate_header(self):
        print("<html><head><title>Report</title></head><body>")
    
    def generate_body(self):
        print("<p>HTML Body Content</p>")
    
    def generate_footer(self):
        print("</body></html>")

# Sử dụng
pdf = PDFReport()
pdf.generate()

html = HTMLReport()
html.generate()
```

---

## PHẦN VII: ĐỌC GHI FILE (Bài 44-50)

### Bài 44 (3 điểm): Đọc file cơ bản

```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

---

### Bài 45 (4 điểm): Đọc file theo dòng

```python
count = 0
with open("students.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
        count += 1

print(f"\nTổng số học sinh: {count}")
```

---

### Bài 46 (4 điểm): Ghi file cơ bản

```python
n = int(input("Nhập số dòng: "))
lines = []

for i in range(n):
    line = input(f"Dòng {i+1}: ")
    lines.append(line + "\n")

with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Đã ghi file thành công!")
```

---

### Bài 47 (5 điểm): Ghi thêm vào file

```python
from datetime import datetime

event = input("Nhập sự kiện: ")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("log.txt", "a", encoding="utf-8") as f:
    f.write(f"Thời gian: {current_time} - Sự kiện: {event}\n")

print("Đã ghi log thành công!")
```

---

### Bài 48 (6 điểm): Quản lý danh sách học sinh với file

```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    
    def __str__(self):
        return f"{self.name},{self.age},{self.score}"
    
    @staticmethod
    def from_string(s):
        parts = s.strip().split(",")
        return Student(parts[0], int(parts[1]), float(parts[2]))

# Lưu vào file
def save_students(students, filename="students.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for student in students:
            f.write(str(student) + "\n")

# Đọc từ file
def load_students(filename="students.txt"):
    students = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    students.append(Student.from_string(line))
    except FileNotFoundError:
        print("File chưa tồn tại!")
    return students

# Chương trình chính
students = load_students()

while True:
    print("\n1. Thêm học sinh")
    print("2. Hiển thị danh sách")
    print("3. Lưu và thoát")
    choice = input("Chọn: ")
    
    if choice == "1":
        name = input("Tên: ")
        age = int(input("Tuổi: "))
        score = float(input("Điểm: "))
        students.append(Student(name, age, score))
    
    elif choice == "2":
        for s in students:
            print(f"Tên: {s.name}, Tuổi: {s.age}, Điểm: {s.score}")
    
    elif choice == "3":
        save_students(students)
        break
```

---

### Bài 49 (7 điểm): Hệ thống quản lý sản phẩm với file

```python
class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.id},{self.name},{self.price},{self.quantity}"
    
    @staticmethod
    def from_string(s):
        parts = s.strip().split(",")
        return Product(parts[0], parts[1], float(parts[2]), int(parts[3]))

def save_products(products, filename="products.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for p in products:
            f.write(str(p) + "\n")

def load_products(filename="products.txt"):
    products = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    products.append(Product.from_string(line))
    except FileNotFoundError:
        pass
    return products

def find_product(products, name):
    return [p for p in products if name.lower() in p.name.lower()]

def update_product(products, id, new_price, new_quantity):
    for p in products:
        if p.id == id:
            p.price = new_price
            p.quantity = new_quantity
            return True
    return False

# Chương trình chính
products = load_products()

while True:
    print("\n1. Thêm sản phẩm")
    print("2. Hiển thị danh sách")
    print("3. Tìm sản phẩm")
    print("4. Cập nhật sản phẩm")
    print("5. Lưu và thoát")
    choice = input("Chọn: ")
    
    if choice == "1":
        id = input("ID: ")
        name = input("Tên: ")
        price = float(input("Giá: "))
        quantity = int(input("Số lượng: "))
        products.append(Product(id, name, price, quantity))
    
    elif choice == "2":
        for p in products:
            print(f"ID: {p.id}, Tên: {p.name}, Giá: {p.price}đ, SL: {p.quantity}")
    
    elif choice == "3":
        name = input("Nhập tên cần tìm: ")
        found = find_product(products, name)
        for p in found:
            print(f"ID: {p.id}, Tên: {p.name}, Giá: {p.price}đ")
    
    elif choice == "4":
        id = input("ID sản phẩm: ")
        new_price = float(input("Giá mới: "))
        new_quantity = int(input("Số lượng mới: "))
        if update_product(products, id, new_price, new_quantity):
            print("Cập nhật thành công!")
        else:
            print("Không tìm thấy!")
    
    elif choice == "5":
        save_products(products)
        break
```

---

### Bài 50 (8 điểm): Dự án tổng hợp - Quản lý thư viện

```python
class Book:
    def __init__(self, id, title, author, year, status="available"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status  # "available" hoặc "borrowed"
    
    def __str__(self):
        return f"{self.id},{self.title},{self.author},{self.year},{self.status}"
    
    @staticmethod
    def from_string(s):
        parts = s.strip().split(",")
        return Book(parts[0], parts[1], parts[2], parts[3], parts[4])

def save_books(books, filename="library.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for book in books:
            f.write(str(book) + "\n")

def load_books(filename="library.txt"):
    books = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    books.append(Book.from_string(line))
    except FileNotFoundError:
        pass
    return books

def find_books(books, keyword):
    return [b for b in books if keyword.lower() in b.title.lower() or keyword.lower() in b.author.lower()]

def borrow_book(books, id):
    for book in books:
        if book.id == id:
            if book.status == "available":
                book.status = "borrowed"
                return True
            else:
                return False
    return None

def return_book(books, id):
    for book in books:
        if book.id == id:
            if book.status == "borrowed":
                book.status = "available"
                return True
            else:
                return False
    return None

def get_borrowed_books(books):
    return [b for b in books if b.status == "borrowed"]

def statistics(books):
    total = len(books)
    borrowed = len(get_borrowed_books(books))
    available = total - borrowed
    return total, borrowed, available

# Chương trình chính
books = load_books()

while True:
    print("\n=== QUẢN LÝ THƯ VIỆN ===")
    print("1. Thêm sách mới")
    print("2. Tìm sách theo tên/tác giả")
    print("3. Mượn sách")
    print("4. Trả sách")
    print("5. Danh sách sách đang mượn")
    print("6. Thống kê")
    print("7. Hiển thị tất cả")
    print("0. Thoát")
    
    choice = input("Chọn: ")
    
    if choice == "1":
        id = input("ID: ")
        title = input("Tên sách: ")
        author = input("Tác giả: ")
        year = input("Năm: ")
        books.append(Book(id, title, author, year))
        save_books(books)
        print("Đã thêm sách!")
    
    elif choice == "2":
        keyword = input("Nhập tên hoặc tác giả: ")
        found = find_books(books, keyword)
        if found:
            for b in found:
                print(f"ID: {b.id}, Tên: {b.title}, Tác giả: {b.author}, Trạng thái: {b.status}")
        else:
            print("Không tìm thấy!")
    
    elif choice == "3":
        id = input("ID sách cần mượn: ")
        result = borrow_book(books, id)
        if result is True:
            save_books(books)
            print("Đã mượn sách!")
        elif result is False:
            print("Sách đã được mượn!")
        else:
            print("Không tìm thấy sách!")
    
    elif choice == "4":
        id = input("ID sách cần trả: ")
        result = return_book(books, id)
        if result is True:
            save_books(books)
            print("Đã trả sách!")
        elif result is False:
            print("Sách chưa được mượn!")
        else:
            print("Không tìm thấy sách!")
    
    elif choice == "5":
        borrowed = get_borrowed_books(books)
        if borrowed:
            print("\nDanh sách sách đang mượn:")
            for b in borrowed:
                print(f"ID: {b.id}, Tên: {b.title}, Tác giả: {b.author}")
        else:
            print("Không có sách nào đang mượn")
    
    elif choice == "6":
        total, borrowed, available = statistics(books)
        print(f"\n=== THỐNG KÊ ===")
        print(f"Tổng số sách: {total}")
        print(f"Số sách đã mượn: {borrowed}")
        print(f"Số sách còn lại: {available}")
    
    elif choice == "7":
        print("\nDanh sách tất cả sách:")
        for b in books:
            print(f"ID: {b.id}, Tên: {b.title}, Tác giả: {b.author}, Năm: {b.year}, Trạng thái: {b.status}")
    
    elif choice == "0":
        save_books(books)
        print("Cảm ơn đã sử dụng!")
        break
```

---

## TỔNG KẾT

Đã hoàn thành 50 bài tập với đáp án chi tiết!

**Mẹo làm bài:**
1. Hiểu rõ từng tính chất OOP trước khi làm
2. Thực hành nhiều với class và object
3. Nắm vững cách đọc ghi file
4. Test với nhiều trường hợp
5. Code phải rõ ràng, có comment

**Chúc em học tốt!**

