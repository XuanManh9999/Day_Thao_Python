# Path trong python
# tuppe thì các phần tử trong nó không thể thay đổi hay cập nhật giá trị
# set là các phần tử nằm bên trong set thì không được phép trùng nhau
# list các phần tử truy cập thông qua chỉ mục và được phép cập nhật hoặc xoá
# dict định dạng từ tiển bao gồm key: value, muốn lấy ra value thì get key
# class -> đóng gói, kế thừa, đa hình, trừu tượng
# a = (1, 2, 3)
# b = {1, 2, 3, 3}

# print(type(b))
# print(b)
# print(a[0])

# print(type(a))


# Path và try, exception trong python

# Path (đường dẫn) là cách xác định vị trí của file hoặc thư mục trên hệ thống máy tính

# D:\workspace\day_them\python-thao\50_BAI_TAP_ON_TAP_CAU_HOI.md -> từ đường dẫn này ta có thể truy ra được vị trí file được lưu trong hệ thống
# Trong python, path dùng để làm gì?
# Đọc/ghi file
# Upload / download file
# Load config, model, template
# Xử lý log, cache, video, excel..

# Python thì có hai loại đường dẫn: Absolute & Relative
# Absolute path (đường dẫn tuyệt đối)
# Luôn bắt đầu từ gốc hệ thống 
# VD: windows: C:\Users\Admin\...
# VD: linux: /home/admin/...
# Ưu điểm:
# Rõ ràng, không phụ thuộc vị trí chạy code
# Nhược điểm:
# Không porttable (đổi máy (có thể sai), đổi server thì hỏng)

# Relative path (đường dẫn tương đối)
# Tính từ thư mục đang chạy chương trình
# "buoi25/data.txt"
# "./buoi25/data.txt"
# "../buoi25/data.txt"

# ./ -> thư mục hiện tại
# ../ -> thư mục cha

# Currtent working directory (CWD) 

# import os # thư viện dùng để lấy đường dẫn

# print(os.getcwd()) # D:\workspace\day_them\python-thao\buoi25 ->  trả về vị trí của thư mục chạy lệnh

# os.path lấy đường dẫn hiện tại
# import os

# current_file = os.path.abspath(__file__) # trả về vị trí đứng của file hiện tại  D:\workspace\day_them\python-thao\buoi25\main.py
# print(current_file)

# Lấy thư mục chứa file:
# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # D:\workspace\day_them\python-thao\buoi25

# print(BASE_DIR)


# Nối path
# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # D:\workspace\day_them\python-thao\buoi25

# file_path = os.path.join(BASE_DIR, "data.txt") # D:\workspace\day_them\python-thao\buoi25\data.txt
# file_path = os.path.join(BASE_DIR, "main.py") # D:\workspace\day_them\python-thao\buoi25\main.py
# file_path = os.path.join(BASE_DIR, "endpoint", "password.txt") # D:\workspace\day_them\python-thao\buoi25\endpoint\password.txt

# print(file_path)



# pathlib -> thư viện dùng để làm việc với nó trong python
# from pathlib import Path # Câu lệnh bắt buộc dùng để import


# Tạo path
# p = Path("data/test.txt") # data\test.txt

# Absolute path (đường dẫn tuyệt đối)
# print(p.resolve()) # D:\workspace\day_them\python-thao\buoi25\data\test.txt

# print(p.cwd()) # D:\workspace\day_them\python-thao\buoi25
# print(p)



# Ứng dụng: tìm 1 thư mục chưa file .py
# BASE_DIR = Path(__file__).resolve().parent 

# file_path = BASE_DIR / "data.txt" # nối thư mục với file # D:\workspace\day_them\python-thao\buoi25\data.txt
# file_path.exists() -> kiểm tra xem file có tồn tại hay không?, nếu tồn tại thì trả về true, không tồn tại thì trả về false

# print(file_path.exists()) # Nếu có file đó trả về true, không có thì trả về false
# if (file_path.exists()):
#     print("Có file đó")
#     with open(file_path, "r", encoding="utf-8") as f:
#         data = f.read()
#         print(data)
# else:
#     print("Không có file đó")


# print(file_path.is_file()) # trả về true nếu có file đó, false nếu không
# print(file_path.is_dir()) # Kiểm tra xem có thư mục đó không, nếu có thì trả về true, không thì false



# from pathlib import Path

# path = Path("thao/hanquoc.jpg")

# print(path.cwd())
# print(path.cwd())

# path.resolve() # thực thi path map với giá trị truyền vào trong path

# print(path)

# if path.is_dir():
#     print("Có thư mục đó")
# else:
#     print("Không có thư mục đó")


# Tạo thư mục
# from pathlib import Path

# Path("uploads").mkdir() # tạo ra 1 thư mục uploads trong thư mục hiện tại
# Path("images").mkdir() # tạo ra 1 thư mục images trong thư mục hiện tại

# Đọc ghi file với path

# path = Path("data.txt")
# write_text(text, encoding="utf-8")
# path.write_text("khong an dau ma an cai khac co", encoding="utf-8") # cách ghi nội dung vào file

# contents = path.read_text(encoding="utf-8")

# print(contents)



# Duyệt file trong thư mục

# from pathlib import Path

# duyệt các file và thư mục có trong thư mục gốc
# for file in Path().iterdir():
#     print(file)


# Lọc theo đuổi file glob("*.txt") 
# for file in Path().glob("*.txt"):
#     contents = file.read_text(encoding="utf-8")
    
#     print(contents)


# for file in Path("../buoi24").glob("*.txt"):
#     contents = file.read_text(encoding="utf-8")
    
#     print(contents)


# Tổng kết

# Có 2 loại đường dẫn:
# Đường dẫn tuyệt đối: tuyệt nghĩa là nó luôn đúng và nó sẽ xuất phát từ root (từ gốc của ổ đĩa) D:\workspace\day_them\python-thao\buoi17
# Đường dẫn tương đối: phạm vi chỉ trong cái thư mục mà ta đang chạy code


# try, exception trong python
# try, exception, finally dùng để bắt và xử lý những lỗi có thể xảy ra để không làm cho chương trình bị lỗi
# ZeroDivisionError -> chia cho 0
# print("Thảo chuyển tiền")
# nhan_tien = False
# try:
#     # những đoạn code mà nghi nghờ có thể lỗi ta cho vào trong try
#     a = 1 / 1
    
#     nhan_tien = True
# except Exception as e:
#     print("Khôi phục lại tiền cho thảo")
#     # nếu đoạn code ở trên try bị lỗi thì nó sẽ nhảy xuống except
# finally:
#     # Không quan tâm có lỗi hay không có lỗi ở try, nó luôn luôn thực thi sau cùng. Lưu ý là finally không bắt buộc
#     print("Vào finaly")


# if nhan_tien:
#     print("Mạnh đã nhận được tiền")


