import pandas as pd
#Filtrare compusă: filtrează rânduri după condiții multiple numeric + text (str.contains, case-insensitive).
df = pd.DataFrame(
    {
        "Nume": ["Mihai", "George", "Andrei"],
        "Functie": ["Administrator", "Manager", "Team-Leader"],
        "Varsta": [30, 34, 28]
    }
)
Filtrare_Multipla = df[(df["Varsta"] >= 30) & (
    df["Functie"].str.contains("Administrator", case=False, na=False))
                       ]

print(Filtrare_Multipla)