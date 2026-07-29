x = input("Nhap 1 chuoi khong chua dau cach: ")

rev = ""
panlindrome = True
st = set(x)
countChar = 0
saveChar = []

check = set({'a', 'e', 'i' , 'o', 'u'})
res = True

for i in x : 
    rev = i + rev

print(f"Chuoi dao nguoc = {rev}")

print(f"Chuoi sap xep = {sorted(x)}")

for i in range(len(x)) :
    if (x[i] != len(x) - i - 1) :
        panlindrome = False

if (panlindrome) :
    print("Day la chuoi doi xung")
else :
    print("Day khong la chuoi doi xung")

for i in st :
    if (countChar < x.count(i)) :
        saveChar.clear()
        countChar = x.count(i)
        saveChar.append(i)
    elif (countChar == x.count(i)) :
        saveChar.append(i)
        
print(f"Ky tu xuat hien nhieu nhat: {saveChar} xuat hien {countChar}", sep=' ')

for i in check :
    if (x.count(i) == 0) :
        res = False

if (res) :
    print("Du 5 nguyen am")
else :
    print("Khong du 5 nguyen am")

