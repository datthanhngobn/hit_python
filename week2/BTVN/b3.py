a = int(input("Nhap so nguyen n: "))

count = 0
i = a
sum = 0
check = True

while i > 0 :
    i /= 10
    count += 1
    sum += i

print(f"Chu so n co {count} chu so")
print(f"Tong cac chu so cua n la {sum}")

for j in range(2, int(a**0.5)) :
    if (a % j == 0) :
        check = False
        break

if (check) :
    print("n la so nguyen to")
else :
    print("n khong la so nguyen to")