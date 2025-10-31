import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("../../../Data/studiefiches_unique_olodpointer.csv")
# df = pd.read_csv("C:/Users/ruben/Documents/3de jaar/DEPII/dep2-GENT01/Data/studiefiches_unique_olodpointer.csv")

# Studiefiche naam,olodpointer
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

df.to_sql('Olod', con=engine, if_exists='append', index=False)