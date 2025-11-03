# Giới thiệu Python là gì?

+, Python nó là một ngôn ngữ lập trình (Ngôn ngữ lập trình nó là một ngôn ngữ giúp ta có thể phát triển lên các phần mềm từ nó, và nói chuyện được với máy tính)
+, Python có thể làm được gì?: Website (FastAPI, DG), AI (...), App.

- Máy tính chỉ hiểu hệ nhị phân (0, 1)

# Kiểu dữ liệu:

- Để kiểm tra được kiểu dữ liệu trong python thì em dùng hàm; type(tên_biến)
  +, Kiểu số nguyên: 0, 1, 2, 3. int (kiểu số nguyên)
  +, Kiểu số thực: 1.2, 0.5. float, double (kiểu số thực)
  +, Kiểu chuỗi: 'Học Viện Công Nghệ Bưu Chính Viễn Thống'. str(chuỗi)
  +, Kiểu đúng đúng sai: True, False; bool
  +, list
  +, tuppe

- Ép kiểu: loại kiểu (int, float, str...)
  VD: a = '1' -> ép về số nguyên; b = int(a) -> biến a được ép về 1

# Toán tử

+, Toán tử số học: +, -, \*, /, // (chia nguyên), % (chia lấy dư), \*\* (luỹ thừa)

+, Toán tử so sách: >=, <=, >, <, =, !=, == (so sánh xem có bằng hay không)
+, Toán tử logic: or (nếu thoả mãn một đk là được), and (bắt buộc phải thoả mãn tất cả ĐK), not (phụ định lại)
+, Toàn tử tập hợp: in (nằm trong), not in (không nằm trong)
+, Toán tử thuộc về: is, not is

# Cách khai báo biến

- Biến là một nơi để ta lưu giá trị vào trong bộ nhớ RAM, và trong python thì nó có cú pháp như sau:
  ten_bien = du_lieu_muon_gan
  +, Quy ước đặt tên biến:

  - Không được có số ở đầu tiên. VD: 01Ngoc
  - Tên biến không được trùng với các từ khoá trong python. VD: print = 1
  - Tên biến cần thể hiện rõ ý nghĩa mục đích của nó VD: age = 25
  - Quy ước chuẩn python đặt tên, nếu tên có nhiều từ nối lại thì dùng dấu \_. VD: nguyen_xuan_manh = True

- Hàm print dùng để in ra màn hình và đây là câu lệnh được sử dụng nhiều nhất
  Hàm print nhận vào 3 giá trị. print(ten_bien, end="\n", sep=" ") trong đó sep và end là không bắt buộc
  nếu không ghi gì thì mặc định end = \n (xuống dòng), sep = " "

# Nhập giá trị trong python từ màn hình console

- input() -> mặc định nó sẽ trả về là chuỗi '' str

# a, b = map(double, input().split()); int -> kiểu số nguyên

# Cấu trúc rẽ nhánh trong python

- Trong python nó quy định khối code ở dạng block dựa vào thụt dòng
- Với kiểu rẽ nhanh ta thường dùng nó với các toán tử so sánh: >=, <=, >, <, !=, ==
- Khi dùng biểu thứ kết hợp với toán tử logic (and, or, not) thì ta chỉ dùng một loạt tại một thời điểm, không dùng đan xen nó, nếu muốn dùng đan xen thì ta nhóm nó trong dấu ()
  VD:
  if a % 2 == 0 and (a >= 3 or b > 50):
  print("ABCXY")

# Dạng 1

if bieu_thuc:
// khối code
else:
// khối code

# Dạng 2

if bieu_thuc:
// khối code
elif bieu_thuc:
// khối code
else:
// khoi code

# Dạng 3

Trong biểu thức rẽ nhanh if-else thì không nhất thiết phải dùng else
if bieu_thuc:
// code block

# Dạng 4 (Toán tử 3 ngôi)

# Cú pháp:

    bieu_thuc_dung if bieu_thuc else bieu_thuc_sai

# Cách comment trong Python

+, Lợi ích của comment là giúp giải thích ý nghĩa code
+, Comment thì sẽ không được chương trình thực thi

Có 2 loại comment:
+, Comment trên 1 dòng. #
+, Commnet trên nhiều dòng. """
// nội dung comment
"""
