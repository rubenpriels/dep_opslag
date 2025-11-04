import pandas as pd

df = pd.read_csv(r"Data\filtered_lokalen.csv")

# floor omzetten naar nummer verdieping
floor_map = {
    100: 0,
    110: 1,
    120: 2,
    130: 3,
    140: 4,
    150: 5,
    160: 6,
    90: -1
}

df["Verdieping"] = df["Verdieping"].map(floor_map).astype(int)

# Zet Capacity om van float naar int
df["Capaciteit"] = df["Capaciteit"].astype("Int64")

df['Lokaal-Beschrijving'] = df['Lokaal-Beschrijving'].str.split().str[0]

# Zet df om naar csv
df.to_csv("Data/lokalendata_opgeschoond.csv", index=False)
