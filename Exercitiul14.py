import pandas as pd

df = pd.DataFrame({
    'Nume':['Vasile', 'Andreea', 'Georgel'],
    'Intrari': ['09/10/2025', '08/09/2025', '7/09/2025']
})

df['Intrari'] = pd.to_datetime(df['Intrari'], format="%d/%m/%Y")

print(df)
df["an"] = df['Intrari'].dt.year
df["luna"] = df['Intrari'].dt.month
df['zi'] = df['Intrari'].dt.day
df['zi_saptamana'] = df['Intrari'].dt.day_name()
print("--------------------------")
print(df)