import pandas as pd
#Series de bază: creează un Series cu index personalizat; selectează prin etichete și poziții; describe().
varste = pd.Series( [20,24,30], index=["Ion","George", "Mihai"])
print(varste)
print("------ion--------")
print(varste["Ion"])
print("-----iongeo------")
print(varste[["Ion","George"]])
print("-----iloc------")
print(varste.iloc[1])
print(varste.iloc[[0,2]])
print("------describe-------")
print(varste.describe())