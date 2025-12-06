# DICTIONARY (dict) {}
# VD: dùng dict để lưu thông tin
# Cách 1 thông dụng nhất
# a = {
#     # key    value
#     "name": "Thảo",
#     "age": 20,
#     "city": 'HanQuoc',
#     "status": True
# }
# print(a)

# cách 2 dùng dict constructor  dict()

# a = [["name", "Thảo"], ["age", 20], ["city", "HanQuoc"], ["status", True]]
# print(type(a))

# print(dict(a))

# cách 3 tạo dict bằng hàm zip(key, value)
# k = ["name", "age", "city", "status"]  # key

# v = ["Thảo", 20, "HanQuoc", True] # value

# print(dict(zip(k, v)))


# Cách 4  tạo dict bằng hàm fromkey(key(list), value from key)

# a = ['a', 'b', 'c']

# # default_value = 0
# b = [10, 20, 30]

# # b = dict.fromkeys(a, default_value)
# b = dict.fromkeys(a, b)
# print(b)
 

# Tính chất của dict -> key trong dict nó là duy nhất, nếu có nhiều thì nó sẽ lấy value cái cuối cùng (mới nhất) của dict
# Key phải là object (int, float, str) và không thể thay đổi. Ta có thể sử dụng nhiều kiểu dữ liệu trong python để làm key (int, float, str..)
# a = {
#     "name": "Mạnh",
#     "age": 25,
#     "name": "Thảo"
# }


# print(a)

# a = {
#     22: "age",
#     "Thao": "city",
#     # [1, 2, 3]: "Manh" # error dict không chấp nhật list, các kiểu tập hợp trừ chuỗi làm key
# }


# print(a)



# Cách 1. truy cập phần tử trong dict 
# Cú pháp: dict[key] -> ra value
# infor = {
#     "name": "Nguyễn Văn A",
#     "age": 20,
#     "address": "Hà Nội",
#     "class": "A7K5"
# }
# print(infor["name"])
# print(infor["age"])
# print(infor["address"])
# print(infor["class"])
# # truy cập tới 1 key không có trong object dict thì nó sẽ báo lỗi Key error
# print(infor["gender"])

# Cách 2: dùng hàm get(key) để tránh lỗi truy cập vào key không tồn tại trong dict. Hàm này sẽ trả về None khi không có key đó ở trong dict
# print(infor.get("name"))
# print(infor.get("age"))
# print(infor.get("address"))
# print(infor.get("class"))
# print(infor.get("gender")) # None

# Duyệt dict() ta có thể dùng các hàm của dict -> keys(), values(), items() để lấy ra các giá trị theo từng trường hợp
# infor = {
#     "name": "Nguyễn Văn C",
#     "age": 50,
#     "address": "HCM"
# }

# keys_data = list(infor.keys()) # trả về 1 mảng gồm toàn key# ['name', 'age', 'address']
# values_data = list(infor.values()) # trả về 1 mảng gồm toàn values ['Nguyễn Văn C', 50, 'HCM']
# items_data = list(infor.items()) # trả về các item ở trong dict dưới dạng data tuppe

# print(keys_data)
# print(values_data)
# print(items_data)


# Cách duyệt dict mặc định

# infor = {
#     "name": "Nguyễn Văn C",
#     "age": 50,
#     "address": "HCM"
# }

# khi duyệt bằng for in với dict nó sẽ gán lại các key vào 
# Cách 1
# for key in infor:
#     print(f"{key};{infor.get(key)}")

# Cách 2: duyệt qua infor.items() nó trả về dict_items([('name', 'Nguyễn Văn C'), ('age', 50), ('address', 'HCM')])

# print(infor.items())

# for (key, value) in infor.items():
#     print(key, value)

# Cách 3 dùng khi muốn duyệt quá các value của dict values
# for x in infor.values():
#     print(x)
# Cách 4 dùng khi muốn duyệt qua value của object
# for x in infor.keys():
#     print(x)


# Thêm và sửa dict

# infor = {
#     "name": "Nguyễn Văn C",
#     "age": 50,
#     "address": "HCM",
#     # "name": "Nguyễn Xuân Mạnh"
# }
# # Cú pháp thêm key và value sau khi đã định nghĩa dict
# infor["gender"] = "Nam"
# infor["school"] = "Trường học"

# # Cú pháp gán lại giá trị trong dict sau khi đã định nghĩa
# infor["name"] = "Nguyễn Xuân Mạnh"


# print(infor)


# Xoá phần tử ở trong dict
# Cách 1: Dùng hàm pop("key") -> lưu ý nếu key không có thì sẽ tạo ra lỗi. Và khi xoá thành công thì nó sẽ trả về phần tử đã bị mình xoá
# infor = {
#     "name": "Nguyễn Văn C",
#     "age": 50,
#     "address": "HCM",
#     "gender": "Nam"
# }
# # infor.pop("address")
# is_exits = infor.get("gender")

# # Fix lỗi xoá key không tồn tại trong dict
# if is_exits != None:
#     infor.pop("gender")

# print(infor)

# Cách 2: Dùng hàm del để xoá nhưng không cần trả về phần tử cần xoá
# Cú pháp: del dict["key"]

# del infor["name"]
# is_exits = infor.get("xvvvv") # infor[""]
# if is_exits != None:
#     del infor["xvvvv"]
# print(infor)

# Cách 3: dùng hàm popitem() để xoá 1 phần tử cuối cùng trong dict rồi trả về list thay đổi, nhưng không làm thay đổi dict ban đầu
# result =  infor.popitem()

# print(result)
# print(infor)

# Cách 4: dùng hàm clear() để xoá tất cả phần tử ở trong dict
# infor.clear()

# print(infor)

# Kiểm tra sự tồn tại của key và value
# Ta có thể sử dụng từ khoá in để kiểm tra sự tồn tại của key, hoặc value ở trong dict
# infor = {
#     "name": "Nguyễn Văn C",
#     "age": 50,
#     "address": "HCM",
#     "gender": "Nam"
# }
# a = [1, 2, 3, 4]
# print(10 in a) # false
# if 10 in a:
#     print("True")
# else:
#     print("False")
# Kiểm tra key có ở trong dict không?
# print("name" in infor) # tương tự như print("name" in infor.keys())
# Kiểm tra có tồn tại value đó ở trong dict hay không
# print(50 in infor.values()) # True
# print(70 in infor.values())
# a = [1, 2, 3]

# b = [4, 5, 6]
# # a.extend(b)
# # a = a + b
# print(a)


# Trộn 2 dict  dùng hàm update để hợp 2 dict
a = {
    "name": "Mạnh",
    "address":  "Hà Nôi"
}
b = {
    "age": 50
}
a.update(b)
print(a)
for (key, value) in a.items():
    print(key, value)









