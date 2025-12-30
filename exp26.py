import matplotlib.pyplot as plt

# Input data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 4, 9, 16, 25]

# First plot
plt.plot(x, y1, label='Linear Data')

# Second plot
plt.plot(x, y2, label='Square Data')

# Labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Multiple Plots Example')
plt.legend()

# Display plot
plt.show()
