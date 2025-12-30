import pandas as pd
import numpy as np

data = {
    'A': [10, 15, np.nan, 12],
    'B': [20, np.nan, 18, 24],
    'C': [np.nan, 25, 22, 28],
    'D': [40, 35, 30, np.nan]
}

df = pd.DataFrame(data)

missing_values = df.isna()

print(missing_values)
