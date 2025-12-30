import pandas as pd
import numpy as np

data = {
    'A': [1, np.nan, 5, np.nan],
    'B': [np.nan, np.nan, 6, 2],
    'C': [np.nan, 3, 7, np.nan],
    'D': [4, 4, 8, np.nan]
}

df = pd.DataFrame(data)

# Keep rows with at least 2 NaN values
result = df[df.isnull().sum(axis=1) >= 2]

print(result)
