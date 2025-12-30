import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

plt.plot(x, y1, label='Linear Data')

plt.plot(x, y2, label='Square Data')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Multiple Plots Example')
plt.legend()

plt.show()
