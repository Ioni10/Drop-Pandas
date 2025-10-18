#Ex17: 17) Apply pe rânduri: calculează scor total din mai multe coloane cu .apply(axis=1); compară cu vectorizare.
import pandas as pd

df = pd.DataFrame({
    'Informatica': [10, 9, 8],
    'Matematica': [10, 9, 10],
    'Engleza': [9,7,10]
})

print("DataFrame initial:")
print(df)
print("---------------------------------")
#Calculam  folosind apply pe randuri
df['total_apply'] = df.apply(lambda row: row['Informatica'] + row['Matematica'] + row['Engleza'], axis=1)

#Calculam folosind vectorizare (suma pe coloane)
df['total_vector'] = df[['Informatica','Matematica','Engleza']].sum(axis=1)

print("DataFrame:")
print(df)