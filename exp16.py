import pandas as pd

data = {
    'School_Code': ['S001', 'S002', 'S001', 'S003', 'S002', 'S001'],
    'Class': ['V', 'VI', 'V', 'VII', 'VI', 'V'],
    'Name': ['John', 'Alice', 'Robert', 'Sophia', 'David', 'Emma'],
    'Age': [12, 13, 11, 14, 13, 12]
}

df = pd.DataFrame(data)

grouped = df.groupby('School_Code')

for name, group in grouped:
    print("\nSchool Code:", name)
    print(group)

print("\nType of GroupBy object:")
print(type(grouped))
