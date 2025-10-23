CREATE DATABASE DEP_Wifi;

ALTER DATABASE DEP_Wifi
SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
DROP DATABASE DEP_Wifi;

USE DEP_Wifi;
USE test

CREATE TABLE DimDate (
    DateKey INT PRIMARY KEY,
    FullDate DATE,
    Year INT,
    Month INT,
    Day INT,
    Semester INT,
    Quarter INT,
    DayOfWeek VARCHAR(50),
);

CREATE TABLE DimTime (
    TimeKey INT PRIMARY KEY,
    FullTime TIME,
    Hour INT,
    Minutes INT
);

CREATE TABLE DimRoom (
    RoomKey INT PRIMARY KEY,
    FullRoom VARCHAR(50),
    Code VARCHAR(50), -- dit doen we erbij voor DimSchedule ---> rooms
    RoomFloor INT,
    Room INT,
    Category VARCHAR(50),
    SurfaceArea  DECIMAL(10,2),
    Capacity INT
);

CREATE TABLE DimClassgroup (
    ClassgroupKey INT PRIMARY KEY,
    SubgroupID INT,
    SubgroupCode VARCHAR(50),
    DeelgroepID INT,
    StudentCount INT,
);

CREATE TABLE DimOlod (
    OlodKey INT PRIMARY KEY,
    Course VARCHAR(50),
    Subject VARCHAR(50),
    URL VARCHAR(100),
    Credits VARCHAR(50),
    Language VARCHAR(50),
    Calender VARCHAR(50),
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
    LectureStatus VARCHAR(50),
    WorkFromCourse VARCHAR(50),
    IsPerson BIT, -- kan een lokaal reserveren
    IsStudents BIT, -- kan een lokaal reserveren
    IsTeacher BIT,
    AttendanceRate DECIMAL(5,2),

    FOREIGN KEY (StartDateKey) REFERENCES DimDate(DateKey),
    FOREIGN KEY (StartTimeKey) REFERENCES DimTime(TimeKey),
    FOREIGN KEY (EndDateKey) REFERENCES DimDate(DateKey),
    FOREIGN KEY (EndTimeKey) REFERENCES DimTime(TimeKey),
    FOREIGN KEY (ClassgroupKey) REFERENCES DimClassgroup(ClassgroupKey),
    FOREIGN KEY (RoomKey) REFERENCES DimRoom(RoomKey),
    FOREIGN KEY (OlodKey) REFERENCES DimOlod(OlodKey)
);