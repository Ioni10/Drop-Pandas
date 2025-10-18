import pandas as pd

dates = pd.date_range(start='2025-01-01', end='2025-01-15')
values = [1,None,3,4,5,None,None,8,9,10,None, None,13,14,15]

s = pd.Series(values, index=dates, name='valoare')
print("Seria initiala:")
print(s)
print("-------------------------------------------------------")
s = s.ffill()

print('Seria dupa forward-fill:')
print(s)
print("-------------------------------------------------------")

#Resample lunar (sum si mean)
suma_luni = s.resample('ME').sum()
medie_luni = s.resample('ME').mean()

print(f"Suma pe luna: {suma_luni}")
print(f"Media pe luna: {medie_luni}")
print("-------------------------------------------------------")
#Comparam suma si media

luna = s.resample('ME').agg(['sum', 'mean', 'count'])
luna.rename(columns={'count': 'Număr zile'}, inplace=True)
print('Rezumat lunar:')
print(luna)
