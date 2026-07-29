n = int(input("So sinh vien: "))

list = []

sum = 0
max = 0
min = 10

for i in range(n) :
    point = int(input())
    while (0 >= point and point >= 10) :
        point = int(input())

    list.append(point)

    sum += point
    if (max < point) :
        max = point

    if (min > point) :
        min = point

    if (point == 10) :
        check = True


agr = sum / n

print(f"Diem trung binh = {agr}")
saveIndex = None
for i in list :
    if (i > agr) :
        saveIndex = i
        break

print(f"Diem lon nhat = {max}")
print(f"Diem nho nhat = {min}")
print(f"Danh sach diem lon hon tb = {list[saveIndex:]}")
print("Co diem 10" if check else "Khong co diem 10")
