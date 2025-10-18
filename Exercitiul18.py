#18) Categoriale: convertește o coloană frecvent repetată la 'category'; compară memory_usage înainte/după.
import pandas as pd

df = pd.DataFrame({
    'oras': ['Bucuresti', 'Cluj', 'Timisoara', 'Bucuresti', 'Cluj', 'Bucuresti', 'Timisoara', 'Cluj', 'Bucuresti', 'Timisoara']
})

print("Memory usage inainte de conversie:")
print(df.memory_usage(deep=True))
print("---------------------------------------")

#Connvertim coloana la 'category'
df['oras'] = df['oras'].astype('category')

#Dupa conversie:
print("Memory usage dupa conversie:")
print(df.memory_usage(deep=True))

#Verificam tipul coloanei:
print("Tipul coloanei oras dupa conversie:")
print(df.dtypes)