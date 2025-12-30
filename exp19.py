import pandas as pd

# Creating sample World Alcohol Consumption DataFrame
data = {
    'Country': ['Afghanistan', 'Albania', 'Algeria', 'Andorra'],
    'Region': ['Asia', 'Europe', 'Africa', 'Europe'],
    'Year': [1986, 1986, 1986, 1986],
    'Beer': [0.0, 89.8, 25.0, 245.0],
    'Wine': [0.0, 21.1, 0.0, 138.0],
    'Spirits': [0.0, 54.0, 0.0, 312.0]
}

df = pd.DataFrame(data)

# Display shape of the dataset
print("Dataset Shape (Rows, Columns):")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)
