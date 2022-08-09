import PyPDF2

pdfFileObj = open("C:\\Users\\Terrence Shang\\OneDrive - University of Cape Town\\Online Lecture\\CSC3003S\\Capstone Project\\CS-Capestone-Project\\Stage 4\\Area Central.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extract_text())
pdfFileObj.close()
