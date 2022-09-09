from turtle import tracer
import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\Stage 4\\TrainSchedule.accdb;')
file = open("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\ANBELWLT1.txt", "r")
cursor = conn.cursor()
count = 0


for line in file:
    key = line[0:2]
    line = line[3:-1]
    list = line.split(",")

    if (key == "SU"):
        key = "SUN"
    elif (key == "SA"):
        key = "SAT"
    print(key)
    print(line)    


    for i in range (len(list)):
        sql = "Update AreaNorth SET BelOtherRoute = 'ANBELWLT1' WHERE TrainNumber = " + list[i] + " AND WorkingTime = '" + key +"'"
        print(sql)
        cursor.execute(sql)
        cursor.commit()



#sql = "Update AreaNorth SET CTOtherRoute = '' WHERE DepartureLocation = 'Retreat' AND ArrivalLocation = 'Cape Town'"



"""
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
        BVPlatformNumberList = line.split(",")
    if count == 6:
        trainNumberList = line.split(",")
        for i in range (len(trainNumberList)):
            a = workingTimeList[i]
            b = departureLocationList[i]
            c = arrivalLocationList[i]
            d = timeOfDepartureList[i]
            e = CTPlatformNumberList[i]
            f = BVPlatformNumberList[i]
            g = trainNumberList[i]
            sql = "INSERT INTO AreaNorth VALUES ('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"','"+g+"')"
            print(sql)
            cursor.execute(sql)
            cursor.commit()

        count = 0
        continue
    count = count + 1
"""



file.close()
cursor.close()

"""
cursor.execute('select * from AreaCentral')

for row in cursor.fetchall():
    print (row)
"""