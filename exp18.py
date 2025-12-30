import pandas as pd

data = {
    'School_Code': ['S001', 'S001', 'S001', 'S002', 'S002', 'S002'],
    'Class': [10, 10, 9, 10, 9, 9],
    'Name': ['John', 'Alice', 'Bob', 'David', 'Eva', 'Frank'],
    'Age': [15, 14, 13, 15, 14, 13]
}

df = pd.DataFrame(data)

grouped = df.groupby(['School_Code', 'Class'])

for name, group in grouped:
    print("\nGroup:", name)
    print(group)
