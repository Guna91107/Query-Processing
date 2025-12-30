import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50]
y1 = [20, 30, 40, 50, 60]
y2 = [25, 35, 45, 55, 65]

plt.plot(x, y1, color='blue', linewidth=2, label='Line 1')
plt.plot(x, y2, color='red', linewidth=3, label='Line 2')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Multiple Line Plot')

plt.legend()

plt.show()
