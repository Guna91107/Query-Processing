import matplotlib.pyplot as plt

math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]

plt.scatter(math_marks, science_marks)

plt.xlabel("Mathematics Marks")
plt.ylabel("Science Marks")
plt.title("Scatter Plot of Mathematics vs Science Marks")

plt.show()
