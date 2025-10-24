import pandas as pd
from sqlalchemy import create_engine
import datetime

# Database configuratie
engine = create_engine('mssql+pyodbc://localhost\\SQL2025/DEP_Wifi?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')

# 📌 **DimDate genereren (2010-01-01 tot 2025-12-31)**
start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2026, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date)

dim_date = pd.DataFrame({
    'DateKey': date_range.strftime('%Y%m%d').astype(int),
    'FullDate': date_range.date,
    'Year': date_range.year,
    'Month': date_range.month,
    'Day': date_range.day,
    'Semester': ((date_range.month - 1) // 6 + 1),
    'Quarter': date_range.to_series().dt.quarter,
    'DayOfWeek': date_range.strftime('%A')
})

# 📌 **Data naar SQL Server wegschrijven**
dim_date.to_sql('DimDate', con=engine,if_exists='append', index=False)