import numpy as np
from math import pi



t_data = np.linspace(0, 10*pi, 100)

print(t_data)
A = 3

y_data = A * np.cos(t_data)
import matplotlib.pyplot as plt

plt.plot(t_data, y_data, label='y(t) = A cos(t)')
plt.title("Колебание струны")
plt.xlabel("Время, с")
plt.ylabel("Отклонение, мм")
plt.legend()
plt.grid()
plt.ylim(-5, 5)



