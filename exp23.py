import matplotlib.pyplot as plt

x = []
y = []

with open("test.txt", "r") as file:
    for line in file:
        values = line.split()
        x.append(int(values[0]))
        y.append(int(values[1]))

plt.plot(x, y)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Graph from Text File")
plt.show()
