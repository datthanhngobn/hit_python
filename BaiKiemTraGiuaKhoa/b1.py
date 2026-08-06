x = int(input("Nhập giá trị của biến x: "))
n = list(map(int,input("Nhập hệ số của hàm: ").split()))

sum = 0

for i in range(len(n) - 1, 0, -1) :
    sum += n[i] * x**i

print(sum)