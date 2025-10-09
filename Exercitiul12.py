import pandas as pd
import numpy as np
df = pd.DataFrame({
    'Index':[1,2,3,4],
    'Name': ['Marian', 'Ion', 'Alexia', np.nan],
    'Sex': ['M','M','F', np.nan]
})

df2= pd.DataFrame({
    'Index_nume': [1,2,3,4],
    'Varsta':[23,24,16,23]
})

df_merge_left = pd.merge(df, df2, left_on='Index', right_on='Index_nume', indicator=True , how='left')
print(df_merge_left.to_string())