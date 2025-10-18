#19) Export CSV/Parquet: salvează fără index CSV; salvează Parquet (dacă pyarrow/fastparquet); compară dimensiuni.
import pandas as pd

df = pd.DataFrame({
    'nume': ['Ana', 'Ion', 'Maria', 'Alex'],
    'varsta': [25, 30, 22, 28],
    'oras': ['Bucuresti', 'Cluj', 'Timisoara', 'Bucuresti']
})
#Exportam csv.ul fara index
df.to_csv('ex19.csv', index=False)

#Exportam Parquet (pyarrow sau fastparquet)
df.to_parquet('ex19.parquet', engine='pyarrow', index=False)

