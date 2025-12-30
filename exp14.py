import pandas as pd
import numpy as np

data = {
    'A': [10, 15, np.nan, 40],
    'B': [20, np.nan, 30, 45],
    'C': [np.nan, 25, 35, 50]
}

df = pd.DataFrame(data)

df_filled = df.fillna(0)

print(df_filled)
