import pandas as pd

data = {
    'Item': ['Television', 'Home Theater', 'Television', 'Cell Phone',
             'Television', 'Home Theater', 'Television', 'Television',
             'Television', 'Home Theater', 'Television', 'Home Theater',
             'Home Theater', 'Television', 'Desk', 'Video Games',
             'Home Theater', 'Cell Phone'],
    'Sale_amt': [113810, 25000, 43128, 6075, 67088, 30000, 89850,
                 107820, 38336, 30000, 107820, 14500, 40500,
                 41930, 250, 936, 14000, 14400]
}

df = pd.DataFrame(data)

pivot_table = pd.pivot_table(
    df,
    index='Item',
    values='Sale_amt',
    aggfunc=['max', 'min']
)

print(pivot_table)