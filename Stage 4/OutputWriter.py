line = input("")
output = ""

"""
for i in range(len(line)):
    if line[i] == "1":
        output = output + "," + "Kapteinsklip"
    elif line[i] == "2":
        output = output + "," + "Chris Hani"
    elif line[i] == "3":
        output = output + "," + "Bellville"

print(output[1:])
"""

for i in range(len(line)):
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
