# Python có 3 phạm vi biến:
# +, Local scope
# +, Global scope: phạm vi toàn file
# +, Enclosing scope

# Local scope: khai báo biến nằm bên trong hàm, phạm vi sử dụng của nó chỉ nằm bên trong hàm thôi, nó sẽ chỉ sống khi mà hàm đó còn được gọi.
# Một biến local scope sẽ chỉ được khởi tạo khi hàm nó nằm trong chưa kết thúc.
# def logs():
#     a = 10 # pham vi của nó là local thì ta chỉ có thể truy cập được biến a ở phạm vi nằm bên trong hàm
    
#     def print_a():

#         print(a)

#         b = 12
#         print(b)
#     print_a()
    
# # def d ():
# #     print(a)

# logs()
# # d()

# def a ():
#     a = 10
#     def b ():
#         b = 20
#         print(a)
#         print(b)
#         def c():
#             c = 30
#             print(b)
#             print(c)
#         c()
#     b()    
# a()
# 10 20 20 30

# 2. Global scope
# Nó là phạm vi khác hàm, hoặc các block code (tab). Phạm vi của nó sẽ có thể được truy cập ở toàn bộ chương trình tính từ thời điểm mà nó được khai báo
# print(a) # error vì tại thời điểm này biến a chưa được khai báo và khởi tạo giá trị

# a = 12 # global scope

# def hello():
#     print(a)
    
# for i in range(0, 2, 1):
#     print(a)
# hello()

# x = 1000 # global sccope


# def printNum():
#     x = 2000 # local scope
#     print(x)

# printNum()
# print(x)

# 2000 (local), 1000 (global)



# x = 1000 # global sccope


# def printNum():
#     global x  # Tôi sẽ xử dụng biến global (lúc này python sẽ quyét vùng nhớ và tìm biến global). Tìm nó
#     x = 2000 # sử dụng x global để gán giá trị
#     print(x)

# printNum()
# print(x)



# Enclosing scope: trong hàm lồng nhau, khi mình khai báo 2 biến cùng tên, ở trong 2 hàm này thì hai biến đó có phạm vi khác nhau


# def ham1():
#     a = 10 # local scope
    
#     def ham2():
#         a = 20 # local scope
#         print(a)
#     print(a)
#     ham2()

# ham1()# 10 20

# Enclosing
# Để có thể sử dụng lại giá trị từ hàm bên ngoài (hàm cha) khi có biến trùng tên

# def ham1():
#     a = 10 # local scope
    
#     def ham2():
#         nonlocal a # tìm trong các cấp ngoài tìm biến local 
#         a = 20 # local scope
#         print(a)
#     ham2()
#     print(a)

# ham1()


# LOCAL (khai bao trong hàm, trong khối), GLOBAL (khai báo ngoài hàm, và ngoài các khối)
# từ khoá global: Sự dụng biến global 
# từ khoá nonlocal: Sử dụng biến cha của nó, không tạo biến local mới

tien_cua_em = 5000 # global 

def mua_sam():
    # tien_cua_em = 1000
    global tien_cua_em
    
    ao = 4000
    
    tien_cua_em -= ao
    
    print(tien_cua_em)
    

mua_sam()