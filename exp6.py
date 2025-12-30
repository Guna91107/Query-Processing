import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Close': [772.56, 776.43, 776.47, 776.86, 775.08],
    'Volume': [1995600, 1568100, 1465300, 1572100, 1491200]
}

df = pd.DataFrame(data)

plt.scatter(df['Volume'], df['Close'])
plt.xlabel('Trading Volume')
plt.ylabel('Closing Price')
plt.title('Alphabet Inc: Volume vs Closing Price')
plt.show()