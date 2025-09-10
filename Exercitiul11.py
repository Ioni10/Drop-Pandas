import pandas as pd

df = pd.DataFrame(
    {
        "Categorie": [
            'Piese', 'Computers', 'Video', 'Software' , 'Windows'
        ],
        'An': [
            2021, 2022, 2023, 2024 , 2025
        ],
        'Vanzari(mii)': [
            10, 12, 16, 20 ,25
        ]
    }
)

pivot = df.pivot_table(index= 'Categorie', columns='An', values= 'Vanzari(mii)', aggfunc='sum').fillna(0)
print(df)
print("....................")
print(pivot)