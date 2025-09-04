import pandas as pd
#Sort multi-cheie:
#sortează după două coloane cu ascending diferit;
#stabilește stable sort.
df = pd.DataFrame(
    {
                    "Nume": ["Mihai" , "George","Andrei"],
                   "Functie":["Administrator", "Manager", "Team-Leader"],
                   "Varsta":[30, 34, 28]
                   }
                  )
print(df.sort_values(
    by=["Functie", "Varsta"],
    ascending=[True, False],
    ignore_index=True
    ))