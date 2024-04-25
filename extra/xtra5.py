import matplotlib.pyplot as plt

from extra.xtra3 import noise
from extra.xtra4 import y_data, t_data

y_noise = y_data + noise

plt.plot(t_data, y_noise, '.', label='y (noise)')
plt.plot(t_data, y_data, linestyle='solid', label='y (ideal)')
plt.title("Колебание струны")
plt.xlabel("Время, с")
plt.ylabel("Отклонение, мм")
plt.legend()
plt.grid()
plt.ylim(-5, 5)
plt.show()