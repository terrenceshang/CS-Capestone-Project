import Functions as FCT

def calc(start,end,day,changeStation,trainLine1,trainLine2,lstLine1,lstLine2,lstDuration1,lstDuration2):
            
    lstStartChangeKeyword = FCT.getKeyword(start, changeStation, lstLine1)
    temp = FCT.getRoute(start, changeStation, lstStartChangeKeyword, lstLine1)
    lstStartChangeBeginningRoute = temp[0]
    lstStartChangeRoute = temp[1]
    temp = FCT.getDuration(lstStartChangeBeginningRoute,lstStartChangeRoute,lstDuration1)
    lstStartChangeDuration = temp[0]
    lstStartChangeBeginningDuration = temp[1]
    myresult1 = FCT.getMyresult(day,lstStartChangeKeyword,trainLine1)
    myresult1 = FCT.updateMyresult(myresult1,lstStartChangeKeyword,lstStartChangeBeginningDuration,lstStartChangeDuration)
                
    lstChangeEndKeyword = FCT.getKeyword(changeStation, end, lstLine2)
    temp = FCT.getRoute(changeStation, end, lstChangeEndKeyword, lstLine2)
    lstChangeEndBeginningRoute = temp[0]
    lstChangeEndRoute = temp[1]
    temp = FCT.getDuration(lstChangeEndBeginningRoute,lstChangeEndRoute,lstDuration2)
    lstChangeEndDuration = temp[0]
    lstChangeEndBeginningDuration = temp[1]
    myresult2 = FCT.getMyresult(day,lstChangeEndKeyword,trainLine2)
    myresult2 = FCT.updateMyresult(myresult2,lstChangeEndKeyword,lstChangeEndBeginningDuration,lstChangeEndDuration)

    output = []
    for i in range (len(myresult1)):
        num1 = int(myresult1[i][1][0:2]) * 60 + int(myresult1[i][1][3:5]) + int(myresult1[0][2])
        for j in range (len(myresult2)):
            num2 = int(myresult2[j][1][0:2]) * 60 + int(myresult2[j][1][3:5])
            if (num2 - num1 <= 30 and num2 - num1 >=15):
                output.append([myresult1[i][0],start,changeStation,myresult1[i][1],myresult1[i][2],myresult2[j][0],changeStation,end,myresult2[j][1],myresult2[j][2] ])
    return output