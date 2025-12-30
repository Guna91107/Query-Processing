import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': ['2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07'],
    'Close': [772.56, 776.43, 776.47, 776.86, 775.08]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

plt.plot(df['Date'], df['Close'])
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Alphabet Inc. Stock Prices')
plt.show()