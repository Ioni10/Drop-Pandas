#20) Schemă simplă: definește dict col→(dtype, nullable) și validează DataFrame-ul; raportează abateri.
import pandas as pd

df = pd.DataFrame({
    'nume': ['Ana', 'Ion', 'Maria', 'Alex'],
    'varsta': [25,30,22,28],
    'oras': ['Bucuresti', 'Cluj', None, 'Bucuresti']

})

#Schema definita simpla:
schema_dtypes = {
    'nume': 'object',
    'varsta': 'int64',
    'oras': 'object'
}

schema_nullable = {
    'nume': False,
    'varsta': False,
    'oras': True
}

tipuri_ok = df.dtypes.equals(pd.Series(schema_dtypes))

#Verificam valorile nule pentru coloanele non-nullable

nullable_ok = df[list(k for k , v in schema_nullable.items() if not v)].notna().all().all()


if tipuri_ok and nullable_ok:
    print("DataFrame.ul respecta schema")
else:
    print("DataFrame.ul Nu respecta schema")