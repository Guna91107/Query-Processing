import pandas as pd

data = {
    'School_Code': ['S001', 'S002', 'S001', 'S002', 'S001', 'S002'],
    'Name': ['John', 'Alice', 'Robert', 'Sophia', 'Michael', 'Emma'],
    'Age': [15, 16, 14, 15, 16, 17]
}

df = pd.DataFrame(data)

result = df.groupby('School_Code')['Age'].agg(['mean', 'min', 'max'])

print(result)
