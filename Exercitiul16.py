#16)Rolling window: media mobila pe 7zile pentru o coloana; adauga ca noua coloana
import pandas as pd

dates = pd.date_range(start='2025-01-01', end='2025-01-10')
values = [12,36,27,48,52,61,70,83,92,53]

s = pd.Series(values, index=dates, name= 'valoare')

s_rolling = s.rolling(window=7).mean()

df = pd.DataFrame({'valoare': s, 'media_mobila_7zile': s_rolling})
print(df)