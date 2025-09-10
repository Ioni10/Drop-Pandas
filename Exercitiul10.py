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
        "Kg":[60,54,34,59,78,49,30, 20 ,101,100,70,30,79,60]
    }
)



def coef_var(series):
    m = series.mean()
    s = series.std()
    return s/m if m != 0 else np.nan

coef_variatie = df.groupby("Varsta")['Kg'].agg(coef_var)

print(coef_variatie)