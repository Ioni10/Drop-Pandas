import pandas as pd

df = pd.DataFrame({
    'Oras': ['Mioveni', 'Costesti', 'Pitesti'],
    'Iunie':[27,29,25],
    'Iulie':[29,30,36],
    'August':[36,37,33]
})

print('DataFrame Original (basic:wide)')
print(df)
print("---------------------------------------")
df_long = pd.melt(df, id_vars=['Oras'], var_name='Luna', value_name='Temperatura')
print("Dupa .melt() (long)")
print(df_long)
print("----------------------------------------")
df_wide = df_long.pivot(index='Oras', columns='Luna', values='Temperatura')
print("Pivot: ")
print(df_wide)