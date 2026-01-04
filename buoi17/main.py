# LAMBADA trong python
# Là hàm vô danh tức làm không có tên hàm
# Được dùng để xây dựng những hàm chỉ bao gồm 1 câu lệnh
# trong lambda không có từ khoá return vì nó đã mặc định như thế rồi

# lambda parameters : expression

# lambda: cú pháp của python
# parameters: các tham số
# expression: biểu thức

# def func(n):
#     return 2 * n


# func = lambda x :  x * 2


# Các tính chất của hàm lambda 
# +, lambda không thể chứa các câu lệnh return, pass..
# +, lambda chỉ chứa một biểu thức duy nhất
# +, IIFE: Biểu thức lambda có thể được gọi ngay lật tức

# Ứng dụng của hàm lambda và hàm map trong python
# Hàm map trong python dùng để custom list thanh một dạng khác và vẫn đảm bảo đủ số lượng phần tử, nó nhận vào 2 đối số là (hàm, list)
# a = [1, 2, 3, 4, 5, 6]
# custom = list(map(lambda x : x ** 2, a))
# print(f"a: {a}")
# print(f"custom: {custom}")

# lambda và filter(hàm, list) nó giống tương tự như hàm map về cách hoạt động của hàm map, nhưng nó khác là những phần từ nảo trong list thoả mãn điểm kiện thì nó sẽ được filter trả ra vào 1 cái list mới

# a = [17, 21, 22, 23] 

# custom =  list(filter(lambda x: x > 17, a)) # [17, 21, 22, 23] 

# print(custom)


# data = [
#     {
#         "id": 1,
#         "name": "Nguyễn Xuân Mạnh",
#         "age": 22,
#         "address": "Hà Nội",
#         "gender": "Nam",
#         "price": 1000
#     },
#     {
#         "id": 2,
#         "name": "Thảo",
#         "age": 20,
#         "address": "Hải Dương",
#         "gender": "Nữ",
#         "price": 3000
#     }
# ]
# Thưởng cho mỗi người 500đ
# result1 = list(map(lambda x : x.get("price") + 500, data))
# print(result1)
# Tìm ra người ở Hà Nội
# result2 = list(filter(lambda x : x.get("address") == "Hải Dương", data))

# print(result2)


# If else và lambda


# findMax = lambda x, y : x if x > y else y

# # Hàm findMax nhận vào 2 tham là x, và y. trả về x nếu x > y người lại trả về y
# print(findMax(10, 20))



# List comprehension và lambda 







# if __name__ == '__main__':
    # res = (lambda x : x ** 2)(10)
    # print(f"res: ", res)
    # Keyword arg
    # res = (lambda x, y, z : x - y + z) (y=10, x=20, z=30)
    # print(f"res: ", res)
    
    # Default paramters 
    # Nó chỉ ăn giá trị mặc định khi và chỉ khi ta không truyền vào đói số tương ứng của nó
    # res = (lambda x, y, z = 40 : x - y + z) (10, 20, 60)
    # print(f"res: ", res)
    
    # print(func(4))
    
    
# Map và filter
# map(hàm, list) là một hàm buil in có  sẵn trong python, nó nhận vào 2 đối số là 1 hàm, và list, tuppe, str..
# map nó sẽ trả về một đối tượng thuộc lớp map,  ta nên ép nó sáng list để dễ sử dụng

# a = range(5)

# print(a)

# 'A'
# ord -> là một hàm bui-on và nó nhận vào 1 thâm số duy nhất là các kí tự.
# ord('f') => 102 vì trong bảng mã acci nó có thự tự như vậy
# print(ord('f'))


# i = input().split(" ")
# # "10 20 30 40 50"
# print(i)

# a = list(map(int, input().split(" ")))

# print(a)


# a = [1, 2, 3, 4]
# b = [2, 3, 4, 5]

# result = list(map(lambda a, b : a - b, a, b))

# print(result) # [3, 5, 7, 9]



# Hàm filter được sử dụng để trích xuất các phần tử trong một cấu trúc có thể lặp, khi apply một hàm nào đó, nếu là true phần tử đó sẽ được trả về
# Cấu trúc: filter (fun, [list, tuppe, str...])
# Giá trị trả về: filter trả về một đối tượng của lớp filter, ta nên ép nó qua list để dễ dùng
