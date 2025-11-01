CREATE OR ALTER PROCEDURE CheckAndUpdateDimOlod
AS
BEGIN
    SET NOCOUNT ON;

    UPDATE t 
    SET t.EndDate = GETDATE(), t.CurrentFlag = 0
    FROM DEP_Wifi.dbo.DimOlod t
    INNER JOIN DEP_ODS.dbo.Olod s ON t.SubjectCode = s.SubjectCode
    WHERE t.CurrentFlag = 1 AND (t.Course <> s.Opleiding OR t.Subject <> s.CourseName OR t.Credits <> s.Credits OR t.Language <> s.Language OR t.Calender <> s.CalendarPeriod);

    INSERT INTO DEP_Wifi.dbo.DimOlod (SubjectCode, Course, Subject, Credits, Language, Calender, StartDate, EndDate, CurrentFlag)
    SELECT s.SubjectCode, s.Opleiding, s.CourseName, s.Credits, s.Language, s.CalendarPeriod, GETDATE(), NULL, 1
    FROM DEP_ODS.dbo.Olod s
    LEFT JOIN DEP_Wifi.dbo.DimOlod t ON t.SubjectCode = s.SubjectCode AND t.CurrentFlag = 1
    WHERE  t.SubjectCode IS NULL OR t.Course <> s.Opleiding OR t.Subject <> s.CourseName OR t.Credits <> s.Credits OR t.Language <> s.Language OR t.Calender <> s.CalendarPeriod;
END;