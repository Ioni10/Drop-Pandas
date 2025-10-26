import pandas as pd

df_valori = pd.DataFrame({
    'Data': pd.to_datetime(['2025-10-01', '2025-10-02','2025-10-03']),
    'Pret': [2.50, 10, 3.50]
})




df_semnal = pd.DataFrame({
    'Data': pd.to_datetime(['2025-10-10','2025-10-11','2025-10-12']),
    'Eveniment': ['C','B','A']
})

print("DataFrame Valori:")
print(df_valori)
print("DataFrame Semnale:")
print(df_semnal)
print("--------------------------------")

df_merged = pd.merge_asof(
    df_valori.sort_values('Data'),
    df_semnal.sort_values('Data'),
    on='Data',
    direction='forward',
    tolerance=pd.Timedelta('10D')
)

print("merge_asof,backward, 1 zi toleranta :")
print(df_merged)