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
import Functions as FCT

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
        lstIntersectingStations = FCT.getIntersectingStation(startLine,endLine)
        
        return (lstIntersectingStations)

def main():
    list = search("Cape Town","Stikland","Monday") 

    for line in list:
        print(line)

if __name__ == "__main__":
    main()