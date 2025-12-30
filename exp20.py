import pandas as pd

data = {
    'Name': ['Anastasia', 'Dima', 'Katherine', 'James',
             'Emily', 'Michael', 'Matthew', 'Laura',
             'Kevin', 'Jonas']
}

df = pd.DataFrame(data)

result = df[df['Name'].str.contains('an', case=False)]

print("Index of rows containing substring 'an':")
print(result.index.tolist())
