line = input("")
output = ""

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


while (line != "done"): #This is a shortcut program that I use to format all my inputs into the time format that I wanted
    output = output + "," + line[:2] + ":" + line[2:]
    line = input("")
print (output[1:])
