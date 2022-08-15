import PyPDF2
import io

file = open('C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\trains.txt', 'w')
pdfFileObj = open("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\PDFDoc\\Area Central.pdf", "rb")
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

pdfFileObj.close()
file.close