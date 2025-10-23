import pandas as pd

df = pd.read_csv(r"Data\filtered_lokalen.csv")

pd.set_option('display.max_columns', None)

df = df[df["TimeEdit"] != 0]

print(df.head(10))
print("")
print("")

print(df.tail(10))
print("")
print("")

# Duplicaten
duplicates = df[df.duplicated(keep=False)]
print(duplicates)
print("")
print("")

# Controleer of PK_fmis_lokalen uniek is
is_unique = df["PK_fmis_lokalen"].is_unique
print("Alle PK_fmis_lokalen zijn uniek: ", is_unique)
print("")
print("")

# juiste formaat
# regex: 2 cijfers . 2 cijfers . 3 cijfers . 3 cijfers
pattern = r'^\d{2}\.\d{2}\.\d{3}\.\d{3}$'
df["formaat_ok"] = df["Code"].astype(str).str.match(pattern)
print(df[df["formaat_ok"] == False])
print("")
print("")

# ongeldige waarden
print("Controle Capaciteit:")
print(df[df["Capaciteit"] <= 0])
print("")
print("")

print("Controle Oppervlakte:")
print(df[df["Oppervlakte"] <= 0])
print("")
print("")

print("Controle rooms:")
print(df[df["Lokaal"] >= 100])
print("")
print("")

print("Controle floor:")
print(df[df["Verdieping"] >= 150])
print(df[df["Verdieping"] < 100])
print("")
print("")

# controle op ongeldige campussen
allemaal_ok = df["Site-beschrijving"].str.contains("Campus Schoonmeersen").all()
print("Alle rijen bevatten 'Campus Schoonmeersen':", allemaal_ok)
print("")
print("")

# juiste formaat
pattern = r'^\d{2}\.\d{2} - GSCHB'
df["formaat_ok"] = df["Gebouw-beschrijving"].astype(str).str.match(pattern)
print(df[df["formaat_ok"] == False])
print("")
print("")

# lokaalid = lokaal
allemaal_gelijk = (df["Lokaal"] == df["Lokaal-ID"]).all()
print("Alle Lokaal-ID's zijn gelijk aan Lokaal:", allemaal_gelijk)
print("")
print("")

# Regex: GSCHB. + verdieping (mag negatief) + . + 3 cijfers + optioneel een letter
pattern = r"^GSCHB\.-?\d\.\d{3}[a-zA-Z]?$"
df["code2_ok"] = df["Code2"].isna() | df["Code2"].str.match(pattern, na=False)
allemaal_ok = df["code2_ok"].all()
print("Alle Code2-waarden hebben het juiste formaat:", allemaal_ok)
print("")
print("")

df["van_kleiner_dan_tot"] = df["Tot"].isna() | (df["Van"] < df["Tot"])
allemaal_ok = df["van_kleiner_dan_tot"].all()
print("Alle rijen hebben Van < Tot (of lege Tot toegestaan):", allemaal_ok)
print("")
print("")

df = df.drop(columns=['formaat_ok', 'code2_ok', 'van_kleiner_dan_tot'])

print(df.dtypes)