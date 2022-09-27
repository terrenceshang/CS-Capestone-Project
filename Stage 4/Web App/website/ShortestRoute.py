from website.Functions import Functions
FCT = Functions()

class ShortestRoute():
    def calc(self,start,end,day,changeStation,trainLine1,trainLine2,lstLine1,lstLine2,lstDuration1,lstDuration2):
                
        lstStartChangeKeyword = FCT.getKeyword(start, changeStation, lstLine1) #Getting a list of the keywords between two stations, keywords are unique identifier for different route routes
        lstChangeEndKeyword = FCT.getKeyword(changeStation, end, lstLine2)
        
        #Checking if the route with the change station is feasible, if not feasible then a different change station will be used
        if len(lstStartChangeKeyword) == 0 or len(lstChangeEndKeyword) == 0:
            lstStartChangeKeyword = FCT.getKeyword(start, "Bellville", lstLine1)
            lstChangeEndKeyword = FCT.getKeyword("Bellville", end, lstLine2)
            if len(lstStartChangeKeyword) == 0 or len(lstChangeEndKeyword) == 0: #Checking if the route is feasible
                lstStartChangeKeyword = FCT.getKeyword(start, "Mutual", lstLine1)
                lstChangeEndKeyword = FCT.getKeyword("Mutual", end, lstLine2)
                if len(lstStartChangeKeyword) == 0 or len(lstChangeEndKeyword) == 0:
                    return self.calc(start,end,day,"Cape Town",trainLine1,trainLine2,lstLine1,lstLine2,lstDuration1,lstDuration2)
                else: 
                    return self.calc(start,end,day,"Mutual",trainLine1,trainLine2,lstLine1,lstLine2,lstDuration1,lstDuration2)
            else:
                return self.calc(start,end,day,"Bellville",trainLine1,trainLine2,lstLine1,lstLine2,lstDuration1,lstDuration2)
        
        temp = FCT.getRoute(start, changeStation, lstStartChangeKeyword, lstLine1) # Getting the route from the start to change station and change station to end
        lstStartChangeBeginningRoute = temp[0]
        lstStartChangeRoute = temp[1]
        temp = FCT.getDuration(lstStartChangeBeginningRoute,lstStartChangeRoute,lstDuration1) #Geting the duration from the start to change station and change station to end
        lstStartChangeDuration = temp[0]
        lstStartChangeBeginningDuration = temp[1]
        myresult1 = FCT.getMyresult(day,lstStartChangeKeyword,trainLine1) #Getting the needed information from database
        for i in range (len(myresult1)):
            myresult1[i] = list(myresult1[i])
        myresult1 = FCT.updateMyresult(myresult1,lstStartChangeKeyword,lstStartChangeBeginningDuration,lstStartChangeDuration) #changing the information to output
            
        temp = FCT.getRoute(changeStation, end, lstChangeEndKeyword, lstLine2)
        lstChangeEndBeginningRoute = temp[0]
        lstChangeEndRoute = temp[1]
        temp = FCT.getDuration(lstChangeEndBeginningRoute,lstChangeEndRoute,lstDuration2)
        lstChangeEndDuration = temp[0]
        lstChangeEndBeginningDuration = temp[1]
        myresult2 = FCT.getMyresult(day,lstChangeEndKeyword,trainLine2)
        for i in range (len(myresult2)):
            myresult2[i] = list(myresult2[i])
        myresult2 = FCT.updateMyresult(myresult2,lstChangeEndKeyword,lstChangeEndBeginningDuration,lstChangeEndDuration)
        
    #Combining the information from myresult1 and myresult2 and make the final edit to the informations
        output = []
        for i in range (len(myresult1)):
            num1 = int(myresult1[i][1][0:2]) * 60 + int(myresult1[i][1][3:5]) + int(myresult1[0][2])
            for j in range (len(myresult2)):
                num2 = int(myresult2[j][1][0:2]) * 60 + int(myresult2[j][1][3:5])
                if (num2 - num1 <= 30 and num2 - num1 >=15):
                    output.append([myresult1[i][0],start,changeStation,myresult1[i][1],myresult1[i][2],myresult2[j][0],changeStation,end,myresult2[j][1],myresult2[j][2] ])
                if len(output) == 0:
                    if (num2 - num1 >= 15 and num2 - num1 <=60):
                        output.append([myresult1[i][0],start,changeStation,myresult1[i][1],myresult1[i][2],myresult2[j][0],changeStation,end,myresult2[j][1],myresult2[j][2]])
                if len(output) == 0:
                    if (num2 - num1 >= 15 and num2 - num1 <=120):
                        output.append([myresult1[i][0],start,changeStation,myresult1[i][1],myresult1[i][2],myresult2[j][0],changeStation,end,myresult2[j][1],myresult2[j][2]])
                
        if len(output) == 0:
            return self.calc(start,end,day,"Cape Town",trainLine1,trainLine2,lstLine1,lstLine2,lstDuration1,lstDuration2)
        return output