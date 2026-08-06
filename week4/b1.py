kho_hang_tong = dict()

def quan_ly_kho_hang(kho_hang, sp_moi, sp_xoa) :
    sum = 0

    for i in range(len(kho_hang)) :
        a = list(kho_hang[i].split(":"))
        kho_hang_tong[a[0]] = int(a[1])

    print(f"So luong laptop ban dau: {kho_hang_tong.get("Laptop", 0)}")

    for i in range(len(sp_moi)) :
        a = list(kho_hang[i].split(":"))
        kho_hang_tong.update({a[0] : int(a[1])})

    print(f"Ket qua xoa {sp_xoa}: {kho_hang_tong.get(sp_xoa)}")
    kho_hang_tong.pop(sp_xoa, None)

    print(f"Cac san pham hien co: {kho_hang_tong.keys()}")

    for x in kho_hang_tong.values() :
        sum += x
    

    print(f"Tong kho hang la: {sum}")

kho_hang = list(input("Kho hang: ").replace('"', "").split(","))
sp_moi = list(input("San pham moi: ").replace('"', " ").split(","))
sp_xoa = input("San pham xoa: ").replace('"', "")

quan_ly_kho_hang(kho_hang, sp_moi, sp_xoa)

