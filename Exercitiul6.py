import pandas as pd

df = pd.DataFrame(
    {
        "Nume": [
            "Marian", "George", "Maria", "Gabriela", "Ion", "Alexia", "Stefan",
            "Mario", "Nadia", "Elena", "Florin", "Mihaela", "Claudiu", "Cristi"
        ],

        "Varsta": [22, 21, 14, 21, 24, 16, 10, 17, 44, 47, 47, 23, 26, 36],
        "Sex": ["M", "M", "F", "F", "M", "F", "M", "M", "F", "F", "M", "F", "M", "M"],
    }
)
df2 = df.set_index("Nume")
print(".........")
print(df2.loc['Florin'])
print("...........")
print(df2.iloc[10])
print("...............")
#Explicatie df2(este un Series in care se afla indexul din dataframe 'Nume')
#loc - cauta indexul dupa un key str
#iar iloc dupa index numeric ca la listele din python


df2 = df.copy() #Am creaet o copie a DataFrame.ului

df.loc[4, 'Varsta'] = 99#Am modificat DataFrame.ul principal
print(df)
print("-----------------------")
print(df2)
#vedem diferenta dintre copia DataFrame.ului si Modificarea