x = list(input("Nhập chuỗi cần kiểm tra: ").split())
y = input("Nhập target: ")

res = []

for i in range(len(x)) :
    if (x[i] == y) :
        res.append(i)

if (len(res) == 0) :
    print(-1)
else :
    print(res)