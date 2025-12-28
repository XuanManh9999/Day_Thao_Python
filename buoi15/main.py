# Tính tổng 2 số a và b
# Yếu do nền toán kém: Em google tìm kiếm rồi bộ sung song song luôn
# Yếu do nền lập trình kém: Là học vững lý thuyết và code nhiều lên để tay to hơn
# 2, 3, 4 (18h - 21h); 5, 6, 7 (17h-2h,3h); 8 (17h-20h)
# Buổi chiều tối
# Sáng?, đầu chiều em làm gi?
# 2, 3 -> về học tiếng hàn tới 23h (ngủ); -> 8h (9h)
# 9h - 11h30 (học lập trình) -> ăn trưa, ngủ trưa 14h
# 14h -> 17h30 (học tiếng, học kĩ năng khác...)
# 2h(60')
# 20' -> đọc lại toàn kiến thức buổi trước
# n số tuỳ chọn: 3
# n (chẵn) and n > 10
#     "Số chẵn lớn hơn 10"
# n = int(input())
# if n % 2 == 0 and n > 10:
#     print("Số chẵn lớn hơn 10")


# Học về đệ quy (cấu trúc dữ liệu ngăn xếp stack) nó là một cấu trúc dữ liệu có liên quan mật thiết tới đệ quy, để hiểu được đệ quy thì ta cần hiểu được kiến thức về ngăn xếp (stack)
# Nguyên lý của stack nó dựa theo LIFO (Last in first out) Vào sau ra trước. Nó gồm 2 thao tác là push, pop


# stackframe là gì?
# Stack frame ... đọc
# process -> tiến trình -> Không chia sẻ tài nguyên được
# thread -> luồng chạy -> chia sẻ tài nguyên được

 
 
#  Process (tiến trình) là một chương trình đang chạy, có không gian bộ nhớ riêng biệt, nặng (heavyweight), tạo tốn thời gian và giao tiếp phức tạp; trong khi thread (luồng) là một đơn vị thực thi nhỏ hơn bên trong một process, chia sẻ chung không gian bộ nhớ với các thread khác, nhẹ hơn, tạo nhanh hơn và giao tiếp giữa các thread rất dễ dàng nhưng cần xử lý xung đột bộ nhớ (Race condition). 




# Hàm đệ quy là hàm mà gọi lại chính
# Một hàm khi được gọi chính nó được gọi là đệ quy, và hàm này sẽ được thêm vào vùng nhớ stack, khi mà số lượng hàm gọi lại chính nó đến một ngưỡng nhất định, nó sẽ bị tràn hiện tượng này gọi là stack overflow.
# def say_hello():
#     print("Hello Thảo")
    
# say_hello()

# count = 0
# def de_quy():
#     # count += 1
#     count = 0
#     print(f"count : {count}")
#     de_quy()

# de_quy()

# 5; 1 + 2 + 3 + 4 + 5 = 15
# Tính tổng 1 - n

# 0 

# def sum (n):
#     if n == 0:
#         return 0 # bài toán con nhỏ nhất (không gọi hàm đó nữa)
#     else:
#         return n + sum(n - 1) # công thức truy hồi
    
# print(sum(3))


# CT chung: n + sum(n - 1)
# sum(0) = 0
# sum(1); 1 + sum(1 - 1) => 1 + sum(0) = 1 + 0 = 1
# sum(2); 2 + sum(2 - 1) => 2 + sum(1) = 2 + 1 = 3
# sum(3); 3 + sum(3 - 1) => 3 + sum(2) = 3 + 3 = 6

# Nhìn lại và làm lại ví dụ về hàm đệ quy này trong tài liệu

# Tinh chất của đệ quy

# 1. Khi viết đệ quy ta cần biết và xác định rõ bài toán con nhỏ nhất để dừng chương trình tránh việc bị lặp vô hạn. (kết quả nhỏ nhất)
# 2. Biết công thức truy hồi (công thức để nó truy hồi về bài toán con nhỏ)

# Bài tập cần tìm hiểu
# Cho 1 list số [1, 3, 2, 5, 7] viết hàm đệ quy để in ra các phần tử trong list đó
# Cho 1 list số [1, 3, 2, 5, 7] tính tổng các phần tử trong list   