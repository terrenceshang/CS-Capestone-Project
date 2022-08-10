import PyPDF2
import io

pdfFileObj = open("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Area Central.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

#print(pdfReader.numPages) reading number of pages
pageObj = pdfReader.getPage(0)
pageText = pageObj.extract_text()

count = 0
list = []

print (pageText)
#Remove the last lines if it is "FROM MUTUAL"
"""
for line in io.StringIO(pageText):
    if (line[0] == "R"):
        list[count-1] = list[count-1][0:len(list[count-1])-2]
        break
    list.append(line)
    count = count + 1

count = 0
for line in list:
    print(str(count) + line)
    count += 1
pdfFileObj.close()
"""