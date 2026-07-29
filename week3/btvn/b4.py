n = int(input("So luong khoan chi tieu: "))
khoan_chi = []
total = 0
st = set()
maxPrice = 0
saveIndex = []

for i in range(n) :
    ip = list(input("Nhap khoan chi: ").split(","))
    name = ip[0]
    price = int(ip[1])
    danh_muc = ip[2]
    khoan_chi.append((name, price, danh_muc))

    total += price
    
    if (maxPrice < price) :
        maxPrice = price
        saveIndex.append(i)


    st.add(danh_muc)

print(f"Danh sach cac khoan chi")
for i in khoan_chi :
    print(i)

print(f"Tong chi tieu = {total}")

lst = list(st) + [0] * 2 * n 

for i in khoan_chi :
    index = lst.index(i[2])
    lst[index + n] += 1
    lst[index + 2 * n] += i[1]

for i in range(len(st)) :
    print(lst[i])
    print(f"- So khoan chi: {lst[i + n]}")
    print(f"- Tong tien: {lst[i + 2 *n ]} VND")

if (total > 5000000) :
    print("Vuot qua 5 trieu")