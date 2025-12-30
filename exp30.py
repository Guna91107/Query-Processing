import matplotlib.pyplot as plt
import numpy as np

men_scores = [22, 30, 35, 35, 26]
women_scores = [25, 32, 30, 35, 29]

groups = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E']

x = np.arange(len(groups))
width = 0.35

plt.bar(x - width/2, men_scores, width, label='Men')
plt.bar(x + width/2, women_scores, width, label='Women')

plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(x, groups)
plt.legend()

plt.show()
