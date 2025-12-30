import pandas as pd
import numpy as np

# Create DataFrame with random values
df = pd.DataFrame(
    np.random.randint(1, 20, size=(10, 4)),
    columns=['A', 'B', 'C', 'D']
)

# Convert some values to NaN
df.iloc[2, 1] = np.nan
df.iloc[5, 3] = np.nan
df.iloc[7, 0] = np.nan

# Function to highlight NaN values
def highlight_nan(val):
    if pd.isna(val):
        return 'background-color: yellow'
    return ''

# Apply styling
styled_df = df.style.map(highlight_nan)

# Save output to HTML file
styled_df.to_html("exp11_output.html")

print("Output saved as exp11_output.html")
