a = int(input("Nhap thang: "))
b = int(input("Nhap nam: "))

if (b % 4 == 0 and a == 2):
    print(f"Thang {a}, nam {b} co {29} ngay")
elif (b % 4 != 0 and a == 2) :
    print(f"Thang {a}, nam {b} co {28} ngay")
elif (a in (4, 6, 9, 11)) :
    print(f"Thang {a}, nam {b} co {30} ngay")
else :
    print(f"Thang {a}, nam {b} co {31} ngay")
