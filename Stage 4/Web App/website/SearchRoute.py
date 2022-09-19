from re import template
import pyodbc
from . import AN_duration, AC_duration, AS_duration, AN_trainRoute, AC_trainRoute, AS_trainRoute, stations

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

#Reading all the Duration Files >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
    lstANDuration = []
    for line in AN_duration:
        lstANDuration.append ((line[:-1].split(",")))
    AN_duration.close()

    
    lstACDuration = []
    for line in AC_duration:
        lstACDuration.append ((line[:-1].split(",")))
    AC_duration.close()

    
    lstASDuration = []
    for line in AS_duration:
        lstASDuration.append ((line[:-1].split(",")))
    AS_duration.close()

    
    lstANTrainRoute = []
    for line in AN_trainRoute:
        lstANTrainRoute.append ((line[:-1].split(",")))
    AN_trainRoute.close()

    
    lstACTrainRoute = []
    for line in AC_trainRoute:
        lstACTrainRoute.append ((line[:-1].split(",")))
    AC_trainRoute.close()

    
    lstASTrainRoute = []
    for line in AS_trainRoute:
        lstASTrainRoute.append ((line[:-1].split(",")))
    AS_trainRoute.close()

    
    lstStation = []
    for line in stations:
        lstStation.append ((line[:-1].split(",")))
    stations.close()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#Finding the route that the station is situated on >>>>>>
    startLine = endLine = ""
    for line in lstStation:
        if start == line[0]:
            startLine = line[1]
        if end == line[0]:
            endLine = line[1]

#To see if the stations situates on the same route
    trainLine=""
    for i in range(len(startLine)):
        for j in range(len(endLine)):
            if startLine[i] == endLine[j]:
                trainLine = startLine[i]
    if trainLine == "":
        trainLine = startLine[0] + endLine[0]


#Find the keyword route that is applicable for same route, i.e.ANCPTCHN1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    if len(trainLine) == 1:
        tempList = [] #This stores all the possible routes
        if trainLine == "N":
            trainLine = "AreaNorth"
            for line in lstANTrainRoute:
                if start in line and end in line:
                    if line.index(start)>=0 and line.index(end)>=0 and line.index(start)<line.index(end):
                        tempList.append(line[0])
        elif trainLine == "S":
            trainLine = "AreaSouth"
            for line in lstASTrainRoute:
                if start in line and end in line:
                    if line.index(start)>=0 and line.index(end)>=0 and line.index(start)<line.index(end):
                        tempList.append(line[0])
        else:
            trainLine = "AreaCentral"
            for line in lstACTrainRoute:
                if start in line and end in line:
                    if line.index(start)>=0 and line.index(end)>=0 and line.index(start)<line.index(end):
                        tempList.append(line[0])

#Getting the duration of the route on the same route
        lstRoute = []
        if trainLine == "AreaCentral":
            for keyword in tempList:
                for lstKeyword in lstACTrainRoute:
                    if keyword == lstKeyword[0]:
                        lstRoute.append(lstKeyword[lstKeyword.index(start):lstKeyword.index(end)+1])
                        break
        elif trainLine == "AreaNorth":
            for keyword in tempList:
                for lstKeyword in lstANTrainRoute:
                    if keyword == lstKeyword[0]:
                        lstRoute.append(lstKeyword[lstKeyword.index(start):lstKeyword.index(end)+1])
                        break   
        else:
            for keyword in tempList:
                for lstKeyword in lstASTrainRoute:
                    if keyword == lstKeyword[0]:
                        lstRoute.append(lstKeyword[lstKeyword.index(start):lstKeyword.index(end)+1])
                        break                          

#Find the list of the duration
        if (len(lstRoute) > 0):
            lstDuration = []
            if trainLine == "AreaCentral":
                for route in lstRoute:
                    duration = 0
                    for i in range (len(route) - 1):
                        for j in range (len(lstACDuration)):
                            if lstACDuration[j][0] == route[i] and lstACDuration[j][1] == route[i+1]:
                                duration = duration + int(lstACDuration[j][2])
                                break
                    lstDuration.append(duration)
            if trainLine == "AreaNorth":
                for route in lstRoute:
                    duration = 0
                    for i in range (len(route) - 1):
                        for j in range (len(lstANDuration)):
                            if lstANDuration[j][0] == route[i] and lstANDuration[j][1] == route[i+1]:
                                duration = duration + int(lstANDuration[j][2])
                                break
                    lstDuration.append(duration)

            if trainLine == "AreaSouth":
                for route in lstRoute:
                    duration = 0
                    for i in range (len(route) - 1):
                        for j in range (len(lstASDuration)):
                            if lstASDuration[j][0] == route[i] and lstASDuration[j][1] == route[i+1]:
                                duration = duration + int(lstASDuration[j][2])
                                break
                    lstDuration.append(duration)

    #Reading access and return the all possible train numbers
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=./TrainSchedule.accdb;')
            cursor = conn.cursor()
            
            tempLine = ""
            for line in tempList:
                tempLine = tempLine + "OR Route = '" + line + "' "
            tempLine = tempLine[3:]  

            if day == "MTH":
                sql = "SELECT TrainNumber, TimeOfDeparture, Route FROM " + trainLine + " WHERE (WorkingTime = 'MF' OR WorkingTime = 'MTH') AND (" + tempLine + ")"
                cursor.execute(sql)
                myresult = cursor.fetchall()

            if day == "MF":
                sql = "SELECT TrainNumber, TimeOfDeparture, Route FROM " + trainLine + " WHERE (WorkingTime = 'MF') AND (" + tempLine + ")"
                cursor.execute(sql)
                myresult = cursor.fetchall()     

            if day == "SAT":
                sql = "SELECT TrainNumber, TimeOfDeparture, Route FROM " + trainLine + " WHERE (WorkingTime = 'SAT') AND (" + tempLine + ")"
                cursor.execute(sql)
                myresult = cursor.fetchall()   

            if day == "SUN":
                sql = "SELECT TrainNumber, TimeOfDeparture, Route FROM " + trainLine + " WHERE (WorkingTime = 'SUN') AND (" + tempLine + ")"
                cursor.execute(sql)
                myresult = cursor.fetchall()


            for i in range (len(myresult)):
                for j in range (len(tempList)):
                    if tempList[j] == myresult[i][2]:
                        myresult[i][2] = lstDuration[j]
                        break
            return myresult 
        #else: Same line, different route
def main():
    list = search("Kraaifontein","Worcester","Monday") 
    for line in list:
        print(line)

if __name__ == "__main__":
    main()