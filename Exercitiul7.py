import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "Nume": [
            "Marian", "George", "Maria", "Gabriela", "Ion", "Alexia", "Stefan",
            "Mario", "Nadia", "Elena", "Florin", "Mihaela", "Claudiu", "Cristi"
        ],

        "Varsta": [np.nan, 21, np.nan, np.nan, 24, 16, 10, 17 , 44, 47, 47, 23, 26, np.nan],
        "Sex": ["M", "M", "F", "F", "M", "F", "M", "M", "F", "F", "M", "F", "M", "M"],
    }
)
#np.nan - comanda care introduce o Non-valoare in Series.ul nostru 'Varsta'

df['Varsta'] = df['Varsta'].fillna(0) #fillna() comanda speciala care inlocuieste valorile NaN cu ce valoare dorim
print(df)