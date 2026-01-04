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
# Điềm dừng list rỗng = 0
# Công thức truy hồi: gọi đệ quy các phần tử cong lại

# a = [1, 3, 2, 5, 7]
# def print_list(arr):
#     if len(arr) == 0:
#         return
#     print(arr[0:])
#     # print_list(arr[1:])
# print_list(a) 
# print_list([1, 3, 2, 5, 7])
# -> in 1
# print_list([3, 2, 5, 7])
# -> in 3
# print_list([2, 5, 7])
# -> in 2
# print_list([5, 7])
# -> in 5
# print_list([7])
# -> in 7
# print_list([])

# Cho 1 list số [1, 3, 2, 5, 7] tính tổng các phần tử trong list   
# a =  [1, 3, 2, 5, 7]
# Điểm dừng: hết phần tử trong list
# Công thức truy hồi: phần tử đàu + các tử cong lại
# def sum_list(arr):
#     if len(arr) == 0:
#         return 0
#     return arr[0] + sum_list(arr[1:])
# print(sum_list(a))
# Bước 1: sum_list([1, 3, 2, 5, 7]); arr[0] ~ 1 + sum_list([3, 2, 5, 7]); 1 + 17 = 18
# Bước 2: sum_list([3, 2, 5, 7]); arr[0] ~ 3 + sum_list([2, 5, 7]); 3 + 14 = 17
# Bước 3: sum_list([2, 5, 7]); arr[0] ~ 2 + sum_list([5, 7]); 2 + 12 = 14
# Bước 4: sum_list([5, 7]); arr[0] ~ 5 + sum_list([7]); 5 + 7 = 12
# Bước 5: sum_list([7]); arr[0] ~ 7 + sum_list([]) ~ 0; 7 + 0 = 7
# Một hàm xử lý xong khi nào?

# Mục tiêu học là?. Nó là bước đệm để em học thuật toán DSA, DFS/BFS, tree, backtracking
# Một hàm đệ quy luôn luôn có 2 phần:
# Điều kiện dừng: -> không có  thì chương trình sẽ bị chạy vô  tận
# Công thức truy hồi (bước gọi lại chính nó): -> Bài toán lớn -> bài toán nhỏ hơn
# Công thức vàng: Bài toán (n) = Bài toán (n - 1) + xử lý thêm

# Tính tổng từ 1 - N?
# S(n) = 1 + 2 + 3 +... +n
# Phân tích:
# Điều kiện dừng: n = 1
# Công thức truy hồi: n + tong(n - 1)


# 5, 4, 3, 2, 1, 0
# 5, 4, 3, 2, 1
# def sum_n(n):
#     if n == 1:
#         return 1
#     return n + sum_n(n - 1)

# 1, 2, 3, 4, 5
# print(sum_n(5))
# sum_n(5)
# = 5 + sum_n(4)
# = 4 + sum_n(3)
# = 3 + sum_n(2)
# = 2 + sum_n(1)
# = 1

# Số factorial
# 0! = 1
# n! = n * (n - 1) * (n - 2) *  ... * 1
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# Điểm dừng 1
# Công thức truy hồi: n * 
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))


# Số fibonacci
# 0 1 1 2 3 5 8 13
# Tính cổng các số fibonaci
# Điểm dừng: n = 0 -> 0, n == 1 -> 1
# Công thức truy hồi: Kết quả số đó bằng tổng 2 số trước đó
# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# print(fib(7))

# Đếm số chữ số của một số nguyên bằng đệ quy
# input -> 12345 -> 5; 12 -> 2
# Điều kiện điểm dừng: < 10 -> 1 (trường hợp bài toán nhỏ nhất)
# Công thức truy hồi: 1 + n // 10

# def count_digits(n):
    #Lần 1: 123  1 +   count_digits(12) = 1 + 2 = 3
    #Lần 2: 12   1 + count_digits(2) = 2
    #Lần 3: 2  -> return về 1: count_digits(2) = 1
    # if n < 10:
    #     return 1
    
    # 1 + count_digits(123 // 10 = 12)
    # 1 + count_digits(12 // 10 = 2)
    # return 1 + count_digits (n // 10)

# print(count_digits(123))
# 123 < 10 -> FALSE. 1 + count_digits(123//10 = 12)  ## 1 + 2 = 3
# 12 < 10 -> FALSE. 1 + count_digits(12//10 = 2)  # 1 + 1
# 2 < 10 -> TRUE -> 1.


#Bài Đảo ngược chuỗi. 'python' -> 'nohtyp'
# Điều kiện dừng: chuỗi rỗng hoặc 1 ký tự
# Công thức truy hồi: lấy ký tự đầu -> đặt về cuối
# 's' -> 's'
# def reverse_string(s):
#     if len(s) <= 1:
#         return s
    
#     print(s)
#     return reverse_string(s[1:]) + s[0]
    
# print(reverse_string('con'))
# def sum_n(n):
#     return n + sum_n(n - 1)

# print(sum_n(5))
# [
#     {
#         name: "IPHONE",
#         price: 1000
#     }
# ]