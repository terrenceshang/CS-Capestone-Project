
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
    list = []

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

    file = open ("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\Duration\\Station.txt", "r")
    lstStation = []
    for line in file:
        lstStation.append ((line[:-1].split(",")))
    file.close()


    for i in range (lstStation):
        if (start == lstStation[i][0]):
            startLine = lstStation[i][1]
        elif (end == lstStation[i][0]):
            endLine = lstStation[i][0]


