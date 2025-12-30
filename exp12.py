import pandas as pd
import numpy as np

# Create DataFrame with random values
df = pd.DataFrame(
    np.random.randint(1, 20, size=(10, 4)),
    columns=['A', 'B', 'C', 'D']
)

# Apply background and font color
styled_df = df.style.set_properties(
    **{
        'background-color': 'black',
        'color': 'yellow'
    }
)

# Save output to HTML file
styled_df.to_html("exp12_output.html")

print("Output saved as exp12_output.html")
