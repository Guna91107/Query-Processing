import matplotlib.pyplot as plt
import numpy as np

men_means = (22, 30, 35, 35, 26)
women_means = (25, 32, 30, 35, 29)

men_std = (4, 3, 4, 1, 5)
women_std = (3, 5, 2, 3, 3)

ind = np.arange(len(men_means))
width = 0.5

plt.bar(ind, men_means, width, yerr=men_std, label='Men')
plt.bar(ind, women_means, width, bottom=men_means, yerr=women_std, label='Women')

plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Stacked Bar Plot with Error Bars')
plt.xticks(ind, ['A', 'B', 'C', 'D', 'E'])
plt.legend()

plt.show()
