# 50 BÀI TẬP ÔN TẬP PYTHON - OOP VÀ ĐỌC GHI FILE

**Mục đích:** Ôn tập kiến thức về Lập trình hướng đối tượng (OOP) và Đọc ghi file  
**Độ khó:** Từ cơ bản đến nâng cao  
**Thời gian:** Làm dần, không giới hạn

---

## HƯỚNG DẪN

1. Làm bài theo thứ tự hoặc chọn chủ đề muốn ôn
2. Mỗi bài tập có số điểm và yêu cầu rõ ràng
3. Code phải chạy được, có nhập xuất đầy đủ
4. Tham khảo đáp án sau khi tự làm

---

## PHẦN I: OOP CƠ BẢN - CLASS VÀ OBJECT (Bài 1-10)

### Bài 1 (2 điểm): Tạo Class cơ bản
Tạo class `Student` với các thuộc tính: `name`, `age`, `grade`.  
Viết hàm khởi tạo `__init__` để nhận 3 tham số trên.  
Tạo đối tượng và in thông tin.

**Ví dụ:**
```
Nhập tên: Nguyễn Văn A
Nhập tuổi: 20
Nhập lớp: 12A1
Thông tin: Nguyễn Văn A, 20 tuổi, lớp 12A1
```

---

### Bài 2 (2 điểm): Phương thức trong Class
Mở rộng class `Student` ở bài 1, thêm phương thức `display_info()` để hiển thị thông tin học sinh.

---

### Bài 3 (3 điểm): Hàm __str__
Tạo class `Book` với thuộc tính: `title`, `author`, `price`.  
Viết hàm `__str__` để khi in đối tượng sẽ hiển thị: "Sách: [title] - Tác giả: [author] - Giá: [price]đ"

---

### Bài 4 (3 điểm): Thuộc tính mặc định
Tạo class `Person` với:
- Thuộc tính: `name`, `age` (mặc định = 18)
- Hàm khởi tạo nhận `name` và `age` (có thể không truyền)
- Phương thức `introduce()` in ra: "Tôi là [name], [age] tuổi"

---

### Bài 5 (3 điểm): Class với nhiều phương thức
Tạo class `Rectangle` với:
- Thuộc tính: `width`, `height`
- Phương thức `area()`: tính diện tích
- Phương thức `perimeter()`: tính chu vi
- Phương thức `display()`: hiển thị thông tin

---

### Bài 6 (3 điểm): Quản lý danh sách đối tượng
Tạo class `Product` với: `id`, `name`, `price`.  
Nhập n sản phẩm, lưu vào list. In danh sách sản phẩm.

---

### Bài 7 (4 điểm): Tìm kiếm trong danh sách đối tượng
Mở rộng bài 6, thêm chức năng:
- Tìm sản phẩm theo tên
- Tìm sản phẩm có giá cao nhất

---

### Bài 8 (4 điểm): Sắp xếp danh sách đối tượng
Cho class `Student` (name, age, score).  
Nhập n học sinh, sắp xếp theo điểm giảm dần và in ra.

---

### Bài 9 (3 điểm): Thuộc tính Class (Class Variable)
Tạo class `Counter` với:
- Thuộc tính class `count = 0`
- Mỗi khi tạo đối tượng mới, `count` tăng lên 1
- Phương thức `get_count()` trả về số lượng đối tượng đã tạo

---

### Bài 10 (4 điểm): Tính toán với đối tượng
Tạo class `BankAccount` với:
- Thuộc tính: `owner`, `balance` (số dư)
- Phương thức `deposit(amount)`: nạp tiền
- Phương thức `withdraw(amount)`: rút tiền (kiểm tra số dư)
- Phương thức `display()`: hiển thị thông tin tài khoản

---

## PHẦN II: STATIC METHOD VÀ CLASS METHOD (Bài 11-15)

### Bài 11 (3 điểm): Static Method cơ bản
Tạo class `MathUtils` với các static method:
- `add(a, b)`: cộng 2 số
- `multiply(a, b)`: nhân 2 số
- `power(a, b)`: tính a^b

Gọi các phương thức này mà không cần tạo đối tượng.

---

### Bài 12 (4 điểm): Static Method với xử lý chuỗi
Tạo class `StringHelper` với static method:
- `reverse_string(s)`: đảo ngược chuỗi
- `count_words(s)`: đếm số từ trong chuỗi
- `is_palindrome(s)`: kiểm tra palindrome

---

### Bài 13 (4 điểm): Class Method
Tạo class `Person` với:
- Thuộc tính class `total_people = 0`
- Class method `create_person(name, age)`: tạo đối tượng và tăng `total_people`
- Class method `get_total()`: trả về tổng số người đã tạo

---

### Bài 14 (5 điểm): So sánh Static và Class Method
Tạo class `Calculator`:
- Static method `add(a, b)`: cộng 2 số
- Class method `create_calculator(version)`: tạo đối tượng với version
- Giải thích sự khác biệt khi sử dụng

---

### Bài 15 (4 điểm): Ứng dụng thực tế
Tạo class `DateUtils` với:
- Static method `is_leap_year(year)`: kiểm tra năm nhuận
- Static method `days_in_month(month, year)`: số ngày trong tháng
- Class method `from_string(date_str)`: tạo đối tượng từ chuỗi "dd/mm/yyyy"

---

## PHẦN III: ENCAPSULATION - ĐÓNG GÓI (Bài 16-23)

### Bài 16 (3 điểm): Public thuộc tính
Tạo class `Car` với thuộc tính public: `brand`, `model`, `year`.  
Tạo đối tượng và truy cập trực tiếp các thuộc tính.

---

### Bài 17 (4 điểm): Private thuộc tính
Tạo class `BankAccount` với:
- Thuộc tính private `__balance`
- Getter method `get_balance()`: trả về số dư
- Setter method `set_balance(amount)`: set số dư (chỉ cho phép >= 0)

---

### Bài 18 (4 điểm): Protected thuộc tính
Tạo class `Animal` với:
- Protected thuộc tính `_name`, `_age`
- Phương thức `display()` để hiển thị thông tin
- Giải thích khi nào nên dùng protected

---

### Bài 19 (5 điểm): Getter và Setter hoàn chỉnh
Tạo class `Student` với:
- Private `__name`, `__age`, `__score`
- Getter cho từng thuộc tính
- Setter với validation:
  - `age`: 6-100
  - `score`: 0-10

---

### Bài 20 (5 điểm): Bảo vệ dữ liệu
Tạo class `Product` với:
- Private `__price` (chỉ >= 0)
- Private `__quantity` (chỉ >= 0)
- Phương thức `get_total()`: tính tổng giá trị (price × quantity)
- Không cho phép set giá trị âm

---

### Bài 21 (4 điểm): Encapsulation với tính toán
Tạo class `Circle` với:
- Private `__radius`
- Getter/Setter cho radius (chỉ >= 0)
- Phương thức `area()`: tính diện tích
- Phương thức `circumference()`: tính chu vi

---

### Bài 22 (5 điểm): Quản lý tài khoản ngân hàng
Tạo class `Account` với:
- Private `__balance`, `__pin`
- Phương thức `withdraw(amount, pin)`: rút tiền (kiểm tra PIN)
- Phương thức `deposit(amount)`: nạp tiền
- Phương thức `check_balance(pin)`: xem số dư (kiểm tra PIN)

---

### Bài 23 (6 điểm): Hệ thống đăng nhập
Tạo class `User` với:
- Private `__username`, `__password`
- Phương thức `login(username, password)`: kiểm tra đăng nhập
- Phương thức `change_password(old_pass, new_pass)`: đổi mật khẩu
- Không cho phép truy cập trực tiếp password

---

## PHẦN IV: INHERITANCE - KẾ THỪA (Bài 24-33)

### Bài 24 (3 điểm): Kế thừa cơ bản
Tạo class `Animal` (name, age).  
Tạo class `Dog` kế thừa `Animal`, thêm thuộc tính `breed`.  
Tạo đối tượng và in thông tin.

---

### Bài 25 (4 điểm): Kế thừa với super()
Tạo class `Person` (name, age).  
Tạo class `Student` kế thừa `Person`, thêm `student_id`.  
Sử dụng `super()` trong hàm khởi tạo.

---

### Bài 26 (4 điểm): Ghi đè phương thức
Tạo class `Shape` với phương thức `area()` (trả về 0).  
Tạo class `Rectangle` và `Circle` kế thừa `Shape`, ghi đè `area()`.

---

### Bài 27 (5 điểm): Kế thừa nhiều cấp
Tạo class `Vehicle` (brand, year).  
Tạo class `Car` kế thừa `Vehicle` (thêm `doors`).  
Tạo class `ElectricCar` kế thừa `Car` (thêm `battery_capacity`).

---

### Bài 28 (5 điểm): Quản lý nhân viên
Tạo class `Employee` (id, name, salary).  
Tạo class `Manager` kế thừa `Employee` (thêm `department`).  
Tạo class `Developer` kế thừa `Employee` (thêm `programming_language`).  
Nhập và quản lý danh sách nhân viên.

---

### Bài 29 (6 điểm): Đa kế thừa
Tạo class `Flyable` với phương thức `fly()`.  
Tạo class `Swimmable` với phương thức `swim()`.  
Tạo class `Duck` kế thừa cả 2 lớp trên.  
Giải thích cách Python xử lý đa kế thừa.

---

### Bài 30 (5 điểm): Override __str__
Tạo class `Person` với `__str__` trả về "Person: [name]".  
Tạo class `Student` kế thừa `Person`, override `__str__` trả về "Student: [name] - ID: [id]".

---

### Bài 31 (6 điểm): Hệ thống quản lý thư viện
Tạo class `Item` (id, title).  
Tạo class `Book` kế thừa `Item` (thêm `author`, `pages`).  
Tạo class `Magazine` kế thừa `Item` (thêm `issue_number`).  
Quản lý danh sách với các chức năng: thêm, tìm, hiển thị.

---

### Bài 32 (5 điểm): Tính đa hình với kế thừa
Tạo class `Animal` với phương thức `make_sound()`.  
Tạo class `Dog`, `Cat`, `Bird` kế thừa `Animal`, mỗi lớp có `make_sound()` riêng.  
Tạo list chứa các đối tượng khác nhau, gọi `make_sound()` cho từng đối tượng.

---

### Bài 33 (6 điểm): Hệ thống thanh toán
Tạo class `Payment` với phương thức trừu tượng `pay(amount)`.  
Tạo class `CashPayment`, `CardPayment`, `MomoPayment` kế thừa `Payment`.  
Mỗi lớp triển khai `pay()` theo cách riêng.

---

## PHẦN V: POLYMORPHISM - ĐA HÌNH (Bài 34-38)

### Bài 34 (4 điểm): Đa hình với phương thức
Tạo class `Shape` với `calculate_area()`.  
Tạo class `Rectangle`, `Circle`, `Triangle` kế thừa `Shape`.  
Mỗi lớp có cách tính diện tích riêng. Tạo list và tính tổng diện tích.

---

### Bài 35 (5 điểm): Đa hình với toán tử
Tạo class `Fraction` (tử số, mẫu số).  
Override các toán tử: `__add__`, `__sub__`, `__mul__`, `__str__`.  
Thực hiện các phép toán với phân số.

---

### Bài 36 (5 điểm): Đa hình trong thực tế
Tạo class `MediaPlayer` với phương thức `play()`.  
Tạo class `AudioPlayer`, `VideoPlayer` kế thừa `MediaPlayer`.  
Mỗi lớp có cách phát khác nhau.

---

### Bài 37 (6 điểm): Hệ thống vận chuyển
Tạo class `Transport` với phương thức `deliver(distance)`.  
Tạo class `Truck`, `Ship`, `Plane` kế thừa `Transport`.  
Mỗi phương tiện có tốc độ và cách tính thời gian khác nhau.

---

### Bài 38 (5 điểm): Đa hình với list
Tạo class `Employee` với phương thức `calculate_salary()`.  
Tạo class `FullTimeEmployee`, `PartTimeEmployee` kế thừa `Employee`.  
Tính tổng lương của tất cả nhân viên trong list.

---

## PHẦN VI: ABSTRACTION - TRỪU TƯỢNG (Bài 39-43)

### Bài 39 (5 điểm): Abstract Class cơ bản
Sử dụng `abc` module, tạo abstract class `Shape` với abstract method `area()`.  
Tạo class `Rectangle`, `Circle` kế thừa và triển khai `area()`.

---

### Bài 40 (6 điểm): Abstract Class với nhiều phương thức
Tạo abstract class `Animal` với:
- Abstract method `make_sound()`
- Abstract method `move()`
- Phương thức thường `sleep()`: in "Đang ngủ"

Tạo class `Dog`, `Cat` triển khai các abstract method.

---

### Bài 41 (6 điểm): Hệ thống Database
Tạo abstract class `Database` với:
- Abstract method `connect()`
- Abstract method `query(sql)`
- Abstract method `close()`

Tạo class `MySQLDatabase`, `PostgreSQLDatabase` triển khai.

---

### Bài 42 (7 điểm): Hệ thống Plugin
Tạo abstract class `Plugin` với abstract method `execute()`.  
Tạo class `TextPlugin`, `ImagePlugin`, `VideoPlugin` kế thừa.  
Quản lý danh sách plugin và gọi `execute()` cho từng plugin.

---

### Bài 43 (6 điểm): Template Method Pattern
Tạo abstract class `Report` với:
- Abstract method `generate_header()`
- Abstract method `generate_body()`
- Abstract method `generate_footer()`
- Phương thức `generate()`: gọi 3 phương thức trên theo thứ tự

Tạo class `PDFReport`, `HTMLReport` triển khai.

---

## PHẦN VII: ĐỌC GHI FILE (Bài 44-50)

### Bài 44 (3 điểm): Đọc file cơ bản
Tạo file `data.txt` chứa nội dung bất kỳ.  
Viết chương trình đọc và in toàn bộ nội dung file.

---

### Bài 45 (4 điểm): Đọc file theo dòng
Đọc file `students.txt` (mỗi dòng là tên học sinh).  
In từng dòng và đếm tổng số học sinh.

---

### Bài 46 (4 điểm): Ghi file cơ bản
Nhập n dòng văn bản từ bàn phím.  
Ghi tất cả vào file `output.txt`.

---

### Bài 47 (5 điểm): Ghi thêm vào file
Tạo file `log.txt`.  
Mỗi lần chạy chương trình, ghi thêm dòng: "Thời gian: [datetime] - Sự kiện: [nội dung]"

---

### Bài 48 (6 điểm): Quản lý danh sách học sinh với file
Tạo class `Student` (name, age, score).  
Chức năng:
- Lưu danh sách học sinh vào file `students.txt`
- Đọc danh sách từ file và hiển thị
- Thêm học sinh mới vào file

---

### Bài 49 (7 điểm): Hệ thống quản lý sản phẩm với file
Tạo class `Product` (id, name, price, quantity).  
Chức năng:
- Lưu sản phẩm vào file `products.txt`
- Đọc và hiển thị danh sách
- Tìm sản phẩm theo tên
- Cập nhật thông tin sản phẩm trong file

---

### Bài 50 (8 điểm): Dự án tổng hợp - Quản lý thư viện
Xây dựng hệ thống quản lý thư viện với:
- Class `Book` (id, title, author, year, status)
- Lưu trữ dữ liệu vào file `library.txt`
- Chức năng:
  1. Thêm sách mới
  2. Tìm sách theo tên/tác giả
  3. Mượn sách (thay đổi status)
  4. Trả sách
  5. Hiển thị danh sách sách đang mượn
  6. Thống kê: tổng số sách, số sách đã mượn

**Gợi ý:** Sử dụng OOP, Encapsulation, File I/O, menu lựa chọn.

---

## TỔNG KẾT

**Tổng điểm:** 250 điểm  
**Phân bổ:**
- Phần I: OOP Cơ bản (28 điểm)
- Phần II: Static/Class Method (20 điểm)
- Phần III: Encapsulation (36 điểm)
- Phần IV: Inheritance (50 điểm)
- Phần V: Polymorphism (25 điểm)
- Phần VI: Abstraction (30 điểm)
- Phần VII: Đọc ghi File (37 điểm)

---

**LƯU Ý:**
- Làm từng bài một, đừng vội xem đáp án
- Chạy thử nhiều test case
- Code phải rõ ràng, có comment khi cần
- Hiểu rõ từng tính chất OOP trước khi làm bài nâng cao
- Thực hành nhiều với file I/O để thành thạo

**CHÚC CÁC ÔN TẬP TỐT!**

