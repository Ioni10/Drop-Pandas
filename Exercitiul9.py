import pandas as pd
import numpy as np
df = pd.DataFrame(
    {
        "Nume": [
            "George", "Georgeana", "Maria", "Gabriela", "Ion", "Alexia", "Stefan",
            "Mario", "Nadia", "Elena", "Florin", "Mihaela", "Claudiu", "Andreea"
        ],

        "Varsta": [28, 22, 14, 21, 24, 16, 10, 17 , 44, 47, 47, 23, 26, 36],
        "Sex": ["M", "F", "F", "F", "M", "F", "M", "M", "F", "F", "M", "F", "M", "F"],
        "Kg":[60,54,34,59,78,49,30, np.nan ,101,100,70,30,79,60]
    }
)
serie= df["Varsta"]

groupby_Kg_count= df.groupby("Kg").count()
groupby_Sex_Varsta_mean =df.groupby("Sex")["Varsta"].mean()
groupby_Varsta_Kg_max =df.groupby(["Varsta", "Kg"]).max()#Creaza cate o grupa cu fiecare varsta , daca doua nume au aceasi varsta o printeaza doar pe cea mai mare alfabetica
groupby_Sex_Kg_min =df.groupby(["Sex","Kg"]).min()#Grupa cu fiecare Sex/Kg separat si sorteaza  lexicografic ASCII/alfabetic

print("................................................................")
print("Gruparea dupa Minim de Sex Kg| cu .reset_index")
print(groupby_Sex_Kg_min.reset_index()) #In variabila noastra Sex.ul devenise index.ul (cu ajutorul .reset_index() resetam index (0-13))
print("-------------------------")
print("Gruparea dupa Minim de Sex Kg")
print(groupby_Sex_Kg_min)
print("...................................................................")
print("Gruparea dupa Maxim de Varsta Kg")
print(groupby_Varsta_Kg_max)
print("....................................................................")
print("Gruparea dupa Medie Sex Varsta")
print(groupby_Sex_Varsta_mean)
print("....................................................................")
print("Gruparea dupa Numararea numerelor non-nan din Kg ")
print(groupby_Kg_count)