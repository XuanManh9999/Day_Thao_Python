# Cách định nghĩa func
# tham số của hàm không bắt buộc phải có
# một hàm có 2 dạng, có kết quả trả về (dùng từ khoá return) hàm không trả về (mặc định nó là None)
# Hàm chỉ được kích hoạt khi ta gọi tên hàm đó
def ten_ham(tham_so1=10, tham_so2=20): # giá trị khi định nghĩa hàm này người ta gọi là  tham số
    print(f"Tham so1: {tham_so1}")
    print(f"Tham so2: {tham_so2}")
    for i in range(0, 10):
        print("VIET NAM")
        
# Nếu file có hàm main thì khi chạy file nó sẽ chạy code từ hàm main trước
if __name__ == '__main__':
    hello = 'HALLO WORLD'
    # data = 1
    print(hello)
    ten_ham(tham_so2=5,tham_so1=10) # giá trị truyền vào khi gọi hàm gọi là đối số