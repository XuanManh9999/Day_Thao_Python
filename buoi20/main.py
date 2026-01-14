# Thuật toán tìm kiếm trong python

# Thuật toán tìm kiếm tuyến tính (nó duyệt tuần tự từ đầu tới cuối, nếu thoả mãn thì trả về phần tử đó)
# Tìm bạn sv có GPA >= 3.4
data = [
    {
        "id": 1,
        "name": "Thảo",
        "GPA": 3.33
    },
    {
        "id": 2,
        "name": "Mạnh",
        "GPA": 3.4
    },
    {
        "id": 3,
        "name": "Khải",
        "GPA": 3.6
    },
    {
        "id": 4,
        "name": "Khải",
        "GPA": 3.7
    }
]
# Tìm 1 bạn ?
# data = list(filter(lambda x : x.get("GPA") > 3.4, data))
# print(data)

# for i in data:
#     if i.get("GPA") > 3.4:
#         print(i)
# 
# # break

# f = [0] * 100000000

# cnt = 0
# tim = 100000000 - 2
# for i in f:
#     print(cnt)
#     cnt += 1
    
#     if cnt == tim:
#         print("TIM DEN")
#         break
    

# Để sử dụng được thuật toán tìm kiếm nhị phân ta cần: Tìm kiếm nhị phân - Binary search được sử dụng trên dãy số đã được sắp xếp tăng dần hoặc giảm dần.
# Ý tưởng của thuật toán đó là ở mỗi lần tìm kiếm trên đoạn [L, R] thì bạn sẽ tìm ra phần tử đứng giữa và so sánh với phần tử X, vì mảng đã sắp xếp tăng dần nên khi so sánh X với phần tử đứng giữa bạn có thể loại bỏ đi 1 nửa khoảng tìm kiếm, cứ như vậy thì đoạn bạn cần tìm kiếm sẽ giảm đi 1 nửa sau mỗi lần tìm kiếm. 

# a = [2, 1, 3, 4]
# a = [1, 2, 3, 4]
# a.sort()
# print(a)
# 10 -> lặp 10 lần, 100 -> lập 100 lần, 1000 -> lặp 1000 lần

# Thuật toán : 

# Chia đôi đoạn tìm kiếm thành 2 nửa bằng cách tìm chỉ số đứng giữa của đoạn cần tìm kiếm, M = (L + R) / 2
# So sánh phần tử ở giữa đoạn là A[M] với phần tử cần tìm kiếm sẽ xảy ra 3 trường hợp 
# Nếu phần tử cần tìm kiếm bằng phần tử ở giữa thì kết luận tìm thấy
# Nếu phần tử cần tìm kiếm nhỏ hơn phần tử ở giữa thì loại bỏ nửa bên phải trong lần tìm kiếm tiếp theo
# Nếu phần tử cần tìm kiếm lớn hơn phần tử ở giữa thì loại bỏ nửa bên trái trong lần tìm kiếm tiếp theo
# Quá trình lặp đi lặp lại từ bước 1 tới bước 5 cho tới khi phần tử được tìm thấy hoặc không còn khoảng tìm kiếm

# Số lượng phần tử trong mảng là số chẵn

a = [0, 1, 3, 4] # list đã sort tăng dần. 4
x = 3 # Cần tìm là số 3
def binary_search(a, x):
    cnt = 0
    l = 0 # (index)
    r = len(a) - 1 # phần tử index cuối
    while l <= r: # 0 < 3 -> True; 2 < 3
        cnt += 1
        print(f"Lần: {cnt}")
        m = (l + r) // 2 # 1, 2
        print(f"m={m}")
        
        if a[m] == x: # 1 == 3 -> Flase, 3 == 3 -> TRUE
            print("Vào a[m] == x")
            return True
        elif a[m] < x: # 1 < 3 -> True
            print("Vào a[m] < x")
            l = m + 1 # l = 1 + 1 = 2 
        else:
            print(f"Vào a[m] < x")
            r = m  - 1
    return False
        
    
is_find =  binary_search(a, x)

if is_find:
    print("Tim thay")
else:
    print("Khong tim thay")
    