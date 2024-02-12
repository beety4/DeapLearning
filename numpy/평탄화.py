import numpy as np

X = np.array([[1, 2, 3, 4], [6, 7, 8, 9]])
X = X.flatten()
print(f"{X} --- {type(X)}")

# Find index 0, 3
B = X[np.array([0, 3])]
print(B)

# 뭔가 Stream API 느낌
print(X[X>7])
print(X > 7, " --- ", type(X>7))

# bool형 리스트 테스트
bLst = [False, True]
print(B[bLst])
