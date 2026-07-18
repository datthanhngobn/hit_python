N = int(input("So tien N cho truoc: "))

res = int(N / 28)
now = res
extra = 0

while now > 0 :
    res += (now + extra) // 3
    extra = now % 3
    now = now // 3
    
print(f"So chia bia co the mua duoc la {res}")