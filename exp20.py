import pandas as pd

# Create DataFrame
data = {
    'Name': ['Anastasia', 'Dima', 'Katherine', 'James',
             'Emily', 'Michael', 'Matthew', 'Laura',
             'Kevin', 'Jonas']
}

df = pd.DataFrame(data)

# Find index of rows containing substring 'an'
result = df[df['Name'].str.contains('an', case=False)]

print("Index of rows containing substring 'an':")
print(result.index.tolist())
