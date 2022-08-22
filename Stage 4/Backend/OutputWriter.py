
"""
for i in range(len(line)): #This is a shortcut program that I use to make the list of departure stations in the format that I wanted
    if line[i] == "1":
        output = output + "," + "Kapteinsklip"
    elif line[i] == "2":
        output = output + "," + "Chris Hani"
    elif line[i] == "3":
        output = output + "," + "Bellville"

print(output[1:])
"""

"""
for i in range(len(line)): #This is a shortcut program that I use to make the list of arrival stations/Cape Town Platform Number/destination stations in the format that I wanted
    if line[i] == "3":
        output = output + "," + "Kapteinsklip"
    elif line[i] == "2":
        output = output + "," + "Chris Hani"
    elif line[i] == "1":
        output = output + "," + "Bellville"

print(output[1:])
output = ",Cape Town" * len(line)
print(output[1:])
output = ", " * len(line)
print(output[1:])
"""

line = input("")
output = ""
while (line != "done"): #This is a shortcut program that I use to format all my inputs into the time format that I wanted
    output = output + "," + line[:2] + ":" + line[2:]
    line = input("")
print (output[1:])


"""
for i in range(len(line)): #This is a shortcut program that I use to make the list of departure stations in the format that I wanted
    if line[i] == "1":
        output = output + "," + "Plumstead"
    elif line[i] == "2":
        output = output + "," + "Retreat"
    elif line[i] == "3":
        output = output + "," + "Fish Hoek"
    elif line[i] == "4":
        output = output + "," + "Simon's Town"

print(output[1:])
"""

"""
for i in range(len(line)): #This is a shortcut program that I use to make the list of arrival stations/Cape Town Platform Number/destination stations in the format that I wanted
    if line[i] == "1":
        output = output + "," + "Simon's Town"
    elif line[i] == "2":
        output = output + "," + "Fish Hoek"
    elif line[i] == "3":
        output = output + "," + "Retreat"
    elif line[i] == "4":
        output = output + "," + "Plumstead"

print(output[1:])
output = ",Cape Town" * len(line)
print(output[1:])
output = ", " * len(line)
print(output[1:])
"""

"""
for i in range(len(line)): #This is a shortcut program that I use to make the list of departure stations in the format that I wanted
    if line[i] == "1":
        output = output + "," + "Heathfield"
    elif line[i] == "2":
        output = output + "," + "Retreat"

print(output[1:])
"""

"""
line = input("")
for i in range(len(line)): #This is a shortcut program that I use to make the list of arrival stations/Cape Town Platform Number/destination stations in the format that I wanted
    if line[i] == "2":
        output = output + "," + "Heathfield"
    elif line[i] == "1":
        output = output + "," + "Retreat"

print(output[1:])
output = ",Cape Town" * len(line)
print(output[1:])
output = ", " * len(line)
print(output[1:])
"""

"""
line = input("")
line2 = input("")
line3 = input("")
line4 = input("")
print(("SUN," * int(line))[:-1])
print(("Bellville," * int(line))[:-1])
print(("Cape Town," * int(line))[:-1])
print(line2.replace(" ", ","))
print(line3.replace(" ", ","))
print(line4.replace(" ", ","))
"""
"""
line = input("")
output = ""
for i in range(len(line)): #This is a shortcut program that I use to make the list of departure stations in the format that I wanted
    if line[i] == "1":
        output = output + "," + "Bellville D"
    if line[i] == "2":
        output = output + "," + "Bellville A"
    if line[i] == "3":
        output = output + "," + "Eerste River A"
    if line[i] == "4":
        output = output + "," + "Eerste River D"
    if line[i] == "5":
        output = output + "," + "Strand"
    if line[i] == "6":
        output = output + "," + "Muldersvlei"
    if line[i] == "7":
        output = output + "," + "Kraaifontein"
    if line[i] == "8":
        output = output + "," + "Wellington"
    if line[i] == "9":
        output = output + "," + "Kuils River"
 #   if line[i] == "9":
  #      output = output + "," + "Malmesbury"
    if line[i] == "0":
        output = output + "," + "Worcester"
print(output[1:])
"""

"""
line = input("")
output = ""
for i in range(len(line)): #This is a shortcut program that I use to make the list of departure stations in the format that I wanted
    if line[i] == "7":
        output = output + "," + "Bellville D"
    if line[i] == "6":
        output = output + "," + "Bellville A"
    if line[i] == "5":
        output = output + "," + "Eerste River"
    if line[i] == "4":
        output = output + "," + "Strand"
    if line[i] == "3":
        output = output + "," + "Muldersvlei"
    if line[i] == "2":
        output = output + "," + "Kraaifontein"
    if line[i] == "1":
        output = output + "," + "Wellington"
    if line[i] == "8":
        output = output + "," + "Kuils River"
    if line[i] == "9":
        output = output + "," + "Malmesbury"
    if line[i] == "0":
        output = output + "," + "Worcester"
tempLine = line
tempOutput = output
output = ""
line = input("")
if len(tempLine) == len(line):
    for i in range(len(line)): 
        if line[i] == "1":
            output = output + "," + "Cape Town"
        if line[i] == "2":
            output = output + "," + "Bellville A"
        if line[i] == "3":
            output = output + "," + "Bellville D"
        if line[i] == "4":
            output = output + "," + "Parow"
else:
    print("Don't Match")
print(tempOutput[1:])
print(output[1:])
output = ", " * len(line)
print(output)
"""