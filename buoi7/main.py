# thuat toan tim kiem tuyen tinh
# a = [1, 2, 3, 4]
# can_tim = 4
# co  = False # danh dau xem co tim thay hay khong mac dinh se de la fale
# # tim xem co so 4 trong list khong, neu co in YES, khong co in NO
# for i in range(0, len(a), 1): # (0, 1, 2, 3)
#     if a[i]  ==  can_tim:
#         co = True
#         break
# if co == True:
#     print("YES")
# else:
#     print("NO")        


# cho 1 list cac phan tu, yeu cau la tim xem trong list do co cap phan tu nao co  tong  la 5 khong
# a =  [1, 2, 3, 4, 5] 
# for i in range(0, len(a), 1):
#     co = False # dung de dat va xac dinh xem co tim thay no khong
#     for j in range(i + 1, len(a), 1): #  (1, 2, 3, 4)
#         if a[i] + a[j] == 5:
#             co = True
#             break
#     if co == True:
#         print(f"a[i]={a[i]};a[j]={a[j]} co tong la 5")

# Combine list
# Ta có thể sử dụng hàm extend hoặc dấu + để thêm các phân tử của 1 list khác vào
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# Cách 1
# b = a + b  # [1, 2, 3, 4, 5] + [6, 7, 8, 9, 10] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Cách 2
# a.extend(b)  # mở rộng list a với các phần tử của list b

# print(a)


# Hàm copy() trả về một list mới có nội dung tương tự như list ban đầu  nhưng không phải là list ban đầu
# a = [1, 2 ,3 ,4, 5, 6]
# # b = a
# b = a.copy()
# b[0] = 1000
# # if a == b:
# #     print("TRUE")
# # else:
# #     print("NO")

# print(a)
            
# Các phương thức list hàm count(), index()
# Hàm count() trả về số lượng phần tử xuất hiện trong list
# a = [1, 2, 3, 4, 5, 5, 6]

# print(a.count(5)) # 2
# print(a.count(2)) # 1
# Đếm số lượng phần tử
# a = [1,2, 2, 3]
# print(a.count(2))

# Hàm index sẽ là hàm sẽ trả về chỉ số, chỉ mục đầu tiên của phần tử tìm thấy trong list
# a = [1, 2, 3, 3, 4, 4, 5, 5, 5]

# print(a.index(5))# 6 vì 6 là chỉ mục đầu tiên mà nó tìm thấy

# Hàm reverse()(dùng để lật ngược một list) và sort() dùng để sắp xếp tăng dần một list
# a = [4, 1, 2, 3, 5] # [5, 3, 2, 1, 4]
# # a.reverse()
# a.sort() # dùng đẻ sx tăng dần 1 list

# a.reverse()


# print(a)

# Các hàm buiin sử dụng với list
# all() -> trả về True nếu mọi phần tử  trong list đều là True
# Những giá trị trong python đc cho là false: 0, False, '', "", [], {}, ()
# a = [1, 2, 3, 4, 6]
# print(all(a)) 

# any() -> Trả về True khi trong list chưa ít nhất 1 phần tử là True
# a = [False, '', "", [], 1]
# print(any(a)) # -> True


# max() trả về phần tử lớn nhất ở trong list, min() trả về phần tử nhỏ nhất ở trong list()
# a = [1, 2, 3, 4, 5, 6]
# print(max(a))
# print(min(a))


# sorted() trả về một list đã sắp xếp của list ban đầu
# a = [3, 1, 2, 4, 5]

# result =  sorted(a)

# print(result)



# sum() trả về tổng các phần tử có ở trong list
# a = [1, 2, 3, 4, 5] 

# print(sum(a) + sum(a) * 0.1)













