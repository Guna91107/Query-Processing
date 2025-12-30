import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(10, 100, 20)
y = np.random.randint(10, 100, 20)

plt.scatter(x, y, facecolors='none', edgecolors='black')

plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Scatter Plot with Empty Circles')

plt.show()
