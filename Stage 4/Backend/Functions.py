import os
from tracemalloc import start
import pyodbc
import sqlite3
#Finding the stations where student can change trains to get to a different line
"""
def getIntersectingStation (start, end):
    lstTempIntersectingStations = [["Ndabeni","CS"],["Pinelands","CS"],["Mutual","CN"],["Ysterplaat","CN"],["Esplanade","CN"],["Bellville","CN"]]
    lstIntersectingStations = []
    for intersectingStations in lstTempIntersectingStations:
        if start in intersectingStations[1] and end in intersectingStations[1]:
            lstIntersectingStations.append(intersectingStations)
    return lstIntersectingStations
"""
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

#Find the list of the duration between the start and the end.

def getDuration(lstBeginning,lstRoute,lstAreaDuration):
    lstDuration= []
    lstDurationBeginning = []
    for route in lstRoute:
        duration = 0
        for i in range (len(route) - 1):
            for j in range (len(lstAreaDuration)):
                if lstAreaDuration[j][0] == route[i] and lstAreaDuration[j][1] == route[i+1]: #To check the distance between two nodes
                    duration = duration + int(lstAreaDuration[j][2]) #adding the distance to the duration if we found node distance
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
    conn = sqlite3.connect(os.path.dirname(os.path.realpath(__file__)) + '\\database.db') #Establishing a connection
    cursor = conn.cursor()

    tempLine = ""
    for line in tempList:
        tempLine = tempLine + "OR Route = '" + line + "' "
    tempLine = tempLine[3:]  

#SQL 
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
        myresult[i] = list(myresult[i])
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

# order the routes found first by closest starting time then by duration
# checks that routes are viable (can reach connecting trains on time, 
# previous trains do not leave after following following trains)
def OrderPaths(input, time):
    if len(input) < 1: #if no available routes, return an empty string
        return [], 0
    numStops = len(input[0]) // 5
    arrDurations = []
    arrTimes = []
    count = -1
    output = []
    arrCompare = []    
    time = time[0:2] + time[3:5] 

    for routes in input: #goes through the list of routes received
        count += 1        
        hours = 0   
        minutes = 0
        bTrue = False   

        for i in range(numStops): #goes through all connecting trains
            arrDurations.append(routes[4])
            arrTimes.append(routes[3])

            if i != numStops -1:
                routes = routes[5: len(routes)]

        if numStops > 1: # if need to take more than one train
            for j in range(arrTimes.__len__()-1):            
                if hours < 0:
                    break
                
                #compares the times of the connecting trains to ensure that the first train leaves before the next
                time1 = arrTimes[j][0:len(arrTimes[j])]
                time2 = arrTimes[j+1][0:len(arrTimes[j+1])]
                arrCompare.append(int(time2[0:2]) - int(time1[0:2]))      

                #checks that previous train arrives before following train by comparing the times in hours and minutes as well as the previous train's duration
                if arrCompare[j] > -1 and ((int(arrCompare[j])*60) - (int(arrTimes[j][3:5])) + (int(arrTimes[j+1][3:5]))) >= int(arrDurations[j]):            
                    hours = hours + arrCompare[j]
                    bTrue = True
                else:
                    bTrue = False
                    break

            minutes = hours * 60

            #calculates the total duration of the trip in minutes
            if hours > -1 and bTrue == True:      
                for j in range(arrTimes.__len__()):
                    if j != arrTimes.__len__()-1 and j == 0:
                        minutes = minutes - (int(arrTimes[j][3:5]))
                    elif j == arrTimes.__len__()-1:
                        minutes += int(arrTimes[j][3:5])
                        minutes += int(arrDurations[j])

                #compares the requested start time with the time the first train in the route leaves
                startTime = arrTimes[0][0:2] + arrTimes[0][3:5]
                compare = int(time) - int(startTime) 

                if compare < 0:
                    compare = compare * -1
                
                #subtracts 40 from times earlier than the start time as there are 60 minutes in an hour, not 100
                if int(startTime[0:2]) < int(time[0:2]):
                    compare = compare - 40   
                                     
                output.append([compare,minutes,count])
        else: #if only take one train
            minutes = int(arrDurations[0])
            startTime = arrTimes[0][0:2] + arrTimes[0][3:5]
            compare = int(time) - int(startTime)

            if compare < 0:
                compare = compare * -1
                
            if int(startTime[0:2]) < int(time[0:2]):
                    compare = compare - 40

            output.append([compare,minutes,count])

        arrTimes = []
        arrDurations = []
        arrCompare = []

    output.sort()
    return(output, numStops)

# returns array of routes in a readable format
def outputPaths(input, time):
    output, numStops = OrderPaths(input, time)
    
    arrOutput = []
    #checks if there are any routes available, if not, a suitable message is returned
    if output.__len__() == 0:
        strOutput = "There are no train routes available"
        arrOutput.append(strOutput)
        return arrOutput

    #represents the information in the new ordered list of trains to a suitable output that is returned as an array
    for i in output:        
        line = input[i[2]]
        strOutput = ""

        for j in range(numStops):
            if j != 0:
                strOutput += "THEN \n"
            strOutput = strOutput + "Depart from " + line[1] + " to " + line[2] + " on train number " + line[0] + " at " + line[3] + "\n"
            line = line[5:len(line)]

        hours = str(i[1]//60) 
        minutes = str(i[1]%60)
        strOutput += "Duration: " + hours + " hour(s) and " + minutes + " minute(s)\n"
        arrOutput.append(strOutput)

    return arrOutput


