import pandas as pd
from sqlalchemy import create_engine
import datetime

# Database configuratie
engine = create_engine('mssql+pyodbc://localhost\\SQL2025/DEP_Wifi?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')

# 📌 **DimTime genereren (00:00 tot 23:59)**
time_range = [datetime.time(h, m) for h in range(24) for m in range(60)]

dim_time = pd.DataFrame({
    'TimeKey': [int(f"{t.hour:02d}{t.minute:02d}") for t in time_range],
    'Hour': [t.hour for t in time_range],
    'Minutes': [t.minute for t in time_range],
    'FullTime': [t.strftime('%H:%M') for t in time_range],
})

# Data naar database schrijven
dim_time.to_sql('DimTime', con=engine, if_exists='append', index=False)