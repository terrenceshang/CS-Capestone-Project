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
import Functions as FCT
import Dijkstra as dk

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

#Getting all the text files in to their list
    lstANDuration = FCT.fileToLst("Area North Duration.txt")
    lstACDuration = FCT.fileToLst("Area Central Duration.txt")
    lstASDuration = FCT.fileToLst("Area South Duration.txt")
    lstANTrainRoute = FCT.fileToLst("Area North Train Route.txt")
    lstACTrainRoute = FCT.fileToLst("Area Central Train Route.txt")
    lstASTrainRoute = FCT.fileToLst("Area South Train Route.txt")
    lstStation = FCT.fileToLst("Station.txt")

#Finding the route that the station is situated on >>>>>>
    startLine = endLine = ""
    for line in lstStation:
        if start == line[0]:
            startLine = line[1]
        if end == line[0]:
            endLine = line[1]

#Checking if the trains are in the same area
    trainLine=FCT.checkSameArea(startLine,endLine)
    

# Find the keyword route that is applicable for same route, i.e.ANCPTCHN1 
    if len(trainLine) == 1:
        tempList = [] #This stores all the possible routes key code
        if trainLine == "N":
            trainLine = "AreaNorth"
            tempList = FCT.getKeyword(start,end,lstANTrainRoute)
        elif trainLine == "S":
            trainLine = "AreaSouth"
            tempList = FCT.getKeyword(start,end,lstASTrainRoute)
        else:
            trainLine = "AreaCentral"
            tempList = FCT.getKeyword(start,end,lstACTrainRoute)

#Getting the route from start to end
#Getting the route from Beginning of the route to start

        if trainLine == "AreaCentral":
            temp = FCT.getRoute(start,end,tempList,lstACTrainRoute)
            lstBeginning = temp[0]
            lstRoute = temp[1]

        elif trainLine == "AreaNorth":
            temp = FCT.getRoute(start,end,tempList,lstANTrainRoute)
            lstBeginning = temp[0]
            lstRoute = temp[1]
        else:
            temp = FCT.getRoute(start,end,tempList,lstASTrainRoute)
            lstBeginning = temp[0]
            lstRoute = temp[1]                          

        if (len(lstRoute) > 0): #Finding if a route from start to end exist without change train
            lstDuration = None
            lstDurationBeginning = None

#Find the list of the duration
            if trainLine == "AreaCentral":
                temp = FCT.getDuration(lstBeginning,lstRoute,lstACDuration)
                lstDuration = temp[1]
                lstDurationBeginning = temp[0]

            if trainLine == "AreaNorth":
                temp = FCT.getDuration(lstBeginning,lstRoute,lstANDuration)
                lstDuration = temp[1]
                lstDurationBeginning = temp[0]

            if trainLine == "AreaSouth":
                temp = FCT.getDuration(lstBeginning,lstRoute,lstASDuration)
                lstDuration = temp[1]
                lstDurationBeginning = temp[0]

#Reading access and return the all possible train numbers
            myresult = FCT.getMyresult(day,tempList,trainLine)

#Changing the start time from beginning station of the route to the start location
#Changing the myresult from <Train number><Unique key><Duration> to <Train number><Start time><Duration>

            myresult = FCT.updateMyresult(myresult,tempList,lstDuration,lstDurationBeginning)
            return myresult 
        
        else: #Same eline, 2 trains
            fastestRoute = dk.findRoute(start,end)
            changeStation = ""
            
            if (trainLine == "AreaNorth"):
                for i in range (1, len(fastestRoute)):
                    if len(FCT.getKeyword(start,fastestRoute[i],lstANTrainRoute)) == 0:
                        changeStation = fastestRoute[i-1]
                        break
                lstStartChangeKeyword = FCT.getKeyword(start, changeStation, lstANTrainRoute)
                temp = FCT.getRoute(start, changeStation, lstStartChangeKeyword, lstANTrainRoute)
                lstStartChangeBeginningRoute = temp[0]
                lstStartChangeRoute = temp[1]
                temp = FCT.getDuration(lstStartChangeBeginningRoute,lstStartChangeRoute,lstANDuration)
                lstStartChangeDuration = temp[0]
                lstStartChangeBeginningDuration = temp[1]
                myresult1 = FCT.getMyresult(day,lstStartChangeKeyword,trainLine)
                myresult1 = FCT.updateMyresult(myresult1,lstStartChangeKeyword,lstStartChangeBeginningDuration,lstStartChangeDuration)
                
                lstChangeEndKeyword = FCT.getKeyword(changeStation, end, lstANTrainRoute)
                temp = FCT.getRoute(changeStation, end, lstChangeEndKeyword, lstANTrainRoute)
                lstChangeEndBeginningRoute = temp[0]
                lstChangeEndRoute = temp[1]
                temp = FCT.getDuration(lstChangeEndBeginningRoute,lstChangeEndRoute,lstANDuration)
                lstChangeEndDuration = temp[0]
                lstChangeEndBeginningDuration = temp[1]
                myresult2 = FCT.getMyresult(day,lstChangeEndKeyword,trainLine)
                myresult2 = FCT.updateMyresult(myresult2,lstChangeEndKeyword,lstChangeEndBeginningDuration,lstChangeEndDuration)
                
                output = []
                for i in range (len(myresult1)):
                    num1 = int(myresult1[i][1][0:2]) * 60 + int(myresult1[i][1][3:5]) + int(myresult1[0][2])
                    for j in range (len(myresult2)):
                        num2 = int(myresult2[j][1][0:2]) * 60 + int(myresult2[j][1][3:5])
                        if (num2 - num1 <= 30 and num2 - num1 >=15):
                            output.append([myresult1[i][0],start,changeStation,myresult1[i][1],myresult1[i][2],myresult2[j][0],changeStation,end,myresult2[j][1],myresult2[j][2] ])
                return output
            
            if (trainLine == "AreaSouth"):
                for i in range (1, len(fastestRoute)):
                    if len(FCT.getKeyword(start,fastestRoute[i],lstASTrainRoute)) == 0:
                        changeStation = fastestRoute[i-1]
                        break
                lstStartChangeKeyword = FCT.getKeyword(start, changeStation, lstASTrainRoute)
                temp = FCT.getRoute(start, changeStation, lstStartChangeKeyword, lstASTrainRoute)
                lstStartChangeBeginningRoute = temp[0]
                lstStartChangeRoute = temp[1]
                temp = FCT.getDuration(lstStartChangeBeginningRoute,lstStartChangeRoute,lstASDuration)
                lstStartChangeDuration = temp[0]
                lstStartChangeBeginningDuration = temp[1]
                myresult1 = FCT.getMyresult(day,lstStartChangeKeyword,trainLine)
                myresult1 = FCT.updateMyresult(myresult1,lstStartChangeKeyword,lstStartChangeBeginningDuration,lstStartChangeDuration)
                
                lstChangeEndKeyword = FCT.getKeyword(changeStation, end, lstASTrainRoute)
                temp = FCT.getRoute(changeStation, end, lstChangeEndKeyword, lstASTrainRoute)
                lstChangeEndBeginningRoute = temp[0]
                lstChangeEndRoute = temp[1]
                temp = FCT.getDuration(lstChangeEndBeginningRoute,lstChangeEndRoute,lstASDuration)
                lstChangeEndDuration = temp[0]
                lstChangeEndBeginningDuration = temp[1]
                myresult2 = FCT.getMyresult(day,lstChangeEndKeyword,trainLine)
                myresult2 = FCT.updateMyresult(myresult2,lstChangeEndKeyword,lstChangeEndBeginningDuration,lstChangeEndDuration)
                
                output = []
                for i in range (len(myresult1)):
                    num1 = int(myresult1[i][1][0:2]) * 60 + int(myresult1[i][1][3:5]) + int(myresult1[0][2])
                    for j in range (len(myresult2)):
                        num2 = int(myresult2[j][1][0:2]) * 60 + int(myresult2[j][1][3:5])
                        if (num2 - num1 <= 30 and num2 - num1 >=15):
                            output.append([myresult1[i][0],start,changeStation,myresult1[i][1],myresult1[i][2],myresult2[j][0],changeStation,end,myresult2[j][1],myresult2[j][2] ])
                return output
            
            if (trainLine == "AreaCentral"):
                for i in range (1, len(fastestRoute)):
                    if len(FCT.getKeyword(start,fastestRoute[i],lstACTrainRoute)) == 0:
                        changeStation = fastestRoute[i-1]
                        break
                lstStartChangeKeyword = FCT.getKeyword(start, changeStation, lstACTrainRoute)
                temp = FCT.getRoute(start, changeStation, lstStartChangeKeyword, lstACTrainRoute)
                lstStartChangeBeginningRoute = temp[0]
                lstStartChangeRoute = temp[1]
                temp = FCT.getDuration(lstStartChangeBeginningRoute,lstStartChangeRoute,lstACDuration)
                lstStartChangeDuration = temp[0]
                lstStartChangeBeginningDuration = temp[1]
                myresult1 = FCT.getMyresult(day,lstStartChangeKeyword,trainLine)
                myresult1 = FCT.updateMyresult(myresult1,lstStartChangeKeyword,lstStartChangeBeginningDuration,lstStartChangeDuration)
                
                lstChangeEndKeyword = FCT.getKeyword(changeStation, end, lstACTrainRoute)
                temp = FCT.getRoute(changeStation, end, lstChangeEndKeyword, lstACTrainRoute)
                lstChangeEndBeginningRoute = temp[0]
                lstChangeEndRoute = temp[1]
                temp = FCT.getDuration(lstChangeEndBeginningRoute,lstChangeEndRoute,lstACDuration)
                lstChangeEndDuration = temp[0]
                lstChangeEndBeginningDuration = temp[1]
                myresult2 = FCT.getMyresult(day,lstChangeEndKeyword,trainLine)
                myresult2 = FCT.updateMyresult(myresult2,lstChangeEndKeyword,lstChangeEndBeginningDuration,lstChangeEndDuration)

                output = []
                for i in range (len(myresult1)):
                    num1 = int(myresult1[i][1][0:2]) * 60 + int(myresult1[i][1][3:5]) + int(myresult1[0][2])
                    for j in range (len(myresult2)):
                        num2 = int(myresult2[j][1][0:2]) * 60 + int(myresult2[j][1][3:5])
                        if (num2 - num1 <= 30 and num2 - num1 >=15):
                            output.append([myresult1[i][0],start,changeStation,myresult1[i][1],myresult1[i][2],myresult2[j][0],changeStation,end,myresult2[j][1],myresult2[j][2] ])
                return output

    else: #Different line
        
        lstIntersectingStations = FCT.getIntersectingStation(startLine,endLine)

        
            
def main():
    list = search("Kraaifontein","Strand","Monday") 

    for line in list:
        print(line)

if __name__ == "__main__":
    main()