import pandas as pd

# Creating the DataFrame
data = {
    'Name': ['Anastasia', 'dImA', 'KATHERINE', 'James', 'emily']
}

df = pd.DataFrame(data)

# Swap case of the Name column
df['Name'] = df['Name'].str.swapcase()

print(df)
