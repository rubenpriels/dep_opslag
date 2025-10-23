import pandas as pd

df = pd.read_csv(r"Data\filtered_lokalen.csv")

# Rijen verwijderen waar TimeEdit = 0 is
df = df[df["TimeEdit"] != 0]

# kollomen verwijderen dat niet in de DWH moeten
df = df.drop(columns=['PK_fmis_lokalen', 'Lokaal-ID', 'Lokaal-Beschrijving', 'Campus', 'Gebouw', 'Site-beschrijving', 'Gebouw-beschrijving', 'Verdieping-beschrijving', 'Locatie-ID', 'TimeEdit', 'Van', 'Tot'])

# Hernoem de kolommen om zo in DWH te steken
df.rename(columns={
    'Code2': 'FullRoom',
    'Code': 'Code',
    'Verdieping': 'RoomFloor',
    'Lokaal': 'Room',
    'Categorie': 'Category',
    'Oppervlakte': 'SurfaceArea',
    'Capaciteit': 'Capacity',
}, inplace=True)

# floor omzetten naar nummer verdieping
floor_map = {
    100: 0,
    110: 1,
    120: 2,
    130: 3,
    140: 4,
    90: -1
}

df["RoomFloor"] = df["RoomFloor"].map(floor_map).astype(int)

# # Enkel GSCHB0.001 overhouden
# df["FullRoom"] = df["FullRoom"].str.extract(r"(GSCHB\.-?\d+\.\d+)") # dit behouden in geval antwoord op vraag

# Zet Capacity om van float naar int
df["Capacity"] = df["Capacity"].astype("Int64")

# Zet df om naar csv
df.to_csv("Data/lokalendata_opgeschoond.csv", index=False)