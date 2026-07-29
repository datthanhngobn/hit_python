list = []
check = set()

gia_Max = 0

x = int(input("Tong san pham: "))
length = x
saveIndex = 0
tong_Kho = 0

for i in range(x) :

    ma_san_pham = int(input("Nhap ma san pham: "))
    ten_san_pham = input("Nhap ten san pham: ")
    gia = int(input("Nhap ma gia san pham: "))
    so_luong = int(input("Nhap ma  so luong san pham: "))

    check.add(ma_san_pham)

    while len(check) != length or gia <= 0 or so_luong < 0 :

        print("Trung ma san pham. Nhap lai")

        ma_san_pham = int(input("Nhap ma san pham: "))
        ten_san_pham = input("Nhap ten san pham: ")
        gia = int(input("Nhap ma gia san pham: "))
        so_luong = int(input("Nhap ma  so luong san pham: "))

    item = (ma_san_pham, ten_san_pham, gia, so_luong)

    list.append(item)

    tong_Tien = item[2] * item[3]
    tong_Kho += tong_Tien
    if (gia_Max < tong_Tien) :
        gia_Max = tong_Tien
        indexMax = i

    print(f"Thanh tien san pham {i + 1} = {tong_Tien}")

print(f"San pham co gia tri lon nhat la {len(list)}")

for i in list :
    if (i[3] < 5) :
        print(i)



