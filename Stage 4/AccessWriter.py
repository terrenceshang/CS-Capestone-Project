import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\Stage 4\\TrainSchedule.accdb;')
cursor = conn.cursor()

cursor.excute("INSERT INTO AreaCentral VALUES ('fdsa','fdsa','fdsa','fdsa', 1, 1)")
"""
file = open("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\forReading\\Testing.txt", "r")
count = 0
for line in file:
    if count == 0:
        workingTimeList = line.split(",")
        count = count + 1
    if count == 1:
        departureLocationList = line.split(",")
        count = count + 1
    if count == 2:
        arrivalLocationList = line.split(",")
        count = count + 1
    if count == 3:
        timeOfDepartureList = line.split(",")
        count = count + 1
    if count == 4:
        CTPlatformNumberList = line.split(",")
        count = count + 1
    if count == 5:
        trainNumberList = line.split(",")
        count = count + 1
    if count == 6:
        count == 0
        for i in range (len(workingTimeList)):
            sql = "INSERT INTO AreaCentral VALUES (%s,%s,%s,%s,%s,%s)" %(workingTimeList[i],departureLocationList[i],arrivalLocationList[i],timeOfDepartureList[i],CTPlatformNumberList[i],trainNumberList[i])
            cursor.excute(sql)
"""
conn.commit() 