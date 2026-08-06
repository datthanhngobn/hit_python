x = int(input("Nhập số tiền của sản phẩm: "))
y = int(input("Nhập số tiền khách trả: "))

temp = tra_lai = y - x

menh_gia = [1, 2, 5, 10, 20]
count = 0

for i in range(4, -1, -1) :
    count += int(temp / menh_gia[i])
    temp = temp % menh_gia[i]
    if (temp == 0) :
        break

print(count)