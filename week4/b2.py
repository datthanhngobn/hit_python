cel = int(input("chuyen doi nhiet do: "))

f = lambda cel : cel * 9/5 + 32

print(f"Nhiet do sau khi chuyen doi la: {f(cel)}")

isEven = lambda x : x % 2 == 0

x = int(input("Chan/Le: "))

if (isEven(x)) :
    print("Chan")
else :
    print(("Le"))

hoa_don = int(input("Hoa don: "))
phan_tram_tip = int(input("Phan tram tip: "))

tien_tip = lambda hoa_don, phan_tram_tip : hoa_don * phan_tram_tip / 100

print(tien_tip(hoa_don, phan_tram_tip))

name = input("Rut gon ten: ")

uppercase = lambda name : name.upper()

print(uppercase(name))