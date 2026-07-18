a = int(input("Nhap ngay: "))
b = int(input("Nhap thang: "))

if (b in (4, 6, 9, 11) and a > 30) :
    print("Ngay thang khong hop le")
elif (b in (1, 3, 5, 7, 8, 12) and a > 31) :
    print("Ngay thang khong hop le")
elif (b == 2 and a > 29) :
    print("Ngay thang khong hop le")
elif ((b == 1 and a <= 19) or (b == 12 and a >= 22)) :
    print("Ma ket")
elif ((b == 1 and a >= 20) or (b == 2 and a <= 18)) :
    print("Bao binh")
elif ((b == 2 and a >= 19) or (b == 3 and a <= 20)) :
    print("Song ngu")
elif ((b == 3 and a >= 21) or (b == 4 and a <= 19)) :
    print("Bach duong")
elif ((b == 4 and a >= 20) or (b == 5 and a <= 20)) :
    print("Kim nguu")
elif ((b == 5 and a >= 21) or (b == 6 and a <= 20)) :
    print("Song Tu")
elif ((b == 6 and a >= 21) or (b == 7 and a <= 22)) :
    print("Cu giai")
elif ((b == 7 and a >= 23) or (b == 8 and a <= 22)) :
    print("Su tu")
elif ((b == 8 and a >= 23) or (b == 9 and a <= 22)) :
    print("Xu nu")
elif ((b == 9 and a >= 23) or (b == 10 and a <= 22)) :
    print("Thien binh")
elif ((b == 10 and a >= 23) or (b == 11 and a <= 21)) :
    print("Bo cap")
else :
    print("Nhan ma")

