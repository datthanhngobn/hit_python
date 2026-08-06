n = int(input("So luong san pham: "))

kho_hang = []

for i in range(n) :
    sp = {}
    sp["ma_sp"] = input("Ma san pham: ")
    sp["ten_sp"] = input("Ten san pham: ")
    sp["danh_muc"] = input("Danh muc san pham: ")
    sp["gia"] = int(input("Gia san pham: "))
    sp["ton_kho"] = int(input("San pham ton kho: "))
    kho_hang.append(sp)


print(list(filter(lambda x : x["danh_muc"] == "Dien tu", kho_hang)))

print(list(filter(lambda x : x["ton_kho"] == 0, kho_hang)))

print(list(map(lambda x : x["ten_sp"], kho_hang)))

print(list(map(lambda x : f"Tang voucher 100k cho khach mua {x["ten_sp"]}", filter(lambda x : x["gia"] >= 1000000, kho_hang))))