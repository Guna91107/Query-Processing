import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randint(-10, 10, size=(10, 4)),
    columns=['A', 'B', 'C', 'D']
)

def highlight_values(val):
    return 'color: red' if val < 0 else 'color: black'

styled_df = df.style.map(highlight_values)

styled_df.to_html("exp10_output.html")

print("Output saved as exp10_output.html")