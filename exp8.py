import pandas as pd

data = {
    'Item': ['Television', 'Home Theater', 'Television', 'Cell Phone',
             'Television', 'Home Theater', 'Television', 'Television',
             'Television', 'Home Theater', 'Television', 'Home Theater',
             'Home Theater', 'Television', 'Desk', 'Video Games',
             'Home Theater', 'Cell Phone'],
    'Units': [95, 50, 36, 27, 56, 60, 75, 90, 32, 60, 90,
              29, 81, 35, 2, 16, 28, 64]
}

df = pd.DataFrame(data)

pivot_units = pd.pivot_table(
    df,
    index='Item',
    values='Units',
    aggfunc='sum'
)

print(pivot_units)  