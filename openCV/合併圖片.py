# ch3_18.py
import numpy as np

x1 = np.arange(4).reshape(2,2)
print(f"陣列 1 \n{x1}")
x2 = np.arange(4,8).reshape(2,2)
print(f"陣列 2 \n{x2}")
x = np.hstack((x1,x2)) #水平合併
print(f"合併結果 \n{x}")

x = np.vstack((x1,x2)) #垂直合併
print(f"合併結果 \n{x}")
















 
