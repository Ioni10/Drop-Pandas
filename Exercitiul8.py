import pandas as pd

df = pd.DataFrame(
    {
        "Nume": [
            "George", "George", "Maria", "Gabriela", "Ion", "Alexia", "Stefan",
            "Mario", "Nadia", "Elena", "Florin", "Mihaela", "Claudiu", "George"
        ],

        "Varsta": [22, 21, 14, 21, 24, 16, 10, 17 , 44, 47, 47, 23, 26, 36],
        "Sex": ["M", "M", "F", "F", "M", "F", "M", "M", "F", "F", "M", "F", "M", "M"],
    }
)
print("Primu DataFrame, Originalul:")
print(df)
print("......................................................")
print("Al 2-lea DataFrame, fara duplicate in coloana 'Nume':")
print(df.drop_duplicates(subset="Nume"))
print(".....................................................")
print("Al 3-lea DataFrame, fara duplicate in coloana 'Varsta':Am pastrat Ultimul(Keep)")
print(df.drop_duplicates(subset="Varsta", keep="last"))