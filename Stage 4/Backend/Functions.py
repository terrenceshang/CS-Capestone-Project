import os
import pyodbc
#Finding the stations where student can change trains to get to a different line
def getIntersectingStation (start, end):
    lstTempIntersectingStations = [["Cape Town","CSN"],["Woodstock","CSN"],["Salt River","CN"],["Koeberg Rd","CS"],["Maitland","CS"],["Ndabeni","CS"],["Pinelands","CS"],["Mutual","CN"],["Ysterplaat","CN"],["Esplanade","CN"],["Bellville","CN"]]
    lstIntersectingStations = []
    for intersectingStations in lstTempIntersectingStations:
        if start in intersectingStations[1] and end in intersectingStations[1]:
            lstIntersectingStations.append(intersectingStations)
    return lstIntersectingStations

#To see if the stations situates on the same area
def checkSameArea(start,end):
    trainLine=""
    for i in range(len(start)):
        for j in range(len(end)):
            if start[i] == end[j]:
                trainLine = start[i]
    if trainLine == "":
        trainLine = start[0] + end[0]
    return trainLine

# Reading all the Duration Files and save the details into a 2d list
# format of the 2d array [All the Routes][Details of each route]
# format of "Details of each route": [Keyword for the route, station names (each station name is its own value in list)]
def fileToLst(txtName):
    file = open (os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\" + txtName, "r")
    lstDuration = []
    for line in file:
        lstDuration.append ((line[:-1].split(",")))
    file.close()
    return lstDuration

# Find the keyword route that is applicable for same route, i.e.ANCPTCHN1 
def getKeyword(start,end,route):
    tempList=[]
    for line in route:
            if start in line and end in line:
                if line.index(start)<line.index(end): #This is to check if start is before end
                    tempList.append(line[0])
    return tempList

#Getting the route from start to end
#Getting the route from Beginning of the route to start
def getRoute(start,end,tempList,trainRoute):
    lstRoute = []
    lstBeginning = []
    for keyword in tempList:
        for lstKeyword in trainRoute:
            if keyword == lstKeyword[0]:
                lstRoute.append(lstKeyword[lstKeyword.index(start):lstKeyword.index(end)+1])
                if lstKeyword[1] != start:
                    lstBeginning.append(lstKeyword[1:lstKeyword.index(start)+1])
                else:
                    lstBeginning.append("")
                break    
    return [lstBeginning,lstRoute]

#Find the list of the duration
def getDuration(lstBeginning,lstRoute,lstAreaDuration):
    lstDuration= []
    lstDurationBeginning = []
    for route in lstRoute:
        duration = 0
        for i in range (len(route) - 1):
            for j in range (len(lstAreaDuration)):
                if lstAreaDuration[j][0] == route[i] and lstAreaDuration[j][1] == route[i+1]:
                    duration = duration + int(lstAreaDuration[j][2])
                    break
        lstDuration.append(duration)
    for route in lstBeginning:
        duration = 0
        if route != "":
            for i in range (len(route) - 1):
                for j in range (len(lstAreaDuration)):
                    if lstAreaDuration[j][0] == route[i] and lstAreaDuration[j][1] == route[i+1]:
                        duration = duration + int(lstAreaDuration[j][2])
                        break
            lstDurationBeginning.append(duration)
        else:
            lstDurationBeginning.append(0)
    return [lstDurationBeginning,lstDuration]

#Reading access and return the all possible train numbers
def getMyresult(day,tempList,trainLine):
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + os.path.dirname(os.path.realpath(__file__))[:-8] + '\\TrainSchedule.accdb;')
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
    return myresult

#Changing the start time from beginning station of the route to the start location
#Changing the myresult from <Train number><Unique key><Duration> to <Train number><Start time><Duration>
def updateMyresult(myresult,tempList,lstDuration,lstDurationBeginning):
    for i in range (len(myresult)):
        for j in range (len(tempList)):
            if tempList[j] == myresult[i][2]:
                myresult[i][2] = lstDuration[j]
                temp = myresult[i][1]
                minute = str ((int(temp[3:]) + lstDurationBeginning[j]))
                hour = str (int(temp[0:2]) + int(minute)//60)
                minute = str(int(minute) % 60)
                if len(minute) == 1:
                    minute = "0" + minute
                if len(hour) == 1:
                    hour = "0" + hour
                myresult[i][1] = hour + ":" + minute
                break
    return myresult
