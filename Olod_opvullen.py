import pandas as pd
from sqlalchemy import create_engine, text

df = pd.read_csv("../../../Data/studiefiches_unique_olodpointer.csv")
# df = pd.read_csv("C:/Users/ruben/Documents/3de jaar/DEPII/dep2-GENT01/Data/studiefiches_unique_olodpointer.csv")

df = df.rename(columns={
    "Opleiding": "Opleiding",
    "Studiefiche naam" : "CourseName",
    "olodpointer" : "SubjectCode",
    "Studiepunten": "Credits",
    "Onderwijstalen": "Language",
    "Kalender" : "CalendarPeriod",
    "URL" : "URL"
})

engine = create_engine('mssql+pyodbc://localhost\\SQL2025/DEP_ODS?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')

# df.to_sql('Olod', con=engine, if_exists='replace', index=False)

with engine.begin() as conn:
    conn.execute(text("DBCC CHECKIDENT ('Olod', RESEED, 0)"))  # reset identity naar 1 (voor gemak)
    conn.execute(text("DELETE FROM Olod"))
    df.to_sql('Olod', con=conn, if_exists='append', index=False)

# GEDACHTEPROCES:
# jaar 1  -> olod data opgehaald en in csv1 gestoken
#         -> dit vult ods op
#         -> dit zet je allemaal in DWH (eerste keer geen historieke data)

# jaar 2  -> olod data wordt opnieuw opgehaald en overschrijft alle data in CSV1 (*1* aangezien dit toch niet nuttig is en alle historieke data wordt ook opgeslagen in de DWH dus er zijn niet echt gegevens verloren)
#         -> hij steekt deze data in ODS -> ODS wordt alle data overschreven (zie *1*)
#         -> met data in DWH te steken checkt hij
#             -> olodpointer hetzelfde, maar geen veranderingen -> niks gebeurd
#             -> olodpointer hetzelfde en veranderingen -> oude record wordt currentflag = 0 en enddate = vandaag + nieuwe record wordt toegevoegd
#             -> olodpointer die met geen record overeenkomen -> toevoegen

# jaar x -> zelfde als jaar 2