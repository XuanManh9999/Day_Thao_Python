# import math
from math import * # lấy tất cả thư viện toán học và ném vào builin
# print(pow(2, 3))
# print(round(2.1))

# print(help(math)) # In ra hướng dẫn cũng như các hàm ở bên trong thư viện math
# Hàm nó sẽ dùng để thực thi một yêu cầu nào đó rồi trả về kết quả
# can_bac_cua_3 = math.sqrt(2) # Hàm tính căn bậc 2  # 1.4142135623730951
# print(can_bac_cua_3)

# print(math.isqrt(2)) # Hàm căn bậc 2 nhưng chỉ lấy phần nguyên 2.9 -> 2; 3.99 -> 3
# Hàm pow dùng để tính luỹ thừa
# 2^3 = 2 * 2 * 2; 2^4 = 2*2*2*2
# print(math.pow(2, 4)) # 2 * 2 * 2 = 8


# Hàm floor (làm tròn xuống), hàm ceil (làm tròn lên)
# print(math.floor(3.9)) # 3 
# print(math.ceil(3.1)) # 4

# Hàm math.fabs() hàm trong thư viện toán học dùng để lấy trị tuyệt đối, abs() hàm builin có sẵn trong ngôn ngữ
 
# print(math.fabs(-1)) # 1.0  -> trả về số thực
# print(abs(-1)) # 1 trả về số nguyên

# Hàm gcd
# Ước chung lớn nhất là số lớn nhất mà 2 số đó có thể chia hết
# 10 20 -> 10 (UCLN)
# print(math.gcd(100, 50))



# Hàm factiorial
# 5! = 1 * 2 * 3 * 4 * 5 = 120

# print(math.factorial(5)) # 120 
# print(math.factorial(10)) # 3628800; 


# Hàm max, min (builin)
# max -> tìm ra số lớn nhất trong tập hợp
# min -> tìm ra số nhỏ nhất trong tập hợp
# print(max(1, 2, 3, 4, 5))# 5
# print(min(1, 2, 3, 4, 5))  # 1

# arr = []

# for i in range(1, 10000000):
#     arr.append(i)
    
# print(max(arr))
    

# Hàm round (builin) hàm làm tròn đều
# VD: 3.4 gần 3 hơn -> làm trong về 3; 3.6 gần 4 hơn thì nó về 4
# print(round(3.49))


# Vòng lặp trong python

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# # ...
# print(100)

# for i in range(1, 1000): 1 -> 999; i++
#     print(i)
#     print(isqrt(i))


# Hàm range() -> hàm này gồm có 3 giá trị (start, stop, step)
# Trong đó
# start là: vị trí bắt đầu default = 0
# stop: vị trì cuối - 1
# step: bước nhảy default 1

# range -> 1 -> 4 (step); 1, 3

# for i in range(1, 5, 2):
#     print(i)
    
    
    
# for i in range(2, 5, 2): # (2, 4)
#     print('28tech')

# In ra các ước của 10 -> 10 = 1, 2, 5, 10

# for var in range(1, 11, 1):# (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#     if 10 % var == 0:
#         print(var)
    
    
# 6 -> 6 *1, 12 * 2, 18 * 3, 24

# bội của 3 in ra 10 số

# for i in range(0, 31, 3): # (0, 3, 6, 9)
#     print(i)
    
# # b1 -> in ra 0

# for i in range(1, 10, 0):
#     print(i)



# Vòng lặp lồng nhau

# In ra bảng cửu chương

# for i in range(2, 11, 1):
#     print('BANG: ', i)
#     for j in range(1, 11):
#         print(i, "*", j, "=", i*j)

# Vòng lặp break (khi vòng lặp for, while gặp câu lệnh break thì nó sẽ dừng vòng lặp for, while đó ngay lật tức), 

# for i in range(1, 10): # (1 - > 9)
#     # if i == 4:
#     #     break
#     # print(i)
#     print("i=", i)
#     for j in range(1, 5, 1): #  (1 - 4)
#         if j == 2:
#             break
#         print("j=", j)
    
# print("CODE TIEP")



# continue (được dùng để bỏ qua bước lặp hiện tại các câu lệnh bên dưới nó sẽ không được thực thi, và chuyển tới bước lặp tiếp)


# for i in range(1, 5): # (1, 4)
#     print(i)
#     if (i == 3):
#         continue
# 1, 2, 4


n = int(input())

sum = 0
for i in range(1, n + 1, 1):
    sum += i
print(sum)