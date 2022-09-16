from distutils.errors import LibError
from re import template
import pyodbc

def search (start, end, day):

    if day == "Friday":
        return searchAllRoute(start,end,"MF")
    elif day == "Saturday":
        return searchAllRoute(start,end,"SAT")
    elif day == "Sunday":
        return searchAllRoute(start,end,"SUN")
    else:
        return searchAllRoute(start,end,"MTH")

def searchAllRoute (start, end, day):

    file = open ("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\Duration\\Area North Duration.txt", "r")
    lstANDuration = []
    for line in file:
        lstANDuration.append ((line[:-1].split(",")))
    file.close()

    file = open ("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\Duration\\Area Central Duration.txt", "r")
    lstACDuration = []
    for line in file:
        lstACDuration.append ((line[:-1].split(",")))
    file.close()

    file = open ("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\Duration\\Area South Duration.txt", "r")
    lstASDuration = []
    for line in file:
        lstASDuration.append ((line[:-1].split(",")))
    file.close()

    file = open ("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\Duration\\Area North Train Route.txt", "r")
    lstANTrainRoute = []
    for line in file:
        lstANTrainRoute.append ((line[:-1].split(",")))
    file.close()

    file = open ("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\Duration\\Area Central Train Route.txt", "r")
    lstACTrainRoute = []
    for line in file:
        lstACTrainRoute.append ((line[:-1].split(",")))
    file.close()

    file = open ("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\Duration\\Area South Train Route.txt", "r")
    lstASTrainRoute = []
    for line in file:
        lstASTrainRoute.append ((line[:-1].split(",")))
    file.close()

    file = open ("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\Duration\\Station.txt", "r")
    lstStation = []
    for line in file:
        lstStation.append ((line[:-1].split(",")))
    file.close()

    startLine = endLine = ""
    for line in lstStation:
        if start == line[0]:
            startLine = line[1]
        if end == line[0]:
            endLine = line[1]
    
    for i in range(len(startLine)):
        for j in range(len(endLine)):
            if startLine[i] == endLine[j]:
                trainLine = startLine[i]

    tempList = []
    if trainLine == "N":
        trainLine = "AreaNorth"
        for line in lstANTrainRoute:
            if start in line and end in line:
                if line.index(start)>=0 and line.index(end)>=0 and line.index(start)<line.index(end):
                    tempList.append(line[0])
    if trainLine == "S":
        trainLine = "AreaSouth"
        for line in lstASTrainRoute:
            if start in line and end in line:
                if line.index(start)>=0 and line.index(end)>=0 and line.index(start)<line.index(end):
                    tempList.append(line[0])
    if trainLine == "C":
        trainLine = "AreaCentral"
        for line in lstACTrainRoute:
            if start in line and end in line:
                if line.index(start)>=0 and line.index(end)>=0 and line.index(start)<line.index(end):
                    tempList.append(line[0])

    for line in tempList:
        if trainLine == "AreaCentral":
            lst

    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\Stage 4\\TrainSchedule.accdb;')
    cursor = conn.cursor()
    
    tempLine = ""
    for line in tempList:
        tempLine = tempLine + "OR Route = '" + line + "' "
    tempLine = tempLine[3:]  

    if day == "MTH":
        sql = "SELECT TrainNumber, Route, TimeOfDeparture, CTPlatformNumber FROM " + trainLine + " WHERE (WorkingTime = 'MF' OR WorkingTime = 'MTH') AND (" + tempLine + ")"
        print(sql)
        cursor.execute(sql)
        myresult = cursor.fetchall()
    
    return myresult 


def main():
    list = search("Cape Town","Mandalay","Monday") 
    for line in list:
        print(line)
if __name__ == "__main__":
    main()