import numpy as np

ls = [35, 42, 89, 125, 50, 80, 120, 200, 150, 220, 300, 450]

new_ls = np.reshape(ls, (4, 3))

print(new_ls)

print(f"Tong doanh thu tung quy {new_ls.sum(axis=1)}")

print(f"Doanh so cao nhat tung quy {new_ls.max(axis=1)}")

print(f"Danh sach cac thang co doanh thu bung no {new_ls[(new_ls > 80) & (new_ls < 200)]}")

add_ls = np.reshape([10, 15, 20, 30], (4, 1))

print(f"Bang sau khi gop them vao chi phi {np.hstack((new_ls, add_ls))}")