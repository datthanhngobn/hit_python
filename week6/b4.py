import numpy as np

arr1 = np.random.randint(1, 50, size=(5, 3))

arr2 = np.random.randint(1, 500, size=(5, 1))

matches = np.hstack((arr1, arr2))
print("Bang thong ke state: ")
print(matches)

print("KDA 3 tran gan nhat: ")
print(matches[0:3, 0:3])

temp_arr = matches[:, 0] * (1 / matches[:, 1])
print(f"K/D: {np.round(temp_arr, decimals=2)}")

print(f" So kill cao nhat: {matches[:, 0].max(axis=0)}")

print(f"Tong so assists: {matches[:, 2].sum(axis=0)}")

print(f"Combat Score thap nhat {matches[:, 2].min(axis=0)}")

print("Du lieu chuan bi ve bieu do: ") 
print(matches.T)