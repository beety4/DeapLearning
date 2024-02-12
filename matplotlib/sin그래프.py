import numpy as np
import matplotlib.pyplot as plt

# 0~6 까지의 수를 0.1간격으로 생성
x = np.arange(0, 6, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.show()

