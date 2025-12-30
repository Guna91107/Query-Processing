import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randint(1, 20, size=(10, 4)),
    columns=['A', 'B', 'C', 'D']
)

df.iloc[2, 1] = np.nan
df.iloc[5, 3] = np.nan
df.iloc[7, 0] = np.nan

def highlight_nan(val):
    if pd.isna(val):
        return 'background-color: yellow'
    return ''

styled_df = df.style.map(highlight_nan)

styled_df.to_html("exp11_output.html")

print("Output saved as exp11_output.html")
