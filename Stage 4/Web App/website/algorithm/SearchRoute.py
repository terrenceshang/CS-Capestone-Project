# How I am approaching the search is to read all the data that I have recorded in my text file in to individual list
# Then I will find if the start and end locations are in the same area
# Then I will find if the start and end locations can be achieved in one train if they are in the same area
# Then I will find if the duration to get from the first station of the route to the start station. 
# i.e. first station time + duration between first station and start station = start time for first station
# Then I will find the duration between the start and end station
# Use SQL to find information for <Train number><start time> 
# I'll the edit the list so the list will become <Train number><start time><Duration>
# The output will the the list shown above
import math
import os
import pyodbc
import SearchRoute

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
# Reading all the Duration Files and save the details into a 2d list
# format of the 2d array [All the Routes][Details of each route]
# format of "Details of each route": [Keyword for the route, station names (each station name is its own value in list)]
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  
    file = open (os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\Area North Duration.txt", "r")
    lstANDuration = []
    for line in file:
        lstANDuration.append ((line[:-1].split(",")))
    file.close()

    file = open (os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\Area Central Duration.txt", "r")
    lstACDuration = []
    for line in file:
        lstACDuration.append ((line[:-1].split(",")))
    file.close()

    file = open (os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\Area South Duration.txt", "r")
    lstASDuration = []
    for line in file:
        lstASDuration.append ((line[:-1].split(",")))
    file.close()

    file = open (os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\Area North Train Route.txt", "r")
    lstANTrainRoute = []
    for line in file:
        lstANTrainRoute.append ((line[:-1].split(",")))
    file.close()

    file = open (os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\Area Central Train Route.txt", "r")
    lstACTrainRoute = []
    for line in file:
        lstACTrainRoute.append ((line[:-1].split(",")))
    file.close()

    file = open (os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\Area South Train Route.txt", "r")
    lstASTrainRoute = []
    for line in file:
        lstASTrainRoute.append ((line[:-1].split(",")))
    file.close()

    file = open (os.path.dirname(os.path.realpath(__file__)) + "\\Duration\\Station.txt", "r")
    lstStation = []
    for line in file:
        lstStation.append ((line[:-1].split(",")))
    file.close()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#Finding the route that the station is situated on >>>>>>
    startLine = endLine = ""
    for line in lstStation:
        if start == line[0]:
            startLine = line[1]
        if end == line[0]:
            endLine = line[1]

#To see if the stations situates on the same area
    trainline = checkSameArea(startLine,endLine)
    trainLine=""
    for i in range(len(startLine)):
        for j in range(len(endLine)):
            if startLine[i] == endLine[j]:
                trainLine = startLine[i]
    if trainLine == "":
        trainLine = startLine[0] + endLine[0]

# Find the keyword route that is applicable for same route, i.e.ANCPTCHN1 
    if len(trainLine) == 1:
        tempList = [] #This stores all the possible routes key code
        if trainLine == "N":
            trainLine = "AreaNorth"
            for line in lstANTrainRoute:
                if start in line and end in line:
                    if line.index(start)<line.index(end): #This is to check if start is before end
                        tempList.append(line[0])
        elif trainLine == "S":
            trainLine = "AreaSouth"
            for line in lstASTrainRoute:
                if start in line and end in line:
                    if line.index(start)<line.index(end):
                        tempList.append(line[0])
        else:
            trainLine = "AreaCentral"
            for line in lstACTrainRoute:
                if start in line and end in line:
                    if line.index(start)<line.index(end):
                        tempList.append(line[0])

#Getting the route from start to end
#Getting the route from Beginning of the route to start
        lstRoute = []
        lstBeginning = []
        if trainLine == "AreaCentral":
            for keyword in tempList:
                for lstKeyword in lstACTrainRoute:
                    if keyword == lstKeyword[0]:
                        lstRoute.append(lstKeyword[lstKeyword.index(start):lstKeyword.index(end)+1])
                        if lstKeyword[1] != start:
                            lstBeginning.append(lstKeyword[1:lstKeyword.index(start)+1])
                        else:
                            lstBeginning.append("")
                        break
        elif trainLine == "AreaNorth":
            for keyword in tempList:
                for lstKeyword in lstANTrainRoute:
                    if keyword == lstKeyword[0]:
                        lstRoute.append(lstKeyword[lstKeyword.index(start):lstKeyword.index(end)+1])
                        if lstKeyword[1] != start:
                            lstBeginning.append(lstKeyword[1:lstKeyword.index(start)+1])
                        else:
                            lstBeginning.append("")
                        break   
        else:
            for keyword in tempList:
                for lstKeyword in lstASTrainRoute:
                    if keyword == lstKeyword[0]:
                        lstRoute.append(lstKeyword[lstKeyword.index(start):lstKeyword.index(end)+1])
                        if lstKeyword[1] != start:
                            lstBeginning.append(lstKeyword[1:lstKeyword.index(start)+1])
                        else:
                            lstBeginning.append("")
                        break                          

#Finding if a route from start to end exist without change stations
        if (len(lstRoute) > 0):
            lstDuration = []
            lstDurationBeginning = []
#Find the list of the duration
            if trainLine == "AreaCentral":
                for route in lstRoute:
                    duration = 0
                    for i in range (len(route) - 1):
                        for j in range (len(lstACDuration)):
                            if lstACDuration[j][0] == route[i] and lstACDuration[j][1] == route[i+1]:
                                duration = duration + int(lstACDuration[j][2])
                                break
                    lstDuration.append(duration)
                for route in lstBeginning:
                    duration = 0
                    if route != "":
                        for i in range (len(route) - 1):
                            for j in range (len(lstACDuration)):
                                if lstACDuration[j][0] == route[i] and lstACDuration[j][1] == route[i+1]:
                                    duration = duration + int(lstACDuration[j][2])
                                    break
                        lstDurationBeginning.append(duration)
                    else:
                        lstDurationBeginning.append(0)

            if trainLine == "AreaNorth":
                for route in lstRoute:
                    duration = 0
                    for i in range (len(route) - 1):
                        for j in range (len(lstANDuration)):
                            if lstANDuration[j][0] == route[i] and lstANDuration[j][1] == route[i+1]:
                                duration = duration + int(lstANDuration[j][2])
                                break
                    lstDuration.append(duration)
                for route in lstBeginning:
                    duration = 0
                    if route != "":
                        for i in range (len(route) - 1):
                            for j in range (len(lstANDuration)):
                                if lstANDuration[j][0] == route[i] and lstANDuration[j][1] == route[i+1]:
                                    duration = duration + int(lstANDuration[j][2])
                                    break
                        lstDurationBeginning.append(duration)
                    else:
                        lstDurationBeginning.append(0)
            if trainLine == "AreaSouth":
                for route in lstRoute:
                    duration = 0
                    for i in range (len(route) - 1):
                        for j in range (len(lstASDuration)):
                            if lstASDuration[j][0] == route[i] and lstASDuration[j][1] == route[i+1]:
                                duration = duration + int(lstASDuration[j][2])
                                break
                    lstDuration.append(duration)
                for route in lstBeginning:
                    duration = 0
                    if route != "":
                        for i in range (len(route) - 1):
                            for j in range (len(lstASDuration)):
                                if lstASDuration[j][0] == route[i] and lstASDuration[j][1] == route[i+1]:
                                    duration = duration + int(lstASDuration[j][2])
                                    break
                        lstDurationBeginning.append(duration)
                    else:
                        lstDurationBeginning.append(0)

    #Reading access and return the all possible train numbers
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

#Changing the start time from beginning station of the route to the start location
#Changing the myresult from <Train number><Unique key><Duration> to <Train number><Start time><Duration>
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
        #else: Same line, different route
        else:
            lstANChange = ["Ysterplaat", "Mutual", "Bellville", "Kraaifontein", "Muldersvlei", "Wellington"]
            lstASChange = ["Salt River", "Retreat"]
            lstACChange = ["Phillipi", "Bontheuwel"]
            
            if trainLine == "AreaNorth":
                for i in range (len(lstANChange)):
                    lstChangeEndRoute = []
                    lstStartChangeRoute = []
                    lstDuration = []
                    for line in lstANTrainRoute:
                        if start in line and lstANChange[i] in line:
                            if line.index(start)<line.index(lstANChange[i]):
                                lstStartChangeRoute.append([line[0]])
                        if end in line and lstANChange[i] in line:
                            if line.index(lstANChange[i])<line.index(end):
                                lstChangeEndRoute.append([line[0]])
                    if (len(lstStartChangeRoute) == 0):
                        lstStartChangeRoute.append(None)
                    if (len(lstChangeEndRoute) == 0):
                        lstChangeEndRoute.append(None)
                    #if ()
                    print(lstStartChangeRoute)
                    print(lstChangeEndRoute)
            return(["fdsafdsafdas"])
    else: #Different line
        lstIntersectingStations = getIntersectingStation(startLine,endLine)
        
        return (lstIntersectingStations)

def getIntersectingStation (start, end):
    lstTempIntersectingStations = [["Cape Town","CSN"],["Woodstock","CSN"],["Salt River","CN"],["Koeberg Rd","CS"],["Maitland","CS"],["Ndabeni","CS"],["Pinelands","CS"],["Mutual","CN"],["Ysterplaat","CN"],["Esplanade","CN"],["Bellville","CN"]]
    lstIntersectingStations = []
    for intersectingStations in lstTempIntersectingStations:
        if start in intersectingStations[1] and end in intersectingStations[1]:
            lstIntersectingStations.append(intersectingStations)
    return lstIntersectingStations

def checkSameArea(start,end):
    trainLine=""
    for i in range(len(start)):
        for j in range(len(end)):
            if start[i] == end[j]:
                trainLine = start[i]
    if trainLine == "":
        trainLine = start[0] + end[0]
    return trainLine
def main():
    list = search("Brackenfell","Kraaifontein","Monday") 

    for line in list:
        print(line)

if __name__ == "__main__":
    main()