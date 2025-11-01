# dit is gemaakt voor eventueel al powerbi analyses te doen met DimOlod

import random
import pandas as pd
from sqlalchemy import create_engine, text

rows = []
for i in range(1, 1000001):
    lecture = {
        "LectureKey": random.randint(1, 1000),
        "ClassgroupKey": random.randint(1, 1000),
        "RoomKey": random.randint(1, 500),
        "OlodKey": random.randint(1, 1000),
        "StartDateKey": random.randint(20240101, 20241231),
        "StartTimeKey": random.randint(800, 1700),
        "EndDateKey": random.randint(20240101, 20241231),
        "EndTimeKey": random.randint(900, 1800),
        "UpdatedDate": random.randint(20240101, 20241231),
        "LectureStatus": random.choice(["Planned", "Completed", "Cancelled"]),
        "WorkFromCourse": random.choice(["Yes", "No"]),
        "NumberPresent": random.randint(0, 50),
        "AttendanceRate": round(random.uniform(0, 100), 2)
    }
    rows.append(lecture)

df = pd.DataFrame(rows)


engine = create_engine('mssql+pyodbc://localhost\\SQL2025/AnalyseDEPDWH?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')

with engine.begin() as conn:
    conn.execute(text("DELETE FROM FactLecture"))
    df.to_sql('FactLecture', con=conn, if_exists='append', index=False)
