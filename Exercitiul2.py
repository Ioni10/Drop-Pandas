import pandas as pd
#DataFrame din dict: construiește DF din dict de liste; reordonează coloane; adaugă coloană derivată.
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
print(df)
print("---------------------")
df = df[["Varsta", "Sex", "Nume"]]
print(df)
df["Kg"] = [55, 60, 48, 49, 74, 53, 32, 102, 53, 50, 110, 49, 64, 60]
print("---------------------")
print(df)