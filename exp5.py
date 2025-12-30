import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': ['2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07'],
    'Volume': [1995600, 1568100, 1465300, 1572100, 1491200]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

plt.bar(df['Date'], df['Volume'])
plt.xlabel('Date')
plt.ylabel('Trading Volume')
plt.title('Alphabet Inc Trading Volume')
plt.show()