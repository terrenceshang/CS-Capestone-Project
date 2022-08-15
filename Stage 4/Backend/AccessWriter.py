from turtle import tracer
import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\Stage 4\\TrainSchedule.accdb;')
file = open("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\forReading\\Area Central Combined.txt", "r")
cursor = conn.cursor()
count = 0

for line in file:
    line = line[0:-1]
    if count == 0:
        workingTimeList = line.split(",")
    if count == 1:
        departureLocationList = line.split(",")
    if count == 2:
        arrivalLocationList = line.split(",")
    if count == 3:
        timeOfDepartureList = line.split(",")
    if count == 4:
        CTPlatformNumberList = line.split(",")
    if count == 5:
        trainNumberList = line.split(",")
        for i in range (len(trainNumberList)):
            a,b,c = workingTimeList[i], departureLocationList[i], arrivalLocationList[i]
            d,e,f = timeOfDepartureList[i], CTPlatformNumberList[i], trainNumberList[i]
            sql = "INSERT INTO AreaCentral VALUES ('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"',"+f+")"
            print(sql)
            cursor.execute(sql)
            cursor.commit()

        count = 0
        continue
    count = count + 1

file.close()
cursor.close()
"""
cursor.execute('select * from AreaCentral')

for row in cursor.fetchall():
    print (row)
"""