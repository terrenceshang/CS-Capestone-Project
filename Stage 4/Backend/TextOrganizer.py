"""
file = open ("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\forReading\\Area North Train Route.txt","r")
list = []
for line in file:
    list.append (line)
    list.sort()
file.close()

file = open ("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\forReading\\Area North Train Route.txt","r")
for line in file:
    if line not in list:
        print (line)
file.close()

file = open ("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\Temp.txt", "w")
for line in list:
    file.writelines(line)
file.close()
"""

file = open ("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\Area Central Train Route.txt", "r")
lstRoute = []
for line in file:
    lstRoute.append (line[:-1].split(","))
file.close()

file = open ("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\Area Central Duration.txt", "r")
lstDuration = []
for line in file:
    lstDuration.append (line[:-1].split(","))
file.close()

file = open  ("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Backend\\Temp.txt", "w")
lstOutput = []
for list in lstRoute:
    output = ""
    for i in range (len(list)-1):
        output = output + list[i] 
        for j in range (len(lstDuration)):
            checker = False
            if lstDuration[j][0] == list[i] and lstDuration[j][1] == list[i+1]:
                output = output + "-" + lstDuration[j][2] + "-"
                checker = True
                break
        if checker == False:
            output = output + ","
    output = output + list[i+1] + "\n"
    file.writelines(output)

print(lstDuration[1])


