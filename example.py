import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
print(x)
y = 3*x + 1

plt.plot(x, y)
plt.show()
