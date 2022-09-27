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
import ShortestRoute as sr
import time

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
            for i in range (len(myresult)):
                myresult[i] = list(myresult[i])

#Changing the start time from beginning station of the route to the start location
#Changing the myresult from <Train number><Unique key><Duration> to <Train number><Start time><Duration>
            myresult = FCT.updateMyresult(myresult,tempList,lstDuration,lstDurationBeginning)
            output = []
                
            for i in range (len(myresult)):
                
                output.append([myresult[i][0],start,end,myresult[i][1],myresult[i][2]])
            return output
        
        else: #Same line, 2 trains
            fastestRoute = dk.findRoute(start,end)
            changeStation = ""
            
            if (trainLine == "AreaNorth"):
                for i in range (1, len(fastestRoute)):
                    if len(FCT.getKeyword(start,fastestRoute[i],lstANTrainRoute)) == 0:
                        changeStation = fastestRoute[i-1]
                        break
                #This is a function used to calculate the trains a person must take when given all the needed information
                output = sr.calc(start,end,day,changeStation,trainLine,trainLine,lstANTrainRoute,lstANTrainRoute,lstANDuration,lstANDuration)
                return output
            
            if (trainLine == "AreaSouth"):
                for i in range (1, len(fastestRoute)):
                    if len(FCT.getKeyword(start,fastestRoute[i],lstASTrainRoute)) == 0:
                        changeStation = fastestRoute[i-1]
                        break
                output = sr.calc(start,end,day,changeStation,trainLine,trainLine,lstANTrainRoute,lstANTrainRoute,lstANDuration,lstANDuration)
                return output
            
            if (trainLine == "AreaCentral"):
                for i in range (1, len(fastestRoute)):
                    if len(FCT.getKeyword(start,fastestRoute[i],lstACTrainRoute)) == 0:
                        changeStation = fastestRoute[i-1]
                        break
                output = sr.calc(start,end,day,changeStation,trainLine,trainLine,lstANTrainRoute,lstANTrainRoute,lstANDuration,lstANDuration)
                return output

    else: # 2 locations are situated in different areas
        if trainLine == "SN":
            changeStation = "Cape Town"
            
            output = sr.calc(start,end,day,changeStation,"AreaSouth","AreaNorth",lstASTrainRoute,lstANTrainRoute,lstASDuration,lstANDuration)
            return output

        if trainLine == "NS":
            changeStation = "Cape Town"
            output = sr.calc(start,end,day,changeStation,"AreaNorth","AreaSouth",lstANTrainRoute,lstASTrainRoute,lstANDuration,lstASDuration)
            return output
            
        if trainLine == "CS":
            changeStation = "Cape Town"
            output = sr.calc(start,end,day,changeStation,"AreaCentral","AreaSouth",lstACTrainRoute,lstASTrainRoute,lstACDuration,lstASDuration)
            return output

        if trainLine == "SC":
            changeStation = "Cape Town"
            output = sr.calc(start,end,day,changeStation,"AreaSouth","AreaCentral",lstASTrainRoute,lstACTrainRoute,lstASDuration,lstACDuration)
            return output

        if trainLine == "NC":
            changeStation = "Bellville"
            output = sr.calc(start,end,day,changeStation,"AreaNorth","AreaCentral",lstANTrainRoute,lstACTrainRoute,lstANDuration,lstACDuration)
            return output

        if trainLine == "CN":
            changeStation = "Bellville"
            output = sr.calc(start,end,day,changeStation,"AreaCentral","AreaNorth",lstACTrainRoute,lstANTrainRoute,lstACDuration,lstANDuration)
            return output
          
def main():
    start_time = time.time()
    list = search("Avondale","Cape Town", "Monday")    
    print("--- %s seconds ---" % (time.time() - start_time))
    tme = '14:00'
    output = FCT.outputPaths(list,tme)
    for line in output:
        print(line) 

if __name__ == "__main__":
    main()