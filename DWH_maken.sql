CREATE DATABASE DEP_Wifi;

USE DEP_Wifi;

CREATE TABLE DimDate (
    DateKey INT PRIMARY KEY,
    FullDate DATE,
    Year INT,
    Month INT,
    Day INT,
    Semester INT,
    Quarter INT,
    DayOfWeek VARCHAR(50),
    SchoolWeek  INT
);

CREATE TABLE DimTime (
    TimeKey INT PRIMARY KEY,
    FullTime TIME,
    Hour INT,
    Minutes INT
);

CREATE TABLE DimRoom (
    RoomKey INT IDENTITY(1,1) PRIMARY KEY,
    FullRoom VARCHAR(100),
    Code VARCHAR(100), -- dit doen we erbij voor DimSchedule ---> rooms
    RoomFloor INT,
    Room INT,
    Category VARCHAR(100),
    SurfaceArea  DECIMAL(10,2),
    Capacity INT
);

CREATE TABLE DimClassgroup (
    ClassgroupKey INT IDENTITY(1,1) PRIMARY KEY,
    SubgroupID INT,
    SubgroupCode VARCHAR(100),
    DeelgroepID INT,
    StudentCount INT,
);

CREATE TABLE DimOlod (
    OlodKey INT IDENTITY(1,1) PRIMARY KEY,
    SubjectCode INT,
    Course VARCHAR(200),
    Subject VARCHAR(255),
    Credits INT,
    Language VARCHAR(100),
    Calender VARCHAR(100),
    StartDate DATE, -- datum
    EndDate DATE, -- datum
    CurrentFlag bit,
);

CREATE TABLE FactLecture (
    LectureKey INT PRIMARY KEY,
    ClassgroupKey INT,
    RoomKey INT,
    OlodKey INT,
    StartDateKey INT,
    StartTimeKey INT,
    EndDateKey INT,
    EndTimeKey INT,
    UpdatedDate INT,
    LectureStatus VARCHAR(100),
    WorkFromCourse VARCHAR(100),
    NumberPresent INT,
    AttendanceRate DECIMAL(5,2),

    FOREIGN KEY (StartDateKey) REFERENCES DimDate(DateKey),
    FOREIGN KEY (StartTimeKey) REFERENCES DimTime(TimeKey),
    FOREIGN KEY (EndDateKey) REFERENCES DimDate(DateKey),
    FOREIGN KEY (EndTimeKey) REFERENCES DimTime(TimeKey),
    FOREIGN KEY (ClassgroupKey) REFERENCES DimClassgroup(ClassgroupKey),
    FOREIGN KEY (RoomKey) REFERENCES DimRoom(RoomKey),
    FOREIGN KEY (OlodKey) REFERENCES DimOlod(OlodKey)
);