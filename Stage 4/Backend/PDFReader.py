import PyPDF2
import io

file = open('C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\\\Backend\\trains.txt', 'w')
pdfFileObj = open("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\PDFDoc\\Area North.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#Getting needed information from Area Central PDF to notepad

"""
for i in range (11): #This loop is for Monday to Friday starting from Cape Town
    #Reading the PDF at page i
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extract_text()
    count = 0
    days, departure = "", ""
    platformNumber = trainNumber = departureTime = list = []
    #Getting the important information needed for Notepad
    for line in io.StringIO(pageText):
        if (line.find("MONDAY TO FRIDAY")>=0):
            days = "MF"
        if (line[0:12] == "PLATFORM NO."):
            platformNumber = line[13:].split(" ")
        if (line[0:9] == "TRAIN NO."):
            trainNumber = line[10:].split(" ")
        
        if (2<count<10) and (line[1:10]=="CAPE TOWN"):
            departure = "Cape Town"
            departureTime = line[11:].split(" ")       
        list.append(line)
        count = count + 1
    #Write the important information to the Notepad
    output = (days+",")*(len(trainNumber)-1)
    file.write(output[:-1]+ "\n")
    output = (departure+",")*(len(trainNumber)-1)
    file.write(output[:-1] + "\n")
    file.write(",".join(str(x) for x in departureTime)[:-2]+"\n")
    file.write(",".join(str(x) for x in platformNumber)[:-2]+"\n")
    file.write(",".join(str(x) for x in trainNumber)[:-2]+"\n")
"""

"""
for i in range (11,22): #This loop is for Monday to Friday ending at Cape Town
    
    #Reading the PDF at page i
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extract_text()
    count = 0
    days = ""
    trainNumber = list = []
    #Getting the important information needed for Notepad
    for line in io.StringIO(pageText):
        if (line.find("MONDAY TO FRIDAY")>=0):
            days = "MF"
        if (line.find("TRAIN NO")>=0):
            trainNumber = line[11:].split(" ")   
        list.append(line)
    #Write the important information to the Notepad
    output = (days+",")*(len(trainNumber)-1)
    file.write(output[:-1]+ "\n")
    file.write(",".join(str(x) for x in trainNumber)[:-2]+"\n")
"""

"""
for i in range (22, 29): #This loop is for Saturday starting from Cape Town
    #Reading the PDF at page i
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extract_text()
    count = 0
    days, departure = "", ""
    platformNumber = trainNumber = departureTime = list = []
    #Getting the important information needed for Notepad
    for line in io.StringIO(pageText):
        if (line[0:12] == "PLATFORM NO."):
            platformNumber = line[13:].split(" ")
        if (line[0:9] == "TRAIN NO."):
            trainNumber = line[10:].split(" ")
        
        if (2<count<10) and (line[1:10]=="CAPE TOWN"):
            departure = "Cape Town"
            departureTime = line[11:].split(" ")       
        list.append(line)
        count = count + 1
    #Write the important information to the Notepad
    output = (days+",")*(len(trainNumber)-1)
    file.write(output[:-1]+ "\n")
    output = (departure+",")*(len(trainNumber)-1)
    file.write(output[:-1] + "\n")
    file.write(",".join(str(x) for x in departureTime)[:-2]+"\n")
    file.write(",".join(str(x) for x in platformNumber)[:-2]+"\n")
    file.write(",".join(str(x) for x in trainNumber)[:-2]+"\n")
"""

"""
for i in range (29,36): #This loop is for Monday to Friday ending at Cape Town
    
    #Reading the PDF at page i
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extract_text()
    count = 0
    days = ""
    trainNumber = list = []
    #Getting the important information needed for Notepad
    for line in io.StringIO(pageText):
        if (line.find("TRAIN NO")>=0):
            trainNumber = line[11:].split(" ")   
        list.append(line)
    #Write the important information to the Notepad
    output = ("SAT"+",")*(len(trainNumber)-1)
    file.write(output[:-1]+ "\n")
    file.write(",".join(str(x) for x in trainNumber)[:-2]+"\n")
"""

"""
for i in range (36,41): #This loop is for Saturday starting from Cape Town
    #Reading the PDF at page i
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extract_text()
    count = 0
    days, departure = "SUN", ""
    platformNumber = trainNumber = departureTime = list = []
    #Getting the important information needed for Notepad
    for line in io.StringIO(pageText):
        if (line[0:12] == "PLATFORM NO."):
            platformNumber = line[13:].split(" ")
        if (line[0:9] == "TRAIN NO."):
            trainNumber = line[10:].split(" ")
        
        if (2<count<10) and (line[1:10]=="CAPE TOWN"):
            departure = "Cape Town"
            departureTime = line[11:].split(" ")       
        list.append(line)
        count = count + 1
    #Write the important information to the Notepad
    output = (days+",")*(len(trainNumber)-1)
    file.write(output[:-1]+ "\n")
    output = (departure+",")*(len(trainNumber)-1)
    file.write(output[:-1] + "\n")
    file.write(",".join(str(x) for x in departureTime)[:-2]+"\n")
    file.write(",".join(str(x) for x in platformNumber)[:-2]+"\n")
    file.write(",".join(str(x) for x in trainNumber)[:-2]+"\n")
"""

"""
for i in range (41,46): #This loop is for Monday to Friday ending at Cape Town
    
    #Reading the PDF at page i
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extract_text()
    count = 0
    trainNumber = list = []
    #Getting the important information needed for Notepad
    for line in io.StringIO(pageText):
        if (line.find("TRAIN NO")>=0):
            trainNumber = line[11:].split(" ")   
        list.append(line)
    #Write the important information to the Notepad
    output = ("SUN"+",")*(len(trainNumber)-1)
    file.write(output[:-1]+ "\n")
    file.write(",".join(str(x) for x in trainNumber)[:-2]+"\n")
"""

"""
for i in range (26,): #This loop is to find the information that I need for the departure being Cape Town

    #Reading the PDF at page i
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extract_text()

    count = 0
    days, departure = "", ""
    platformNumber = trainNumber = departureTime = list = []

    #Getting the important information needed for Notepad
    for line in io.StringIO(pageText):
        if (line.find("MONDAYS TO FRIDAYS")>=0):
            days = "MF"
        if (line.find("SATURDAYS")>=0):
            days = "SAT"
        if (line.find("SUNDAYS")>=0):
            days = "SUN"
        if (line[0:12] == "PLATFORM NO."):
            platformNumber = line[13:].split(" ")
        if (line[0:10] == " TRAIN NO."):
            trainNumber = line[11:].split(" ")
        if (2<count<10) and (line[1:10]=="CAPE TOWN"):
            departure = "Cape Town"
            departureTime = line[11:].split(" ")       
            break
        list.append(line)
        count = count + 1

    #Write the important information to the Notepad
    output = (days+",")*(len(trainNumber)-1)
    file.write(output[:-1]+ "\n")
    output = (departure+",")*(len(trainNumber)-1)
    file.write(output[:-1] + "\n")
    file.write(",".join(str(x) for x in departureTime)[:-2]+"\n")
    file.write(",".join(str(x) for x in platformNumber)[:-1]+"\n")
    file.write(",".join(str(x) for x in trainNumber)[:-2]+"\n")
"""


for i in range (23,27): #This loop is to find the information that I need for the destination being Cape Town in the Area Central PDF
    
    #Reading the PDF at page i
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extract_text()

    count = 0
    days = ""
    trainNumber = list = []

    #Getting the important information needed for Notepad
    for line in io.StringIO(pageText):
        print(line)
        if (line.find("MONDAYS TO FRIDAYS")>=0):
            days = "MF"
        if (line.find("SATURDAYS")>=0):
            days = "SAT"
        if (line.find("SUNDAYS")>=0):
            days = "SUNPUB"
        if (line.find("TRAIN NO")>=0):
            trainNumber = line[11:].split(" ")   
            break
        list.append(line)

    #Write the important information to the Notepad
    output = (days+",")*(len(trainNumber)-1)
    file.write(output[:-1]+ "\n")
    file.write(",".join(str(x) for x in trainNumber)[:-2]+"\n")


"""
for i in range (26,33): #This loop is to find the information that I need for the departure being Cape Town

    #Reading the PDF at page i
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extract_text()

    count = 0
    days, departure = "", ""
    platformNumber = trainNumber = departureTime = list = []

    #Getting the important information needed for Notepad
    for line in io.StringIO(pageText):
        if (line.find("MONDAYS TO FRIDAYS")>=0):
            days = "MF"
        if (line.find("SATURDAYS")>=0):
            days = "SAT"
        if (line.find("SUNDAYS")>=0):
            days = "SUN"
        if (line.find("PLATFORM NO.")>=0):
            platformNumber = line.split(" ")
        if (line.find("TRAIN NO.")>=0):
            trainNumber = line.split(" ")
        if (2<count<10) and (line.find("CAPE TOWN")>=0):
            departure = "Cape Town"
            departureTime = line.split(" ")       
            break
        list.append(line)
        count = count + 1

    #Write the important information to the Notepad
    output = (days+",")*(len(trainNumber)-1)
    file.write(output[:-1]+ "\n")
    output = (departure+",")*(len(trainNumber)-1)
    file.write(output[:-1] + "\n")
    file.write(",".join(str(x) for x in departureTime)[:-2]+"\n")
    file.write(",".join(str(x) for x in platformNumber)[:-1]+"\n")
    file.write(",".join(str(x) for x in trainNumber)[:-2]+"\n")
"""

"""
for i in range (27,29): #This loop is to find the information that I need for the departure being Cape Town

    #Reading the PDF at page i
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extract_text()

    count = 0
    days, departure = "", ""
    CTplatformNumber = BelplatformNumber = trainNumber = departureTime = list = []
    checker = False
    #Getting the important information needed for Notepad
    for line in io.StringIO(pageText):
        if (line.find("MONDAYS TO FRIDAYS")>=0):
            days = "MF"
        if (line.find("SATURDAYS")>=0):
            days = "SAT"
        if (line.find("SUNDAYS")>=0):
            days = "SUN"
        if (line[0:12] == "PLATFORM NO."):
            CTplatformNumber = line[13:].split(" ")
            checker = True
        if (line[0:11] == "PLATFORM NO") and (checker == True):
            BelplatformNumber = line[12:].split(" ")
        if (line[0:10] == " TRAIN NO."):
            trainNumber = line[11:].split(" ")
        if (2<count<10) and (line[1:10]=="CAPE TOWN"):
            departure = "Cape Town"
            departureTime = line[11:].split(" ")       
        list.append(line)
        count = count + 1

    #Write the important information to the Notepad
    output = (days+",")*(len(trainNumber)-1)
    file.write(output[:-1]+ "\n")
    output = (departure+",")*(len(trainNumber)-1)
    file.write(output[:-1] + "\n")
    file.write(",".join(str(x) for x in departureTime)[:-2]+"\n")
    file.write(",".join(str(x) for x in CTplatformNumber)[:-1]+"\n")
    file.write(",".join(str(x) for x in BelplatformNumber)[:-1]+"\n")
    file.write(",".join(str(x) for x in trainNumber)[:-2]+"\n")
"""

"""
for i in range (29,31): #This loop is to find the information that I need for the destination being Cape Town in the Area Central PDF
    
    #Reading the PDF at page i
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extract_text()

    count = 0
    days = ""
    trainNumber = list = []

    #Getting the important information needed for Notepad
    for line in io.StringIO(pageText):
        if (line.find("MONDAYS TO FRIDAYS")>=0):
            days = "MF"
        if (line.find("SATURDAYS")>=0):
            days = "SAT"
        if (line.find("SUNDAYS")>=0):
            days = "SUNPUB"
        if (line.find("TRAIN NO")>=0):
            trainNumber = line[11:].split(" ")   
        if (line[0:11] == "PLATFORM NO"):
            CTplatformNumber = line[12:].split(" ")
            break
        list.append(line)

    #Write the important information to the Notepad
    output = (days+",")*(len(trainNumber)-1)
    file.write(output[:-1]+ "\n")
    file.write(",".join(str(x) for x in CTplatformNumber)[:-1]+"\n")
    file.write(",".join(str(x) for x in trainNumber)[:-2]+"\n")
"""
"""
for i in range (31,37): #This loop is to find the information that I need for the departure being Cape Town

    #Reading the PDF at page i
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extract_text()

    count = 0
    days, departure = "", ""
    CTplatformNumber = BelplatformNumber = trainNumber = departureTime = list = []
    checker = False
    #Getting the important information needed for Notepad
    for line in io.StringIO(pageText):
        print(line)
        if (line.find("MONDAYS TO FRIDAYS")>=0):
            days = "MF"
        if (line.find("SATURDAYS")>=0):
            days = "SAT"
        if (line.find("SUNDAYS")>=0):
            days = "SUN"
        if (line[0:12] == "PLATFORM NO."):
            CTplatformNumber = line[13:].split(" ")
        if (line[0:10] == " TRAIN NO."):
            trainNumber = line[11:].split(" ")
        if (2<count<10) and (line[1:10]=="CAPE TOWN"):
            departure = "Cape Town"
            departureTime = line[11:].split(" ")       
            break
        list.append(line)
        count = count + 1

    #Write the important information to the Notepad
    output = (days+",")*(len(trainNumber)-1)
    file.write(output[:-1]+ "\n")
    output = (departure+",")*(len(trainNumber)-1)
    file.write(output[:-1] + "\n")
    file.write(",".join(str(x) for x in departureTime)[:-2]+"\n")
    file.write(",".join(str(x) for x in CTplatformNumber)[:-1]+"\n")
    file.write(",".join(str(x) for x in BelplatformNumber)[:-1]+"\n")
    file.write(",".join(str(x) for x in trainNumber)[:-2]+"\n")
"""

pdfFileObj.close()
file.close