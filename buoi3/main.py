# Đếm số lượng chữ số
# # # 100 -> 3; 1000 -> 4
# n = abs(int(input())) # -100 
# cnt = 0 # 0
# if n == 0:
#     print(1)
# else:
#     while n != 0:
#         cnt += 1 # cnt += 1 -> tăng lên 0 + 1 = 1; 1 + 1 = 2; 2 + 1 = 3
#         n = n // 10 # n = n // 10 -> 100 // 10 = 10 -? 10 // 10 = 1; 1 // 10 -> 0
#     print(cnt)


# Tính tổng chữ số

# n = int(input()) # 1234 -> 1 + 2 + 3 + 4 = 10

# sum = 0 # biến lưu giá trị;0

# while n != 0:
#     sum += n % 10 # 1234 % 10 = 4 => 1230 -> chia hết cho 10 -> dư 4; 0 + 4 = 4; 4 + 3 = 7 + 2 = 9 + 1 = 10
#     n //= 10 # 1234 // 10 -> 123; 123 // 10 -> 12// 12 // 10 -> 1 // 10 -> 0 # điểm dừng
# print(sum) # 10


# 4321 -> 1234
# 4321 -> 1+2+3+4 = 10    
# n = int(input()) # 4321

# reversed = ''# ''

# while n != 0:
#     reversed +=  str(n % 10)# 4321 % 10 = 1; '' + '1' = '1' ; 432 % 10 = 2 => '1' + '2' = '12'; 43 % 10 = '12' + '3' = '123'# '123'  + '4' = '1234'
#     n //= 10 # 4321 // 10 = 432; 432 // 10 -> 43; 43 // 10 -> 4 # 4 // 10 = 0
        
# print(reversed)


# -1200 
# 00-21




# Vòng lặp for -> thường được dùng khi ta biết trước số lần lặp            
# Vòng lặp while -> thường dùng khi ta chưa biết trước số lần lặp


# in từ 1 đến 10 for
# for i in range(1, 11, 1):
#     print(i)

# dùng while luôn phải nhớ nếu không có điều kiện dừng thì sẽ bị lặp vô hạn
# i = 1
# while i <= 10:
#     print(i)
#     i += 1 # điều kiện dừng
# else:
#     print("XONG")

# làm bàng cửu chương từ 2 -> 10 bằng while

# i = 2 # i = 2

while i <= 10: # 2 <= 10 -> True
    j = 0 # j = 0
    print("BANG: ", i) # BẢNG 2
    while j <= 10: # True
        if j == 2:
            j += 1
            continue
        if j == 5:
            break
        print(i, "*", j, "=", i*j) # 2 * 0 = 0;  2 * 1 = 2; 2 * 2 = 4
        j += 1# 0 + 1 = 1# 1 + 1 = 2
    i+= 1
else:
    print("Hoàn thành")



