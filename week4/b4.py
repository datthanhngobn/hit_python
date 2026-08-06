danh_sach = []

while True :
    hs = {}
    hs["ten"] = input("Ten hoc sinh: ")
    if (hs["ten"] == " ") :
        break
    
    hs["Toan"] = int(input("Diem toan: "))
    hs["Van"] = int(input("Diem van: "))
    hs["Anh"] = int(input("Diem anh: "))
    hs["tong"] = hs["Toan"] + hs["Van"] + hs["Anh"]

    danh_sach.append(hs)

    

a = sorted(danh_sach, key=lambda x : -x["Toan"])

print(list(map(lambda x : x["ten"], a)))

a = max(danh_sach, key=lambda x : x["Anh"])

print(list(map(lambda x : x["ten"], filter(lambda x : x["Anh"] == a["Anh"], danh_sach))))

a = sorted(danh_sach, key=lambda x : (-x["tong"], x["ten"]))

print(list(map(lambda x : x["ten"], a)))

a = sorted(filter(lambda x : x["tong"] >= 24, danh_sach), key=lambda x : -x["tong"])

print(list(map(lambda x : x["ten"], a)))