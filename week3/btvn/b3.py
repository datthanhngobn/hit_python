A = list(input("So thich cua A: ").split(", "))
B = list(input("So thich cua B: ").split(", "))

stA = set(A)
stB = set(B)
stAnB = set(A + B)

onlyA = []
AnB = []

for i in stA :
    if (B.count(i) > 0) :
        AnB.append(i)
    else :
        onlyA.append(i)

print(f"So thich cua A: {stA}")
print(f"So thich cua B: {stB}")
print(f"So thich chung cua A va B: {AnB}")
print(f"So thich chi co A co: {onlyA}")
print(f"So thich cua ca A va B: {stAnB}")
print(f"Do tuong dong = {(len(AnB) * 100 / len(stAnB)):.2f}")
