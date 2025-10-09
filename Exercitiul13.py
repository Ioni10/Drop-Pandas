import numpy as np
import pandas as pd

df = pd.DataFrame({
    'Nume':['Vasile', 'Andreea', 'Georgel', np.nan],
    'Sex': ['M', 'F', 'M', np.nan]
})


one_hot_encoding = pd.get_dummies(df['Sex'], dummy_na=True).astype(int)
print(one_hot_encoding)

df_concat = pd.concat([df, one_hot_encoding], axis= 1)
print(df_concat)