
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

"""
while (line != "done"): #This is a shortcut program that I use to format all my inputs into the time format that I wanted
    output = output + "," + line[:2] + ":" + line[2:]
    line = input("")
print (output[1:])
"""

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