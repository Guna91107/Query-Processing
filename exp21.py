import pandas as pd

data = {
    'Name': ['Anastasia', 'dImA', 'KATHERINE', 'James', 'emily']
}

df = pd.DataFrame(data)

df['Name'] = df['Name'].str.swapcase()

print(df)
