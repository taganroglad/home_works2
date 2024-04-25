import numpy as np
import matplotlib.pyplot as plt
noise = np.random.normal(loc=0, scale=0.2, size=100)

plt.hist(noise)
plt.hist(noise,bins=50)
plt.title("Гистограмма пограшностей")
plt.xlabel("Погрешность, мм")
plt.ylabel("Количество")
plt.xlim(-1, 1)
plt.show()