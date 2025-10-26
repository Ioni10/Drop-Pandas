import pandas as pd

data = {
    ('Temperatura', 'Ianuarie'): [10,20],
    ('Temperatura', 'Februarie'): [15,25]
}

df = pd.DataFrame(data, index=['Bucuresti', 'Berlin'])

print("Tabel original")
print(df)
print("-------------------------------------------------")

df_stack = df.stack()
print("Aplicam .stack(), 'long format'")
print(df_stack)
print("--------------------------------------------------")
print("Verificam index:")
print(df_stack.index)
print("-------------------------------------------------")
df_unstack = df_stack.unstack()
print(df_unstack)
print("------------------------------------------------")
print("Verificam index:")
print(df_unstack.index)