import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("fdata.csv")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%y')

# Plot line charts
plt.plot(df['Date'], df['Open'], label='Open')
plt.plot(df['Date'], df['High'], label='High')
plt.plot(df['Date'], df['Low'], label='Low')
plt.plot(df['Date'], df['Close'], label='Close')

# Labels and title
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Alphabet Inc Financial Data (Oct 3–7, 2016)')
plt.legend()

plt.show()
