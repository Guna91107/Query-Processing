import matplotlib.pyplot as plt

height1 = [150, 155, 160, 165, 170]
weight1 = [50, 55, 60, 65, 70]

height2 = [160, 165, 170, 175, 180]
weight2 = [60, 65, 70, 75, 80]

height3 = [170, 175, 180, 185, 190]
weight3 = [70, 75, 80, 85, 90]

plt.scatter(height1, weight1, label='Group 1')
plt.scatter(height2, weight2, label='Group 2')
plt.scatter(height3, weight3, label='Group 3')

plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.title('Scatter Plot of Height vs Weight for Three Groups')
plt.legend()

plt.show()
